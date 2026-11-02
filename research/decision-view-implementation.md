# Fire-safety evidence decision view implementation

Historical implementation snapshot. Subsequent source-method work expanded the
mapping to 19 assignments; current behavior and verification are described in
[the source-method follow-up](source-method-followup-2026-11-02.md).

Implemented `/decide/` as a static, deterministic research directory, with navigation and home-page entry links. Review status is **internal review only**. No independent researcher review, safety validation, gravity-equivalence validation, predictive model, deployment, or mission suitability claim is established by this work.

## Files and preserved boundaries

| File | Change |
| --- | --- |
| `psi-data/decision-contexts.yaml` | Eleven source-quoted assignments, direct/indirect relevance, automated checker identity and actual UTC checking timestamp; explicit instrument and report-only excerpts. |
| `system/site/lib/decision.ts` | Validated URL state, preset/custom conversion, exhaustive query-derived buckets, ordering, categorical exclusions, missing-field counts, Explorer links and separately versioned export wrapper. |
| `system/site/lib/decision-mapping.ts` | Build/test validation of investigation IDs, stable document status, body quotations, excerpt quotations, duplicate membership and checker metadata; requires support for each job. |
| `system/site/lib/decision.test.ts` | Eight scenario-oriented tests covering mapping, inputs, data semantics, ordering, export and links. |
| `system/site/app/decide/page.tsx` | Static page reading and checking the mapping at build time. |
| `system/site/components/decide/decision-view.tsx` | Job/scenario controls, expandable investigation directory and source inspection, error/retry states, comparison selection, shareable URLs and JSON download. |
| `system/site/app/global.css` | Scoped responsive decision-view styles using existing theme tokens and visible keyboard focus. |
| `system/site/components/workspace-nav.tsx` | Find relevant evidence entry. |
| `system/site/app/(home)/page.tsx` | Find relevant evidence entry. |
| `scripts/check-decision-contexts.mjs`, `package.json` | `npm run check:decision`. |
| `build.lock.json` | Refreshed by the ordinary governed build; this file was already modified before work began. |
| `research/decision-view-implementation.md` | This implementation and verification report. |

The working tree was already dirty. Existing README, literature, summary, research and script work was preserved. No knowledge body, approval stamp, eligibility notice, PSI ingest rule, raw matrix, query implementation, Python twin, Explorer implementation or existing `evidenceExport()` function was edited. Generated data was not hand-edited. No infrastructure or dependency was added. Local preview, screenshots, browser logs and downloaded JSON are under the already-untracked `.playwright-mcp/` directory.

## Implementation choices and observable checks

| Choice | Observable evidence |
| --- | --- |
| Keep all investigation identities visible; an absent mapping is unknown, not exclusion or negative relevance. | Browser default lists 19 investigations. Mapping check prints all unclassified memberships; detection test retains SAME and SAME-R with atmosphere fields missing. |
| Classify from selected stable-document quotations, never names or geometry. | Mapping tests reject unknown IDs, unsupported quotes, a non-stable document, human-review impersonation and duplicate job assignments. All three jobs have at least one supported assignment. |
| Retain preset pressure rounding while displaying source kPa; edited pressure uses the shared conversion constant without added rounding. | Preset tests cover ISS, Gateway and Lunar; custom pressure/tolerance tests check exact multiplication by `ATM_PER_KPA`; a converted tolerance edge remains inclusive. |
| Detection starts with atmosphere disabled and unconditioned browsing; prevention and suppression use Lunar. Rover, spacesuit, Mars and custom have no numerical preset. | Defaults/activation tests and browser walkthroughs; rover export remains disabled until conditions or explicit browsing are selected. |
| Preserve invalid URL input as text and block evidence/export until corrected. | URL tests; browser `pressure_kpa=bad` remains after reload, has `aria-invalid=true`, and disables export. |
| Use only existing `conditions.flow_cm_s` for flow filtering. | Inspected both query implementations; Python reads `run["conditions"].get(axis)` and TypeScript `measureOf()` reads `run.conditions[axis]`. Adversarial test with only outcome-at-flow and panel-setting values remains missing on the flow axis. Existing Python query parity suite passes. |
| Partition returned axis statuses; request the full near pool. | Synthetic full/partial/outside-only/outside-plus-missing/none-reported cases, continuous range versus discrete multi-value cases, more than ten near records, conflict overlays and partition totals pass. |
| Count only tests/test points as individuals; retain other granularities separately. | Summary exclusion and partition-total assertions; gaseous export contains every record without display truncation. |
| Preserve global relevance order, then geometry labels and filters. | Direct/indirect ordering and deterministic tie tests pass; Lunar walkthrough keeps BRE indirect despite its full condition record. Spatial regrouping is deferred. |
| Omit full/partial sorting keys when neither oxygen nor pressure is requested, including flow-only browsing. Numeric flow still produces its own condition buckets. | A flow-only fixture puts two outside records with cited outcomes ahead of one full record; unconditioned ordering tests also pass. |
| Keep conflicting source values as an overlay rather than excluding or resolving them. | Synthetic conflict remains in the full bucket and retains both values; source-indexed conflict values appear in record inspection/export. |
| Present original representations and query-normalized tolerance distance; never synthesize a nearest scalar. | Multi-value/range tests and raw source inspection. Infinite distance at zero tolerance has an explicit export sidecar because JSON numeric infinity serializes to null; the unchanged evidence payload is preserved. |
| Distinguish report-only agents/objectives and requirements from structured run conditions/outcomes. | Suppression test and browser walkthrough show BASS's nitrogen objective separately from FLEX diluent fields and FLEX-2's requirements-only caveat. |
| Keep publication-only observations unranked and outside individual-test counts. | Dedicated page section and export document IDs for LUCI, DAFT and FLEX-2 cool-flame supplement; no new PSI runs are constructed. |
| Defer details until opened. | Browser opens an investigation, then a record, and obtains source/Explorer links; collapsed investigations do not mount all record fields. |
| Restrict pairwise selection to one geometry. | Browser selects a solid record and confirms BRE's selection checkbox is disabled. Existing Explorer comparison is linked with compatible query/tolerance parameters. |
| Wrap, rather than modify, the existing evidence export. | Deep equality against `evidenceExport()` passes; fixed-generation-time output is reproducible. Browser download contains all 1,951 records and the dataset SHA-256. |

Blank tolerance inputs retain existing query defaults; an explicitly entered zero remains zero. All numeric inputs must be finite; oxygen is in 0–100%, pressure must be positive, and flow/tolerances must be non-negative. Changes to job/scenario reset their defaults while retaining material and geometry filters; changes within a scenario retain text for correction. A custom edit of preset conditions is explicitly described as custom. These are interface choices, not new numerical mission presets.

## Classification coverage and gaps

Supported assignments are prevention: BASS, BASS-II, SAFFIRE-1, SAFFIRE-2, SAFFIRE IV–VI (direct), ACME BRE (indirect); detection: SAME and SAME-R (direct); suppression: FLEX and BASS (direct), FLEX-2 (indirect). BASS's suppression assignment concerns a documented objective, not an observed suppression result. FLEX-2's assignment concerns planned requirements/envelopes, not flight results. Direct means direct relevance to the research job; it does not upgrade a plan to empirical evidence.

No unsupported assignments were admitted. The shared reason for every membership below is **no source-checked assignment for this job selected in this release**. This is not a finding that the investigation is irrelevant or that no supporting source exists. An investigation mapped to one job remains unclassified for other jobs until a separate quote is checked.

| Job | Every unclassified investigation ID |
| --- | --- |
| Prevention | `acme-cld`, `acme-efield`, `acme-flame-design`, `acme-s-flame`, `cfi`, `cfi-g`, `flex`, `flex-2`, `saffire-3`, `same`, `same-r`, `slice`, `spice` |
| Detection | `acme-bre`, `acme-cld`, `acme-efield`, `acme-flame-design`, `acme-s-flame`, `bass`, `bass-ii`, `cfi`, `cfi-g`, `flex`, `flex-2`, `saffire-1`, `saffire-2`, `saffire-3`, `saffire-iv-vi`, `slice`, `spice` |
| Suppression | `acme-bre`, `acme-cld`, `acme-efield`, `acme-flame-design`, `acme-s-flame`, `bass-ii`, `cfi`, `cfi-g`, `saffire-1`, `saffire-2`, `saffire-3`, `saffire-iv-vi`, `same`, `same-r`, `slice`, `spice` |

Nine investigations have no assignment to any job: `acme-cld`, `acme-efield`, `acme-flame-design`, `acme-s-flame`, `cfi`, `cfi-g`, `saffire-3`, `slice`, `spice`. For ACME CLD/E-FIELD/Flame Design/S-Flame, CFI and SPICE, this implementation did not establish a defensible task-specific quote and direct/indirect class, so it withheld a mapping. CFI-G and SLICE additionally lack a stable-document citation in the current investigation metadata. The selected SAFFIRE document describes flights 1/2 and IV–VI; this implementation did not extend that support to SAFFIRE-3 by family name. Relevance coverage remains intentionally incomplete.

## Actual verification

- `npm.cmd --prefix system/site run test:psi`: **53 passed**, including eight decision tests and unchanged query/comparison/export tests.
- `uv run pytest tests/test_psi_query.py -q`: **19 passed**. The first attempt was blocked by sandbox access to uv's cache; the authorized retry succeeded. An initial invocation used the nonexistent `test_query.py` filename and ran no tests; it was corrected.
- `npm.cmd run check:decision`: **passed**, eleven source-supported assignments and all three jobs represented.
- `npm.cmd run check`: **passed**; record well formed.
- TypeScript `tsc --noEmit`: **passed**; final static build also completed its TypeScript check.
- `$env:KSOR_BASE_PATH='/flame-freefall'; npm.cmd run build`: **passed**, static `/decide` output among 109 generated routes. Build reports the existing dirty working tree and ordinary Fumadocs dynamic-import cache warnings. No clean-commit/release claim is made.
- `git diff --check`: **passed**; only Git line-ending notices.
- Full gaseous-flame export: **1,203 records**, **4,044,349 bytes** compact serialized JSON, **82.3 ms** generation plus serialization in the final TypeScript test run on this machine. This is a local measurement, not a browser/device performance guarantee. The decision wrapper repeats source-linked run views alongside the unchanged evidence payload, trading file size for a self-contained audit.
- Actual browser download: **1,951 records** in both the evidence payload and decision rows, eleven classification assignments, SHA-256 `3286c2da58bd7c85704551d1021f8bd9c9f1564ed368fa236725b4c01fd3fcb2`, with internal-review and evidence-limit notices.
- Browser desktop at 1440 px and mobile at 390 px: **no horizontal overflow**. Existing neutral typography/colors retained; mobile stacks the same investigation fields. Keyboard Tab advances from research job to scenario; focus styling is explicit.
- Simulated dataset network failure: retry appears and export disables; removing the failure and retrying restores 19 investigations and export.
- Preset/publication source URLs and inspected classification/Explorer URLs returned **HTTP 200** under `/flame-freefall`. Clicking the classification source reaches the BASS-II governed page. The first navigation assertion required a trailing slash and timed out after successful navigation to the slashless URL; an optional-slash assertion passed.
- The minimal static preview reports 404s for existing Next.js segmented-prefetch filenames. Direct HTML source links return 200 and the tested client navigation succeeds. No routing infrastructure was changed to hide this issue; deployed hosting behavior remains unverified.

Artifacts: `.playwright-mcp/decision-desktop-verified.png`, `.playwright-mcp/decision-mobile-verified.png`, `.playwright-mcp/decision-export-verified.json`. A local static preview helper was used solely for production-base-path inspection; it is not deployment infrastructure.

## Three agent walkthroughs

1. **Lunar prevention and sensitivity.** At default tolerances BASS-II leads by direct relevance and 129 individuals with cited outcomes; all 129 lack pressure, and all are outside-plus-missing. The quoted inclusion reason and source-inspection action are accessible on expansion. Raising oxygen tolerance to 15 percentage points moves SAFFIRE IV–VI first, with three full individuals. BRE has one full individual at the default Lunar window but remains indirect, explicitly “Emulator, not a solid sample.” No cross-geometry outcome ranking is constructed.
2. **Detection and missing metadata.** SAME-R leads unconditioned browsing with 109 individual records and 108 with cited outcomes. Its M-pass instrument excerpt is source-linked. Explicit atmosphere activation retains all 109 as none-reported rather than removing the investigation. Inspect the source for missing oxygen/pressure without assuming it contains the values. SAME remains discoverable too.
3. **Suppression and next action.** FLEX leads as directly relevant, with structured diluent conditions and source-indexed outcomes. At the default Lunar window, no classified suppression investigation has full/partial individual evidence, so the page offers explicit material/tolerance changes and acknowledges possible new tests. BASS's nitrogen requirement is report-only evidence, and FLEX-2 remains indirect with its preflight caveat. Choosing rover clears numerical conditions and requires explicit browsing or conditions before export.

These scripted rehearsals located the first inclusion reason, missing evidence and next action in less than approximately two minutes each. **No researcher was observed or interviewed. Whether an independent researcher can explain those three items in approximately two minutes remains unmeasured; agent rehearsal does not establish acceptance.**

## Remaining launch limitations and material fallbacks

Sparse pressure coverage and absent atmosphere metadata remain prominent on both page and export. They are unknowns, not implied ambient conditions. Classification is partial and internally checked only. Source excerpts establish textual support, not independent scientific endorsement of the chosen relevance classes. Stable-document quotes are checked automatically; no human approval was invented.

Global direct/indirect ordering takes precedence over contiguous geometry grouping. Geometry labels, filtering and single-geometry comparison controls are the implemented fallback; spatial regrouping awaits a precedence decision. Publication-only evidence remains unranked. Report-only agents and planned envelopes remain distinct from measured per-test evidence. Missing fields lead to source inspection without promising recovery; outside conditions produce comparison candidates, not equivalence; conflict inspection retains both values.

No independent review, researcher acceptance, safety validation, gravity-equivalence validation or live deployment verification was performed. Existing eligibility notices and governance stamps remain as supplied. No commit or push was requested or performed.
