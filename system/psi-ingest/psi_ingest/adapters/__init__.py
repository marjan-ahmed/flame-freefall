"""One adapter per PSI source file. Each maps its own columns onto the
unified Run record and reports every row it read, emitted, or skipped (and
why) — the ingest report is how a row count is honestly stated."""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class FileReport:
    file: str
    investigation: str
    rows_read: int = 0
    runs_emitted: int = 0
    merged_into_previous: int = 0  # continuation rows folded into the run above them
    skipped: list[dict] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def skip(self, row: int, reason: str) -> None:
        self.skipped.append({"row": row, "reason": reason})

    def to_json(self) -> dict:
        return {
            "file": self.file,
            "investigation": self.investigation,
            "rows_read": self.rows_read,
            "runs_emitted": self.runs_emitted,
            "merged_into_previous": self.merged_into_previous,
            "skipped": self.skipped,
            "notes": self.notes,
        }


@dataclass
class Ctx:
    repo_root: Path
    raw_dir: Path
    registry: dict
    reports: list[FileReport] = field(default_factory=list)
    table_notes: dict[str, list[str]] = field(default_factory=dict)

    def psi_id(self, inv: str) -> str:
        return self.registry[inv]["psi_id"]

    def report(self, file: str, inv: str) -> FileReport:
        r = FileReport(file=file, investigation=inv)
        self.reports.append(r)
        return r

    def note(self, inv: str, text: str) -> None:
        self.table_notes.setdefault(inv, []).append(text)


def _clean_header(h: str) -> str:
    return re.sub(r"\s+", " ", h.replace("﻿", "")).strip()


def read_csv(ctx: Ctx, name: str) -> list[tuple[int, dict]]:
    """Rows as (1-based line number, {clean header: cell}). The header is
    line 1. Whitespace in headers is collapsed so ' XO2 before test' and
    'XO2  after test' are addressable; cells are left untouched."""
    path = ctx.raw_dir / "csvs" / name
    for enc in ("utf-8-sig", "cp1252"):
        try:
            with path.open(encoding=enc, newline="") as f:
                rows = list(csv.reader(f))
            break
        except UnicodeDecodeError:
            continue
    header = [_clean_header(h) for h in rows[0]]
    out = []
    for i, cells in enumerate(rows[1:], start=2):
        out.append((i, {h: (cells[j] if j < len(cells) else "") for j, h in enumerate(header)}))
    return out


def blank(row: dict) -> bool:
    return all(not str(v).strip() for v in row.values())


def raw_of(row: dict) -> dict:
    """The row as the source wrote it, empty cells dropped (they carry nothing)."""
    return {k: v for k, v in row.items() if str(v).strip()}


_DATE_FORMATS = ("%m/%d/%Y", "%m/%d/%y", "%d-%b-%y", "%Y-%b-%d", "%Y-%m-%d")


def iso_date(raw: str | None) -> str | None:
    if not raw:
        return None
    s = raw.strip()
    for fmt in _DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    return None


def yyddd(raw: str | None) -> str | None:
    """ACME's 'Test Day' — YYDDD, per the source's own note."""
    if not raw or not re.fullmatch(r"\d{5}", raw.strip()):
        return None
    s = raw.strip()
    try:
        return datetime.strptime(f"20{s[:2]}{s[2:]}", "%Y%j").date().isoformat()
    except ValueError:
        return None
