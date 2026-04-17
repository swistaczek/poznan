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

## Przepływ po otrzymaniu wyniku od eksperta

Surowy output (LLM lub człowiek) to jeden blok tekstu bez formatowania. Kolejność:

1. **Wklej surowy wynik** do `<obszar>/wyniki-0N-*.md` — bez formatowania, to źródło historyczne.
2. **Dodaj header nawigacyjny** na górze pliku (wzór: `wyniki-07-kompetencje-instytucji.md`):
   - blok `> UWAGA: nie edytuj, używaj chunków`
   - lista linków do chunków
   - metadane: prompt źródłowy, data, zasięg
3. **Utwórz podkatalog** `<obszar>/0N-nazwa/` i rozbij treść na chunki ≤ 12 KB:
   - `index.md` — TL;DR + tabela szybkiego lookup + nawigacja chunków
   - `01-*.md`, `02-*.md` … — tematyczne sekcje
   - `99-faq.md` — FAQ (12–15 pytań aktywisty) — **zawsze osobny plik, pierwszy layer retrieval**
   - `zasoby.md` lub `bibliografia.md` — linki z datami dostępu, sygnatury Dz.U.
4. **Zaktualizuj** `<obszar>/index.md` (jeśli istnieje) o wskaźnik do nowego podkatalogu.

Nie formatuj monolitu przed chunkingiem — strata czasu i tokeny bez wartości.

## Rozmiary

Docelowo chunki ≤ 12 KB. Obecne `wyniki-*.md` są 45–77 KB — w toku reorganizacji. Nie powielaj tego anti-patternu w nowych plikach.
