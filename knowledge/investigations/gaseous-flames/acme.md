---
type: Document
title: "ACME: Advanced Combustion via Microgravity Experiments"
description: Six gaseous-fuel laminar flame experiments on the ISS Combustion Integrated Rack, summarized from NASA's own poster presentation of selected results.
status: stable
generated: { by: "claude-code/sonnet-5", at: 2026-09-21T19:56:58Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-21T19:56:58Z }
order: 23
geometry_class: gaseous-flames
sources:
  - id: acme-ps-03403
    title: "Advanced Combustion via Microgravity Experiments (ACME) on the International Space Station (ISS)"
    resource: "https://ntrs.nasa.gov/citations/20210015913"
verified:
  - by: human:you
    at: 2026-09-21T19:56:58Z
---

> [!NOTE]
> Geometry class: **gaseous laminar flames**. Not directly comparable to
> [BASS-II](../solid-fuel/bass-ii.md) or [SAFFIRE](../solid-fuel/saffire.md)
> (large-scale solid-fuel burns) or [FLEX](../droplet-combustion/flex.md)
> (droplet combustion) without noting the geometry mismatch — ACME burns
> gaseous fuel jets, not a condensed-phase fuel surface or droplet.

> [!IMPORTANT]
> The source is a **poster presentation** (contact: Dennis Stocker, NASA
> Glenn), not a full technical report — it summarizes selected findings from
> five of six sub-experiments rather than reporting complete datasets. This
> entry reports exactly what that poster states; it is narrower and less
> detailed than the BASS-II/SAFFIRE technical reports.

ACME ran six independent gaseous-fuel combustion experiments — sharing one set
of modular hardware in the Combustion Integrated Rack (CIR) — studying laminar
spherical and axisymmetric nonpremixed flames. Five studies were selected by
NASA and one by NSF/CASIS; on-orbit operations have run since September
2017.[^acme-ps-03403]

## Structured facts

Every value below is drawn from the single source cited throughout this
document.

### Experimental conditions

| Field | Value |
| --- | --- |
| Facility | Combustion Integrated Rack (CIR), ISS |
| Number of sub-experiments | six independent experiments, one set of modular hardware |
| Operations underway since | September 2017 |
| Flames ignited (as of poster) | over 1,000, across 3.5 years of ISS testing |
| Sub-experiments completed (as of poster) | four of six |

### Measured outcomes (selected findings, by sub-experiment)

| Sub-experiment | Finding |
| --- | --- |
| Coflow Laminar Diffusion Flame (CLD Flame) | microgravity flames contain five to eight times more soot than equivalent normal-gravity flames; are taller and wider |
| Burning Rate Emulator (BRE) | flames self-extinguish in O₂ concentrations below ~25 percent by volume; larger flames generally self-extinguish within 1.5 minutes even at elevated O₂ |
| BRE — fuel-specific | ethylene flames can burn for minutes at elevated O₂; methane flames self-extinguish within a minute |
| Flame Design | flame size increases with reactant flow rate, decreases with ambient O₂ concentration; large flames grow until extinguishing from radiative heat loss, via an oscillatory partial-extinguish/reform mode of growing magnitude |
| Structure and Response of Spherical Diffusion Flames (s-Flame) | both radiative extinction (high flow rates) and kinetic/convective extinction (low flow rates) observed |
| Electric-Field Effects (E-FIELD Flames) | a distinct peak ion current corresponds to the most compact flame; highly diluted flames can be stabilized with very weak electric fields |

## Findings by sub-experiment

**Coflow Laminar Diffusion Flame** (Long, Smooke, Tinajero, Yale): microgravity
increases the limits of fuel dilution for both methane and ethylene flames,
and near those limits, microgravity flames are more stable — allowing lifted
flames at lower fuel concentrations.[^acme-ps-03403]

**Electric-Field Effects on Laminar Diffusion Flames** (Dunn-Rankin, Chien, UC
Irvine): jet flames under strong electric fields were unstable and exhibited
corona, then arc, discharges; when soot is present, electric fields produce a
wide range of behaviors.[^acme-ps-03403]

**Burning Rate Emulator** (Quintiere, Sunderland, U. Maryland; de Ris, FM
Global): low-momentum microgravity flames can burn for minutes in the absence
of airflow or flame spread.[^acme-ps-03403]

**Flame Design** (Axelbaum, Washington U. in St. Louis; Sunderland, U.
Maryland): very small flames have low radiative loss and asymptotically
approach steady-state behavior.[^acme-ps-03403]

**Structure and Response of Spherical Diffusion Flames** (Law, Princeton;
Tse, Rutgers): with helium rather than nitrogen dilution of fuel and oxygen,
extinction limits shift and kinetic extinction becomes generally difficult to
discern.[^acme-ps-03403]

**Cool Flames Investigation with Gases (CFI-G)** (Sunderland, Axelbaum,
Williams, UC San Diego): goal is to observe quasi-steady nonpremixed spherical
cool flames — no findings are listed in this source.[^acme-ps-03403]

## Open questions

- This source is a poster, not the full underlying technical reports for each
  of the six sub-experiments; only qualitative/selected findings are
  available here, not the raw numeric datasets each PI presumably holds.
- CFI-G has no reported findings in this source — its results, if any existed
  as of this poster's date, are not captured.
- The specific ~25 percent O₂ self-extinguish threshold and 1.5-minute
  self-extinguish figure are BRE-specific; they should not be generalized to
  the other five ACME sub-experiments without their own data.

[^acme-ps-03403]: Advanced Combustion via Microgravity Experiments (ACME) on the ISS (poster presentation). Overview: "Advanced Combustion via Microgravity Experiments (ACME) on the International Space Station (ISS) / Tests carried out within the Combustion Integrated Rack (CIR)... Laminar spherical and axisymmetric nonpremixed flames of gaseous fuels... Six independent experiments using one set of modular hardware. Five studies selected by NASA. One study selected by NSF (National Science Foundation) and CASIS (Center for the Advancement of Science in Space)." "On-orbit operations underway since September 2017. Over 1,000 flames ignited during 3.5 years of ISS testing. Space station tests for four of six ACME experiments completed." Coflow Laminar Diffusion Flame: "Key researchers: Marshall Long, Mitch Smooke, and Jesse Tinajero (Yale)... Selected findings — Microgravity flames contain five to eight times more soot than the equivalent normal-gravity flames. — Microgravity flames are taller and wider. — Microgravity increases the limits of fuel dilution for both methane and ethylene flames. Near limits, microgravity flames are more stable, allowing for lifted flames at lower fuel concentrations." Electric-Field Effects on Laminar Diffusion Flames: "Key researchers: Derek Dunn-Rankin and Yu-Chien Chien (UC Irvine)... Selected findings — In microgravity, flames exhibit a distinct peak ion current that corresponds to the most compact flame... When soot is present in a flame, electric fields create a wide range of behaviors. Highly diluted flames can be stabilized with very weak electric fields. Jet flames, under the influence of the electric field, were unstable at high field strengths and exhibited corona and then arc discharges." Burning Rate Emulator: "Key researchers: Jim Quintiere and Peter Sunderland (U. Maryland), and John de Ris (FM Global, retired)... Selected findings — Low-momentum microgravity flames can burn for minutes in the absence of an airflow or flame spread. While the flames can burn for minutes in elevated oxygen concentrations, like those being considered for future spacecraft, they were found to self-extinguish in concentrations below ~25 percent (by volume). While smaller flames can burn for minutes at elevated oxygen concentrations, larger flames were generally seen to self-extinguish within 1.5 minutes. While ethylene flames at elevated oxygen concentrations can burn for minutes, methane flames were seen to self-extinguish within a minute." Flame Design: "Key researchers: Rich Axelbaum (Washington U. in St. Louis) and Peter Sunderland (U. Maryland)... Selected findings — Flame size increases with reactant flow rate and decreases with ambient oxygen concentration. Very small flames have low radiative loss and asymptotically approach steady-state behavior. Large flames increase in size over time until the flame extinguishes due to radiative heat loss. Before total extinction, these flames experience an unstable, oscillatory mode, in which they partially extinguish and reform. The oscillations grow in magnitude until total extinction." Structure and Response of Spherical Diffusion Flames: "Key researchers: C.K. Law (Princeton) and Stephen Tse (Rutgers)... Selected findings — Both radiative and kinetic (i.e., convective) extinction of the spherical flames appear to have been observed. Radiative extinction seems to occur at high flow rates and kinetic extinction at low flow rates... With helium, rather than nitrogen, dilution of both the fuel and oxygen, the extinction limits are shifted and kinetic extinction is generally difficult to discern." Cool Flames Investigation with Gases: "Key researchers: Peter Sunderland (U. Maryland), Rich Axelbaum (Washington U. in St. Louis), and Forman Williams (UC San Diego)... Goal: Observe quasi-steady nonpremixed spherical cool flames."
