"""Guard the public Lunar case study against drift in the PSI table/query.

The landing page computes the same condition query through its TypeScript twin;
the existing golden fixtures pin that twin to this production implementation.
If this test changes, review the public case-study wording and representative
links before treating the new counts as a finding.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from psi_query import readiness  # noqa: E402


def test_lunar_case_study_is_a_reproducible_coverage_gap() -> None:
    result = readiness("lunar")
    classes = {item["geometry_class"]: item for item in result["classes"]}

    assert result["atmosphere"]["o2_pct"] == 34.0
    assert result["atmosphere"]["pressure_source_value"] == "56.5 kPa"
    assert classes["gaseous-flames"]["match"] == 10
    assert classes["gaseous-flames"]["partial"] == 75
    assert classes["gaseous-flames"]["nearest_tested"]["run_id"] == "PSI-159:21153 F1"
    assert classes["solid-fuel"]["match"] == 0
    assert classes["solid-fuel"]["partial"] == 0
    assert classes["solid-fuel"]["nearest_tested"]["run_id"] == "saffire-iv-vi:VI-2"
