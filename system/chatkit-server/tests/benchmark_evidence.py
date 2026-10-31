"""Offline retrieval/source audit and warm-query timings; no model or network.

Run from repo root with the backend venv Python. Source-cell checks use the
ingest venv (which contains openpyxl) via --source-audit in the companion
script. These are regression expectations, not expert relevance judgements.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import statistics
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "system/chatkit-server"))
import psi_query

CASES = [
    ("pure fuel", {"fuel_family": "n-dodecane"}, 22),
    ("explicit family", {"fuel_family": "n-dodecane*"}, 79),
    ("unknown material", {"fuel_family": "unsupported-material"}, 0),
    ("missing BASS pressure", {"investigation": "BASS", "pressure_atm": 1}, 0),
    ("unknown investigation", {"investigation": "unsupported-investigation"}, 0),
    ("unsupported atmosphere", {"o2_pct": 99, "pressure_atm": 100}, 0),
]


def benchmark(repeats=30):
    runs, _ = psi_query.load()
    results = []
    for name, query, expected in CASES:
        got = psi_query.query(query)
        assert got["counts"]["match"] == expected, name
        times = []
        for _ in range(repeats):
            start = time.perf_counter()
            psi_query.query(query)
            times.append((time.perf_counter() - start) * 1000)
        results.append({"name": name, "query": query, "expected_matches": expected,
                        "actual_matches": got["counts"]["match"], "passed": True,
                        "samples": repeats, "p50_ms": round(statistics.median(times), 3),
                        "p95_ms": round(sorted(times)[min(len(times)-1, int(.95*len(times)))], 3)})
    source_links = 0
    for run in runs:
        assert len(run["sources"]) == len(run["raw"])
        for outcome in run["outcomes"]:
            assert 0 <= outcome["source"] < len(run["sources"])
            source_links += 1
    flex = [r for r in runs if r["investigation"] == "flex-2"]
    assert flex and all(r["granularity"] == "envelope" for r in flex)
    literature = [o for r in flex for o in r["outcomes"]
                  if r["sources"][o["source"]].get("source_id") == "flex-2-cool-flame-2014"]
    assert len(literature) == 13
    assert all(s.get("doc_status") != "draft" for r in runs for s in r["sources"])
    saffire_checks = []
    for label, temperature, pressure in (("IV-1", 25, 1.03), ("V-2", 23, 1.26),
                                         ("VI-2", 20, 1.15), ("VI-3", 21, 3.51), ("VI-4", 21, 3.37)):
        record = next(r for r in runs if r["id"] == f"saffire-iv-vi:{label}")
        for quantity, value, unit in (("max_temp_ffd_nearest", temperature, "°C"),
                                      ("co2_partial_pressure_increase", pressure, "mmHg")):
            outcome = next(o for o in record["outcomes"] if o["quantity"] == quantity)
            assert outcome["measure"]["value"] == value and outcome["measure"]["unit"] == unit
            source = record["sources"][outcome["source"]]
            assert source["source_id"] == "saffire-vi-ices-2024" and source["table"] == "Table 2"
            saffire_checks.append({"run": record["id"], "quantity": quantity, "value": value, "unit": unit})
    return {"measured_at": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(),
            "platform": platform.platform(), "dataset_sha256": hashlib.sha256((ROOT / "psi-data/derived/runs.json").read_bytes()).hexdigest(),
            "scope": "Local warm deterministic query latency; offline regression cases and source-index validity. No live chatbot, MCP retrieval, predictive accuracy, scientific expert review or safety validation.",
            "cases": results, "source_indices_checked": source_links,
            "saffire_table2_checks": saffire_checks,
            "draft_sources_in_serving_data": 0,
            "flex2_envelopes": len(flex), "flex2_literature_outcomes": len(literature)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "research/evidence-benchmark.json")
    args = parser.parse_args()
    result = benchmark()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{len(result['cases'])} retrieval cases passed; {result['source_indices_checked']} outcome source indices checked; {args.output}")
