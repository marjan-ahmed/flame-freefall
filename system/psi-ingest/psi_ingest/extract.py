"""`uv run psi-extract` — pull per-test values out of converted NASA report
text into psi-data/extracted/report-outcomes.csv.

This is Step 5's first half: extraction writes a reviewable CSV, one row per
(test, field), each carrying the report page and the VERBATIM cell text it came
from. It never interprets: a cell is copied, not paraphrased, and a table whose
column headers did not survive conversion contributes only the columns whose
meaning is unambiguous from their own content (a test id like "B1", a flow
direction word, the free-text observation), never a numeric column whose unit
or meaning would have to be guessed.

The second half — verification — is in verify.py and runs inside psi-ingest:
a row whose verbatim text is not literally present in its source file is
refused, so hand edits to the CSV cannot smuggle in a value.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT = REPO_ROOT / "psi-data" / "extracted" / "report-outcomes.csv"
COLUMNS = ["investigation", "run_label", "granularity", "field", "value", "qualifier", "source_file", "table", "page", "verbatim"]

BASS_II_TM = "investigation_reports/_converted/TM-20210011385.md"
BASS_II_TITLE_RE = re.compile(r"TABLE (A\.\d)\.")
PAGE_RE = re.compile(r"NASA/TM-20210011385 (\d+)")
TEST_ID_RE = re.compile(r"[BFPMOT]\d+[ab]?")
DIRECTIONS = {"opposed": "opposed", "concurrent": "concurrent", "stagnation": "stagnation"}


def cell_text(raw: str) -> str:
    return re.sub(r"\s+", " ", raw.replace("<br/>", " ")).strip()


def bass_ii_appendix_a(repo_root: Path = REPO_ROOT) -> list[dict]:
    """Tables A.1–A.6: one row per BASS-II test (126 tests, per the report)."""
    text = (repo_root / BASS_II_TM).read_text(encoding="utf-8")
    start = text.index("Appendix A.-Test Matrices")
    pages = [(m.start(), m.group(1)) for m in PAGE_RE.finditer(text)]
    titles = [(m.start(), m.group(1)) for m in BASS_II_TITLE_RE.finditer(text)]
    out: list[dict] = []
    for m in re.finditer(r"<tr>(.*?)</tr>", text[start:], re.S):
        pos = start + m.start()
        cells_raw = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", m.group(1), re.S)
        cells = [cell_text(c) for c in cells_raw]
        # Appendix rows are 31–32 columns wide with the test id 4th; the
        # 9-column rows are Table 5.1 (already in the governed record).
        if len(cells) < 30 or not TEST_ID_RE.fullmatch(cells[3]):
            continue
        page = next((p for off, p in pages if off > pos), "")
        table = next((f"Table {t}" for off, t in reversed(titles) if off < pos), "Appendix A")
        base = {"investigation": "bass-ii", "run_label": cells[3], "granularity": "", "qualifier": "",
                "source_file": BASS_II_TM, "table": table, "page": page}
        direction = DIRECTIONS.get(cells[7].lower())
        if direction:
            out.append({**base, "field": "flow_direction", "value": direction, "verbatim": cells[7]})
        observation = cells[-1]
        if observation and not re.fullmatch(r"[-–—\s]*", observation):
            out.append({**base, "field": "observation", "value": observation, "verbatim": observation})
    return out


def _html_tables_after(text: str, caption: str, occurrence: int = -1) -> list[list[str]]:
    """Rows (as cell lists) of the first HTML table after a caption."""
    starts = [m.start() for m in re.finditer(re.escape(caption), text)]
    if not starts:
        raise LookupError(f"caption not found: {caption!r}")
    seg = text[starts[occurrence]:]
    tb = re.search(r"<table>(.*?)</table>", seg, re.S)
    return [[cell_text(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)]
            for r in re.findall(r"<tr>(.*?)</tr>", tb.group(1), re.S)]


SPICE_REPORT = "psi-data/derived/report-extractions/SPICE Final Report 12_2_2012.md"
# Row label (as the converted table writes it) → field. Only rows whose label
# names the quantity and unit; Zst/Tad are computed, uf/Re derived, and the
# mass-flow row's symbol did not survive conversion — all left out.
SPICE_ROWS = {"d, mm": "nozzle_diameter_mm", "ua, cm/s": "flow_cm_s", "LSP, mm": "smoke_point_length",
              "# smoke": "smoke_points_observed"}


def spice_table_1(repo_root: Path = REPO_ROOT) -> list[dict]:
    """SPICE Table 1: smoke-point ranges per fuel — a per-fuel SUMMARY of many
    tests, not per-test values, and recorded with that granularity."""
    text = (repo_root / SPICE_REPORT).read_text(encoding="utf-8")
    rows = _html_tables_after(text, "Table 1.", 0)
    header = next(r for r in rows if r and r[0] == "Parameter")
    fuels = header[1:]
    out = []
    for r in rows:
        field = SPICE_ROWS.get(r[0]) if r else None
        if not field:
            continue
        for fuel, cell in zip(fuels, r[1:]):
            if cell:
                out.append({"investigation": "spice", "run_label": f"Smoke-point summary — {fuel}", "granularity": "summary",
                            "field": field, "value": cell, "qualifier": f"{fuel}; row '{r[0]}'",
                            "source_file": SPICE_REPORT, "table": "Table 1", "page": "", "verbatim": cell})
    for fuel in fuels:
        out.append({"investigation": "spice", "run_label": f"Smoke-point summary — {fuel}", "granularity": "summary",
                    "field": "fuel", "value": fuel, "qualifier": "", "source_file": SPICE_REPORT, "table": "Table 1",
                    "page": "", "verbatim": fuel})
    return out


SAMER_REPORT = "psi-data/derived/report-extractions/SAMER_Final 0602 2014.md"


def samer_table_2(repo_root: Path = REPO_ROOT) -> list[dict]:
    """SAME-R Table 2 (TEM vs moment method): per flight test, the sample
    temperature and the number of particles counted. The diameter columns'
    headers did not survive conversion intact, so they are not extracted."""
    text = (repo_root / SAMER_REPORT).read_text(encoding="utf-8")
    rows = _html_tables_after(text, "Table 2: Flight Data Comparison", 0)
    head = rows[0]
    if not (head[0] == "Sample" and head[1].startswith("Temperature") and "counted" in head[2]):
        raise LookupError("SAME-R Table 2 columns changed — refusing to extract")
    out = []
    for r in rows[1:]:
        m = re.match(r"(.+?) #(\d+) \(ISS\) (\w+)", r[0])
        t = re.search(r"(\d+(?:\.\d+)?)$", r[1])
        if not m or not t:
            continue
        base = {"investigation": "same-r", "run_label": f"SAME #{m.group(2)}", "granularity": "",
                "source_file": SAMER_REPORT, "table": "Table 2", "page": ""}
        out.append({**base, "field": "sample_temperature_c", "value": t.group(1), "qualifier": r[1], "verbatim": r[1]})
        out.append({**base, "field": "tem_particles_counted", "value": r[2], "qualifier": m.group(3).lower(), "verbatim": r[2]})
    return out


EXTRACTORS = [bass_ii_appendix_a, spice_table_1, samer_table_2]


def main() -> None:
    rows = [r for ex in EXTRACTORS for r in ex()]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    tests = {(r["investigation"], r["run_label"]) for r in rows}
    print(f"psi-extract: {len(rows)} values for {len(tests)} tests -> {OUT.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
