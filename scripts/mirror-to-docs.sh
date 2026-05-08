#!/usr/bin/env bash
# Mirror root do docs/ dla buildu MkDocs.
#
# MkDocs wymaga by docs_dir był podkatalogiem. Repo trzyma treść na płaskim
# root-level (dla aktywisty, Claude Code, GitHub UI). Ten skrypt odtwarza
# zawartość repo w docs/ przed buildem.
#
# Wywołanie: `./scripts/mirror-to-docs.sh` (z root repo lub dowolnego miejsca).
# Używane przez: CI (`.github/workflows/gh-pages.yml`) i lokalnie przez autorów
# przed `mkdocs serve` / `mkdocs build`.
#
# SEO:
#   1. Per-file mtime ustawiany z git log → MkDocs sitemap dostaje sensowny
#      lastmod na URL (zamiast jednolitej build-date).
#   2. Sekcja "Ostatnie zmiany" w README.md auto-generowana — crawlery
#      Google/Bing widzą swieze linki na home page.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

rm -rf docs
mkdir -p docs

rsync -a \
  --exclude='/docs/' \
  --exclude='/_site/' \
  --exclude='/.git/' \
  --exclude='/.github/' \
  --exclude='/.claude/' \
  --exclude='.venv*/' \
  --exclude='venv/' \
  --exclude='env/' \
  --exclude='__pycache__/' \
  --exclude='*.pyc' \
  --exclude='/node_modules/' \
  --exclude='/scripts/' \
  --exclude='/overrides/' \
  --exclude='/mkdocs.yml' \
  --exclude='/requirements-docs.txt' \
  --exclude='.DS_Store' \
  ./ docs/

COUNT=$(find docs -type f | wc -l | tr -d ' ')
echo "Mirrored repo -> docs/ ($COUNT plikow)"

# ---------------------------------------------------------------------------
# 1. Per-file mtime z git log (poprawne <lastmod> w sitemap.xml)
#
# git log -1 --format=%ct <path> zwraca Unix timestamp ostatniego commita
# dotyczacego pliku. Iterujemy po `git ls-files` (tylko pliki tracked).
# ---------------------------------------------------------------------------
echo "Ustawiam mtime plikow z git log..."
SET_COUNT=0
SKIPPED=0
while IFS= read -r FILE; do
  if [[ ! -f "docs/$FILE" ]]; then
    SKIPPED=$((SKIPPED+1))
    continue
  fi
  TS=$(git log -1 --format=%ct -- "$FILE" 2>/dev/null || true)
  [[ -n "$TS" ]] || continue
  # GNU touch (Linux CI): -d "@<unix>"; BSD touch (macOS): -t YYYYMMDDhhmm.SS
  if ! touch -d "@$TS" "docs/$FILE" 2>/dev/null; then
    touch -t "$(date -r "$TS" '+%Y%m%d%H%M.%S')" "docs/$FILE"
  fi
  SET_COUNT=$((SET_COUNT+1))
done < <(git ls-files)
echo "mtime ustawiony dla $SET_COUNT plikow (pominieto $SKIPPED nie-mirrorowanych)"

# ---------------------------------------------------------------------------
# 2. Sekcja "Ostatnie zmiany" w README.md (auto-generated)
#
# Top 30 ostatnio zmienionych .md z git log. Pomija indexy, CLAUDE.md,
# rejestry pism i prompty. Wstawia liste miedzy markery
# najnowsze:start/end w docs/README.md.
# ---------------------------------------------------------------------------
echo "Generuje sekcje 'Ostatnie zmiany'..."

NAJNOWSZE_RAW=$(mktemp)
NAJNOWSZE_TOP=$(mktemp)
SNIPPET_FILE=$(mktemp)

# git log: name-only z ISO date jako commit header
git log --name-only --format='COMMITDATE %cI' --no-merges -- '*.md' > "$NAJNOWSZE_RAW"

# AWK: grupuj po commicie, dla kazdego .md path zapisz pierwsza (najswiezszą)
# wystapienie z odpowiednia data.
NAJNOWSZE_FULL=$(mktemp)
awk '
  /^COMMITDATE / { date = substr($0, 12); next }
  /\.md$/ {
    path = $0
    if (path ~ /(^|\/)(CLAUDE|MEMORY|README|TODO)\.md$/) next
    if (path ~ /^\.claude\//) next
    if (path ~ /^research\/prompty\//) next
    if (path ~ /\/pisma\/REJESTR\.md$/) next
    if (!seen[path]++) print date " " path
  }
' "$NAJNOWSZE_RAW" > "$NAJNOWSZE_FULL"
head -30 "$NAJNOWSZE_FULL" > "$NAJNOWSZE_TOP"
rm -f "$NAJNOWSZE_FULL"

{
  echo "<!-- najnowsze:start -->"
  echo
  while IFS=' ' read -r DATE PATH_; do
    [[ -n "$PATH_" ]] || continue
    [[ -f "$PATH_" ]] || continue  # rename/delete safety

    # Tytul: pierwszy '# H1' z pliku, fallback do basename
    TITLE=$(grep -m1 -E '^#[[:space:]]+' "$PATH_" 2>/dev/null | sed -E 's/^#[[:space:]]+//; s/[[:space:]]+$//' || true)
    if [[ -z "$TITLE" ]]; then
      TITLE=$(basename "$PATH_" .md)
    fi

    DIR=$(dirname "$PATH_")
    [[ "$DIR" == "." ]] && DIR="(root)"

    SHORT_DATE="${DATE:0:10}"
    TITLE_SAFE="${TITLE//|/\\|}"

    echo "- **${SHORT_DATE}** [${TITLE_SAFE}](./${PATH_}) <small>kat. \`${DIR}\`</small>"
  done < "$NAJNOWSZE_TOP"
  echo
  echo "<!-- najnowsze:end -->"
} > "$SNIPPET_FILE"

# Podmien blok miedzy markerami w docs/README.md
README_DOCS="docs/README.md"
if [[ -f "$README_DOCS" ]] && grep -q "najnowsze:start" "$README_DOCS"; then
  TMP_README=$(mktemp)
  awk -v snippet="$SNIPPET_FILE" '
    BEGIN { skip=0 }
    /<!-- najnowsze:start -->/ {
      while ((getline line < snippet) > 0) print line
      close(snippet)
      skip=1
      next
    }
    /<!-- najnowsze:end -->/ { skip=0; next }
    skip==0 { print }
  ' "$README_DOCS" > "$TMP_README"
  mv "$TMP_README" "$README_DOCS"
  LINES=$(wc -l < "$SNIPPET_FILE" | tr -d ' ')
  echo "docs/README.md zaktualizowany ($LINES linii w sekcji)"
else
  echo "Nie znaleziono markerow najnowsze:start/end w $README_DOCS"
fi

# Po podmianie - odswiez mtime README na najnowsza date commita
README_TS=$(git log -1 --format=%ct -- README.md 2>/dev/null || true)
if [[ -n "$README_TS" ]]; then
  if ! touch -d "@$README_TS" "$README_DOCS" 2>/dev/null; then
    touch -t "$(date -r "$README_TS" '+%Y%m%d%H%M.%S')" "$README_DOCS"
  fi
fi

rm -f "$NAJNOWSZE_RAW" "$NAJNOWSZE_TOP" "$SNIPPET_FILE"

echo "SEO post-processing zakonczony"
