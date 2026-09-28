---
type: Document
title: "FLEX-2: Fundamental Studies in Droplet Combustion and Flame Extinguishment"
description: The planned objectives and test-matrix envelope of the FLEX-2 droplet experiments on the ISS, from the FLEX-2 Science Requirements Document (March 2010) — a plan, not a results report.
status: stable
generated: { by: "claude-code/opus-5.5", at: 2026-09-24T07:55:18Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-24T07:55:18Z }
order: 25
geometry_class: droplet-combustion
verified:
  - by: "human:muhammad-marjan-ahmed"
    at: 2026-09-24T07:55:18Z
sources:
  - id: flex-2-srd
    title: "Fundamental Studies in Droplet Combustion and Flame Extinguishment in Microgravity (FLEX-2) — Science Requirements Document, SRD Rev. 1"
    resource: "FLEX-2 Science Requirements Document, research team lead Forman A. Williams (UC San Diego), project scientist Michael C. Hicks (NASA Glenn), dated March 15, 2010; distributed in the NASA Physical Sciences Informatics (PSI) archive as 'FLEX-2 SRD Final.pdf'"
---

> [!NOTE]
> Geometry class: **droplet combustion**, the same class as [FLEX](flex.md) and
> [CFI](cfi.md). Not directly comparable with solid-fuel or gaseous-flame
> investigations.

> [!WARNING]
> This source is a **requirements document written before the flights**. It
> states what FLEX-2 was designed to measure and the envelope of conditions it
> planned — "Detailed experimental test points are not provided at this time."
> It contains no flight results. Nothing here says what was actually flown.

FLEX-2 studies several fundamental aspects of droplet combustion with the
droplet apparatus (MDCA) in the Combustion Integrated Rack (CIR) on the
International Space Station (ISS), focusing on large droplets with burning
times of the order of tens of seconds. It builds on the earlier flight
experiments DCE, FSDC-1 and FSDC-2, which used heptane and methanol.[^flex-2-srd]

## Planned experiment categories and objectives

The independently varied parameters are fuel type, ambient gas composition,
ambient pressure, droplet initial diameter, droplet translation velocity, and
droplet spacing and initial size in a binary linear array.[^flex-2-srd]

- **Pure fuel experiments** (decane and ethanol): determine diffusive and
  radiative flame extinction boundaries in atmospheres containing N2 or He at
  pressures ranging from 0.5 atm to 3.0 atm; measure droplet extinction
  diameters for validation of chemical kinetic models; measure soot volume
  fractions and soot temperatures; measure radiant emissions.
- **Fuel mixture experiments**: propanol/glycerol and heptane/hexadecane to
  study liquid-phase diffusion and preferential evaporation; heptane/octane
  and decane/propylbenzene to simulate "real" fuels such as gasoline and jet
  fuel (JP8 surrogates).
- **Convective droplet experiments**: slow imposed flows (Reynolds number of
  order unity) — radiative and diffusive extinction limits, droplet regression
  rates for sooting (decane) and non-sooting (ethanol) fuels, flame stand-off
  distance and shape.
- **Droplet array experiments**: the flammability map and burning rate
  constant k of a binary droplet array as a function of spacing.

## Structured facts

Every value below is drawn from the single source cited throughout this
document.

### Test matrix envelope (source Table 2)

| Parameter | Value |
| --- | --- |
| Pure fuels | n-decane, ethanol |
| Fuel mixtures | n-heptane/n-hexadecane; 1-propanol/glycerol; n-heptane/iso-octane (2,2,4 trimethylpentane); n-decane/n-propylbenzene |
| Ambient gas | O2/N2 and O2/He mixtures |
| Oxygen mole fraction | 0.17, 0.21, 0.25, and 0.30 |
| Ambient pressure | 0.5, 1.0, 1.5, 2.0, and 3.0 atm. |
| Initial droplet size | 1.5 to 5.0 mm |
| Arrays configuration | binary linear |
| Flow velocity | 0.1 to 5 cm/s |

### Estimated number of tests (source Table 3, planning estimate)

| Category | Fuel | Tests |
| --- | --- | --- |
| Pure fuel (quiescent) | n-decane | 100 |
| Pure fuel (quiescent) | ethanol | 100 |
| Pure fuel (flow) | n-decane | 50 |
| Pure fuel (flow) | ethanol | 50 |

The remaining rows of Table 3 (arrays and mixtures) did not survive text
extraction in a form that can be read row by row, and are not reproduced.

## Open questions

- **What actually flew.** This SRD plans the tests; it does not report them.
  The PSI experimental table for FLEX-2 lists one row per fuel with the same
  condition envelope as Table 2 above, but names some fuels (e.g. pure
  iso-octane and n-octane) that differ from this plan — see
  [the PSI experimental tables](../../data-sources/psi-experimental-tables.md).
  Which fuels were flown is not established by this source.
- The apparatus is named "Multiple Droplet Combustion Apparatus" here, while
  the [CFI](cfi.md) report writes "Multi-used Droplet Combustion Apparatus";
  both refer to the MDCA.
- No FLEX-2 results report is among the sources of this record.

[^flex-2-srd]: FLEX-2 Science Requirements Document (Williams et al.; March 15, 2010). §4 Flight Experiment Description: "The flight experiment utilizes the Multiple Droplet Combustion Apparatus (MDCA) installed in the Combustion Integrated Rack (CIR) in the International Space Station (ISS)... Combustion of large droplets with burning times of the order of tens of seconds are the focus of the flight experiments... The independently varied experimental parameters during FLEX-2 experiments are: 1) Fuel type, 2)Ambient gas composition, 3)Ambient Pressure, 4)Droplet initial diameter, 5)Droplet translation velocity (and acceleration) and 6)Droplet spacing and initial size in a binary linear array." §4.1: "decane (C10H22) and ethanol (C2H5OH) fuels are chosen so that we can build on the results of our earlier flight experiments (DCE, FSDC-1 and FSDC-2) with heptane and methanol... Determine diffusive and radiative flame extinction boundaries for ethanol and decane droplets in test atmospheres containing N2 or He at pressures ranging from 0.5 atm to 3.0 atm... Propanol/glycerol and heptane/hexadecane mixtures are used to examine the role of liq- uid phase diffusion, preferential evaporation, and mixing... Heptane/octane and decane/propylbenzene experiments are focussed on simulating the characteristics of 'real' fuels, like gasoline and jet fuels... JP8 surrogate fuel mixtures... The imposed flow velocities are such that the Reynolds number based on initial droplet diameter is of the order unity... Measure droplet regression rates for sooting (decane) and non sooting (ethanol) fuels... Measure variations in burning rate constant k." §4.2 Test Matrix Envelope: "Detailed experimental test points are not provided at this time." Table 2: "Pure Fuels n-decane, ethanol; Fuel Mixtures n-heptane/n-hexadecane mixtures, 1-propanol/glycerol mixtures, n-heptane/iso-octane (2,2,4 trimethylpentane), n-decane/n-propylbenzene; Ambient Gas O2=N2 mixtures, O2=He mixtures; Oxygen mole fraction 0.17, 0.21, 0.25, and 0.30; Ambient Pressure 0.5, 1.0, 1.5, 2.0, and 3.0 atm.; Initial Droplet Size 1.5 to 5.0 mm; Arrays Configuration binary linear; Flow Velocity 0.1 to 5 cm/s." Table 3 (Estimated Number of Tests): "Pure Fuel (quiescent) n-decane 100, ethanol 100; Pure Fuel (flow) n-decane 50, ethanol 50."
