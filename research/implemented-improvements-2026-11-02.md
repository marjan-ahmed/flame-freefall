# Implemented research workflow and reliability improvements

This is an earlier implementation snapshot. See [the source-method follow-up](source-method-followup-2026-11-02.md) for subsequent metadata, classification, test and retrieval verification results.

This is the implementation handoff for `eval-feedback-by-you.md`. Existing work and governance stamps were preserved. No commit, push, deployment, researcher acceptance, independent scientific review, safety validation or gravity-equivalence validation is asserted.

## What changed

| Evaluated weakness | Implemented correction |
| --- | --- |
| Model silently adds pressure, geometry or direction | `request_intent.py` binds current-turn explicit conditions with supported units and source-backed named atmospheres. Actual tool-invocation tests recover the user's PMMA/15%/10 cm/s request and remove invented pressure/opposed-flow/geometry. Correction widgets expose applied filters. Other condition-based PSI tools use the same binding or refuse a view that cannot apply the requested conditions. |
| Ambiguous requests become guessed queries | Ranges, unsupported units/materials, conflicting conditions, contextual-only follow-ups, negated filters and outcome rates mistaken for flow receive deterministic clarification and a working unconstrained Explorer link. An ISS platform mention alone cannot set cabin pressure. Record-detail tools cannot substitute an unrequested real ID. |
| Numerical model prose can escape before or after a tool | The entire assistant-text event path is held until tool use is known. PSI-turn text, including added/delta/done/persisted items and pre-tool prose, is replaced by a fixed nonnumeric evidence handoff. Values/citations remain in code-owned widgets. Narrative-only document answers retain their separate path and bounded limitations. |
| Diagnostic accepts a value with the wrong unit | Unit-aware citation diagnostic plus the independent widget-only PSI text boundary. The controlled 34%-as-34-mm/s counterexample is rejected and cannot appear in PSI prose. |
| Pairwise comparison only says metadata insufficient | Additive Python/TypeScript `comparison-audit-v1`: shared facts, setup differences, missing/conflicted fields, original source-indexed outcomes and reason-coded next checks. Strict comparability remains unchanged. The real SAFFIRE VI-3/VI-4 outlet-temperature audit verifies Table 2's 77°C and 57°C against saved original report extraction. It does not infer subtraction, causality or a controlled comparison. |
| Individual measurements look like material distributions | `sorted-observations-v1` keeps every eligible record separate, exposes raw value/unit/source/setup and marks comparability unaudited. No n=2 pooling from coincidentally equal incomplete setup. Legacy statistical keys remain for compatibility with n=1; the widget displays individual observations rather than a material leaderboard. |
| Outcome selection can conceal unsuitable values | Existing and strengthened guards reject censored points, nonfinite values, missing units, source conflicts, unresolved definitions, non-ignition burn times and ambiguous/contradictory outcome-condition sweeps. Python/TypeScript parity remains tested. |
| Plots mix incompatible data | Preserved the existing in-progress outcome-series improvement: distinct quantity/geometry/unit groups, with source-conflict/censored outcomes excluded from plotting and retained in source records. |
| Sharing acquires default PMMA query | Explicit `search=1` marker, including Python widget links, preserves intentionally unconstrained requests. Detail/comparison-only links do not gain default numeric filters. Similar-test buttons omit range/multi-value axes rather than inventing midpoint conditions. |
| Finding records does not finish a researcher task | `/decide` now records the research question verbatim, uses explicit controls and a measurement focus, supports an investigation shortlist, computes retrieval sensitivity, supplies source-backed inclusion and deterministic next checks, and exports a versioned dossier plus full evidence appendix. The question is not secretly interpreted by a model. |
| Coverage count merges complete and incomplete evidence | Mission cards now display full/incomplete separately rather than a combined pill number. Indexed observations are explicitly distinguished from independent experimental replicates. |
| Unreliable secondary surfaces distract from the core | Home primary action opens the evidence workflow; a worked real SAFFIRE audit is linked. Chat starters no longer imply universal gap discovery or material safety rankings. Upload UI is disabled; temporary chat history is not described as durable evidence storage. |
| Evidence tests do not gate publication | Reusable `validate-psi.yml` runs source mapping, TypeScript and locked Python suites. Pages build depends on this job. This workflow is implemented locally; no hosted Actions run is claimed. |
| Documentation overstates generation-10 verification | README separates the generation-10 ingest receipt from the saved generation-9 retrieval report. Expanded-detail retrieval is not claimed verified. Method/export documentation describes dossier v2, audit v1, individual observations and bounded chat behavior. |

## Reproducible research result

In the built `/decide/` application, choose material evidence near the Lunar atmosphere, then shortlist SAFFIRE IV–VI and ACME BRE. The dossier records the question, measurement focus and explicit conditions; preserves BRE's emulator role; exposes outside-window/missing-condition/source-audit actions; and shows that doubling the oxygen retrieval tolerance admits one full SAFFIRE record. The experiment and its scientific transfer limitations remain unchanged.

The actual browser-downloaded dossier contains all 1,951 source-linked evidence records as an appendix and the two selected investigations separately. Reloading its URL restores the question and shortlist. This is a complete auditable research-selection journey, not a declaration that a material is safe.

The worked comparison URL is:

`/explore/?compare=saffire-iv-vi%3AVI-3&compare=saffire-iv-vi%3AVI-4&compare_quantity=max_temp_sfu_outlet`

The audit exposes the original observations, differences in fuel description/oxygen/pressure and missing metadata. It continues to report `insufficient_metadata` for a condition-matched claim. This deliberately implements a useful audit rather than fabricating an instrument or relaxing the guard.

## Actual verification

- **67 TypeScript tests passed**, including real dataset/source audit, dossier/sensitivity, plots, rank observations and query/comparison parity.
- **267 backend tests passed, 3 expected failures** in the final full run.
- **63 ingest tests passed, 2 expected failures**. No ingest rules or generated PSI data were changed by this implementation.
- **397 passing tests in total**, with five known expected failures remaining; these are not counted as passing behavior.
- `npm run check:decision`: passed, eleven quoted assignments across all three jobs.
- `npm run check`: passed; governed record remains well formed.
- Full static build with `KSOR_BASE_PATH=/flame-freefall`: passed; final site-only rebuild after accessible-name changes passed too, including TypeScript and 109 static routes.
- `git diff --check`: passed, with ordinary line-ending notices.
- Local Chrome/Playwright end-to-end run: **passed**, exercising shortlist, sensitivity, both actual downloads, source-indexed audit, URL restoration, 390px layout, detection activation and dataset failure/retry. No JavaScript page errors or horizontal overflow were observed in those scenarios.
- Export completeness: real browser dossier contains 1,951 records; gaseous export regression contains 1,203 records, 4,045,705 bytes and measured 81.1 ms generation/serialization in the final TypeScript run. This is a local measurement, not a device performance promise.

The browser connector became unavailable during the session. Verification continued using an already-cached Playwright package and installed Chrome in an isolated headless session; no production dependency was added. Browser artifacts: `.playwright-mcp/implemented-workflow-result.json`, `implemented-dossier.json`, `implemented-comparison.json`, `implemented-dossier-desktop.png`, `implemented-dossier-mobile.png`, and `implemented-audit-mobile.png`. The reusable local scenario script is `verify-implemented-workflow.cjs` in the same artifact directory.

## Remaining uncertainty and limitations

“All fixed” would be inaccurate. Required instrument/method metadata remains absent from the structured dataset. The comparison audit makes this useful and explicit but does not establish a source-complete positive matched comparison. Classification still has eleven internally checked assignments, with other memberships remaining unclassified; the existing mapping report lists them. No unsupported relevance was invented.

The chat parser is deliberately bounded; complex, negated or context-dependent requests may require explicit Explorer controls or restating conditions. Narrative document answers are not universally guaranteed correct. PSI widgets are code-owned, while their underlying source interpretation still requires scientific scrutiny. Five expected-failure cases remain in the wider QA suites, including raw-data identity/placeholder issues and legacy boundary behavior. Disabled upload UI does not constitute a complete backend upload-security redesign.

Pressure sparsity, uncertain experimental independence and missing source metadata remain real scientific constraints. No researcher time-saving study, independent expert adjudication, NASA endorsement, predictive validation or safety certification was performed. Generation-10 expanded-detail retrieval remains unverified by a refreshed saved report.

These are local implemented changes. The public `/decide` route previously returned 404, and no publication was performed during this work. A successful local build is not evidence that the live site or backend has changed.
