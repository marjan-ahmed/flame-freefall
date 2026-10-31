from copy import deepcopy

import pytest

from psi_ingest import knowledge, verify
from psi_ingest.cli import REPO_ROOT, run

DOC = "knowledge/investigations/solid-fuel/saffire"
EXTRACTION = "investigation_reports/_converted/Saffire-ICES-2024-ICES-365-accepted final.md"
HEADING = "Measured outcomes (Table 2"


def test_far_field_outcomes_preserve_values_locations_and_sources():
    runs = run(write=False)["runs"]
    expected = {"IV-1": (25, 1.03), "V-2": (23, 1.26), "VI-2": (20, 1.15),
                "VI-3": (21, 3.51), "VI-4": (21, 3.37)}
    found = {}
    for r in runs:
        if r["investigation"] != "saffire-iv-vi":
            continue
        values = {}
        for o in r["outcomes"]:
            if o["quantity"] not in ("max_temp_ffd_nearest", "co2_partial_pressure_increase"):
                continue
            values[o["quantity"]] = o["measure"]["value"]
            assert o["measure"]["unit"] == ("°C" if o["quantity"] == "max_temp_ffd_nearest" else "mmHg")
            source = r["sources"][o["source"]]
            assert source["doc"] == DOC and source["table"] == "Table 2"
            assert source["source_id"] == "saffire-vi-ices-2024"
            assert source["doc_status"] == "stable"
        if values:
            found[r["label"]] = (values["max_temp_ffd_nearest"], values["co2_partial_pressure_increase"])
    assert found == expected


def test_ambiguous_energy_bundle_is_retained_but_quarantined():
    records = run(write=False)["runs"]
    record = next(r for r in records if r["id"] == "saffire-iv-vi:VI-2")
    bundle = {o["quantity"]: o for o in record["outcomes"] if
              "source_definition_unresolved" in o.get("measure", {}).get("flags", [])}
    assert set(bundle) == {"burn_time", "peak_heat_release", "total_heat_release_imaging", "avg_heat_release_o2", "total_heat_release_o2"}
    assert bundle["total_heat_release_imaging"]["measure"]["value"] == 580
    assert all("source_definition_unresolved" not in o.get("measure", {}).get("flags", [])
               for o in record["outcomes"] if o["quantity"] == "co2_partial_pressure_increase")


@pytest.mark.parametrize("change", ["value", "identity", "swap_columns"])
def test_table_transfer_requires_complete_source_row(change):
    columns, rows, _ = knowledge.table_under(REPO_ROOT, DOC, HEADING)
    rows = deepcopy(rows)
    if change == "value":
        rows[0][columns[8]] = "999"
    elif change == "identity":
        rows[0][columns[0]] = "VI-3"
    else:
        rows[0][columns[7]], rows[0][columns[8]] = rows[0][columns[8]], rows[0][columns[7]]
    with pytest.raises(verify.ExtractionNotVerified, match="exact source rows"):
        verify.verify_html_rows(REPO_ROOT, EXTRACTION, columns, rows)
