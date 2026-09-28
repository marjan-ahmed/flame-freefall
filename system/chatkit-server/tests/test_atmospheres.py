"""Every mission-atmosphere preset must quote its cited governed document
verbatim (whitespace-normalized — markdown line-wrapping isn't semantic), so
a preset's numbers can never drift from the record they claim to summarize.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import psi_atmospheres  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def test_every_preset_quote_is_verbatim_in_its_doc():
    for atm_id, a in psi_atmospheres.ATMOSPHERES.items():
        doc_path = REPO_ROOT / (a["doc"] + ".md")
        assert doc_path.is_file(), f"{atm_id}: missing doc {doc_path}"
        text = _norm(doc_path.read_text(encoding="utf-8"))
        assert _norm(a["quote"]) in text, f"{atm_id}: quote not found verbatim in {a['doc']}"


def test_pressure_atm_is_a_kpa_conversion_of_the_quoted_value():
    for atm_id, a in psi_atmospheres.ATMOSPHERES.items():
        kpa = float(a["pressure_source_value"].split()[0])
        assert abs(a["pressure_atm"] - kpa * psi_atmospheres.ATM_PER_KPA) < 1e-4, atm_id


def test_query_for_returns_only_numeric_axes():
    q = psi_atmospheres.query_for("lunar")
    assert set(q) == {"o2_pct", "pressure_atm"}
    assert q["o2_pct"] == 34.0
