# Flame in Freefall: data accuracy, expansion, and competitor research

> Historical session snapshot. For the subsequent owner approvals, new source evidence, scientific audit and vector publication, see [current completion report](2026-10-31-approved-evidence-and-publication.md).

Research date: 2026-10-31. This is an implementation research brief, not a governed scientific finding or an approved knowledge document. No production data or knowledge documents were changed.

## Scope and evidence

The local `challenge-details.md` asks for a dashboard that summarizes, ranks, and interprets combustion investigations for spacecraft, stations, habitats, and rovers. Its audience includes faculty, students, aerospace researchers, and engineers. Prevention, detection, and suppression all matter. The live challenge page could not be fetched in this research session, so challenge-specific requirements below are based on the supplied local copy.

Repository counts were computed directly from `psi-data/derived/runs.json` and checked against `ingest-report.json` and `investigations.json`. Both the ingest output and the backend copy of `runs.json` have SHA-256 `af748120545cfe5103d602128cb59a5b55b6722b45c3f494a96a63b39eab4406`.

Competitor claims below come from public READMEs and, where specified, inspected source code. These are not independent assessments of deployed scientific accuracy, user adoption, competition standings, or NASA endorsement.

## Baseline before implementation

| Metric | Baseline value | Interpretation |
| --- | ---: | --- |
| Investigation registry entries | 19 | Includes a combined SAFFIRE IV–VI entry; not a universal count of independent studies |
| Indexed records | 1,951 | All granularities combined |
| Individual test and test-point records | 1,838 | Not necessarily independent physical experiments |
| Daily, summary, and planned-envelope records | 113 | 100 daily records, 5 summaries, 8 envelopes |
| Records with any outcome field | 932 | Includes qualitative text and status fields; not 932 independently verified measurements |
| Records with a numeric outcome minimum | 914 | A parsing/availability measure, not an accuracy score |
| Individual records with a numeric outcome minimum | 821 | Useful starting denominator for outcome-focused enrichment |
| Records with a numeric spread-rate outcome | 22 | Includes multiple reported values within some records |
| Solid-fuel records with usable pressure | 5 of 268 | Limits atmosphere-based comparisons; missing pressure must remain unknown |
| Smoke/aerosol records with numeric outcomes | 11 of 117 | Detection diagnostics are a promising enrichment area |

Selected investigation gaps: FLEX-2 currently contributes 8 planned envelopes and no outcomes; ACME Flame Design contributes 327 condition records and no outcomes; SPICE contributes 440 records, with outcomes on 5 report-summary records. These are evidence-access gaps in this index, not claims that the underlying experiments produced no measurements.

## Accuracy work before expansion

### 1. Distinguish pure fuels from blends

The current production Python query for `fuel_family=n-dodecane` returns 79 matches: 22 pure-fuel records and 57 `n-dodecane/iso-dodecane` blend records. Reproduced directly with `psi_query.query`.

Add explicit exact-fuel and family/blend search semantics. Pure-fuel filters should not silently include mixtures. Change both Python and TypeScript query implementations and regenerate parity fixtures. Preserve a separate, intentional way to search the broader fuel family.

### 2. Make unavailable quantities explicit

`psi_widgets.results_data` currently substitutes the most common available quantity when a requested quantity is unavailable. `results_summary` does not identify the original request or substitution. The existing QA test still produces the expected failure.

Return an explicit unavailable result with available alternatives, or carry the requested and displayed quantities through both payload and chart labels. A request for spread rate must not be presented as if a burn-time chart answered it.

### 3. Separate the provenance of conditions and outcomes

Outcomes already carry source indices. Extend that precision to normalized conditions: source file/table/row or page, raw value, units, transformation, and whether a condition is test-specific or inherited from a documented apparatus setting. Do not assign generic ISS pressure to every run merely because the experiment flew on the ISS.

### 4. Represent experimental uncertainty separately

The current `Measure` supports values, reported intervals, lists, and interpretation flags. Add separate fields for source-reported measurement uncertainty, detection limits/censoring, replicate identity, and processing method where sources supply them. A range swept during a test is not a confidence interval. Unreported uncertainty should remain unreported.

### 5. Reconcile QA expectations with current scientific policy

Three selected code-quality tests remain expected failures: pure-fuel matching, unavailable-quantity disclosure, and conflict handling in rankings. The ranking test expects a widened result interval, while the inspected production implementation already excludes conflicted runs. Review whether that test reflects the intended policy before calling it an unfixed production defect. Do not change defensible exclusion rules merely to satisfy an outdated assertion.

The targeted test command was `system/chatkit-server/.venv/Scripts/python.exe -m pytest system/chatkit-server/tests/test_qa_codequality.py -k 'pure_fuel_filter or requested_quantity or conflicting_outcomes' -rx -q`, with a dummy API key. It returned 3 expected failures and 25 deselected tests; no live model was called.

## Highest-value data acquisition

| Priority | Source/workstream | Contribution | Admission rule |
| --- | --- | --- | --- |
| 1 | Existing BASS/BASS-II reports and later SAFFIRE publications | Solid-fuel spread, extinction, dimensions, confinement, and reported atmosphere conditions | Enrich identified runs; retain report/table provenance and preliminary status |
| 2 | `Combined SAMER Results 06 02 14.xlsx` | Smoke diagnostics already present locally but listed as unmapped | Inspect safe workbook structure; map only unambiguous headers and join on verified run identifiers |
| 3 | FLEX-2 experimental outputs | Actual tests and measured outcomes beyond the current planned envelopes | Discover accessible PSI files first; do not turn envelope combinations into fictional tests |
| 4 | DAFT/DAFT-2 | Dust response context for smoke detection | Keep dust, smoke, heated non-burning samples, and combustion distinct |
| 5 | ACME/SPICE/SLICE result files and time series | Outcomes for existing condition-only or daily records | Preserve test/time-series hierarchy and prevent duplicate counting |
| 6 | Published partial-gravity studies, especially LUCI | Directly relevant evidence for lunar research questions | Label simulated partial gravity, apparatus, duration, rotation effects, and publication-only status |

NASA's current [PSI investigation catalog](https://www.nasa.gov/physical-sciences-informatics-psi/psi-investigations-by-research-area/) lists FLEX-2, DAFT, and DAFT-2. This establishes research relevance, not guaranteed availability of every desired raw file.

The local ingest report explicitly identifies the SAME/SAME-R results workbook as not yet mapped. This could improve outcome completeness without increasing the record count at all.

NASA's [Saffire VI preliminary results record](https://ntrs.nasa.gov/citations/20240002981) is a candidate for additional spacecraft-scale evidence. Some SAFFIRE IV–VI material is already ingested, so compare test identifiers and sources before adding anything; a second publication about the same burn is an additional source, not a new experiment.

The [LUCI presentation acquired in November 2025](https://ntrs.nasa.gov/citations/20250010653) describes extended-duration combustion tests in simulated lunar gravity using a rotating sounding rocket and discusses Coriolis effects. Therefore, distinguish absence in the current PSI/index scope from absence across the published literature. Its abstract establishes a promising source; it does not by itself supply a complete verified per-run dataset. This session did not extract its PDF tables.

NASA's [FM2 project page](https://www.nasa.gov/glenn/glenn-expertise-space-exploration/physical-sciences-program/combustion-science/flammability-of-materials-on-the-moon-fm2/) describes the experiment and its objectives. Do not present proposed settings or planned mission outputs as completed lunar measurements without a released results source.

For every acquisition, record a persistent source identifier, retrieval date, checksum, file version, license/access status, and ingestion status. First account for newly discovered files, then extract and verify, then join/deduplicate, then regenerate derived outputs and query fixtures. Never open the credential-bearing BASS planning workbook excluded by the repository contract.

## Comparable tools and direct challenge projects

| Project | Publicly documented scope | Useful lesson | Boundary |
| --- | --- | --- | --- |
| [Mehedi752 / Flame-in-Freefall](https://github.com/Mehedi752/Flame-in-Freefall) | README describes 31 curated records from approximately 25 publications, a deterministic analyst, comparisons, mission scenarios, and an eight-step demo journey | Make the question-to-source-to-comparison-to-export journey easy to demonstrate | Publication-level records are not comparable to this repository's run count. README notes that some values came from abstracts/excerpts |
| [FLARENEXUS / Team Cosmic Nexus](https://github.com/KhalidHasan03/Flame-in-Freefall) | README describes 26 experiment records, comparisons, Flame Lab, Mission Lab, an assistant, and saved work | Saved comparisons, clear scenarios, and approachable visual explanations | README explicitly labels records, risk scores, charts, and assistant answers as synthetic demonstration data |
| [NASA PSI](https://psi.nasa.gov/physci/repo/) and its [catalog](https://www.nasa.gov/physical-sciences-informatics-psi/psi-investigations-by-research-area/) | Authoritative discovery and access point for physical-science investigations and associated resources | Retain authoritative identities, original files, and citations; provide a convenient cross-investigation analysis layer | It is primarily an upstream source and workflow alternative, not a rival whose completeness this prototype has matched |
| [ReSpecTh](https://respecth.hu/) and its [dataset paper](https://www.nature.com/articles/s41597-025-05272-6) | Structured reaction-kinetics, spectroscopy, and thermochemical datasets with experimental metadata and analysis tooling | Portable experimental data and explicit uncertainty belong in the data model | Adjacent combustion infrastructure, not an equivalent spacecraft materials-flammability collection |
| [NIST FDS/Smokeview](https://pages.nist.gov/fds-smv/) | Fire-flow simulation, visualization, documentation, and validation resources | Make experimental datasets usable for independent model validation | A simulator is not measured evidence; applicability to a specific low-gravity problem needs validation |

The inspected Mehedi project [engine](https://github.com/Mehedi752/Flame-in-Freefall/blob/main/lib/engine.ts) uses manually specified evidence weights and additive scenario-risk rules. These are implementation heuristics, not demonstrated calibrated probabilities. Borrow the guided workflow; do not copy the appearance of quantitative safety confidence without validation.

This review establishes relevant public comparisons, not a comprehensive competitor census, benchmark ranking, or official entrant list.

## Research workflow to build

Support one complete journey: choose a mission atmosphere and material; inspect directly relevant tests; see missing conditions and incompatible apparatus; compare eligible outcomes; open each source value; export the exact evidence and limitations.

Comparison should check more than geometry class. Include material composition and dimensions, fuel concentration, ambient versus burner-stream oxygen, pressure, flow direction, confinement, gravity regime, instrument, and measurement method. A common experiment name does not guarantee comparability.

Surface source-reported evidence separately from derived aggregates and interpretation. Keep research relevance and evidence coverage distinct from safety certification or a calibrated probability of ignition. Provide a separate discovery mode for nearby or incomplete evidence, rather than treating it as an eligible ranking population.

## What to measure

Maintain an expert-reviewed question set covering prevention, detection, suppression, incompatible geometries, blends, missing axes, source conflicts, and unsupported mission conditions. Reserve questions and studies for evaluation before tuning retrieval or modeling.

| Goal | Metric |
| --- | --- |
| More useful data | Independently identified test records with relevant outcomes and necessary conditions; completeness per field and investigation |
| Accurate extraction | Audited source-cell agreement, correct units, correct joins, provenance completeness, duplicate rate |
| Better retrieval | Relevant-evidence recall and precision on a reviewed benchmark; correct abstention on unsupported questions |
| Correct answers | Numerical agreement with tools, citation support, and preservation of missing/conflicting evidence |
| Valid models | Evaluation on held-out experiments/studies, reported uncertainty, and checks for out-of-domain inputs |
| Faster interface | Payload size, cold-load time, chart interaction latency, and p50/p95 query time on specified hardware |

Proposed release gates: all displayed numerical values resolve to their contributing sources; known blend and quantity-substitution failures are closed; all regeneration/parity checks pass after ingestion changes; and benchmarks show the effect of each expansion. These are proposed acceptance criteria, not measured achievements or a claim of 100% accuracy.

If the index grows enough to slow the browser, benchmark a query worker, indexed condition lookups, lazy investigation/raw-detail loading, and compact cached data. For narrative retrieval, evaluate lexical-plus-semantic search and reranking against the same held-out questions. More files or a larger embedding model do not automatically improve precision, latency, or model validity.

## Recommended order

1. Fix exact-fuel filtering and unavailable-quantity disclosure; reconcile existing QA markers.
2. Establish the reviewed benchmark and a generated completeness report.
3. Enrich BASS/SAFFIRE conditions/outcomes and map the local smoke diagnostics workbook.
4. Add verified FLEX-2 and DAFT data where accessible; deduplicate overlapping reports.
5. Add published partial-gravity evidence as a clearly separated, apparatus-aware collection.
6. Deliver the complete comparison/source/export journey and measure its correctness and latency.

The defensible product position is a reproducible research workbench in which users can trace and compare evidence for a specific fire-safety question. Increasing meaningful evidence coverage should drive the roadmap, rather than increasing the displayed row count.

## Implementation update

The first implementation closes exact-fuel versus blend filtering and prevents unavailable chart quantities from silently selecting another measurement. Both query implementations support explicit family searches with a trailing `*`; the Explorer exposes those choices separately from exact compositions. Previously expected failures for those two defects are now ordinary passing regression tests.

The safe SAME-R workbook was mapped without adding tests or repairing source identifiers. The join uses both test number and material: this disambiguates the two PSI rows labeled SAME #57. Workbook test #112 has no matching PSI number/material identity and is accounted for as skipped rather than attached to an unrelated test. Only explicitly unit-labeled mass concentrations and diameters are imported. Nonpositive diagnostic cells are excluded because the reduced sheet does not distinguish disabled diagnostics from meaningful zero readings.

| Availability metric | Before | After |
| --- | ---: | ---: |
| Indexed records | 1,951 | 1,951 |
| Records with any outcome | 932 | 1,033 |
| Records with numeric outcomes | 914 | 1,015 |
| Smoke/aerosol records with numeric outcomes | 11 | 112 |

There are 408 additional source-processed values across 108 existing SAME-R records: 90 DustTrak A concentrations, 108 DustTrak B concentrations, 105 arithmetic mean diameters, and 105 diameters of average mass. Cached results, source-sheet rows, formulas, and processing notes are preserved. These are published processed values, not new independent measurements, and no improvement in predictive-model accuracy has been claimed.

The ingest report now generates completeness counts by geometry, shown in an expandable Explorer table. Source-processed records are explicitly a subset of numeric-outcome records. Existing test identities, conditions, dates, granularities, and source-conflict fields are unchanged by the enrichment.

Verification: ingest 35 passed and 2 existing expected failures; backend 192 passed and 5 existing expected failures; site 23 tests passed; TypeScript and the record format checker passed. Chromium verified exact-fuel and broader-family queries, exported populations, processing labels, workbook formulas, completeness counts, and source-bearing smoke exports. Expanded source/completeness views fit at 320, 375, and 768 pixels. Broader source acquisition, expert benchmarking, and external partial-gravity ingestion remain future work; this change does not claim to complete them.
