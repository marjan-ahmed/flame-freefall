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
import re
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
# Sentinel score for a near-tier run reporting NONE of the query's axes: it
# is not "near" in any measured sense and must sort after every run that
# reports the axis, however far off that reading is. Finite (not inf) so it
# stays ordinary JSON.
NO_AXES_REPORTED_SCORE = 1e6
# A target exactly one tolerance-width from a run's value must match from
# either side. Plain float division (e.g. (1.1-1.0)/0.1) can land a hair
# above 1.0, excluding it on one side only; this absorbs that noise without
# ever admitting a run genuinely outside tolerance.
TOLERANCE_EPS = 1e-9

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


# A trailing roman numeral, converted to its arabic digit -- so a real name
# ending in one ("BASS-II") also answers to an informally arabic-typed query
# ("BASS 2"). One-directional on purpose (see _investigation_ids): only ever
# applied to the CANDIDATE id/name, never to the query itself, so a query
# that itself uses a roman numeral ("SAFFIRE-II") is never treated as an
# alias of an arabic-named investigation (SAFFIRE-2) -- that is a genuinely
# wrong name, not an alias, and must stay unresolved.
_ROMAN_TO_ARABIC = {"i": "1", "ii": "2", "iii": "3", "iv": "4", "v": "5",
                    "vi": "6", "vii": "7", "viii": "8", "ix": "9", "x": "10"}
_TRAILING_NUMERAL_RE = re.compile("(" + "|".join(sorted(_ROMAN_TO_ARABIC, key=len, reverse=True)) + r")$")
_ALNUM = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())  # noqa: E731


def _numeral_canon(s: str) -> str:
    """Alphanumeric-only, with a trailing ROMAN numeral (only) converted to
    arabic. A tail that's already a plain digit, or no numeral at all, is
    returned as-is -- this never invents an arabic->roman direction."""
    base = _ALNUM(s)
    m = _TRAILING_NUMERAL_RE.search(base)
    return base[:m.start()] + _ROMAN_TO_ARABIC[m.group(1)] if m else base


def _investigation_ids(name: str, invs: dict[str, dict]) -> set[str]:
    """Investigation ids a user/model name resolves to. An exact id or name
    match wins ("BASS" is BASS, not BASS-II); otherwise a family name matches
    every member ("SAFFIRE" -> SAFFIRE-1/-2/-3/IV-VI, "ACME" -> every ACME
    experiment); otherwise a hyphen-insensitive exact match ("FLEX 2" ->
    FLEX-2); otherwise, if the query itself ends in a plain arabic digit
    (never a roman numeral -- see _numeral_canon), a candidate whose OWN
    trailing roman numeral converts to that digit ("BASS 2" -> BASS-II).
    One resolver shared by query()'s investigation filter and
    psi_widgets.compare_data/results_data, so all three agree on what a name
    means (see AGENTS.md/C7 -- they used to disagree). A blank name resolves
    to nothing, never to "every investigation" (every id/name trivially
    starts with ""); query()'s own callers already filter blanks out before
    this point, but compare_data's investigations list does not, and a stray
    "" there must not silently defeat a real filter it's unioned with."""
    if not name or not name.strip():
        return set()
    norm = lambda s: s.lower().replace(" ", "").replace("_", "-")  # noqa: E731
    n = norm(name)
    exact = {i for i, inv in invs.items() if n in (norm(i), norm(inv["name"]))}
    if exact:
        return exact
    prefix = {i for i, inv in invs.items() if norm(i).startswith(n) or norm(inv["name"]).startswith(n)}
    if prefix:
        return prefix
    an = _ALNUM(name)
    alnum_exact = {i for i, inv in invs.items() if an in (_ALNUM(i), _ALNUM(inv["name"]))}
    if alnum_exact:
        return alnum_exact
    if not re.search(r"\d$", an):  # query doesn't end in a plain digit: no roman-alias attempt
        return set()
    return {i for i, inv in invs.items() if an == _numeral_canon(i) or an == _numeral_canon(inv["name"])}


def _cat_match(run: dict, key: str, want: str, invs: dict[str, dict]) -> bool:
    """Case-insensitive identity matching; an explicit trailing * requests
    a broader fuel/constituent prefix, including blends. SIBAL is a named alias,
    not permission to include every fuel that starts with a pure fuel's name."""
    if key == "investigation":
        return run["investigation"] in _investigation_ids(want, invs)
    have = (_cat_value(run, key, invs) or "").lower()
    if key == "fuel_family":
        if want.endswith("*"):
            prefix = want[:-1].strip()
            return bool(prefix) and (have.startswith(prefix) or any(part.strip().startswith(prefix) for part in have.split("/")))
        want = {"sibal": "sibal (cotton-fiberglass)"}.get(want, want)
    return have == want


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


def _source_ref(s: dict) -> dict:
    """One run source, in the shape _citation() gives it."""
    if s["kind"] == "report":
        return {"kind": "report", "title": s.get("title"), "table": s["table"]}
    return {"kind": s["kind"], "dataset": s["dataset"], "row": s.get("row"),
            **({"sheet": s["sheet"]} if s.get("sheet") else {})}


def source_label(ref: dict, report_keys: dict[tuple[str, str], str] | None = None) -> str:
    """Where ONE value came from. A report is named by its table and title
    (or, keyed by (table, title) into a short numeric tag, to keep a payload
    with many repeated citations of the same table small -- see the
    compact()-payload budget note in AGENTS.md)."""
    if ref["kind"] == "report":
        if report_keys is not None:
            return f"report {report_keys[(ref['table'], ref['title'])]}"
        return f"{ref['table']}, {ref['title']}"
    if ref["kind"] == "psi-workbook":
        return f"{ref['dataset']} workbook sheet {ref.get('sheet')} row {ref['row']}"
    return f"{ref['dataset']} line {ref['row']}"


def sourced_conflicts(run: dict) -> list[dict]:
    """A run's conflicts (condition or outcome), with each disagreeing value
    tagged by the source that actually reported it -- e.g. "PSI-99 line 7:
    20 cm/s" vs "Table I (conditions), Results of Large-Scale Spacecraft
    Flammability Tests: 25 cm/s" -- instead of a bare {"source": 0}/{"source":
    1} the model would have to guess at. BOTH values are always kept; neither
    is chosen."""
    out = []
    for c in run.get("conflicts", []):
        tagged = [{**{k: val for k, val in v.items() if k != "source"},
                   "source": source_label(_source_ref(run["sources"][v["source"]]))}
                  for v in c["values"]]
        out.append({"field": c["field"], "values": tagged})
    return out


def _outcome_summary(run: dict, q: dict) -> list[dict]:
    """Outcomes, and for values measured at several flows, the one nearest the requested flow first.
    Each carries `from` (and `also_from` when a second source agrees): the source
    that actually holds that value — never inferred from the run's other sources."""
    target_flow = q.get("flow_cm_s")
    outs = []
    for o in run["outcomes"]:
        entry = {"quantity": o["quantity"], "from": _source_ref(run["sources"][o["source"]])}
        if o.get("confirmed_by"):
            entry["also_from"] = [_source_ref(run["sources"][i]) for i in o["confirmed_by"]]
        if "measure" in o:
            m = o["measure"]
            if "source_definition_unresolved" in m.get("flags", []):
                entry["text"] = "Excluded from quantitative analysis: source method/interval definitions unresolved; reported raw value retained in record."
                entry["analysis_status"] = "source_definition_unresolved"
                outs.append(entry)
                continue
            entry["value"] = m.get("value")
            entry["raw"] = m["raw"]
            if m.get("min") is not None and m.get("max") is not None and m["min"] != m["max"]:
                entry["min"], entry["max"] = m["min"], m["max"]
            entry["unit"] = m.get("unit")
            for field in ("uncertainty", "interval_kind", "detection_limit"):
                if m.get(field) is not None:
                    entry[field] = m[field]
            if "source_processed" in m.get("flags", []):
                entry["source_processed"] = True
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
            axes[axis] = {"status": "within" if d <= 1 + TOLERANCE_EPS else "outside", "raw": m["raw"], "min": m["min"],
                          "max": m["max"], "unit": m.get("unit"), "distance": round(d, 3),
                          **({"flags": m["flags"]} if m.get("flags") else {})}
        within = all(d <= 1 + TOLERANCE_EPS for d in dists)
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
            # A run reporting NONE of the query's axes has no measured
            # information about it at all -- it must never rank as "nearer"
            # than a run that DOES report an axis, however far off that
            # value is. MISSING_PENALTY is a small constant meant only to
            # nudge an otherwise-close multi-axis match that lacks one axis;
            # alone (dists empty) it made "we have no idea" look nearer than
            # "we measured, and it's far" -- e.g. the "nearest" results for
            # an out-of-range o2_pct were runs with no O2 column at all.
            near.append((score if dists else NO_AXES_REPORTED_SCORE, run, axes))

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
    """Only an explicitly reported scalar. Ranges remain source evidence,
    never invented midpoint observations in a distribution."""
    value = o.get("value")
    if value is not None and math.isfinite(value) and not o.get("values"):
        if o.get("min", value) == o.get("max", value):
            return value
    return None


def _cohort_conditions(run: dict, outcome: dict) -> dict:
    """Conservative strata: all normalized recorded conditions, not just
    the search axes. Missing conditions never imply physical equivalence."""
    out = {}
    for key, c in sorted(run["conditions"].items()):
        if isinstance(c.get("value"), str):
            out[key] = c["value"]
        else:
            out[key] = {k: c[k] for k in ("value", "min", "max", "unit", "values", "flags") if k in c}
    if outcome.get("at"):
        out["outcome_at"] = outcome["at"]
    return out


def rank(q: dict, quantity: str, geometry_class: str, direction: str = "desc", limit: int = 10,
         runs=None, invs=None) -> dict:
    """Descriptive distributions, stratified by investigation, all recorded
    conditions and unit. Only individual full-match tests with scalar,
    unconflicted outcomes contribute. This is not a material safety ranking."""
    if geometry_class not in RANKABLE or quantity not in RANKABLE[geometry_class]:
        return {"error": f"{quantity!r} is not a rankable result for {geometry_class!r}",
                "rankable": RANKABLE.get(geometry_class, [])}
    if runs is None or invs is None:
        runs, invs = load()
    full_q = {**q, "geometry_class": geometry_class}
    result = query(full_q, runs=runs, invs=invs)

    by_material: dict[str, list[dict]] = defaultdict(list)
    by_id = {run["id"]: run for run in runs}
    excluded: Counter = Counter({"incomplete_conditions": len(result["partial"])})
    target_flow = q.get("flow_cm_s", 0.0)
    for tier in ("match",):
        for v in result[tier]:
            run = by_id[v["id"]]
            if run["granularity"] not in ("test", "test-point"):
                excluded["summary_or_envelope"] += 1
                continue
            if run.get("conflicts"):
                excluded["source_conflict"] += 1
                continue
            if quantity == "burn_time" and any(
                o["quantity"] in ("hot_ignition", "ignited") and str(o.get("text", "")).strip().lower() in ("no", "no ignition", "false")
                for o in run["outcomes"]
            ):
                excluded["did_not_ignite"] += 1
                continue
            # A run may report this quantity at several flow settings (e.g.
            # BASS-II spread rate); one contribution per run, the entry
            # nearest the requested flow (0 if none given) — tie-broken by
            # the flow value itself so the pick is independent of list order,
            # which the TS twin (reading the same JSON) cannot rely on
            # matching v["outcomes"]'s Python-side _outcome_summary sort.
            candidates = [o for o in v["outcomes"] if o["quantity"] == quantity and _outcome_value(o) is not None]
            if not candidates:
                excluded["no_scalar_outcome"] += 1
                continue
            # Do not choose an arbitrary flow if the query did not request
            # one, or use an outcome outside the requested flow tolerance.
            if len(candidates) > 1 and "flow_cm_s" not in q:
                excluded["multiple_outcome_conditions"] += 1
                continue
            if "flow_cm_s" in q:
                candidates = [o for o in candidates if "flow_cm_s" not in o.get("at", {}) or
                              abs(o["at"]["flow_cm_s"] - target_flow) <= (abs(target_flow) or 1) * NUMERIC_AXES["flow_cm_s"][1] + TOLERANCE_EPS]
                if not candidates:
                    excluded["outcome_outside_flow_window"] += 1
                    continue
            o = min(candidates, key=lambda o: (abs(o.get("at", {}).get("flow_cm_s", target_flow) - target_flow),
                                               o.get("at", {}).get("flow_cm_s", target_flow)))
            fam = v["fuel_family"] or "unassigned"
            conditions = _cohort_conditions(run, o)
            key = json.dumps([fam, run["investigation"], conditions, o.get("unit")], sort_keys=True)
            by_material[key].append({"run_id": v["id"], "investigation": v["investigation"], "fuel_family": fam,
                                     "conditions": conditions,
                                     "tier": v["tier"], "value": _outcome_value(o), "unit": o.get("unit")})

    rows = []
    for entries in by_material.values():
        vals = sorted(e["value"] for e in entries)
        n = len(vals)
        median = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
        rows.append({
            "fuel_family": entries[0]["fuel_family"], "n": n, "min": round(vals[0], 4), "max": round(vals[-1], 4),
            "median": round(median, 4), "unit": entries[0].get("unit"),
            "runs": sorted(e["run_id"] for e in entries),
            "conditions": entries[0]["conditions"],
            "investigations": sorted({e["investigation"] for e in entries}),
        })
    rows.sort(key=lambda r: (-r["median"] if direction == "desc" else r["median"], r["fuel_family"], r["runs"][0]))

    # "Untested at these conditions" means no match/partial run at all under
    # this query's OWN filters (categorical + numeric) -- not "every family
    # in the geometry class" (which ignores the query's own fuel_family/etc.
    # filter, so a filtered-out family like SIBAL under fuel_family='PMMA'
    # would wrongly be called untested) and not "ranked" (a family can have
    # match/partial runs at these conditions that simply don't report THIS
    # quantity -- that is not the same as never having been tested here).
    cat_q = {k: str(v).lower() for k, v in full_q.items() if k in CATEGORICAL_AXES and v}
    candidate_families = {(_cat_value(r, "fuel_family", invs) or "unassigned") for r in runs
                          if invs[r["investigation"]]["geometry_class"] == geometry_class
                          and all(_cat_match(r, k, v, invs) for k, v in cat_q.items())}
    tested_families = {v["fuel_family"] or "unassigned" for t in ("match", "partial") for v in result[t]}
    return {
        "query": full_q, "quantity": quantity, "geometry_class": geometry_class, "direction": direction,
        "rows": rows[:limit], "total_ranked": len(rows),
        "excluded": dict(excluded),
        "method": "Full-match individual tests; scalar outcomes only; separate investigation, recorded-condition and unit strata. Descriptive comparison, not a safety ranking.",
        "untested": sorted(candidate_families - tested_families),
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
        "excluded": result["excluded"], "method": result["method"],
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


def outcome_conditions(at: dict | None) -> str:
    """Format every outcome-specific condition without assuming a flow sweep."""
    parts = []
    for key, value in (at or {}).items():
        if key == "flow_cm_s":
            parts.append(f"{value:g} cm/s")
        elif key == "selected_mass_concentration_mg_m3":
            parts.append(f"{value:g} mg/m³ selected smoke threshold")
        else:
            parts.append(f"{key}={value:g}")
    return ", ".join(parts)


def _fmt_outcome(o: dict) -> str:
    """Normalized value + unit (the raw cell may be in another unit, e.g. minutes)."""
    if o.get("detection_limit"):
        limit = o["detection_limit"]
        val = f"{limit['operator']}{limit['value']:g} {limit.get('unit') or ''} (reported bound)"
    elif o.get("uncertainty") and o.get("value") is not None and "plus" in o["uncertainty"]:
        val = f"{o['value']:g} ± {o['uncertainty']['plus']:g} {o.get('unit') or ''} (reported uncertainty)"
    elif o.get("min") is not None and o.get("max") is not None and o.get("at") is None:
        # a range stays a range: its midpoint is a number no source states
        val = f"{o['min']:g}–{o['max']:g}" + (f" {o['unit']}" if o.get("unit") else "")
    elif o.get("value") is not None:
        val = f"{o['value']:g}" + (f" {o['unit']}" if o.get("unit") else "")
    elif o.get("values"):
        val = ", ".join(f"{x:g}" for x in o["values"]) + (f" {o['unit']}" if o.get("unit") else "")
    else:
        val = o.get("text") or o.get("raw") or "?"
    at = f" @ {outcome_conditions(o['at'])}" if o.get("at") else ""
    return f"{o['quantity']}={val}{at}"


def fmt_sourced_outcome(o: dict, report_keys: dict[tuple[str, str], str] | None = None) -> str:
    """A value and its provenance as ONE string, so the model can only repeat
    them together: 'spread_rate=0.071 mm/s @ 9 cm/s [Table 5.1, report 1]',
    or (report_keys given) '... [report 1]' with the table/title looked up
    once in the payload's top-level "reports" map."""
    tags = [source_label(r, report_keys) for r in [o["from"], *o.get("also_from", [])]]
    if o.get("source_processed"):
        tags.append("source-processed cached workbook value")
    return f"{_fmt_outcome(o)} [{'; also '.join(tags)}]"


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


def _shrink_to_budget(payload: dict, max_bytes: int) -> None:
    """Guarantee compact()'s output fits the token budget regardless of which
    specific query produced it (AGENTS.md: Groq's free tier is 8000 TPM for
    the whole turn, so tool replies must stay small -- a fixed per-outcome
    citation tag can, for an unusual query with many long free-text
    outcomes and little repetition to compress away, still push a payload
    over budget; a single pinned test case is not proof every query shape
    fits). Trims the single longest outcome string across every listed run
    -- never the run itself first, so a run's remaining outcomes/axes/id
    stay intact -- until the payload fits or nothing is left to trim. A run
    left with zero outcomes is dropped entirely, so "no values recorded"
    is never implied for a run that had some."""
    tiers = ("match", "partial", "near")
    while len(json.dumps(payload, ensure_ascii=False)) > max_bytes:
        longest = None  # (tier, run_index, outcome_index, length)
        for t in tiers:
            for i, v in enumerate(payload.get(t, [])):
                for j, o in enumerate(v["outcomes"]):
                    if longest is None or len(o) > longest[3]:
                        longest = (t, i, j, len(o))
        if longest is None:
            return  # nothing left to trim; leave the payload as-is
        t, i, j, _ = longest
        del payload[t][i]["outcomes"][j]
        if not payload[t][i]["outcomes"]:
            del payload[t][i]


def compact(result: dict, max_runs: int = 10, max_bytes: int = 5800) -> dict:
    """The LLM-facing view: small enough for a tight token budget, still cited.
    The widget renders the full result; the model only needs enough to write
    a one-paragraph, cited summary."""

    # A (table, title) pair is listed once and referenced by a short key, so
    # a payload with many outcomes citing the same report table -- the common
    # case -- doesn't repeat that table's full name every time (it did: one
    # real query's payload went from 5983 to 6798 bytes, over the ~6000
    # budget, purely from restating "Table A.5, p. 110, Burning and
    # Suppression of Solids-II (BASS-II) Summary Report" per outcome).
    report_keys: dict[tuple[str, str], str] = {}

    def slim(v: dict) -> dict:
        outcomes = v["outcomes"][:3]
        for o in outcomes:
            for r in [o["from"], *o.get("also_from", [])]:
                if r["kind"] == "report":
                    key = (r["table"], r["title"])
                    if key not in report_keys:
                        report_keys[key] = str(len(report_keys) + 1)
        # No run-level citation: a single per-run cite (it was always the PSI
        # line) got copied as the source of values that came from a report
        # table. Each value's source is the tag on that value instead.
        return {
            "id": v["id"], "inv": v["investigation"], "fuel": v["fuel"],
            **({"granularity": v["granularity"]} if v["granularity"] not in ("test", "test-point") else {}),
            "axes": {k: _axis_for_compact(a) for k, a in v["axes"].items()},
            "outcomes": [fmt_sourced_outcome(o, report_keys) for o in outcomes],
            "conflicts": len(v["conflicts"]),
        }

    budget = max_runs
    picks = {}
    for tier in ("match", "partial", "near"):
        picks[tier] = [slim(v) for v in prefer_outcomes(result[tier])[:budget]]
        budget -= len(picks[tier])
        budget = max(budget, 2)  # always show a couple from each remaining tier
    measured = Counter(o["quantity"] for t in ("match", "partial") for v in result[t] for o in v["outcomes"])
    payload = {
        "query": result["query"],
        "counts": result["counts"],
        # across ALL matching/partial runs, not just the ones listed below — so
        # "no values recorded" can never be concluded from a truncated list
        "results_recorded": dict(measured.most_common(8)),
        **picks,
        **({"reports": {v: f"{table}, {title}" for (table, title), v in report_keys.items()}} if report_keys else {}),
        "coverage": [
            {"inv": c["investigation"], "runs": c["runs"],
             **{k: (a.get("statement") or f"{a['min']}–{a['max']} ({a['reported_by']}/{a['of']} runs){'' if a['target_in_range'] else ' — target OUTSIDE tested range'}")
                for k, a in c["axes"].items()}}
            for c in result["coverage"][:10]
        ],
        "relaxed": result["relaxed"][:5],
        "geometry_classes": result["geometry_classes"],
    }
    _shrink_to_budget(payload, max_bytes)
    return payload


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


def _nearest_reported_value(m: dict | None, target: float) -> float | None:
    """The number that actually put this axis within tolerance -- for a
    multi-value cell (several distinct readings in one cell, e.g. an ACME BRE
    run logging "21; 26.5; 40"), the ONE reading nearest target, never the
    cell's bare minimum, which can be a different, unrelated reading. A plain
    interval with no discrete readings falls back to its nearer endpoint; a
    single value is returned as-is. Mirrors _norm_distance's own choice of
    which number in the cell counts as "the" value at this target."""
    if m is None or m.get("min") is None:
        return None
    if m.get("values"):
        return min(m["values"], key=lambda v: abs(v - target))
    if m.get("value") is not None:
        return m["value"]
    lo, hi = m["min"], m["max"]
    return lo if abs(target - lo) <= abs(target - hi) else hi


def readiness(atm_id: str, runs=None, invs=None) -> dict:
    atm = psi_atmospheres.ATMOSPHERES.get(atm_id)
    if atm is None:
        return {"error": f"Unknown atmosphere {atm_id!r}", "known": sorted(psi_atmospheres.ATMOSPHERES)}
    if runs is None or invs is None:
        runs, invs = load()
    runs = [r for r in runs if r["granularity"] in ("test", "test-point")]
    base_q = {"o2_pct": atm["o2_pct"], "pressure_atm": atm["pressure_atm"]}
    by_id = {r["id"]: r for r in runs}

    classes = []
    for gc in sorted({i["geometry_class"] for i in invs.values()}):
        result = query({**base_q, "geometry_class": gc}, runs=runs, invs=invs)
        best_pool = result["match"] or result["partial"] or result["near"]
        nearest = None
        if best_pool:
            b = best_pool[0]
            full = by_id[b["id"]]
            nearest = {"run_id": b["id"], "investigation": b["investigation"], "tier": b["tier"],
                      "o2_pct": _nearest_reported_value(full["conditions"].get("o2_pct"), atm["o2_pct"]),
                      "pressure_atm": _nearest_reported_value(full["conditions"].get("pressure_atm"), atm["pressure_atm"])}
        quantities = sorted({o["quantity"] for v in (result["match"] + result["partial"]) for o in v["outcomes"]
                             if o.get("value") is not None
                             or (o.get("min") is not None and o.get("max") is not None) or o.get("values")})
        classes.append({
            "geometry_class": gc, "match": result["counts"]["match"], "partial": result["counts"]["partial"],
            "near_pool": result["counts"]["near_pool"],
            "covered": result["counts"]["match"] > 0,
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
