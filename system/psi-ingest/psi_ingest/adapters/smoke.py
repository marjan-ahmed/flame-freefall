"""Smoke-aerosol adapters: SAME (PSI-102), SAME-R (PSI-101).

These heat (age) material samples to produce smoke — not flames. They share
the flow axis with the combustion tables but sit in their own geometry class
so no query compares them with a flame.
"""

from __future__ import annotations

import re
from collections import defaultdict
from urllib.parse import quote

from .. import fuels
from ..model import Run, cat, psi_source
from ..units import parse_measure, text
from . import Ctx, blank, raw_of, read_csv

MICROGRAVITY = cat("microgravity")


def same(ctx: Ctx) -> list[Run]:
    inv, name = "same", "PSI-102_Experimental table_SAME.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        if blank(row):
            rep.skip(line, "blank row")
            continue
        material_cell = text(row["Sample Material"]) or ""
        material = material_cell.split(":")[0].strip()
        run = Run(inv, f"Sample {row['Sample #'].strip()}")
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        run.set("fuel", cat(material, material_cell))
        run.set("fuel_family", cat(fuels.family(material)))
        m = re.search(r"same conditions as (\d+-\d+)", material_cell, re.I)
        if m:
            # The source says the conditions repeat samples 1-4 but doesn't
            # restate them; they are NOT copied in (samples 1-4 differ from
            # each other, so "the same" is not one value).
            run.notes.append(f"source: 'same conditions as {m.group(1)}' — conditions not restated per sample")
        run.set("flow_cm_s", parse_measure(row["Air Flow (cm/s)"], "cm/s"))
        run.set("aging_duration_min", parse_measure(row["Aging Duration (minutes)"], "min"))
        run.outcome("weight_loss_rate", parse_measure(row["Weight loss rate (mg/min)"], "mg/min"))
        runs.append(run)
        rep.runs_emitted += 1
    return runs


def same_r(ctx: Ctx) -> list[Run]:
    inv, name = "same-r", "PSI-101_Experimental table_SAME-R.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        if blank(row):
            rep.skip(line, "blank row")
            continue
        run = Run(inv, f"SAME #{row['SAME Test #'].strip()}")
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        material = text(row["Sample Type"])
        run.set("fuel", cat(material))
        run.set("fuel_family", cat(fuels.family(material)))
        run.set("description", cat(text(row["Description"])))
        run.set("date_as_written", cat(text(row["Date"]), basis="day-month only; the table gives no year"))
        run.set("flow_cm_s", parse_measure(row["Inlet velocity (cm/s)"], "cm/s"))
        run.set("rt_r0", parse_measure(row["Rt/R0"]))
        run.set("duration_s", parse_measure(row["Duration (sec)"], "s"))
        run.set("primary_aging_s", parse_measure(row["Primary aging time (sec)"], "s"))
        run.set("primary_mixing_s", parse_measure(row["Primary mixing time (sec)"], "s"))
        run.set("net_aging_s", parse_measure(row["Net aging time (sec)"], "s"))
        source_label = row["SAME Test #"].strip()
        match = re.fullmatch(r"(\d+)([a-z]*)", source_label, re.I)
        description = text(row["Description"]) or ""
        role = "unaged" if re.search(r"\bunaged\b", description, re.I) else "aged" if re.search(r"\baged\b", description, re.I) and not re.search(r"\b(?:not|non)[ -]+aged\b", description, re.I) else "unspecified"
        run.observation_relationship = {
            "method_version": "same-r-source-identifiers-v1",
            "basis": "source identifier grouping; not a claim of independent experiments or replicates",
            "source": 0, "source_field": "SAME Test #", "source_label": source_label,
            "description": description, "role": role, "role_basis": "explicit Description text only; suffixes do not establish aging",
            "base_test_number": match.group(1) if match else None,
            "material": material, "group_id": None, "independence": "unknown",
            "status": "ambiguous_identifier", "related_source_labels": [],
        }
        runs.append(run)
        rep.runs_emitted += 1
    link_same_r_identifiers(runs)
    return runs


def link_same_r_identifiers(runs: list[Run]) -> None:
    """Group exact source labels conservatively, retaining every observation.

    A letter suffix is stripped only to form an explicitly derived identifier
    stem. It supplies neither an aging label nor proof of a shared specimen.
    Cross-material stems and duplicate full labels are unresolved, never joined.
    """
    groups = defaultdict(list)
    for run in runs:
        relation = run.observation_relationship
        if relation and relation["base_test_number"] is not None:
            groups[relation["base_test_number"]].append(run)
    for stem, members in groups.items():
        materials = {(r.conditions.get("fuel") or {}).get("value") for r in members}
        labels = [r.observation_relationship["source_label"] for r in members]
        ambiguous = len(materials) != 1 or None in materials or len(labels) != len(set(labels))
        for run in members:
            relation = run.observation_relationship
            relation["status"] = "ambiguous_identifier" if ambiguous else "identifier_grouped"
            relation["group_id"] = None if ambiguous else f"same-r:source-test:{quote(str(relation['material']), safe='')}:{stem}"
            relation["related_source_labels"] = [] if ambiguous else sorted(labels)
            if ambiguous:
                run.notes.append("SAME-R identifier relationship unresolved: repeated labels or materials share this numeric stem; observations were not joined.")


ADAPTERS = [same, same_r]
