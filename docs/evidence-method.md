# Evidence method and export dictionary

Method: `atmosphere-overlap-v2`. This is a retrieval method, not a validated
combustion model. Each claim about a test must be checked against its source.

## What the query means

Numeric search distance is distance to a reported interval (or to the nearest
listed value for a discrete multi-value cell), divided by the selected tolerance.
This can identify an interval containing a target; it cannot establish that every
combination inside two marginal intervals was experimentally observed. Full means
all requested axes reported within tolerance, incomplete means at least one missing
and every reported axis within tolerance, and near contains the rest. A record
reporting none of the requested axes sorts after measured neighbors. Categorical
filters remain hard constraints. Missing axes are unknown, never zero.

The default oxygen tolerance is absolute percentage points, pressure is absolute
atm, and flow/thickness/initial droplet diameter use relative fractions. Changing
these windows changes retrieval, not the experiments. A source range is not a
confidence interval. Unknown uncertainty must not be replaced with a made-up error bar.

Mission tables include only `test` and `test-point` records. BRE is shown separately
in the Lunar case study as a subset of gaseous physical geometry with a condensed-fuel
emulation role. The three report examples do not enumerate all BRE tests.

Heatmaps use only finite single values for both axes, individual granularity and
no conflict on either axis. One eligible record occupies one cell. All exclusions
remain available in the Explorer. A pressure/oxygen grid cannot assess the usefulness
of smoke-detection investigations whose atmospheric metadata is absent.

Sorted measurements (`sorted-observations-v1`) retain each eligible individual
record as one observation. No records are pooled on the basis of equal recorded
fields: missing setup or method metadata cannot establish a replicate cohort.
Each row exposes its raw value, unit, source index, setup and record ID. Different
units form separate ordering groups. Legacy `n/min/median/max` fields remain for
compatibility, with `n=1`; they are not material distributions. Conflicts, censored
values, unresolved definitions, ambiguous outcome sweeps and missing units are
excluded. This is not a ranking of material safety or a comparability assessment.

## Research dossier and comparison audit

`/decide/` records a research question verbatim and applies only the explicit
controls. Measurement focus changes cited-outcome availability counts, not the
condition query. Select investigations to preserve a shortlist and deterministic
source-check actions. Missing metadata, outside-window observations and BRE
emulation retain their distinct meanings. Indexed observations are not necessarily
independent experimental replicates.

The `fire-safety-decision` schema version 2 wraps the unchanged evidence payload.
`dossier` contains the question, focused measurement, selected investigations,
record IDs, selection warnings and reason-coded next steps. `sensitivity` records
current, halved-pressure-tolerance and doubled-oxygen-tolerance retrieval windows
when those axes are requested. These are availability checks, not safety margins
or changes to the experiments. Each investigation/geometry remains separate.
URL state restores the question, focus, filters and shortlist.

`comparison-audit-v1` adds shared recorded facts, setup differences, unknowns,
retained conflicts, source-indexed outcomes and next steps to the existing strict
comparability assessment. The real SAFFIRE VI-3 / VI-4 outlet-temperature example
supports source inspection while still abstaining from a condition-matched claim.
It does not subtract outcomes, attribute a causal effect or fill missing methods.

The underlying `comparability-v2` assessment reads instrument/method metadata
from the selected outcome when available. Each field must retain a valid run-local
source index and a quote present in that source. Invalid outcome metadata remains
unknown rather than falling back to a campaign-wide claim. FLEX burning-rate
constants have a source-defined HiBMs imaging and linear-fit method; this does not
supply a method for extinction diameters. SAME-R channels identify instruments
and published processing, while calibration methods remain unknown.

`observation_relationship` preserves source test labels, material, description,
derived identifier groups and explicit aging descriptions for SAME-R. Identifier
collisions across materials remain ungrouped. Independence is always unknown;
neither a suffix nor a repeated identifier establishes a replicate or shared
specimen. No rows are merged. `npm run evaluate:research` verifies three bounded
engineering scenarios and writes a researcher-review packet with blank answers
and no approval. It is not independent scientific validation.

PSI chat turns bind lookup conditions to a bounded deterministic interpretation
of the current user message. Unsupported or ambiguous conditions are refused with
an Explorer link. The model's numerical prose is withheld at the stream/persistence
boundary; measurements and corrections appear in code-owned widgets. Narrative
document replies remain a separate, source-cited path, not a universal correctness
guarantee. Context-dependent follow-ups may require restating explicit conditions.

## JSON download

| Field | Meaning |
| --- | --- |
| `schema_version`, `method_version` | Export structure and retrieval semantics |
| `dataset.generated_at` | Ingest timestamp, not date of experiment |
| `dataset.sha256` | SHA-256 of the complete generated `runs.json` bytes used by the site |
| `query` | Applied numeric and categorical filters |
| `tolerances` | Effective windows including defaults, in canonical units |
| `scope`, `excluded_investigation` | Granularity and investigation exclusions |
| `counts` | Full, incomplete and remaining counts in selected scope |
| `investigations` | Investigation identities and citation metadata |
| `records[].tier`, `axes` | Classification and per-axis distance/missing state |
| `records[].run.id` | Stable identifier; never an implicit ordinal |
| `run.granularity` | Test, test-point, day, summary or planned envelope |
| `run.conditions` | Canonical measures/categories with original cell text and flags |
| `measure.min/max/values` | Reported bounds/discrete values, not estimated uncertainty |
| `run.outcomes[].source` | Zero-based index into that run's `sources` array |
| `run.sources` | PSI file/row or report/table/doc/URL references where available |
| `run.conflicts` | Both source values retained, neither silently preferred |
| `run.notes` | Limitations, preliminary results and interpretation notes |

The download includes ALL remaining records inside the selected categorical scope,
not merely the nearest records displayed on screen. It does not silently truncate
provenance. Original full table rows can be inspected through per-run details;
condition and outcome raw cells are included in the download itself.

For reproducibility, retain the JSON, source files and code revision together. The
hash identifies bytes; it is not a signature, endorsement or accuracy certificate.
The URL stores query and tolerances but follows the current deployed dataset.

## Use before model fitting

Select a compatible investigation/setup and endpoint. Separate summaries from
individual tests; inspect non-ignition, censoring and duplicate observations.
Retain source disagreements and missingness, and establish independent validation
and uncertainty treatment before fitting. The export deliberately makes no claim
that heterogeneous records are directly suitable for pooled predictive modeling.

## Literature and scientific audit

The owner-approved LUCI and DAFT documents are publication observations, not
new PSI tests. FLEX-team rates attach to planned fuel envelopes by exact fuel
identity, retaining the literature burn ID and its source. They are excluded
from individual-test populations and rankings.

The SAFFIRE VI-3 smoke observation retains the report-selected concentration
threshold in `outcomes[].at.selected_mass_concentration_mg_m3`. Its timeline
value is not a measured ignition-to-alarm delay. A conditional energy-consistency
flag requests clarification of method and integration interval while preserving
the published numbers. The affected heat-release/time bundle carries
`source_definition_unresolved`: charts, rankings, quantitative comparisons and
numeric tool summaries exclude it; source details and exports retain it.

Reproduce the internal audit with the backend Python environment:

```powershell
.\system\chatkit-server\.venv\Scripts\python.exe scripts/evaluate-scientific-evidence.py
.\system\chatkit-server\.venv\Scripts\python.exe scripts/evaluate-rag-publication.py
```

The second command defaults to the local MCP door. To check the published corpus,
pass `--url https://flamefreefall-sor.vercel.app/mcp --timeout 240`. Results are
recorded under `research/`. The refreshed public generation-10 check found all
13 target documents, all four checked expanded-detail phrases and all eight
expected control abstentions. Retrieval hit rate on internal source-anchored
questions is an engineering check, not an expert relevance benchmark. The
retrieval floor is 0.415, measured on a separate 16/12 calibration set. These
measurements do not establish universal abstention or model-answer correctness.
`npm run verify:release` separately checks public routes and dataset identity;
neither command publishes local code.
