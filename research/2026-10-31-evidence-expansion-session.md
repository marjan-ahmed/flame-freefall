# Evidence-expansion session notes: detector signals, access checks, browser verification

> Historical session snapshot. For the subsequent owner approvals, new source evidence, scientific audit and vector publication, see [current completion report](2026-10-31-approved-evidence-and-publication.md).

Date: 2026-10-31 (same day as `2026-10-31-data-accuracy-and-competitors.md`, whose roadmap this continues). This is a session log, not a governed finding. Production state changes are listed; no knowledge documents were edited and nothing was committed or deployed.

## What changed in production data

### SAME-R smoke-detector signals joined (roadmap priority 2: more smoke-detection measurements)

`system/psi-ingest/psi_ingest/smoke_results.py` now joins a second sheet of the
already-mapped workbook (`Combined SAMER Results 06 02 14.xlsx`):

- `Reduced Data with ISS Det` — the exact rows of the mapped `Reduced data sheet`
  (flight-2 key multisets verified identical: 109 flight-2 rows each) **plus two
  explicitly unit-labeled instrument columns**:
  - `ISS Detector Scatter (volts)` → `iss_detector_scatter_volts` — populated on all
    109 rows (cached range 0.18–6.28 V); positive-only admission.
  - `STS Detector (volts)` → `sts_detector_volts` — populated on 17 rows; 92 rows are
    exactly zero and are excluded as "trace never recorded", never stated as
    absence of smoke. **No negative flight-2 values exist in the cached data**, but
    the admission policy keeps negatives anyway, because the SAME final science
    report states smoke deflects the ISS signal POSITIVE and the STS signal
    NEGATIVE — a sign-aware policy documented per outcome.
- The `STS Detector offset (volts)`, `STS detector delta` and `Yeild: Dust Trak
  mass/mass lostt` columns stay unmapped (no unit label / instrument-processing
  columns), recorded in the ingest-report notes.
- Every joined cell keeps its cached value and its formula string
  (`='SAME R Results'!ARn`), flagged `source_processed` + `workbook_cached`, with a
  per-outcome note; the ISS note adds that the sheet states no zero-point, so
  readings are instrument-scale volts, not calibrated smoke density.

Counts after the change (generated files, commit pending with everything else):
runs stay 1,951 / 1,033 with outcomes (the detector readings join onto records that
already carry the DustTrak/AMD diagnostics, so no new run or new record count);
source-processed workbook measurements grow 408 → 532. Label maps updated on both
twins (`psi_widgets.py` QUANTITY_LABEL, `format.ts` QUANTITY_LABEL).

### Verification state after the change

- ingest: 44 passed / 2 xfailed (existing expected failures)
- chatkit-backend: 198 passed / 4 xfailed (existing: e.g. A10 attachment fencing); `gen_query_fixtures.py` regenerated; parity holds
- site: 41 passed
- `tests/audit_source_agreement.py` extended to the second sheet: **532 source
  cells checked, 0 transfer mismatches** (`research/source-agreement.json`)
- static rebuild passed; browser verification (`scripts/verify-evidence-browser.py`)
  passed **both viewports (1280 px, 390 px)** including the repaired source-citation
  checks (URL-bearing and descriptor-only apparatus citations both asserted).

## Roadmap items resolved or checked

1. Browser verification: fixed the script's assumption that every source has a URL.
   BASS's apparatus source is a poster cited by a textual `descriptor` with no URL;
   `run-detail.tsx` now renders that descriptor, and the script asserts both
   citation forms (link+href where a URL exists; visible title + descriptor and NO
   fabricated link where it doesn't).
2. Additional SAME measurements: delivered as the detector join above.
3. BASS/BASS-II/SAFFIRE further enrichment: **checked and rejected with reasons.**
   - BASS poster ("ISS Denver 2013-BASS") gives test-level atmospheres/flows but no
     test numbers; "Nomex III Natural" / "nomex natural III" appear as two distinct
     PSI rows for one poster photograph, so per-row joins would be guesses. No join.
   - `SAFFIRE-*-MergeResult*` workbooks are image-file transfer logs (verified
     columns), not combustion measurements — already characterized in the
     data-sources doc; nothing to join.
   - `ACME Daily Test Point Log 2.xlsx` is a downlink-volume log; `thermal
     precipitator map...xlsx` is a slot map. Neither holds outcomes.
   - BASS-II flow velocities exist only in report Tables 5.1/7.1 (already joined).
4. SAFFIRE-VI "new evidence": downloaded NTRS 20240002981 and found it
   **byte-identical (SHA-256 verified) to the already-held
   `investigation_reports/Saffire-ICES-2024-ICES-365-accepted final.pdf`** whose
   Tables 1–2 are already reproduced in the governed SAFFIRE-VI doc and already
   merged into the `saffire-iv-vi` records. Download/extraction duplicates were
   deleted. Remaining unmapped columns of its Table 2 (max temperature, CO₂
   partial-pressure increase) would require widening a stable doc's tables — owner
   approval territory, listed below.
5. FLEX-2 measured outcomes: NTRS searched (multiple queries incl. the API);
   the accessible detailed-results report covers FLEX (first-generation, already
   table-rich in our PSI-69 records), **no accessible file with per-test FLEX-2
   measured outcomes was found**. The 8 FLEX-2 envelope records stay planned
   conditions; the gap remains a real acquisition blocker, not an indexing choice.

## Remaining (owner or blocked)

- Owner approval before publishing the LUCI/DAFT literature drafts.
- Owner decision on widening the stable SAFFIRE-VI doc's outcome tables (detector
  alarm timing — ionization alarm at 981 s on one VI test — and the unmapped
  Table 2 columns are in the verified extraction, not yet in the record surfaces).
- FLEX-2 per-test outcomes require an actual data source (none published/in reach).
- Expert-reviewed retrieval evaluation.
