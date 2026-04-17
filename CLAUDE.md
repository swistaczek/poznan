# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repo

Baza inicjatyw obywatelskich dla Poznania: hałas tramwajowy (ul. Dąbrowskiego, Jeżyce), ścieżki rowerowe, uspokojenie ruchu, transparentność (UDIP), kompetencje organów, jakość życia. **Nie jest projektem kodowym** — brak build/test/dependencies. Treść: `.md`, `.pdf`, dane, linki.

## Język i styl

- Wszystko po polsku: odpowiedzi, commity, nazwy plików, treść.
- Terminologia polskiego porządku prawnego ("rozporządzenie", nie "regulation"; "immisje", nie "nuisance").
- **Dokumenty źródłowe** (`research/`, notatki, analizy, rejestry): **gęsty styl**. Bez zwrotów grzecznościowych, bez „warto zauważyć", bez „w niniejszym dokumencie". Fakty, liczby, sygnatury, linki. Oszczędzaj tokeny — te pliki ładują się do wielu sesji.
- **Pisma urzędowe** (`<inicjatywa>/pisma/`): **pełny protokół urzędowy**. Nie skracaj zwrotów, adresat z pełną właściwością rzeczową, podstawa prawna konkretnie, petitum, termin odpowiedzi, klauzule doręczenia. Tu forma ma wartość procesową.

## Struktura

```
research/<obszar>/              # wiedza referencyjna, reużywalna
research/prompty/               # briefy 01–NN dla top 1% ekspertów (persona + zakres)
<inicjatywa>/<obszar>/          # kampania (np. dabrowskiego/halas/)
szablony/<obszar>/              # reużywalne szablony pism (w budowie)
```

Obszary: `halas`, `rowery`, `uspokojenie-ruchu`, `transparentnosc`, `instytucje`.

Decyzja przy nowym materiale: ogólna wiedza → `research/`, sprawa konkretna → `<inicjatywa>/`, reużywalny szablon → `szablony/`.

**Nazwy plików**: kebab-case, **bez polskich znaków i spacji** (łamie URL/git na różnych OS).

## Nested CLAUDE.md

Podkatalogi mogą mieć własne `CLAUDE.md` z lokalnymi konwencjami — ładują się gdy Claude czyta plik z tego katalogu. **Caveat: nested CLAUDE.md NIE reładują się po `/compact`** (tylko root). Kluczowe reguły trzymaj w tym pliku; nested służą do konwencji specyficznych dla obszaru.

## Rozmiary plików

- Cel: każdy plik ≤ 12 KB (bezpieczny budżet tokenów jednym Read).
- Twardy limit: **nie twórz plików > 25 K tokenów (~40 KB PL)** — Read zwraca błąd, Claude pracuje na ślepo przez Grep.
- Obecne `research/<obszar>/wyniki-*.md` (45–77 KB) przekraczają limit — reorganizacja w fazie planowania; do czasu jej ukończenia czytaj z `offset`/`limit` lub Grep po sekcjach.

## Styl pracy z dokumentami

- Cytuj akty prawne dokładnie: akt, Dz.U., art./§/ust., data aktualnej wersji.
- Rozdzielaj stan prawny, stan faktyczny, żądanie.
- Nie zmyślaj liczb, dat, sygnatur. Niepewne → `[do weryfikacji]`.
- Zachowuj oryginalne nazwy: ZDM Poznań, MPK Poznań sp. z o.o., WIOŚ, RDOŚ, Rada Miasta Poznania, rada osiedla.

## Pisanie pism urzędowych

1. Podstawa prawna — konkretny artykuł, nie „zgodnie z przepisami".
2. Adresat właściwy rzeczowo i miejscowo → mapa w `research/instytucje/wyniki-07-kompetencje-instytucji.md`.
3. Termin — KPA art. 35/237 lub UDIP 14 dni.
4. Forma doręczenia (ePUAP / e-mail / adres pocztowy) — jawna klauzula.

## Dane publiczne

- bip.poznan.pl — uchwały, budżet, oświadczenia, zamówienia.
- sip.poznan.pl — MPZP, WZ.
- Rejestr umów, petycji, interpelacji.
- UDIP: 14 dni, forma elektroniczna wystarcza (zwykły e-mail).

Przy cytowaniu — **URL + data dostępu** (treść BIP znika po kadencjach).

## Panel ekspertów przed finalną rekomendacją

Sprawy wysokostawkowe i wieloaspektowe (prawo + technika + zdrowie + urbanistyka + polityka). Pojedyncza perspektywa = płytka rada.

**Przed rekomendacją strategiczną: uruchom 4–6 sub-agentów równolegle** (jedna wiadomość, wiele wywołań `Agent`), model Opus, w rolach top 1% specjalistów. Persony w `research/prompty/`.

- Każdy sub-agent: persona + brief + „czego NIE chcemy".
- Syntezę robi agent główny: konsensus, rozbieżności, finalna propozycja.
- **NIE** uruchamiaj panelu dla zadań operacyjnych (formatowanie, literówki).

Kryterium: „gdybym pomylił się, kosztowałoby więcej niż kilka minut korekty" → panel.

## Compact instructions

Gdy streszczasz sesję, **zawsze** zachowaj:
- Sygnatury orzeczeń i konkretne art. cytowane w trakcie.
- Daty i adresatów pism wysłanych; otwarte terminy KPA/UDIP.
- Decyzje o strukturze repo i konwencjach.
- Wnioski z paneli ekspertów (ze wskazaniem plików wynikowych).

## Czego NIE robić

- Nie twórz struktury projektu kodowego (`package.json`, CI, `.gitignore` na `node_modules`).
- Nie tłumacz na angielski bez wyraźnej prośby.
- Nie usuwaj dokumentów źródłowych — wyglądające na duplikaty mogą różnić się datą lub wersją.
- Nie agreguj wielu spraw w jeden dokument — jedna sprawa = jeden katalog = osobna ścieżka urzędowa.
- **Nie** używaj wiki-links `[[...]]` — martwe poza Obsidian; używaj markdown relative.
- **Nie** używaj polskich znaków ani spacji w nazwach plików.
