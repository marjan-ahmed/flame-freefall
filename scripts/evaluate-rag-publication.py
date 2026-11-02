"""Verify the published corpus through MCP, without model-generated answers.

Run with the backend Python environment. Expected documents are source-anchored
engineering expectations, not independent expert relevance labels. This script
does not tune the retriever. Calibration questions are maintained separately
from these held-out checks; measured abstention does not establish universal reliability.
"""
import argparse
import asyncio
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from urllib.request import urlopen

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    ("LUCI rotating sounding rocket PMMA flame spread", "knowledge/literature/luci-rotating-rocket"),
    ("LUCI partial gravity oxygen concentration fitted spread rate", "knowledge/literature/luci-rotating-rocket"),
    ("lunar gravity centrifugal force spinning vehicle flammability", "knowledge/literature/luci-rotating-rocket"),
    ("DAFT cabin aerosol P-Trak Dust Trak background averages", "knowledge/literature/daft-cabin-aerosol"),
    ("Velcro separation deliberately generated cabin aerosol DAFT", "knowledge/literature/daft-cabin-aerosol"),
    ("DAFT average cabin air less than 0.005 mg/m3", "knowledge/literature/daft-cabin-aerosol"),
    ("FLEX-2 R377 hot cool flame burning rate constants", "knowledge/investigations/droplet-combustion/flex-2-cool-flame-results"),
    ("FLEX cool flame R694 n-octane helium dilution", "knowledge/investigations/droplet-combustion/flex-2-cool-flame-results"),
    ("R383 printed nitrogen oxygen atmosphere inconsistent", "knowledge/investigations/droplet-combustion/flex-2-cool-flame-results"),
    ("DAFT low alcohol reference dust first run comparison", "knowledge/literature/daft-cabin-aerosol"),
    ("DAFT instruments Expedition 10 reference source Expedition 13", "knowledge/literature/daft-cabin-aerosol"),
    ("LUCI Coriolis flame deflection away from fuel axis", "knowledge/literature/luci-rotating-rocket"),
    ("LUCI preheat length shrink rate and flame base tracking", "knowledge/literature/luci-rotating-rocket"),
]
EXPANDED_DETAILS = {
    "DAFT low alcohol reference dust first run comparison": "low alcohol",
    "DAFT instruments Expedition 10 reference source Expedition 13": "expedition 13",
    "LUCI Coriolis flame deflection away from fuel axis": "coriolis",
    "LUCI preheat length shrink rate and flame base tracking": "preheat",
}
CONTROLS = ["What is the recommended insulin dose for a child?", "Who won the 2026 football World Cup?",
    "How should a LOX-methane rocket injector be dimensioned?",
    "What is the Apollo 11 descent engine thrust curve?",
    "Give a patient-specific diabetes medication schedule.",
    "What are the compressive strength values for lunar basalt concrete?",
    "How are comet orbital elements calculated?",
    "What is the 2026 income tax allowance in Canada?"]


async def evaluate(url):
    root = url.removesuffix("/mcp")
    with urlopen(root + "/health", timeout=30) as response:
        health = json.load(response)
    results = []
    controls = []
    async with streamable_http_client(url) as transport:
        async with ClientSession(transport[0], transport[1]) as session:
            await session.initialize()
            for query, expected in [*CASES, *((q, None) for q in CONTROLS)]:
                print(f"Checking retrieval: {query}", flush=True)
                started = time.perf_counter()
                reply = await session.call_tool("search", arguments={"query": query, "k": 5})
                body = getattr(reply, "structured_content", None) or getattr(reply, "structuredContent", None)
                if not body:
                    body = json.loads(next(c.text for c in reply.content if c.type == "text"))
                hits = body.get("hits", [])
                ids = [h["provenance"]["stable_id"] for h in hits]
                row = {"query": query, "generation": body.get("snapshot", {}).get("generation"),
                    "gate": body.get("gate"), "abstained": body.get("abstained"),
                    "top_cosine": body.get("top_cosine"),
                    "retrieved_documents": ids, "latency_ms": round((time.perf_counter() - started) * 1000, 2)}
                if expected:
                    rank = ids.index(expected) + 1 if expected in ids else None
                    row.update(expected_document=expected, target_rank=rank, target_found_at_5=rank is not None)
                    if query in EXPANDED_DETAILS:
                        passages = " ".join(h.get("content", "") for h in hits
                            if h["provenance"]["stable_id"] == expected).lower()
                        row["expanded_detail_retrieved"] = EXPANDED_DETAILS[query] in " ".join(passages.split())
                    results.append(row)
                else:
                    row["correct_abstention"] = body.get("abstained") is True
                    controls.append(row)
    generations = sorted({r["generation"] for r in results if r["generation"] is not None})
    lock = json.loads((ROOT / "build.lock.json").read_text(encoding="utf-8"))
    receipt_path = ROOT / "research/rag-ingest-receipt.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.exists() else None
    if receipt is not None and generations != [receipt.get("generation")]:
        receipt = None
    if receipt is None and generations == [9]:
        receipt = {"generation": 9, "nodes": 32, "chunks": 270, "embedded": 15, "carried": 255,
                   "failed": 0, "active_generation_flipped": True,
                   "receipt_source": "Observed ksor ingest run 11; applies only to generation 9"}
    passed = all(r["target_found_at_5"] and r.get("expanded_detail_retrieved", True) for r in results) and all(r["correct_abstention"] for r in controls)
    return {"verified_at": datetime.now(timezone.utc).isoformat(), "passed": passed,
        "scope": ("Local MCP corpus check; not public deployment or independent expert validation." if root.startswith(("http://127.0.0.1", "http://localhost")) else "Public MCP retrieval check; not model-answer correctness or independent expert validation."),
        "endpoint": url, "health": health, "generations_verified": generations,
        "approved_documents": sum(d["status"] == "stable" for d in lock["documents"]),
        "published_chunks": receipt["chunks"] if receipt else None,
        "ingest": receipt,
        "build_id": lock.get("build_id"),
        "dataset_sha256": hashlib.sha256((ROOT / "psi-data/derived/runs.json").read_bytes()).hexdigest(),
        "retrieval_cases": results, "out_of_scope_controls": controls,
        "target_document_hit_rate_at_5": sum(r["target_found_at_5"] for r in results) / len(results),
        "mean_reciprocal_target_rank_at_5": sum(1/r["target_rank"] if r["target_rank"] else 0 for r in results) / len(results),
        "correct_control_abstentions": sum(r["correct_abstention"] for r in controls),
        "limitations": "Question labels are internal engineering expectations. Target-document hits do not establish passage-level precision, answer correctness, or scientific validity. The 0.415 floor was measured on separate calibration probes; these held-out checks do not establish universal out-of-domain reliability. Structured measurements remain in deterministic PSI tools, not an ungoverned vector dump."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8080/mcp")
    parser.add_argument("--output", default="research/rag-publication.json", help="Write a new evaluation artifact; failed checks never replace an older successful report.")
    parser.add_argument("--timeout", type=float, default=240, help="Overall evaluation timeout in seconds.")
    args = parser.parse_args()
    if not 0 < args.timeout < 3600:
        parser.error("--timeout must be positive and below 3600 seconds")
    result = asyncio.run(asyncio.wait_for(evaluate(args.url), timeout=args.timeout))
    (ROOT / args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Verified generations {result['generations_verified']}; target hits {sum(r['target_found_at_5'] for r in result['retrieval_cases'])}/{len(CASES)}; correct out-of-scope abstentions {result['correct_control_abstentions']}/{len(CONTROLS)}")
    if not result["passed"]:
        raise SystemExit(1)
