---
type: Document
title: "SPICE: Smoke Point in Co-flow Experiment"
description: Laminar smoke points of non-buoyant gas-jet diffusion flames in co-flowing air, measured in the ISS Microgravity Science Glovebox in 2009, from the SPICE final report.
status: stable
generated: { by: "claude-code/opus-5.5", at: 2026-09-24T07:55:18Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-24T07:55:18Z }
order: 29
geometry_class: gaseous-flames
verified:
  - by: "human:muhammad-marjan-ahmed"
    at: 2026-09-24T07:55:18Z
sources:
  - id: spice-final-report
    title: "Smoke Point in Co-flow Experiment (SPICE): Laminar Smoke Point Properties of Non-buoyant Round-Jet Diffusion Flames — Final Report"
    resource: "SPICE final report by David L. Urban (NASA Glenn), Peter B. Sunderland (University of Maryland) and Zeng-Guang Yuan (NCSER), dated 2 December 2011; distributed in the NASA Physical Sciences Informatics (PSI) archive as 'SPICE Final Report 12_2_2012.pdf'"
---

> [!NOTE]
> Geometry class: **gaseous flames** (round gas jets burning in a co-flow of
> air). Comparable with the [ACME](acme.md) gaseous-flame experiments, not
> directly with solid-fuel burns ([BASS-II](../solid-fuel/bass-ii.md),
> [SAFFIRE](../solid-fuel/saffire.md)) or droplets ([FLEX](../droplet-combustion/flex.md)).
> A "co-flow velocity" here is the air stream around a gas jet, not the flow
> over a solid sample.

> [!IMPORTANT]
> The source is the project's own final report, with a title page that still
> carries an editing note ("Need to show PI, Co-I and PS?"). Its per-fuel
> summary table is reproduced below; the per-flame test matrix it refers to
> (its Appendix A) is the PSI experimental table for SPICE, described in
> [the PSI experimental tables](../../data-sources/psi-experimental-tables.md).

The laminar smoke point is the condition — and the luminous flame length —
at which a flame begins to emit soot, and it indicates the sooting propensity
of a fuel. SPICE measured laminar smoke points of non-buoyant laminar jet
diffusion flames in co-flowing air aboard the International Space Station,
reusing an apparatus built for Enclosed Laminar Flames (ELF), which flew in
the Middle Deck Glovebox of Space Shuttle Columbia on USMP-4/STS-87 in
November 1997.[^spice-final-report]

## Structured facts

Every value below is drawn from the single source cited throughout this
document.

### Experimental conditions

| Field | Value |
| --- | --- |
| Facility | Microgravity Science Glovebox (MSG), ISS |
| Test sessions | twelve, from February 14, 2009 to June 23, 2009 |
| Fuels with smoke points | ethylene, propane, propylene, and propylene/nitrogen mixtures |
| Methane | smoke points attempted but not obtained — flames impinged on the copper plate at the end of the duct |
| Burner diameters | 0.41, 0.76, and 1.6 mm |
| Co-flow velocities | 5.4 - 65 cm/s |
| Ambient O₂ | ISS cabin air, maintained within 19 - 24% (MSG flushed with cabin air after every two burns) |
| Typical burn time | 60 s |
| Fuel supply | two 150 cc bottles of each fuel at gage pressures of 760 - 1440 kPa |
| Flames ignited | 526 |

### Smoke points by fuel (source Table 1)

| Parameter | C2H4 | C3H8 | C3H6 | 75% C3H6 | 50% C3H6 |
| --- | --- | --- | --- | --- | --- |
| Burner diameter d, mm | 0.76 - 1.6 | 0.76 - 1.6 | 0.41 - 1.6 | 0.76 - 1.6 | 0.76 - 1.6 |
| Co-flow velocity ua, cm/s | 18 - 58 | 16 - 45 | 5.4 - 57 | 13 - 65 | 11 - 49 |
| Smoke-point length LSP, mm | 37 - 105 | 46 - 105 | 13 - 59 | 15 - 44 | 22 - 50 |
| Smoke points observed | 6 | 6 | 20 | 13 | 7 |

Smoke-point lengths were measured from the burner to the tip of the luminous
flame on the flame axis; the tips were not sharply defined, transitioning from
bright yellow to black over 2 - 5 mm, and were read where the centerline
grayscale intensity changed most rapidly.[^spice-final-report]

## Findings

The report's closing remarks list its major conclusions:[^spice-final-report]

1. An increase in coflow velocity increases the smoke point length.
2. A decrease in burner diameter increases the smoke point length.
3. Both effects can be explained qualitatively by residence times.
4. Sooting propensity in microgravity increases in the order ethylene <
   propane < 50% propylene < 75% propylene < propylene — the same as in normal
   gravity except that ethylene and propane exchange positions.
5. Luminous length at the smoke point is proportional to fuel mass flow rate,
   with a slight increase as ua / uf decreases.
6. Residence time helps explain the smoke points but does not yield
   quantitative correlations of them.
7. Smoke point lengths scale with d -0.91 uair0.41 (burner diameter to the
   -0.91 power times co-flow velocity to the 0.41 power).

The abstract adds that the measurements allow estimates of pseudo threshold
soot indices (TSI) for microgravity diffusion flames, "indicating an unusually
high sooting propensity for propane in microgravity".[^spice-final-report]

## Open questions

- **The source disagrees with itself on the count of smoke points.** The
  abstract says "Fifty-two smoke points were found"; the closing remarks say
  "Smoke points of 55 microgravity gas-jet diffusion flames" were measured.
  Table 1's per-fuel counts (6, 6, 20, 13, 7) sum to 52. Both statements are
  kept; neither is chosen here.
- **Report date.** The title page is dated 2 December 2011; the file name the
  PSI archive gives it (see this document's source entry) carries a different
  year. Which is the release date is not stated in the report.
- The pseudo threshold soot index values themselves are not given in the
  report body read for this entry; they are said to appear in the
  publications listed in the report's Appendices B through F, which are not
  part of this source.

[^spice-final-report]: SPICE Final Report (Urban, Sunderland, Yuan; 2 December 2011). Abstract: "The laminar smoke point is the condition (and the luminous flame length) where a flame begins to emit soot... SPICE project measured laminar smoke points in non-buoyant laminar jet diffusion flames in co-flowing air aboard the International Space Station. Fifty-two smoke points were found for ethylene, propane, propylene, and propylene/nitrogen mixtures. Burner diameters were 0.41, 0.76, and 1.6 mm and co-flow velocities varied from 5.4 - 65 cm/s... The measured smoke point lengths were found to correlate with burner diameter to the -0.91 power times coflow velocity to the 0.41 power. The measurements allow estimates of pseudo threshold soot indices (TSI) for microgravity diffusion flames, indicating an unusually high sooting propensity for propane in microgravity." SPICE Experiment Setup: "The SPICE project utilized and modified an apparatus constructed for a previous project, Enclosed Laminar Flames (ELF), which was conducted in the Middle Deck Glovebox of Space Shuttle Columbia during mission USMP-4/STS-87 in November, 1997." SPICE Flight Tests: "The actual SPICE tests were conducted in SMG in twelve sessions from February 14, 2009 to June 23, 2009... Typical burn times were 60 s, and after each two such burns the MSG contents were flushed with ISS cabin air. The oxygen mole fraction of this cabin air is maintained within 19 - 24%... The luminous flame tips were not sharply defined in most images, but rather transitioned from bright yellow to black over an axial distance of 2 - 5 mm... Totally 526 flames were ignited and studied." Test Results: "the supply was limited to two 150 cc bottles of each fuel at gage pressures of 760 - 1440 kPa. Smoke points were attempted with methane, but could not be obtained before the flames impinged on the copper plate at the end of the duct." Table 1 (smoke points observed): d, mm 0.76 - 1.6 / 0.76 - 1.6 / 0.41 - 1.6 / 0.76 - 1.6 / 0.76 - 1.6; ua, cm/s 18 - 58 / 16 - 45 / 5.4 - 57 / 13 - 65 / 11 - 49; LSP, mm 37 - 105 / 46 - 105 / 13 - 59 / 15 - 44 / 22 - 50; # smoke points 6 / 6 / 20 / 13 / 7 (C2H4 / C3H8 / C3H6 / 75% C3H6 / 50% C3H6). Closing Remarks: "Smoke points of 55 microgravity gas-jet diffusion flames in coflowing air were measured in earth orbit... The sooting propensities of the present fuel mixtures in microgravity increase according to ethylene < propane < 50% propylene < 75% propylene < propylene. This is the same as in normal gravity except for the exchanged positions of ethylene and propane... The present smoke point lengths scale with d -0.91 uair0.41."
