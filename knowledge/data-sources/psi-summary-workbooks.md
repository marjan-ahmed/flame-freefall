---
type: Document
title: "PSI summary and matrix workbooks"
description: The spreadsheets held from NASA's PSI archive beside the experimental tables — test matrices, a CFI data summary, a SAME/SAME-R results workbook, and SAFFIRE image-downlink records — and what each does and does not contain.
status: draft
ksor:
  audience: [public]
  owner: human:you
order: 42
sources:
  - id: psi-workbook-inventory
    title: "Inventory of the PSI summary and matrix workbooks"
    resource: "Workbooks in psi-data/raw/summaries and psi-data/raw/matrices, as downloaded from the NASA Physical Sciences Informatics (PSI) archive for this project, inventoried sheet by sheet (name, row count, first row) in psi-data/derived/source-inventory.md"
---

> [!IMPORTANT]
> A workbook's file name does not say what is in it. The SAFFIRE "MergeResult"
> workbooks, for example, sound like merged results but hold only records of
> image files. Each workbook is described below by what its sheets actually
> contain.[^psi-workbook-inventory]

## Summaries (psi-data/raw/summaries)

### SAFFIRE MergeResult workbooks — image records, no combustion data

| File | Sheets | What the columns are |
| --- | --- | --- |
| SAFFIRE-1_MergeResult-jpeg_Update_Final_v2.xlsx | 12 | Timestamp, Time delta, Jpeg File Name, S1 / S2 / F1 / F2 Received and Rec'd Corrupt, Jpeg File size (bytes), Zip File Name, Zip File size (bytes) |
| SAFFIRE-II_MergeResult-jpeg_v5_Final.xlsx | 13 | EpochTime, Jpeg File ID (hex and decimal), Jpeg File Name, Received flags for BIT, F1 FV, F2 FV and samples S1 to S9, file sizes |
| SAFFIRE-III_MergeResult-jpeg_Final.xlsx | 6 | as SAFFIRE-II, for BIT, flow-visualization and sample images |
| SAFFIRE-III_MergeResult-raw_Final.xlsx | 7 | Requested and Received RAW image files; EpochTime, File Name, Exposure, Gain |

Every sheet lists image or archive files per camera and sample, with sizes and
received / corrupt flags. The largest sheets run to 38053 rows. None holds a
flame spread rate, O₂, flow or any other combustion measurement; the SAFFIRE
results are in the [SAFFIRE](../investigations/solid-fuel/saffire.md) reports.

### Combined SAMER Results 06 02 14.xlsx — SAME and SAME-R reduced results

43 sheets, most headed "SAME Combined Results | Smoke Generation |
Primary Diagnostics | Secondary Diagnostics Volume". They include per-material
sheets (DBP, Pyrell, Lampwick, Silicone, Teflon, Kapton — "R&T plots" and "V
plots"), reduced-data sheets ("Reduced data sheet", "Reduced Data with ISS
Det", "Reduced Data with STS Det", "REduced data MPASS", "REduced data mass
weighted"), "SAME R Results", "SAME1 Flight Tests 8-27-09", "SAME Ground Test
Results", ground verification and drum tests from August 2012 ("Gnd Verif.
8-2012", "Drum 8-2012", "3-tests Compar."), and sheets behind papers ("ICES
2012 Paper data table", "AIAA 2012 Paper data table", "IAASS Paper data
table"). It is the working results file behind [SAME](../investigations/smoke-aerosol/same.md)
and [SAME-R](../investigations/smoke-aerosol/same-r.md).

## Matrices (psi-data/raw/matrices)

| File | Sheets | What it is |
| --- | --- | --- |
| BASS test matrix.xlsx | "as run matrix", "2012", "2013", "Data without TP", "TP without Data" | the BASS matrix as run: date, test and sample numbers, material, igniter, Flow restrictor, Sample distance, Fan display, Air display, camera settings |
| CFI_DataSummary_Spreadsheet_Jan2021.xlsx | "Master Sheet", "DATA", "Camera Settings", "Igniter", "Comments", "Graphs" | the CFI test list, and in "DATA" per test: D0 ( mm ), Dext, hot ( mm ), khot ( mm^2/s ), kcool ( mm^2/s ), Dext,cool ( mm ), Reignitions, HF Burn Time — the CFI results the experimental table lacks |
| ACME Daily Test Point Log 2.xlsx | "ACME", "WITH IPSU2" | a downlink data log ("Downlink Data Limit (MB) = 127,000"), not test conditions |
| thermal precipitator map corrected 10-12-2011 (1).xlsx | three sheets | "SAME-R Thermal Precipitator Usage" |
| SAME VPRED Matrix PLN-005 Baseline.xls | — | older .xls format, not inventoried |
| BASS Test Matrix 050213.xlsx | — | not opened: contains account credentials |

## Open questions

- Which sheet of the Combined SAMER Results workbook is authoritative for
  which report table is not stated in the workbook.
- The SAME VPRED matrix is in the older .xls format and has not been
  inventoried, so its contents are not described.

[^psi-workbook-inventory]: Inventory of PSI workbooks (psi-data/derived/source-inventory.md). SAFFIRE-1_MergeResult-jpeg_Update_Final_v2.xlsx: sheets 'PreFlowVis - TimeSort', 'Sample1 - jpeg TimeSort', 'BIT - jpeg', 'Received - jpeg Corrupted'... first rows "Timestamp | Time delta | Jpeg File Name | S1 Received | S1 Rec'd Corrupt | Jpeg File size (bytes) | Zip File Name | Zips Received | Zip File size (bytes)". SAFFIRE-II_MergeResult-jpeg_v5_Final.xlsx: "BIT Received | F1 FV Received | F2 FV Received | S1 Received ... S9 Received"; "EpochTime | Time delta | Jpeg File ID (hex) | Jpeg File ID (decimal) | Jpeg File Name". SAFFIRE-III_MergeResult-jpeg_Final.xlsx: sheet 'Received - jpeg': 38053 rows. SAFFIRE-III_MergeResult-raw_Final.xlsx: "EpochTime | Time | File ID (hex) | File ID (decimal) | File Name | Exposure | Gain | BIT Received". Combined SAMER Results 06 02 14.xlsx: sheets 'DBP', 'Pyrell R&T plots', 'Lampwick V Plots', 'ICES 2012 Paper data table', 'AIAA 2012 Paper data table', 'IAASS Paper data table', 'Reduced data sheet', 'Reduced Data with ISS Det', 'REduced data mass weighted', 'REduced data MPASS', 'Reduced Data with STS Det', '3-tests Compar.', 'Drum 8-2012', 'Gnd Verif. 8-2012', 'SAME R Results', 'SAME1 Flight Tests 8-27-09', 'SAME Ground Test Results'; first row "SAME Combined Results | Smoke Generation | Primary Diagnostics | Secondary Diagnostics Volume". BASS test matrix.xlsx: sheets 'as run matrix', '2012', '2013', 'Data without TP', 'TP without Data'. CFI_DataSummary_Spreadsheet_Jan2021.xlsx: sheet 'DATA': "Flex Number | D0 ( mm ) | Dext, hot ( mm ) | khot ( mm^2/s ) | kcool ( mm^2/s ) | Dext,cool ( mm ) | Pressure (atm) | Reignitions | Extrap CF? | HF Burn Time". ACME Daily Test Point Log 2.xlsx: "Downlink Data Limit (MB) = 127,000". thermal precipitator map corrected 10-12-2011 (1).xlsx: "SAME-R Thermal Precipitator Usage". SAME VPRED Matrix PLN-005 Baseline.xls: format .xls (not inventoried). BASS Test Matrix 050213.xlsx: not opened: contains account credentials.
