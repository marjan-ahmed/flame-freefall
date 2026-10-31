from pathlib import Path
import re
import yaml
import pytest

from psi_ingest.cli import run
from psi_ingest.apparatus import enrich_apparatus, RULES, normalized
from psi_ingest.adapters import Ctx

ROOT = Path(__file__).resolve().parents[3]


def test_approved_literature_quotes_are_separate_from_test_index():
    collection = yaml.safe_load((ROOT / "psi-data/literature.yaml").read_text(encoding="utf-8"))
    for entry in collection["entries"]:
        text = (ROOT / entry["extraction"]).read_text(encoding="utf-8")
        assert normalized(entry["quote"]) in normalized(text)
        assert entry["section"] in text
        doc = (ROOT / (entry["document"] + ".md")).read_text(encoding="utf-8")
        assert f"status: {entry['status']}" in doc
        assert entry["status"] == "stable"
        assert entry["source"] in doc
        assert entry["granularity"] in ("publication-observation", "campaign-summary")
    runs = run(write=False)["runs"]
    assert not any(r["investigation"] in ("luci", "daft") for r in runs)
    assert all(r["granularity"] == "envelope" for r in runs if r["investigation"] == "flex-2")
    for r in runs:
        if r["investigation"] == "flex-2":
            for outcome in r["outcomes"]:
                assert "exact fuel identity" in outcome["note"]
                assert "literature-identified" in outcome["note"]
                assert r["sources"][outcome["source"]]["source_id"] == "flex-2-cool-flame-2014"


def test_apparatus_enrichment_keeps_pressure_unknown_and_source_index_resolvable():
    result = run(write=False)
    solids = [r for r in result["runs"] if "apparatus" in r["conditions"]]
    assert solids
    for r in solids:
        c = r["conditions"]["apparatus"]
        s = r["sources"][c["source"]]
        assert s["scope"] == "campaign apparatus" and s["kind"] == "report"
        assert s["quote"] in r["raw"][c["source"]]["apparatus quote"]
        assert normalized(s["quote"]) in normalized((ROOT / s["via"]).read_text(encoding="utf-8"))
    assert sum("pressure_atm" in r["conditions"] for r in result["runs"] if r["investigation"] in ("bass", "bass-ii")) == 0


def test_apparatus_quote_drift_fails_closed(tmp_path):
    extraction = tmp_path / RULES[0][3]
    extraction.parent.mkdir(parents=True)
    extraction.write_text("Source text changed", encoding="utf-8")
    with pytest.raises(ValueError, match="Apparatus quote changed"):
        enrich_apparatus(Ctx(repo_root=tmp_path, raw_dir=tmp_path, registry={}), [])
