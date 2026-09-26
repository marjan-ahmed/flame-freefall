"""The model's doors into the PSI run table. Each tool renders one widget
(psi_widgets.py) into the chat and hands the model a small, cited summary to
write 2-4 sentences from — the model supplies CONDITIONS, never values.

Replaces the old show_comparison tool, which asked the model for one flame
spread rate per investigation (BASS-II alone ran 129 tests; one number per
investigation is either an average nobody published or a value picked from
one test).

Every widget also carries buttons (Gap map, Compare, Results chart, Details)
that the server answers directly — see main.py action() — so after the first
answer the user can steer without another model call.
"""

from __future__ import annotations

import functools
import json
import time
from typing import Literal

from agents import RunContextWrapper, function_tool
from chatkit.agents import AgentContext

import psi_atmospheres
import psi_query
import psi_widgets

GeometryClass = Literal["solid-fuel", "droplet-combustion", "gaseous-flames", "smoke-aerosol"]
FlowDirection = Literal["opposed", "concurrent", "coflow", "stagnation"]
YAxis = Literal["flow_cm_s", "pressure_atm"]
XAxis = Literal["flow_cm_s", "o2_pct", "pressure_atm", "thickness_mm", "droplet_d0_mm"]
MissionAtmosphere = Literal["iss", "gateway", "lunar"]
RankDirection = Literal["asc", "desc"]

REPEAT_WINDOW_S = 120
_recent_calls: dict[tuple[str, str], float] = {}  # (thread id, tool+args) → last call time


def _site(ctx: RunContextWrapper[AgentContext]) -> str | None:
    """The site this chat is running on (set per request in main.py)."""
    rc = getattr(ctx.context, "request_context", None)
    return rc.get("site") if isinstance(rc, dict) else None


def _q(**kw) -> dict:
    return {k: v for k, v in kw.items() if v not in (None, "")}


def _is_repeat(ctx: RunContextWrapper[AgentContext], name: str, args: dict) -> bool:
    """gpt-oss sometimes re-issues the identical call after reading the result
    (seen live 2026-09-24: two identical calls, two identical cards). A repeat
    in the same thread shortly after gets the data back but no second card."""
    key = (ctx.context.thread.id, name + json.dumps(args, sort_keys=True))
    now = time.monotonic()
    repeat = now - _recent_calls.get(key, -1e9) < REPEAT_WINDOW_S
    _recent_calls[key] = now
    return repeat


def _guarded(fn):
    """Record on this turn's TurnGuard any exception a PSI tool raises (a
    widget-stream failure, a bad payload, …), then re-raise so the agents
    SDK still converts it to its own "An error occurred while running the
    tool..." string exactly as before -- this only ADDS a trace for the
    reply guard. main.py's on_tool_end failure check only recognises the
    "search"/"read" tool names (the MCP door), so a PSI tool's own failure
    was otherwise invisible to should_override_reply(): no widget shown, no
    override set, and the model free to write "no tests match" instead of
    an honest "couldn't run that query" (see C8). record_tool_result(name,
    None) already classifies a None payload as a failure for ANY tool
    name -- see TurnGuard._classify_failure -- so no guard changes needed."""
    @functools.wraps(fn)
    async def wrapper(ctx: RunContextWrapper[AgentContext], *args, **kwargs):
        try:
            return await fn(ctx, *args, **kwargs)
        except Exception:
            ctx.context._guard.record_tool_result(fn.__name__, None)
            raise
    return wrapper


def _reply(repeat: bool, instructions: str, payload: dict, cite_run_ids: bool = True) -> str:
    head = ("You already showed this exact widget; do not call the tool again. " if repeat
            else "Widget shown to the user. ")
    cite = (" Cite run ids in parentheses using the FULL id exactly as given in each "
            "result's \"id\" field, e.g. (PSI-25:M18) — never drop the ':M18' part and cite just the dataset "
            "(PSI-25) on its own, and never reuse one citation for two different runs; no other citation markup; "
            "no tables." if cite_run_ids else
            " This payload has no per-run \"id\" field — do not write any parenthetical run-id citation "
            "(nothing like (PSI-25:M18)) in this reply; no other citation markup; no tables.")
    return head + instructions + cite + "\n" + json.dumps(payload, ensure_ascii=False)


@function_tool(
    description_override=(
        "Find the NASA PSI microgravity-combustion tests at given CONDITIONS and show a cited evidence card "
        "(tests at the conditions, partial matches, nearest tests, coverage gaps). Use for any question about "
        "which tests exist or what was measured at some O2 %, flow cm/s, pressure atm, or fuel. Pass only what "
        "the user stated. fuel_family e.g. PMMA, SIBAL, Nomex, silicone, n-heptane, methanol, n-dodecane, "
        "ethylene, methane, propane, propylene."
    )
)
@_guarded
async def query_test_runs(
    ctx: RunContextWrapper[AgentContext],
    o2_pct: float | None = None,
    flow_cm_s: float | None = None,
    pressure_atm: float | None = None,
    fuel_family: str | None = None,
    geometry_class: GeometryClass | None = None,
    flow_direction: FlowDirection | None = None,
    investigation: str | None = None,
) -> str:
    q = _q(o2_pct=o2_pct, flow_cm_s=flow_cm_s, pressure_atm=pressure_atm, fuel_family=fuel_family,
           geometry_class=geometry_class, flow_direction=flow_direction, investigation=investigation)
    if not q:
        return "Please narrow your question — at least one condition (O₂ %, flow cm/s, pressure atm, fuel, geometry, investigation) is required to query the PSI test table."
    result = psi_query.query(q)
    print(f"[query_test_runs] {q} -> {result['counts']}")
    repeat = _is_repeat(ctx, "query", q)
    if not repeat:
        await ctx.context.stream_widget(psi_widgets.evidence_widget(q, result, site=_site(ctx)))
    payload = psi_query.compact(result)
    # The model is asked below to cite run ids inline in its prose; nothing
    # validates it got the id right (unlike the widget, which is rendered
    # from this same payload by code, not retyped). Record every id this
    # payload actually contains so main.py's response-text guard can check
    # the model's citations against it after the turn completes.
    ctx.context._guard.record_valid_run_ids(
        {v["id"] for tier in ("match", "partial", "near") for v in payload.get(tier, [])}
    )
    return _reply(repeat, "Reply in at most 90 words: (1) how many tests match all conditions, say plainly if none; "
                          "(2) how many are partial and which condition they don't report; "
                          "(3) if matches > 0, cite 2–3 representative run ids with their measured values exactly as "
                          "listed — never merge two runs into one approximate number; "
                          "(4) conflicts if any. The widget already has buttons; do not write button labels or "
                          "bracketed links in your reply. Do NOT list all matching runs — the widget shows them.",
                  payload)


@function_tool(
    description_override=(
        "Show the GAP MAP: a grid of O2 bands × flow (or pressure) bands, each cell shaded by how many tests were "
        "run there, the user's target outlined, empty cells = conditions never tested. Use when the user asks what "
        "has or hasn't been tested, where the gaps are, or how well conditions are covered. Filters narrow it to a "
        "fuel / geometry / investigation."
    )
)
@_guarded
async def show_gap_map(
    ctx: RunContextWrapper[AgentContext],
    o2_pct: float | None = None,
    flow_cm_s: float | None = None,
    pressure_atm: float | None = None,
    fuel_family: str | None = None,
    geometry_class: GeometryClass | None = None,
    flow_direction: FlowDirection | None = None,
    investigation: str | None = None,
    y_axis: YAxis = "flow_cm_s",
) -> str:
    q = _q(o2_pct=o2_pct, flow_cm_s=flow_cm_s, pressure_atm=pressure_atm, fuel_family=fuel_family,
           geometry_class=geometry_class, flow_direction=flow_direction, investigation=investigation)
    summary = psi_widgets.gap_map_summary(q, y_axis)
    print(f"[show_gap_map] {q} y={y_axis} -> {summary}")
    repeat = _is_repeat(ctx, f"gap:{y_axis}", q)
    if not repeat:
        await ctx.context.stream_widget(psi_widgets.gap_map_widget(q, y_axis))
    return _reply(repeat, "Reply in at most 70 words: how many cells have tests, whether the target cell is tested "
                          "(and by which investigations), and one notable gap. tested_cells lists EVERY cell that has "
                          "a test; untested_bands lists every untested region directly — name gaps from that list, "
                          "not by inference. Do not restate individual cell counts — the widget shows every one; "
                          "speak in O2 / flow ranges.",
                  summary, cite_run_ids=False)


@function_tool(
    description_override=(
        "Show investigations SIDE BY SIDE (one column each): records, how many tests are at / near the conditions, "
        "the O2 / flow / pressure ranges each covered, and the range of its main measured results. Use for "
        "'compare X and Y', 'which investigation is most relevant', or cross-investigation questions. "
        "investigations: optional names like ['SAFFIRE-2','BASS-II']; omit to compare all that match the filters."
    )
)
@_guarded
async def compare_investigations(
    ctx: RunContextWrapper[AgentContext],
    investigations: list[str] | None = None,
    o2_pct: float | None = None,
    flow_cm_s: float | None = None,
    pressure_atm: float | None = None,
    fuel_family: str | None = None,
    geometry_class: GeometryClass | None = None,
) -> str:
    q = _q(o2_pct=o2_pct, flow_cm_s=flow_cm_s, pressure_atm=pressure_atm, fuel_family=fuel_family,
           geometry_class=geometry_class)
    rows = psi_widgets.compare_data(q, investigations)
    print(f"[compare_investigations] {q} {investigations} -> {[r['name'] for r in rows]}")
    repeat = _is_repeat(ctx, "compare", {**q, "inv": investigations})
    if not repeat:
        await ctx.context.stream_widget(psi_widgets.compare_widget(q, investigations))
    payload = [{"inv": r["name"], "class": r["geometry_class"], "fuels": r["fuels"], "records": r["records"], "match": r["match"],
                "partial": r["partial"],
                "ranges": {k: (f"{a['min']:g}-{a['max']:g}" if a else "not reported") for k, a in r["axes"].items()},
                "results": [f"{x['quantity']} {x['min']:g}-{x['max']:g} {x['unit'] or ''} (n={x['n']})" for x in r["results"]],
                "conflicts": r["conflicts"]} for r in rows[:6]]
    return _reply(repeat, "Reply in at most 90 words comparing them: which covers the conditions best, what each "
                          "measured, and any caveat. A shared geometry class makes results comparable in kind, not "
                          "interchangeable: name the fuels when they differ, and never call two results directly "
                          "comparable across different fuels or classes. Mention conflicts if any. Refer to "
                          "investigations by name.", {"columns": payload}, cite_run_ids=False)


@function_tool(
    description_override=(
        "Show ONE test's full record: every condition with its original cell, every result, the sources "
        "(PSI table line, NASA report table/page) and any disagreement between sources. Use when the user names a "
        "test id (e.g. PSI-25:M18, PSI-69:FLEX-157) or asks for details of one test."
    )
)
@_guarded
async def show_test_details(ctx: RunContextWrapper[AgentContext], run_id: str) -> str:
    runs, _ = psi_query.load()
    run = next((r for r in runs if r["id"].lower() == run_id.strip().lower()), None)
    if run is None:
        return f"No test with id {run_id!r}. Ids look like PSI-25:M18 — use query_test_runs to find tests."
    print(f"[show_test_details] {run['id']}")
    repeat = _is_repeat(ctx, "test", {"id": run["id"]})
    if not repeat:
        await ctx.context.stream_widget(psi_widgets.test_widget(run["id"], site=_site(ctx)))
    # This tool's own reply also cites the run id (see _reply below); without
    # this, the guard has nothing to check a fabricated id from THIS tool
    # against (query_test_runs already records its own matches/partials).
    ctx.context._guard.record_valid_run_ids({run["id"]})
    # Each result, and each side of a conflict, names the source that holds it
    # (report table + title, or PSI line) -- never a bare index to guess at.
    payload = {"id": run["id"], "results": [psi_query.fmt_sourced_outcome(o) for o in psi_query._outcome_summary(run, {})][:6],
               "conflicts": psi_query.sourced_conflicts(run), "sources": len(run["sources"])}
    return _reply(repeat, "Reply in at most 60 words: what this test was and what it measured.", payload)


@function_tool(
    description_override=(
        "Plot measured RESULTS against a condition as a chart (e.g. flame spread rate vs flow, burning-rate "
        "constant vs O2, smoke-point length). Tests that swept flow are drawn one line each; otherwise one bar per "
        "test. quantity e.g. spread_rate, burning_rate_k, extinction_diameter, burn_time, smoke_point_length; omit "
        "to use the result measured most often for these filters. Pass only the filters the user actually stated — "
        "never guess geometry_class, flow_direction, or investigation from what's typical for a fuel; an "
        "unstated filter must stay None, even if that returns more tests than a narrower guess would."
    )
)
@_guarded
async def plot_results(
    ctx: RunContextWrapper[AgentContext],
    quantity: str | None = None,
    x_axis: XAxis = "flow_cm_s",
    fuel_family: str | None = None,
    geometry_class: GeometryClass | None = None,
    flow_direction: FlowDirection | None = None,
    investigation: str | None = None,
) -> str:
    q = _q(fuel_family=fuel_family, geometry_class=geometry_class, flow_direction=flow_direction,
           investigation=investigation)
    summary = psi_widgets.results_summary(q, quantity, x_axis)
    print(f"[plot_results] {q} {quantity} vs {x_axis} -> {summary}")
    repeat = _is_repeat(ctx, f"plot:{quantity}:{x_axis}", q)
    if not repeat:
        await ctx.context.stream_widget(psi_widgets.results_widget(q, quantity, x_axis))
    return _reply(repeat, "Reply in at most 60 words: what the chart shows (quantity, how many tests, the range) — "
                          "describe only what is plotted; do not infer trends the values don't show. If "
                          "\"investigation_unresolved\" is present, say plainly that name isn't a recognized "
                          "investigation — never present it as \"no data\" for a real one. Otherwise, if \"tests\" "
                          "is 0 or \"points\" is 0, say plainly there is no plottable data for these filters and "
                          "suggest widening them — do not invent a range or a test count.", summary, cite_run_ids=False)


@function_tool(
    description_override=(
        "RANK materials within ONE geometry class by a measured result — highest or lowest first. Use for "
        "'which material burns fastest/slowest', 'rank fuels by...', or any question that names an order. Never "
        "compares across geometry classes. quantity must fit geometry_class: solid-fuel -> spread_rate; "
        "droplet-combustion -> burning_rate_k or extinction_diameter; gaseous-flames -> burn_time or "
        "peak_burner_temp_c. atmosphere: a named mission atmosphere ('iss', 'gateway' for the Lunar Gateway, "
        "'lunar' for a Lunar surface habitat) — use this when the user names a mission, the ISS, the Gateway, the "
        "Moon, or Artemis instead of stating O2 %% / pressure atm directly; it sets o2_pct and pressure_atm from "
        "the governed record. Explicit o2_pct/pressure_atm/flow_cm_s override the atmosphere if both are given."
    )
)
@_guarded
async def rank_results(
    ctx: RunContextWrapper[AgentContext],
    # The full GeometryClass, not RankableGeometryClass: excluding
    # smoke-aerosol from the schema made Groq reject a call naming it with a
    # raw tool-validation error the model never sees as a normal reply (an
    # APIError, not an APIStatusError, so _FallbackCompletions never even
    # tries the next provider) -- the whole turn then showed a false
    # "rate limit or quota exhausted" message instead of psi_query.rank()'s
    # own honest "not rankable, here's what is" refusal (see C8). Accepting
    # every real class here and letting rank() answer is the fix.
    geometry_class: GeometryClass,
    quantity: str,
    atmosphere: MissionAtmosphere | None = None,
    o2_pct: float | None = None,
    pressure_atm: float | None = None,
    flow_cm_s: float | None = None,
    fuel_family: str | None = None,
    direction: RankDirection = "desc",
) -> str:
    base = psi_atmospheres.query_for(atmosphere) if atmosphere else {}
    q = {**base, **_q(o2_pct=o2_pct, pressure_atm=pressure_atm, flow_cm_s=flow_cm_s, fuel_family=fuel_family)}
    result = psi_query.rank(q, quantity, geometry_class, direction)
    print(f"[rank_results] {geometry_class} {quantity} {q} dir={direction} -> "
          f"{result.get('total_ranked', result.get('error'))}")
    repeat = _is_repeat(ctx, f"rank:{geometry_class}:{quantity}:{direction}", q)
    if not repeat:
        await ctx.context.stream_widget(psi_widgets.rank_widget(q, quantity, geometry_class, direction))
    payload = psi_query.compact_rank(result)
    if result.get("error"):
        return _reply(repeat, "Reply in at most 40 words: say this quantity can't be ranked for this geometry "
                              "class and name what CAN be ranked instead (the \"rankable\" list). Do not invent "
                              "a ranking.", payload, cite_run_ids=False)
    return _reply(repeat, "Reply in at most 90 words: name the top few materials in rank order with their median "
                          "value exactly as given (never compute your own average or rank order) — each is a "
                          "median over n runs (given per material), not one test's number, so refer to materials "
                          "by name, never by a run id. Mention at most one 'untested_at_these_conditions' "
                          "material worth noting.", payload, cite_run_ids=False)


@function_tool(
    description_override=(
        "Show MISSION READINESS: how much PSI test data exists near a named mission atmosphere (iss, gateway for "
        "the Lunar Gateway, lunar for a Lunar surface habitat), per geometry class, next to what the governed "
        "record says about why a gap matters. Use for 'is there data for the Moon/Gateway/34% oxygen', 'are we "
        "ready for a Lunar atmosphere', or any question about coverage of a mission environment rather than a "
        "specific fuel or test."
    )
)
@_guarded
async def show_mission_readiness(ctx: RunContextWrapper[AgentContext], atmosphere: MissionAtmosphere) -> str:
    result = psi_query.readiness(atmosphere)
    print(f"[show_mission_readiness] {atmosphere} -> "
          f"{[(c['geometry_class'], c['covered']) for c in result.get('classes', [])]}")
    repeat = _is_repeat(ctx, "readiness", {"atmosphere": atmosphere})
    if not repeat:
        await ctx.context.stream_widget(psi_widgets.readiness_widget(atmosphere))
    payload = psi_query.compact_readiness(result)
    return _reply(repeat, "Reply in at most 90 words: say which geometry classes are covered near this "
                          "atmosphere and which are a gap, exactly as the payload states — a class with 0 match "
                          "and 0 partial is a gap, say so plainly. If a class has a quoted finding, work its "
                          "quote or its substance into the sentence about that class. Never invent a safety "
                          "conclusion beyond what a quote or the coverage numbers state.", payload,
                  cite_run_ids=False)


TOOLS = [query_test_runs, show_gap_map, compare_investigations, show_test_details, plot_results, rank_results,
         show_mission_readiness]
