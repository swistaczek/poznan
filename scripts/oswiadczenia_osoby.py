#!/usr/bin/env python3
"""Wybrane osoby -> linki do oswiadczen majatkowych (z indeksu BIP).

Wejscie (poza repo): CSV z kolumna imie_nazwisko (pozostale kolumny ignorowane).
Indeks: research/transparentnosc/oswiadczenia-majatkowe/dane/oswiadczenia.csv
        + dane/oswiadczenia-zewnetrzne.csv
Wyjscie: osoby.md i dane/osoby.csv - tylko osoby z oswiadczeniami, tylko linki.

Dopasowanie: imie + nazwisko po normalizacji (bez polskich znakow, dowolna kolejnosc,
drugie imie w wejsciu ignorowane).

  python3 scripts/oswiadczenia_osoby.py --wejscie /sciezka/osoby.csv
"""
import argparse
import csv
import os
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "research", "transparentnosc", "oswiadczenia-majatkowe")
DANE = os.path.join(DIR, "dane")
RODZAJ_KOLEJNOSC = {"na rozpoczęcie": 0, "roczne": 1, "korekta": 2, "na zakończenie": 3}


def tokens(s):
    s = s.replace("ł", "l").replace("Ł", "L")
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z\- ]", " ", s).split()


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wejscie", required=True, help="CSV z kolumna imie_nazwisko")
    args = ap.parse_args()

    index = load(os.path.join(DANE, "oswiadczenia.csv")) + load(os.path.join(DANE, "oswiadczenia-zewnetrzne.csv"))
    by_tok = {}
    for r in index:
        for t in set(tokens(r["imie_nazwisko"])):
            by_tok.setdefault(t, []).append(r)

    out_rows = []
    md = ["# Wybrane osoby: oświadczenia majątkowe\n",
          "| Osoba | Oświadczenia (PDF) |", "|---|---|"]
    for o in load(args.wejscie):
        t = tokens(o["imie_nazwisko"])
        if not t:
            continue
        imie, nazwisko = t[0], t[-1]
        hits = [r for r in by_tok.get(nazwisko, []) if imie in tokens(r["imie_nazwisko"])]
        if not hits:
            continue
        hits.sort(key=lambda r: (r["jednostka"], -(int(r["rok"]) if r["rok"].isdigit() else 0),
                                 RODZAJ_KOLEJNOSC.get(r["rodzaj"], 9)))
        linki = []
        for jed in dict.fromkeys(r["jednostka"] for r in hits):
            rs = [r for r in hits if r["jednostka"] == jed]
            czesci = []
            for r in rs:
                etykieta = r["rok"] or "b.d."
                if r["rodzaj"] and r["rodzaj"] != "roczne":
                    etykieta += " " + r["rodzaj"]
                czesci.append("[%s](%s)" % (etykieta, r["url_pdf"]))
                out_rows.append({"imie_nazwisko": rs[0]["imie_nazwisko"], "jednostka": jed, "rok": r["rok"],
                                 "rodzaj": r["rodzaj"], "url_pdf": r["url_pdf"], "url_strony": r["url_strony"]})
            linki.append("[%s](%s): %s" % (jed, rs[0]["url_strony"], ", ".join(czesci)))
        md.append("| %s | %s |" % (hits[0]["imie_nazwisko"], "<br>".join(linki)))

    with open(os.path.join(DIR, "osoby.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    with open(os.path.join(DANE, "osoby.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["imie_nazwisko", "jednostka", "rok", "rodzaj", "url_pdf", "url_strony"],
                           lineterminator="\n")
        w.writeheader()
        w.writerows(out_rows)
    print("osob z oswiadczeniami: %d, PDF: %d" % (len(md) - 3, len(out_rows)))


if __name__ == "__main__":
    main()
