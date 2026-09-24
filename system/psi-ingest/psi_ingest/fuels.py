"""Fuel-family and sample-form vocabulary.

A family is assigned only when the source text NAMES the material ("PMMA",
"SIBAL", "C2H4"…). Text that doesn't name one ("2 cm sphere", "1/4\" black
rod") returns family None here; an adapter may then infer it, but only from a
sourced statement, recorded as the condition's `basis`.
"""

from __future__ import annotations

import re

# Order matters: first match wins ("PMMA & Nomex" is a composite → its own family).
FAMILIES: list[tuple[str, str]] = [
    (r"pmma.*nomex|nomex.*pmma", "PMMA/Nomex composite"),
    (r"pmma", "PMMA"),
    (r"sibal|cotton[- ]fiberglass", "SIBAL (cotton-fiberglass)"),
    (r"cotton", "cotton"),
    (r"nomex", "Nomex"),
    (r"silicone", "silicone"),
    (r"ultem", "Ultem"),
    (r"kapton", "Kapton"),
    (r"teflon", "Teflon"),
    (r"lampwick", "lampwick"),
    (r"pyrell", "Pyrell"),
    (r"dibutyl|\bdbp\b", "dibutyl phthalate"),
    (r"japan wax", "wax (Japan)"),
    (r"paraff?in|parrafin", "wax (paraffin)"),
    (r"\bwax\b|candle", "wax (unspecified)"),
    # gases
    (r"propylene|c3h6", "propylene"),
    (r"c2h4|ethylene", "ethylene"),
    (r"c2h6|\bethane", "ethane"),
    (r"c3h8|propane", "propane"),
    (r"butane", "butane"),
    (r"h2.*ch4|ch4.*h2", "hydrogen/methane"),
    (r"ch4|methane", "methane"),
    (r"\bh2\b|hydrogen", "hydrogen"),
    # liquids (droplets)
    (r"methanol", "methanol"),
    (r"heptane.*iso-?octane|iso-?octane.*heptane", "n-heptane/iso-octane"),
    (r"heptane", "n-heptane"),
    (r"iso-?dodecane|c12h26.*iso", "n-dodecane/iso-dodecane"),
    (r"c12h26|dodecane", "n-dodecane"),
    (r"iso-?octane", "iso-octane"),
    (r"n-octane", "n-octane"),
    (r"decane", "n-decane"),
    (r"ethanol", "ethanol"),
    (r"propanol", "propanol/glycerol"),
]

FORMS: list[tuple[str, str]] = [
    (r"sphere|spherical", "sphere"),
    (r"\brod\b", "rod"),
    (r"slab", "slab"),
    (r"film|micron", "film"),
    (r"fabric|sibal|cloth|jersey", "fabric"),
    (r"candle", "candle"),
    (r"sheet", "sheet"),
]


def family(text: str | None) -> str | None:
    if not text:
        return None
    t = text.lower()
    for pattern, name in FAMILIES:
        if re.search(pattern, t):
            return name
    return None


def form(text: str | None) -> str | None:
    if not text:
        return None
    t = text.lower()
    for pattern, name in FORMS:
        if re.search(pattern, t):
            return name
    return None
