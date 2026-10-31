"""Join the identified VI-3 smoke-threshold observation; never infer ignition delay."""

import re

from . import knowledge
from .adapters import Ctx
from .model import Run
from .units import parse_measure

DOC = "knowledge/investigations/solid-fuel/saffire"
EXTRACTION = "investigation_reports/_converted/Saffire-ICES-2024-ICES-365-accepted final.md"
GUARDS = (
    "Figure 7. Far field ionization smoke detector and particulate matter measurements for Saffire VI-3 (two-sided PMMA).",
    "Selecting 1 mg/m3 as a relatively",
    "threshold at 981 seconds.",
    "hazardous gas release had occurred.",
)


def merge_saffire_detection(ctx: Ctx, runs: list[Run]) -> None:
    citation = knowledge.citation(ctx.repo_root, DOC, "saffire-vi-ices-2024")
    if citation["doc_status"] != "stable":
        raise ValueError("SAFFIRE detection observation requires an approved document")
    fold = lambda s: re.sub(r"\s+", " ", s).strip()
    extracted = fold((ctx.repo_root / EXTRACTION).read_text(encoding="utf-8"))
    for guard in GUARDS:
        if fold(guard) not in extracted:
            raise ValueError(f"SAFFIRE detection source guard missing: {guard}")
    doc = fold(knowledge.doc_path(ctx.repo_root, DOC).read_text(encoding="utf-8"))
    if "reached that threshold at 981 seconds" not in doc:
        raise ValueError("SAFFIRE detection observation missing from governed document")
    candidates = [r for r in runs if r.investigation == "saffire-iv-vi" and r.label == "VI-3"]
    if len(candidates) != 1:
        raise ValueError("SAFFIRE detection needs exactly one VI-3 record")
    run = candidates[0]
    source = len(run.sources)
    run.sources.append({"kind": "report", **citation, "table": "Figure 7 and accompanying text (VI-3)",
                        "via": EXTRACTION, "quote": " | ".join(GUARDS)})
    run.raw.append({"test": "VI-3", "reported_time_s": "981", "selected_threshold_mg_m3": "1",
                    "watched_sentence": " | ".join(GUARDS)})
    run.outcome("smoke_threshold_crossing_time", parse_measure("981", "s"), source=source,
                at={"selected_mass_concentration_mg_m3": 1},
                note="Saffire VI-3, Figure 7: far-field smoke threshold crossing at the report-selected "
                     "1 mg/m³ threshold. Time on the reported experiment timeline; the source does not "
                     "establish an ignition-to-alarm delay. Not an instrument detection limit, universal "
                     "alarm setting, or validated response-time specification. Much hazardous gas release "
                     "had already occurred, according to the report.")
