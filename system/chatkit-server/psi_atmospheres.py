"""Named mission-atmosphere presets for the ranking and readiness views.

Every number here is copied from a stable governed document and cited by its
stable id; nothing is computed from general knowledge. `tests/test_atmospheres.py`
checks each `quote` appears verbatim in its source file, so a preset can never
drift silently from the record it claims to summarize.

Mirrored in TypeScript at system/site/lib/psi-atmospheres.ts — keep both in
sync (there is no fixture pinning these; they change rarely and by hand).
"""

from __future__ import annotations

ATM_PER_KPA = 1 / 101.325
ATM_PER_PSIA = 1 / 14.696

ATMOSPHERES: dict[str, dict] = {
    "iss": {
        "id": "iss",
        "label": "ISS / ambient (NASA-STD-6001B)",
        "o2_pct": 20.9,
        "pressure_atm": round(101.4 * ATM_PER_KPA, 4),
        "pressure_source_value": "101.4 kPa (14.7 psia)",
        "doc": "knowledge/foundations/nasa-std-6001b",
        "doc_title": "NASA-STD-6001B",
        "quote": "ambient conditions are defined as 20.9% O₂, 101.4 kPa (14.7 psia), 23±5°C",
    },
    "gateway": {
        "id": "gateway",
        "label": "Lunar Gateway (proposed)",
        "o2_pct": 26.5,
        "pressure_atm": round(73.5 * ATM_PER_KPA, 4),
        "pressure_source_value": "73.5 kPa",
        "doc": "knowledge/foundations/decadal-survey/liao-micro-partial-gravity-fires",
        "doc_title": "Challenges and Research Needs for Micro- and Partial-Gravity Fires",
        "quote": "the Lunar Gateway is expected to have an oxygen concentration of 26.5% and a pressure of 73.5 kPa",
    },
    "lunar": {
        "id": "lunar",
        "label": "Lunar surface habitat (proposed)",
        "o2_pct": 34.0,
        "pressure_atm": round(56.5 * ATM_PER_KPA, 4),
        "pressure_source_value": "56.5 kPa",
        "doc": "knowledge/foundations/decadal-survey/liao-micro-partial-gravity-fires",
        "doc_title": "Challenges and Research Needs for Micro- and Partial-Gravity Fires",
        "quote": "the Lunar modules are expected to have an oxygen concentration of 34% and a pressure of 56.5 kPa",
    },
}


def preset(atm_id: str) -> dict | None:
    return ATMOSPHERES.get(atm_id)


def query_for(atm_id: str) -> dict:
    """The {o2_pct, pressure_atm} slice of a preset, ready to merge into a psi_query.query()."""
    a = ATMOSPHERES[atm_id]
    return {"o2_pct": a["o2_pct"], "pressure_atm": a["pressure_atm"]}
