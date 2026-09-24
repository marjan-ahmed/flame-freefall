"""Every Mission Readiness finding must quote its cited governed document
verbatim (whitespace-normalized), exactly like tests/test_atmospheres.py for
the atmosphere presets — this file adds no fact, so it can't drift from one.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import psi_atmospheres  # noqa: E402
import psi_query  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def test_findings_file_is_non_empty():
    assert psi_query._findings()


def test_every_finding_quote_is_verbatim_in_its_doc():
    for f in psi_query._findings():
        doc_path = REPO_ROOT / (f["doc"] + ".md")
        assert doc_path.is_file(), f"{f['id']}: missing doc {doc_path}"
        text = _norm(doc_path.read_text(encoding="utf-8"))
        assert _norm(f["quote"]) in text, f"{f['id']}: quote not found verbatim in {f['doc']}"


def test_every_finding_scopes_to_a_real_atmosphere_and_class():
    for f in psi_query._findings():
        assert f.get("atmosphere") in (None, *psi_atmospheres.ATMOSPHERES), f["id"]
        assert f.get("geometry_class") in (None, "solid-fuel", "droplet-combustion", "gaseous-flames", "smoke-aerosol"), f["id"]
