"""Droplet-combustion adapters: FLEX (PSI-69), FLEX-2 (PSI-68), CFI (PSI-39 + CFI data summary workbook)."""

from __future__ import annotations

import openpyxl

from .. import fuels
from ..model import Run, cat, psi_source
from ..units import Measure, fraction_to_pct, parse_measure, text, to_atm
from . import Ctx, blank, iso_date, raw_of, read_csv

MICROGRAVITY = cat("microgravity")
FLEX_K_NOTE = (
    "PSI header reads 'Burning rate; mm'; the FLEX report's Table IX key defines burning rate as the "
    "average burning-rate constant from a d²-vs-time fit, in mm²/s (knowledge/investigations/droplet-combustion/flex)"
)


def _diluent(parts: dict[str, Measure | None]) -> dict | None:
    names = [n for n, m in parts.items() if m is not None and m.usable and (m.max or 0) > 0]
    return cat("/".join(names)) if names else None


def flex(ctx: Ctx) -> list[Run]:
    inv, name = "flex", "PSI-69_Experimental table_FLEX.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        if blank(row):
            rep.skip(line, "blank row")
            continue
        num = row["FLEX Test #"].strip()
        run = Run(inv, f"FLEX-{int(num):03d}" if num.isdigit() else num, date=iso_date(row["Test Date"]))
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        run.set("identifier", cat(text(row["FLEX Identifier"])))
        fuel = text(row["Fuel"])
        run.set("fuel", cat(fuel))
        run.set("fuel_family", cat(fuels.family(fuel)))
        run.set("fuel_form", cat("droplet"))
        run.set("pressure_atm", to_atm(parse_measure(row["Ambient pressure; mmHg"], "mmHg"), "mmHg"))
        o2 = fraction_to_pct(parse_measure(row["O initial ambient composition; mole fraction"]))
        run.set("o2_pct", o2)
        n2 = fraction_to_pct(parse_measure(row["N initial ambient composition; mole fraction"]))
        co2 = fraction_to_pct(parse_measure(row["CO initial ambient composition; mole fraction"]))
        he = fraction_to_pct(parse_measure(row["He initial ambient composition; mole fraction"]))
        run.set("n2_pct", n2)
        run.set("co2_pct", co2)
        run.set("he_pct", he)
        run.set("diluent", _diluent({"N2": n2, "CO2": co2, "He": he}))
        run.set("droplet_d0_mm", parse_measure(row["Droplet initial diameter; mm"], "mm"))

        run.outcome("extinction_diameter", parse_measure(row["Visible flame extinction diameter; mm"], "mm"))
        k = parse_measure(row["Burning rate; mm"])
        if k is not None:
            k.unit = "mm²/s"
            k.flag("unit_from_report")
            run.outcome("burning_rate_k", k, note=FLEX_K_NOTE)
        run.outcome("burn_time", parse_measure(row["Burn time; s"], "s"))
        run.outcome("test_end", text=text(row["Test end"]))
        runs.append(run)
    rep.runs_emitted = len(runs)
    return runs


def flex_2(ctx: Ctx) -> list[Run]:
    inv, name = "flex-2", "PSI-68_Experimental table_Flex2.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    runs = []
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        fuel = text(row["Sample (Fuel Type)"])
        run = Run(inv, fuel or f"row {line}", granularity="envelope")
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.notes.append("test-matrix envelope for this fuel (planned condition ranges), not an individual test")
        run.set("gravity", MICROGRAVITY)
        run.set("fuel", cat(fuel))
        run.set("fuel_family", cat(fuels.family(fuel)))
        run.set("fuel_form", cat("droplet"))
        run.set("droplet_d0_mm", parse_measure(row["Initial Droplet Diameter (mm)"], "mm"))
        run.set("diluent", cat(text(row["Ambient Gas Mixture"])))
        run.set("o2_pct", fraction_to_pct(parse_measure(row["Oxygen Mole Fraction"])))
        run.set("pressure_atm", to_atm(parse_measure(row["Ambient Pressure (atm)"], "atm"), "atm"))
        run.set("ambient_temp_c", parse_measure(row["Ambient Temperature (C)"], "°C"))
        run.set("flow_cm_s", parse_measure(row["Flow Velocity (cm/s)"], "cm/s"))
        runs.append(run)
    rep.runs_emitted = len(runs)
    return runs


CFI_BOOK = "CFI_DataSummary_Spreadsheet_Jan2021.xlsx"


def _cfi_data_sheet(ctx: Ctx) -> dict[str, tuple[int, dict]]:
    """Flex Number → (sheet row, {column: value}) from the workbook's DATA sheet."""
    wb = openpyxl.load_workbook(ctx.raw_dir / "matrices" / CFI_BOOK, read_only=True, data_only=True)
    ws = wb["DATA"]
    rows = ws.iter_rows(values_only=True)
    header = [str(h).strip() if h is not None else "" for h in next(rows)]
    out: dict[str, tuple[int, dict]] = {}
    for i, cells in enumerate(rows, start=2):
        rec = {h: c for h, c in zip(header, cells) if h and c is not None and str(c).strip() != ""}
        key = rec.get("Flex Number")
        if key is None:
            continue
        out.setdefault(str(key).strip().split(".")[0], (i, rec))
    return out


def cfi(ctx: Ctx) -> list[Run]:
    inv, name = "cfi", "PSI-39_Experimental table_CFI.csv"
    rep, psi = ctx.report(name, inv), ctx.psi_id(inv)
    data = _cfi_data_sheet(ctx)
    rep.notes.append(f"outcomes joined on Flex Number from {CFI_BOOK} sheet DATA ({len(data)} rows)")
    runs = []
    seen: dict[str, int] = {}
    for line, row in read_csv(ctx, name):
        rep.rows_read += 1
        if blank(row):
            rep.skip(line, "blank row")
            continue
        flex_no = row["Flex Number"].strip()
        if flex_no in seen:
            rep.skip(line, f"duplicate of Flex Number {flex_no} at row {seen[flex_no]}")
            continue
        seen[flex_no] = line
        run = Run(inv, f"Flex {flex_no}", date=iso_date(row["Test Date"]))
        run.sources.append(psi_source(psi, name, line))
        run.raw.append(raw_of(row))
        run.set("gravity", MICROGRAVITY)
        fuel = text(row["Fuel"])
        run.set("fuel", cat(fuel))
        run.set("fuel_family", cat(fuels.family(fuel)))
        run.set("fuel_form", cat("droplet"))
        run.set("pressure_atm", to_atm(parse_measure(row["Pressure"], "atm"), "atm"))
        run.set("o2_pct", fraction_to_pct(parse_measure(row["Oxygen"])))
        n2 = fraction_to_pct(parse_measure(row["Nitrogen"]))
        he = fraction_to_pct(parse_measure(row["Helium"]))
        run.set("n2_pct", n2)
        run.set("he_pct", he)
        run.set("diluent", _diluent({"N2": n2, "He": he}))
        run.set("fiber_supported", cat(text(row["Fiber"])))

        hit = data.get(flex_no)
        if hit:
            sheet_row, rec = hit
            run.sources.append({"kind": "psi-workbook", "dataset": psi, "file": CFI_BOOK, "sheet": "DATA", "row": sheet_row})
            run.raw.append({k: str(v) for k, v in rec.items()})
            src = len(run.sources) - 1
            run.set("droplet_d0_mm", parse_measure(rec.get("D0 ( mm )"), "mm"))
            for col, q, unit in (
                ("Dext, hot ( mm )", "extinction_diameter_hot", "mm"),
                ("khot ( mm^2/s )", "burning_rate_k_hot", "mm²/s"),
                ("kcool ( mm^2/s )", "burning_rate_k_cool", "mm²/s"),
                ("Dext,cool ( mm )", "extinction_diameter_cool", "mm"),
                ("HF Burn Time", "burn_time_hot_flame", None),  # unit not stated in the workbook
                ("Reignitions", "reignitions", None),
            ):
                run.outcome(q, parse_measure(rec.get(col), unit), source=src)
        else:
            run.notes.append(f"no row for this Flex Number in {CFI_BOOK} DATA sheet — no outcomes")
        runs.append(run)
    rep.runs_emitted = len(runs)
    return runs


ADAPTERS = [flex, flex_2, cfi]
