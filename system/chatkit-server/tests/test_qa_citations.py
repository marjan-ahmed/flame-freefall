"""Citation-integrity checks from the citation-verifier QA audit (2026-09-27).

Two kinds of test live here:
- guards that pass today and pin behaviour the audit verified (every run
  citation resolves to a real source; every source conflict cites both sides);
- xfail(strict=True) tests that pin CONFIRMED defects. They "pass" as xfail
  while the defect exists and turn into a hard failure (XPASS) once it is
  fixed, which is the signal to delete the marker.
"""

import csv
import json
import re
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

REPO_ROOT = Path(__file__).resolve().parents[3]
RUNS = json.loads((REPO_ROOT / "system/chatkit-server/data/runs.json").read_text(encoding="utf-8"))["runs"]


def _frontmatter(doc_id: str) -> dict:
    text = (REPO_ROOT / (doc_id + ".md")).read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


def _norm_header(h: str) -> str:
    return re.sub(r"\s+", " ", h.replace("﻿", "")).strip()


# -- guards (pass today) ------------------------------------------------------

def test_every_report_citation_resolves_to_its_docs_sources_entry():
    for r in RUNS:
        for s in r["sources"]:
            if s["kind"] != "report" or not s.get("doc"):
                continue
            fm = _frontmatter(s["doc"])
            entry = next((x for x in fm.get("sources") or [] if x["id"] == s["source_id"]), None)
            assert entry is not None, f"{r['id']}: {s['doc']} has no source {s['source_id']!r}"
            assert entry.get("title") == s["title"], f"{r['id']}: title drifted from {s['doc']} frontmatter"
            url = entry["resource"] if entry["resource"].startswith(("http://", "https://")) else None
            assert url == s["url"], f"{r['id']}: url drifted from {s['doc']} frontmatter"
            assert fm.get("status") == "stable", f"{r['id']}: cites non-stable doc {s['doc']}"
            if s.get("line"):
                line = (REPO_ROOT / (s["doc"] + ".md")).read_text(encoding="utf-8").splitlines()[s["line"] - 1]
                assert line.lstrip().startswith("|"), f"{r['id']}: line {s['line']} of {s['doc']} is not a table row"


def test_every_psi_citation_points_at_the_row_holding_its_raw_cells():
    cache: dict[str, list[list[str]]] = {}
    for r in RUNS:
        for i, s in enumerate(r["sources"]):
            if s["kind"] != "psi":
                continue
            path = REPO_ROOT / "psi-data/raw/csvs" / s["file"]
            assert path.is_file(), f"{r['id']}: missing PSI file {s['file']}"
            if s["file"] not in cache:
                with path.open(encoding="utf-8-sig", errors="replace", newline="") as fh:
                    cache[s["file"]] = list(csv.reader(fh))
            rows = cache[s["file"]]
            assert 2 <= s["row"] <= len(rows), f"{r['id']}: row {s['row']} out of range for {s['file']}"
            cells = {_norm_header(h): v for h, v in zip(rows[0], rows[s["row"] - 1])}
            for k, v in r["raw"][i].items():
                nk = _norm_header(k)
                if nk in cells and "�" not in cells[nk]:
                    assert cells[nk].strip() == str(v).strip(), f"{r['id']}: {k!r} is not at {s['file']} line {s['row']}"


def test_every_conflict_cites_both_disagreeing_sources():
    for r in RUNS:
        for c in r.get("conflicts", []):
            idx = {v["source"] for v in c["values"]}
            assert len(idx) >= 2, f"{r['id']}: conflict on {c['field']} names fewer than two sources"
            for j in idx:
                assert 0 <= j < len(r["sources"]), f"{r['id']}: conflict cites missing source {j}"


# -- confirmed defects (xfail strict) -----------------------------------------

# Fixed: commit 899b48f had left saffire_table_i()'s results loop as dead code
# after `return False` in _is_note_marker(). Now a plain regression test.
def test_saffire_table_i_results_are_merged_and_cited():
    with_conditions = [r for r in RUNS if r["investigation"] in ("saffire-1", "saffire-2")
                       and any(s.get("table") == "Table I (conditions)" for s in r["sources"])]
    assert with_conditions
    missing = [r["id"] for r in with_conditions
               if not any(s.get("table") == "Table I (ignition and results)" for s in r["sources"])]
    assert not missing, f"no Table I (ignition and results) citation on {missing}"


def test_instance_scope_does_not_disclaim_investigations_the_record_publishes():
    body = (REPO_ROOT / "instance.md").read_text(encoding="utf-8").split("---", 2)[2]
    m = re.search(r"does not\s+cover other PSI-catalogued investigations[^)]*\(e\.g\.([^)]*)\)", body)
    disclaimed = {n.strip().lower() for n in m.group(1).split(",")} if m else set()
    published = set()
    for p in (REPO_ROOT / "knowledge/investigations").rglob("*.md"):
        if p.name == "index.md" or p.name.endswith(".summary.md"):
            continue
        fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
        if fm.get("status") == "stable":
            published.add(p.stem.lower())
    assert not (disclaimed & published), f"instance.md disclaims published docs: {sorted(disclaimed & published)}"
