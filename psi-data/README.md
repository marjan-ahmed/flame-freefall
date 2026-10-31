# psi-data — NASA PSI test tables and what is made of them

Raw files downloaded from NASA's Physical Sciences Informatics (PSI) system, and
the unified run table generated from them. This folder is **not** part of the
governed record (`knowledge/`); it is source data plus a build artifact.

| Path | What it is | Edit by hand? |
| --- | --- | --- |
| `raw/` | Files exactly as downloaded from PSI | never |
| `derived/runs.json` | One record per test (or daily summary / planned envelope), every value with its raw cell and source line | never — `uv run psi-ingest` |
| `derived/investigations.json` | Per-investigation identity, citation (read from `knowledge/` frontmatter), coverage | never |
| `derived/ingest-report.json` | Rows read / emitted / skipped (and why) per file; report-table joins; files not ingested | never |
| `derived/report-extractions/*.md` | The `reports/` PDFs converted to Markdown (Nutrient `pdf-to-markdown`): extraction ground truth | never, regenerate with the converter |
| `extracted/report-outcomes.csv` | Per-test values pulled from converted report text: value, table, page, and the verbatim cell | never — `uv run psi-extract`; ingest refuses any row whose verbatim text is not in its source |
| `query-fixtures.json` | Golden query cases both query implementations must reproduce | never — `system/chatkit-server/tests/gen_query_fixtures.py` |

Regenerate: `cd system/psi-ingest && uv run psi-ingest`.

## Raw files

| File | PSI dataset | Ingested as |
| --- | --- | --- |
| `csvs/PSI-25_…BASS-II.csv` | PSI-25 | BASS-II tests (129) |
| `csvs/PSI-26_…BASS.csv` | PSI-26 | BASS tests (121; one "SOOT Cleaning" row skipped) |
| `csvs/PSI-98/99/100_…SAFFIRE-1/2/3.csv` | PSI-98/99/100 | Saffire burn samples (flow-visualization rows skipped; SAFFIRE-2 table notes kept) |
| `csvs/PSI-69_…FLEX.csv` | PSI-69 | FLEX droplet tests (274) |
| `csvs/PSI-68_…Flex2.csv` | PSI-68 | FLEX-2 planned condition envelopes, per fuel (not tests); approved cool-flame literature supplement attaches by fuel identity |
| `csvs/PSI-39_…CFI.csv` + `matrices/CFI_DataSummary_Spreadsheet_Jan2021.xlsx` (sheet DATA) | PSI-39 | CFI droplet tests, outcomes joined on Flex Number (8 duplicate rows skipped) |
| `csvs/PSI-159_…CFI-G_*.csv` | PSI-159 | CFI-G normal and inverse gaseous flames (861 blank rows skipped) |
| `csvs/PSI-10_…Flame Design_*.csv` | PSI-10 | ACME Flame Design normal and inverse flames |
| `csvs/PSI-20/21/22/23_…ACME *.csv` | PSI-20–23 | ACME BRE, CLD, E-FIELD, s-Flame — daily summaries |
| `csvs/19304A1_mfcSetpoints.csv` | PSI-23 | attached to s-Flame day 19304 as an auxiliary time series |
| `csvs/PSI-107_…Spice.csv` | PSI-107 | SPICE test points (34 exact duplicates skipped) |
| `csvs/PSI-106_…Slice.csv` | PSI-106 | SLICE daily summaries |
| `csvs/PSI-101/102_…SAME(-R).csv` | PSI-101/102 | SAME / SAME-R smoke tests |
| `matrices/BASS Test Matrix 050213.xlsx` | — | **never read, and gitignored: its first row contains account credentials.** |
| `reports/BASS-II Summary Report.pdf` (via `investigation_reports/_converted/TM-20210011385.md`) | — | Appendix A, Tables A.1–A.6: flow direction + observation for all 126 BASS-II tests. Numeric columns are skipped: their headers did not survive conversion |
| `reports/SPICE Final Report…pdf` | — | Table 1: per-fuel smoke-point length ranges, nozzle and air-velocity ranges, count of smoke points (5 summary records, not tests) |
| `reports/SAMER_Final…pdf` | — | Table 2: sample temperature and TEM particle count (aged / unaged) for 7 SAME-R tests. Diameter columns skipped (garbled headers) |
| `summaries/Combined SAMER Results 06 02 14.xlsx` | PSI-101 | `Reduced data sheet`: source-processed DustTrak A/B mass concentrations and aerosol diameters joined to existing SAME-R records by exact test number and material. `Reduced Data with ISS Det`: the same rows plus the ISS and STS smoke-detector analog signals (cached instrument readings; smoke deflects the ISS signal positive and the STS signal negative). Cached values and formulas retained; nonpositive diagnostics and unmatched identities excluded, with reasons |
| other `matrices/`, `summaries/`, `reports/` | — | not ingested; reasons listed in `derived/ingest-report.json` → `not_ingested` (e.g. the SAFFIRE MergeResult workbooks are camera-image downlink logs, not combustion data) |

## Normalization rules (the short version)

- Every normalized value keeps the cell it came from (`raw`) and flags anything
  interpreted: `approx`, `range`, `multi`, `converted`, `drifted_during_test`, …
- A cell that can't be read with confidence becomes `null` + `unparsed` /
  `suspect_value`, never a guess (e.g. `037 mm`, `3400%`, `#DIV/0!`).
- BASS-II flow appears only as control-panel "Air/Fan display" readings. Those are
  kept as settings and never converted to cm/s. Velocities come only from the
  report tables that state them.
- Inverse-flame O₂ is the burner stream's O₂ (`oxidizer_stream_o2_pct`), never
  ambient `o2_pct`.
- Report tables from `knowledge/` are joined per test. A matching value confirms
  the PSI value; a differing one is recorded as a conflict with both values, and
  neither is chosen.
- SAME-R workbook diagnostics are source-processed cached values, not newly
  computed or independently measured results. Each value retains its sheet,
  row, cached cell and formula. A join requires the test number **and** material;
  unmatched identities and nonpositive diagnostics with ambiguous instrument
  availability are excluded and accounted for in the ingest report. No test
  number, material or zero-reading interpretation is silently repaired.
- `derived/ingest-report.json` includes generated completeness counts by
  geometry class, with separate counts for numeric and source-processed
  outcomes. These count data availability, not scientific accuracy or safety.

## Comparisons, uncertainty and literature

Explorer comparisons audit geometry, individual-record status, exact fuel,
recorded atmosphere/flow, specimen and duct dimensions, apparatus, confinement,
instrument, method, composition, outcome units and per-outcome conditions.
Unknown or conflicted required metadata blocks a condition-matched claim.
An intentionally varied axis does not waive missing values or unknown units.
The Python and TypeScript comparison engines share generated adversarial cases
in `query-fixtures.json`.

`Measure.uncertainty` retains explicitly reported plus/minus values separately
from ranges, swept conditions and source disagreements. `detection_limit`
retains a reported censoring operator and bound, without creating a measured
point. A bound does not by itself establish an instrument detection limit.
Charts show central values and reported intervals; they disclose that they do
not draw measurement-uncertainty error bars. Details and exports retain the
uncertainty metadata. No confidence level is inferred.

`literature.yaml` holds owner-approved publication observations and campaign
summaries with source quotes and saved extraction paths. LUCI and DAFT live in
`knowledge/literature/`; neither contributes test records to `runs.json`.
They are published through the governed narrative retrieval corpus.

The approved FLEX-2 cool-flame supplement has 13 rates for literature-identified
burns attached to two planned fuel envelopes. These do not become individual
PSI tests or replace the envelopes' swept conditions. Ingest excludes any future
draft supplement by default; programmatic draft review uses
`run(write=False, include_review=True)` and cannot write serving files.

SAFFIRE Table 2 supplies maximum far-field-device/nearest-location temperature
and CO₂ partial-pressure increase for five existing records. Complete-row checks
against the saved extraction preserve identity, empty cells and column positions.
Figure 7 supplies one VI-3 smoke-threshold crossing at a report-selected 1 mg/m³
threshold and reported time of 981 s; this is not a known ignition-to-alarm delay,
universal alarm setting or instrument detection limit. A conditional energy
consistency policy quarantines the VI-2 heat-release/time bundle from numeric
analysis while preserving its reported values for source inspection. Unaffected
temperature, gas and smoke measurements remain available.

The internal scientific evaluation is generated with
`python scripts/evaluate-scientific-evidence.py` using the backend environment.
It writes `research/scientific-evaluation.md` and `.json`; it is neither a NASA
review nor a validation of pooled predictive models or material safety.

Campaign apparatus metadata is inherited only from a verified source quote
(`psi_ingest/apparatus.py`), with its own citation and source index. Duct
dimensions are distinct from specimen dimensions. This adds no pressure,
temperature, test-specific instrument or measurement-method assumptions.

Reproduce local validation from the repository root (PowerShell):

```powershell
.\system\psi-ingest\.venv\Scripts\python.exe system/psi-ingest/tests/audit_source_agreement.py
.\system\chatkit-server\.venv\Scripts\python.exe system/chatkit-server/tests/benchmark_evidence.py
npm run build
# In another terminal, set PORT=3100 in your shell and run npm run preview.
python scripts/verify-evidence-browser.py --url http://localhost:3100
```

These write bounded reports under `research/`: cached-cell transfer agreement,
offline query regression expectations and warm latency, and a Chromium static
export comparison/source/download journey at desktop and mobile widths. They
do not measure predictive accuracy, expert relevance, or deployed performance.
