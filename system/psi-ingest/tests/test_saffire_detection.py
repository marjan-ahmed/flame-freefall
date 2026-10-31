from copy import deepcopy

import pytest

from psi_ingest.adapters import Ctx
from psi_ingest.cli import REPO_ROOT, run
from psi_ingest.model import Run
from psi_ingest.saffire_detection import GUARDS, merge_saffire_detection


def test_threshold_is_test_specific_and_not_ignition_delay():
    records = run(write=False)["runs"]
    selected = [(r, o) for r in records for o in r["outcomes"]
                if o["quantity"] == "smoke_threshold_crossing_time"]
    assert len(selected) == 1
    record, outcome = selected[0]
    assert record["id"] == "saffire-iv-vi:VI-3"
    assert outcome["measure"]["value"] == 981 and outcome["measure"]["unit"] == "s"
    assert outcome["at"] == {"selected_mass_concentration_mg_m3": 1}
    assert "does not establish an ignition-to-alarm delay" in outcome["note"]
    source = record["sources"][outcome["source"]]
    assert source["source_id"] == "saffire-vi-ices-2024" and "VI-3" in source["table"]
    assert "Figure 7" in source["quote"]


@pytest.mark.parametrize("count", [0, 2])
def test_identity_is_required(count):
    ctx = Ctx(REPO_ROOT, REPO_ROOT / "psi-data/raw", {})
    with pytest.raises(ValueError, match="exactly one VI-3"):
        merge_saffire_detection(ctx, [Run("saffire-iv-vi", "VI-3") for _ in range(count)])


def test_source_guard_drift_fails_closed(monkeypatch):
    from psi_ingest import saffire_detection
    monkeypatch.setattr(saffire_detection, "GUARDS", (*GUARDS, "invented source sentence"))
    ctx = Ctx(REPO_ROOT, REPO_ROOT / "psi-data/raw", {})
    record = Run("saffire-iv-vi", "VI-3")
    with pytest.raises(ValueError, match="source guard missing"):
        merge_saffire_detection(ctx, [record])
    assert not record.sources and not record.outcomes
