"""Smoke-aerosol adapters: SAME (PSI-102), SAME-R (PSI-101).

These heat (age) material samples to produce smoke — not flames. They share
the flow axis with the combustion tables but sit in their own geometry class
so no query compares them with a flame.
"""

from __future__ import annotations

import re

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
        runs.append(run)
        rep.runs_emitted += 1
    return runs


ADAPTERS = [same, same_r]
