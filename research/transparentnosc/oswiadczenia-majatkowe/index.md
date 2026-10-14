# Oświadczenia majątkowe: linki (BIP Poznania)

Linki do PDF oświadczeń majątkowych w BIP. Stan: 2026-10-14.

| Co | Plik |
|---|---|
| Wyszukiwarka | [`szukaj.html`](./szukaj.html) |
| Wybrane osoby | [`osoby.md`](./osoby.md), [`dane/osoby.csv`](./dane/osoby.csv) |
| Indeks BIP Poznania | [`dane/oswiadczenia.csv`](./dane/oswiadczenia.csv) |
| Inne BIP | [`dane/oswiadczenia-zewnetrzne.csv`](./dane/oswiadczenia-zewnetrzne.csv) |

Źródła:

- https://bip.poznan.pl/bip/oswiadczenia-majatkowe-wydzialy/
- https://bip.poznan.pl/bip/oswiadczenia-majatkowe-mjo/
- https://bip.poznan.pl/bip/prezydent-i-zastepcy/
- https://bip.poznan.pl/bip/radni/
- https://bip.poznan.pl/bip/archiwum-oswiadczenia-majatkowe-wydzialy/
- https://bip.umww.pl/7---81---k_62---k_oswiadczenia--osoby-wydajace-decyzje-administracyjne-w-imieniu-marszalka-wojewodztwa

```
python3 scripts/oswiadczenia_szukaj.py <nazwisko|funkcja|jednostka> [--rok RRRR] [--jednostka X]
python3 scripts/oswiadczenia_crawl.py
python3 scripts/oswiadczenia_osoby.py --wejscie <plik.csv>
```
