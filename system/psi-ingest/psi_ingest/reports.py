"""Merge report-sourced per-test tables (as reproduced in the governed
knowledge/ documents) into the PSI runs.

Rule from AGENTS.md: two sources that disagree stay two cited statements.
So a report value that matches the PSI value CONFIRMS it (and the run cites
both); one that differs is recorded as a conflict with both raw values and
the condition's interval widens to cover both — the query then neither
trusts nor drops the run on the disputed axis, and every surface shows the
disagreement. Nothing is silently chosen.
"""

from __future__ import annotations

import re
from pathlib import Path

from . import fuels, knowledge, verify
from .adapters import Ctx
from .model import Outcome, Run, cat
from .units import Measure, parse_measure, pct, to_atm, to_mm

REL_TOL = 0.01


def _agree(a: Measure, b: Measure) -> bool:
    if not (a.usable and b.usable):
        return True  # nothing numeric to disagree about
    slack = max(abs(a.max or 0), abs(b.max or 0), 1e-9) * REL_TOL
    if a.values and b.values and len(a.values) == len(b.values):
        return all(abs(x - y) <= slack for x, y in zip(sorted(a.values), sorted(b.values)))
    return (a.min - slack) <= b.max and (b.min - slack) <= a.max


class Merger:
    def __init__(self, ctx: Ctx, runs: list[Run]):
        self.ctx = ctx
        self.runs = runs
        self.by_key = {(r.investigation, r.label): r for r in runs}
        self.stats: list[dict] = []

    # -- sources ---------------------------------------------------------
    def add_source(self, run: Run, inv: str, table: str, line: int, raw_row: dict) -> int:
        reg = self.ctx.registry[inv]
        c = knowledge.citation(self.ctx.repo_root, reg["ksor_doc"], reg["source_id"])
        run.sources.append({"kind": "report", "table": table, "line": line, **c})
        run.raw.append({k: v for k, v in raw_row.items() if k != "__line__"})
        return len(run.sources) - 1

    # -- merging ---------------------------------------------------------
    def condition(self, run: Run, key: str, new: Measure | None, src: int) -> None:
        if new is None:
            return
        old = run.conditions.get(key)
        if old is None or not isinstance(old, Measure) or not old.usable:
            run.conditions[key] = new.flag(f"from_source_{src}")
            return
        if not new.usable:
            return
        if _agree(old, new):
            old.flag(f"confirmed_by_source_{src}")
            return
        run.conflicts.append({
            "field": key,
            "values": [
                {"source": 0, "raw": old.raw, "min": old.min, "max": old.max, "unit": old.unit},
                {"source": src, "raw": new.raw, "min": new.min, "max": new.max, "unit": new.unit},
            ],
        })
        run.conditions[key] = Measure(
            raw=f"{old.raw} | {new.raw}", value=None, min=min(old.min, new.min), max=max(old.max, new.max),
            unit=old.unit, flags=["sources_disagree"],
        )

    def category(self, run: Run, key: str, value: str | None, src: int, raw: str | None = None, basis: str | None = None) -> None:
        if not value:
            return
        old = run.conditions.get(key)
        if old is None:
            run.conditions[key] = cat(value, raw, basis) | {"source": src}
        elif old["value"].lower() != value.lower():
            run.conflicts.append({"field": key, "values": [
                {"source": 0, "raw": old.get("raw", old["value"])}, {"source": src, "raw": raw or value}]})

    def outcome(self, run: Run, o: Outcome) -> None:
        for existing in run.outcomes:
            if existing.quantity != o.quantity or existing.at != o.at:
                continue
            if existing.measure is not None and o.measure is not None and o.measure.usable and existing.measure.usable:
                if _agree(existing.measure, o.measure):
                    existing.confirmed_by.append(o.source)
                else:
                    run.conflicts.append({"field": f"outcome:{o.quantity}", "values": [
                        {"source": existing.source, "raw": existing.measure.raw},
                        {"source": o.source, "raw": o.measure.raw}]})
                    run.outcomes.append(o)
                return
            if existing.measure is None and o.measure is None and (existing.text or "").lower() == (o.text or "").lower():
                existing.confirmed_by.append(o.source)
                return
        run.outcomes.append(o)

    def standalone(self, inv: str, label: str, **kw) -> Run:
        run = Run(inv, label, **kw)
        run.conditions["gravity"] = cat("microgravity")
        self.runs.append(run)
        self.by_key[(inv, label)] = run
        return run

    def stat(self, table: str, rows: int, joined: int, standalone: int) -> None:
        self.stats.append({"table": table, "rows": rows, "joined_to_psi_runs": joined, "report_only_runs": standalone})


def _paired_outcomes(m: Merger, run: Run, quantity: str, values_cell: str, flow: Measure | None, unit: str, src: int) -> None:
    """'0.106, 0.099, 0.083, and 0.07' at velocities '10, 6, 5, and 3' → one outcome per velocity."""
    v = parse_measure(values_cell, unit)
    if v is None:
        return
    if not v.usable:
        m.outcome(run, Outcome(quantity, text=v.raw, source=src))
        return
    vals = v.values or [v.value]
    flows = (flow.values or [flow.value]) if flow is not None and flow.usable else []
    if len(vals) > 1 and len(flows) == len(vals):
        for val, f in zip(vals, flows):
            m.outcome(run, Outcome(quantity, Measure(raw=v.raw, value=val, min=val, max=val, unit=unit), source=src,
                                   at={"flow_cm_s": f}))
    elif len(vals) == 1 and len(flows) == 1:
        m.outcome(run, Outcome(quantity, v, source=src, at={"flow_cm_s": flows[0]}))
    else:
        m.outcome(run, Outcome(quantity, v, source=src))


def _o2_pair(initial: str, final: str | None) -> Measure | None:
    a = pct(parse_measure(initial, "%"))
    b = pct(parse_measure(final, "%")) if final else None
    if a is None or not a.usable:
        return a
    if b is None or not b.usable:
        return a
    return Measure(raw=f"initial {a.raw} / final {b.raw}", value=a.value, min=min(a.min, b.min),
                   max=max(a.max, b.max), unit="%", flags=["drifted_during_test"])


def bass_ii_table_5_1(m: Merger) -> None:
    doc = m.ctx.registry["bass-ii"]["ksor_doc"]
    table = "Table 5.1"
    _, rows, _ = knowledge.table_under(m.ctx.repo_root, doc, "Full test matrix (Table 5.1")
    joined = alone = 0
    for row in rows:
        label = row["Test"].strip()
        run = m.by_key.get(("bass-ii", label))
        if run is None:
            run, alone = m.standalone("bass-ii", label), alone + 1
        else:
            joined += 1
        src = m.add_source(run, "bass-ii", table, row["__line__"], row)
        m.condition(run, "thickness_mm", parse_measure(row["Thickness (mm)"], "mm"), src)
        m.condition(run, "width_cm", parse_measure(row["Width (cm)"], "cm"), src)
        m.category(run, "sides_burning", row["Sides burning"].strip(), src)
        flow = parse_measure(row["Velocity (cm/s)"], "cm/s")
        m.condition(run, "flow_cm_s", flow, src)
        m.category(run, "flow_direction", "opposed", src, basis="bass-ii Table 5.1 note: 'All flow was opposed'")
        m.category(run, "fuel_family", "PMMA", src, basis="bass-ii §5.3: 'A total of 20 PMMA flat samples were burnt'")
        m.condition(run, "o2_pct", _o2_pair(row["Initial O₂ (%)"], row["Final O₂ (%)"]), src)
        _paired_outcomes(m, run, "spread_rate", row["Spread rate (mm/s)"], flow, "mm/s", src)
        bt = parse_measure(row["Burn time (min)"], "min")
        if bt is not None and bt.usable:
            m.outcome(run, Outcome("burn_time", bt.scaled(60, "s"), source=src))
    m.stat(f"{doc} {table}", len(rows), joined, alone)


def _comment_outcomes(m: Merger, run: Run, comment: str, src: int) -> None:
    c = comment.lower()
    if c in ("", "—", "-"):
        return
    if "no ignition" in c or "did not ignite" in c:
        m.outcome(run, Outcome("ignited", text="no", source=src, note=comment))
    elif "ignited" in c:
        m.outcome(run, Outcome("ignited", text="yes", source=src, note=comment))
    if "quenched" in c:
        m.outcome(run, Outcome("end_mode", text="quenched", source=src, note=comment))
    elif "no blowoff" in c:
        m.outcome(run, Outcome("end_mode", text="no blowoff", source=src, note=comment))
    elif "blow-off" in c or "blowoff" in c:
        m.outcome(run, Outcome("end_mode", text="blow-off", source=src, note=comment))
    if not any(k in c for k in ("ignit", "quench", "blow")):
        m.outcome(run, Outcome("comment", text=comment, source=src))


def bass_ii_table_7_1(m: Merger) -> None:
    doc = m.ctx.registry["bass-ii"]["ksor_doc"]
    table = "Table 7.1"
    _, rows, _ = knowledge.table_under(m.ctx.repo_root, doc, "Full test matrix (Table 7.1")
    joined = alone = 0
    bass_runs = [r for r in m.runs if r.investigation == "bass"]
    for row in rows:
        test = row["Test"].strip()
        mt = re.match(r"GMT(\d+)-T(\w+)(\s*\(BASS\))?", test)
        if not mt:
            continue
        gmt, tnum, is_bass = mt.group(1), mt.group(2), bool(mt.group(3))
        run = None
        if is_bass:
            cands = [r for r in bass_runs
                     if r.conditions.get("gmt_day", {}).get("value") == gmt
                     and r.conditions.get("test_number", {}).get("value") == tnum
                     and (r.conditions.get("fuel_family") or {}).get("value", "").startswith("SIBAL")]
            run = cands[0] if len(cands) == 1 else None
            inv = "bass"
        else:
            run = m.by_key.get(("bass-ii", f"T{tnum}"))
            inv = "bass-ii"
        if run is None:
            run, alone = m.standalone(inv, test), alone + 1
        else:
            joined += 1
        src = m.add_source(run, inv, table, row["__line__"], row)
        m.condition(run, "width_cm", parse_measure(row["Width (cm)"], "cm"), src)
        flow = parse_measure(row["Flow (cm/s)"], "cm/s")
        if flow is not None and "range" in flow.flags:
            flow.flag("varied_during_test")
        m.condition(run, "flow_cm_s", flow, src)
        o2_cell = row["O₂ (vol%)"]
        o2 = pct(parse_measure(re.sub(r"\(.*?\)", "", o2_cell).strip(), "%"))
        if o2 is not None:
            o2.raw = o2_cell
            if "inaccurate" in o2_cell:
                o2.flag("reading_may_be_inaccurate")
        m.condition(run, "o2_pct", o2, src)
        m.category(run, "flow_direction", "concurrent", src, basis="bass-ii Table 7.1 heading: 'all SIBAL fabric, concurrent flow'")
        m.category(run, "fuel_family", "SIBAL (cotton-fiberglass)", src)
        _comment_outcomes(m, run, row["Comments"].strip(), src)
    m.stat(f"{doc} {table}", len(rows), joined, alone)


_SAFFIRE_KEYS = {"1-1": ("saffire-1", "S1"), "1-2": ("saffire-1", "S2")}


def _saffire_run(m: Merger, sample: str) -> tuple[Run, str, bool]:
    inv, label = _SAFFIRE_KEYS.get(sample, ("saffire-2", sample))
    run = m.by_key.get((inv, label))
    if run is None:
        return m.standalone(inv, label), inv, False
    return run, inv, True


def saffire_table_i(m: Merger) -> None:
    doc = m.ctx.registry["saffire-1"]["ksor_doc"]
    _, cond_rows, _ = knowledge.table_under(m.ctx.repo_root, doc, "Full sample matrix — Saffire-1 / Saffire-2 (Table I, conditions)")
    _, res_rows, _ = knowledge.table_under(m.ctx.repo_root, doc, "Full sample matrix — Saffire-1 / Saffire-2 (Table I, ignition and results)")
    joined = alone = 0
    for row in cond_rows:
        run, inv, hit = _saffire_run(m, row["Sample"].strip())
        joined, alone = joined + hit, alone + (not hit)
        src = m.add_source(run, inv, "Table I (conditions)", row["__line__"], row)
        material = row["Material"].strip()
        m.category(run, "fuel_family", fuels.family(material), src, raw=material)
        if "fuel" not in run.conditions:
            m.category(run, "fuel", material, src)
        m.condition(run, "width_cm", parse_measure(row["Width"], "cm"), src)
        m.condition(run, "thickness_mm", to_mm(parse_measure(row["Thickness"], "mm")), src)
        m.condition(run, "length_cm", parse_measure(row["Length"], "cm"), src)
        m.condition(run, "flow_cm_s", parse_measure(row["Flow"], "cm/s"), src)
        m.category(run, "flow_direction", row["Direction"].strip().lower(), src, raw=row["Direction"].strip())
        o2 = pct(parse_measure(row["Initial O₂ (%)"], "%"))
        m.condition(run, "o2_pct", o2, src)
    for row in res_rows:
        run, inv, _ = _saffire_run(m, row["Sample"].strip())
        src = m.add_source(run, inv, "Table I (ignition and results)", row["__line__"], row)
        m.condition(run, "ignition_power_w", parse_measure(row["Ignition power"], "W"), src)
        m.condition(run, "ignition_time_s", parse_measure(row["Ignition time"], "s"), src)
        for col, q, unit, note in (
            ("µ-g burn duration", "burn_time", "s", None),
            ("µ-g spread extent", "spread_extent", "cm", None),
            ("µ-g spread rate", "spread_rate", "mm/s", None),
            ("1-g burn extent", "burn_extent_1g", "cm", "normal-gravity comparison test"),
            ("1-g spread rate", "spread_rate_1g", "mm/s", "normal-gravity comparison test"),
        ):
            cell = row[col].strip()
            mm = parse_measure(cell, unit)
            if mm is not None and mm.usable:
                m.outcome(run, Outcome(q, mm, source=src, note=note))
            elif cell and cell not in ("—", "-"):
                m.outcome(run, Outcome(q, text=cell, source=src, note=note))
    m.stat(f"{doc} Table I", len(cond_rows), joined, alone)


def saffire_iv_vi(m: Merger) -> None:
    inv = "saffire-iv-vi"
    doc = m.ctx.registry[inv]["ksor_doc"]
    _, cond_rows, _ = knowledge.table_under(m.ctx.repo_root, doc, "Full test matrix (Table 1: Saffire IV, V and VI")
    _, res_rows, _ = knowledge.table_under(m.ctx.repo_root, doc, "Measured outcomes (Table 2")
    for row in cond_rows:
        label = row["Flight/Sample"].strip()
        run = m.standalone(inv, label)
        src = m.add_source(run, inv, "Table 1", row["__line__"], row)
        material = row["Material"].strip()
        m.category(run, "fuel", material, src)
        m.category(run, "fuel_family", fuels.family(material), src, raw=material)
        m.category(run, "fuel_form", fuels.form(material), src)
        m.condition(run, "length_cm", parse_measure(row["Length (cm)"], "cm"), src)
        m.condition(run, "flow_cm_s", parse_measure(row["Air flow rate (cm/s)"], "cm/s"), src)
        m.category(run, "flow_direction", row["Flow direction"].strip().lower(), src, raw=row["Flow direction"].strip())
        m.condition(run, "pressure_atm", to_atm(parse_measure(row["Ambient pressure (kPa)"], "kPa"), "kPa"), src)
        m.condition(run, "o2_pct", pct(parse_measure(row["Oxygen concentration (mol %)"], "%")), src)
        m.condition(run, "free_volume_m3", parse_measure(row["Free volume (m³)"], "m³"), src)
    for row in res_rows:
        run = m.by_key.get((inv, row["Flight/Sample"].strip()))
        if run is None:
            continue
        src = m.add_source(run, inv, "Table 2", row["__line__"], row)
        for col, q, unit in (
            ("Burn duration (s)", "burn_time", "s"),
            ("Peak heat release (W)", "peak_heat_release", "W"),
            ("Total heat release, imaging method (kJ)", "total_heat_release_imaging", "kJ"),
            ("Average heat release, O₂-consumption method (W)", "avg_heat_release_o2", "W"),
            ("Total heat release, O₂-consumption method (kJ)", "total_heat_release_o2", "kJ"),
            ("Max temp at SFU outlet (°C)", "max_temp_sfu_outlet", "°C"),
            ("FFD inlet CO₂ increase (ppm)", "co2_increase_ppm", "ppm"),
            ("FFD inlet CO increase (ppm)", "co_increase_ppm", "ppm"),
        ):
            mm = parse_measure(row.get(col), unit)
            if mm is not None and mm.usable:
                m.outcome(run, Outcome(q, mm, source=src))
    m.stat(f"{doc} Tables 1–2 (Saffire IV–VI)", len(cond_rows), 0, len(cond_rows))


def flex_table_ix(m: Merger) -> None:
    doc = m.ctx.registry["flex"]["ksor_doc"]
    _, rows, _ = knowledge.table_under(m.ctx.repo_root, doc, "Full per-test results (Table IX)")
    # Joined on the CIR engineering identifier (e.g. "20CAL08"), not the test
    # number: the PSI table and the report's Table IX number their tests
    # differently from about FLEX-157 on, so a number join pairs different tests.
    by_ident: dict[str, list[Run]] = {}
    for r in m.runs:
        if r.investigation == "flex" and r.conditions.get("identifier"):
            by_ident.setdefault(r.conditions["identifier"]["value"], []).append(r)
    joined = alone = 0
    for row in rows:
        label = row["Test"].strip()
        cands = by_ident.get(row["Identifier"].strip(), [])
        if len(cands) > 1:
            # One identifier, several tests (193F001 is both FLEX-070 and
            # FLEX-073): break the tie on test number AND initial droplet
            # diameter, both of which must agree. Left unjoined, each test
            # was counted twice (seen 2026-09-24).
            d0 = parse_measure(row["Initial diameter (mm)"], "mm")
            cands = [r for r in cands if r.label == label and d0 is not None and d0.usable
                     and (r.conditions.get("droplet_d0_mm") is not None)
                     and abs(r.conditions["droplet_d0_mm"].value - d0.value) < 1e-9]
        run = cands[0] if len(cands) == 1 else None
        if run is None:
            run, alone = m.standalone("flex", f"{label} (report)"), alone + 1
            run.conditions["identifier"] = cat(row["Identifier"].strip())
        else:
            joined += 1
            if run.label != label:
                run.notes.append(f"report Table IX numbers this test {label}; the PSI table numbers it {run.label}")
        src = m.add_source(run, "flex", "Table IX", row["__line__"], row)
        fuel = row["Fuel"].strip()
        m.category(run, "fuel", fuel, src)
        m.category(run, "fuel_family", fuels.family(fuel), src, raw=fuel)
        m.category(run, "fuel_form", "droplet", src)
        m.condition(run, "pressure_atm", to_atm(parse_measure(row["Pressure (mmHg)"], "mmHg"), "mmHg"), src)
        for col, key in (("O2", "o2_pct"), ("N2", "n2_pct"), ("CO2", "co2_pct"), ("He", "he_pct")):
            cell = row[col].strip()
            if cell.lower() == "not stated":
                continue
            fr = parse_measure(cell)
            if fr is not None and fr.usable and (fr.max or 0) <= 1:
                m.condition(run, key, fr.scaled(100, "%", "mole_fraction_to_pct"), src)
        m.condition(run, "droplet_d0_mm", parse_measure(row["Initial diameter (mm)"], "mm"), src)
        for col, q, unit in (("Extinction diameter (mm)", "extinction_diameter", "mm"),
                             ("Burning rate (mm2/s)", "burning_rate_k", "mm²/s"),
                             ("Burn time (s)", "burn_time", "s")):
            mm = parse_measure(row[col], unit)
            if mm is not None and mm.usable:
                m.outcome(run, Outcome(q, mm, source=src))
        if row["Test end"].strip():
            m.outcome(run, Outcome("test_end", text=row["Test end"].strip(), source=src))
    m.stat(f"{doc} Table IX", len(rows), joined, alone)


EXTRACTED = "psi-data/extracted/report-outcomes.csv"


# field → (kind, unit): how an extracted value enters the run
EXTRACTED_FIELDS = {
    "flow_direction": ("category", None),
    "fuel": ("category", None),
    "observation": ("text", None),
    "nozzle_diameter_mm": ("condition", "mm"),
    "flow_cm_s": ("condition", "cm/s"),
    "sample_temperature_c": ("condition", "°C"),
    "smoke_point_length": ("outcome", "mm"),
    "smoke_points_observed": ("outcome", "smoke points"),
    "tem_particles_counted": ("outcome", "particles"),
}


def _report_citation(m: Merger, inv: str, source_file: str) -> dict:
    reg = m.ctx.registry[inv]
    if reg["ksor_doc"] and reg["source_id"]:
        c = knowledge.citation(m.ctx.repo_root, reg["ksor_doc"], reg["source_id"])
        return {k: c.get(k) for k in ("doc", "doc_title", "doc_status", "source_id", "title", "url")}
    # No governed document for this investigation: cite the report file itself.
    return {"title": Path(source_file).stem, "url": None}


def extracted_report_values(m: Merger) -> None:
    """Values pulled straight from converted report text (psi-extract), each
    already verified verbatim against that text. Unlike the knowledge/ tables
    these have not been through the record's human review, so the source says
    exactly where they came from: the report, its table and page, the file."""
    rows = verify.load_verified(m.ctx.repo_root, m.ctx.repo_root / EXTRACTED)
    by_run: dict[tuple[str, str], list[dict]] = {}
    for r in rows:
        by_run.setdefault((r["investigation"], r["run_label"]), []).append(r)
    joined = alone = 0
    for (inv, label), rs in by_run.items():
        run = m.by_key.get((inv, label))
        if run is None:
            run, alone = m.standalone(inv, label, granularity=rs[0]["granularity"] or "test"), alone + 1
            if run.granularity == "summary":
                run.notes.append("per-fuel summary across many tests, as the report tabulates it — not one test")
        else:
            joined += 1
        src_index: dict[tuple[str, str], int] = {}
        for r in rs:
            key = (r["table"], r["page"])
            if key not in src_index:
                run.sources.append({
                    "kind": "report", "table": r["table"] + (f", p. {r['page']}" if r["page"] else ""), "line": None,
                    "via": r["source_file"], "extraction": "verbatim cell from converted report text",
                    **_report_citation(m, inv, r["source_file"]),
                })
                run.raw.append({})
                src_index[key] = len(run.sources) - 1
            src = src_index[key]
            run.raw[src][r["field"] + (f" ({r['qualifier']})" if r["qualifier"] else "")] = r["verbatim"]
            kind, unit = EXTRACTED_FIELDS[r["field"]]
            if kind == "category":
                value = r["value"]
                if r["field"] == "fuel":
                    m.category(run, "fuel_family", fuels.family(value), src, raw=value)
                m.category(run, r["field"], value, src, raw=r["verbatim"])
            elif kind == "text":
                m.outcome(run, Outcome(r["field"], text=r["value"], source=src))
            elif kind == "condition":
                cm = parse_measure(r["value"], unit)
                if cm is not None and run.granularity == "summary" and "range" in cm.flags:
                    cm.flag("range_across_tests")
                m.condition(run, r["field"], cm, src)
            else:
                om = parse_measure(r["value"], unit)
                quantity = r["field"]
                if quantity == "tem_particles_counted":
                    # aged and unaged smoke from one test are two measurements,
                    # not two sources disagreeing about one
                    quantity = f"{quantity}_{r['qualifier']}"
                m.outcome(run, Outcome(quantity, om, source=src))
    m.stat(EXTRACTED, len(rows), joined, alone)


def merge_all(ctx: Ctx, runs: list[Run]) -> list[dict]:
    m = Merger(ctx, runs)
    for step in (bass_ii_table_5_1, bass_ii_table_7_1, saffire_table_i, saffire_iv_vi, flex_table_ix,
                 extracted_report_values):
        step(m)
    return m.stats
