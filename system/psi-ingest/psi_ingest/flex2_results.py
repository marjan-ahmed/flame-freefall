"""Attach as-run FLEX-2 per-burn outcomes from the FLEX-team cool-flame papers.

The PSI-68 experimental table is a planned envelope — one row per fuel with
identical swept ranges and no result columns — so a literature-reported burn
can only attach to that fuel's envelope record. The burn identifiers (R377,
R694, ...) exist only in the cited papers; they are NOT record-identity
evidence, and every joined outcome's note says so.

Each governed table row's values must appear in the paper's own text (the
verified extraction), checked here as close-range fragments per test — the
BRE pattern: changing a value or joining a different test fails closed at
ingest. Numbers the papers print but that do not stand up as written (R383's
diluent summing beyond 100%) are carried verbatim and documented in the
governed doc's open questions, never silently cleaned.
"""

from __future__ import annotations

import re

from . import knowledge
from .adapters import Ctx
from .model import Run
from .units import parse_measure

DOC = "knowledge/investigations/droplet-combustion/flex-2-cool-flame-results"
SOURCE_ID = "flex-2-cool-flame-2014"
TABLE_HEADING = "Per-burn results (2014 paper"
EXTRACTION = "psi-data/derived/report-extractions/FLEX-2 Cool-flame Extinction N-Alkane Droplets.md"

# governed-table Fuel cell → envelope record's exact fuel_family value.
ENVELOPE_FAMILY = {"n-decane": "n-decane", "n-octane": "n-octane", "n-heptane": "n-heptane"}

# Every fragment is folded (lowercase, whitespace-collapsed) and must appear in
# the extraction; every numeric governed-table cell of the same test must be
# contained in this test's fragments' text.
GUARDS = {
    "R377": ["Figure 1a (R377)", "initial diameter of 4.03 mm", "at 0.5 atm pressure", "were found to be 0.41 and 0.33 mm2/s"],
    "R374": ["Figure 1b (R374)", "for a 3.79 mm n-decane droplet", "oxygen concentration of 25%", "nitrogen at 0.5 atm", "rate constant was 0.52 mm2/s", "micro-explodes 26 seconds after ignition"],
    "R379": ["Fig. 1c (R379)", "3.86 mm", "17%O2 and 83%N2 mixture at 0.5 atm", "extinction occurs at 7 seconds", "0.31 and 0.27 mm2/s"],
    "R383": ["(d) R383 D0=3.14 mm, 14%O2 and 96%N2", "burning at 0.5 atm pressure", "0.29 and 0.25 mm2/s"],
    "R298": ["Test R298", "D0= 3.6 mm", "0.21:0.79", "burning rates of 0.48 and 0.38 mm2/s", "cool flame extinction occurring at 30.5 seconds", "at one atmospheric pressure"],
    "R694": ["In test R694", "D0 was 3.37 mm", "0.54 and 0.43 mm2/s", "at one atmospheric pressure"],
    "R698": ["test R698 which had D0= 3.6 mm", "0.63 and 0.53 mm2/s", "at one atmospheric pressure"],
}

K_COLUMNS = (("Hot-flame K (mm2/s)", "burning_rate_k_hot"), ("Cool-flame K (mm2/s)", "burning_rate_k_cool"))


def _fold(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def merge_flex2_literature(ctx: Ctx, runs: list[Run], *, include_review: bool = False) -> None:
    """Join the governed per-burn table onto the matching PSI-68 envelope records.

    Fails closed: a row whose test lacks paper-guard fragments, whose numbers
    are not in those fragments, or whose fuel has no unique envelope record
    aborts the ingest rather than joining silently.
    """
    citation = knowledge.citation(ctx.repo_root, DOC, SOURCE_ID)
    if citation["doc_status"] != "stable" and not include_review:
        ctx.note("flex-2", "Cool-flame literature supplement is awaiting owner approval; "
                 "draft outcomes are excluded from serving data.")
        return
    folded_extraction = _fold((ctx.repo_root / EXTRACTION).read_text(encoding="utf-8")).lower()
    _, table_rows, _ = knowledge.table_under(ctx.repo_root, DOC, TABLE_HEADING)
    envelopes = [r for r in runs if r.investigation == "flex-2"]

    joined_tests = []
    for row in table_rows:
        test = row["Test"].strip()
        cells = [(row[col].strip(), col, quantity) for col, quantity in K_COLUMNS
                 if not row[col].strip().lower().startswith("not stated")]
        if not cells:
            continue
        guards = GUARDS.get(test)
        if guards is None:
            raise ValueError(f"{DOC}: no paper guards for {test!r}")
        for fragment in guards:
            if _fold(fragment).lower() not in folded_extraction:
                raise ValueError(f"{DOC}: guard fragment not found: {fragment!r}")
        guarded = _fold(" ".join(guards)).lower()
        # Preserve the paper's first/second-stage order. Token membership
        # alone would also accept swapped hot/cool rates from the same burn.
        pair = re.search(r"(\d+\.\d+) and (\d+\.\d+) mm2/s", guarded)
        single = re.search(r"rate constant was (\d+\.\d+) mm2/s", guarded)
        rates = list(pair.groups()) if pair else [single.group(1)] if single else []
        for index, (column, _) in enumerate(K_COLUMNS):
            cell = row[column].strip()
            if index < len(rates):
                if cell != rates[index]:
                    raise ValueError(f"{DOC}: {test}: numeric cell for stage {column} differs from paper")
            elif not cell.lower().startswith("not stated"):
                raise ValueError(f"{DOC}: {test}: numeric cell for stage {column} has no paper rate")
        for value in [row["D\u2080 (mm)"].strip(), *(cell for cell, _, _ in cells)]:
            if not re.search(r"(?<![\d.])" + re.escape(value) + r"(?![\d.])", guarded):
                raise ValueError(f"{DOC}: {test}: numeric cell {value!r} absent from paper guards")
        pressure = row["Pressure (atm)"].strip()
        pressure_guard = {"0.5": "0.5 atm", "1.0": "one atmospheric pressure"}.get(pressure)
        if pressure_guard is None or pressure_guard not in guarded:
            raise ValueError(f"{DOC}: {test}: pressure {pressure!r} absent from paper guards")
        family = ENVELOPE_FAMILY.get(row["Fuel"].strip())
        expected_family = "n-decane" if test in {"R377", "R374", "R379", "R383"} else "n-octane"
        if family != expected_family:
            raise ValueError(f"{DOC}: {test}: fuel differs from the paper's test identity")
        candidates = [r for r in envelopes if r.granularity == "envelope" and family is not None
                      and (r.conditions.get("fuel_family") or {}).get("value") == family]
        if len(candidates) != 1:
            raise ValueError(f"{DOC}: {test}: expected one envelope for {family!r}, found {len(candidates)}")
        parsed = []
        for cell, column, quantity in cells:
            measure = parse_measure(cell, "mm\u00b2/s")
            if measure is None or not measure.usable:
                raise ValueError(f"{DOC}: {test}: invalid rate {cell!r}")
            parsed.append((quantity, measure))
        run = candidates[0]
        src = len(run.sources)
        quote = " | ".join(guards)
        run.sources.append({"kind": "report", "table": f"Per-burn results ({test})",
                            **citation,
                            "line": row["__line__"], "via": EXTRACTION, "quote": quote,
                            "descriptor": "NASA NTRS citation 20140006750 (free download)"})
        run.raw.append({**{k: v for k, v in row.items() if k != "__line__"},
                        "watched_sentence": quote})
        note = (f"FLEX-2 burn {test} ({row['D\u2080 (mm)']} mm, "
                f"{row['Atmosphere (as printed)']}, {pressure} atm). {row['Stage events']} "
                "Attached to this planned PSI-68 envelope by exact fuel identity; the burn itself "
                "is a literature-identified test (Nayagam et al. 2014), not a PSI-68 row.")
        if test == "R383":
            note += " Printed atmosphere sums beyond 100%; retained as printed, not corrected."
        for quantity, measure in parsed:
            run.outcome(quantity, measure, source=src, note=note)
        joined_tests.append(test)
    if joined_tests:
        ctx.note("flex-2", "Literature-identified burns attached by exact fuel identity to planned "
                 "PSI-68 envelopes; not additional PSI tests. Envelope conditions are unchanged.")
