# Roadmap continuation: verified SAFFIRE outcomes and draft admission

> Historical session snapshot. For the subsequent owner approvals, new source evidence, scientific audit and vector publication, see [current completion report](2026-10-31-approved-evidence-and-publication.md).

This local implementation report supersedes the earlier session's statements
that SAFFIRE's additional Table 2 values require editing the stable document,
and that no FLEX-2 literature rates are available. It is not a governed finding
or a claim of scientific validation. Nothing was committed, pushed or deployed.

## Delivered

- Exposed ten source-reported values already present in the stable SAFFIRE
  document: maximum far-field-device/nearest-location temperature and CO₂
  partial-pressure increase for IV-1, V-2, VI-2, VI-3 and VI-4. No records,
  conditions, approval stamps or stable document bodies were changed.
- Added complete-row agreement checks against the saved HTML extraction of
  Table 2, retaining empty columns, identity and material. Changed values,
  substituted identities and swapped numeric columns fail ingest. Both
  Explorer and chat have readable labels for the new quantities.
- Closed the draft-admission defect introduced during the FLEX-2 work. The
  default ingest excludes the cool-flame supplement until its document is
  stable; the citation gate remains unchanged. Local programmatic review uses
  `run(write=False, include_review=True)`. Review mode with writes enabled
  raises before doing any work, so it cannot overwrite serving files.
- Prepared `flex2-review.json`: thirteen rates on two planned fuel envelopes,
  carrying literature burn identifiers and provenance. The rates do not become
  individual PSI tests. The guards check extraction fragments, stage-specific
  rate order, diameter, pressure, fuel identity and unique envelope joins.
- Regenerated serving files and fixtures; refreshed source-audit and offline
  benchmark reports. Extended browser validation to the new SAFFIRE values,
  their units and source indices in exports.

## Current serving dataset

| Metric | Count |
| --- | ---: |
| Indexed records | 1,951 |
| Records with outcomes | 1,033 |
| Individual records with numeric outcomes | 922 |
| Numeric outcome entries across all granularities | 2,703 |
| Outcome source indices checked | 3,990 |
| Source-processed workbook cells audited | 532 |
| Workbook transfer mismatches | 0 |
| Draft citations in serving data | 0 |

These are availability, transfer and integrity measures. They do not establish
calibration, experiment independence, predictive accuracy or fire safety.

## Verification

- Full ingest suite: 57 passed, 2 existing expected failures. After adding the
  final stage-order regression, the FLEX-2 suite separately passed all 10 tests.
- Backend: 198 passed, 4 existing expected failures.
- TypeScript parity/display/export suite: 41 passed; TypeScript type check passed.
- Record format checker and production static export passed.
- Chromium passed at 1280 px and 390 px, including comparison controls,
  descriptor-only and URL citations, source cells, new SAFFIRE values/units in
  evidence exports, matching dataset fingerprints and no viewport overflow or
  page errors. Local navigation-to-ready timings were about 3.25 s and 1.53 s
  respectively; these are single observations, not latency percentiles.
- Browser results are recorded in `browser-validation.json`; source transfer
  results in `source-agreement.json`; deterministic retrieval and warm local
  latency in `evidence-benchmark.json`. These do not cover a deployed host,
  live chatbot/MCP latency or expert-reviewed retrieval relevance.

## Remaining

- Owner approval of FLEX-2, LUCI and DAFT drafts before publication. Review
  snapshots are not approval, and the ingestion gate must remain in place.
- Further BASS/BASS-II conditions need identifiable as-run source evidence;
  source material without test identifiers cannot repair missing pressure.
- Expert-reviewed questions and scientific review, with held-out studies where
  modeling is attempted. Current query cases are engineering regressions.
- Additional source acquisition where usable measurements and unambiguous
  identities exist. No simulated lunar-gravity observations are being relabeled
  as PSI tests, and no safety threshold is derived from the new measurements.
