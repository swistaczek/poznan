"""MkDocs hook: per-page git lastmod dla sitemap.xml.

Problem: docs/ jest gitignored mirrorem root repo (patrz scripts/mirror-to-docs.sh),
więc plugin git-revision-date-localized nie znajduje historii. MkDocs domyślnie
używa build_date dla wszystkich URL — sitemap traci sygnał świeżości.

Rozwiązanie: hook czyta `git log -1 --format=%cs <oryginalna ścieżka>` w katalogu
ROOT repo (nie docs/) i nadpisuje `page.update_date`. MkDocs sitemap.xml template
({{ page.update_date }}) generuje wtedy poprawne <lastmod>YYYY-MM-DD</lastmod>
per URL.

Aktywacja: w mkdocs.yml dodaj `hooks: [scripts/hooks_seo.py]`.
"""

from __future__ import annotations

import subprocess
from functools import lru_cache
from pathlib import Path

# Cache: jeden subprocess na plik na cały build (~400 plików = 400 git log calls,
# ale każdy <50ms). Cache zapobiega ponownym wywołaniom przy on_page_* multi-pass.
@lru_cache(maxsize=2048)
def _git_short_date(rel_path: str, repo_root: str) -> str | None:
    """Zwraca datę ostatniego commita pliku jako 'YYYY-MM-DD' lub None."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel_path],
            capture_output=True,
            text=True,
            cwd=repo_root,
            check=False,
            timeout=5,
        )
        date = result.stdout.strip()
        return date if date else None
    except (subprocess.SubprocessError, OSError):
        return None


def on_page_markdown(markdown, page, config, files):
    """Ustawia page.update_date z git log per-file (poprawne lastmod w sitemap)."""
    src_path = page.file.src_path  # np. "research/halas/index.md"

    # ROOT repo to katalog nadrzędny do docs_dir. mkdocs.yml jest w ROOT.
    repo_root = str(Path(config["config_file_path"]).parent)

    date = _git_short_date(src_path, repo_root)
    if date:
        page.update_date = date

    return markdown
