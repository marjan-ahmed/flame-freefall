# Source methods and researcher-workflow follow-up

This report follows `implemented-improvements-2026-11-02.md`; its measurements
replace that report's earlier test counts, classification coverage and retrieval
verification status. Existing uncommitted work and governed approval stamps were
preserved. No commit, push or deployment was performed.

## Implemented changes

| Change | Scientific purpose and observable check |
| --- | --- |
| Outcome-specific instrument and method provenance | 260 FLEX burning-rate outcomes carry the report-defined HiBMs instrument and diameter-squared linear-fit definition, with source indexes and verbatim quotes checked against the original extraction and stable document. Extinction diameters receive no blanket method because the report includes extrapolated diameters. |
| Instrument channels separated from calibration | 108 SAME-R ISS detector outcomes and 16 STS detector outcomes retain their exact workbook channel headers and published-processing basis. Voltage is not relabeled as calibrated concentration; calibration remains unknown. |
| Selected-outcome comparison checks | Python and TypeScript `comparability-v2` assess the selected outcome's source-backed metadata. Invalid source indexes or unsupported quotes remain unknown. The real FLEX pair now shares instrument/method evidence but remains `insufficient_metadata` because other required setup fields are missing. |
| Source observation relationships | SAME-R retains 109 observations and 65 resolved identifier groups. Two observations at stem 57 conflict across materials and remain unjoined. Explicit descriptions determine aging role: suffix `a` alone does not. Independence remains unknown and no rows are merged. |
| Classification coverage | Eight additional stable-document-backed assignments bring the mapping to 19. Each new assignment records an automated checker and timestamp, quote and explicit relevance rationale. Indirect soot, flame-control and cool-flame evidence does not become detector performance or validated suppression hardware. |
| Source inspection | Explorer, comparisons and decision records show outcome metadata, basis and source quotes. Decision dossiers preserve observation relationship summaries and explicitly record independent review as not performed. |
| Executable researcher scenarios | `npm run evaluate:research` checks Lunar retrieval sensitivity/BRE separation, SAME-R channel and identifier interpretation, and FLEX method inspection with remaining comparison blockers. A separate review packet leaves researcher answers, completion times and approval blank. |
| Read-only release and retrieval verification | `npm run verify:release` checks routes, dataset identity and service health without publishing. The public MCP evaluator checks expanded approved literature and control abstentions, with a bounded timeout and nonzero exit on failure. |

Primary implementation files include `system/psi-ingest/psi_ingest/measurement_methods.py`,
`system/psi-ingest/psi_ingest/adapters/smoke.py`, both comparison implementations,
`system/site/lib/observation-relationships.ts`, the three evidence inspection
components, `psi-data/decision-contexts.yaml`, and the scenario/release scripts.
Generated data and parity fixtures were regenerated through their normal tools.
The dataset remains 1,951 records, 19 investigations and eight recorded conflicts.
The review-packet generator preserves existing packets and their original dataset
identity, including any researcher answers; a rerun cannot clear them. Visual
inspection also caught narrow result/unit columns beside long citations. Results
now reserve column widths and place method details across the full row.

## Actual verification

- TypeScript: **71 passed**.
- Chat backend: **270 passed, 3 expected failures**.
- Ingest: **70 passed, 2 expected failures**.
- Total: **411 passing tests**, with five known expected failures remaining.
- Mapping validation: all 19 assignments pass stable-document, identity, quote,
  timestamp and duplicate-membership checks.
- Record checker and static production build with `/flame-freefall`: passed.
- Three executable research scenarios: passed. Their saved facts and limitations
  are in `research-scenario-verification.json`.
- Existing scientific-evidence evaluation was rerun against the regenerated data.
- Public generation-10 retrieval: 13/13 target documents, 4/4 expanded-detail
  phrases and 8/8 expected control abstentions passed. See `rag-publication.json`.
  These are internal engineering queries, not an expert relevance benchmark or
  proof of model-answer correctness.

The regenerated dataset SHA-256 is
`7c7143cb7c7385d0be5dd97ce2041218305f7cfd5b1b88f15fec9fb27365e031`.

## Remaining limitations

CFI-G, SLICE and SAFFIRE-3 still have no supported job assignment. Other
investigations may be classified for one job and unclassified for another; the
mapping checker reports every such membership. No mapping is inferred from an
investigation's name or family. The relevance rationale is internal interpretation,
not independent scientific adjudication.

| Job | Unclassified investigation IDs |
| --- | --- |
| Prevention | acme-cld, acme-efield, acme-flame-design, cfi, cfi-g, flex, flex-2, saffire-3, same, same-r, slice, spice |
| Detection | acme-bre, acme-efield, acme-flame-design, acme-s-flame, bass, bass-ii, cfi-g, flex, flex-2, saffire-1, saffire-2, saffire-3, saffire-iv-vi, slice |
| Suppression | acme-bre, acme-cld, bass-ii, cfi-g, saffire-1, saffire-2, saffire-3, saffire-iv-vi, same, same-r, slice, spice |

These memberships lack an admitted checked assignment, rather than evidence of
irrelevance. No unsupported assignment was admitted. Method enrichment was limited
to source-defined FLEX burning rates and exact SAME-R workbook channels; other
outcomes need their own source checks. Source-identifier grouping is a conservative
fallback, not an asserted parent/specimen hierarchy. Spatial regrouping remains
deferred to preserve the explicit global decision ordering.

There is still no source-complete positive condition-matched comparison in these
worked scenarios. Sparse pressure coverage, missing atmosphere/setup metadata,
unknown calibration and uncertainty, and uncertain observation independence limit
transfer and pooling. Missing source fields remain missing. This work establishes
neither safety nor gravity equivalence, a predictive model, NASA endorsement, or
independent researcher acceptance. `researcher-review-packet.json` awaits a real
reviewer; agent rehearsal does not establish two-minute task success.

Five expected failures remain in the wider suites, including CLD fuel-identity
disagreement recording, PSI placeholder outcomes and legacy cross-layer/QA
behavior. They were not hidden or counted as passing functionality.

The read-only public release check **fails**: `/decide/` returns 404 and the
public dataset SHA differs from the regenerated local dataset. Site, chat-health,
corpus-health and corpus-ready endpoints respond, but HTTP health does not prove
local implementation deployment. The new workflow and metadata require deployment
and a fresh release check before being described as live.

These changes strengthen the submission by making source inspection and the
next evidence needed concrete and reproducible. Their competitive value still
requires demonstration with actual researchers and scientific review.
