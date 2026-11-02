"""Outcome-specific method provenance, never campaign-wide numeric imputation.

FLEX burning-rate constants have a source-defined image/fit method. Extinction
diameters do not receive a blanket method: the report describes both observed
and extrapolated diameters. SAME-R channel headers identify instruments and
published processing, but do not establish calibration or uncertainty.
"""
from __future__ import annotations

import re

from . import knowledge
from .model import cat

FLEX_DOC = "knowledge/investigations/droplet-combustion/flex"
FLEX_EXTRACTION = "investigation_reports/_converted/flex.md"
FLEX_INSTRUMENT = "The backlit HiBMs view of the droplet provides the droplet size and droplet dynamics as a function of time."
FLEX_FIT = "Burning rate-average burning rate constant from a linear fit"
FLEX_FIT_AXIS = "of the droplet diameter squared versus time from shortly after"
FLEX_GOVERNED = "**Burning rate** — average burning-rate constant from a linear fit of droplet-diameter-squared vs. time, mm²/s."
DETECTORS = {
    "iss_detector_scatter_volts": ("ISS detector scattering channel", "ISS Detector Scatter (volts)"),
    "sts_detector_volts": ("STS detector voltage channel", "STS Detector (volts)"),
}


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def _metadata(value, quote, index, basis):
    return {**cat(value, raw=quote, basis=basis), "source": index, "quote": quote}


def enrich_measurement_methods(ctx, runs):
    extraction = (ctx.repo_root / FLEX_EXTRACTION).read_text(encoding="utf-8")
    fm, body = knowledge._split(knowledge.doc_path(ctx.repo_root, FLEX_DOC))
    if fm.get("status") != "stable" or normalize(FLEX_GOVERNED) not in normalize(body):
        raise ValueError("FLEX outcome method requires its unchanged stable governed definition")
    quotes = (FLEX_INSTRUMENT, FLEX_FIT, FLEX_FIT_AXIS)
    for quote in quotes:
        if normalize(quote) not in normalize(extraction):
            raise ValueError(f"FLEX method quote not found in original extraction: {quote}")
    citation = knowledge.citation(ctx.repo_root, FLEX_DOC, "flex-tp-2015")
    for run in runs:
        if run.investigation == "flex":
            outcomes = [o for o in run.outcomes if o.quantity == "burning_rate_k"]
            if not outcomes:
                continue
            index = len(run.sources)
            run.sources.append({"kind": "report", "table": "Sections 3 / 3.1 and Table IX key",
                                "via": FLEX_EXTRACTION, "scope": "campaign definition for burning_rate_k only; not per-test calibration or fit quality",
                                "quote": "\n".join(quotes), **citation})
            run.raw.append({"instrument quote": FLEX_INSTRUMENT, "method quote": FLEX_FIT, "fit axis quote": FLEX_FIT_AXIS})
            for outcome in outcomes:
                outcome.metadata["instrument"] = _metadata("HiBMs backlit droplet imaging", FLEX_INSTRUMENT, index, "source-defined instrument for this outcome only")
                outcome.metadata["measurement_method"] = _metadata("Average linear fit of droplet diameter squared versus time", FLEX_FIT, index, "Table IX outcome definition; supporting fit-axis fragment retained in source")
        elif run.investigation == "same-r":
            for outcome in run.outcomes:
                if outcome.quantity not in DETECTORS:
                    continue
                instrument, header = DETECTORS[outcome.quantity]
                if not 0 <= outcome.source < len(run.sources):
                    raise ValueError("Detector outcome has invalid original source index")
                source = run.sources[outcome.source]
                raw = run.raw[outcome.source]
                if source.get("kind") != "psi-workbook" or source.get("sheet") != "Reduced Data with ISS Det" or header not in raw:
                    raise ValueError(f"Detector metadata requires the exact admitted workbook channel: {header}")
                previous = source.get("quote", "")
                if header not in previous.splitlines():
                    source["quote"] = "\n".join(filter(None, (previous, header)))
                outcome.metadata["instrument"] = _metadata(instrument, header, outcome.source, "exact source workbook column, not inferred from investigation identity")
                outcome.metadata["processing_method"] = _metadata("Published cached workbook value; not recalculated", header, outcome.source, "source-processed cached value; formula retained in raw cells where supplied; calibration and uncertainty not established")
