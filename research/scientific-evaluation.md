# Internal scientific evaluation

Codex internal source-based scientific evaluation; not NASA review or endorsement

Dataset SHA-256: `3286c2da58bd7c85704551d1021f8bd9c9f1564ed368fa236725b4c01fd3fcb2`. Evaluated 2026-10-31T12:55:20.491286+00:00.

## Assessment

The index supports source-traceable descriptive research. It does not establish a pooled material safety ranking, a validated predictive model, or lunar fire-safety certification.

The dataset contains 1,951 records, 1,838 individual test/test-point records, and 1,035 records with outcomes. Literature burns attached to planned fuel envelopes remain envelopes.

## Within-burn cool-flame comparison

These six paired values were selected by the publication, not sampled as independent replicates. No significance test, confidence interval or general fuel ranking is justified. Ratios below are derived, not source-reported measurements.

| Literature burn | Hot K (mm²/s) | Cool K (mm²/s) | Derived cool/hot | Caveat |
| --- | ---: | ---: | ---: | --- |
| R298 | 0.48 | 0.38 | 0.791667 | Selected literature burn |
| R694 | 0.54 | 0.43 | 0.796296 | Selected literature burn |
| R698 | 0.63 | 0.53 | 0.84127 | Selected literature burn |
| R377 | 0.41 | 0.33 | 0.804878 | Selected literature burn |
| R379 | 0.31 | 0.27 | 0.870968 | Selected literature burn |
| R383 | 0.29 | 0.25 | 0.862069 | Printed atmosphere sums beyond 100% |

Source: [Nayagam et al., 2014](https://ntrs.nasa.gov/citations/20140006750). The source's R383 atmosphere is preserved, not repaired.

## Conditional energy consistency

If a peak heat-release rate and an integrated energy share a measurement method and integration interval, energy cannot exceed peak power multiplied by duration. This is a diagnostic condition, not proof that those assumptions hold for the table.

| Record | Total imaging energy (kJ) | Peak × duration (kJ) | Needs source clarification |
| --- | ---: | ---: | --- |
| saffire-iv-vi:VI-2 | 580.0 | 360.304 | True |
| saffire-iv-vi:VI-3 | 1280.0 | 2402.4 | False |
| saffire-iv-vi:VI-4 | 830.0 | 1808.4 | False |

Source: [SAFFIRE preliminary results, Table 2](https://ntrs.nasa.gov/citations/20240002981). Do not silently correct a published value. Method labels, integration periods and possible source errors need clarification before model fitting.

The governed SAFFIRE prose labels the SIBAL cross-check VI-3, while the original report and Table 1 identify that SIBAL sample as VI-2. Structured records use the table identities. This narrative discrepancy needs governed correction and must not support the VI-3 PMMA result.

## Detection and partial-gravity interpretation

Camera non-detection applies to the imagers used in the FLEX study; it is not a demonstrated performance criterion for every crew camera.

The SAFFIRE VI-3 threshold-crossing observation uses a report-selected concentration threshold and the reported timeline. It is not a demonstrated ignition-to-alarm delay or universal detector response specification. Remote temperature maxima and source-outlet maxima are not necessarily simultaneous; their difference is not an instantaneous thermal gradient.

DAFT reports bounds on campaign-average background aerosols, not fire-smoke detection limits. SAME-R cached diagnostics measure transfer agreement, not calibration. LUCI uses a rotating platform, time-varying oxygen and fitted flame tracking; Coriolis effects and changing acceleration prevent treating its results as a stationary lunar habitat certification.

## Comparability and missingness

The production comparison audit evaluated 10 pairs among the five SAFFIRE records. 0 support a condition-matched comparison under the recorded metadata. A common investigation name is insufficient.

Per-geometry missingness, uncertainty counts, full comparison diagnoses and source pointers are in the companion JSON. Missing metadata and uncertainty must remain unknown.

## Required scientific work

The affected SAFFIRE heat-release/time bundle is quarantined from quantitative analysis while its reported values are retained for source inspection. Source clarification is still needed to admit that bundle to analysis. Obtain independently identified as-run conditions and calibration/uncertainty; establish replicate and study identities; and evaluate any predictive model on held-out studies. This internal review does not substitute for independent subject-matter review or NASA materials qualification.
