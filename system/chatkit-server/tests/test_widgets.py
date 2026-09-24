"""Every widget must build (ChatKit validates the tree with pydantic) for the
queries users actually ask, stay a sane size, and never show a number that is
not in the data."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main  # noqa: E402  (imports the action router)
import psi_query  # noqa: E402
import psi_widgets as w  # noqa: E402

QUERIES = [
    {"o2_pct": 15, "flow_cm_s": 10, "fuel_family": "PMMA"},
    {"o2_pct": 21, "flow_cm_s": 20, "fuel_family": "sibal"},
    {"o2_pct": 30, "pressure_atm": 0.55},
    {"fuel_family": "propylene", "investigation": "spice"},
    {"geometry_class": "droplet-combustion"},
    {},
]


def _size(card) -> int:
    return len(card.model_dump_json())


@pytest.mark.parametrize("q", QUERIES)
def test_every_widget_builds(q):
    for card in (w.evidence_widget(q), w.gap_map_widget(q, "flow_cm_s"), w.gap_map_widget(q, "pressure_atm"),
                 w.compare_widget(q), w.results_widget(q)):
        assert _size(card) < 60_000


def test_test_widget_for_every_kind_of_record():
    for rid in ("PSI-25:M18", "PSI-98:S1", "PSI-69:FLEX-157", "spice:Smoke-point summary — C3H6", "PSI-101:SAME #62",
                "saffire-iv-vi:VI-3", "PSI-23:19304"):
        assert _size(w.test_widget(rid)) < 60_000


def test_gap_map_target_cell_is_honest():
    s = w.gap_map_summary({"o2_pct": 15, "flow_cm_s": 10, "fuel_family": "PMMA"})
    # no PMMA test states ~15 % O2 AND ~10 cm/s (the evidence query agrees)
    assert s["target_cell_tests"] == 0
    assert s["same_o2_band_axis_not_reported"] > 0


def test_results_chart_uses_per_flow_values():
    d = w.results_data({"fuel_family": "PMMA", "flow_direction": "opposed"}, "spread_rate", "flow_cm_s")
    assert d["mode"] == "lines"
    m7 = sorted((p["x"], p["y"]) for p in d["points"] if p["run"]["id"] == "PSI-25:M7")
    assert m7 == [(3, 0.07), (5, 0.083), (6, 0.099), (10, 0.106)]


def test_results_chart_keeps_ranges_as_ranges():
    d = w.results_data({"investigation": "spice"}, "smoke_point_length", "flow_cm_s")
    assert d["mode"] == "bars"
    card = json.loads(w.results_widget({"investigation": "spice"}, "smoke_point_length").model_dump_json())
    chart = next(c for c in card["children"] if c["type"] == "Chart")
    assert {"low", "high"} <= set(chart["data"][0])  # no midpoints invented


def test_compare_is_horizontal_and_cited():
    rows = w.compare_data({"o2_pct": 21, "flow_cm_s": 20, "fuel_family": "sibal"})
    names = [r["name"] for r in rows]
    assert "SAFFIRE-1" in names and "BASS-II" in names
    card = json.loads(w.compare_widget({"o2_pct": 21, "flow_cm_s": 20, "fuel_family": "sibal"}).model_dump_json())
    row = next(c for c in card["children"] if c["type"] == "Row")
    assert len(row["children"]) >= 2 and all(c["type"] == "Col" for c in row["children"])


def test_action_router_rejects_junk():
    assert main._action_widget("nope", {}) is None
    assert main._clean_query({"o2_pct": "15", "fuel_family": "PMMA", "evil": "x", "flow_cm_s": "abc"}) == {
        "o2_pct": 15.0, "fuel_family": "PMMA"}
    assert main._action_widget("gap_map", {"q": {"o2_pct": 15}, "y": "../../etc"}) is not None


def test_widget_numbers_come_from_the_data():
    """Every number shown in the M18 test widget is a value (or raw cell) in its record."""
    runs, _ = psi_query.load()
    m18 = next(r for r in runs if r["id"] == "PSI-25:M18")
    text = w.test_widget("PSI-25:M18").model_dump_json()
    for o in m18["outcomes"]:
        if o.get("measure", {}).get("value") is not None:
            assert f"{o['measure']['value']:g}" in text


def test_compare_resolves_investigation_families():
    # seen live: the model passed ['SAFFIRE', 'BASS-II'] and only BASS-II came back
    q = {"o2_pct": 21, "flow_cm_s": 20, "fuel_family": "SIBAL", "geometry_class": "solid-fuel"}
    names = {r["name"] for r in w.compare_data(q, ["SAFFIRE", "BASS-II"])}
    assert {"SAFFIRE-1", "SAFFIRE-2", "BASS-II"} <= names and "BASS" not in names
    assert {r["name"] for r in w.compare_data(q, ["BASS"])} == {"BASS"}


def test_gap_map_summary_lists_every_tested_cell():
    # seen live: with only counts, the model called high-O2/high-flow PMMA
    # untested although SAFFIRE VI tests sit there
    s = w.gap_map_summary({"fuel_family": "PMMA"})
    assert len(s["tested_cells"]) == s["cells_with_tests"]
    assert any(c.startswith("O2 30–35 % / flow 20–30") and "SAFFIRE IV–VI" in c for c in s["tested_cells"])


def test_details_buttons_have_unique_keys():
    # seen live: Details spun forever; the card's many Details buttons were
    # otherwise identical components
    card = json.loads(w.evidence_widget({"fuel_family": "PMMA"}).model_dump_json())
    keys = []

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "Button" and node.get("label") == "Details":
                keys.append(node.get("key"))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(card)
    assert keys and None not in keys and len(keys) == len(set(keys))


def test_explorer_link_follows_the_requesting_site():
    # seen live: the link pointed at localhost:3000 for every real user
    from starlette.requests import Request

    def req(origin):
        return Request({"type": "http", "headers": [(b"origin", origin.encode())]})

    assert main._site_for(req("https://marjan-ahmed.github.io")) == "https://marjan-ahmed.github.io/flame-freefall"
    assert main._site_for(req("http://localhost:3000")) == "http://localhost:3000"
    assert main._site_for(req("https://evil.example")) is None
    link = w.explorer_url({"o2_pct": 15}, site="https://marjan-ahmed.github.io/flame-freefall")
    assert link.startswith("https://marjan-ahmed.github.io/flame-freefall/explore/?")
    assert w.explorer_url({"o2_pct": 15}).startswith("https://marjan-ahmed.github.io/flame-freefall/explore/")


def test_a_failing_view_still_answers_the_button():
    import asyncio

    class T:
        id = "t"

    class A:
        type = "psi.test"
        payload = {"id": 123}  # not a string: _action_widget returns None

    async def collect():
        out = []

        async def fake_stream(thread, widget, copy, gen):
            yield widget

        orig = main.stream_widget
        main.stream_widget = fake_stream
        try:
            async for ev in main.server.action(T(), A(), None, {}):
                out.append(ev)
        finally:
            main.stream_widget = orig
        return out

    got = asyncio.run(collect())
    assert len(got) == 1  # a card came back, so the client's spinner ends


def test_details_expands_in_place_through_the_chatkit_protocol():
    """The browser's exact request for a sync button: threads.sync_custom_action.
    The reply must be the SAME card (same item id) with the row opened, so the
    clicked button resolves and the record appears where the user clicked."""
    import asyncio
    from datetime import datetime

    from chatkit.actions import Action
    from chatkit.store import NotFoundError  # noqa: F401  (import check)
    from chatkit.types import ThreadMetadata, ThreadsSyncCustomActionReq, ThreadCustomActionParams, WidgetItem

    from store import InMemoryChatKitStore

    srv = main.FlameFreefallChatKitServer(store=InMemoryChatKitStore(), attachment_store=main.attachment_store)
    q = {"fuel_family": "PMMA"}

    async def go():
        thread = ThreadMetadata(id="thr_t", created_at=datetime.now())
        await srv.store.save_thread(thread, context={})
        card = WidgetItem(id="wid_t", thread_id="thr_t", created_at=datetime.now(), widget=w.evidence_widget(q))
        await srv.store.add_thread_item("thr_t", card, context={})
        first = w.psi_query.prefer_outcomes(w.psi_query.query(q)["match"])[0]["id"]

        async def click(open_):
            req = ThreadsSyncCustomActionReq(params=ThreadCustomActionParams(
                thread_id="thr_t", item_id="wid_t",
                action=Action(type="psi.expand", payload={"q": q, "id": first, "open": open_})))
            res = await srv.process(req.model_dump_json().encode(), context={})
            return json.loads(res.json)["updated_item"]

        opened = await click(True)
        closed = await click(False)
        return first, opened, closed

    first, opened, closed = asyncio.run(go())
    assert opened["id"] == "wid_t"
    text = json.dumps(opened)
    assert '"Hide details"' in text and '"Conditions"' in text and '"Sources"' in text
    assert '"Hide details"' not in json.dumps(closed)
