---
type: Document
title: "NASA PSI data behind this record"
description: What this record holds from NASA's Physical Sciences Informatics (PSI) archive — experimental tables, summary and matrix workbooks, and final reports — and where each is described.
status: stable
generated: { by: "claude-code/opus-5.5", at: 2026-09-24T07:55:18Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-24T07:55:18Z }
order: 40
sources:
  - id: psi-file-inventory
    title: "Inventory of the PSI files held for this project"
    resource: "Files downloaded from the NASA Physical Sciences Informatics (PSI) archive for the Flame in Freefall project, inventoried file by file (name, row counts, column headers, workbook sheets) in psi-data/derived/source-inventory.md"
  - id: thriving-in-space-2023
    title: "Thriving in Space: Ensuring the Future of Biological and Physical Sciences Research: A Decadal Survey for 2023-2032"
    resource: "https://doi.org/10.17226/26750"
---

The Physical Sciences Informatics (PSI) data repository "was opened in 2015
and contains most of the original data (including images and videos) from
experiments in reduced-gravity environments such as the ISS, space shuttle
flights, and free-flyers"; it is open access so that investigators can
reanalyze data in new ways, and NASA funds 2-year projects that use it.[^thriving-in-space-2023]

For each combustion investigation this record covers, the files held from PSI
are some mix of three kinds, and each kind is described in its own document
here:[^psi-file-inventory]

| Kind | What it is | Described in |
| --- | --- | --- |
| Experimental tables | one table per investigation (two for some), one row per test, test point, day or planned fuel | [PSI experimental tables](psi-experimental-tables.md) |
| Summary and matrix workbooks | spreadsheets kept by the flight teams: test matrices, reduced results, image downlink records | [PSI summary and matrix workbooks](psi-summary-workbooks.md) |
| Reports | final reports, science requirements documents, a conference poster, a data layout document | the investigation documents under [investigations](../investigations/) |

## How the record uses these files

- **Reports** are the sources of the investigation documents: each document
  names its report in its sources, and every value in it has been checked
  against that report's text.
- **Experimental tables** are catalogued here — what each row is, which
  columns it has, and what it does not record — so a reader knows what the
  per-test data can and cannot answer before using it.
- **Workbooks** are catalogued with the same care, including the ones that
  turn out to hold no combustion measurements at all.

## What is deliberately not described

One matrix workbook, "BASS Test Matrix 050213.xlsx", was never opened for
this record: it contains account credentials in its first row. The BASS tests
it plans are covered by the BASS experimental table and the
[BASS](../investigations/solid-fuel/bass.md) document.[^psi-file-inventory]

## Open questions

- The PSI archive's own record pages (investigation descriptions, dataset
  URLs) are not part of the files held here, so no document links to a PSI
  web page; datasets are identified by their PSI numbers (for example PSI-25)
  as they appear in the file names.

[^psi-file-inventory]: Inventory of PSI files (psi-data/derived/source-inventory.md): "Experimental tables (psi-data/raw/csvs)"; "Workbooks (psi-data/raw/matrices)"; "Workbooks (psi-data/raw/summaries)"; "Reports (psi-data/raw/reports)"; "BASS Test Matrix 050213.xlsx — not opened: contains account credentials".

[^thriving-in-space-2023]: Thriving in Space (2023 decadal survey), Informatics Platforms and Data Repositories: "The Physical Sciences Informatics (PSI) data repository was opened in 2015 and contains most of the origi- nal data (including images and videos) from experiments in reduced-gravity environments such as the ISS, space shuttle flights, and free-flyers. PSI also includes data from some related ground-based studies. This open access repository allows for investigators to reanalyze data in new ways. To support these efforts, NASA has an annual funding call for 2-year projects that use the PSI."
