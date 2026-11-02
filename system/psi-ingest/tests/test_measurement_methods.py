"""Outcome-specific provenance is verified from sources, not guessed from a campaign name."""
from pathlib import Path
from types import SimpleNamespace

import pytest

from psi_ingest.cli import run
from psi_ingest import measurement_methods as methods
from psi_ingest.model import Run

ROOT = Path(__file__).resolve().parents[3]


@pytest.fixture(scope="module")
def result():
    return run(write=False)


def test_flex_fit_method_is_outcome_specific_and_has_verified_original_source(result):
    record = next(r for r in result["runs"] if r["id"] == "PSI-69:FLEX-001")
    rate = next(o for o in record["outcomes"] if o["quantity"] == "burning_rate_k")
    for key in ("instrument", "measurement_method"):
        c = rate["metadata"][key]
        source = record["sources"][c["source"]]
        assert c["quote"] in source["quote"]
        assert source["doc_status"] == "stable"
        assert source["via"] == methods.FLEX_EXTRACTION
        assert source["source_id"] == "flex-tp-2015"
    assert "squared versus time" in rate["metadata"]["measurement_method"]["value"]
    extinction = next(o for o in record["outcomes"] if o["quantity"] == "extinction_diameter")
    assert "metadata" not in extinction, "observed and extrapolated extinction methods must not be collapsed"
    assert "instrument" not in record["conditions"]


def test_same_r_instrument_names_come_from_exact_admitted_channel_headers(result):
    count = 0
    for record in result["runs"]:
        if record["investigation"] != "same-r":
            continue
        for outcome in record["outcomes"]:
            if outcome["quantity"] not in methods.DETECTORS:
                continue
            c = outcome["metadata"]["instrument"]
            source = record["sources"][c["source"]]
            assert c["source"] == outcome["source"]
            assert c["quote"] in record["raw"][c["source"]]
            assert source["kind"] == "psi-workbook"
            assert source["sheet"] == "Reduced Data with ISS Det"
            assert "measurement_method" not in outcome["metadata"], "processing does not establish scientific calibration"
            assert "not recalculated" in outcome["metadata"]["processing_method"]["value"]
            count += 1
    assert count > 100


def test_changed_method_quote_blocks_enrichment(monkeypatch):
    monkeypatch.setattr(methods, "FLEX_FIT", "A method nobody reported")
    with pytest.raises(ValueError, match="not found in original extraction"):
        methods.enrich_measurement_methods(SimpleNamespace(repo_root=ROOT), [])


def test_detector_channel_without_its_exact_source_header_is_rejected():
    record = Run("same-r", "SAME #57")
    record.sources.append({"kind": "psi-workbook", "sheet": "Reduced Data with ISS Det"})
    record.raw.append({"not the published header": "1"})
    record.outcome("iss_detector_scatter_volts", text="placeholder")
    with pytest.raises(ValueError, match="exact admitted workbook channel"):
        methods.enrich_measurement_methods(SimpleNamespace(repo_root=ROOT), [record])
