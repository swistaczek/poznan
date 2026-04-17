# Indeks repo

Mapa nawigacyjna bazy wiedzy i inicjatyw obywatelskich dla Poznania.

## Szybkie wejście

| Cel | Ścieżka |
|---|---|
| Piszę pismo urzędowe | [`szablony/`](./szablony/) + [`ADRESY.md`](./ADRESY.md) |
| Sprawdzam termin KPA/UDIP | [`TERMINY.md`](./TERMINY.md) |
| Szukam adresata właściwego | [`research/instytucje/_index.md`](./research/instytucje/_index.md) |
| Zaczynam nowy research | [`research/prompty/`](./research/prompty/) |
| Prowadzę kampanię Dąbrowskiego | [`dabrowskiego/`](./dabrowskiego/) |

## Baza wiedzy — `research/`

| Obszar | Temat | Indeks |
|---|---|---|
| halas | hałas tramwajowy — akustyka, immisje, zdrowie | [`_index`](./research/halas/_index.md) |
| uspokojenie-ruchu | Tempo 30, woonerfy, interwencje | [`_index`](./research/uspokojenie-ruchu/_index.md) |
| rowery | polityka rowerowa Poznania, audyt CROW | [`_index`](./research/rowery/_index.md) |
| transparentnosc | UDIP, budżet, skargi na bezczynność | [`_index`](./research/transparentnosc/_index.md) |
| instytucje | mapa kompetencji organów | [`_index`](./research/instytucje/_index.md) |

## Szablony pism — `szablony/`

Reużywalne wzory pism. Zobacz `szablony/<obszar>/` — lista pojawi się po ekstrakcji z research'u.

## Kampanie — katalogi inicjatyw

| Inicjatywa | Opis | CLAUDE.md |
|---|---|---|
| [`dabrowskiego/`](./dabrowskiego/) | ul. Dąbrowskiego (Jeżyce) — hałas tramwajowy | [`dabrowskiego/CLAUDE.md`](./dabrowskiego/CLAUDE.md) |

## Meta

- [`CLAUDE.md`](./CLAUDE.md) — konwencje dla Claude Code (obowiązkowy)
- [`research/prompty/`](./research/prompty/) — briefy 01–07 dla top 1% ekspertów
- `MEMORY.md` — auto-memory Claude Code (gdy aktywne)

## Konwencje (skrót)

- **Nazwy plików**: polski kebab-case, **bez polskich znaków i spacji**
- **Język treści**: polski
- **Rozmiar pliku**: ≤ 12 KB (cel), twardy limit ~40 KB
- **Dokumenty źródłowe** = gęsty styl, bez uprzejmości
- **Pisma urzędowe** = pełny protokół (w `<inicjatywa>/pisma/`)
- **Bez wiki-links** — tylko markdown relative

Pełne konwencje: [`CLAUDE.md`](./CLAUDE.md).
