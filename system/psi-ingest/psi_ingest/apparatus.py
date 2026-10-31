"""Documented campaign hardware, explicitly inherited, never test atmosphere.

These fields describe the apparatus, not specimen dimensions or measured
conditions. Every quote must still occur in the saved source extraction;
citations are resolved from the governed record.
"""
import re
from . import knowledge
from .model import cat
from .units import Measure

RULES = [
    ({"bass"}, "knowledge/investigations/solid-fuel/bass", "bass-iss-overview-2013",
     "psi-data/derived/report-extractions/ISS Denver 2013-BASS.md",
     "Fuel samples were mounted inside a small wind tunnel which could impose airflow speeds up to 40 cm/s",
     {"apparatus": "BASS small wind tunnel", "confinement": "wind tunnel"}, {}),
    ({"bass-ii"}, "knowledge/investigations/solid-fuel/bass-ii", "bass-ii-tm-2021",
     "psi-data/derived/report-extractions/BASS-II Summary Report.md",
     "The black anodized 7.6- by 7.6- by 17-cm rectangular flow duct with rounded corners",
     {"apparatus": "BASS-II rectangular flow duct", "confinement": "rectangular flow duct"},
     {"duct_width_cm": (7.6, "cm"), "duct_height_cm": (7.6, "cm"), "duct_length_cm": (17, "cm")}),
    ({"saffire-1", "saffire-2"}, "knowledge/investigations/solid-fuel/saffire", "saffire-results-2017",
     "investigation_reports/_converted/saffire.md", 'The Saffire flow duct (18" x 20").',
     {"apparatus": "Saffire I–II flow duct", "confinement": "flow duct"}, {}),
    ({"saffire-iv-vi"}, "knowledge/investigations/solid-fuel/saffire", "saffire-vi-ices-2024",
     "investigation_reports/_converted/Saffire-ICES-2024-ICES-365-accepted final.md",
     "the tests were conducted in a rectangular flow tunnel that was 30 cm high by 45 cm wide by 109 cm long.",
     {"apparatus": "Saffire IV–VI rectangular flow tunnel", "confinement": "rectangular flow tunnel"},
     {"duct_width_cm": (45, "cm"), "duct_height_cm": (30, "cm"), "duct_length_cm": (109, "cm")}),
]


def normalized(text):
    return re.sub(r"\s+", " ", text).strip()


def enrich_apparatus(ctx, runs):
    for invs, doc, source_id, extraction, quote, categories, dimensions in RULES:
        for path in (ctx.repo_root / extraction,):
            if normalized(quote) not in normalized(path.read_text(encoding="utf-8")):
                raise ValueError(f"Apparatus quote changed: {path}: {quote}")
        citation = knowledge.citation(ctx.repo_root, doc, source_id)
        for run in runs:
            if run.investigation not in invs:
                continue
            index = len(run.sources)
            run.sources.append({"kind": "report", "table": "Campaign apparatus description",
                                "via": extraction, "quote": quote, "scope": "campaign apparatus", **citation})
            run.raw.append({"apparatus quote": quote})
            for key, value in categories.items():
                if key not in run.conditions:
                    run.conditions[key] = {**cat(value, basis="documented campaign apparatus; not a test-specific measurement"), "source": index}
            for key, (value, unit) in dimensions.items():
                if key not in run.conditions:
                    run.conditions[key] = Measure(raw=quote, value=value, unit=unit,
                                                  flags=["documented_apparatus", f"from_source_{index}"])
