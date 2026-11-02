from psi_ingest.adapters.smoke import same_r, link_same_r_identifiers
from psi_ingest.adapters import Ctx
from psi_ingest.cli import REPO_ROOT, load_registry
from psi_ingest.model import Run, cat


def test_real_same_r_relationships_preserve_source_and_ambiguity():
    ctx = Ctx(repo_root=REPO_ROOT, raw_dir=REPO_ROOT / "psi-data/raw", registry=load_registry())
    runs = same_r(ctx)
    assert len(runs) == 109
    relationships = [r.observation_relationship for r in runs]
    assert len({r["base_test_number"] for r in relationships}) == 66
    assert len({r["group_id"] for r in relationships if r["group_id"]}) == 65
    assert all(r["independence"] == "unknown" and r["source"] == 0 for r in relationships)
    by_label = {r["source_label"]: r for r in relationships}
    assert by_label["51a"]["role"] == "unspecified"  # suffix is not an aging claim
    assert by_label["61a"]["role"] == "aged"
    assert by_label["51"]["group_id"] == by_label["51a"]["group_id"]
    ambiguous = [r for r in relationships if r["base_test_number"] == "57"]
    assert len({r["material"] for r in ambiguous}) == 2
    assert all(r["status"] == "ambiguous_identifier" and r["group_id"] is None for r in ambiguous)
    for r in runs:
        relation = r.to_json()["observation_relationship"]
        assert relation["source_label"] == r.raw[0]["SAME Test #"].strip()
        assert relation["description"] == r.raw[0]["Description"].strip()


def test_duplicate_source_labels_are_not_joined():
    runs = []
    for _ in range(2):
        run = Run("same-r", "SAME #51")
        run.conditions["fuel"] = cat("Kapton")
        run.observation_relationship = {"base_test_number": "51", "source_label": "51", "material": "Kapton"}
        runs.append(run)
    link_same_r_identifiers(runs)
    assert all(r.observation_relationship["group_id"] is None for r in runs)
    assert all(r.observation_relationship["status"] == "ambiguous_identifier" for r in runs)


def test_relationship_is_optional_for_existing_records():
    assert "observation_relationship" not in Run("flex", "sample").to_json()
