"""Every view of the PSI run table, as ChatKit widgets rendered in the chat.

The chat is the product: the evidence list, the gap map, the side-by-side
comparison, a single test's full record and the results chart are all widgets
here, reachable two ways — the model calls a tool (psi_tools.py), or the user
clicks a button on a widget already on screen, which the server answers
directly (main.py → action()) with no LLM call and no token spend.

Every number shown comes from data/runs.json with its PSI line or report
table beside it; nothing here computes a new scientific value (no averages,
no fits). Bins in the gap map count tests; they never merge their results.

Widget classes are constructed directly (Card, Row, Box, Chart, …); openai-
chatkit marks that path deprecated in favor of .widget templates but it is
supported, and needs no external designer tool.
"""

from __future__ import annotations

import os
from collections import Counter, defaultdict
from urllib.parse import urlencode

from chatkit.actions import ActionConfig
from chatkit.widgets import (
    Badge,
    BarSeries,
    Box,
    Button,
    Caption,
    Card,
    Chart,
    Col,
    Divider,
    LineSeries,
    Markdown,
    Row,
    Text,
    Title,
)

import psi_atmospheres
import psi_query

# Fallback only; each request normally supplies its own site (see explorer_url).
SITE_URL = os.environ.get("SITE_URL", "https://marjan-ahmed.github.io/flame-freefall").rstrip("/")

AXIS_LABEL = {"o2_pct": "O₂", "flow_cm_s": "flow", "pressure_atm": "pressure", "thickness_mm": "thickness",
              "droplet_d0_mm": "droplet d₀"}
GEOMETRY_LABEL = {"solid-fuel": "Solid fuel", "droplet-combustion": "Droplet combustion",
                  "gaseous-flames": "Gaseous flames", "smoke-aerosol": "Smoke / aerosol"}
QUANTITY_LABEL = {
    "spread_rate": "Flame spread rate", "burning_rate_k": "Burning-rate constant k",
    "burning_rate_k_hot": "Burning-rate constant k (hot flame)", "burning_rate_k_cool": "Burning-rate constant k (cool flame)",
    "extinction_diameter": "Extinction diameter", "extinction_diameter_hot": "Extinction diameter (hot flame)",
    "burn_time": "Burn time", "smoke_point_length": "Smoke-point length", "flames_ignited": "Flames ignited per day",
    "weight_loss_rate": "Weight-loss rate", "peak_heat_release": "Peak heat release", "spread_rate_1g": "Spread rate (1-g)",
    "spread_extent": "Spread extent", "final_co2_pct": "Final CO₂", "final_co_ppm": "Final CO",
    "peak_burner_temp_c": "Peak burner temperature", "observation": "Observation", "end_mode": "End mode",
    "test_end": "Test end", "ignited": "Ignited", "hot_ignition": "Hot ignition",
    "burn_time_hot_flame": "Hot-flame burn time (unit not stated)", "reignitions": "Re-ignitions",
    "extinction_diameter_cool": "Extinction diameter (cool flame)", "tem_particles_counted_unaged": "TEM particles counted (unaged)",
    "tem_particles_counted_aged": "TEM particles counted (aged)", "smoke_points_observed": "Smoke points observed",
    "comment": "Comment", "flame_color": "Flame color", "cool_flame": "Cool flame",
}
GRANULARITY_LABEL = {"day": "daily summary", "summary": "per-fuel summary", "envelope": "planned envelope"}
PALETTE = ["#dc2626", "#2563eb", "#16a34a", "#d97706", "#7c3aed", "#0891b2", "#db2777", "#65a30d", "#ea580c", "#4f46e5"]


# ── helpers ──────────────────────────────────────────────────────────────────

def _fmt(x) -> str:
    if x is None:
        return "?"
    return f"{x:g}" if isinstance(x, (int, float)) else str(x)


def _unit(axis: str) -> str:
    return psi_query.NUMERIC_AXES.get(axis, ("", 0, ""))[2]


def query_title(q: dict) -> str:
    bits = []
    for k, v in q.items():
        if k in psi_query.NUMERIC_AXES:
            bits.append(f"{AXIS_LABEL[k]} ≈ {_fmt(v)} {_unit(k)}")
        else:
            bits.append(f"{k.replace('_', ' ')}: {v}")
    return " · ".join(bits) or "all tests"


def explorer_url(q: dict, run: str | None = None, site: str | None = None) -> str:
    """`site` is the base URL of the page the chat is running on (main.py derives
    it per request from the Referer, checked against the CORS allowlist), so the
    link opens the Explorer on that same deployment — localhost in dev, GitHub
    Pages in production. SITE_URL is only the fallback."""
    params = {k: v for k, v in q.items()}
    if run:
        params["run"] = run
    return f"{(site or SITE_URL).rstrip('/')}/explore/?{urlencode(params)}"


def action(kind: str, **payload) -> ActionConfig:
    """A button the server answers directly (main.py action())."""
    return ActionConfig(type=f"psi.{kind}", payload=payload, handler="server", loadingBehavior="self")


def nav_buttons(q: dict, *, skip: str = "", extra: list | None = None) -> Row:
    """The same next-step buttons on every widget: the user steers from here."""
    buttons = []
    if skip != "evidence":
        buttons.append(Button(label="Evidence list", onClickAction=action("evidence", q=q), size="sm", variant="outline"))
    if skip != "gap":
        buttons.append(Button(label="Gap map", onClickAction=action("gap_map", q=q, y="flow_cm_s"), size="sm", variant="outline"))
    if skip != "compare":
        buttons.append(Button(label="Compare investigations", onClickAction=action("compare", q=q), size="sm", variant="outline"))
    if skip != "results":
        buttons.append(Button(label="Results chart", onClickAction=action("results", q=q), size="sm", variant="outline"))
    return Row(gap=2, wrap="wrap", children=[*buttons, *(extra or [])])


def _cat_q(q: dict) -> dict:
    return {k: v for k, v in q.items() if k in psi_query.CATEGORICAL_AXES}


def _filtered_runs(q: dict) -> list[dict]:
    """Runs passing the categorical filters of q (fuel, geometry, direction, investigation)."""
    runs, invs = psi_query.load()
    cq = {k: str(v).lower() for k, v in _cat_q(q).items()}
    return [r for r in runs if all(psi_query._cat_match(r, k, v, invs) for k, v in cq.items())]


def _measure(run: dict, axis: str) -> dict | None:
    m = run["conditions"].get(axis)
    return m if isinstance(m, dict) and m.get("min") is not None else None


def _points(m: dict) -> list[float]:
    """Where a run sits on an axis: each stated value, else the midpoint of its span."""
    if "multi" in m.get("flags", []) and m.get("values"):
        return list(m["values"])
    return [(m["min"] + m["max"]) / 2]


# ── 1. evidence list ─────────────────────────────────────────────────────────

TIER_TITLE = {
    "match": "Tests at the requested conditions",
    "partial": "Partial evidence: matches every condition it reports, silent on at least one",
    "near": "Nearest tests (outside tolerance on at least one condition)",
}
TIER_SHOWN = {"match": 6, "partial": 5, "near": 4}


def _axis_line(v: dict) -> str:
    parts = []
    for axis, a in v["axes"].items():
        name = AXIS_LABEL.get(axis, axis)
        if a["status"] == "not_reported":
            parts.append(f"{name} not reported")
        else:
            flag = " ⚠" if "sources_disagree" in a.get("flags", []) else ""
            unit = a.get("unit") or ""
            raw = a.get("raw", "")
            flags = a.get("flags", [])
            # If the value was converted, show normalized value with source cell
            conv_flag = next((f for f in flags if f.startswith("converted_from_")), None)
            mole_flag = "mole_fraction_to_pct" in flags
            if conv_flag or mole_flag:
                # Show normalized min/max with unit, then source cell in parentheses
                if a.get("min") is not None and a.get("max") is not None:
                    if a["min"] == a["max"]:
                        val = f"{a['min']:g} {unit}"
                    else:
                        val = f"{a['min']:g}–{a['max']:g} {unit}"
                    parts.append(f"{name} {val} (cell {raw}){flag}")
                else:
                    parts.append(f"{name} {raw} {unit}{flag}")
            else:
                parts.append(f"{name} {raw}{' ' + unit if unit and unit not in raw else ''}{flag}")
    if v.get("fuel"):
        parts.append(v["fuel"])
    return " · ".join(parts)


def _cite_line(v: dict) -> str:
    out = []
    for c in v["citations"]:
        if c["kind"] == "psi":
            out.append(f"{c['dataset']} {c['file']}{' [' + c['sheet'] + ']' if c.get('sheet') else ''} line {c['row']}")
        else:
            out.append(f"{c['title']} — {c['table']}")
    return "Source: " + " · ".join(dict.fromkeys(out))


def _run_item(v: dict, q: dict | None = None, expanded: bool = False) -> Col:
    badges = [Badge(label=v["investigation"], color="secondary", size="sm")]
    if v["granularity"] in GRANULARITY_LABEL:
        badges.append(Badge(label=GRANULARITY_LABEL[v["granularity"]], color="warning", size="sm"))
    if v["conflicts"]:
        badges.append(Badge(label=f"sources disagree ({len(v['conflicts'])})", color="danger", size="sm"))
    lines = [
        Row(gap=2, align="center", wrap="wrap", children=[
            Text(value=v["label"], weight="semibold", size="sm"), *badges, Box(flex=1),
            # Details expands the record IN PLACE: a sync action (streaming=False)
            # answered by main.py sync_action(), which returns this same card with
            # the row opened (ChatKit's documented way to update the clicked
            # widget). As a streaming action it appended a new card at the end of
            # the chat and left the clicked button loading (seen live 2026-09-24).
            Button(key=f"details:{v['id']}", label="Hide details" if expanded else "Details", size="xs",
                   variant="soft" if expanded else "ghost",
                   onClickAction=ActionConfig(type="psi.expand", handler="server", streaming=False,
                                              loadingBehavior="self",
                                              payload={"q": q or {}, "id": v["id"], "open": not expanded})),
        ]),
        Caption(value=_axis_line(v), size="sm"),
    ]
    shown = [f"{QUANTITY_LABEL.get(o['quantity'], o['quantity'].replace('_', ' '))}: "
             f"{psi_query._fmt_outcome(o).split('=', 1)[1]}" for o in v["outcomes"][:3]]
    if shown:
        lines.append(Caption(value="Result: " + "; ".join(shown), size="sm", color="emphasis"))
    lines.append(Caption(value=_cite_line(v), size="sm", color="tertiary"))
    if expanded:
        run = next((r for r in psi_query.load()[0] if r["id"] == v["id"]), None)
        if run is not None:
            lines.append(Col(gap=1, padding=2, radius="md", border={"size": 1, "color": "subtle"},
                             children=detail_sections(run)))
    return Col(gap=1, padding={"y": 1}, children=lines)


def _coverage_line(c: dict) -> str:
    parts = []
    for axis, a in c["axes"].items():
        name = AXIS_LABEL.get(axis, axis)
        if a.get("statement"):
            parts.append(f"{name} {a['statement']}")
        else:
            mark = "covers target" if a["target_in_range"] else "target outside tested range"
            parts.append(f"{name} {_fmt(a['min'])}–{_fmt(a['max'])} ({a['reported_by']}/{a['of']}; {mark})")
    return f"{c['investigation']} ({c['runs']}): " + "; ".join(parts) if parts else f"{c['investigation']} ({c['runs']} records)"


def evidence_widget(q: dict, result: dict | None = None, site: str | None = None, expanded: str | None = None) -> Card:
    result = result or psi_query.query(q)
    counts = result["counts"]
    children = [
        Title(value="PSI test-run evidence", size="md"),
        Caption(value=query_title(q)),
        Row(gap=2, wrap="wrap", children=[
            Badge(label=f"{counts['match']} at conditions", color="success" if counts["match"] else "secondary"),
            Badge(label=f"{counts['partial']} partial", color="info" if counts["partial"] else "secondary"),
            *[Badge(label=GEOMETRY_LABEL.get(g, g), color="secondary", variant="outline") for g in result["geometry_classes"]],
        ]),
    ]
    if not counts["match"] and any(k in psi_query.NUMERIC_AXES for k in q):
        children.append(Text(value="No test in the PSI tables states all of these conditions.", size="sm", weight="semibold"))
    if len(result["geometry_classes"]) > 1:
        children.append(Caption(value="Results span several geometry classes; compare outcomes only within one class.",
                                color="warning"))
    for tier in ("match", "partial", "near"):
        rows = psi_query.prefer_outcomes(result[tier])[: TIER_SHOWN[tier]]
        if not rows or (tier == "near" and counts["match"] >= 3):
            continue
        more = (counts[tier] if tier != "near" else counts["near_pool"]) - len(rows)
        children += [Divider(spacing=2), Text(value=TIER_TITLE[tier], size="sm", weight="semibold"),
                     *[_run_item(v, q, expanded == v["id"]) for v in rows]]
        if more > 0:
            children.append(Caption(value=f"+ {more} more (ask to narrow the conditions, or open the full list in the Explorer)",
                                    color="tertiary"))
    if result["coverage"]:
        children += [Divider(spacing=2), Text(value="Coverage and gaps, by investigation", size="sm", weight="semibold")]
        children += [Caption(value=_coverage_line(c), size="sm") for c in result["coverage"][:8]]
    if result["relaxed"]:
        rel = "; ".join(f"{r['fuel_family']} ({r['investigation']}, {r['runs']})" for r in result["relaxed"][:4])
        children.append(Caption(value=f"Same conditions, other materials: {rel}", size="sm", color="tertiary"))
    children += [Divider(spacing=2), nav_buttons(q, skip="evidence"),
                 Markdown(value=f"[Full list in the Explorer →]({explorer_url(q, site=site)})")]
    return Card(size="full", children=children)


# ── 2. gap map ───────────────────────────────────────────────────────────────

O2_BINS = [(0, 14), (14, 16), (16, 18), (18, 20), (20, 22), (22, 25), (25, 30), (30, 35), (35, 45), (45, 101)]
Y_BINS = {
    "flow_cm_s": [(-10, 2), (2, 5), (5, 10), (10, 15), (15, 20), (20, 30), (30, 50), (50, 1000)],
    "pressure_atm": [(0, 0.6), (0.6, 0.9), (0.9, 1.1), (1.1, 1.6), (1.6, 2.5), (2.5, 3.5), (3.5, 100)],
}


def _bin_label(lo: float, hi: float, first: bool, last: bool) -> str:
    if first:
        return f"<{_fmt(hi)}"
    if last:
        return f"≥{_fmt(lo)}"
    return f"{_fmt(lo)}–{_fmt(hi)}"


def _bin_of(x: float, bins: list[tuple[float, float]]) -> int | None:
    for i, (lo, hi) in enumerate(bins):
        if lo <= x < hi:
            return i
    return None


# empty = the gap; then light → strong by number of tests
SHADES = [
    (0, {"light": "#f8fafc", "dark": "#1e293b"}),
    (1, {"light": "#fed7aa", "dark": "#7c2d12"}),
    (3, {"light": "#fdba74", "dark": "#9a3412"}),
    (10, {"light": "#fb923c", "dark": "#c2410c"}),
    (30, {"light": "#ea580c", "dark": "#ea580c"}),
]


def _shade(n: int) -> dict:
    color = SHADES[0][1]
    for threshold, c in SHADES:
        if n >= threshold:
            color = c
    return color


def gap_map_data(q: dict, y_axis: str = "flow_cm_s") -> dict:
    runs = _filtered_runs(q)
    invs = psi_query.load()[1]
    ybins = Y_BINS[y_axis]
    grid: dict[tuple[int, int], set[str]] = defaultdict(set)
    unreported: dict[int, set[str]] = defaultdict(set)
    by_inv: dict[tuple[int, int], Counter] = defaultdict(Counter)
    no_o2 = 0
    for r in runs:
        o2 = _measure(r, "o2_pct")
        if not o2:
            no_o2 += 1
            continue
        xs = {b for p in _points(o2) if (b := _bin_of(p, O2_BINS)) is not None}
        ym = _measure(r, y_axis)
        if not ym:
            for x in xs:
                unreported[x].add(r["id"])
            continue
        ys = {b for p in _points(ym) if (b := _bin_of(p, ybins)) is not None}
        for x in xs:
            for y in ys:
                grid[(x, y)].add(r["id"])
                by_inv[(x, y)][invs[r["investigation"]]["name"]] += 1
    tx = _bin_of(q["o2_pct"], O2_BINS) if "o2_pct" in q else None
    ty = _bin_of(q[y_axis], ybins) if y_axis in q else None
    return {"runs": runs, "grid": grid, "unreported": unreported, "by_inv": by_inv, "no_o2": no_o2,
            "tx": tx, "ty": ty, "ybins": ybins}


def gap_map_widget(q: dict, y_axis: str = "flow_cm_s") -> Card:
    d = gap_map_data(q, y_axis)
    grid, ybins, tx, ty = d["grid"], d["ybins"], d["tx"], d["ty"]
    y_name = AXIS_LABEL[y_axis]
    cell_w = 44

    def cell(n: int, target: bool, label: str | None = None) -> Box:
        return Box(
            width=cell_w, height=30, align="center", justify="center", radius="sm",
            background=_shade(n),
            border={"size": 2, "color": "blue-600"} if target else {"size": 1, "color": "subtle"},
            children=[Caption(value=label if label is not None else (str(n) if n else "·"), size="sm",
                              weight="semibold" if n else "normal", color="primary" if n else "tertiary")],
        )

    header = Row(gap=1, children=[Box(width=68, children=[Caption(value=f"{y_name} ({_unit(y_axis)})", size="sm")]),
                                  *[Box(width=cell_w, align="center",
                                        children=[Caption(value=_bin_label(lo, hi, i == 0, i == len(O2_BINS) - 1), size="sm")])
                                    for i, (lo, hi) in enumerate(O2_BINS)]])
    rows = [header]
    for yi in reversed(range(len(ybins))):
        lo, hi = ybins[yi]
        rows.append(Row(gap=1, children=[
            Box(width=68, justify="center", children=[Caption(value=_bin_label(lo, hi, yi == 0, yi == len(ybins) - 1), size="sm")]),
            *[cell(len(grid.get((xi, yi), ())), xi == tx and yi == ty) for xi in range(len(O2_BINS))],
        ]))
    rows.append(Row(gap=1, children=[
        Box(width=68, justify="center", children=[Caption(value=f"{y_name} not reported", size="sm", color="tertiary")]),
        *[cell(len(d["unreported"].get(xi, ())), xi == tx and ty is None) for xi in range(len(O2_BINS))],
    ]))
    rows.append(Row(gap=1, children=[Box(width=68), Box(children=[Caption(value="O₂ (%) →", size="sm")])]))

    # what the target cell holds, and where the nearest populated cells are
    notes = []
    if tx is not None and ty is not None:
        n = len(grid.get((tx, ty), ()))
        tlabel = f"O₂ {_bin_label(*O2_BINS[tx], tx == 0, tx == len(O2_BINS) - 1)} %, {y_name} {_bin_label(*ybins[ty], ty == 0, ty == len(ybins) - 1)} {_unit(y_axis)}"
        if n:
            who = ", ".join(f"{k} {v}" for k, v in d["by_inv"][(tx, ty)].most_common())
            notes.append(f"Target cell ({tlabel}): {n} tests ({who}).")
        else:
            notes.append(f"Target cell ({tlabel}): no tests. This is an untested gap.")
            near = sorted(((abs(x - tx) + abs(y - ty), (x, y)) for (x, y), ids in grid.items() if ids))[:3]
            for _, (x, y) in near:
                who = ", ".join(f"{k} {v}" for k, v in d["by_inv"][(x, y)].most_common(3))
                notes.append(f"Nearest tested: O₂ {_bin_label(*O2_BINS[x], x == 0, x == len(O2_BINS) - 1)} %, "
                             f"{y_name} {_bin_label(*ybins[y], y == 0, y == len(ybins) - 1)}: {len(grid[(x, y)])} tests ({who})")
        un = len(d["unreported"].get(tx, ()))
        if un:
            notes.append(f"{un} more tests sit in the target O₂ band but don't report {y_name}.")
    filled = sum(1 for ids in grid.values() if ids)
    total_cells = len(O2_BINS) * len(ybins)
    other_y = "pressure_atm" if y_axis == "flow_cm_s" else "flow_cm_s"
    children = [
        Title(value=f"Gap map: O₂ × {y_name}", size="md"),
        Caption(value=f"{query_title(_cat_q(q)) if _cat_q(q) else 'All investigations'} · {len(d['runs'])} records · "
                      f"{filled} of {total_cells} condition cells have any test"),
        Col(gap=1, children=rows),
        Row(gap=2, wrap="wrap", align="center", children=[
            Caption(value="Tests per cell:", size="sm"),
            *[Row(gap=1, align="center", children=[Box(width=14, height=14, radius="xs", background=c,
                                                       border={"size": 1, "color": "subtle"}),
                                                   Caption(value=("0 (gap)" if t == 0 else f"{t}+"), size="sm")])
              for t, c in SHADES],
            Caption(value="blue outline = your target", size="sm", color="tertiary"),
        ]),
        *[Caption(value=n, size="sm") for n in notes],
        Caption(value=f"A test is counted in every cell its stated values fall in; O₂ that drifted during a burn is placed at "
                      f"its midpoint. {d['no_o2']} records don't report ambient O₂ and are not on this map.",
                size="sm", color="tertiary"),
        Divider(spacing=2),
        nav_buttons(q, skip="gap", extra=[Button(label=f"Map O₂ × {AXIS_LABEL[other_y]}",
                                                 onClickAction=action("gap_map", q=q, y=other_y), size="sm", variant="soft")]),
    ]
    return Card(size="full", children=children)


def gap_map_summary(q: dict, y_axis: str = "flow_cm_s") -> dict:
    d = gap_map_data(q, y_axis)
    out = {"records": len(d["runs"]), "cells_with_tests": sum(1 for v in d["grid"].values() if v),
           "cells_total": len(O2_BINS) * len(d["ybins"])}
    if d["tx"] is not None and d["ty"] is not None:
        out["target_cell_tests"] = len(d["grid"].get((d["tx"], d["ty"]), ()))
        out["target_cell_by_investigation"] = dict(d["by_inv"][(d["tx"], d["ty"])])
        out["same_o2_band_axis_not_reported"] = len(d["unreported"].get(d["tx"], ()))
    # Every tested cell, spelled out. Seen live 2026-09-24: given only counts,
    # the model described "the higher-O2, higher-flow region" as untested when
    # SAFFIRE VI tests sit there. With the cells listed it has no gap to fill.
    ybins, nb = d["ybins"], len(O2_BINS)
    y_name = AXIS_LABEL[y_axis]
    out["tested_cells"] = [
        f"O2 {_bin_label(*O2_BINS[x], x == 0, x == nb - 1)} % / {y_name} "
        f"{_bin_label(*ybins[y], y == 0, y == len(ybins) - 1)} {_unit(y_axis)}: {len(ids)} ("
        + ", ".join(f"{k} {v}" for k, v in d["by_inv"][(x, y)].most_common(3)) + ")"
        for (x, y), ids in sorted(d["grid"].items()) if ids
    ]
    out["axis_not_reported_by_o2_band"] = {
        f"O2 {_bin_label(*O2_BINS[x], x == 0, x == nb - 1)} %": len(ids)
        for x, ids in sorted(d["unreported"].items()) if ids
    }
    # Precomputed the same way as tested_cells, not left for the model to
    # infer by absence. Seen live 2026-09-24: given only tested_cells, the
    # model still called a region untested that actually had tests in a
    # different cell of the same band it wasn't checking carefully.
    out["untested_bands"] = [
        f"O2 {_bin_label(*O2_BINS[x], x == 0, x == nb - 1)} % / {y_name} "
        f"{_bin_label(*ybins[y], y == 0, y == len(ybins) - 1)} {_unit(y_axis)}"
        for x in range(nb) for y in range(len(ybins))
        if not d["grid"].get((x, y))
    ]
    return out


# ── 3. horizontal comparison ─────────────────────────────────────────────────

def _resolve_investigations(names: list[str], invs: dict[str, dict]) -> set[str]:
    """User/model names → investigation ids, unioned. One resolver
    (psi_query._investigation_ids) shared with query()'s own investigation
    filter, so this and query_test_runs agree on what a name means — see C7."""
    out: set[str] = set()
    for name in names:
        out |= psi_query._investigation_ids(name, invs)
    return out


def compare_data(q: dict, investigations: list[str] | None = None) -> list[dict]:
    runs, invs = psi_query.load()
    result = psi_query.query(q)
    tier_counts: dict[str, Counter] = defaultdict(Counter)
    for tier in ("match", "partial"):
        for v in result[tier]:
            tier_counts[v["investigation_id"]][tier] += 1
    wanted = _resolve_investigations(investigations or [], invs)
    # Names were explicitly given but NONE resolved: an explicit filter to
    # nothing, never silently widened to "no filter at all" (`wanted` empty
    # used to be indistinguishable from investigations=None/[], and every
    # investigation came back as if the caller had asked for it).
    if investigations and not wanted:
        return []
    rows = []
    by_inv: dict[str, list[dict]] = defaultdict(list)
    for r in _filtered_runs({k: v for k, v in q.items() if k != "investigation"} if wanted else q):
        by_inv[r["investigation"]].append(r)
    for inv_id, rs in by_inv.items():
        inv = invs[inv_id]
        if wanted and inv_id not in wanted:
            continue
        axes = {}
        for axis in ("o2_pct", "flow_cm_s", "pressure_atm"):
            ms = [m for r in rs if (m := _measure(r, axis))]
            if ms:
                lo, hi = min(m["min"] for m in ms), max(m["max"] for m in ms)
                t = q.get(axis)
                axes[axis] = {"min": lo, "max": hi, "n": len(ms),
                              "target": None if t is None else lo <= t <= hi}
            else:
                axes[axis] = None
        results: dict[str, list[dict]] = defaultdict(list)
        for r in rs:
            for o in r["outcomes"]:
                m = o.get("measure")
                if m and m.get("min") is not None:
                    results[o["quantity"]].append(m)
        # Scientific priority first (spread rate, burning rate, extinction…),
        # then frequency. By frequency alone CFI's headline result was its
        # re-ignition count rather than its burning rates (seen 2026-09-24).
        rank = {qn: i for i, qn in enumerate(psi_query.OUTCOME_PRIORITY)}
        top = sorted(results.items(), key=lambda kv: (rank.get(kv[0], 99), -len(kv[1])))[:2]
        rows.append({
            "id": inv_id, "name": inv["name"], "geometry_class": inv["geometry_class"], "records": len(rs),
            "match": tier_counts[inv_id]["match"], "partial": tier_counts[inv_id]["partial"],
            "axes": axes,
            "results": [{"quantity": qn, "min": min(m["min"] for m in ms), "max": max(m["max"] for m in ms),
                         "unit": ms[0].get("unit"), "n": len(ms)} for qn, ms in top],
            "fuels": [f for f, _ in Counter((r["conditions"].get("fuel_family") or {}).get("value") or "unassigned"
                                            for r in rs).most_common(4)],
            "conflicts": sum(len(r.get("conflicts", [])) for r in rs),
            "citation": (inv.get("citation") or {}).get("title") or (f"NASA PSI {inv['psi_id']}" if inv["psi_id"] else None),
        })
    rows.sort(key=lambda x: (-(x["match"] * 1000 + x["partial"]), -x["records"]))
    return rows


def _range_line(name: str, a: dict | None, unit: str, has_target: bool) -> Caption:
    if a is None:
        return Caption(value=f"{name}: not reported", size="sm", color="tertiary")
    mark = ""
    if has_target:
        mark = "  ✓ covers target" if a["target"] else "  ✗ target outside"
    return Caption(value=f"{name}: {_fmt(a['min'])}–{_fmt(a['max'])} {unit} ({a['n']}){mark}", size="sm",
                   color="success" if has_target and a["target"] else ("warning" if has_target else None))


def compare_widget(q: dict, investigations: list[str] | None = None) -> Card:
    rows = compare_data(q, investigations)
    shown = rows[:6]
    columns = []
    for x in shown:
        lines = [
            Title(value=x["name"], size="sm"),
            Badge(label=GEOMETRY_LABEL.get(x["geometry_class"], x["geometry_class"]), color="secondary", size="sm"),
            Caption(value=f"{x['records']} records · {x['match']} at conditions · {x['partial']} partial", size="sm"),
            Caption(value="Fuels: " + ", ".join(x["fuels"]), size="sm"),
            _range_line("O₂", x["axes"]["o2_pct"], "%", "o2_pct" in q),
            _range_line("Flow", x["axes"]["flow_cm_s"], "cm/s", "flow_cm_s" in q),
            _range_line("Pressure", x["axes"]["pressure_atm"], "atm", "pressure_atm" in q),
        ]
        for res in x["results"]:
            label = QUANTITY_LABEL.get(res["quantity"], res["quantity"].replace("_", " "))
            rng = _fmt(res["min"]) if res["min"] == res["max"] else f"{_fmt(res['min'])}–{_fmt(res['max'])}"
            lines.append(Caption(value=f"{label}: {rng} {res['unit'] or ''} (n={res['n']})", size="sm", color="emphasis"))
        if not x["results"]:
            lines.append(Caption(value="No measured results in these sources", size="sm", color="tertiary"))
        if x["conflicts"]:
            lines.append(Badge(label=f"sources disagree ×{x['conflicts']}", color="danger", size="sm"))
        if x["citation"]:
            lines.append(Caption(value=x["citation"], size="sm", color="tertiary", maxLines=2))
        lines.append(Button(label="Evidence", size="xs", variant="ghost",
                            onClickAction=action("evidence", q={**q, "investigation": x["id"]})))
        columns.append(Col(gap=1, flex=1, minWidth=170, padding=2, radius="md",
                           border={"size": 1, "color": "subtle"}, children=lines))
    classes = {x["geometry_class"] for x in shown}
    children = [
        Title(value="Investigations side by side", size="md"),
        Caption(value=query_title(q)),
        Row(gap=2, wrap="wrap", align="stretch", children=columns) if columns
        else Text(value="No investigation has records matching these filters.", size="sm"),
    ]
    if len(rows) > len(shown):
        children.append(Caption(value=f"+ {len(rows) - len(shown)} more investigations with fewer relevant tests: "
                                      + ", ".join(x["name"] for x in rows[len(shown):]), size="sm", color="tertiary"))
    if len(classes) > 1:
        children.append(Caption(value="These span several geometry classes; ranges are comparable, results are not across classes.",
                                size="sm", color="warning"))
    children.append(Caption(value="Ranges are what each table reports (count of records in brackets). Result ranges span "
                                  "individual tests; they are not averages.", size="sm", color="tertiary"))
    children += [Divider(spacing=2), nav_buttons(q, skip="compare")]
    return Card(size="full", children=children)


# ── 4. one test, in full ─────────────────────────────────────────────────────

CONDITION_LABEL = {
    "o2_pct": "O₂", "flow_cm_s": "Flow", "pressure_atm": "Pressure", "thickness_mm": "Thickness", "width_cm": "Width",
    "width_nominal_cm": "Width (nominal)", "length_cm": "Length", "diameter_mm": "Diameter",
    "droplet_d0_mm": "Droplet d₀", "fuel": "Fuel / material", "fuel_family": "Fuel family", "fuel_form": "Form",
    "flow_direction": "Flow direction", "diluent": "Diluent", "flame_type": "Flame type",
    "oxidizer_stream_o2_pct": "Oxidizer-stream O₂", "fuel_fraction_pct": "Fuel fraction",
    "flow_setting_air": "Air display (panel)", "flow_setting_fan": "Fan display (panel)",
    "sample_temperature_c": "Sample temperature", "nozzle_diameter_mm": "Nozzle diameter", "pi": "PI",
    "n2_pct": "N₂", "co2_pct": "CO₂", "he_pct": "He", "identifier": "Identifier", "fiber_supported": "Fiber-supported",
    "flame_type": "Flame type", "test_type": "Test type", "fuel_flow_mg_s": "Fuel flow", "oxidizer_flow_mg_s": "Oxidizer flow",
    "ambient_fuel_pct": "Ambient fuel fraction", "stoich_mixture_fraction": "Stoichiometric mixture fraction",
    "adiabatic_flame_temp_k": "Adiabatic flame temperature", "ignition_power_w": "Igniter power",
    "ignition_time_s": "Igniter on-time", "flow_restrictor": "Flow restrictor", "sides_burning": "Sides burning",
    "burner_diameter_mm": "Burner diameter", "e_field_polarity": "E-field polarity", "gmt_day": "GMT day",
    "test_number": "Test number",
}
HIDDEN_FLAGS = ("from_source", "confirmed_by")


def _cond_text(c: dict) -> str:
    if isinstance(c.get("value"), str):
        return c["value"] + (f"  (basis: {c['basis']})" if c.get("basis") else "")
    unit = f" {c['unit']}" if c.get("unit") else ""
    if c.get("values") and c.get("value") is None:
        val = ", ".join(_fmt(v) for v in c["values"]) + unit
    elif c.get("min") is not None and c.get("max") is not None and c["min"] != c["max"]:
        val = f"{_fmt(c['min'])}–{_fmt(c['max'])}{unit}"
    elif c.get("value") is not None:
        val = f"{_fmt(c['value'])}{unit}"
    else:
        val = "not machine-readable"
    flags = [f for f in c.get("flags", []) if not f.startswith(HIDDEN_FLAGS)]
    extra = f'  cell "{c["raw"]}"' if c.get("raw") and c["raw"] not in val else ""
    return val + extra + (f"  [{', '.join(f.replace('_', ' ') for f in flags)}]" if flags else "")


def detail_sections(run: dict) -> list:
    """A test's full record (results, conditions, disagreements, sources, notes):
    the body of the test card, and what expands in place under an evidence row."""
    children = [Divider(spacing=2), Text(value="Results", size="sm", weight="semibold")]
    if run["outcomes"]:
        for o in run["outcomes"][:12]:
            m = o.get("measure")
            if m and m.get("min") is None and not m.get("values") and o.get("text"):
                val = f'{o["text"]}  cell "{m["raw"]}"'
            else:
                val = _cond_text(m) if m else (o.get("text") or "")
            at = f" at {_fmt(o['at']['flow_cm_s'])} cm/s" if o.get("at") else ""
            conf = " ✓ two sources" if o.get("confirmed_by") else ""
            children.append(Caption(value=f"{QUANTITY_LABEL.get(o['quantity'], o['quantity'].replace('_', ' '))}: {val}{at}{conf}"
                                          f"  (source {o['source'] + 1})", size="sm", maxLines=4))
    else:
        children.append(Caption(value="No results recorded in these sources.", size="sm", color="tertiary"))

    children += [Divider(spacing=2), Text(value="Conditions", size="sm", weight="semibold")]
    for k, c in run["conditions"].items():
        if k == "gravity" or not isinstance(c, dict):
            continue
        children.append(Caption(value=f"{CONDITION_LABEL.get(k, k.replace('_', ' '))}: {_cond_text(c)}", size="sm", maxLines=3))

    if run.get("conflicts"):
        children += [Divider(spacing=2), Text(value="Sources disagree (both kept, neither chosen)", size="sm",
                                              weight="semibold", color="danger")]
        for c in run["conflicts"]:
            vals = " vs ".join(f'"{v["raw"]}" (source {v["source"] + 1})' for v in c["values"])
            children.append(Caption(value=f"{CONDITION_LABEL.get(c['field'], c['field'])}: {vals}", size="sm"))

    children += [Divider(spacing=2), Text(value="Sources", size="sm", weight="semibold")]
    for i, s in enumerate(run["sources"], start=1):
        if s["kind"].startswith("psi"):
            where = f"line {s['row']}" if s.get("row") else s.get("note", "")
            text = f"{i}. NASA PSI {s['dataset']}: {s['file']}{' [' + s['sheet'] + ']' if s.get('sheet') else ''} {where}"
        elif s.get("line"):
            text = f"{i}. {s.get('title')}, {s['table']} (as reproduced in the governed record {s.get('doc')})"
        else:
            text = f"{i}. {s.get('title')}, {s['table']} (extracted verbatim from the converted report; not yet human-reviewed)"
        children.append(Caption(value=text, size="sm", maxLines=3))
        if s.get("url"):
            children.append(Markdown(value=f"[{s['url']}]({s['url']})"))
    for n in run.get("notes", []):
        children.append(Caption(value=f"Note: {n}", size="sm", color="tertiary", maxLines=3))

    return children


def test_widget(run_id: str, site: str | None = None) -> Card:
    runs, invs = psi_query.load()
    run = next((r for r in runs if r["id"] == run_id), None)
    if run is None:
        return Card(children=[Text(value=f"No test with id {run_id}.")])
    inv = invs[run["investigation"]]
    head = [Badge(label=inv["name"], color="secondary")]
    if run["granularity"] in GRANULARITY_LABEL:
        head.append(Badge(label=GRANULARITY_LABEL[run["granularity"]], color="warning"))
    if run.get("conflicts"):
        head.append(Badge(label="sources disagree", color="danger"))
    children = [Title(value=run["id"], size="md"), Row(gap=2, wrap="wrap", children=head)]
    if run.get("date"):
        children.append(Caption(value=f"Date: {run['date']}"))
    children += detail_sections(run)

    near_q: dict = {}
    for axis in ("o2_pct", "flow_cm_s", "pressure_atm"):
        m = _measure(run, axis)
        if m:
            near_q[axis] = round((m["min"] + m["max"]) / 2, 2) if m.get("value") is None else m["value"]
    fam = (run["conditions"].get("fuel_family") or {}).get("value")
    if fam:
        near_q["fuel_family"] = fam
    children += [Divider(spacing=2), Row(gap=2, wrap="wrap", children=[
        Button(label="Similar tests", onClickAction=action("evidence", q=near_q), size="sm", variant="outline"),
        Button(label="Gap map around this test", onClickAction=action("gap_map", q=near_q, y="flow_cm_s"), size="sm",
               variant="outline"),
    ]), Markdown(value=f"[Source cells, exactly as written, in the Explorer →]({explorer_url(near_q, run['id'], site=site)})")]
    return Card(size="full", children=children)


# ── 5. results chart ─────────────────────────────────────────────────────────

X_AXES = ("flow_cm_s", "o2_pct", "pressure_atm", "thickness_mm", "droplet_d0_mm")


def _numeric_outcomes(runs: list[dict]) -> Counter:
    return Counter(o["quantity"] for r in runs for o in r["outcomes"]
                   if (o.get("measure") or {}).get("min") is not None)


def _unresolved_investigation(q: dict) -> str | None:
    """The investigation NAME in q, if q asked for one and it resolves to no
    real investigation ("SAFFIRE-II" -- the real id is SAFFIRE-2) -- so an
    empty result can say the name wasn't recognised, not just "no data"."""
    name = q.get("investigation")
    if not name:
        return None
    _, invs = psi_query.load()
    return name if not psi_query._investigation_ids(name, invs) else None


def results_data(q: dict, quantity: str | None = None, x_axis: str = "flow_cm_s") -> dict:
    runs = _filtered_runs(q)
    available = _numeric_outcomes(runs)
    if not available:
        unresolved = _unresolved_investigation(q)
        return {"quantity": None, "available": {}, "mode": None, "points": [],
                **({"investigation_unresolved": unresolved} if unresolved else {})}
    if quantity not in available:
        quantity = available.most_common(1)[0][0]
    pts = []  # (run, x, y, source_raw)
    for r in runs:
        for o in r["outcomes"]:
            m = o.get("measure")
            if o["quantity"] != quantity or not m or m.get("min") is None:
                continue
            if x_axis == "flow_cm_s" and o.get("at", {}).get("flow_cm_s") is not None:
                x = o["at"]["flow_cm_s"]
            else:
                xm = _measure(r, x_axis)
                if not xm:
                    continue
                x = (xm["min"] + xm["max"]) / 2 if xm.get("value") is None else xm["value"]
            y = m["value"] if m.get("value") is not None else None
            pts.append({"run": r, "x": x, "y": y, "lo": m["min"], "hi": m["max"], "unit": m.get("unit"), "raw": m["raw"]})
    paired = [p for p in pts if p["y"] is not None and x_axis == "flow_cm_s"
              and any(o.get("at") for o in p["run"]["outcomes"] if o["quantity"] == quantity)]
    mode = "lines" if len({p["run"]["id"] for p in paired}) >= 2 and len(paired) >= 4 else "bars"
    return {"quantity": quantity, "available": dict(available.most_common(6)), "mode": mode,
            "points": paired if mode == "lines" else pts}


def results_widget(q: dict, quantity: str | None = None, x_axis: str = "flow_cm_s") -> Card:
    d = results_data(q, quantity, x_axis)
    title = query_title(_cat_q(q)) if _cat_q(q) else "all investigations"
    if not d["quantity"]:
        return Card(size="full", children=[Title(value="Results chart", size="md"),
                                           Text(value=f"No measured numeric results for {title}.", size="sm"),
                                           Divider(spacing=2), nav_buttons(q, skip="results")])
    qn = d["quantity"]
    qlabel = QUANTITY_LABEL.get(qn, qn.replace("_", " "))
    unit = next((p["unit"] for p in d["points"] if p["unit"]), "")
    xname = AXIS_LABEL.get(x_axis, x_axis)
    children = [Title(value=f"{qlabel} vs {xname}", size="md"), Caption(value=title)]

    if not d["points"]:
        children.append(Text(value=f"No test reports both {qlabel.lower()} and {xname}.", size="sm"))
    elif d["mode"] == "lines":
        # one line per test: the tests that swept flow and reported a result at each setting
        by_run: dict[str, list[dict]] = defaultdict(list)
        for p in d["points"]:
            by_run[p["run"]["id"]].append(p)
        chosen = sorted(by_run, key=lambda k: -len(by_run[k]))[:8]
        xs = sorted({p["x"] for k in chosen for p in by_run[k]})
        data = []
        for x in xs:
            row: dict = {"x": _fmt(x)}
            for k in chosen:
                for p in by_run[k]:
                    if p["x"] == x:
                        row[k] = p["y"]
            data.append(row)
        series = [LineSeries(dataKey=k, label=k, color=PALETTE[i % len(PALETTE)], curveType="linear")
                  for i, k in enumerate(chosen)]
        children += [
            Chart(data=data, series=series, xAxis={"dataKey": "x"}, showLegend=True, showTooltip=True, showYAxis=True,
                  height=260),
            Caption(value=f"x: {xname} ({_unit(x_axis)}) · y: {qlabel} ({unit}). Each line is one test measured at several "
                          f"flow settings{' (showing 8 of ' + str(len(by_run)) + ')' if len(by_run) > 8 else ''}.",
                    size="sm", color="tertiary"),
        ]
    else:
        pts = sorted(d["points"], key=lambda p: (p["x"], p["run"]["id"]))[:24]
        ranged = any(p["y"] is None or p["lo"] != p["hi"] for p in pts)
        data = [{"test": f"{p['run']['label']} · {_fmt(p['x'])}",
                 **({"low": p["lo"], "high": p["hi"]} if ranged else {"value": p["y"]})} for p in pts]
        series = ([BarSeries(dataKey="low", label="low end", color="#fdba74"),
                   BarSeries(dataKey="high", label="high end", color="#ea580c")] if ranged
                  else [BarSeries(dataKey="value", label=qlabel, color="#ea580c")])
        children += [
            Chart(data=data, series=series, xAxis={"dataKey": "test"}, showLegend=ranged, showTooltip=True, showYAxis=True,
                  height=260),
            Caption(value=f"One bar per test (label · {xname} in {_unit(x_axis)}), ordered by {xname}"
                          f"{'; ranges show the low and high end the source states' if ranged else ''}. "
                          f"{'Showing 24 of ' + str(len(d['points'])) + '.' if len(d['points']) > 24 else ''}",
                    size="sm", color="tertiary"),
        ]
    others = [k for k in d["available"] if k != qn][:4]
    switch = [Button(label=QUANTITY_LABEL.get(k, k.replace("_", " ")), size="xs", variant="soft",
                     onClickAction=action("results", q=q, quantity=k, x=x_axis)) for k in others]
    axes = [Button(label=f"vs {AXIS_LABEL[a]}", size="xs", variant="soft",
                   onClickAction=action("results", q=q, quantity=qn, x=a)) for a in X_AXES if a != x_axis][:4]
    children += [Caption(value="Other results:", size="sm"), Row(gap=2, wrap="wrap", children=switch)] if switch else []
    children += [Row(gap=2, wrap="wrap", children=axes), Divider(spacing=2), nav_buttons(q, skip="results")]
    return Card(size="full", children=children)


def results_summary(q: dict, quantity: str | None = None, x_axis: str = "flow_cm_s") -> dict:
    d = results_data(q, quantity, x_axis)
    pts = d["points"]
    return {"quantity": d["quantity"], "mode": d["mode"], "points": len(pts),
            "tests": len({p["run"]["id"] for p in pts}),
            "range": [min(p["lo"] for p in pts), max(p["hi"] for p in pts)] if pts else None,
            "unit": next((p["unit"] for p in pts if p["unit"]), None),
            "other_results_available": list(d["available"]),
            **({"investigation_unresolved": d["investigation_unresolved"]} if "investigation_unresolved" in d else {})}


# ── 6. ranking ───────────────────────────────────────────────────────────────
# Materials ranked by a measured result, within ONE geometry class (never
# across classes — folder = geometry class = comparability, see AGENTS.md).
# psi_query.rank() does the aggregation; this only draws it.

RANK_BAR_MAX = 220


def rank_widget(q: dict, quantity: str, geometry_class: str, direction: str = "desc", limit: int = 10) -> Card:
    r = psi_query.rank(q, quantity, geometry_class, direction, limit)
    qlabel = QUANTITY_LABEL.get(quantity, quantity.replace("_", " "))
    gc_label = GEOMETRY_LABEL.get(geometry_class, geometry_class)
    children = [Title(value=f"{qlabel}, ranked by material", size="md"),
                Caption(value=f"{gc_label} · {query_title(q) if q else 'no conditions given'}")]
    full_q = {**q, "geometry_class": geometry_class}

    if r.get("error"):
        children.append(Text(value=r["error"], size="sm", weight="semibold"))
        if r.get("rankable"):
            children.append(Caption(value="Rankable results in this class: "
                                          + ", ".join(QUANTITY_LABEL.get(x, x.replace("_", " ")) for x in r["rankable"]),
                                    size="sm"))
        children += [Divider(spacing=2), nav_buttons(full_q)]
        return Card(size="full", children=children)

    rows = r["rows"]
    if not rows:
        children.append(Text(value="No test at these conditions reports this result for any material.", size="sm"))
    else:
        top_val = max(row["median"] for row in rows) or 1.0
        for i, row in enumerate(rows, start=1):
            unit = f" {row['unit']}" if row.get("unit") else ""
            bar_w = max(6, round(RANK_BAR_MAX * row["median"] / top_val)) if top_val else 6
            children.append(Row(gap=2, align="center", wrap="wrap", children=[
                Box(width=22, children=[Caption(value=f"{i}.", size="sm", color="tertiary")]),
                Col(gap=1, flex=1, minWidth=180, children=[
                    Row(gap=2, align="center", wrap="wrap", children=[
                        Text(value=row["fuel_family"], size="sm", weight="semibold"),
                        Badge(label=f"n={row['n']}", color="secondary", size="sm"),
                        *([Badge(label=iv, color="secondary", variant="outline", size="sm") for iv in row["investigations"][:2]]),
                    ]),
                    Box(width=bar_w, height=10, radius="sm", background=PALETTE[(i - 1) % len(PALETTE)]),
                    Caption(value=f"median {_fmt(row['median'])}{unit} · range {_fmt(row['min'])}–{_fmt(row['max'])}{unit}",
                            size="sm", color="tertiary"),
                ]),
                Button(label="Evidence", size="xs", variant="ghost",
                       onClickAction=action("evidence", q={**full_q, "fuel_family": row["fuel_family"]})),
            ]))
        children.append(Caption(value=f"Ranked by median {qlabel.lower()} across tests at these conditions; "
                                      f"each row lists every contributing run, never an average across materials.",
                                size="sm", color="tertiary"))
    if r.get("untested"):
        shown = r["untested"][:8]
        more = len(r["untested"]) - len(shown)
        children.append(Caption(value=f"Not tested at these conditions: {', '.join(shown)}"
                                      + (f" (+{more} more)" if more > 0 else ""), size="sm", color="warning"))
    children += [Divider(spacing=2), nav_buttons(full_q)]
    return Card(size="full", children=children)


def rank_summary(q: dict, quantity: str, geometry_class: str, direction: str = "desc") -> dict:
    return psi_query.compact_rank(psi_query.rank(q, quantity, geometry_class, direction))


# ── 7. mission readiness ─────────────────────────────────────────────────────
# How much of a named mission atmosphere the PSI data actually covers, per
# geometry class — the coverage counts are computed by psi_query.readiness();
# every interpretive line beside them is a verbatim quote from a governed doc
# (psi-data/findings.yaml, checked by tests/test_findings.py). Nothing here
# states a safety conclusion itself.

DOCS_BASE_URL = "https://marjan-ahmed.github.io/flame-freefall/docs"


def _doc_url(stable_id: str) -> str:
    return f"{DOCS_BASE_URL}/{stable_id.removeprefix('knowledge/')}"


def readiness_widget(atm_id: str) -> Card:
    r = psi_query.readiness(atm_id)
    if r.get("error"):
        return Card(children=[Text(value=r["error"], size="sm", weight="semibold"),
                              Caption(value="Known atmospheres: " + ", ".join(r["known"]), size="sm")])
    atm = r["atmosphere"]
    general_findings = [f for f in r["findings"] if f.get("geometry_class") is None]
    children = [
        Title(value=f"Mission readiness: {atm['label']}", size="md"),
        Caption(value=f"O₂ {_fmt(atm['o2_pct'])}% · pressure {_fmt(atm['pressure_atm'])} atm "
                      f"(cell {atm['pressure_source_value']})"),
        Markdown(value=f"Source: [{atm['doc_title']}]({_doc_url(atm['doc'])}) — “{atm['quote']}”"),
    ]
    for f in general_findings:
        children.append(Caption(value=f"“{f['quote']}” — {f['doc_title']}", size="sm", color="tertiary"))
    children.append(Divider(spacing=2))

    for c in r["classes"]:
        gc_label = GEOMETRY_LABEL.get(c["geometry_class"], c["geometry_class"])
        lines = [Row(gap=2, align="center", children=[
            Text(value=gc_label, size="sm", weight="semibold"),
            Badge(label="covered" if c["covered"] else "GAP: not tested here",
                  color="success" if c["covered"] else "danger"),
        ]), Caption(value=f"{c['match']} at conditions · {c['partial']} partial", size="sm")]
        n = c["nearest_tested"]
        if n:
            o2 = f"{_fmt(n['o2_pct'])}%" if n["o2_pct"] is not None else "O₂ not reported"
            p = f"{_fmt(n['pressure_atm'])} atm" if n["pressure_atm"] is not None else "pressure not reported"
            lines.append(Caption(value=f"Nearest tested: {o2}, {p} ({n['tier']}, {n['investigation']})",
                                 size="sm", color="tertiary"))
        if c["quantities_available"]:
            lines.append(Caption(value="Measured here: " + ", ".join(
                QUANTITY_LABEL.get(q, q.replace("_", " ")) for q in c["quantities_available"][:5]), size="sm"))
        for f in r["findings"]:
            if f.get("geometry_class") == c["geometry_class"]:
                lines.append(Caption(value=f"“{f['quote']}” — {f['doc_title']}", size="sm",
                                     color="warning" if not c["covered"] else "tertiary"))
        lines.append(Button(label="Evidence at these conditions", size="xs", variant="outline",
                            onClickAction=action("evidence", q={**r["query"], "geometry_class": c["geometry_class"]})))
        children.append(Col(gap=1, padding=2, radius="md", border={"size": 1, "color": "subtle"}, children=lines))

    children += [Divider(spacing=2), Caption(value="Coverage is computed from data/runs.json; quotes above are "
                                                    "verbatim from the governed record, never generated.",
                                              size="sm", color="tertiary"),
                 Row(gap=2, wrap="wrap", children=[
                     Button(label=psi_atmospheres.ATMOSPHERES[other]["label"], size="sm", variant="soft",
                            onClickAction=action("readiness", atmosphere=other))
                     for other in psi_atmospheres.ATMOSPHERES if other != atm_id
                 ])]
    return Card(size="full", children=children)
