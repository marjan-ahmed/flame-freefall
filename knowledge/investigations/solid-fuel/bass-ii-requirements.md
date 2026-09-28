---
type: Document
title: "BASS-II: Science Requirements and Sample Manifest"
description: What BASS-II was required to test and measure, its success criteria and its flight sample manifest, from the BASS-II science requirements briefing (2010) — the plan behind the BASS-II Summary Report.
status: stable
generated: { by: "claude-code/opus-5.5", at: 2026-09-24T07:55:18Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-24T07:55:18Z }
order: 33
geometry_class: solid-fuel
verified:
  - by: "human:muhammad-marjan-ahmed"
    at: 2026-09-24T07:55:18Z
sources:
  - id: bass-ii-srd
    title: "BASS-II Science Requirements (briefing charts)"
    resource: "BASS-II science requirements, success criteria, hardware manifest and science overview charts (pages dated 4/14/2010, 10/28/2013 and 6/6/2023); distributed in the NASA Physical Sciences Informatics (PSI) archive as 'SRD_BASS-II.pdf'"
---

> [!NOTE]
> Geometry class: **solid fuel**. This is the planning companion to
> [BASS-II](bass-ii.md), whose summary report gives the results; read that
> document for what was found.

> [!IMPORTANT]
> The source is a set of briefing charts, not a report: requirements and
> plans. It says what BASS-II set out to do, not what happened.

BASS-II "tests the hypothesis that materials in microgravity, with adequate
ventilation, burn as well if not better than the same material in normal
gravity with other conditions being identical (pressure, oxygen concentration,
temperature, etc.)". It reused the on-orbit BASS hardware launched originally
for SPICE on STS-126.[^bass-ii-srd]

## Objectives

- To identify what is the worst case for material flammability in spacecraft
  environments, and how that compares to the terrestrial upward burning used
  to screen materials for safe use aboard spacecraft.
- To determine how quickly a fire in space can grow and if the flames reach a
  finite size or continue to grow — with implications for firefighting
  strategies in spacecraft.

Primary variables: ambient oxygen concentration, ventilation flow velocity,
and fuel type, thickness, and geometry.[^bass-ii-srd]

## Requirements

- **Samples**: 20 samples for each of the 5 PIs.
- **Measurements**: the GN2 flow rate, fan voltage, air flow velocity and
  direction, and flame radiation are measured and **overlaid on the Video**;
  acquisition rate 4 Hz, unchanged from SPICE/BASS; accuracy ±10%.
- **MSG working-volume gas**: a Compound Specific Analyzer (CSA-CP) and a CO2
  sensor (CDM) read the oxygen concentration before and after each burn.
- **Acceleration**: testing scheduled around thruster firing or docking, with
  the environment measured by a nearby SAMS.[^bass-ii-srd]

### Success criteria

| Level | Criterion |
| --- | --- |
| Minimal success | 10 samples from each PI (of their total 20) successfully tested at the desired test conditions (O2, flow), with ignition, flame video, and still camera data for at least 7 tests per PI |
| Complete success | All PI samples (100) tested at the desired conditions, video for all tests, ignition in most of the tests (90+), extinction observed for tests that seek a flammability limit, still camera data for most tests (90+) |

### Team (science overview chart)

| Role | Name |
| --- | --- |
| PS | Dr. Paul Ferkul, NCSER |
| PI | Dr. Sandra Olson, NASA GRC |
| Co-PI | Prof. Subrata Bhattacharjee, SDSU |
| Co-PI | Prof. James T'ien, CWRU |
| Co-PI | Prof. Fletcher Miller, SDSU |
| Co-PI | Prof. Carlos Fernandez-Pello, UCB |

### Flight sample manifest (new designs)

| Samples | Count |
| --- | --- |
| Flat 2 cm PMMA, 0.1 mm thick | 8 |
| Flat 2 cm PMMA, 0.2 mm thick | 4 |
| Flat 1 cm PMMA, 0.2 mm thick | 4 |
| Black PMMA rods, 0.25" diameter | 14 |
| Black PMMA rods, 0.375" diameter | 6 |
| Black PMMA rods, 0.500" diameter | 2 |
| Clear PMMA rods, 0.25" diameter | 12 |
| Clear PMMA rods, 0.375" diameter | 4 |
| Clear PMMA rods, 0.500" diameter | 2 |
| Sphere Sample 4 cm | 1 |

Previously flown designs on the manifest: 15 SIBAL Samples (2 cm wide), 4 SIBAL
Samples (1 cm wide), 3 NOMEX Samples (2 cm wide); plus thicker flat PMMA
samples of several thicknesses, one or two of each.[^bass-ii-srd]

## Open questions

- **Flow velocities per test.** The requirements put air flow velocity on the
  video overlay. The PSI experimental table for BASS-II records control-panel
  readings instead (see [the PSI experimental tables](../../data-sources/psi-experimental-tables.md));
  per-test velocities in cm/s would have to be read from the video, which this
  record does not contain.
- The requirements count 5 PIs; the [BASS-II](bass-ii.md) summary report's
  Appendix A has six per-PI test matrices, including one for Ferkul, listed
  here as project scientist.
- The chart pages carry three different dates (4/14/2010, 10/28/2013,
  6/6/2023); which revision this is, is not stated.

[^bass-ii-srd]: BASS-II Science Requirements charts. Requirements (4/14/2010): "20 samples for each of the 5 PIs... Measurement of the GN2 flow rate, fan voltage, air flow velocity and direction, and flame radiation will be measured and overlaid on the Video. The acquisition rate of 4 Hz can not be changed from SPICE/BASS. The measurement accuracy of ±10%... BASS-II testing will be scheduled around planned thruster firing or spacecraft dock or undock. The acceleration environment will be measured by a nearby SAMS... install a Compound Specific Analyzer (CSA-CP) and the CO2 sensor (CDM) into the MSG to measure the Oxygen concentration." Success criteria: "Minimal Success: 10 samples from each PI (of their total 20) will be successfully tested per PI matrices at the desired test conditions (O2, flow)... Still camera data is obtained for at least 7 tests per PI... Complete Success: All PI samples (100) are tested at the desired test conditions. Video data is obtained for all tests. Ignition occurs in most of the tests (90+). Extinction is observed for tests that seek to find a flammability limit. Most of the tests (90+) provide still camera data." Hardware manifest (6/6/2023): "15 SIBAL Samples (2 cm wide)... 4 SIBAL Samples (1 cm wide)... 3 NOMEX Samples (2 cm wide)... 8 Flat 2 cm PMMA Samples (0.1 mm thick)... 4 Flat 2 cm PMMA Samples (0.2 mm thick)... 4 Flat 1 cm PMMA Samples (0.2 mm thick)... 14 Black PMMA Rod Samples (0.25" Diameter)... 6 Black PMMA Rod Samples (0.375" Diameter)... 2 Black PMMA Rod Samples (0.500" Diameter)... 12 Clear PMMA Rod Samples (0.25" Diameter)... 4 Clear PMMA Rod Samples (0.375" Diameter)... 2 Clear PMMA Rod Samples (0.500" Diameter)... 1 Sphere Sample 4 cm." Science overview: "PS: Dr. Paul Ferkul, NCSER; PI: Dr. Sandra Olson, NASA GRC; Co-PI: Prof. Subrata Bhattacharjee, SDSU; Co-PI: Prof. James T'ien, CWRU; Co-PI: Prof. Fletcher Miller, SDSU; Co-PI: Prof. Carlos Fernandez-Pello, UCB... Burning and Suppression of Solids - II (BASS-II) tests the hypothesis that materials in microgravity, with adequate ventilation, burn as well if not better than the same material in normal gravity with other conditions being identical (pressure, oxygen concentration, temperature, etc.). Objectives: To identify what is the worst case for material flammability in spacecraft environments, and how does that compare to the terrestrial upward burning used to screen the materials for safe use aboard spacecraft. To determine how quickly a fire in space can grow and if the flames reach a finite size or continue to grow... BASS-II will utilize the on orbit BASS hardware launched originally for SPICE on STS-126."
