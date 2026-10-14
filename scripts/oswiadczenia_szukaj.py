#!/usr/bin/env python3
"""Wyszukiwarka w indeksie linkow do oswiadczen majatkowych (BIP Miasta Poznania).

Szuka po nazwisko_norm / funkcja / jednostka, bez polskich znakow i bez wielkosci liter.
Fragmenty slow dzialaja; wiele slow = AND (kazde slowo musi wystapic gdziekolwiek).

Przyklady:
  python3 scripts/oswiadczenia_szukaj.py kowalsk
  python3 scripts/oswiadczenia_szukaj.py "zarzad drog" dyrektor --rok 2024
  python3 scripts/oswiadczenia_szukaj.py jaskowiak --rodzaj roczne
  python3 scripts/oswiadczenia_szukaj.py --jednostka "inzyniera ruchu"
  python3 scripts/oswiadczenia_szukaj.py golek --csv > wynik.csv

Tylko biblioteka standardowa Pythona 3.
"""

import argparse
import csv
import os
import re
import sys
import unicodedata

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CSV = os.path.join(REPO_ROOT, "research", "transparentnosc", "oswiadczenia-majatkowe",
                           "dane", "oswiadczenia.csv")
EXT_CSV = os.path.join(os.path.dirname(DEFAULT_CSV), "oswiadczenia-zewnetrzne.csv")  # inne BIP-y (np. UMWW)


def norm(s):
    s = (s or "").replace("ł", "l").replace("Ł", "L")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"\s+", " ", s).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fraza", nargs="*", help="slowa (AND) szukane w nazwisku, funkcji i jednostce")
    ap.add_argument("--rok", help="rok (np. 2024) albo zakres 2020-2023")
    ap.add_argument("--jednostka", help="fragment nazwy jednostki/wydzialu (AND, bez polskich znakow)")
    ap.add_argument("--rodzaj", help="fragment rodzaju: roczne / rozpocz / zakoncz / korekta / inne")
    ap.add_argument("--sekcja", help="fragment sekcji_bip: wydzialy, mjo, radni, prezydent, archiwum")
    ap.add_argument("--csv", action="store_true", help="wynik jako CSV (wszystkie kolumny) na stdout")
    ap.add_argument("--plik", action="append", default=None,
                    help="plik indeksu, mozna powtorzyc (domyslnie oswiadczenia.csv + oswiadczenia-zewnetrzne.csv)")
    ap.add_argument("--limit", type=int, default=0, help="max liczba wynikow (0 = bez limitu)")
    args = ap.parse_args()

    if not args.fraza and not (args.jednostka or args.rok or args.rodzaj or args.sekcja):
        ap.error("podaj fraze albo co najmniej jeden filtr (--jednostka/--rok/--rodzaj/--sekcja)")
    pliki = args.plik or [DEFAULT_CSV] + ([EXT_CSV] if os.path.exists(EXT_CSV) else [])
    for p in pliki:
        if not os.path.exists(p):
            sys.exit("brak pliku indeksu: %s (uruchom scripts/oswiadczenia_crawl.py)" % p)

    terms = [norm(t) for t in " ".join(args.fraza).split() if t.strip()]
    jterms = [norm(t) for t in (args.jednostka or "").split() if t.strip()]
    rok_od = rok_do = None
    if args.rok:
        m = re.fullmatch(r"\s*(\d{4})\s*(?:-\s*(\d{4}))?\s*", args.rok)
        if not m:
            ap.error("--rok: podaj RRRR albo RRRR-RRRR")
        rok_od = int(m.group(1))
        rok_do = int(m.group(2) or m.group(1))

    def wiersze():
        for p in pliki:
            with open(p, encoding="utf-8", newline="") as fh:
                yield from csv.DictReader(fh)

    with open(pliki[0], encoding="utf-8", newline="") as fh:
        fields = csv.DictReader(fh).fieldnames
    if True:
        hits = []
        for r in wiersze():
            hay = " ".join([r.get("nazwisko_norm", ""), norm(r.get("imie_nazwisko", "")),
                            norm(r.get("funkcja", "")), norm(r.get("jednostka", ""))])
            if any(t not in hay for t in terms):
                continue
            if jterms:
                jn = norm(r.get("jednostka", ""))
                if any(t not in jn for t in jterms):
                    continue
            if rok_od is not None:
                if not r.get("rok", "").isdigit() or not (rok_od <= int(r["rok"]) <= rok_do):
                    continue
            if args.rodzaj and norm(args.rodzaj) not in norm(r.get("rodzaj", "")):
                continue
            if args.sekcja and norm(args.sekcja) not in norm(r.get("sekcja_bip", "")):
                continue
            hits.append(r)

    hits.sort(key=lambda r: (r.get("nazwisko_norm", ""), r.get("jednostka", ""), r.get("rok", "") or "0000"))
    if args.limit:
        hits = hits[:args.limit]

    if args.csv:
        w = csv.DictWriter(sys.stdout, fieldnames=fields)
        w.writeheader()
        for r in hits:
            w.writerow(r)
    else:
        for r in hits:
            print(" | ".join([r.get("imie_nazwisko", ""), r.get("funkcja", "") or "-",
                              r.get("jednostka", "") or "-", r.get("rok", "") or "-",
                              r.get("rodzaj", "") or "-", r.get("url_pdf", "")]))
        print("wynikow: %d" % len(hits), file=sys.stderr)


if __name__ == "__main__":
    main()
