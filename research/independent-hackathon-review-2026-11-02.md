# Flame Freefall: critical competition review

Historical review snapshot. Its public-site observations do not describe the
current local implementation. See [the source-method follow-up](source-method-followup-2026-11-02.md)
for later changes and bounded verification results.

Review date: 2026-11-02 local. Scope: supplied `challenge-details.md`, current public GitHub implementation at `d30f6dea3bbb55a4367d08fac9c832e913e9c60f`, live GitHub Pages application and local working tree. The outdated Drive deck was excluded at the owner's instruction. `DEMO.md` is a proposed script, not a reviewed finished pitch.

Separate agents examined science, engineering and judging/product strategy. This is an agent-assisted critical review, not independent human peer review, NASA endorsement, or a measured user study. No application code, record, approval, deployment or external account was changed. Only review artifacts were written.

## Judgment

The project has a substantial research-data foundation and a defensible technical differentiator: source-preserving normalization and deterministic evidence inspection. Its competition proposition is weaker than its implementation. It has not yet demonstrated that a researcher reaches a better, reproducible research decision, and some prominently suggested analysis workflows lack a real positive path.

The best product is an experiment-selection and evidence-transfer workbench: identify applicable investigations, explain transfer limits, inspect what blocks comparison, and export an auditable selection. It should not claim to choose safe materials, validate Lunar behavior, or identify a best suppressant from incomplete heterogeneous catalogs.

## Challenge interpretation

The central task is to make fragmented PSI research useful for prevention, detection and suppression in crew environments. A successful tool must preserve scientific distinctions while helping a user decide what to investigate next. It is not sufficient to concatenate reports, offer chat, or sort measurements without explaining setup differences.

Important distinctions:

- Oxygen concentration and total pressure remain separate; equivalent oxygen partial pressure need not imply equivalent material flammability. NASA's evaluated materials showed stronger dependence on concentration: https://ntrs.nasa.gov/citations/20160001047 .
- Atmosphere overlap is a retrieval property, not a validated transfer across gravity, fuel, geometry, apparatus or measurement method. NASA's FM2 work motivates direct partial-gravity testing: https://www.nasa.gov/glenn/glenn-expertise-space-exploration/physical-sciences-program/combustion-science/flammability-of-materials-on-the-moon-fm2/ .
- BRE is useful indirect evidence about condensed fuels, although its flames are gas-fed. Do not hide it under an irrelevant gas category or relabel it a solid specimen.
- Inverse CFI-G oxidizer-stream oxygen is not cabin oxygen. Current ingest keeps these distinct.
- Detection investigations remain relevant when indexed atmosphere fields are missing. Dust/aerosol background, fire-smoke signals and universal detector performance are different evidence claims.
- FLEX's catalog makes experiments available rather than establishing a universal interpretation or winning suppressant: https://ntrs.nasa.gov/citations/20150023456 .
- The challenge's predictive-modeling-data objective does not require inventing a predictive model from records that lack sufficient metadata or independent replication.

## Verified public behavior

| Probe | Actual observation | Limit |
| --- | --- | --- |
| GitHub main commit API | Public main is `d30f6dea3bbb55a4367d08fac9c832e913e9c60f`, dated 2026-10-31. | A commit alone does not establish every backend's revision. |
| `/psi/runs.json` | HTTP 200; 1,951 records; generated `2026-10-31T12:54:38+00:00`; SHA-256 `3286c2da58bd7c85704551d1021f8bd9c9f1564ed368fa236725b4c01fd3fcb2`. | Counts are indexed records, not independently validated trials. |
| Home | Reports 1,035 records with outcomes, geometry-specific coverage, source-linked literature and explicit scientific caveats. | Outcome presence includes text; it is not a count of validated numeric measurements. |
| New `/decide/` | HTTP 404 on the public site; no navigation entry. | Local implementation cannot count as deployed functionality. |
| Explorer Lunar query | `o2_pct=34&pressure_atm=0.5576`: 11 full and 75 partial across all granularities. | Partial records do not establish atmosphere coverage. |
| Home Lunar gaseous pill | 74 = 11 full + 63 partial individual records. | Not a data disagreement. The split is mainly in the title tooltip; the visible merged number is easy to misread. |
| Home sensitivity case | Default: solids 0/0, BRE 1/0, other gas 10/63; tighter pressure: 0/0, 1/0, 0/54; wider oxygen: 1/0, 1/0, 14/63 (full/incomplete). | These are search-window results, not safety or gravity equivalence. |
| Download actual gaseous export | 1,203 records, all source-bearing; query/tolerances, method version and dataset fingerprint present; includes full/partial/near without UI truncation. | Source linkage is valuable but does not certify source correctness. |
| Live pairwise comparison | `PSI-99:2-8` versus `PSI-99:2-9`, `spread_rate`, displays insufficient metadata, including unknown instrument/method. | Conservative abstention works; it does not demonstrate a successful condition-matched comparison. |
| Live chat | A longer probe returned a deterministic evidence widget; an earlier 12-second observation had not completed. | Not a latency benchmark; chat was not universally unavailable. |
| Mobile home | At 390 px, no horizontal overflow and navigation opens with the four current destinations. | Not a comprehensive screen-reader, contrast or WCAG audit. |

Public Explorer export is saved at `.playwright-mcp/review-live-evidence-export.json`. Screenshots include `review-live-home.png` and `review-live-case-study.png`.

## Major findings

### 1. Chat can change the research question

Observed live prompt:

> Find PMMA tests at 15% oxygen and 10 cm/s. Show the evidence widget.

The returned widget applied oxygen 15%, flow 10 cm/s, **pressure approximately 1 atm**, geometry solid-fuel and **opposed flow**. Pressure and flow direction were not requested. `psi_tools.py:248–263` defaults these optional fields to `None`; they were model-selected additions, not backend defaults. The instruction to pass only stated conditions is prompt text, not a code-enforced intent guarantee.

The model's prose also restated measured values and used dataset-only `PSI-25` references rather than individual run IDs. The widget contained richer source information. This is an observed query-intent and citation-specificity limitation, not proof that its displayed measured values were fabricated.

Fix: make the interpreted filters visible and editable, distinguish user-stated conditions from assumptions, prevent silent constraints, and use deterministic rendering for quantities and their source-specific claims. Test paraphrases and compare structured user intent against actual tool calls.

### 2. Comparison has no supported real-data positive path

Both `instrument` and `measurement_method` are absent from all 1,951 current records. The comparison engines require them universally (`system/site/lib/psi-comparison.ts:4`, `system/chatkit-server/psi_comparison.py:5`). There is no per-outcome fallback. Consequently every real pair must be marked insufficient metadata. Synthetic complete-metadata fixtures establish code behavior, not practical dataset coverage.

Fix: source-check one bounded within-investigation comparison, including outcome-specific method/instrument and all other required conditions. Retain unknowns and abstention if the source cannot establish them. Until a positive case exists, describe the feature as a comparison audit or side-by-side inspection, not a validated comparison engine.

### 3. Ranking overstates the usefulness of its aggregation

Fresh unconstrained ranking results:

| Quantity | Cohort rows | Largest cohort |
| --- | ---: | ---: |
| Solid spread rate | 6 | 1 |
| Droplet burning-rate constant | 260 | 1 |
| Droplet extinction diameter | 190 | 1 |
| Gaseous burn time | 272 | 1 |
| Peak burner temperature | 282 | 2 |

The cohort key includes every condition, including identifiers, dates, descriptions and processing flags (`psi_query.py:406,477`, TypeScript query around 410–416). Preserving strata prevents unsafe pooling, but mostly yields single observations dressed as medians/ranges. Sorting separate strata can still invite comparisons across materials, flow directions, dimensions or apparatus.

Fix: display individual observations plainly; replace material-leaderboard framing with stratified measurement summaries. Define a scientific cohort schema before aggregating replicates. Removing identifiers alone is insufficient to establish independence or compatible methods.

### 4. Guard coverage is narrower than an all-answers trust claim

The numerical citation guard pools all numerical values on a run without binding each value to quantity/unit. Synthetic reproduction:

```python
g = TurnGuard()
g.record_valid_run_ids({"acme-bre:19070D1"})
g.check_citations("The spread rate is 34 mm/s (acme-bre:19070D1).")
# set()
```

The 34 comes from the record's oxygen condition, not a spread-rate measurement. A fabricated 999 is detected. Moreover `main.py:536–562` logs citation failures after streaming rather than blocking or replacing this prose. Dataset-only references without a colon are outside the individual-run citation pattern.

This is a controlled counterexample, not an observed live assertion of a 34 mm/s spread rate. It establishes that deterministic widget provenance does not extend to every model sentence. Fix the architecture and bound claims rather than adding more instructions.

### 5. Scientific value needs task-specific metadata and independent assessment

No populated current `instrument`/`measurement_method` fields, limited explicit uncertainty and incomplete pressure coverage constrain interpretation. SAME-R's 109 indexed observations collapse to 66 base test numbers when a/b suffixes are removed; aged observations are not automatically independent tests. Add observation-to-parent-test relationships without silently merging them.

No external researcher study or independent combustion-science adjudication was verified. Owner approval metadata is a recorded governance event, not evidence that this agent independently confirmed scientific peer review.

### 6. Release and CI evidence need tightening

Fresh tests:

- TypeScript: 53 passed.
- Chat backend: 201 passed, 4 expected failures.
- Ingest: 63 passed, 2 expected failures, after rerunning outside the sandbox to resolve pytest temp-directory access.

Expected failures include a CLD fuel/test-type identity inconsistency and untrusted upload-framing concerns. They are known defects, not passing behavior. Format validation and static build run in GitHub workflows; PSI business tests are not deployment gates.

The **committed** README says generation 9/270 chunks and is consistent with `research/rag-publication.json`. The **modified local** README says generation 10/284 chunks and expanded-detail checks, while the saved report still verifies generation 9. The untracked generation-10 receipt records ingestion, not successful retrieval of the new details. Re-run and publish the verification artifact before claiming this stronger capability. This distinction is not a finding that the public committed README makes the stronger unsupported claim.

## Competition assessment

An official-hosted 2026 local-event page lists Impact, Creativity, Validity, Relevance and Presentation: https://www.spaceappschallenge.org/2026/local-events/ajmer/ . Detailed global 2026 weights and final presentation-duration rules were not verified. The following is our diagnostic judgment, not an official score or winning probability.

| Criterion | Score / 5 | Reason |
| --- | ---: | --- |
| Impact | 3 | A real researcher problem and reusable evidence artifact; no measured improvement over raw PSI/report work. |
| Creativity | 3.5 | Provenance, deterministic tools and sensitivity-aware retrieval are a substantive combination. Chat/RAG/dashboard alone is readily imitated. |
| Validity | 3 | Strong data boundaries and tests; real comparison path, intent integrity, cohort interpretation and external scientific assessment remain incomplete. |
| Relevance | 4 | Closely addresses PSI discovery, evidence inspection and model-data preparation; detection/suppression task completion is weaker than condition browsing. |
| Presentation | Unscored | Outdated deck excluded; no current recording supplied. Live communication is clear but dense and does not yet prioritize a single useful research decision. |

Four assessable dimensions total **13.5/20**. Do not convert this into a complete official submission score. Engineering depth is stronger than demonstrated user impact. I cannot establish a current finalist/winner position relative to unreviewed competitors.

Eligibility is a separate gate: official event dates are November 14–15, 2026 (https://www.spaceappschallenge.org/2026/), and official-hosted guidance expressly prohibits developing the intended submission early (https://www.spaceappschallenge.org/2026/local-events/santiago-dominican-republic/). This repository predates the event. Obtain written organizer clarification on permitted prior work and disclosure; no definitive eligibility exception or disqualification is established here. Preserve history. Third-party rights also require review under https://www.spaceappschallenge.org/legal/ ; project MIT licensing does not establish rights over every bundled scientific PDF.

## Highest-value strategy

| Priority | Work | Completion evidence |
| --- | --- | --- |
| Gate | Resolve prior-work eligibility and intended-submission scope. | Written clarification; preserved history and disclosed prior work. |
| 1 | Close query-intent and checkable-prose gaps. | Canonical prompt/paraphrase set adds no unstated filters; quantities/citations render from typed evidence; known guard counterexample is no longer presented as valid prose. |
| 2 | Demonstrate one source-complete comparison or explicitly useful blocked comparison. | A real published pair with traceable metadata, transparent differences and no manufactured conditions. |
| 3 | Complete a researcher journey through relevance, transfer limits, source inspection and export. | Independently observed task completion and correct explanation of the first result, missing evidence and next action. Local `/decide` is a useful foundation but is not deployed and has only eleven internally checked assignments. |
| 4 | Replace misleading statistical/coverage presentation. | Full and incomplete counts shown separately, n=1 shown as an observation, parent-test relationships explicit. |
| 5 | Validate usefulness and scientific correctness on a bounded set. | Expert-adjudicated difficult questions and source records; task times, retrieval errors and unsupported conclusions measured against the raw PSI/report workflow. |
| 6 | Gate releases on business tests and versioned public smoke checks. | PSI tests in CI; matching dataset/method versions across site/export/backend; current retrieval report. |
| 7 | Record a new task-based demonstration. | Completed recording using the deployed revision, actual evidence and a usable export; no outdated counts or universal trust claims. |

Limit scope to three scientific demonstrations:

1. **Prevention:** an exploration-atmosphere evidence dossier separating direct solid specimens, BRE emulation and missing-condition evidence. Show how sensitivity changes the shortlist and why it does not establish safety.
2. **Detection:** a source-backed brief connecting SAME-R particle/instrument response to SAFFIRE VI's gas-versus-thermal hazard observations. Keep any threshold-crossing observation specific to its experiment; do not call it a universal alarm delay. NASA's report supports the hazard distinction: https://ntrs.nasa.gov/citations/20240002981 .
3. **Suppression:** a scoped FLEX extinction-evidence selection, with gas composition, geometry and source limits, rather than a universally best suppressant recommendation.

De-emphasize architecture tours, additional models, broad prediction, simulated spacecraft visuals without validation, generic safety scores, statistically decorated single observations, and new corpus volume without useful retrieval. Keep the static Explorer as a reliable demonstration path; optional chat should help route users rather than silently alter the research question.

NASA's official 2025 winner descriptions identify SpaceGenes+ with a specific researcher question and Astro Sweepers with concrete assessment outputs. The transferable pattern is a named user, consequential question and inspectable output; this is an inference from official descriptions, not a claim that their videos or implementations were reviewed or that the pattern causes awards: https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-announces-2025-international-space-apps-challenge-global-winners/ .

A prospective two-minute demonstration, subject to final official format: state the researcher's question; show a tempting but unsupported comparison; inspect direct/indirect evidence and the missing condition; export the reproducible dossier; finish with actual evaluation results and remaining limits. A useful final artifact is more persuasive than a menu tour or a montage of chat responses.
