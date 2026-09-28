"""Solid-fuel adapters: BASS (PSI-26), BASS-II (PSI-25), SAFFIRE-1/2/3 (PSI-98/99/100)."""

from __future__ import annotations

import re

from .. import fuels
from ..model import Run, cat, psi_source
from ..units import Measure, parse_measure, pct, text, to_mm
from . import Ctx, blank, iso_date, raw_of, read_csv

MICROGRAVITY = cat("microgravity")

# Sourced bases for families the CSV text doesn't name (quotes are from the
# BASS-II Summary Report as reproduced in the governed bass-ii document).
_ROD_BASIS = 'BASS-II TM §1.2: "cast polymethylmethacrylate (PMMA) samples were shaped as rods of various diameters (6.35 to 12.7 mm)"'
_SPHERE_BASIS = 'BASS-II TM §1.2: PMMA samples were shaped as "a section of a 4-cm-diameter sphere"'
_FILM_BASIS = 'BASS-II TM §2.1 (Bhattacharjee): "Samples were 1- and 2-cm-wide thin films of plastic (PMMA)"'
_ROD_DIAMETERS_MM = {"1/4": 6.35, "3/8": 9.525, "1/2": 12.7, "0.5": 12.7}
_ROD_DIAMETER_BASIS = "BASS-II TM §4.1.1: rod diameters 6.35, 9.525, and 12.7 mm (1/4, 3/8, and 1/2 in.)"


def _geometry_from_text(run: Run, material: str) -> None:
    """Thickness / width / rod diameter / sides, where the material text states them."""
    t = material.lower()
    m = re.search(r"(\d+(?:\.\d+)?)\s*micron", t)
    if m:
        run.set("thickness_mm", Measure(raw=m.group(0), value=float(m.group(1)) / 1000, unit="mm", flags=["converted"]))
    else:
        m = re.search(r"(\d*\.?\d+)\s*mm(?:\s*thick)?", t)
        if m and "rod" not in t:
            v = float(m.group(1))
            run.set("thickness_mm", Measure(raw=m.group(0), value=v, min=v, max=v, unit="mm"))
    if "rod" in t:
        m = re.search(r"(1/4|3/8|1/2|0\.5)", t)
        if m:
            v = _ROD_DIAMETERS_MM[m.group(1)]
            run.set("diameter_mm", Measure(raw=m.group(0) + " in", value=v, min=v, max=v, unit="mm", flags=["converted"]))
    # "2 cm SIBAL" is the sample's nominal size in a free-text description;
    # the report tables give measured widths (2.2 cm) — kept apart so a
    # nominal label is never mistaken for a disagreement with a measurement.
    m = re.search(r"(\d+(?:\.\d+)?)\s*cm", t)
    if m and "sphere" not in t and "spherical" not in t:
        v = float(m.group(1))
        run.set("width_nominal_cm", Measure(raw=m.group(0), value=v, min=v, max=v, unit="cm", flags=["nominal"]))
    m = re.search(r"([12])\s*sided", t)
    if m:
        run.set("sides_burning", cat(m.group(1), m.group(0)))
    if "sphere" in t or "spherical" in t:
        m = re.search(r"(\d+(?:\.\d+)?)\s*cm", t)
        if m:
            v = float(m.group(1)) * 10
            run.set("diameter_mm", Measure(raw=m.group(0), value=v, min=v, max=v, unit="mm", flags=["converted"]))


def bass_ii(ctx: Ctx) -> list[Run]:
    inv, name = "bass-ii", "PSI-25_Experimental table_BASS-II.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        if blank(row):
            rep.skip(line, "blank row")
            continue
        label = row["Test #"].strip()
        run = Run(inv, label, date=iso_date(row["Date"]))
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        run.set("pi", cat(text(row["PI"])))

        material = text(row["Fuel Sample Material"]) or ""
        run.set("fuel", cat(material))
        fam, basis = fuels.family(material), None
        low = material.lower()
        if fam is None and "rod" in low:
            fam, basis = "PMMA", _ROD_BASIS
        elif fam is None and "spherical" in low:
            fam, basis = "PMMA", _SPHERE_BASIS
        elif fam is None and ("film" in low or "micron" in low) and row["PI"].strip() == "Bhattacharjee":
            fam, basis = "PMMA", _FILM_BASIS
        run.set("fuel_family", cat(fam, basis=basis))
        run.set("fuel_form", cat(fuels.form(material) or ("rod" if "rod" in low else None)))
        _geometry_from_text(run, material)
        if "diameter_mm" in run.conditions and "rod" in low:
            run.notes.append("rod diameter converted from inches; " + _ROD_DIAMETER_BASIS)

        o2_i = pct(parse_measure(row["Calibrated initial O2 % by vol"], "%"))
        o2_f = pct(parse_measure(row["Calibrated final O2 % by vol"], "%"))
        if o2_i is not None and o2_i.usable:
            o2 = Measure(raw=o2_i.raw, value=o2_i.value, min=o2_i.min, max=o2_i.max, unit="%", flags=["initial"])
            if o2_f is not None and o2_f.usable and not (o2_i.value - 10 <= o2_f.value <= o2_i.value + 3):
                # e.g. B2 "22.2 → 1.6" or P22b "20 → 39.1": a 20-point drop in a
                # 255 L glovebox from one sample is not credible, and burning
                # cannot raise O2 by 19 points. Widening the interval to those
                # values would make the run "match" almost any O2 query, so the
                # final reading is recorded as suspect — not used, not corrected.
                o2.raw = f"initial {o2_i.raw} / final {o2_f.raw}"
                o2.flag("final_reading_suspect")
            elif o2_f is not None and o2_f.usable:
                o2.raw = f"initial {o2_i.raw} / final {o2_f.raw}"
                o2.min, o2.max = min(o2_i.min, o2_f.min), max(o2_i.max, o2_f.max)
                o2.flag("drifted_during_test")
            run.set("o2_pct", o2)
        # "Air display" / "Fan display" are control-panel readings, not a
        # stated velocity in cm/s; nothing in this table converts them.
        for col, key in (("Air display", "flow_setting_air"), ("Fan display", "flow_setting_fan")):
            if text(row[col]):
                run.set(key, cat(text(row[col]), basis="control-panel reading; not a velocity in cm/s"))
        if text(row["Flow restrictor"]):
            run.set("flow_restrictor", cat(text(row["Flow restrictor"])))

        run.outcome("final_co2_pct", pct(parse_measure(row["Final CO2 % by vol"], "%")))
        run.outcome("final_co_ppm", parse_measure(row["Final CO (ppm)"], "ppm"))
        runs.append(run)
    rep.runs_emitted = len(runs)
    return runs


def bass(ctx: Ctx) -> list[Run]:
    inv, name = "bass", "PSI-26_Experimental table_BASS.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        material = text(row["Fuel Sample Material"]) or ""
        if blank(row):
            rep.skip(line, "blank row")
            continue
        if "soot cleaning" in material.lower():
            rep.skip(line, "maintenance entry ('SOOT Cleaning'), not a combustion test")
            continue
        run = Run(inv, f"As-run {row['As Run Test #'].strip()}", date=iso_date(row["Date"]))
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        run.set("fuel", cat(material))
        fam = fuels.family(material)
        run.set("fuel_family", cat(fam))
        if fam is None:
            run.notes.append("material not named in the source row (e.g. '2 cm sphere') — family left unassigned")
        run.set("fuel_form", cat(fuels.form(material)))
        _geometry_from_text(run, material)
        low = material.lower()
        if "oppos" in low or "oppsed" in low:
            run.set("flow_direction", cat("opposed", material))
        if "wake" in low:
            run.notes.append("wake ignition (per material cell)")
        run.set("test_number", cat(row["Test #"].strip()))
        run.set("gmt_day", cat(row["GMT"].strip()))
        runs.append(run)
    rep.runs_emitted = len(runs)
    return runs


def _saffire_common(run: Run, row: dict, cols: dict) -> None:
    run.set("gravity", MICROGRAVITY)
    material = text(row.get(cols["material"]))
    if material:
        run.set("fuel", cat(material))
        run.set("fuel_family", cat(fuels.family(material)))
        run.set("fuel_form", cat(fuels.form(material)))
    run.set("thickness_mm", to_mm(parse_measure(row.get(cols["thickness"]), cols.get("thickness_unit"))))
    width = parse_measure(row.get(cols["width"]), "cm")
    run.set("width_cm", width)
    run.set("length_cm", parse_measure(row.get(cols["length"]), "cm"))
    run.set("flow_cm_s", parse_measure(row.get(cols["flow"]), "cm/s"))
    direction = text(row.get(cols["direction"]))
    if direction:
        run.set("flow_direction", cat(direction.lower(), direction))
    if cols.get("o2"):
        run.set("o2_pct", pct(parse_measure(row.get(cols["o2"]), "%")))
    if cols.get("ign_power"):
        run.set("ignition_power_w", parse_measure(row.get(cols["ign_power"]), "W"))
        run.set("ignition_time_s", parse_measure(row.get(cols["ign_time"]), "s"))


def _burn_time(run: Run, raw: str | None) -> None:
    m = parse_measure(raw, "s")
    if m is None:
        return
    if m.usable:
        run.outcome("burn_time", m)
    else:
        run.outcome("burn_time", text=text(raw))


def saffire_1(ctx: Ctx) -> list[Run]:
    inv, name = "saffire-1", "PSI-98_Experimental table_SAFFIRE-1.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    cols = dict(material="Material", thickness="Sample Thickness (cm)", thickness_unit="cm",
                width="Sample Width (cm)", length="Sample Length (cm)", flow="Air Flow (cm/s)",
                direction="Flow Direction", o2="Percent O2", ign_power="Ignition Power (W)",
                ign_time="Ignition Time (s)")
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        label = row["Sample Number"].strip()
        if not re.fullmatch(r"S\d+", label):
            rep.skip(line, f"not a burn sample ({text(row['Material'])})")
            continue
        run = Run(inv, label)
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        _saffire_common(run, row, cols)
        _burn_time(run, row["Burn Time (s)"])
        runs.append(run)
    rep.runs_emitted = len(runs)
    return runs


def saffire_2(ctx: Ctx) -> list[Run]:
    inv, name = "saffire-2", "PSI-99_Experimental table_SAFFIRE-2.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    cols = dict(material="Material", thickness="Samle Thickness", width="Sample Width (cm)",
                length="Sample Length", flow="Air Flow (cm/s)", direction="Flow Direction",
                o2="Percent O2 (Note 1)", ign_power="Ignition Power (W)", ign_time="Ignition Time (s)")
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        label = row["Sample Number"].strip()
        if label.lower().startswith("note"):
            ctx.note(inv, label)
            rep.skip(line, "table footnote (kept as an investigation note)")
            continue
        if not re.fullmatch(r"2-\d+", label):
            rep.skip(line, f"not a burn sample ({text(row['Material'])})")
            continue
        run = Run(inv, label)
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        _saffire_common(run, row, cols)
        if not text(row["Material"]):
            run.notes.append("material cell empty in the PSI table")
        _burn_time(run, row["Burn Time (s)"])
        # The "µ-g Spread Length" column holds values the cells themselves
        # label mm/s (e.g. "2.1 mm/s") — read by the cell's own unit.
        spread = parse_measure(row["?-g Spread Length"])
        if spread is not None and spread.usable and spread.unit == "mm/s":
            run.outcome("spread_rate", spread, note="PSI column header reads 'Spread Length'; the cell states mm/s")
        elif text(row["?-g Spread Length"]):
            run.outcome("spread_rate", text=text(row["?-g Spread Length"]))
        extent = parse_measure(row["?-g Burn Length"], "cm")
        if extent is not None:
            run.outcome("spread_extent", extent if extent.usable else None, text=None if extent.usable else extent.raw)
        g1 = parse_measure(row["1-g Spread Rate"])
        if g1 is not None and g1.usable:
            run.outcome("spread_rate_1g", g1, note="normal-gravity comparison test")
        elif text(row["1-g Spread Rate"]):
            run.outcome("spread_rate_1g", text=text(row["1-g Spread Rate"]), note="normal-gravity comparison test")
        runs.append(run)
    rep.runs_emitted = len(runs)
    return runs


def saffire_3(ctx: Ctx) -> list[Run]:
    inv, name = "saffire-3", "PSI-100_Experimental table_SAFFIRE-3.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    cols = dict(material="Material", thickness="Sample Thickness", width="Sample Width",
                length="Sample Length", flow="Air Flow", direction="Direction")
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        label = row["Sample Number"].strip()
        run = Run(inv, label)
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        _saffire_common(run, row, cols)
        runs.append(run)
    rep.runs_emitted = len(runs)
    return runs


ADAPTERS = [bass, bass_ii, saffire_1, saffire_2, saffire_3]
