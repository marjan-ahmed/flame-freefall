"""Refuse any extracted report value whose verbatim text is not in its source.

The same idea as .agents/skills/add-sources/verify.mjs, applied to the
extraction CSV: the converted report text is the ground truth, and a value
that cannot be found there — typed in, "cleaned up", or copied from memory —
does not enter the run table.
"""

from __future__ import annotations

import csv
import re
from html.parser import HTMLParser
from pathlib import Path


class ExtractionNotVerified(ValueError):
    pass


class _HTMLRows(HTMLParser):
    """Read saved extraction table cells, preserving empty columns and row identity."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows = []
        self.row = None
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.cell = []
        elif tag == "br" and self.cell is not None:
            self.cell.append(" ")

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.cell is not None:
            if self.row is not None:
                self.row.append(_norm("".join(self.cell)))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def verify_html_rows(repo_root: Path, extraction: str, columns: list[str], rows: list[dict]) -> None:
    """Require each governed row to match a unique full row in the extraction.

    Empty source cells correspond to the governed table's em dash. This tests
    the identity, material, units-bearing column positions and values together;
    finding the same numeric token elsewhere in the paper is insufficient.
    """
    parser = _HTMLRows()
    parser.feed((repo_root / extraction).read_text(encoding="utf-8"))
    for row in rows:
        expected = [_norm(row[c]) if row[c].strip() != "\u2014" else "" for c in columns]
        matches = [r for r in parser.rows if r == expected]
        if len(matches) != 1:
            raise ExtractionNotVerified(f"{extraction}: {expected[0]} has {len(matches)} exact source rows")


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("<br/>", " ")).strip()


def load_verified(repo_root: Path, path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    sources: dict[str, str] = {}
    bad = []
    for i, r in enumerate(rows, start=2):
        src = r["source_file"]
        if src not in sources:
            sources[src] = _norm((repo_root / src).read_text(encoding="utf-8"))
        verbatim = _norm(r["verbatim"])
        if not verbatim or verbatim not in sources[src]:
            bad.append(f"line {i}: {r['run_label']} {r['field']} — verbatim text not found in {src}")
        elif r["field"] != "observation" and r["value"].lower() not in verbatim.lower():
            bad.append(f"line {i}: {r['run_label']} {r['field']} — value {r['value']!r} is not in its verbatim cell")
    if bad:
        raise ExtractionNotVerified(f"{path.name}: {len(bad)} unverified rows\n  " + "\n  ".join(bad[:20]))
    return rows
