# Approved evidence, internal scientific evaluation and vector publication

This report supersedes earlier session snapshots. It records completed work,
measured checks and remaining limits; it is not a NASA assessment.

Release handoff: the owner subsequently requested commit and push. The source
changes, generated artifacts and validation reports are included in that handoff.
Final release checks passed 201 backend tests (4 existing expected failures),
63 ingest tests (2 existing expected failures), and 45 frontend tests, plus the
record checker. Statements below about uncommitted or undeployed work describe
their original session snapshot; Git history and deployment workflow results
record the later release status.

## Follow-up: analysis quarantine and retrieval calibration

The user requested that the two reported limitations be addressed. The affected
VI-2 heat-release/time bundle is now retained as source evidence but excluded
from quantitative charts, rankings, comparisons and numeric tool summaries.
This prevents uncertain source definitions from entering analysis without
inventing corrected measurements. Unaffected temperature, gas and detector
outcomes remain available. Source uncertainty itself is not claimed to vanish.

The retrieval floor is now 0.415 (predicate digest `8bfb07d0e6f5`), measured on
16 relevant and 12 out-of-scope calibration probes. Their score ranges separated
with a reported margin of 0.016. The calibrated local MCP door retained all nine
expected documents on separate evaluation queries and correctly abstained with
no passages on all eight out-of-scope controls. Calibration inputs and hashes
are recorded in `retrieval-calibration.json`; evaluation results are recorded
in `rag-publication.json`. These are bounded internal checks, not a guarantee
for every possible unsupported question.

Follow-up validation: the full ingest suite passed 63 tests with 2 expected
failures; the full backend suite passed 200 with 4 expected failures, followed
by 19 passing query tests including the additional ranking-quarantine guard;
all 45 frontend tests passed. The production build and record checker passed.
The sections below preserve the initial publication's history.

## Approval and evidence

The owner explicitly approved the existing FLEX-2 cool-flame, LUCI and DAFT
literature documents in conversation. Approval is recorded as `human:you`, the
actor authorized by `.ksor/governance.yaml`, at 2026-10-31T11:55:40Z. All 23
documents are stable and have summary attachments. Approval does not assert
independent human source verification.

The approved FLEX-2 document now supplies 13 source-guarded rates on two existing
fuel envelopes. Fuel identity is the join; literature burn identifiers are not
PSI row identities. No individual-test records were invented. Hot/cool ordering,
diameter, pressure, extraction fragments and unique fuel joins are checked.

Added an identifiable SAFFIRE VI-3 observation from Figure 7 and its accompanying
text: the reported threshold-crossing time at the report-selected concentration
threshold. Its original timeline and threshold remain explicit. It is not a
known ignition-to-alarm delay, instrument detection limit or universal alarm
setting. General outcome-specific conditions now render in chat and Explorer;
they no longer assume every condition is a flow velocity.

The run index remains 1,951 records, including 1,838 individual tests/test points.
There are 1,035 records with outcomes; LUCI and DAFT remain separately governed
publication observations. Their source documents are retrievable without
inflating the run count.

## Internal scientific evaluation

See [the generated assessment](scientific-evaluation.md) and
[machine-readable diagnoses](scientific-evaluation.json). The reproducible
script examines six within-burn hot/cool pairs, ten SAFFIRE comparisons,
uncertainty availability, missing conditions and conditional energy consistency.

The selected cool-flame rates are lower than their paired hot-flame rates. This
does not establish a general material ranking or independent replicate result.
R383 retains its inconsistent printed atmospheric composition.

VI-2 requires clarification if its listed peak heat-release rate, duration and
integrated energy are assumed to use identical methods and intervals. The
conditional inconsistency is flagged in the served record; all published values
are preserved. No corrected measurement or safety margin was invented.

The dataset is useful for bounded descriptive research, with inadequate evidence
for pooled material-safety rankings, validated predictive performance or lunar
habitat certification. Camera non-detection findings apply to the study's
instruments; they are not a universal test of all crew cameras. This review is
internal and source-based, not independent peer review or NASA endorsement.

## Vector publication and retrieval evaluation

The configured Neon database `flame_freefall_sentence_transformers` now serves
generation 9: 32 nodes, 23 documents and 270 chunks. Ingest carried 255 chunks,
embedded 15 new chunks and recorded zero embedding failures before flipping the
active generation. Fourteen navigation-like chunks are readable but excluded
from semantic search. Model: `sentence-transformers/all-MiniLM-L6-v2`, native
384 dimensions padded to the configured 1536-dimensional schema.

The embedding service loaded the existing cached model in offline mode after
the first ingest timed out. No embedding-model migration or destructive database
reset was performed. The health check and MCP search responses confirm generation
9. The project connector was unavailable, so verification used the configured
local MCP door against the Neon store.

See [the publication receipt and retrieval cases](rag-publication.json).
All nine internally labeled source-anchored questions retrieved the expected
document in the top five. Both unrelated controls returned passages rather than
abstaining: the retrieval floor remains uncalibrated. Target-document hit rate
does not establish passage precision, model-answer correctness or out-of-domain
reliability. No threshold was tuned on the evaluation set to make it pass.

## Web and documentation updates

The landing page shows generated current evidence counts, source links and the
three approved literature documents. The Lunar case study links to separate LUCI
observations. Explorer and chat display the new threshold condition explicitly.
README, instance scope, AGENTS.md, the data README and evidence-method dictionary
now reflect approval, literature granularity and evaluation limits. Older dated
research notes are marked as historical rather than rewritten as current results.

## Verification

- Ingest: 62 passed, 2 existing expected failures.
- Backend: 199 passed, 4 existing expected failures.
- Frontend: 42 passed; type check and static production build passed.
- Record format checker passed; 23 documents admitted by the governed build.
- Source transfer audit: 532 cached workbook cells, zero mismatches.
- Offline query benchmark: six cases; 4,004 outcome source indices checked.
- Chromium at 1280 px and 390 px: comparison controls, source cells, URL and
  descriptor citations, SAFFIRE measurements and thresholds in exports,
  literature machine-readable pages and landing links, matching dataset hash,
  no page errors or horizontal viewport overflow.

The vector database has been updated. Web changes are built and browser-tested
locally; no commit, push or public web deployment was performed by this work.
