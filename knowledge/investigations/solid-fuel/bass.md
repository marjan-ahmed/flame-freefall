---
type: Document
title: "BASS: Burning and Suppression of Solids"
description: The first BASS campaign (2012-2013) — solid samples burned in a small flow duct in the ISS Microgravity Science Glovebox — from its science requirements, its 2013 results overview, and the PSI data layout document.
status: stable
generated: { by: "claude-code/opus-5.5", at: 2026-09-24T07:55:18Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-24T07:55:18Z }
order: 24
geometry_class: solid-fuel
verified:
  - by: "human:muhammad-marjan-ahmed"
    at: 2026-09-24T07:55:18Z
sources:
  - id: bass-srd-2010
    title: "Requirements for Science — Burning and Suppression of Solids (BASS) in Low-Speed Air Flow in Microgravity"
    resource: "BASS Science Requirements Document ('Material Flammability... Including an Assessment of Inert-Gas Extinguishing Agent: An ISS Glovebox Experiment Utilizing Existing SPICE Hardware with Minor Modifications'), February 2010; distributed in the NASA Physical Sciences Informatics (PSI) archive as 'SRD_BASS.pdf'"
  - id: bass-iss-overview-2013
    title: "Burning and Suppression of Solids (BASS): An Overview of Recent ISS Results"
    resource: "Poster by Paul V. Ferkul, Sandra L. Olson, Fumiaki Takahashi, Michael C. Johnston, Makoto Endo and James S. T'ien, presented at the 2nd Annual ISS Research and Development Conference, Denver, Colorado, July 16-18, 2013; distributed in the NASA PSI archive as 'ISS Denver 2013-BASS.pdf'"
  - id: bass-psi-data-layout
    title: "PSI Data Layout Document - BASS (Burning and Suppression of Solids) Investigation"
    resource: "NASA Physical Sciences Informatics (PSI) data layout document for the BASS investigation; distributed in the PSI archive as 'DLD_BASS.pdf'"
---

> [!NOTE]
> Geometry class: **solid fuel** — thin and thick flat samples, spheres and
> candles burning in a forced low-speed air flow. Directly comparable with its
> successor [BASS-II](bass-ii.md) (same duct) and, with care for scale, with
> [SAFFIRE](saffire.md).

> [!IMPORTANT]
> The results source is a **conference poster**, not a technical report: it
> summarizes selected observations. Per-test values live in the PSI
> experimental table for BASS, described in
> [the PSI experimental tables](../../data-sources/psi-experimental-tables.md).

BASS examines the burning and extinction characteristics of a wide variety of
fuel samples in microgravity, to guide strategies for extinguishing accidental
fires and to feed the combustion models used in the design of fire detection
and suppression systems.[^bass-psi-data-layout]

## Why it was run

The science requirements state the hypothesis that "materials in
microgravity, with adequate ventilation, burn as well if not better than the
same material in normal gravity with other conditions being identical" — and
that if it is true, it "implies serious safety concerns over the utility and
margin of safety provided NASA- STD-6001 Test #1" (see
[NASA-STD-6001B](../../foundations/nasa-std-6001b.md)). Its two objectives:[^bass-srd-2010]

1. Begin to bridge the gap between the normal-gravity NASA-STD-6001 Test#1
   method, ground-based microgravity tests, and actual material flammability
   in space — including wake flames and fuels "significantly thicker than the
   thin sheets studied in ground-based facilities".
2. Assess the effectiveness of an inert, gaseous extinguishing agent (similar
   to that used on ISS) on flames over different materials, geometries,
   preheating, and flow.

The plan reused the on-orbit SPICE glovebox hardware with four changes:
replaceable solid fuel samples, an adjustable igniter, a nitrogen gas jet for
flame extinguishment, and a way to shut off the flow completely.[^bass-srd-2010]

## Structured facts

### Experimental conditions

| Field | Value | Source |
| --- | --- | --- |
| Facility | small wind tunnel in the Microgravity Science Glovebox (MSG), ISS | poster |
| Airflow | speeds up to 40 cm/s, opposed and concurrent | poster |
| Samples and burns | 41 samples, 115 burns completed | poster |
| Sample types | thin, flat (17); spheres (12); thick, flat (4); candles (8) | poster |
| Main variable | airflow speed; "More recent tests varying oxygen (below 21%) have been completed" | poster |
| Data in PSI | two datasets by year: BASS_2012 (21 image galleries) and BASS_2013 (12 audio/video collections, 15 image galleries) | data layout document |

### Selected results (from the poster)

- **Thin fuel, opposed flow**: the flame quickly reached steady spread, and
  spread rate "was fastest at an intermediate value of flow speed".
- **Thin fuel, concurrent flow**: spread rate increased linearly with
  increasing flow; quenching extinction was observed around 1 cm/s.
- "This is the first time that detailed transient flame growth data was
  obtained in purely forced flows in microgravity."
- **Fire-retarded materials**: Ultem and Nomex HT90-40 samples did not burn in
  the ISS atmosphere (21% to 22% O2, flow speeds around 15 cm/s), "Similar to
  1-g"; a Nomex-III sample did burn (22% O2, 1 atm, 14 cm/s), shrinking in
  width until it extinguished within 1 cm of the end of the sample.
- **Opposed flow, 0-g vs 1-g**: at 10 cm/s in 0-g the flame reached steady
  size and spread; in 1-g the flame "does not propagate downward".
- **PMMA spheres and candles** were burned at 17% oxygen at flows from 12 cm/s
  down to less than 1 cm/s; the images give flame growth rate, flame-to-fuel
  distance and solid regression rate for model comparison.[^bass-iss-overview-2013]

## Open questions

- The nitrogen-suppression objective is described in the requirements but no
  suppression result appears in the poster.
- Numeric spread rates are shown on the poster only as plot annotations that
  did not survive text extraction legibly; they are not reproduced here.
- The PSI data layout document describes images and video only. What the
  per-test table records (and does not) is described in
  [the PSI experimental tables](../../data-sources/psi-experimental-tables.md).

[^bass-srd-2010]: BASS Science Requirements (February 2010). Background: "There is some evidence for the hypothesis that materials in microgravity, with adequate ventilation, burn as well if not better than the same material in normal gravity with other conditions being identical... If this hypothesis is true, it implies serious safety concerns over the utility and margin of safety provided NASA- STD-6001 Test #1." Objectives: "Begin to bridge the gap between the normal gravity NASA-STD-6001 Test#1 method, ground-based microgravity tests, and actual material flammability in space... Fuels can be significantly thicker than the thin sheets studied in ground-based facilities... Assess the effectiveness of an inert, gaseous extinguishing agent (similar to that used on ISS) in putting out flames over different materials, geometries, preheating, and flow." Hardware changes: "The plan is to use the existing NASA glovebox SPICE hardware with four changes: Accommodation of replaceable solid fuel samples; Igniter element adjustable... Nitrogen gas jet for flame extinguishment; Providing a way to shut off the flow completely."

[^bass-iss-overview-2013]: BASS: An Overview of Recent ISS Results (Ferkul, Olson, Takahashi, Johnston, Endo, T'ien; 2nd Annual ISS Research and Development Conference, Denver, Colorado, July 16-18, 2013). "Fuel samples were mounted inside a small wind tunnel which could impose airflow speeds up to 40 cm/s... More recent tests varying oxygen (below 21%) have been completed." "Thin, flat (17) Spheres (12) Thick, flat (4) Candles (8)... Airflow speed was the main variable... 41 samples, 115 burns completed." Summary 1: "Opposed flow: flame quickly reached steady spread; spread rate was fastest at an intermediate value of flow speed. Concurrent flow: Flame spread rate increased linearly with increasing flow. Quenching extinction was observed (around 1 cm/s). This is the first time that detailed transient flame growth data was obtained in purely forced flows in microgravity." Results: "Ultem and Nomex HT90-40 samples did not burn on ISS atmosphere 21% to 22% O2 Flow speeds around 15 cm/s Similar to 1-g... Nomex-III sample did burn; NOMEX - III, 22% O2, 1 atm 14 cm/s (0g)... Flame was shrinking in width until it extinguished within 1 cm of the end of the sample." "0-g with flow (10 cm/s) Steady flame size and spread... 1-g Flame does not propagate downward." "a burning 2-cm diameter PMMA sphere at 17% oxygen and 12 cm/s flow... less than 1 cm/s... flame growth rate, flame-to-fuel distance, and the solid regression rate."

[^bass-psi-data-layout]: PSI Data Layout Document - BASS: "BASS (Burning and Suppression of Solids) examines the burning and extinction characteristics of a wide variety of fuel samples in microgravity. The BASS experiment will guide strategies for extinguishing accidental fires in microgravity. BASS results contribute to the combustion computational models used in the design of fire detection and suppression systems in microgravity and on Earth. The BASS data available in PSI is organized into 2 datasets by the year the tests were conducted: BASS_2012, BASS_2013... There are 21 image galleries for BASS_2012... There are 12 audio/video collections and 15 image galleries for BASS_2013."
