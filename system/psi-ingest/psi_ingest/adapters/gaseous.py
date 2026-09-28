"""Gaseous-flame adapters: ACME Flame Design (PSI-10), CFI-G (PSI-159), ACME BRE / CLD /
E-FIELD / s-Flame (PSI-20..23), SPICE (PSI-107), SLICE (PSI-106).

Normal vs. inverse flames: in a NORMAL flame the ambient is the oxidizer, so
the table's XO2 is the ambient O2 → `o2_pct`. In an INVERSE flame the burner
issues oxidizer into a fuel-laden ambient, so XO2 is the burner stream's O2
→ `oxidizer_stream_o2_pct`, deliberately NOT `o2_pct`: querying "ambient O2
= 21 %" must not match an inverse flame's oxidizer jet.
"""

from __future__ import annotations

import re

from .. import fuels
from ..model import Run, cat, psi_source
from ..units import Measure, fraction_to_pct, parse_measure, pct, text, to_atm
from . import Ctx, blank, iso_date, raw_of, read_csv, yyddd

MICROGRAVITY = cat("microgravity")


def _drift(a: Measure | None, b: Measure | None) -> Measure | None:
    """Before/after pair → one Measure spanning both, flagged as drift."""
    if a is None or not a.usable:
        return b
    if b is None or not b.usable:
        return a
    return Measure(
        raw=f"initial {a.raw} / final {b.raw}", value=a.value, min=min(a.min, b.min),
        max=max(a.max, b.max), unit=a.unit, flags=sorted(set(a.flags + b.flags + ["drifted_during_test"])),
    )


def _test_date(label: str) -> str | None:
    m = re.match(r"(\d{5})", label)
    return yyddd(m.group(1)) if m else None


def _notes_once(ctx: Ctx, inv: str, row: dict, col: str = "Notes") -> None:
    note = text(row.get(col))
    if note and note not in ctx.table_notes.get(inv, []):
        ctx.note(inv, note)


def flame_design(ctx: Ctx) -> list[Run]:
    inv = "acme-flame-design"
    runs = []
    for name, kind in (
        ("PSI-10_Experimental table_Flame Design_Normal Flame.csv", "normal"),
        ("PSI-10_Experimental table_Flame Design_Inverse Flame.csv", "inverse"),
    ):
        rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
        for line, row in read_csv(ctx, name):
            rep.rows_read += 1
            if blank(row):
                rep.skip(line, "blank row")
                continue
            label = text(row["Test"]) or f"row {line}"
            run = Run(inv, label, date=_test_date(label))
            run.sources.append(psi_source(psi, name, line))
            run.raw.append(raw_of(row))
            run.set("gravity", MICROGRAVITY)
            run.set("flame_type", cat(kind))
            run.set("pressure_atm", _drift(parse_measure(row["pinit (atm)"], "atm"), parse_measure(row["pfinal (atm)"], "atm")))
            if kind == "normal":
                fuel = text(row["Fuel"])
                run.set("fuel", cat(fuel))
                run.set("fuel_family", cat(fuels.family(fuel)))
                run.set("fuel_fraction_pct", fraction_to_pct(parse_measure(row["Xfuel"])))
                run.set("fuel_flow_mg_s", parse_measure(row["mfuel (mg/s)"], "mg/s"))
                run.set("o2_pct", _drift(fraction_to_pct(parse_measure(row["XO2 (init)"])),
                                         fraction_to_pct(parse_measure(row["XO2 (final)"]))))
            else:
                run.set("fuel", cat("C2H4 (ambient)", basis="column 'XC2H4 initial/final' is the ambient ethylene fraction"))
                run.set("fuel_family", cat("ethylene"))
                run.set("ambient_fuel_pct", _drift(fraction_to_pct(parse_measure(row["XC2H4 initial"])),
                                                   fraction_to_pct(parse_measure(row["XC2H4 final"]))))
                run.set("oxidizer_stream_o2_pct", fraction_to_pct(parse_measure(row["XO2"])))
                run.set("oxidizer_flow_mg_s", parse_measure(row["mO2 (mg/s)"], "mg/s"))
            run.set("stoich_mixture_fraction", parse_measure(row["mean Zst"]))
            tad = parse_measure(row["Tad (K)"], "K")
            if tad is not None:
                run.set("adiabatic_flame_temp_k", tad.flag("computed"))
            runs.append(run)
            rep.runs_emitted += 1
    return runs


def _yes_no(raw: str | None) -> str | None:
    t = (text(raw) or "").lower()
    return {"yes": "yes", "no": "no", "flash": "flash"}.get(t)


def cfi_g(ctx: Ctx) -> list[Run]:
    inv = "cfi-g"
    runs = []
    for name, kind in (
        ("PSI-159_Experimental table_CFI-G_Normal Flames.csv", "normal"),
        ("PSI-159_Experimental table_CFI-G_Inverse Flames.csv", "inverse"),
    ):
        rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
        for line, row in read_csv(ctx, name):
            rep.rows_read += 1
            if blank(row):
                rep.skip(line, "blank row")
                continue
            label = text(row["Test"]) or f"row {line}"
            run = Run(inv, label, date=_test_date(label))
            run.sources.append(psi_source(psi, name, line))
            run.raw.append(raw_of(row))
            run.set("gravity", MICROGRAVITY)
            run.set("flame_type", cat(kind))
            fuel = text(row["Fuel"])
            run.set("fuel", cat(fuel))
            run.set("fuel_family", cat(fuels.family(fuel)))
            p = parse_measure(row["approx p (bar)"], "bar")
            run.set("pressure_atm", None if p is None else to_atm(p.flag("approx"), "bar"))
            if kind == "normal":
                run.set("o2_pct", _drift(fraction_to_pct(parse_measure(row["XO2 before test"])),
                                         fraction_to_pct(parse_measure(row["XO2 after test"]))))
                run.set("fuel_fraction_pct", fraction_to_pct(parse_measure(row["Xf"])))
                run.set("fuel_flow_mg_s", parse_measure(row["mHC (mg/s)"], "mg/s"))
                run.outcome("cool_flame", text=text(row["Cool flame?"]))
                run.outcome("peak_burner_temp_c", parse_measure(row["Peak burner T (C )"], "°C"))
                ext = text(row["Self-ext or flow term"])
            else:
                run.set("ambient_fuel_pct", _drift(fraction_to_pct(parse_measure(row["Xf before test"])),
                                                   fraction_to_pct(parse_measure(row["Xf after test"]))))
                run.set("oxidizer_stream_o2_pct", fraction_to_pct(parse_measure(row["XO2"])))
                run.set("fuel_flow_mg_s", parse_measure(row["HC burnrate (mg/s)"], "mg/s"))
                run.set("oxidizer_flow_mg_s", parse_measure(row["O2 flow rate (mg/s)"], "mg/s"))
                run.outcome("peak_burner_temp_c", parse_measure(row["Peak burner Temp (C)"], "°C"))
                run.outcome("flame_color", text=text(row["Color"]))
                ext = text(row["Self -ext or flow term"])
            run.set("stoich_mixture_fraction", parse_measure(row["Zst"]))
            tad = parse_measure(row["Tad (K)"], "K")
            if tad is not None:
                run.set("adiabatic_flame_temp_k", tad.flag("computed"))
            run.outcome("hot_ignition", text=_yes_no(row["Hot ignition"]))
            run.outcome("burn_time", parse_measure(row["burn time (sec)"], "s"))
            if ext in ("SE", "FT"):
                run.outcome("end_mode", text={"SE": "self-extinguished", "FT": "flow terminated"}[ext], note=f"source code '{ext}'")
            run.outcome("comment", text=text(row["Comments"]))
            runs.append(run)
            rep.runs_emitted += 1
    return runs


_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], start=1)}


def _ymd(year: str, month: str, day: str) -> str | None:
    try:
        mo = int(month) if month.strip().isdigit() else _MONTHS[month.strip().lower()[:3]]
        return f"{int(year):04d}-{mo:02d}-{int(day):02d}"
    except (KeyError, ValueError):
        return None


def acme_bre(ctx: Ctx) -> list[Run]:
    inv, name = "acme-bre", "PSI-20_Experimental table_ACME BRE.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        _notes_once(ctx, inv, row)
        date = _ymd(row["Year"], row["Month"], row["Date"])
        run = Run(inv, date or f"row {line}", granularity="day", date=date)
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        fuel = text(row["Fuel Bottle"])
        run.set("fuel", cat(fuel))
        run.set("fuel_family", cat(fuels.family(fuel)))
        run.set("burner_diameter_mm", parse_measure(row["Burner Size (mm)"], "mm"))
        o2 = pct(parse_measure(row["Oxygen Conc (percent)"], "%"))
        if o2 is not None:
            o2.flag("approx")  # the source's note: "approximate concentrations for tests that ignited"
        run.set("o2_pct", o2)
        run.outcome("flames_ignited", parse_measure(row["Flames Ignited"], "flames"))
        runs.append(run)
        rep.runs_emitted += 1
    return runs


def acme_cld(ctx: Ctx) -> list[Run]:
    inv, name = "acme-cld", "PSI-21_Experimental table_CLD Flame.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        _notes_once(ctx, inv, row)
        day = text(row["Test Day"])
        run = Run(inv, day or f"row {line}", granularity="day", date=yyddd(day))
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        bottle, test_type = text(row["Fuel Bottle"]), text(row["Test Type"])
        run.set("fuel", cat(bottle))
        fam = fuels.family(bottle)
        basis = None
        if fam is None and test_type:
            fam = fuels.family(test_type)
            basis = f"Fuel Bottle cell '{bottle}' names no known fuel; family from Test Type '{test_type}'"
        run.set("fuel_family", cat(fam, basis=basis))
        run.set("test_type", cat(test_type))
        run.set("fuel_fraction_pct", pct(parse_measure((row["Fuel conc. Range"] or "").replace("%", ""), "%")))
        run.outcome("flames_ignited", parse_measure(row["Flames ignited"], "flames"))
        runs.append(run)
        rep.runs_emitted += 1
    return runs


def acme_efield(ctx: Ctx) -> list[Run]:
    inv, name = "acme-efield", "PSI-22_Experimental table_ACME E-FIELD Flames.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs: list[Run] = []
    seen_blocks: set[tuple] = set()
    current: Run | None = None
    concs: list[str] = []

    def close() -> None:
        nonlocal current, concs
        if current is None:
            return
        key = (current.label, tuple(concs), current.raw[0].get("Mesh Polarity"), current.raw[0].get("Fuel Bottle"))
        if key in seen_blocks:
            rep.skip(current.sources[0]["row"], f"repeat of test day {current.label} block already ingested")
        else:
            seen_blocks.add(key)
            m = pct(parse_measure("; ".join(c.replace("%", "") for c in concs), "%"))
            current.set("fuel_fraction_pct", m)
            runs.append(current)
            rep.runs_emitted += 1
        current, concs = None, []

    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        _notes_once(ctx, inv, row)
        day = text(row["Test Day"])
        if not day:
            if current is not None and text(row["Fuel Conc"]):
                concs.append(row["Fuel Conc"].strip())
                rep.merged_into_previous += 1
                current.sources.append(psi_source(ctx.psi_id(inv), name, line))
                current.raw.append(raw_of(row))
            else:
                rep.skip(line, "notes-only row")
            continue
        close()
        current = Run(inv, day, granularity="day", date=yyddd(day))
        current.sources.append(psi_source(psi, name, line))
        current.raw.append(raw_of(row))
        current.set("gravity", MICROGRAVITY)
        current.set("test_type", cat(text(row["Test Type"])))
        bottle = text(row["Fuel Bottle"])
        current.set("fuel", cat(bottle))
        current.set("fuel_family", cat(fuels.family(bottle)))
        current.set("e_field_polarity", cat(text(row["Mesh Polarity"])))
        current.outcome("flames_ignited", parse_measure(row["Flames Ignited"], "flames"))
        concs = [row["Fuel Conc"].strip()] if text(row["Fuel Conc"]) else []
    close()
    return runs


def acme_s_flame(ctx: Ctx) -> list[Run]:
    inv, name = "acme-s-flame", "PSI-23_Experimental table_ACME s-Flame.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        _notes_once(ctx, inv, row)
        day = text(row["Test Day*"])
        run = Run(inv, day or f"row {line}", granularity="day", date=yyddd(day))
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        run.set("test_type", cat(text(row["Test Type"])))
        atm = text(row["Atmosphere*"]) or ""
        o2s = re.findall(r"~?\s*(\d+(?:\.\d+)?)\s*%", atm)
        if o2s:
            run.set("o2_pct", pct(parse_measure("; ".join(o2s) if len(o2s) > 1 else o2s[0], "%")).flag("approx"))
            run.conditions["o2_pct"].raw = atm
        if re.search(r"\bHe\b", atm):
            run.set("diluent", cat("He", atm))
        elif re.search(r"\bN2\b", atm):
            run.set("diluent", cat("N2", atm))
        else:
            run.notes.append(f"atmosphere diluent '{atm}' not recognized (possible spreadsheet fill artifact) — left unassigned")
        run.set("pressure_atm", Measure(raw="~1 atm (table note)", value=1.0, min=1.0, max=1.0, unit="atm",
                                        flags=["approx", "from_table_note"]))
        bottle = text(row["Fuel Bottle"])
        run.set("fuel", cat(bottle))
        run.set("fuel_family", cat(fuels.family(bottle)))
        run.outcome("flames_ignited", parse_measure(row["Flames Ignited*"], "flames"))
        runs.append(run)
        rep.runs_emitted += 1
    # One test point's mass-flow-controller log ships beside the tables.
    aux = "19304A1_mfcSetpoints.csv"
    for run in runs:
        if run.label == "19304":
            run.sources.append({"kind": "psi-aux", "dataset": ctx.psi_id(inv), "file": aux, "row": None,
                                "note": "MFC setpoint time series for test point 19304A1"})
            run.raw.append({})
    rep.notes.append(f"{aux} attached to test day 19304 as an auxiliary time series (not a run)")
    return runs


def spice(ctx: Ctx) -> list[Run]:
    inv, name = "spice", "PSI-107_Experimental table_Spice.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    seen: dict[tuple, int] = {}
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        if blank(row):
            rep.skip(line, "blank row")
            continue
        key = tuple(v.strip() for v in row.values())
        if key in seen:
            rep.skip(line, f"exact duplicate of row {seen[key]}")
            continue
        seen[key] = line
        gmt_day, ign = row["GMT date"].strip(), row["GMT ignition"].strip()
        air = row["Air Rate (cm/s)"].strip()
        # One flame is logged as several rows (one per air-rate setting), and
        # two rows can share day, ignition time AND air rate while differing in
        # fuel rate — the source line is the only unique handle.
        run = Run(inv, f"GMT {gmt_day} {ign} · line {line}", granularity="test-point")
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        fuel = text(row["Fuel"])
        run.set("fuel", cat(fuel))
        run.set("fuel_family", cat(fuels.family(fuel)))
        m = re.match(r"(\d+)\s*%", fuel or "")
        if m:
            v = float(m.group(1))
            run.set("fuel_fraction_pct", Measure(raw=fuel, value=v, min=v, max=v, unit="%"))
        run.set("nozzle_diameter_mm", parse_measure(row["Nozzle (mm)"], "mm"))
        run.set("fuel_flow_mg_s", parse_measure(row["Fuel Rate (mg/s)"], "mg/s"))
        flow = parse_measure(air, "cm/s")
        if flow is not None and flow.usable and flow.value < 0:
            flow.flag("negative_reading")
        run.set("flow_cm_s", flow)
        run.set("flow_direction", cat("coflow") if flow is not None else None)
        run.set("gmt_day", cat(gmt_day))
        runs.append(run)
        rep.runs_emitted += 1
    return runs


def slice_(ctx: Ctx) -> list[Run]:
    inv, name = "slice", "PSI-106_Experimental table_Slice.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        date_cell = text(row["Test Date"]) or ""
        m = re.match(r"(\d{4}-[A-Z]{3}-\d{2})", date_cell)
        date = iso_date(m.group(1).title()) if m else None
        run = Run(inv, m.group(1) if m else date_cell, granularity="day", date=date)
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        fuel = text(row["Fuel Type"])
        run.set("fuel", cat(fuel))
        run.set("fuel_family", cat(fuels.family(fuel)))
        fm = re.match(r"\s*(\d+)\s*%", fuel or "")
        if fm:
            v = float(fm.group(1))
            run.set("fuel_fraction_pct", Measure(raw=fuel, value=v, min=v, max=v, unit="%"))
        if "SPICE" in date_cell:
            run.notes.append(f"source row notes: '{date_cell}'")
        runs.append(run)
        rep.runs_emitted += 1
    return runs


ADAPTERS = [flame_design, cfi_g, acme_bre, acme_cld, acme_efield, acme_s_flame, spice, slice_]
