"""Condition query over the unified PSI run table (data/runs.json, generated
by system/psi-ingest — never hand-edited).

"What do all the experiments say about ~15 % O2, ~10 cm/s, PMMA?" is answered
in three tiers plus a coverage/gap report, never as one number:

  match    every requested axis is reported and within tolerance
  partial  every axis the run REPORTS is within tolerance, but it doesn't
           report at least one requested axis (e.g. BASS-II flow is a fan
           setting, not cm/s) — evidence with a stated hole, not a match
  near     the closest remaining runs, with the per-axis gap spelled out

Categorical filters (fuel family, geometry class, flow direction, …) are
hard: a SIBAL test is not "near" a PMMA question. What the filter removed is
still reported (`relaxed`) so an empty answer says where data DOES exist.

This module is mirrored in TypeScript at system/site/lib/psi-query.ts; both
run the golden cases in psi-data/query-fixtures.json. Change them together.
"""

from __future__ import annotations

import json
import math
import os
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

import yaml

import psi_atmospheres

# axis → (tolerance kind, default tolerance, unit)
NUMERIC_AXES: dict[str, tuple[str, float, str]] = {
    "o2_pct": ("abs", 1.5, "%"),
    "flow_cm_s": ("rel", 0.3, "cm/s"),
    "pressure_atm": ("abs", 0.1, "atm"),
    "thickness_mm": ("rel", 0.5, "mm"),
    "droplet_d0_mm": ("rel", 0.25, "mm"),
}
CATEGORICAL_AXES = ("fuel_family", "geometry_class", "flow_direction", "fuel_form", "investigation")
MISSING_PENALTY = 1.5  # a missing axis ranks like being 1.5 tolerances away

GRANULARITY_RANK = {"test": 0, "test-point": 0, "day": 1, "summary": 1, "envelope": 2}

# Display order: the flame-behavior results first, bookkeeping readings last.
OUTCOME_PRIORITY = [
    "spread_rate", "burning_rate_k", "burning_rate_k_hot", "burning_rate_k_cool", "extinction_diameter",
    "extinction_diameter_hot", "extinction_diameter_cool", "end_mode", "test_end", "ignited", "hot_ignition",
    "cool_flame", "burn_time", "burn_time_hot_flame", "spread_extent", "peak_heat_release", "flames_ignited",
    "weight_loss_rate", "spread_rate_1g", "burn_extent_1g",
]

_DATA_DIR = Path(os.environ.get("PSI_DATA_DIR", Path(__file__).resolve().parent / "data"))


@lru_cache(maxsize=1)
def load() -> tuple[list[dict], dict[str, dict]]:
    runs = json.loads((_DATA_DIR / "runs.json").read_text(encoding="utf-8"))["runs"]
    invs = json.loads((_DATA_DIR / "investigations.json").read_text(encoding="utf-8"))["investigations"]
    return runs, {i["id"]: i for i in invs}


def _cat_match(run: dict, key: str, want: str, invs: dict[str, dict]) -> bool:
    """Case-insensitive. fuel_family matches by prefix ("sibal" → "SIBAL
    (cotton-fiberglass)", "wax" → every wax); investigation by id or name."""
    if key == "investigation":
        inv = invs[run["investigation"]]
        return want in (inv["id"].lower(), inv["name"].lower())
    have = (_cat_value(run, key, invs) or "").lower()
    return have.startswith(want) if key == "fuel_family" else have == want


def _cat_value(run: dict, key: str, invs: dict[str, dict]) -> str | None:
    if key == "investigation":
        return run["investigation"]
    if key == "geometry_class":
        return invs[run["investigation"]]["geometry_class"]
    c = run["conditions"].get(key)
    return c.get("value") if isinstance(c, dict) else None


def _norm_distance(axis: str, target: float, m: dict, tol: float) -> float | None:
    """Distance in tolerances (0 = inside the run's value/interval). None = not reported."""
    if m is None or m.get("min") is None:
        return None
    kind = NUMERIC_AXES[axis][0]
    scale = tol * abs(target) if kind == "rel" and target else tol
    if "multi" in m.get("flags", []) and m.get("values"):
        d = min(abs(v - target) for v in m["values"])
    else:
        lo, hi = m["min"], m["max"]
        d = 0.0 if lo <= target <= hi else min(abs(target - lo), abs(target - hi))
    return d / scale if scale else (0.0 if d == 0 else math.inf)


def _citation(run: dict, invs: dict[str, dict]) -> list[dict]:
    out = []
    for s in run["sources"]:
        if s["kind"] in ("psi", "psi-workbook"):
            out.append({"kind": "psi", "dataset": s["dataset"], "file": s["file"], "row": s["row"],
                        **({"sheet": s["sheet"]} if s.get("sheet") else {})})
        elif s["kind"] == "report":
            out.append({"kind": "report", "title": s.get("title"), "url": s.get("url"), "table": s["table"],
                        "doc": s.get("doc")})
    return out


def _outcome_summary(run: dict, q: dict) -> list[dict]:
    """Outcomes, and for values measured at several flows, the one nearest the requested flow first."""
    target_flow = q.get("flow_cm_s")
    outs = []
    for o in run["outcomes"]:
        entry = {"quantity": o["quantity"]}
        if "measure" in o:
            m = o["measure"]
            entry["value"] = m.get("value")
            entry["raw"] = m["raw"]
            if m.get("min") is not None and m.get("max") is not None and m["min"] != m["max"]:
                entry["min"], entry["max"] = m["min"], m["max"]
            entry["unit"] = m.get("unit")
            if m.get("values") and m.get("value") is None:
                entry["values"] = m["values"]
            if o.get("text"):  # e.g. a FLEX 0 that means "no visible extinction", not 0 mm
                entry["text"] = o["text"]
        else:
            entry["text"] = o.get("text")
        if o.get("at"):
            entry["at"] = o["at"]
        if o.get("note"):
            entry["note"] = o["note"]
        if o.get("confirmed_by"):
            entry["confirmed_by_second_source"] = True
        outs.append(entry)
    rank = {q: i for i, q in enumerate(OUTCOME_PRIORITY)}
    tf = target_flow if target_flow is not None else 0.0
    outs.sort(key=lambda e: (rank.get(e["quantity"], len(rank)),
                             abs(e.get("at", {}).get("flow_cm_s", math.inf) - tf) if target_flow is not None else 0))
    return outs


def _run_view(run: dict, invs: dict[str, dict], axes: dict, tier: str, score: float, q: dict) -> dict:
    inv = invs[run["investigation"]]
    c = run["conditions"]
    return {
        "id": run["id"],
        "investigation": inv["name"],
        "investigation_id": inv["id"],
        "geometry_class": inv["geometry_class"],
        "label": run["label"],
        "granularity": run["granularity"],
        "tier": tier,
        "distance": round(score, 3),
        "fuel": (c.get("fuel") or {}).get("value"),
        "fuel_family": (c.get("fuel_family") or {}).get("value"),
        "flow_direction": (c.get("flow_direction") or {}).get("value"),
        "axes": axes,
        "outcomes": _outcome_summary(run, q),
        "conflicts": run.get("conflicts", []),
        "notes": run.get("notes", []),
        "citations": _citation(run, invs),
    }


def query(q: dict, tolerances: dict | None = None, near_limit: int = 10, runs=None, invs=None) -> dict:
    """q: any of NUMERIC_AXES → number, CATEGORICAL_AXES → string (case-insensitive)."""
    if runs is None or invs is None:
        runs, invs = load()
    tol = {k: v[1] for k, v in NUMERIC_AXES.items()} | (tolerances or {})
    num_q = {k: float(v) for k, v in q.items() if k in NUMERIC_AXES and v is not None}
    cat_q = {k: str(v).lower() for k, v in q.items() if k in CATEGORICAL_AXES and v}

    matched, partial, near = [], [], []
    relaxed: Counter = Counter()
    considered_invs: set[str] = set()
    for run in runs:
        cat_ok = all(_cat_match(run, k, v, invs) for k, v in cat_q.items())
        axes, dists, missing = {}, [], []
        for axis, target in num_q.items():
            m = run["conditions"].get(axis)
            d = _norm_distance(axis, target, m, tol[axis])
            if d is None:
                missing.append(axis)
                axes[axis] = {"status": "not_reported"}
                continue
            dists.append(d)
            axes[axis] = {"status": "within" if d <= 1 else "outside", "raw": m["raw"], "min": m["min"],
                          "max": m["max"], "unit": m.get("unit"), "distance": round(d, 3),
                          **({"flags": m["flags"]} if m.get("flags") else {})}
        within = all(d <= 1 for d in dists)
        if not cat_ok:
            if num_q and within and not missing:
                relaxed[(_cat_value(run, "fuel_family", invs) or "unassigned", invs[run["investigation"]]["name"])] += 1
            continue
        considered_invs.add(run["investigation"])
        score = math.sqrt(sum(d * d for d in dists) + MISSING_PENALTY ** 2 * len(missing))
        if not num_q:
            matched.append((0.0, run, axes))
        elif within and not missing:
            matched.append((score, run, axes))
        elif within and dists:
            partial.append((score, run, axes))
        else:
            near.append((score, run, axes))

    # Individual tests outrank daily summaries, which outrank planned
    # envelopes: a matrix row "0.17–0.30 O2" is not a test at 0.30. Then by
    # distance, then id (deterministic order for the golden tests).
    key = lambda t: (GRANULARITY_RANK.get(t[1]["granularity"], 9), t[0], t[1]["id"])  # noqa: E731
    matched.sort(key=key)
    partial.sort(key=key)
    near.sort(key=key)
    return {
        "query": {**num_q, **cat_q},
        "tolerances": {k: {"kind": NUMERIC_AXES[k][0], "value": tol[k], "unit": NUMERIC_AXES[k][2]} for k in num_q},
        "counts": {"match": len(matched), "partial": len(partial), "near_pool": len(near)},
        "match": [_run_view(r, invs, a, "match", s, q) for s, r, a in matched],
        "partial": [_run_view(r, invs, a, "partial", s, q) for s, r, a in partial],
        "near": [_run_view(r, invs, a, "near", s, q) for s, r, a in near[:near_limit]],
        "coverage": _coverage(runs, invs, num_q, cat_q, considered_invs),
        "relaxed": [{"fuel_family": f, "investigation": i, "runs": n} for (f, i), n in relaxed.most_common()],
        "geometry_classes": sorted({invs[r["investigation"]]["geometry_class"] for _, r, _ in matched + partial}),
    }


def _coverage(runs, invs, num_q, cat_q, considered) -> list[dict]:
    """Per investigation (among those passing the categorical filters): what
    range each requested axis spans, and whether the target falls inside it."""
    by_inv: dict[str, list[dict]] = defaultdict(list)
    for r in runs:
        if r["investigation"] in considered:
            if all(_cat_match(r, k, v, invs) for k, v in cat_q.items()):
                by_inv[r["investigation"]].append(r)
    out = []
    for inv_id, rs in sorted(by_inv.items(), key=lambda kv: invs[kv[0]]["name"]):
        axes = {}
        for axis, target in num_q.items():
            ms = [r["conditions"][axis] for r in rs if r["conditions"].get(axis, {}).get("min") is not None]
            if not ms:
                reported_as = sorted({k for r in rs for k in r["conditions"] if k.startswith("flow_setting")}) if axis == "flow_cm_s" else []
                axes[axis] = {"reported_by": 0, "of": len(rs),
                              "statement": "not reported" + (f" (only as control-panel settings: {', '.join(reported_as)})" if reported_as else "")}
                continue
            lo, hi = min(m["min"] for m in ms), max(m["max"] for m in ms)
            axes[axis] = {"reported_by": len(ms), "of": len(rs), "min": lo, "max": hi,
                          "target_in_range": lo <= target <= hi}
        out.append({"investigation": invs[inv_id]["name"], "investigation_id": inv_id,
                    "geometry_class": invs[inv_id]["geometry_class"], "runs": len(rs), "axes": axes})
    return out


# Which (geometry class, quantity) pairs have enough numeric runs to rank.
# Solid fuels have no numeric extinction outcome (only end_mode/ignited text)
# and report pressure on almost no runs; smoke-aerosol has no measured
# quantity comparable across materials. Ranking never crosses a class.
RANKABLE: dict[str, list[str]] = {
    "solid-fuel": ["spread_rate"],
    "droplet-combustion": ["burning_rate_k", "extinction_diameter"],
    "gaseous-flames": ["burn_time", "peak_burner_temp_c"],
}


def _outcome_value(o: dict) -> float | None:
    """A single number to rank by: the stated value, else a range's midpoint
    (never a number the source states outright), else the median of several
    stated values. Text-only outcomes (e.g. end_mode="blow-off") return None."""
    if o.get("value") is not None:
        return o["value"]
    if o.get("min") is not None and o.get("max") is not None:
        return (o["min"] + o["max"]) / 2
    if o.get("values"):
        vs = sorted(o["values"])
        n = len(vs)
        return vs[n // 2] if n % 2 else (vs[n // 2 - 1] + vs[n // 2]) / 2
    return None


def rank(q: dict, quantity: str, geometry_class: str, direction: str = "desc", limit: int = 10,
         runs=None, invs=None) -> dict:
    """Rank materials within ONE geometry class by a measured quantity, at
    conditions given by q (any NUMERIC_AXES/CATEGORICAL_AXES key). Aggregates
    per fuel_family as (n, min, median, max) over every match/partial run
    reporting that quantity — never merges runs into one number silently;
    every row keeps its run ids. `untested` lists materials in the class with
    no run at these conditions, so an empty top spot is visible, not silent."""
    if geometry_class not in RANKABLE or quantity not in RANKABLE[geometry_class]:
        return {"error": f"{quantity!r} is not a rankable result for {geometry_class!r}",
                "rankable": RANKABLE.get(geometry_class, [])}
    if runs is None or invs is None:
        runs, invs = load()
    full_q = {**q, "geometry_class": geometry_class}
    result = query(full_q, runs=runs, invs=invs)

    by_material: dict[str, list[dict]] = defaultdict(list)
    target_flow = q.get("flow_cm_s", 0.0)
    for tier in ("match", "partial"):
        for v in result[tier]:
            # A run may report this quantity at several flow settings (e.g.
            # BASS-II spread rate); one contribution per run, the entry
            # nearest the requested flow (0 if none given) — tie-broken by
            # the flow value itself so the pick is independent of list order,
            # which the TS twin (reading the same JSON) cannot rely on
            # matching v["outcomes"]'s Python-side _outcome_summary sort.
            candidates = [o for o in v["outcomes"] if o["quantity"] == quantity and _outcome_value(o) is not None]
            if not candidates:
                continue
            o = min(candidates, key=lambda o: (abs(o.get("at", {}).get("flow_cm_s", target_flow) - target_flow),
                                               o.get("at", {}).get("flow_cm_s", target_flow)))
            fam = v["fuel_family"] or "unassigned"
            by_material[fam].append({"run_id": v["id"], "investigation": v["investigation"],
                                     "tier": v["tier"], "value": _outcome_value(o), "unit": o.get("unit")})

    rows = []
    for fam, entries in by_material.items():
        vals = sorted(e["value"] for e in entries)
        n = len(vals)
        median = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
        rows.append({
            "fuel_family": fam, "n": n, "min": round(vals[0], 4), "max": round(vals[-1], 4),
            "median": round(median, 4), "unit": entries[0].get("unit"),
            "runs": [e["run_id"] for e in entries][:8],
            "investigations": sorted({e["investigation"] for e in entries}),
        })
    rows.sort(key=lambda r: (-r["median"] if direction == "desc" else r["median"], r["fuel_family"]))

    ranked_families = {r["fuel_family"] for r in rows}
    all_families = {(_cat_value(r, "fuel_family", invs) or "unassigned") for r in runs
                    if invs[r["investigation"]]["geometry_class"] == geometry_class}
    return {
        "query": full_q, "quantity": quantity, "geometry_class": geometry_class, "direction": direction,
        "rows": rows[:limit], "total_ranked": len(rows),
        "untested": sorted(all_families - ranked_families),
        "coverage": result["coverage"],
    }


def compact_rank(result: dict, max_rows: int = 10) -> dict:
    """The LLM-facing view of rank(): small and already formatted, never asks
    the model to compute or restate a median itself."""
    if result.get("error"):
        return result
    return {
        "quantity": result["quantity"], "geometry_class": result["geometry_class"],
        "query": result["query"], "direction": result["direction"], "total_ranked": result["total_ranked"],
        "top": [{"material": r["fuel_family"], "n": r["n"],
                 "median": f"{r['median']:g}" + (f" {r['unit']}" if r["unit"] else ""),
                 "range": f"{r['min']:g}–{r['max']:g}" + (f" {r['unit']}" if r["unit"] else ""),
                 "runs": r["runs"][:4]} for r in result["rows"][:max_rows]],
        "untested_at_these_conditions": result["untested"][:10],
    }


def prefer_outcomes(views: list[dict]) -> list[dict]:
    """Display order only (the query's own ranking is untouched, and is what
    the golden fixtures pin): within a tier, runs that carry measured numeric
    results first. Text-only outcomes (e.g. test_end=Disruption) rank below
    numeric ones. Otherwise 342 SPICE test points with no results bury the five
    per-fuel summaries that hold the smoke points."""
    def has_numeric(v: dict) -> bool:
        for o in v["outcomes"]:
            if o.get("value") is not None or o.get("values") or (o.get("min") is not None and o.get("max") is not None):
                return True
        return False
    return sorted(views, key=lambda v: not has_numeric(v))


def _fmt_outcome(o: dict) -> str:
    """Normalized value + unit (the raw cell may be in another unit, e.g. minutes)."""
    if o.get("min") is not None and o.get("max") is not None and o.get("at") is None:
        # a range stays a range: its midpoint is a number no source states
        val = f"{o['min']:g}–{o['max']:g}" + (f" {o['unit']}" if o.get("unit") else "")
    elif o.get("value") is not None:
        val = f"{o['value']:g}" + (f" {o['unit']}" if o.get("unit") else "")
    elif o.get("values"):
        val = ", ".join(f"{x:g}" for x in o["values"]) + (f" {o['unit']}" if o.get("unit") else "")
    else:
        val = o.get("text") or o.get("raw") or "?"
    at = f" @ {o['at']['flow_cm_s']:g} cm/s" if o.get("at") else ""
    return f"{o['quantity']}={val}{at}"


def _axis_for_compact(a: dict) -> str:
    """Format axis for compact view: normalized value with source cell if converted."""
    if a["status"] == "not_reported":
        return "not_reported"
    raw = a.get("raw", "")
    flags = a.get("flags", [])
    unit = a.get("unit") or ""
    conv_flag = next((f for f in flags if f.startswith("converted_from_")), None)
    mole_flag = "mole_fraction_to_pct" in flags
    if conv_flag or mole_flag:
        if a.get("min") is not None and a.get("max") is not None:
            if a["min"] == a["max"]:
                return f"{a['min']:g} {unit} (cell {raw})"
            return f"{a['min']:g}–{a['max']:g} {unit} (cell {raw})"
    return raw + (f" {unit}" if unit and unit not in raw else "")


def compact(result: dict, max_runs: int = 10) -> dict:
    """The LLM-facing view: small enough for a tight token budget, still cited.
    The widget renders the full result; the model only needs enough to write
    a one-paragraph, cited summary."""

    def slim(v: dict) -> dict:
        cite = next((c for c in v["citations"] if c["kind"] == "psi"), v["citations"][0] if v["citations"] else {})
        # The run id already names the dataset and test; dataset + line is the
        # handle a reader opens the CSV at.
        cite_s = f"{cite.get('dataset')} line {cite.get('row')}" if cite.get("kind") == "psi" else \
            f"{cite.get('title')}, {cite.get('table')}"
        return {
            "id": v["id"], "inv": v["investigation"], "fuel": v["fuel"],
            **({"granularity": v["granularity"]} if v["granularity"] not in ("test", "test-point") else {}),
            "axes": {k: _axis_for_compact(a) for k, a in v["axes"].items()},
            "outcomes": [_fmt_outcome(o) for o in v["outcomes"][:3]],
            "conflicts": len(v["conflicts"]),
            "cite": cite_s,
        }

    budget = max_runs
    picks = {}
    for tier in ("match", "partial", "near"):
        picks[tier] = [slim(v) for v in prefer_outcomes(result[tier])[:budget]]
        budget -= len(picks[tier])
        budget = max(budget, 2)  # always show a couple from each remaining tier
    measured = Counter(o["quantity"] for t in ("match", "partial") for v in result[t] for o in v["outcomes"])
    return {
        "query": result["query"],
        "counts": result["counts"],
        # across ALL matching/partial runs, not just the ones listed below — so
        # "no values recorded" can never be concluded from a truncated list
        "results_recorded": dict(measured.most_common(8)),
        **picks,
        "coverage": [
            {"inv": c["investigation"], "runs": c["runs"],
             **{k: (a.get("statement") or f"{a['min']}–{a['max']} ({a['reported_by']}/{a['of']} runs){'' if a['target_in_range'] else ' — target OUTSIDE tested range'}")
                for k, a in c["axes"].items()}}
            for c in result["coverage"][:10]
        ],
        "relaxed": result["relaxed"][:5],
        "geometry_classes": result["geometry_classes"],
    }


# ── Mission readiness ────────────────────────────────────────────────────────
# How much of a named mission atmosphere (psi_atmospheres.py) the PSI data
# actually covers, per geometry class — computed here, never asserted by the
# model. Paired in the widget with governed-doc quotes from
# psi-data/findings.yaml, each checked verbatim against its doc by
# tests/test_findings.py. This view adds no new fact: it is the existing
# query() tiers, reshaped, next to what the record already says about why a
# gap matters.

_FINDINGS_PATH = Path(__file__).resolve().parents[2] / "psi-data" / "findings.yaml"


@lru_cache(maxsize=1)
def _findings() -> list[dict]:
    if not _FINDINGS_PATH.is_file():
        return []
    return yaml.safe_load(_FINDINGS_PATH.read_text(encoding="utf-8")) or []


def readiness(atm_id: str, runs=None, invs=None) -> dict:
    atm = psi_atmospheres.ATMOSPHERES.get(atm_id)
    if atm is None:
        return {"error": f"Unknown atmosphere {atm_id!r}", "known": sorted(psi_atmospheres.ATMOSPHERES)}
    if runs is None or invs is None:
        runs, invs = load()
    base_q = {"o2_pct": atm["o2_pct"], "pressure_atm": atm["pressure_atm"]}

    classes = []
    for gc in sorted({i["geometry_class"] for i in invs.values()}):
        result = query({**base_q, "geometry_class": gc}, runs=runs, invs=invs)
        best_pool = result["match"] or result["partial"] or result["near"]
        nearest = None
        if best_pool:
            b = best_pool[0]
            nearest = {"run_id": b["id"], "investigation": b["investigation"], "tier": b["tier"],
                      "o2_pct": (b["axes"].get("o2_pct") or {}).get("min"),
                      "pressure_atm": (b["axes"].get("pressure_atm") or {}).get("min")}
        quantities = sorted({o["quantity"] for v in (result["match"] + result["partial"]) for o in v["outcomes"]
                             if o.get("value") is not None
                             or (o.get("min") is not None and o.get("max") is not None) or o.get("values")})
        classes.append({
            "geometry_class": gc, "match": result["counts"]["match"], "partial": result["counts"]["partial"],
            "near_pool": result["counts"]["near_pool"],
            "covered": result["counts"]["match"] > 0 or result["counts"]["partial"] > 0,
            "nearest_tested": nearest, "quantities_available": quantities,
        })

    findings = [f for f in _findings() if f.get("atmosphere") in (None, atm_id)]
    return {"atmosphere": atm, "query": base_q, "classes": classes, "findings": findings}


def compact_readiness(result: dict) -> dict:
    if result.get("error"):
        return result
    atm = result["atmosphere"]

    def nearest_str(n: dict | None) -> str | None:
        if n is None:
            return None
        o2 = f"{n['o2_pct']:g}% O2" if n["o2_pct"] is not None else "O2 not reported"
        p = f"{n['pressure_atm']:g} atm" if n["pressure_atm"] is not None else "pressure not reported"
        return f"{o2}, {p} ({n['tier']}, {n['investigation']})"

    return {
        "atmosphere": {"id": atm["id"], "label": atm["label"], "o2_pct": atm["o2_pct"], "pressure_atm": atm["pressure_atm"]},
        "classes": [{"geometry_class": c["geometry_class"], "match": c["match"], "partial": c["partial"],
                    "covered": c["covered"], "nearest_tested": nearest_str(c["nearest_tested"]),
                    "quantities": c["quantities_available"][:6]} for c in result["classes"]],
        "findings": [{"quote": f["quote"].strip(), "doc_title": f["doc_title"], "geometry_class": f.get("geometry_class")}
                     for f in result["findings"]],
    }
