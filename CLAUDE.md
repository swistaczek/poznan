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

## Ochrona danych osobowych (krytyczne — nigdy nie omijaj)

Pisma urzędowe zawierają **dane osobowe nadawców**: imię i nazwisko, adres zamieszkania, adres do korespondencji, e-mail, telefon, sygnatury własne odsyłające do adresu, kontekst rodzinny (dzieci, wiek, zdrowie). **Te dane nie wchodzą do repo** — ani w commitach, ani w plikach śledzonych.

**Dwuwarstwowa struktura:**

- **Publiczne (w repo):**
  - `szablony/<obszar>/*.md` — wzory z placeholderami `{{...}}`
  - `<inicjatywa>/<obszar>/pisma/REJESTR.md` — zsanityzowany (bez imion/adresów/e-maili; sygnatury neutralne typu `EB/HAL/2026/04/01`, nie `EB/DAB87/…`)
  - `<inicjatywa>/<obszar>/index.md` — zsanityzowany (bez numeru budynku zamieszkania)

- **Lokalne (ignorowane przez git):**
  - `<inicjatywa>/<obszar>/pisma/YYYY-MM-DD_temat/` — `pismo.md`, `pismo.docx`, `pismo.pdf`, `email.txt`
  - `<inicjatywa>/<obszar>/odpowiedzi/*.pdf|*.docx`

**Wzorce `.gitignore` (w root repo — utrzymuj, nie usuwaj):**

```
**/pisma/2*/                # foldery spraw (YYYY-MM-DD_*)
**/pisma/*.docx
**/pisma/*.pdf
**/pisma/*.rtf
**/pisma/email.txt
**/pisma/email-*.txt
**/odpowiedzi/*.pdf
**/odpowiedzi/*.docx
```

**Przed `git add` / `git commit`:**

1. `git check-ignore -v <plik>` dla każdego nowego pliku mogącego zawierać dane osobowe — potwierdź że jest ignorowany.
2. `git status --untracked-files=all` — zobacz co dokładnie git chce tracknąć; jeśli widzisz pismo z prawdziwymi danymi, STOP i popraw `.gitignore`.
3. Przejrzyj diffy sanityzowanych plików (REJESTR.md, index.md) — żadnego imienia, adresu, e-maila, sygnatury z nr budynku.
4. Gdy pojawia się nowa kategoria plików ze sprawą (np. `notatki-telefoniczne.md`, `zdjecia/`) — dodaj wzorzec w `.gitignore` **przed** pierwszym `git add`.

**Wyjątki:**
- Odpowiedź urzędu bez danych osobowych wnioskodawcy można zarchiwizować publicznie po świadomej decyzji użytkownika: `git add -f <plik>`.
- Dane publicznych urzędników (imię, nazwisko, stanowisko, e-mail służbowy, adres urzędu) **nie są** danymi osobowymi w rozumieniu tej sekcji — mogą być w repo.

**Gdy użytkownik prosi o commit:** zawsze wykonaj krok 1–3 powyżej, nawet gdy nie prosi wprost o weryfikację prywatności.

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
