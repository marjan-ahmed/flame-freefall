---
type: Document
title: "FLEX-2 as-run cool-flame results (FLEX-team literature)"
description: As-run FLEX-2 droplet-burn measurements reported by the FLEX team (n-decane, n-octane, n-heptane; hot- and cool-flame burning rates, extinction events) — literature evidence that supplements the planned-envelope PSI-68 table, whose rows carry no results.
status: stable
generated: { by: "process:codex-source-review", at: 2026-10-31T11:55:40Z }
order: 26
geometry_class: droplet-combustion
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-10-31T11:55:40Z }
sources:
  - id: flex-2-cool-flame-2014
    title: "Cool-flame extinction during n-alkane droplet combustion in microgravity (Nayagam, Dietrich, Hicks, Williams; Central States Section of the Combustion Institute, Spring Technical Meeting, March 2014)"
    resource: "https://ntrs.nasa.gov/citations/20140006750"
  - id: flex-2-cool-flame-asgsr-2020
    title: "Effects of Ambient Inert Gas Properties on Cool-Flame Combustion of Normal-Alkane Droplets in Microgravity (Nayagam, Dietrich, Williams; ASGSR Annual Meeting, November 2020)"
    resource: "https://ntrs.nasa.gov/citations/20205008449"
---

> [!NOTE]
> Geometry class: **droplet combustion**, the same class as [FLEX](flex.md),
> [CFI](cfi.md) and the [FLEX-2 plan](flex-2.md). Not directly comparable with
> solid-fuel or gaseous-flame investigations.

> [!WARNING]
> The PSI-68 experimental table for FLEX-2 is a **planned envelope** — one row
> per fuel, identical swept ranges, no results (see [flex-2.md](flex-2.md)).
> This document carries what the FLEX team's own reports say about the burns
> they ran. It is a **literature supplement, not PSI-table data**: the test
> identifiers below (`R377`, `R694`, …) exist only in the cited papers and
> cannot be checked against any PSI as-run table, because none is in this
> record. Where a value is attached to a PSI-68 envelope record by the ingest,
> that join is by exact fuel identity only, and every value's own note says so.

The FLEX-2 experiments ran on the Multi-User Droplet Combustion Apparatus
(MDCA) in the Combustion Integrated Rack (CIR) on the ISS: droplets of chosen
size deployed between opposed needles (or tethered on a 80 µm silicon-carbide
fibre when needed), ignited by two hot-wire igniters, with back-lit droplet
imaging, OH* chemiluminescence imaging at 310 nm, and broadband (0.6–5.0 µm)
plus narrowband (5.0–7.0 µm) radiometers sampling at 100 Hz. The chamber free
volume is approximately 95 liters, refilled between environments through the
Fuel and Oxidizer Management Assembly.[^flex-2-cool-flame-2014]

[^flex-2-cool-flame-2014]: Cool-flame extinction during n-alkane droplet combustion in microgravity (Nayagam et al., 2014). §2 Experiments: "The experiments were conducted using the Multi-User Droplet Combustion Apparatus installed in the Combustion Integrated Rack (CIR) facility in the US Module of the ISS. The cylindrical combustion chamber in the CIR has a free-volume of approximately 95 liters with the MDCA insert installed. The MDCA used an opposed-needle deployment technique to freely deploy droplets of chosen size in microgravity. When needed it was also possible to use 80 µm silicon-carbide fiber to tether the droplet. Ignition of the free droplet was accomplished using two symmetrically positioned hot-wire igniters." §3 Results: "Over three hundred droplet combustion tests were completed as part of the FLEX experiments using three different normal alkane fuels and two different alcohol fuels in a variety of diluent substituted environments at ambient pressures in the range of 0.5 to 3 atm to date."

[^flex-2-cool-flame-asgsr-2020]: Effects of Ambient Inert Gas Properties on Cool-Flame Combustion of Normal-Alkane Droplets in Microgravity (Nayagam et al., ASGSR 2020). Background: "In this study we present experimental results (from FLEX/FLEX-2/CFI) for n-alkane fuel-droplet cool-flame burning rates and extinction diameters in Helium or Xenon diluted ambient conditions." Summary: "Xenon decreases burning rates substantially, but can sustain cool flames at much lower oxygen concentrations compared to helium."

## Two combustion stages, one invisible to the imagers

The defining FLEX-2 observation: after the visible (hot) flame undergoes
radiative extinction, large n-alkane droplets keep burning quasi-steadily in a
low-temperature ("cool flame") regime governed by negative-temperature-
coefficient (NTC) chemistry, then extinguish abruptly at a finite droplet
diameter, mostly leaving a vapor cloud, and the residue evaporates. The cool
flame responds to the radiometers but **not to either camera**:[^flex-2-cool-flame-2014]

> [!IMPORTANT]
> Fire-safety relevance: a flame that continues releasing chemical heat after
> the visible flame dies is a post-extinction hazard that crew cameras and the
> UV imager would not register. Detection in microgravity cannot rely on
> visible-flame observation for large n-alkane droplets.

- Cool-flame burning rates are slightly lower than the hot-flame rates of the
  same burn ("The cool flame burning rates are slightly lower compared to the
  hot flame rates").[^flex-2-cool-flame-2014]
- For O₂/N₂ environments the cool-flame extinction diameter varies with oxygen
  concentration roughly as CO2 to the power −3/4, "within the scatter of the
  data"; for diluent-substituted atmospheres (CO₂ or He) it does not, but the
  measured residence time D²ce/Kc correlates with the oxygen molar
  concentration, in agreement with the theoretical slope of −3/2, again "within
  the appreciable scatter".[^flex-2-cool-flame-2014]
- Diluents act through heat transfer and diffusion, not chemistry: CO₂ replaces
  nitrogen through its radiative participation, helium through a thermal
  conductivity almost 10 times that of nitrogen, which shortens the burning
  times of both stages considerably.[^flex-2-cool-flame-2014]
- In the 2020 FLEX/FLEX-2/CFI compilation, helium or xenon displacing air at
  21% O₂ makes quasi-steady cool-flame theory invalid (burning becomes highly
  transient for He); xenon sustains cool flames at much lower oxygen
  concentrations than helium; theory agreements are reasonable for heptane and
  octane while dodecane extinction diameters are over-predicted "despite the
  lumped parameters". The numeric values that support the 2020 plots sit in the
  figures and are not recoverable from that document's text.[^flex-2-cool-flame-asgsr-2020]

## Per-burn results (2014 paper, §3 and Figure captions)

Every cell is copied from the source text as written (the extraction under
`psi-data/derived/report-extractions/FLEX-2 Cool-flame Extinction N-Alkane
Droplets.md` is the verification text). Where the source prints a value that
cannot be right as written (R383's diluent), the anomaly is carried in the cell
and questioned below, never silently cleaned.

| Test | Fuel | D₀ (mm) | Atmosphere (as printed) | Pressure (atm) | Hot-flame K (mm2/s) | Cool-flame K (mm2/s) | Stage events |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R377 | n-decane | 4.03 | 21%O2 and 79%N2 | 0.5 | 0.41 | 0.33 | hot-flame extinction abruptly at around 14.6 seconds; cool-flame stage end not timed |
| R374 | n-decane | 3.79 | 25%O2 and 75%N2 | 0.5 | 0.52 | not stated | droplet micro-explodes 26 seconds after ignition; K valid only for the in-field-of-view duration |
| R379 | n-decane | 3.86 | 17%O2 and 83%N2 | 0.5 | 0.31 | 0.27 | radiative extinction at 7 seconds (hot stage) |
| R383 | n-decane | 3.14 | 14%O2 and 96%N2 (as printed) | 0.5 | 0.29 | 0.25 | further reduction in O2 leads to earlier extinctions in both regimes |
| R298 | n-octane | 3.6 | air (O2:N2 = 0.21:0.79), no helium dilution | 1.0 | 0.48 | 0.38 | oscillatory visible-flame instability; cool-flame extinction at 30.5 seconds, captured radiometrically (droplet drifted out of view) |
| R694 | n-octane | 3.37 | 0.21 O2 / 0.15 He / 0.64 N2 | 1.0 | 0.54 | 0.43 | burning times of both stages considerably shortened by helium; reduced peak radiative heat loss |
| R698 | n-octane | 3.6 | 0.21 O2 / 0.50 He / 0.29 N2 | 1.0 | 0.63 | 0.53 | not timed in the text |
| R707 | n-octane | 2.49 | 0.21 O2 / 0.75 He / 0.04 N2 | 1.0 | not stated (first stage almost eliminated) | not stated | entire process transient; quasi-steady burning not achieved |
| n-heptane case 1 | n-heptane | 3.91 | 21% oxygen, 79% nitrogen | 1.0 | not stated | not stated | radiative extinction, cool-flame combustion, second-stage extinction, pure vaporization |
| n-heptane case 2 | n-heptane | 3.48 | 18% oxygen, 82% nitrogen | 1.0 | not stated | not stated | radiative extinction, cool-flame combustion, second-stage extinction, pure vaporization |
| n-heptane case 3 | n-heptane | 2.49 | 18% oxygen, 67% nitrogen, 15% carbon dioxide | 1.0 | not stated | not stated | radiative extinction, cool-flame combustion, second-stage extinction, pure vaporization |

## Open questions

- **R383's diluent as printed sums to more than the whole atmosphere.** The
  source caption reads
  "(d) R383 D0=3.14 mm, 14%O2 and 96%N2" — fourteen percent plus ninety-six
  percent exceeds one hundred. The oxygen value
  (14%) is the one the paper's −3/4 trend depends on, and the K values for the
  two regimes are given separately, so both stages' rates join; the nitrogen
  value as printed is kept but not trusted, and no balance is inferred.
- **No test chronology.** Neither paper dates individual burns (dates, GMT, or
  ID-level ISS session metadata are absent). Test identifiers cannot be pinned
  to the PSI table, which has no as-run FLEX-2 rows at all; the per-burn values
  therefore attach to the PSI-68 planned envelopes only as a supplement, never
  as record-identity evidence.
- **The heptane cases are anonymous.** The paper plots "three typical
  free-floated cases" without identifiers, so no R-number exists for them; the
  table rows above carry their measured initial diameters only.
- **The 2020 figures are the data.** The ASGSR abstract's burning-rate and
  extinction plots exist only as images; per-test values for xenon-diluted
  burns are not recoverable from its text.
