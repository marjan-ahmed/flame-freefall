---
type: Document
title: "ACME s-Flame: Structure and Response of Spherical Diffusion Flames"
description: Spherical diffusion flames from a porous spherical burner in quiescent microgravity, tested on the ISS in 2019-2020 with nitrogen and helium dilution, from the ACME/s-Flame final report.
status: draft
ksor:
  audience: [public]
  owner: human:you
order: 28
geometry_class: gaseous-flames
sources:
  - id: acme-s-flame-final-report
    title: "Advanced Combustion via Microgravity Experiments (ACME) Structure and Response of Spherical Diffusion Flames (s-Flame) — ACME/s-Flame Final Report (2021)"
    resource: "ACME/s-Flame final report prepared by Dennis P. Stocker (NASA Glenn) and Chung K. Law (Princeton University) with the s-Flame team, dated 29 July 2021; distributed in the NASA Physical Sciences Informatics (PSI) archive as 's_Flame_final_report_20210729.pdf'"
---

> [!NOTE]
> Geometry class: **gaseous flames** — a spherical diffusion flame around a
> porous spherical burner fed with gaseous fuel. Comparable with the other
> [ACME](acme.md) experiments; not directly with solid-fuel or droplet tests.

> [!IMPORTANT]
> The report states that "detailed analyses of the acquired data,
> computational simulation, and theoretical analysis are ongoing", and many of
> its findings are phrased as "seem to" or "may have". They are reproduced
> with that uncertainty intact.

s-Flame is one of six independent experiments in the Advanced Combustion via
Microgravity Experiments (ACME) project, run in the Combustion Integrated Rack
(CIR) on the International Space Station (ISS). Principal Investigator:
Prof. Chung K. Law (Princeton University); the co-investigators are Prof.
Stephen D. Tse (Rutgers University) and Dr. Kurt R. Sacksteder (NASA Glenn);
the project scientist is Dennis P. Stocker (NASA Glenn).[^acme-s-flame-final-report]

A burner-generated spherical diffusion flame is a simple, one-dimensional
flame geometry that permits a rigorous comparison between detailed theory and
experiment. Changing the fuel supply rate moves a flame toward a
convective-kinetic extinction limit (short residence time) or lets radiative
losses quench it (very long residence time); near these dual flammability
boundaries, flame-front instabilities may appear.[^acme-s-flame-final-report]

## Structured facts

Every value below is drawn from the single source cited throughout this
document.

### Experimental conditions

| Field | Value |
| --- | --- |
| Facility | Combustion Integrated Rack (CIR), ACME hardware, Destiny module of the ISS |
| Round 1 | Sept. 2019 to Jan. 2020 — nitrogen dilution |
| Round 2 | May to July 2020 — helium rather than nitrogen dilution |
| Increments | 60-63 (no testing during Increment 62, limited crew availability) |
| Fuels | hydrogen, methane, ethylene, and H2/CH4 mixtures |
| Diluents | nitrogen and helium |
| Ambient | quiescent oxidizing atmosphere; air and enriched O2 environments |

### Aims of the tests

1. Advance prediction of the structure and dynamics, including extinction, of
   soot-free and sooty flames.
2. Obtain data in simple, well-defined flow fields.
3. Identify the extinction limits for both radiative and convective
   extinction (high and low system Damköhler numbers).
4. Determine the existence, onset and nature of pulsating instabilities
   predicted for fuel/diluent mixtures above a critical Lewis number.
5. Validate and/or improve computational simulation with detailed chemistry
   and transport.

## Findings

Initial surprises and discoveries, as the report lists them:[^acme-s-flame-final-report]

- Nitrogen-diluted methane and ethylene flames in air seem to demonstrate
  kinetic extinction at low flow rates and radiative extinction at high flow
  rates — not seen in ground-based research, given the limited microgravity
  durations. "Surprisingly, radiative extinction has been found to be a common
  event in ISS testing, which was predicted computationally, but not observed
  previously for our flame conditions."
- Ethylene flames, which tend to soot in normal gravity, did not soot in
  microgravity except during forced ignition from the hotwire — also not in
  enriched oxidizer conditions or with either inert.
- Nitrogen-diluted hydrogen flames seem to need very large sizes to
  self-extinguish; radiative extinction was not observed, but kinetic
  extinction during ramp down seems to be exhibited.
- Nitrogen-diluted hydrogen/methane flames manifested radiative extinction,
  as predicted by simulation; kinetic extinction could not be identified
  conclusively.
- Helium-diluted cases had shifted extinction limits; kinetic extinction was
  generally difficult to observe, and ignition was severely affected.
- The pulsating instabilities the helium cases were meant to isolate "were not
  conclusively observed in the ISS tests, at least from the video images".
- Flame luminosity does not necessarily correspond with flame strength.
- Characteristically sooty flames were not observed, so "the effect of soot on
  extinction could not be" assessed.

## Open questions

- Temperature distributions from thin-filament pyrometry were still being
  processed; species distributions were not measured directly.
- Radiometer and PMT data were still to be examined in detail for the
  instability question.
- The per-day test log (flames ignited per day, fuel bottle, atmosphere) is
  the PSI experimental table for s-Flame, described in
  [the PSI experimental tables](../../data-sources/psi-experimental-tables.md).

[^acme-s-flame-final-report]: ACME/s-Flame Final Report (Stocker, Law and team; 29 July 2021). §1 Overview: "The Structure and Response of Spherical Diffusion Flames (s-Flame) experiment is one of six independent experiments that make up the Advanced Combustion via Microgravity Experiments (ACME) project for which tests are conducted within the Combustion Integrated Rack (CIR) on the International Space Station (ISS). The experiment's Principal Investigator (PI) is Prof. Chung K. Law of Princeton University. The experiment has two Co-Investigators (Co-Is), namely Prof. Stephen D. Tse of Rutgers University and Dr. Kurt R. Sacksteder of the NASA Glenn Research Center... Dennis P. Stocker of the NASA Glenn Research Center is the Project Scientist (PS)... The s-Flames operations were conducted in two rounds of testing during Increments 60-63, where there was no testing during Increment 62 due to limited crew availability... the first round of testing was conducted from Sept. 2019 to Jan. 2020, while the second-round testing - featuring helium rather than nitrogen dilution - occurred from May to July 2020." §2.C: "A burner-generated spherical diffusion flame provides a simple, one-dimensional flame geometry that permits a rigorous comparison between detailed theory and experimental verification... altering fuel supply rates to limit flame residence time induces a convective-kinetic extinction limit. Alternatively, very large residence times allow radiative heat losses and diffusive transport mechanisms to quench the flame. Near these dual flammability boundaries of quasi-steady flames, flame-front instabilities may appear." §4.C: "The s-Flame experiment uses the Combustion Integrated Rack (CIR) and the ACME hardware in the Destiny module of the ISS... Identify the extinction limits for both radiative and convective extinction (i.e., at high and low system Damköhler numbers, respectively); Determine the existence, onset, and nature of pulsating instabilities that have been theoretically predicted to occur in such flames with fuel/diluent mixtures that are above a critical Lewis number... Currently, detailed analyses of the acquired data, computational simulation, and theoretical analysis are ongoing... Conventional gaseous fuels including hydrogen, methane, and ethylene are used... Diluents mixed with fuel include nitrogen and helium." §4.D: "Nitrogen-diluted methane and ethylene flames in air seem to demonstrate kinetic extinction at low flow rates (low system Da) and radiative extinction at high flow rates (high system Da)... Surprisingly, radiative extinction has been found to be a common event in ISS testing, which was predicted computationally, but not observed previously for our flame conditions... The nitrogen-diluted methane flames were tested in air and enriched O2 environments... Ethylene flames which tend to soot under normal gravity conditions did not soot under microgravity conditions. Sooting only occurred during forced ignition from the hotwire... Nitrogen-diluted hydrogen flames seem to need to be at very large characteristic sizes to self- extinguish... Nitrogen-diluted hydrogen/methane mixture flames manifested radiative extinction, as predicted by computational simulations... Helium-diluted cases had shifted extinction limits... Ignition was also severely affected by using He as diluent... such instabilities were not conclusively observed in the ISS tests, at least from the video images. Radiometer and PMT data will need to be examined in detail... Flame luminosity does not necessarily correspond with flame strength." §4.E: "Species distribution is not explicitly measured... Characteristically sooty flames were not observed... None of the flames were inherently sooty, so the effect of soot on extinction could not be."
