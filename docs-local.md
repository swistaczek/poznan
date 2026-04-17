# Lokalny podgląd strony

Strona publikowana jest automatycznie na `https://swistaczek.github.io/poznan/` po każdym pushu na `main` (workflow `.github/workflows/gh-pages.yml`).

Do lokalnego podglądu (optional — służy autorom, nie wymagany do edycji treści):

## Wymagania

- Python 3.12+ (wersja identyczna jak w CI).
- `pip`.

## Uruchomienie

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt

# Mirror treści repo do docs/ (MkDocs wymaga docs_dir jako podkatalog):
./scripts/mirror-to-docs.sh

mkdocs serve
```

Otwórz `http://127.0.0.1:8000/poznan/`.

> [!TIP]
> Po każdej edycji pliku źródłowego: ponownie `./scripts/mirror-to-docs.sh`
> (mkdocs serve nie obserwuje zmian poza `docs/`). Alternatywa: edytuj
> wprost w `docs/` dla szybkiego preview, potem przepisz do root.

## Build produkcyjny (jak w CI)

```bash
./scripts/mirror-to-docs.sh
mkdocs build --strict
```

Wynik: katalog `_site/` (wykluczony z gita przez `.gitignore`).

## Najczęstsze problemy

| Problem | Rozwiązanie |
|---|---|
| Błąd `Config value 'plugins': The 'awesome-pages' plugin is not installed` | `pip install -r requirements-docs.txt` |
| Build strict fail: „documentation file not found in any subdirectory" | plik odwołuje się do nieistniejącej ścieżki; popraw link markdown albo dodaj plik |
| Polskie znaki w URL | nie używaj polskich znaków ani spacji w nazwach plików — patrz `CLAUDE.md` |
| Dziwna kolejność w menu | edytuj odpowiedni plik `.pages` w danym katalogu |

## Struktura konfiguracji

- [`mkdocs.yml`](./mkdocs.yml) — globalna konfiguracja (theme, pluginy, exclude_docs).
- `.pages` w każdym kluczowym katalogu — lokalny porządek nawigacji (plugin `awesome-pages`).
- [`requirements-docs.txt`](./requirements-docs.txt) — wersje pluginów (lockowane major).
- [`.github/workflows/gh-pages.yml`](./.github/workflows/gh-pages.yml) — CI.

## Możliwe rozszerzenia

- **Custom CSS** (`docs_overrides/` + `theme.custom_dir`) — większa czcionka, lepsze tabele, civic aesthetic. Obecnie wyłączone.
- **git-revision-date-localized** — pokazuje datę ostatniej modyfikacji na dole każdej strony. Odkomentuj w `mkdocs.yml` i `requirements-docs.txt`.
- **minify** — redukcja rozmiaru HTML/CSS/JS. Jak wyżej.
- **custom domain** (np. `poznan.obywatelski.pl`) — dodaj `CNAME` do repo i w GitHub Pages ustaw domenę.
