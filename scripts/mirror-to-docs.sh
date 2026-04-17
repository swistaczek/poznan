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
echo "✓ Mirrored repo → docs/ ($COUNT plików)"
