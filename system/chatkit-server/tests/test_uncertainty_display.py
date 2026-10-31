import psi_query
from psi_widgets import _cond_text, results_data


def test_chat_and_detail_render_uncertainty_and_bounds():
    uncertain = {"raw": "10 +/- 2 s", "value": 10, "min": 10, "max": 10, "unit": "s",
                 "uncertainty": {"plus": 2, "minus": 2}}
    bound = {"raw": "<0.005 mg/m3", "unit": "mg/m3", "detection_limit": {"value": .005, "operator": "<"}}
    assert "reported uncertainty" in _cond_text(uncertain)
    assert "reported uncertainty" in psi_query._fmt_outcome({**uncertain, "quantity": "burn_time"})
    assert "reported bound" in _cond_text(bound) and "0.005" in _cond_text(bound)
    assert "reported bound" in psi_query._fmt_outcome({**bound, "quantity": "mass"})


def test_censored_results_are_never_plotted_as_exact_points(monkeypatch):
    run = {"id": "synthetic", "conditions": {"flow_cm_s": {"value": 5, "min": 5, "max": 5}},
           "outcomes": [{"quantity": "mass", "measure": {"raw": "<0.005", "detection_limit": {"operator": "<", "value": .005}}}]}
    monkeypatch.setattr("psi_widgets._filtered_runs", lambda q: [run])
    result = results_data({}, "mass")
    assert result["requested_unavailable"] and not result["points"]
