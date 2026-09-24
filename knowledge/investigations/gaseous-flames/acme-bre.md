---
type: Document
title: "ACME BRE: Burning Rate Emulator"
description: Gas-fed porous burners that emulate burning condensed materials in quiescent microgravity, tested on the ISS in 2019-2021 in the exploration atmospheres NASA proposed, from the ACME/BRE final report.
status: draft
ksor:
  audience: [public]
  owner: human:you
order: 27
geometry_class: gaseous-flames
sources:
  - id: acme-bre-final-report
    title: "Advanced Combustion via Microgravity Experiments (ACME) Burning Rate Emulator (BRE) — ACME/BRE Final Report (2022)"
    resource: "ACME/BRE final report prepared by Dennis P. Stocker (NASA Glenn), James G. Quintiere and Peter B. Sunderland (University of Maryland), John L. de Ris (FM Global, retired) and Parham Dehghani (University of Maryland), dated 1 Feb. 2022; distributed in the NASA Physical Sciences Informatics (PSI) archive as 'BRE_final_report_20220201.pdf'"
---

> [!NOTE]
> Geometry class: **gaseous flames** — a gaseous fuel mixture issues from a
> flat porous burner. The point of BRE is that this gas flame *emulates* a
> burning condensed material (a "heat of gasification" is inferred), so its
> findings speak to solids like PMMA; but the flames themselves are gas-fed
> and are compared here only with the other [ACME](acme.md) experiments, not
> directly with solid-fuel tests ([BASS-II](../solid-fuel/bass-ii.md),
> [SAFFIRE](../solid-fuel/saffire.md)).

> [!IMPORTANT]
> The report marks its own results as **preliminary**: "While BRE's results
> are still preliminary". Every finding below carries that status.

BRE is one of six independent experiments in the Advanced Combustion via
Microgravity Experiments (ACME) project, run in the Combustion Integrated Rack
(CIR) on the International Space Station (ISS). Principal Investigator: Prof.
James G. Quintiere (University of Maryland); the two co-investigators are
Prof. Peter B. Sunderland and Dr. John L. de Ris; the project scientist is
Dennis P. Stocker (NASA Glenn).[^acme-bre-final-report]

## Objectives

From the experiment's June 2013 Science Requirements Document: (1) observe
burning behavior in long-duration microgravity for CH4/N2 and C2H4/N2 mixtures
on porous circular burners of 25 and 50 mm diameter, in O2/N2 ambients —
including the NASA-considered atmospheres "14.7 psia, 21 % oxygen: 10.2 psia,
26.5 %; and 8.2 psia, 34 % oxygen"; (2) the same in O2/CO2 ambients (desired);
(3) extinction limits under those conditions. NASA effectively limited the
experiment to objectives 1 and 3; two of the three were accomplished.[^acme-bre-final-report]

## Structured facts

Every value below is drawn from the single source cited throughout this
document.

### Experimental conditions

| Field | Value |
| --- | --- |
| Facility | Combustion Integrated Rack (CIR), ISS |
| Round 1 | Increments 58-59, Feb. to April 2019 — ethylene and the 25-mm burner only |
| Round 2 | Increments 63-64, Sept. 2020 to Jan. 2021 — also methane and the 50-mm burner (not together) |
| Burners | porous circular, 25 and 50 mm diameter |
| Atmospheres targeted | 14.7 psia / 21 % O₂; 10.2 psia / 26.5 % O₂; 8.2 psia / 34 % O₂ |
| Air flow | none — quiescent ambient |

### Example tests reported in the results section

| Test | Fuel | Mass flux | O₂ | Pressure | Heat of gasification L | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| 19056F1 | ethylene/N2, hc = 24 kJ/g | 4.55 g/m2s | 27% | 10.2 psia | 0.66 kJ/g | extinction at 45 s |
| 19070K1 | ethylene/N2, hc = 24 kJ/g | 2.3 g/m2s | 26.5% | 10.2 psia | 3.0 kJ/g | steady |
| 19070D1 | ethylene/N2 (see Open questions) | 4.95 g/m2s | 34% | 8.2 psia | 2.42 kJ/g | steady |

## Findings

The report's list of surprises and new discoveries:[^acme-bre-final-report]

1. Quasi-steady burning on a flat surface, representing a pool fire, can exist
   in microgravity; ambient O₂ matters most — quasi-steady flames were observed
   for nominal ambient oxygen mole fractions of 0.265 and above.
2. Ambient pressure has a weak effect on burning quality but changes
   radiative loss through the partial pressures of H2O and CO2.
3. Methane/nitrogen flames self-extinguished within a minute for all ambient
   conditions — burn time depends on fuel chemistry.
4. Ethylene flames, which soot in normal gravity, did not soot in
   microgravity except briefly at ignition.
5. Radiative loss fraction in microgravity can reach about 60% compared to
   30% for normal-gravity flames.
6. Thin-filament pyrometry (TFP) of four flames confirmed a critical
   temperature range for extinction of 1100 to 1200 K.
7. The BRE can emulate several liquids and solids, including Acetone,
   Ethanol, Methanol, PMMA, Nylon and Phenolic glass fiber.
8. For the first time, two limits of extinction were obtained on a plot of
   heat of combustion vs. heats of gasification: radiative extinction for
   large flames and another limit for small flames.

On test 19070K1 (26.5% O₂, 10.2 psia) the report says the emulation
"could represent PMMA as a material solid. This is a profound result indicating
a common plastic could steadily burn under these NASA proposed atmospheric
conditions." Its impact statement adds that this continued burning without
air flow — where stopping ventilation is an established step in putting out
spacecraft fires — was seen in the elevated-oxygen atmospheres being
considered for future spacecraft, while such flames in 21% oxygen
self-extinguished in a short time. It suggests NASA "may want to increase use
of its alternative flammability Test 2, with the cone calorimeter".[^acme-bre-final-report]

## Open questions

- **Heat of combustion for test 19070D1.** The Figure 9 caption gives
  hc = 24 kJ/g; the Figure 10 caption for the same test gives hc = 22 kJ/g.
  The source does not reconcile them; both are kept.
- The results are preliminary by the report's own statement; a revised
  analysis is not part of this source.
- Several BRE radiometers saturated in round 1, so the radiative loss data set
  "is limited"; which tests are affected is not listed in the sections used
  here.
- How BRE's no-flow burning relates to the [NASA-STD-6001B](../../foundations/nasa-std-6001b.md)
  tests is the report's suggestion, not a finding.

[^acme-bre-final-report]: ACME/BRE Final Report (Stocker, Quintiere, Sunderland, de Ris, Dehghani; 1 Feb. 2022). §1 Overview: "The Burning Rate Emulator (BRE) experiment is one of six independent experiments that make up the Advanced Combustion via Microgravity Experiments (ACME) project for which tests are conducted within the Combustion Integrated Rack (CIR) on the International Space Station (ISS)... The ISS operations were conducted in two separate rounds of testing during Increments 58-59 and 63-64... the first round of testing was conducted from Feb. to April 2019, while the second-round testing occurred from Sept. 2020 to Jan. 2021. The first round of tests was limited to ethylene and the 25-mm BRE burner, while the second round also included tests with methane and the 50-mm burner (although not together)." §2.C Science Objectives (SRD, June 2013): "Observe burning behavior in long-duration microgravity for CH4/N2 and C2H4/N2 mixtures on porous circular burners of 25 and 50 mm diameter... NASA- considered atmosphere for human space missions will be examined: 14.7 psia, 21 % oxygen: 10.2 psia, 26.5 %; and 8.2 psia, 34 % oxygen." §4.C Summary of Preliminary Results: "Flame growth from ignition to self-extinction in test 19056F1. The conditions are ethylene/N2, hc = 24 kJ/g, 4.55 g/m2s, 27% O2, 10.2 psia, L = 0.66 kJ/g, extinction at 45 s... test 19070K1. The conditions are ethylene/N2, hc = 24 kJ/g, 2.3 g/m2s, 26.5% O2, 10.2 psia, L = 3.0 kJ/g, steady... As such it could represent PMMA as a material solid. This is a profound result indicating a common plastic could steadily burn under these NASA proposed atmospheric conditions... test 19070D1. The conditions are ethylene/N2, hc = 24 kJ/g, 4.95 g/m2s, 34% O2, 8.2 psia, L = 2.42 kJ/g, steady" (Figure 9); "4.95 g/m2s, 34% O2, 8.2 psia, L = 2.42 kJ/g, steady. ethylene/N2, hc = 22 kJ/g" (Figure 10); "the data set is limited as the BRE sensors were saturated for several tests." §4.D Surprises and New Discoveries: "quasi-steady burning on a flat surface, representing a pool fire, can exist in microgravity... The quasi-steady flames were observed for nominal ambient oxygen mole fractions of 0.265 and above... Methane nitrogen-generated flames self-extinguished within a minute for all ambient conditions... Radiative loss fraction for the flames in microgravity can reach about 60% compared to 30% for the normal gravity flames. TFP measurements of four flames confirmed that critical temperature range for extinction is 1100 to 1200 K... the BRE can emulate several liquids and solids including Acetone, Ethanol, Methanol, PMMA, Nylon, Phenolic glass fiber... For the first time, two limits of extinction were obtained on a plot of heat of combustion vs. heats of gasification." §4.E: "Two of the three approved objectives were accomplished." §4.G Impacts: "Quasi-steady burning corresponding to various condensed-phase materials (such as PMMA and Nylon) was observed in microgravity despite the absence of air flow, where the cessation of ventilation is an established step in putting out spacecraft fires... such flames in a normal atmosphere of 21% oxygen self-extinguished in a short time. While BRE's results are still preliminary, they suggest that NASA may want to increase use of its alternative flammability Test 2, with the cone calorimeter."
