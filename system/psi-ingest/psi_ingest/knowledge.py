"""Read the governed record (knowledge/) — frontmatter citations and the
per-test tables the documents reproduce verbatim from their NASA reports.

This is a READ of the record, never a write: the record survives the
system, and nothing here changes it. A table is located by the heading text
above it, so a reworded heading fails loudly (TableNotFound) instead of
silently ingesting the wrong table.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml


class TableNotFound(LookupError):
    pass


def _split(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def doc_path(repo_root: Path, doc_id: str) -> Path:
    return repo_root / f"{doc_id}.md"


def citation(repo_root: Path, doc_id: str, source_id: str | None) -> dict:
    """The document's own `sources[]` entry for `source_id` (id, title,
    resource) plus the document's title and status — the whole citation, read
    from its one home."""
    fm, _ = _split(doc_path(repo_root, doc_id))
    out = {"doc": doc_id, "doc_title": fm.get("title"), "doc_status": fm.get("status")}
    if source_id:
        for s in fm.get("sources") or []:
            if s.get("id") == source_id:
                out.update(source_id=s["id"], title=s.get("title"), url=s.get("resource"))
                break
        else:
            raise LookupError(f"{doc_id} declares no source {source_id!r}")
    return out


def _cells(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def table_under(repo_root: Path, doc_id: str, heading: str) -> tuple[list[str], list[dict], int]:
    """The first GFM table after the heading whose text starts with `heading`.
    Returns (columns, rows, 1-based line number of the header row)."""
    _, body = _split(doc_path(repo_root, doc_id))
    full = doc_path(repo_root, doc_id).read_text(encoding="utf-8").splitlines()
    offset = len(full) - len(body.splitlines())
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^#{2,6}\s", line) and line.lstrip("#").strip().startswith(heading):
            start = i
            break
    if start is None:
        raise TableNotFound(f"{doc_id}: no heading starting {heading!r}")
    i = start + 1
    while i < len(lines) and not lines[i].lstrip().startswith("|"):
        if re.match(r"^#{2,6}\s", lines[i]):
            raise TableNotFound(f"{doc_id}: heading {heading!r} has no table before the next heading")
        i += 1
    if i >= len(lines):
        raise TableNotFound(f"{doc_id}: heading {heading!r} has no table")
    header_line = i
    columns = _cells(lines[i])
    rows: list[dict] = []
    i += 2  # skip the --- separator row
    while i < len(lines) and lines[i].lstrip().startswith("|"):
        cells = _cells(lines[i])
        row = dict(zip(columns, cells))
        row["__line__"] = offset + i + 1
        rows.append(row)
        i += 1
    return columns, rows, offset + header_line + 1
