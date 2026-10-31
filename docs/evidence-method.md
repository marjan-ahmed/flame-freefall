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

Rankings summarize scalar, non-conflicting results among full matches, grouped by
material, investigation and recorded setup. Missing setup fields do not establish
compatibility. Sorted measurements are not a universal ranking of material safety;
users must inspect apparatus, endpoint definition, flow and gravity before comparing.

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

The second command requires the embedding service and local MCP door. Results
are recorded under `research/`. Retrieval hit rate on internal source-anchored
questions is an engineering check, not an expert relevance benchmark. The
retrieval floor is 0.415, measured on a separate 16/12 calibration set. The
held-out checks retrieved all nine target documents and abstained on all eight
out-of-scope controls. These measurements do not establish universal abstention
or model-answer correctness.
