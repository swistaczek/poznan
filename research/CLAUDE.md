# research/ — baza wiedzy referencyjna

Studia, analizy, wyniki deep-researchu, prompty dla sub-ekspertów. Reużywalne między kampaniami.

## Struktura

- `prompty/0N-*.md` — brief dla top 1% eksperta (persona + zakres + „czego NIE chcemy").
- `<obszar>/wyniki-0N-*.md` — wynik researchu z prompta 0N.
- Obszary: `halas`, `rowery`, `uspokojenie-ruchu`, `transparentnosc`, `instytucje`.

Każdy `wyniki-*.md` zawiera na końcu sekcję **FAQ** — 12–15 pytań mieszkańca-aktywisty z odpowiedziami eksperta. Sięgaj po FAQ zanim przeczytasz pełen esej — to pierwszy layer retrieval.

## Styl

Gęsty research. Bez akademickich wstępów, bez podsumowań redundantnych.

- Cytuj DOI / sygnatury / art. konkretnie.
- Sygnatury orzeczeń tylko **zweryfikowane** — niepewne oznacz `[do weryfikacji]`, nie zmyślaj.
- Cytowania BIP: URL + data dostępu.

## Dodawanie

- **Nowy duży obszar**: najpierw `prompty/0N-nowy-obszar.md` (brief), odpal zewnętrznego eksperta, wynik → `<obszar>/wyniki-0N-*.md`. Puste szablony wyników z metadanymi jako baza.
- **Uzupełnienie istniejącego**: dopisz sekcję w odpowiednim `wyniki-*.md`, zaktualizuj FAQ jeśli pytanie już pokryte.
- **Nie atomizuj** przedwcześnie — atomy mają sens gdy są wielokrotnie używane samodzielnie.

## Rozmiary

Docelowo chunki ≤ 12 KB. Obecne `wyniki-*.md` są 45–77 KB — w toku reorganizacji. Nie powielaj tego anti-patternu w nowych plikach.
