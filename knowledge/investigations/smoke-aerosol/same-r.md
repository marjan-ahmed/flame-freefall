---
type: Document
title: "SAME-R: Smoke Aerosol Measurement Experiment Re-flight"
description: The 2010 re-flight of SAME — new material (Pyrell), higher sample temperatures and no-flow runs, a new two-moment detector, and ground tests that check the moment method — from the SAMER final report.
status: stable
generated: { by: "claude-code/opus-5.5", at: 2026-09-24T07:55:18Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-24T07:55:18Z }
order: 31
geometry_class: smoke-aerosol
verified:
  - by: "human:muhammad-marjan-ahmed"
    at: 2026-09-24T07:55:18Z
sources:
  - id: samer-final-report
    title: "Smoke Aerosol Measurement Experiment Re-flight (SAMER) — Final Report, June 2, 2014"
    resource: "SAMER final report by David L. Urban, Gary A. Ruff, William Sheredy, Marit Meyer (NASA Glenn), Thomas Cleary, Jiann Yang (NIST), George Mulholland (University of Maryland) and Zeng-Guang Yuan (NCSER), covering 01 November 2000 - June 2, 2014, with appendices including the paper 'Particle Morphology and Size Results from the Smoke Aerosol Measurement Experiment-2'; distributed in the NASA Physical Sciences Informatics (PSI) archive as 'SAMER_Final 0602 2014.pdf'"
---

> [!NOTE]
> Geometry class: **smoke / aerosol** — heated, non-burning samples; not
> comparable with any flame measurement. This is the re-flight of
> [SAME](same.md), on the same hardware.

> [!IMPORTANT]
> The report's own results section is largely excerpts from an attached paper
> on SAME-2, and it says so: "Below are excerpts from the relevant part of the
> paper." Statements attributed below to that paper are marked as such.

SAMER was one of the Rapid Turn Around (RTA) projects solicited by NASA
Headquarters in June 2009, extending SAME, which ran in the Microgravity
Science Glovebox (MSG) on the International Space Station (ISS) from
September 9 to October 5, 2007. SAME's apparatus worked, but "all the TEM
grids were severely contaminated with some unidentified foreign particles,
making these grids unusable". SAMER re-flew the hardware with reloaded sample
carousels, 30 extra loose samples and rebuilt thermal precipitators.[^samer-final-report]

## What changed from SAME

1. A new test material, **Pyrell**, an intumescent fire-retardant foam by
   Foamex, replaced the DBP samples.
2. Test conditions were broadened to higher heating temperatures and **no flow**
   during sample heating.
3. A new instrument, **M-pass** (developed in-house at GRC), replaced one of the
   two Commercial Diagnostic Enclosures used in SAME.

Two data-reduction changes followed: each test is characterized by a derived
**sample heating temperature** instead of Rt/R0 (the ratio of heated-wire
resistance to room-temperature resistance), because "for the same Rt/R0, the
actual heating temperature difference can be as large as 30 degrees Celsius";
and a method to estimate the fraction of a cumulative moment an instrument with
a limited size range can see.[^samer-final-report]

## Structured facts

Every value below is drawn from the single source cited throughout this
document.

### Experimental conditions

| Field | Value |
| --- | --- |
| Facility | Microgravity Science Glovebox (MSG), ISS |
| Flight tests | July 16, to September 9, 2010 |
| Test points completed | 66 |
| Baseline air flow | 8 cm/s, with runs down to 2 cm/s and a limited set with no airflow while the sample was heated (per the appended paper) |
| Baseline sample temperature | chosen to produce 1 to 2 mg of weight loss in 60 seconds (per the appended paper) |
| Post-flight ground tests | apparatus flow tests (dilution ratios), 1-g TEM tests under the flight conditions, SMPS tests of the lognormal assumption |
| Measured flight flow rates after return | DustTrak B 1.69076 LPM; Mpass 1.68576 LPM |

### Sample heating temperatures for the TEM-analysed flight tests (source Table 2)

| Sample | Temperature, °C | Particles counted (TEM) |
| --- | --- | --- |
| Lampwick #54 (ISS) Unaged | Low Temp 264.7 | 511 |
| Lampwick #55 (ISS) Aged | Low Temp 262.9 | 196 |
| Kapton #94 (ISS) Aged | Low Temp 527.3 | 1353 |
| Kapton #62 (ISS) Unaged | High Temp 574.3 | 1320 |
| Kapton #62 (ISS) Aged | High Temp 574.3 | 796 |
| Pyrell #63 (ISS) Unaged | Low Temp 225.3 | 3436 |
| Pyrell #63 (ISS) Aged | Low Temp 225.3 | 2658 |
| Pyrell #64 (ISS) Unaged | High Temp 242.1 | 1888 |
| Pyrell #64 (ISS) Aged | High Temp 242.1 | 1560 |
| Silicone #60 (ISS) Unaged | High Temp 379.9 | 557 |

The same table's diameter columns (TEM vs moment-method) are not reproduced:
their headers did not survive text extraction legibly.

## Findings

- The abstract concludes that "the moment method in conjunction the lognormal
  distribution assumption is a valid and effective approach to
  characterization of the aerosol encountered in space vehicles", and that
  particle size distributions of aerosol from 5 tested materials were
  identified.[^samer-final-report]
- The appended paper reports that for typical runs "the particle
  concentrations were a few million particles / cc and the mass concentrations
  were 2 to 15 mg/m3", and that with more rigorous assembly controls "numerous
  good particle images were obtained" on the SAME-2 TEM grids.
- Its conclusions: all samples produced significant numbers of sub-micron
  particulate readily detected by an ionization smoke detector; aging can grow
  some smoke (e.g. silicone rubber) to sizes better detected by light
  scattering; "The zero flow conditions produced smoke particles that were 2 to
  3 times larger than those produced at the nominal 8 cm/s flow rate"; and the
  prototype 2-moment detector (MPASS) was "very encouraging" for broad-range
  detection with fewer false alarms.[^samer-final-report]

## Open questions

- **Sample count.** The abstract reports 66 test points; the excerpted paper
  says "Over 100 sample materials were tested" across 6 materials including
  dibutyl-phthalate, while the report says Pyrell replaced DBP. The paper
  likely counts both flights together, but the report does not say so; both
  statements are kept.
- The derived heating temperatures for every test (not only those in Table 2)
  are in the report's appendices, not reproduced here.
- The report's reference to the SAME-2 paper is left as "[ref. xx]" in the
  source.

[^samer-final-report]: SAMER Final Report (Urban, Ruff, Sheredy, Meyer, Cleary, Yang, Mulholland, Yuan; June 2, 2014). Abstract: "Smoke Aerosol Measurement Experiment Re-flight (SAMER) is an extension or continuation of Smoke Aerosol Measurement Experiment (SAME), conducted in space from September 9 to October 5, 2007... 1) a new test sample material Pyrell®, an intumescent fire-retardant foam by Foamex was introduced to replace DBP samples, 2) test condition ranges was extended to include higher heating temperature and no-flow conditions, and 3) a new instrument, M-pass, developed in-house GRC, was used to replace one of the two Commercial Diagnostic Enclosures used in SAME. SAMER flight tests were conducted from July 16, to September 9, 2010, successfully completing 66 test points... it is concluded that the moment method in conjunction the lognormal distribution assumption is a valid and effective approach to characterization of the aerosol encountered in space vehicles. Particle size distributions of aerosol produced from 5 tested materials commonly found in space crafts were identified." Introduction: "SAMER is one of the awarded Rapid Turn Around (RTA) projects, solicited by NASA Headquarters in June 2009... all the TEM grids were severely contaminated with some unidentified foreign particles, making these grids unusable... SAME-R utilized the SAME hardware already on orbit with reloaded sample carousels, 30 extra loose samples, rebuilt thermal precipitators." SAMER results (excerpts from the SAME-2 paper): "Over 100 sample materials were tested... The baseline air flow rate was 8 cm/s with runs conducted at rates down to 2 cm/s with a limited set conducted with no airflow while the sample was heated... The baseline temperature was selected to produce 1 to 2 mg of weight loss in 60 seconds... For SAME-2 more rigorous assembly controls were followed and numerous good particle images were obtained. For typical runs, the particle concentrations were a few million particles / cc and the mass concentrations were 2 to 15 mg/m3." Flow tests: "The total flow rate of Flight unit DustTrak B (used in SAMER) is later found to be 1.69076 LPM. The total flow rate of Flight unit Mpass (used in SAMER) is later found to be 1.68576 LPM." Sample heating temperature derivation: "for the same Rt/R0, the actual heating temperature difference can be as large as 30 degrees Celsius." Table 2 (Flight Data Comparison of TEM and Moment Method Distribution Parameters), Sample / Temperature, °C / # particles counted: Lampwick #54 (ISS) Unaged, Low Temp 264.7, 511; Lampwick #55 (ISS) Aged, Low Temp 262.9, 196; Kapton #94 (ISS) Aged, Low Temp 527.3, 1353; Kapton #62 (ISS) Unaged, High Temp 574.3, 1320; Kapton #62 (ISS) Aged, High Temp 574.3, 796; Pyrell #63 (ISS) Unaged, Low Temp 225.3, 3436; Pyrell #63 (ISS) Aged, Low Temp 225.3, 2658; Pyrell #64 (ISS) Unaged, High Temp 242.1, 1888; Pyrell #64 (ISS) Aged, High Temp 242.1, 1560; Silicone #60 (ISS) Unaged, High Temp 379.9, 557. Appendix F conclusions: "The zero flow conditions produced smoke particles that were 2 to 3 times larger than those produced at the nominal 8 cm/s flow rate... The results from the prototype 2-moment detector (MPASS) were very encouraging."
