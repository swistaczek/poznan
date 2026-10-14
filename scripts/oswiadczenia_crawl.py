#!/usr/bin/env python3
"""Indeks linkow do jawnych oswiadczen majatkowych w BIP Miasta Poznania.

Zbiera TYLKO metadane i linki (kto, funkcja, jednostka, rok, rodzaj, URL PDF,
URL strony BIP). Nie pobiera i nie zapisuje tresci oswiadczen (PDF).

Sekcje BIP (bip.poznan.pl):
  wydzialy           /bip/oswiadczenia-majatkowe-wydzialy/            (biura i wydzialy UMP)
  mjo                /bip/oswiadczenia-majatkowe-mjo/                 (miejskie jednostki organizacyjne)
  prezydent          /bip/prezydent-i-zastepcy/ (+ kadencje)          (prezydent, zastepcy, sekretarz, skarbnik)
  radni              /bip/radni/ (+ kadencje)                         (radni Rady Miasta Poznania)
  archiwum-wydzialy  /bip/archiwum-oswiadczenia-majatkowe-wydzialy/
  archiwum-osoby     /bip/archiwum-oswiadczenia-majatkowe-osoby/

Tylko biblioteka standardowa Pythona 3. Przyklady:
  python3 scripts/oswiadczenia_crawl.py
  python3 scripts/oswiadczenia_crawl.py --sekcja wydzialy --limit 2 --out /tmp/test.csv
  python3 scripts/oswiadczenia_crawl.py --sekcja radni,prezydent --cache /tmp/osw_cache

Zrodlo danych: Biuletyn Informacji Publicznej Miasta Poznania, https://bip.poznan.pl/
(art. 23b ust. 2 udip: w CSV kazdy wiersz ma url_strony i data_pobrania).
"""

import argparse
import csv
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

BASE = "https://bip.poznan.pl"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0 Safari/537.36 (civic-index; oswiadczenia-majatkowe)")

SEKCJE = ["prezydent", "radni", "wydzialy", "mjo", "archiwum-wydzialy", "archiwum-osoby"]

CSV_FIELDS = [
    "imie_nazwisko", "nazwisko_norm", "funkcja", "jednostka", "sekcja_bip", "rok",
    "rodzaj", "url_pdf", "url_strony", "data_pobrania",
    # kolumny dodatkowe (na koncu, nie psuja konsumentow pierwszych 10 kolumn)
    "tytul", "url_pdf_dostepny",
]

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUT = os.path.join(REPO_ROOT, "research", "transparentnosc", "oswiadczenia-majatkowe",
                           "dane", "oswiadczenia.csv")


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------- normalizacja

def strip_pl(s):
    s = s.replace("ł", "l").replace("Ł", "L")
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def norm(s):
    s = strip_pl(s or "").lower()
    s = re.sub(r"[^a-z0-9\- ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def clean_ws(s):
    return re.sub(r"\s+", " ", html.unescape(s or "")).strip()


# --------------------------------------------------------------------------- HTTP z cache

class BlockedError(RuntimeError):
    pass


class Fetcher:
    def __init__(self, cache_dir, delay=0.6, timeout=30, retries=3, refresh=False):
        self.cache_dir = cache_dir
        self.delay = delay
        self.timeout = timeout
        self.retries = retries
        self.refresh = refresh
        self.last = 0.0
        self.n_net = 0
        self.n_cache = 0
        self.consecutive_blocks = 0
        os.makedirs(cache_dir, exist_ok=True)

    def _paths(self, url):
        h = hashlib.sha1(url.encode("utf-8")).hexdigest()
        return (os.path.join(self.cache_dir, h + ".body"),
                os.path.join(self.cache_dir, h + ".meta.json"))

    def get(self, url):
        """Zwraca (tekst, data_pobrania YYYY-MM-DD). Cache na dysku."""
        body_p, meta_p = self._paths(url)
        if not self.refresh and os.path.exists(body_p) and os.path.exists(meta_p):
            with open(meta_p, encoding="utf-8") as f:
                meta = json.load(f)
            with open(body_p, "rb") as f:
                data = f.read()
            self.n_cache += 1
            return data.decode("utf-8", errors="replace"), meta.get("fetched", "")[:10]

        err = None
        for attempt in range(1, self.retries + 1):
            wait = self.delay - (time.time() - self.last)
            if wait > 0:
                time.sleep(wait)
            self.last = time.time()
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/json;q=0.9,*/*;q=0.8",
                "Accept-Language": "pl,en;q=0.5",
            })
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    ctype = r.headers.get("Content-Type", "")
                    if "pdf" in ctype.lower():
                        raise RuntimeError("nieoczekiwany PDF pod %s - nie pobieram tresci" % url)
                    data = r.read()
                    status = r.status
                self.n_net += 1
                text = data.decode("utf-8", errors="replace")
                low = text[:5000].lower()
                if "captcha" in low or "recaptcha" in low:
                    raise BlockedError("CAPTCHA pod %s - przerywam (nie obchodze zabezpieczen)" % url)
                self.consecutive_blocks = 0
                fetched = dt.datetime.now().isoformat(timespec="seconds")
                with open(body_p, "wb") as f:
                    f.write(data)
                with open(meta_p, "w", encoding="utf-8") as f:
                    json.dump({"url": url, "fetched": fetched, "status": status,
                               "content_type": ctype}, f)
                return text, fetched[:10]
            except urllib.error.HTTPError as e:
                err = e
                if e.code in (403, 429):
                    self.consecutive_blocks += 1
                    if self.consecutive_blocks >= 5:
                        raise BlockedError("seryjne HTTP %s (ostatnio %s) - przerywam" % (e.code, url))
                    time.sleep(5 * attempt)
                    continue
                if e.code == 404:
                    break
                time.sleep(2 * attempt)
            except BlockedError:
                raise
            except Exception as e:  # timeout, reset itp.
                err = e
                time.sleep(2 * attempt)
        raise RuntimeError("blad pobierania %s: %s" % (url, err))


# --------------------------------------------------------------------------- mini-DOM

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "source", "track", "wbr"}


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = []
        self.parent = parent

    def text(self):
        out = []
        for c in self.children:
            out.append(c if isinstance(c, str) else c.text())
        return "".join(out)

    def iter(self):
        yield self
        for c in self.children:
            if isinstance(c, Node):
                yield from c.iter()

    def find_all(self, tag):
        return [n for n in self.iter() if n.tag == tag]

    def child_nodes(self, tag=None):
        return [c for c in self.children if isinstance(c, Node) and (tag is None or c.tag == tag)]


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, dict(attrs), self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, dict(attrs), self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def parse_html(text):
    tb = TreeBuilder()
    tb.feed(text)
    tb.close()
    return tb.root


def main_article(root):
    for n in root.iter():
        if n.tag == "article":
            return n
    for n in root.iter():
        if n.attrs.get("role") == "main":
            return n
    return root


def page_heading(article):
    for h in article.find_all("h3"):
        t = clean_ws(h.text())
        if t:
            return t
    return ""


LZ_RE = re.compile(r"zalaczniki\.html\?co=show&(?:amp;)?lz_id=(\d+)")


def pdf_url(lz_id):
    return "%s/public/bip/zalaczniki.html?co=show&lz_id=%s" % (BASE, lz_id)


FUNC_WORDS = ("dyrektor", "naczelnik", "kierownik", "specjalista", "zastepca", "z-ca", "inspektor",
              "p.o.", "p. o.", "prezes", "komendant", "sekretarz", "skarbnik", "glowny", "starszy",
              "referent", "podinspektor", "ksiegow", "radca", "koordynator", "wicedyrektor",
              "pelnomocnik", "konserwator", "inzynier", "kierowniczka", "dyrektorka", "zastepczyni",
              "naczelniczka", "pracownik", "stanowisko", "ds.", "audytor", "geodeta", "architekt",
              "rzecznik", "lekarz", "przewodnicz")


def looks_like_function(s):
    n = strip_pl(s).lower()
    return any(w in n for w in FUNC_WORDS)


def split_person(span_text):
    """'Dyrektor\\nJan Kowalski' -> ('Jan Kowalski', 'Dyrektor')."""
    lines = [clean_ws(l) for l in span_text.split("\n")]
    lines = [l for l in lines if l]
    if not lines:
        return "", ""
    if len(lines) == 1:
        one = lines[0]
        m = re.match(r"^(.*?)\s+[-–]\s+(.*)$", one)
        if m:
            a, b = m.group(1), m.group(2)
            if looks_like_function(b) and not looks_like_function(a):
                return a, b
            if looks_like_function(a) and not looks_like_function(b):
                return b, a
        return one, ""
    name, func = lines[-1], " ".join(lines[:-1])
    if looks_like_function(name) and not looks_like_function(lines[0]):
        name, func = lines[0], " ".join(lines[1:])
    return name, func


def extract_items(article):
    """Zwraca liste dict: person_span, title, lz_id, url_dostepny, h3.

    Pozycja = <li>, ktorego bezposrednie dzieci <div> zawieraja link zalaczniki.html?co=show&lz_id=.
    Osoba = tekst <span> w najblizszym nadrzednym <li> (strony wydzialow/MJO/archiwow).
    Naglowek = najblizszy poprzedzajacy <h3> (filtr: musi dotyczyc oswiadczen).
    """
    items = []
    last_h3 = [""]

    def walk(n):
        for c in n.children:
            if not isinstance(c, Node):
                continue
            if c.tag == "h3":
                last_h3[0] = clean_ws(c.text())
                continue
            if c.tag == "li":
                divs = c.child_nodes("div")
                lz = None
                acc = ""
                for d in divs:
                    for a in d.find_all("a"):
                        href = a.attrs.get("href", "")
                        m = LZ_RE.search(href)
                        if m and lz is None:
                            lz = m.group(1)
                        elif "aidapta/zalaczniki.html" in href and not acc:
                            acc = urllib.parse.urljoin(BASE, html.unescape(href))
                if lz:
                    title = ""
                    for d in divs:
                        if not d.find_all("a"):
                            title = clean_ws(d.text())
                            if title:
                                break
                    person = ""
                    p = c.parent
                    while p is not None:
                        if p.tag == "li":
                            sp = p.child_nodes("span")
                            if sp:
                                person = sp[0].text()
                                break
                        p = p.parent
                    items.append({"person_span": person, "title": title, "lz_id": lz,
                                  "url_dostepny": acc, "h3": last_h3[0]})
                    continue
            walk(c)

    walk(article)
    out = []
    for it in items:
        ctx = strip_pl(it["h3"] + " " + it["title"]).lower()
        if "oswiadcz" in ctx or "majatk" in ctx:
            out.append(it)
        else:
            log("  [pomijam zalacznik spoza sekcji oswiadczen] h3=%r tytul=%r" % (it["h3"], it["title"]))
    return out


# --------------------------------------------------------------------------- klasyfikacja

YEAR_RE = re.compile(r"(?<!\d)(19[9]\d|20[0-4]\d)(?!\d)")


def classify(title):
    t = strip_pl(title).lower()
    m = YEAR_RE.search(t)
    rok = m.group(1) if m else ""
    if "korekt" in t or "korygując" in title.lower() or "korygujac" in t:
        rodzaj = "korekta"
    elif re.search(r"pierwsz|rozpocz|powolan|objec|poczatek|poczatku|zatrudnien|nawiazan|na start|"
                   r"nadani[ae] upowaznien|powierzeni|poczatkow|nowo wybran|nowo powolan", t):
        rodzaj = "na rozpoczęcie"
    elif re.search(r"ostatni|oststni|koncow|zakoncz|odwolan|rezygnac|rozwiazan|koniec|konca|ustani|"
                   r"przed uplywem|wygasn|odejsci|zwolnien|wypowiedz|przejsci|cofniec|ustepujac", t):
        rodzaj = "na zakończenie"
    elif re.search(r"(?<![a-z])za\s*(rok\s*)?(19|20)\d\d|roczn|31\s*(grudnia|12)|stan na", t) or \
            (rok and not re.search(r"wyjasnien|uzupelnien", t)):
        # tytul z samym rokiem (np. "oswiadczenie majatkowe_2021_XX") traktujemy jako roczne
        rodzaj = "roczne"
    else:
        rodzaj = "inne/nieokreślone"
    return rok, rodzaj


# --------------------------------------------------------------------------- sekcje

def abs_url(href):
    return urllib.parse.urljoin(BASE + "/", html.unescape(href))


def list_units(fetcher, index_url, pattern):
    text, _ = fetcher.get(index_url)
    art = main_article(parse_html(text))
    units = []
    seen = set()
    for a in art.find_all("a"):
        href = a.attrs.get("href", "")
        if re.search(pattern, href):
            u = abs_url(href)
            if u in seen:
                continue
            seen.add(u)
            units.append((u, clean_ws(a.text())))
    return units


def unit_name_from_heading(heading, fallback):
    # "Oświadczenia majątkowe wg wydziałów - Biuro Miejskiego Inżyniera Ruchu"
    # "Oświadczenia majątkowe wg wydziałów - archiwum - Biuro Nadzoru Właścicielskiego"
    parts = [p.strip() for p in re.split(r"\s+-\s+", heading)]
    parts = [p for p in parts if p and not p.lower().startswith("oświadczenia majątkowe")
             and p.lower() != "archiwum"]
    if parts:
        return " - ".join(parts)
    return fallback


def rows_from_page(text, fetched, url, sekcja, jednostka, default_name="", default_func=""):
    art = main_article(parse_html(text))
    rows = []
    for it in extract_items(art):
        if it["person_span"]:
            name, func = split_person(it["person_span"])
        else:
            name, func = default_name, default_func
        if not func:
            func = default_func
        rok, rodzaj = classify(it["title"])
        rows.append({
            "imie_nazwisko": name,
            "nazwisko_norm": norm(name),
            "funkcja": func,
            "jednostka": jednostka,
            "sekcja_bip": sekcja,
            "rok": rok,
            "rodzaj": rodzaj,
            "url_pdf": pdf_url(it["lz_id"]),
            "url_strony": url,
            "data_pobrania": fetched,
            "tytul": it["title"],
            "url_pdf_dostepny": it["url_dostepny"],
            "_lz": it["lz_id"],
        })
    return rows


def crawl_units(fetcher, sekcja, index_url, pattern, limit, stats):
    units = list_units(fetcher, index_url, pattern)
    log("[%s] jednostek na liscie: %d" % (sekcja, len(units)))
    stats.setdefault("jednostki", {})[sekcja] = len(units)
    if limit:
        units = units[:limit]
    rows = []
    for i, (u, label) in enumerate(units, 1):
        try:
            text, fetched = fetcher.get(u)
        except BlockedError:
            raise
        except Exception as e:
            log("  BLAD %s: %s" % (u, e))
            stats.setdefault("bledy", []).append(u)
            continue
        art = main_article(parse_html(text))
        jedn = unit_name_from_heading(page_heading(art), label.title())
        r = rows_from_page(text, fetched, u, sekcja, jedn)
        if not r:
            stats.setdefault("puste", []).append((sekcja, jedn, u))
        rows.extend(r)
        if i % 25 == 0:
            log("  [%s] %d/%d stron, %d pozycji" % (sekcja, i, len(units), len(rows)))
    log("[%s] pozycji: %d" % (sekcja, len(rows)))
    return rows


def kadencje(fetcher, index_url, prefix):
    """Zwraca liste (url_listy, etykieta_kadencji) - aktualna + archiwalne."""
    text, _ = fetcher.get(index_url)
    art_all = parse_html(text)
    out = []
    cur_label = ""
    h = page_heading(main_article(art_all))
    m = re.search(r"kadencja\s+(\d{4}-\d{4})", h)
    if m:
        cur_label = m.group(1)
    out.append((index_url, cur_label))
    seen = {index_url}
    for a in art_all.find_all("a"):
        href = a.attrs.get("href", "")
        m = re.match(r"^/bip/%s/kadencja-(\d{4}-\d{4}),\d+/$" % re.escape(prefix), href)
        if m:
            u = abs_url(href)
            if u not in seen:
                seen.add(u)
                out.append((u, m.group(1)))
    return out


def crawl_prezydent(fetcher, limit, stats):
    rows = []
    kad = kadencje(fetcher, BASE + "/bip/prezydent-i-zastepcy/", "prezydent-i-zastepcy")
    stats.setdefault("jednostki", {})["prezydent"] = len(kad)
    n_os = 0
    for list_url, label in kad:
        # JSON API: imie / nazwisko / funkcja po id
        api_url = list_url.replace("/bip/", "/api-json/bip/", 1)
        meta = {}
        try:
            jtext, _ = fetcher.get(api_url)
            for o in _walk_dicts(json.loads(jtext)):
                if "imie" in o and "id" in o:
                    meta[str(o["id"])] = o
        except Exception as e:
            log("  [prezydent] brak JSON %s: %s" % (api_url, e))
        text, _ = fetcher.get(list_url)
        art = main_article(parse_html(text))
        persons = []
        seen = set()
        for a in art.find_all("a"):
            href = a.attrs.get("href", "")
            m = re.match(r"^/bip/prezydent-i-zastepcy/(?:kadencja-\d{4}-\d{4},\d+/)?(?!kadencja-)[^/,]+,(\d+)/$",
                         href)
            if not m:
                continue
            pid = m.group(1)
            if pid in seen or not clean_ws(a.text()):
                continue
            seen.add(pid)
            persons.append((abs_url(href), pid, clean_ws(a.text())))
        if limit:
            persons = persons[:limit]
        for u, pid, label_txt in persons:
            o = meta.get(pid)
            if o:
                name = clean_ws("%s %s" % (o.get("imie", ""), o.get("nazwisko", "")))
                func = clean_ws(o.get("funkcja", ""))
            else:
                name, func = label_txt, ""
            if label:
                func = (func + ", kadencja " + label).strip(", ")
            try:
                ptext, fetched = fetcher.get(u)
            except BlockedError:
                raise
            except Exception as e:
                log("  BLAD %s: %s" % (u, e))
                stats.setdefault("bledy", []).append(u)
                continue
            n_os += 1
            r = rows_from_page(ptext, fetched, u, "prezydent-i-zastepcy", "Urząd Miasta Poznania",
                               default_name=name, default_func=func)
            for x in r:
                x["imie_nazwisko"], x["nazwisko_norm"], x["funkcja"] = name, norm(name), func
            rows.extend(r)
    stats.setdefault("strony_osob", {})["prezydent"] = n_os
    log("[prezydent] osob (stron): %d, pozycji: %d" % (n_os, len(rows)))
    return rows


def _walk_dicts(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from _walk_dicts(v)
    elif isinstance(o, list):
        for v in o:
            yield from _walk_dicts(v)


MANDAT_RE = re.compile(r"\s*[-–,(]?\s*(wygaśnięcie|wygasniecie|wygaśnięciem|mandat wygasł|złożenie mandatu)\b.*$",
                       re.I)


def crawl_radni(fetcher, limit, stats):
    rows = []
    kad = kadencje(fetcher, BASE + "/bip/radni/", "radni")
    stats.setdefault("jednostki", {})["radni"] = len(kad)
    n_os = 0
    for list_url, label in kad:
        text, _ = fetcher.get(list_url)
        art = main_article(parse_html(text))
        persons = []
        seen = set()
        for a in art.find_all("a"):
            href = a.attrs.get("href", "")
            m = re.match(r"^/bip/radni/(?:kadencja-[^/]+,\d+/)?([^/,]+),(\d+)/$", href)
            if not m or m.group(1).startswith("kadencja-"):
                continue
            pid = m.group(2)
            txt = clean_ws(a.text())
            if pid in seen or not txt:
                continue
            seen.add(pid)
            persons.append((abs_url(href), pid, txt))
        if limit:
            persons = persons[:limit]
        log("[radni] kadencja %s: %d radnych" % (label or "?", len(persons)))
        for u, pid, txt in persons:
            note = ""
            mm = MANDAT_RE.search(txt)
            name = txt
            if mm:
                name = txt[:mm.start()].strip(" -–,(")
                note = txt[mm.start():].strip(" -–,()")
            func = "Radny Rady Miasta Poznania" + (", kadencja " + label if label else "")
            if note:
                func += " (" + note + ")"
            try:
                ptext, fetched = fetcher.get(u)
            except BlockedError:
                raise
            except Exception as e:
                log("  BLAD %s: %s" % (u, e))
                stats.setdefault("bledy", []).append(u)
                continue
            n_os += 1
            r = rows_from_page(ptext, fetched, u, "radni", "Rada Miasta Poznania",
                               default_name=name, default_func=func)
            for x in r:
                x["imie_nazwisko"], x["nazwisko_norm"], x["funkcja"] = name, norm(name), func
            rows.extend(r)
    stats.setdefault("strony_osob", {})["radni"] = n_os
    log("[radni] stron radnych: %d, pozycji: %d" % (n_os, len(rows)))
    return rows


def crawl_archiwum_osoby(fetcher, limit, stats):
    # Strona osoby w archiwum pokazuje w praktyce cale archiwum jej wydzialu (bez nazwy wydzialu).
    units = list_units(fetcher, BASE + "/bip/archiwum-oswiadczenia-majatkowe-osoby/",
                       r"^/bip/archiwum-oswiadczenia-majatkowe-osoby/[^/]+,\d+/$")
    stats.setdefault("jednostki", {})["archiwum-osoby"] = len(units)
    if limit:
        units = units[:limit]
    rows = []
    for u, label in units:
        text, fetched = fetcher.get(u)
        rows.extend(rows_from_page(text, fetched, u, "archiwum-osoby", ""))
    log("[archiwum-osoby] pozycji (przed deduplikacja): %d" % len(rows))
    return rows


# --------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sekcja", default="all",
                    help="lista po przecinku: %s (domyslnie all)" % ",".join(SEKCJE))
    ap.add_argument("--limit", type=int, default=0,
                    help="max jednostek/osob na sekcje (lub na kadencje) - do testow")
    ap.add_argument("--cache", default="/tmp/oswiadczenia_cache", help="katalog cache HTTP")
    ap.add_argument("--refresh", action="store_true", help="ignoruj cache (pobierz od nowa)")
    ap.add_argument("--delay", type=float, default=0.6, help="min. odstep miedzy zapytaniami [s]")
    ap.add_argument("--timeout", type=float, default=30)
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--out", default=DEFAULT_OUT, help="plik CSV (domyslnie %(default)s)")
    ap.add_argument("--stats-json", default="", help="opcjonalnie zapisz statystyki do JSON")
    args = ap.parse_args()

    if args.delay < 0.5:
        log("delay < 0.5 s - podnosze do 0.5 s (max ~2 req/s)")
        args.delay = 0.5
    sek = SEKCJE if args.sekcja == "all" else [s.strip() for s in args.sekcja.split(",") if s.strip()]
    bad = [s for s in sek if s not in SEKCJE]
    if bad:
        ap.error("nieznane sekcje: %s" % ", ".join(bad))

    f = Fetcher(args.cache, args.delay, args.timeout, args.retries, args.refresh)
    stats = {}
    rows = []
    try:
        if "prezydent" in sek:
            rows += crawl_prezydent(f, args.limit, stats)
        if "radni" in sek:
            rows += crawl_radni(f, args.limit, stats)
        if "wydzialy" in sek:
            rows += crawl_units(f, "wydzialy", BASE + "/bip/oswiadczenia-majatkowe-wydzialy/",
                                r"^/bip/oswiadczenia-majatkowe-wydzialy,\d+,\d+/$", args.limit, stats)
        if "mjo" in sek:
            rows += crawl_units(f, "mjo", BASE + "/bip/oswiadczenia-majatkowe-mjo/",
                                r"^/bip/oswiadczenia-majatkowe-mjo,\d+,\d+/$", args.limit, stats)
        if "archiwum-wydzialy" in sek:
            rows += crawl_units(f, "archiwum-wydzialy", BASE + "/bip/archiwum-oswiadczenia-majatkowe-wydzialy/",
                                r"^/bip/archiwum-oswiadczenia-majatkowe-wydzialy/[^/]+,\d+/$", args.limit, stats)
        if "archiwum-osoby" in sek:
            rows += crawl_archiwum_osoby(f, args.limit, stats)
    except BlockedError as e:
        log("STOP: %s" % e)
        sys.exit(2)

    # deduplikacja: ten sam PDF (lz_id) + ta sama osoba -> pierwszy wg kolejnosci sekcji
    seen = {}
    out = []
    dup = 0
    for r in rows:
        key = (r["_lz"], r["nazwisko_norm"])
        if key in seen:
            dup += 1
            continue
        # archiwum-osoby: gdy ten sam PDF jest juz w archiwum-wydzialy pod inna pisownia osoby
        if r["sekcja_bip"] == "archiwum-osoby" and any(k[0] == r["_lz"] for k in seen):
            dup += 1
            continue
        seen[key] = True
        out.append(r)
    by_lz = {}
    for r in out:
        by_lz.setdefault(r["_lz"], set()).add(r["sekcja_bip"])
    multi = sum(1 for v in by_lz.values() if len(v) > 1)

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    order = {s: i for i, s in enumerate(["prezydent-i-zastepcy", "radni", "wydzialy", "mjo",
                                         "archiwum-wydzialy", "archiwum-osoby"])}
    out.sort(key=lambda r: (order.get(r["sekcja_bip"], 9), norm(r["jednostka"]), r["nazwisko_norm"],
                            r["rok"] or "0000", int(r["_lz"])))
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in out:
            w.writerow(r)

    years = sorted({r["rok"] for r in out if r["rok"]})
    persons = {(r["nazwisko_norm"]) for r in out}
    persons_ctx = {(r["nazwisko_norm"], norm(r["jednostka"])) for r in out}
    per_sek = {}
    for r in out:
        per_sek[r["sekcja_bip"]] = per_sek.get(r["sekcja_bip"], 0) + 1
    rodz = {}
    for r in out:
        rodz[r["rodzaj"]] = rodz.get(r["rodzaj"], 0) + 1
    summary = {
        "pozycji": len(out),
        "duplikatow_pominietych": dup,
        "pdf_w_wielu_sekcjach": multi,
        "osob_unikalnych_wg_nazwiska": len(persons),
        "osob_unikalnych_wg_nazwiska_i_jednostki": len(persons_ctx),
        "pozycji_wg_sekcji": per_sek,
        "pozycji_wg_rodzaju": rodz,
        "pozycji_bez_roku": sum(1 for r in out if not r["rok"]),
        "lata": [years[0], years[-1]] if years else [],
        "jednostek_na_listach": stats.get("jednostki", {}),
        "stron_osob": stats.get("strony_osob", {}),
        "stron_bez_oswiadczen": len(stats.get("puste", [])),
        "bledy": stats.get("bledy", []),
        "zapytan_siec": f.n_net,
        "z_cache": f.n_cache,
        "plik": args.out,
    }
    log(json.dumps(summary, ensure_ascii=False, indent=1))
    if args.stats_json:
        summary["puste_strony"] = stats.get("puste", [])
        with open(args.stats_json, "w", encoding="utf-8") as fh:
            json.dump(summary, fh, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
