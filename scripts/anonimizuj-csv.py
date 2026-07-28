#!/usr/bin/env python3
"""Anonimizacja eksportu CSV z formularza poparcia (Google Forms, LimeSurvey itp.).

Problem: eksport ankiety poparcia zawiera imiona, nazwiska, adresy e-mail i tekst
opisowy z adresami zamieszkania. Takich danych nie wolno przekazać radnemu, urzędowi
ani wrzucić do repo (patrz sekcja RODO w CLAUDE.md). Jednocześnie liczba i struktura
poparcia to główny argument w interpelacji i wniosku PBO — trzeba ją udowodnić.

Rozwiązanie: pseudonimizacja zachowująca wartość dowodową:
- nazwisko → pierwsza litera (`Justyna K.`); jeden człon → sam inicjał (nie wiadomo,
  czy to imię, nazwisko czy pseudonim)
- e-mail → usunięty, zastąpiony solonym skrótem SHA-256 (6 znaków) = dowód, że głosy
  są odrębne (wykrywa duplikaty), bez możliwości odtworzenia adresu; osobno zachowana
  sama domena (kanał zgłoszeń)
- data → bez godziny (godzina + dzielnica to silny odcisk palca)
- tekst opisowy → wycięte numery budynków/mieszkań, kody pocztowe, telefony, e-maile,
  linki; nazwy własne tylko FLAGOWANE do decyzji człowieka (automat nie odróżni
  „park Sołacki" od nazwiska sąsiada)

Wyjście (3 pliki w --out-dir):
    <nazwa>-anonimizowana.csv    do przekazania na zewnątrz
    <nazwa>-podsumowanie.md      statystyki zbiorcze + opis metody anonimizacji
    <nazwa>-do-przegladu.md      wpisy z flagami — przejrzeć przed publikacją

Użycie:
    python3 scripts/anonimizuj-csv.py "ankieta.csv" --out-dir <katalog>
    python3 scripts/anonimizuj-csv.py "eksport.zip"           # zip z Google Forms
    ANON_SALT="stala-sol" python3 scripts/anonimizuj-csv.py ankieta.csv

Sól: bez soli skrót e-maila byłby odwracalny słownikowo (lista adresów → hash → dopasowanie).
Bez ustawionego ANON_SALT skrypt generuje sól losową dla jednego uruchomienia — id głosów
NIE będą wtedy spójne między kolejnymi eksportami tej samej ankiety. Do porównywania
kolejnych eksportów ustaw ANON_SALT (i trzymaj wartość lokalnie, nie w repo).

Katalog docelowy: `<inicjatywa>/<obszar>/pisma/YYYY-MM-DD_temat/` — gitignored.
Sam plik CSV z `Justyna K.` + dzielnicą to nadal dane pseudonimizowane (RODO) —
do repo wchodzi wyłącznie `-podsumowanie.md` (czyste agregaty), i to po przejrzeniu.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import secrets
import sys
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path

# --- heurystyki rozpoznawania kolumn (nagłówki polskie i angielskie) ---
WZORCE_KOLUMN: dict[str, tuple[str, ...]] = {
    "nazwisko": ("imię i nazwisko", "imie i nazwisko", "imię", "nazwisko", "name", "full name"),
    "email": ("e-mail", "email", "mail", "adres e-mail"),
    "data": ("timestamp", "data", "sygnatura czasowa", "date"),
    "tekst": ("dlaczego", "uzasadnienie", "komentarz", "uwagi", "opinia", "why", "comment"),
    "zgoda": ("zgoda", "rodo", "consent"),
}

# Dane kontaktowe/adresowe w tekście opisowym — wycinane automatycznie.
RE_MAIL = re.compile(r"\b[\w.+-]+@[\w.-]+\.\w+\b")
RE_URL = re.compile(r"https?://\S+|\bwww\.\S+")
RE_TEL = re.compile(r"(?<!\d)(?:\+48[\s-]?)?(?:\d[\s-]?){9}(?!\d)")
RE_KOD = re.compile(r"\b\d{2}-\d{3}\b")
RE_NR_MIESZK = re.compile(r"\b\d{1,3}\s*/\s*\d{1,3}[a-zA-Z]?\b")
RE_ADRES_NR = re.compile(
    r"((?:ul\.|ulicy|ulica|al\.|aleja|os\.|osiedlu|osiedle|pl\.|placu)\s+[^\d,;.]{2,40}?)"
    r"\s*\d+[a-zA-Z]?(?:/\d+[a-zA-Z]?)?",
    re.IGNORECASE,
)
RE_KANDYDAT_NAZWA = re.compile(
    r"(?<=[a-ząćęłńóśźż,] )([A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]{2,})"
)

# Nazwy własne miejskie i częste wyrazy zdaniowe — nie flagujemy ich jako możliwych nazwisk.
# Uzupełniaj przy nowych kampaniach (porównanie jest bez ogonków i bez wielkości liter).
SLOWNIK_MIEJSKI = """
poznan poznania poznaniu poznaniak poznaniakow poznanianek poznanskiego jezyce jezycach
jezyc jezycami solacz solaczu solacza solaczem solacki solackiego solackim winiary winiarach
golecin golecina podolany strzeszyn grunwald lazarz wilda debiec naramowice piatkowo
koscielna koscielnej wawrzynca poleska poleskiej niestachowska niestachowskiej dabrowskiego
urbanowska urbanowskiej szamarzewskiego polna polnej hetmanska hetmanskiej zeromskiego
wodziczki wierzbak wierzbakiem rusalka rusalke goplana goplany goplanie ogrody ogrodach
grudzieniec grudzencu botaniczny botanicznego przyrodniczego uniwersytetu
park parku parkiem parkow miasto miasta miastem miescie rada rady rade radzie osiedle
osiedla osiedlu urzad urzedzie prezydent zdm mpk pkp plk mpzp pbo wpf um kpa udip
swietego sw sw. tramwaj autobus rower rowerem wozek wozkiem dziecko dzieci szkola przedszkole
nie tak moim mysle musze chce chcialbym chcialabym czesto codziennie zawsze wreszcie
przeciez niestety dlatego poniewaz bardzo jestem mieszkam wasza waszą pani panie panstwo
"""


def bez_ogonkow(s: str) -> str:
    """Normalizuje do porównań: małe litery, bez znaków diakrytycznych."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s.lower())
        if unicodedata.category(c) != "Mn"
    )


ZNANE = {bez_ogonkow(w) for w in SLOWNIK_MIEJSKI.split()}


def wczytaj(sciezka: Path) -> tuple[list[dict[str, str]], str]:
    """Czyta CSV — także spakowany w .zip (eksport Google Forms). Zwraca (wiersze, nazwa)."""
    if sciezka.suffix.lower() == ".zip":
        # unzip(1) na macOS wywala się na nazwach UTF-8 z eksportów Google — czytamy zipfile.
        with zipfile.ZipFile(sciezka) as z:
            nazwy = [n for n in z.namelist() if n.lower().endswith(".csv")]
            if not nazwy:
                sys.exit(f"BŁĄD: brak pliku .csv w archiwum {sciezka}")
            tekst = z.read(nazwy[0]).decode("utf-8-sig")
            nazwa = Path(nazwy[0]).stem
    else:
        tekst = sciezka.read_text(encoding="utf-8-sig")
        nazwa = sciezka.stem
    wiersze = list(csv.DictReader(tekst.splitlines()))
    if not wiersze:
        sys.exit(f"BŁĄD: pusty plik {sciezka}")
    return wiersze, nazwa


def znajdz_kolumny(naglowki: list[str], nadpisania: dict[str, str | None]) -> dict[str, str | None]:
    """Dopasowuje nagłówki do ról (nazwisko/email/data/tekst/zgoda). Nadpisania mają priorytet."""
    mapa: dict[str, str | None] = {}
    for rola, wzorce in WZORCE_KOLUMN.items():
        if nadpisania.get(rola):
            wybrana = nadpisania[rola]
            if wybrana not in naglowki:
                sys.exit(f"BŁĄD: kolumna '{wybrana}' nie istnieje. Dostępne: {naglowki}")
            mapa[rola] = wybrana
            continue
        mapa[rola] = next(
            (h for h in naglowki if any(w in bez_ogonkow(h) for w in map(bez_ogonkow, wzorce))),
            None,
        )
    return mapa


def maskuj_nazwisko(pelne: str) -> str:
    czesci = [c for c in pelne.split() if c]
    if not czesci:
        return "[bez podpisu]"
    if len(czesci) == 1:
        return f"{czesci[0][0].upper()}."
    return f"{czesci[0]} {czesci[-1][0].upper()}."


def skrot_mail(mail: str, sol: str) -> tuple[str, str]:
    mail = mail.strip().lower()
    if "@" not in mail:
        return ("", "")
    return (hashlib.sha256((sol + mail).encode()).hexdigest()[:6], mail.split("@", 1)[1])


def scrub(txt: str) -> tuple[str, list[str]]:
    """Wycina dane kontaktowe/adresowe. Zwraca (tekst, flagi_do_przegladu)."""
    flagi: list[str] = []
    t = txt.strip()
    if not t:
        return ("", flagi)

    for rx, etykieta, zamiennik in (
        (RE_MAIL, "e-mail w treści", "[e-mail usunięty]"),
        (RE_URL, "link", "[link usunięty]"),
        (RE_TEL, "możliwy nr telefonu", "[nr usunięty]"),
        (RE_KOD, "kod pocztowy", "[kod usunięty]"),
        (RE_NR_MIESZK, "nr mieszkania", "[nr usunięty]"),
    ):
        if rx.search(t):
            flagi.append(etykieta)
            t = rx.sub(zamiennik, t)
    if RE_ADRES_NR.search(t):
        flagi.append("adres z numerem")
        t = RE_ADRES_NR.sub(r"\1", t)  # zostaje nazwa ulicy, spada numer

    for m in RE_KANDYDAT_NAZWA.finditer(t):
        if bez_ogonkow(m.group(1)) not in ZNANE:
            flagi.append(f"możliwa nazwa własna: {m.group(1)}")
    return (t, flagi)


def main() -> None:
    p = argparse.ArgumentParser(description="Anonimizacja CSV z ankiety poparcia (RODO).")
    p.add_argument("plik", type=Path, help="CSV albo ZIP z eksportem ankiety")
    p.add_argument("--out-dir", type=Path, default=Path("."), help="katalog wyjściowy")
    p.add_argument("--kol-nazwisko", help="nagłówek kolumny z imieniem i nazwiskiem")
    p.add_argument("--kol-email", help="nagłówek kolumny z e-mailem")
    p.add_argument("--kol-data", help="nagłówek kolumny z datą/timestampem")
    p.add_argument("--kol-tekst", help="nagłówek kolumny z tekstem opisowym")
    p.add_argument("--kol-zgoda", help="nagłówek kolumny ze zgodą RODO")
    p.add_argument("--maks-kategorii", type=int, default=12,
                   help="ile wartości kolumny traktować jako pytanie zamknięte (domyślnie 12)")
    args = p.parse_args()

    sol = os.environ.get("ANON_SALT")
    if not sol:
        sol = secrets.token_hex(8)
        print("UWAGA: brak ANON_SALT — sól losowa, id głosów niespójne między uruchomieniami.",
              file=sys.stderr)

    wiersze, nazwa = wczytaj(args.plik)
    naglowki = list(wiersze[0].keys())
    kol = znajdz_kolumny(naglowki, {
        "nazwisko": args.kol_nazwisko, "email": args.kol_email, "data": args.kol_data,
        "tekst": args.kol_tekst, "zgoda": args.kol_zgoda,
    })
    print("rozpoznane kolumny:", {k: v for k, v in kol.items() if v}, file=sys.stderr)

    # kolumny zamknięte (dzielnica, forma wsparcia…) — przepisywane bez zmian i zliczane.
    # Liczymy kategorie PO rozbiciu na średnikach: Google Forms zapisuje wybór wielokrotny
    # jako "A;B;C", więc bez rozbicia kolumna z 5 opcjami ma dziesiątki kombinacji
    # i wypadłaby z zestawienia jako "otwarta".
    obsluzone = {v for v in kol.values() if v}

    def kategorie(h: str) -> set[str]:
        return {x.strip() for w in wiersze for x in w[h].split(";") if x.strip()}

    zamkniete = [
        h for h in naglowki
        if h not in obsluzone and len(kategorie(h)) <= args.maks_kategorii
    ]
    pominiete = [h for h in naglowki if h not in obsluzone and h not in zamkniete]

    out: list[dict[str, object]] = []
    przeglad: list[tuple[int, str, list[str], str]] = []
    skroty: Counter[str] = Counter()

    for i, r in enumerate(wiersze, start=1):
        h, domena = skrot_mail(r[kol["email"]] if kol["email"] else "", sol)
        skroty[h] += 1
        tekst, flagi = scrub(r[kol["tekst"]] if kol["tekst"] else "")
        podpis = maskuj_nazwisko(r[kol["nazwisko"]]) if kol["nazwisko"] else ""
        rekord: dict[str, object] = {"lp": i}
        if kol["data"]:
            rekord["data"] = r[kol["data"]].split(" ")[0].replace("/", "-")
        if podpis:
            rekord["podpis"] = podpis
        if h:
            rekord["id_glosu"] = h
            rekord["domena_e-mail"] = domena
        for c in zamkniete:
            rekord[c] = "; ".join(x.strip() for x in r[c].split(";") if x.strip())
        if kol["zgoda"]:
            rekord["zgoda_rodo"] = "tak" if r[kol["zgoda"]].strip() else "nie"
        if kol["tekst"]:
            rekord["uzasadnienie"] = tekst
        out.append(rekord)
        if flagi:
            przeglad.append((i, podpis, sorted(set(flagi)), tekst))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    baza = args.out_dir / nazwa

    csv_out = Path(f"{baza}-anonimizowana.csv")
    with csv_out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    daty = sorted(str(r.get("data", "")) for r in out if r.get("data"))
    dupy = {k: v for k, v in skroty.items() if k and v > 1}
    unikalne = len([k for k in skroty if k])
    z_tekstem = sum(1 for r in out if r.get("uzasadnienie"))

    md = Path(f"{baza}-podsumowanie.md")
    with md.open("w", encoding="utf-8") as f:
        f.write(f"# Ankieta — podsumowanie zbiorcze\n\n")
        f.write(f"Zebrano **{len(out)}** zgłoszeń")
        if daty:
            f.write(f" w okresie **{daty[0]} – {daty[-1]}**")
        f.write(".\n\n")
        if unikalne:
            f.write(f"- unikalnych adresów e-mail: **{unikalne}** (powtórzenia: {len(dupy)})\n")
        if kol["tekst"]:
            f.write(f"- zgłoszeń z własnym uzasadnieniem opisowym: **{z_tekstem}**\n")
        if kol["zgoda"]:
            zg = sum(1 for r in out if r.get("zgoda_rodo") == "tak")
            f.write(f"- wyrażona zgoda RODO: **{zg}**\n")
        f.write("\n")
        for c in zamkniete:
            licznik: Counter[str] = Counter()
            for r in wiersze:
                for cz in [x.strip() for x in r[c].split(";") if x.strip()]:
                    licznik[cz] += 1
            f.write(f"## {c}\n\n| Wartość | Zgłoszeń | Udział |\n|---|---:|---:|\n")
            for k, v in licznik.most_common():
                f.write(f"| {k} | {v} | {v / len(out) * 100:.1f}% |\n")
            f.write("\n")
        if daty:
            po_mies = Counter(d[:7] for d in daty)
            f.write("## Rozkład w czasie\n\n| Miesiąc | Zgłoszeń |\n|---|---:|\n")
            for k in sorted(po_mies):
                f.write(f"| {k} | {po_mies[k]} |\n")
            f.write("\n")
        f.write("## Metoda anonimizacji\n\n")
        f.write("- nazwisko skrócone do pierwszej litery (`Justyna K.`)\n")
        f.write("- adres e-mail usunięty; zastąpiony solonym skrótem SHA-256 (6 znaków) — "
                "służy wyłącznie do wykazania unikalności zgłoszenia, nie pozwala odtworzyć adresu\n")
        f.write("- z daty zgłoszenia zachowany tylko dzień (bez godziny)\n")
        f.write("- z treści opisowej usunięte numery budynków i mieszkań, kody pocztowe, "
                "numery telefonów, adresy e-mail i linki\n")
        f.write("- surowy eksport pozostaje wyłącznie u organizatora inicjatywy, "
                "udostępniany do wglądu na żądanie\n")
        if pominiete:
            f.write(f"\nKolumny pominięte w pliku anonimizowanym: {', '.join(pominiete)}.\n")

    rev = Path(f"{baza}-do-przegladu.md")
    with rev.open("w", encoding="utf-8") as f:
        f.write("# Wpisy opisowe do ręcznego przeglądu przed publikacją\n\n")
        f.write(f"{len(przeglad)} z {len(out)} wpisów zawiera wzorce mogące identyfikować "
                "wtórnie (nazwy własne, adresy, numery). Numery i kontakty zostały wycięte "
                "automatycznie; nazwy własne wymagają decyzji człowieka.\n\n")
        for i, podpis, flagi, tekst in przeglad:
            f.write(f"## lp. {i} — {podpis}\n\nFlagi: {', '.join(flagi)}\n\n> {tekst}\n\n")

    print(f"wierszy: {len(out)} | unikalnych e-maili: {unikalne} | duplikaty: {len(dupy)}")
    print(f"do ręcznego przeglądu: {len(przeglad)}")
    for f_out in (csv_out, md, rev):
        print(f"  {f_out}")


if __name__ == "__main__":
    main()
