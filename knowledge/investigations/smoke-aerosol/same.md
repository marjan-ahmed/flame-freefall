---
type: Document
title: "SAME: Smoke Aerosol Measurement Experiment"
description: Size distributions of smoke from overheated (not burning) spacecraft materials, measured in the ISS Microgravity Science Glovebox in 2007, from the SAME final report.
status: stable
generated: { by: "claude-code/opus-5.5", at: 2026-09-24T07:55:18Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-24T07:55:18Z }
order: 30
geometry_class: smoke-aerosol
verified:
  - by: "human:muhammad-marjan-ahmed"
    at: 2026-09-24T07:55:18Z
sources:
  - id: same-final-report
    title: "Smoke Aerosol Measurement Experiment (SAME) — Final Report, November 1, 2000 - April 14, 2009"
    resource: "SAME final report by David L. Urban, Gary A. Ruff, William Sheredy (NASA Glenn), Thomas Cleary, Jiann Yang (NIST), George Mulholland (University of Maryland) and Zeng-Guang Yuan (NCSER), dated March 15, 2010, with conference papers attached; distributed in the NASA Physical Sciences Informatics (PSI) archive as 'SAME Final Science report  03 18 10 with papers attached.pdf'"
---

> [!NOTE]
> Geometry class: **smoke / aerosol**. SAME heated samples to temperatures
> below the ignition point to make smoke; nothing burned. Its results are
> about smoke particle sizes for fire *detection*, and are not comparable with
> any flame measurement in the solid-fuel, droplet or gaseous-flame
> investigations. Its re-flight is [SAME-R](same-r.md).

> [!IMPORTANT]
> The source is the project's final report with several conference papers
> attached as appendices. This entry uses the report body (abstract, flight
> tests, results, closing remarks); the attached papers are not summarized
> here.

Early detection of an overheat event or fire lets a spacecraft crew respond
before the hazard gets out of control, and the limited response options make
earlier detection more important than on Earth. SAME characterized the size
distribution of smoke particulate produced in low gravity from overheated
spacecraft materials, in the Microgravity Science Glovebox (MSG) on the
International Space Station (ISS), to inform the design of next-generation
smoke detectors.[^same-final-report]

## Why it was run

An earlier Space Shuttle glovebox project, Comparative Soot Diagnostics (CSD),
suggested that particles generated in low gravity tend to be larger than on
Earth, but its results "were not conclusive" and it could not measure particle
size distributions on orbit. SAME was designed to obtain that data. Because
the MSG is too small for laboratory aerosol instruments, a new procedure — the
**moment method** — measures three moments of the size distribution (the
zeroth, first and third) with small instruments, and infers the total number
concentration, the geometric mean diameter and the geometric standard
deviation, assuming a lognormal distribution.[^same-final-report]

## Structured facts

Every value below is drawn from the single source cited throughout this
document.

### Experimental conditions

| Field | Value |
| --- | --- |
| Facility | Microgravity Science Glovebox (MSG), ISS, Expedition 15 |
| Flight tests | September and early October of 2007 |
| Samples | 30: six samples each of 5 materials |
| Materials | Teflon, Kapton, silicone rubber, cellulose (lamp wick); dibutyl-phthalate (DBP) on a cotton wick as a reference |
| Heating | samples heated to temperatures below the ignition point |
| Air flow | air flow rates ranging from 2 to 8 cm/s |
| Aging (simulated transport time) | smoke held in an aging chamber from 10 seconds to 1800 seconds |
| Instruments digitized at | 1 Hz, 8 bit A/D converter |
| Detectors compared | ISS and space shuttle smoke detectors built into the apparatus |

### Measured outcomes (source Table 1, "Results of SAME flight tests")

| Sample | (nm) | (nm) | (nm) | σg |
| --- | --- | --- | --- | --- |
| Kapton | 80 | 105 | 179 | 2.08 |
| Kapton aged | 155 | 186 | 267 | 1.82 |
| Lamp wick | 186 | 227 | 341 | 1.89 |
| Lamp wick aged | 258 | 308 | 438 | 1.81 |
| Silicone | 189 | 257 | 472 | 2.18 |
| Silicone aged | 352 | 422 | 606 | 1.83 |
| Teflon | 170 | 205 | 297 | 1.84 |
| Teflon aged | 228 | 273 | 392 | 1.82 |

The three diameter columns are reproduced with the headers exactly as the
source prints them (see Open questions).

## Findings

- For the materials tested, "a substantial portion of the smoke particles are
  below 500 nm in diameter".[^same-final-report]
- Teflon and Kapton particles are very small, with narrow size distributions
  and little mass in particles larger than 1 μm; the lamp wick and silicone
  results show substantially larger diameters of average mass. Aging
  substantially increases average particle sizes, "rising to over 1 m for the
  aged silicone diameter of average mass".
- Although the CMD for silicone rubber is 189 nm, "almost half the particle
  mass is larger than 1 m", as shown by the ratio of the two DustTrak
  instruments; lamp wick behaves similarly.
- The space shuttle (ionization) detector gave strong signals in all tests;
  the ISS detector was more erratic for Teflon smoke — "the smoke detectors
  used in STS and ISS have different response to particle size range".
- The smoke transport model showed that mixing dominates smoke transport, so
  detection time lags are longer than in normal gravity.
- Closing remark: detecting smoke across the size range seen in SAME and CSD
  while still discriminating against dust "will probably require a detection
  system that can discriminate the particle size distribution to at least a
  limited degree".[^same-final-report]

## Open questions

- **Which diameter is which in Table 1.** The text above the table reads
  "Geom.Mean Diam. Arithmetic Mean Diam." and the words "Diam. of Average
  Mass" appear after it, but the source does not label the three (nm) columns
  individually. The body text gives a count mean diameter (CMD) for silicone
  rubber of 189 nm, the value in the first column. The column-to-name mapping
  is therefore not stated unambiguously and is left open here.
- The "1 m" in the source's findings is presumably 1 μm (the μ symbol appears
  elsewhere in the same text), but the source prints it as written here.
- The TEM grids "were unfortunately contaminated with extraneous particles";
  how that affects any TEM-based size result is not quantified in the report
  body.
- Per-test conditions (sample temperature, flow, aging time) for each of the
  30 samples are in the report's Appendix A chronology, not reproduced here.

[^same-final-report]: SAME Final Report (Urban, Ruff, Sheredy, Cleary, Yang, Mulholland, Yuan; March 15, 2010). Abstract: "This report describes the outcomes of the Smoke Aerosol Measurements Experiment (SAME), an experiment conducted in the Microgravity Science Glovebox (MSG) on the International Space Station (ISS) to characterize the size distribution of smoke particulate produced in low-gravity from a variety of overheated spacecraft materials... the preliminary results of CSD project were not conclusive... Therefore, a new procedure was developed, the moment method... The SAME experiments were conducted during Expedition 15 on the ISS. Four materials, typical of those found in spacecraft, were tested including cellulose (lamp wick), Kapton, silicone rubber, and Teflon. A fifth material, dibutyl-phthalate (DBP) retained in a cotton wick was used as a reference... samples were heated to temperatures below the ignition point... holding the smoke in an aging chamber for times ranging from 10 seconds to 1800 seconds... The experimental results show that, for the materials tested, a substantial portion of the smoke particles are below 500 nm in diameter. The smoke transport model demonstrated that mixing dominates the smoke transport and that consequently detection time lags are longer than in normal gravity." §3 SAME Experiment: "measuring three moments of the size distribution (the zeroth, first and third moment)... the total number concentration, Nt, the geometric mean diameter, Dg, and the geometric standard deviation... air flow rates ranging from 2 to 8 cm/s." §4 Flight Tests: "The SAME tests were performed on board ISS in September and early October of 2007. Overall 30 sample materials were tested. These were comprised of six samples each of 5 materials." §5 Test Results: "digitized at 1 Hz by an 8 bit A/D converter... This shows that the smoke detectors used in STS and ISS have different response to particle size range... The aging results show substantial increase in the average particle sizes with them rising to over 1 m for the aged silicone diameter of average mass... although the CMD for silicone rubber is 189 nm, almost half the particle mass is larger than 1 m... The TEM grids recovered from the thermal precipitators were unfortunately contaminated with extraneous particles." Table 1 (Results of SAME flight tests; header "Geom.Mean Diam. Arithmetic Mean Diam."): Kapton 80 105 179 2.08; Kapton aged 155 186 267 1.82; Lamp wick 186 227 341 1.89; Lamp wick aged 258 308 438 1.81; Silicone 189 257 472 2.18; Silicone aged 352 422 606 1.83; Teflon 170 205 297 1.84; Teflon aged 228 273 392 1.82. §6 Closing Remarks: "detection of smoke across the size range seen in SAME and CSD, while still discriminating against dust (which tends to be large), will probably require a detection system that can discriminate the particle size distribution to at least a limited degree."
