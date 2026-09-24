"""Refuse any extracted report value whose verbatim text is not in its source.

The same idea as .agents/skills/add-sources/verify.mjs, applied to the
extraction CSV: the converted report text is the ground truth, and a value
that cannot be found there — typed in, "cleaned up", or copied from memory —
does not enter the run table.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


class ExtractionNotVerified(ValueError):
    pass


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
