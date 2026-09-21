---
type: Document
title: "FLEX: Flame Extinguishment Experiment"
description: Droplet-combustion tests aboard the ISS Combustion Integrated Rack — full apparatus, procedure, and the complete 275-test results table from March 2009 to December 2011.
status: stable
generated: { by: "claude-code/sonnet-5", at: 2026-09-21T19:56:58Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-21T19:56:58Z }
order: 22
geometry_class: droplet-combustion
sources:
  - id: flex-tp-2015
    title: "Detailed Results From the Flame Extinguishment Experiment (FLEX) March 2009 to December 2011"
    resource: "https://ntrs.nasa.gov/citations/20150023456"
verified:
  - by: human:you
    at: 2026-09-21T19:56:58Z
---

> [!NOTE]
> Geometry class: **droplet combustion**. Not directly comparable to
> [BASS-II](../solid-fuel/bass-ii.md) or [SAFFIRE](../solid-fuel/saffire.md)
> (large-scale solid-fuel burns) or [ACME](../gaseous-flames/acme.md)
> (gaseous laminar flames) without noting the geometry mismatch — FLEX burns
> a single spherical liquid-fuel droplet, a fundamentally different flame
> structure from a solid-fuel surface burn or a gaseous jet flame.

> [!IMPORTANT]
> This source explicitly declines to interpret its own results: "The intent
> is not to interpret the experimental results but rather to make them
> available to the entire scientific community for possible future
> interpretations."[^flex-tp-2015] This entry reports the full apparatus,
> procedure, and results catalog as the source presents it — it is not a
> findings report, and no scientific conclusions are drawn here that the
> source itself does not draw.

FLEX studied the spherically symmetric combustion of single liquid-fuel
droplets aboard the ISS, using the Multi-User Droplet Combustion Apparatus
(MDCA) inside the Combustion Integrated Rack (CIR) in the Destiny
module. Spherical symmetry is only achievable in microgravity — natural
convection destroys it in normal gravity — which is why this class of
experiment requires spaceflight.[^flex-tp-2015]

## Apparatus and hardware

The CIR is a 90-liter combustion chamber that can operate at pressures of
approximately 0 to 9 atm, though a conservative safety analysis reduced the
maximum working pressure for FLEX to approximately 3 atm. Ambient conditions
are controlled by the Fuel and Oxidizer Mixing Apparatus (FOMA) — gas
bottles, an ISS-nitrogen connection, pressure transducers, and mass flow
controllers — with chamber contents evacuable via the ISS overboard
vent.

The MDCA, based on the Space Shuttle Droplet Combustion Experiment design,
deploys both free and fiber-supported droplets in a quiescent microgravity
environment. Stainless-steel tubes with 250-µm outside diameters dispense
fuel from two crew-replaceable reservoirs (one per fuel: methanol or
heptane), each loaded with about 2.5 mL of methanol or 1.25 mL of heptane per
the safety analysis. During a test, the syringe dispenses fluid between
horizontally opposed needles, which stretch until nearly the point the fluid
would pull off, then rapidly retract — ideally leaving a motionless droplet
floating in the chamber center — at which point two hot-wire igniters
(180° apart) fire for a preset time, then retract. Fiber-supported tests use
the same procedure but deploy the droplet on an 80-µm support fiber, with
some tests translating the fiber at a prescribed speed for cases needing
controlled subbuoyant convective flow.[^flex-tp-2015]

## Diagnostics

Three imaging systems recorded each test:

- **HiBMs** (High-Bit-Depth Multispectral) — a backlit, laser-diode-illuminated
  view of the droplet at 650–660 nm, full 1024×1024 array, 12-bit output,
  ~30 fps, ~30 mm FOV on a side. Measures droplet size and (for soot-producing
  heptane flames) soot volume fraction.
- **LLUV** (Low Light Level Ultra-Violet) — images hydroxyl (OH•)
  chemiluminescence at a 310-nm notch filter (10-nm FWHM), 1024×1024
  monochrome CCD coupled to an 18-mm Gen II-UV microchannel plate intensifier,
  used at 2×2 binning (512×512), ~50 mm FOV, mostly 30 fps (some 15 fps for
  dim flames).
- **MDCA color camera** — a visual overview (110×90 mm FOV) with white-LED
  illumination during droplet formation, downlinked during nominal operations
  for flame size/shape/color.

Two radiometers (broadband and water-vapor-filtered) were installed but were
not sensitive enough to provide reliable quantitative data for the tests in
this report, so radiometer data is not reported.[^flex-tp-2015]

## Experimental procedure

Test-point operations required three Telescience Support Center (Glenn)
operators plus a science-team representative, following a fixed sequence:
activate the CIR; fill the chamber to the target pressure/composition via
FOMA (recording pressure history to compute actual composition after the
fact); activate the MDCA; purge the fuel line; dispense and stretch the
droplet; then — under automated control — start recording, deploy the
droplet, ignite (preset time/power), retract the igniter, and stop recording
(typically ~40 s later); finally perform housekeeping and, if reusing the
same atmosphere, run the circulation fan (~1 min) to mix gases
uniformly. The Passive Rack Isolation System (PaRIS) isolated
the CIR from higher-frequency ISS vibration/g-jitter; for every test in this
report, the g-environment was low enough that buoyant flow was negligible,
though g-jitter still caused droplet drift, sometimes out of camera
FOV.[^flex-tp-2015]

## Image analysis methods and measurement uncertainty

All three camera streams were analyzed semi-automatically (Image J or Igor
Pro): identify in-FOV frames, denoise, set a manually-tuned segmentation
threshold, fill holes/remove stray objects, then measure area, center of
mass, and perimeter, converted to a size via a scale factor.
Reported measurement uncertainty, by camera:

| Camera | Scale factor | Spatial resolution | Estimated size uncertainty |
| --- | --- | --- | --- |
| HiBMs (droplet) | 32.5 pixels/mm | ±29.5 µm | ±50 µm |
| LLUV (flame, OH• edge) | 8.86 pixels/mm | ±113 µm | ±200 µm |
| MDCA color camera (flame, visible edge) | 6.87 pixels/mm | ±146 µm | ±250 µm |

The LLUV flame dimension is the outer edge of OH• chemiluminescence; the
color-camera flame dimension is the outer edge of the visible flame. For
almost all tests the LLUV-measured diameter is larger than the color-camera
diameter — typically the color-camera figure is about three-fourths of the
LLUV figure — because LLUV is sensitive to OH• chemiluminescence (which peaks
outside the visible flame), an effect that grows larger for sooty heptane
flames where soot luminosity (invisible to LLUV) dominates the color-camera
image and peaks inside the blue flame envelope.[^flex-tp-2015]

## Structured facts

### Experimental conditions

| Field | Value | Report section |
| --- | --- | --- |
| Facility | Multi-User Droplet Combustion Apparatus (MDCA), Combustion Integrated Rack (CIR), ISS Destiny module | Executive Summary |
| Fuels tested | methanol and n-heptane | Executive Summary |
| Droplet initial diameter | 2 to 5 mm | Executive Summary |
| Ambient pressure range | 0.70 to 3.05 atm | Executive Summary |
| Most tests conducted at | 0.7 to 1 atm, many in air | Executive Summary |
| Dilution ranges tested | oxygen diluted with nitrogen, with carbon dioxide, with helium, and with mixtures of these (see full table below) | Executive Summary; §4.1/Appendix A |
| Total tests reported | first 284 tests performed; 275 appear as individually tabulated rows in the source's own Table IX (see notes below the table) | Executive Summary; Appendix A |

### Measured outcomes

| Field | Value | Report section |
| --- | --- | --- |
| Useful combustion histories obtained | more than 100 | §6.0 Conclusions |
| Extinction modes observed | radiative extinction (higher dilutions), diffusive extinction (lower dilutions), and disruptive extinctions, for both fuels | Executive Summary |
| Limiting oxygen index (LOI) | observed values "appear to be slightly lower than initially expected" — no single summary percentage is stated in the report's own overview; per-test conditions at which each test ended (Extinction/Disruption/Completion) are in the full table below | Executive Summary |
| Color-camera vs. LLUV flame diameter | color-camera flame diameters are smaller — approximately three-fourths of the LLUV (hydroxyl-filter) results | Executive Summary |

## Full per-test results (Table IX)

The source's Table IX (Appendix A.2) is reproduced here in full: every
individually tabulated test, its ambient composition, droplet size, burn
outcome, and how the test ended. Column definitions, per the source's own
"A.1 Summary Data" key:[^flex-tp-2015]

- **Test** / **Identifier** — the FLEX science-team test number and the CIR
  engineering-team identifier for the same test.
- **Date** / **GMT time** — when the test was performed.
- **Fuel** — methanol (CH3OH) or heptane (C7H16).
- **Pressure** — absolute ambient pressure (mmHg).
- **O2 / N2 / CO2 / He** — ambient mole fractions from detailed records of
  chamber fill, recirculation, filter, and combustion history. A dash (`-`)
  in any data column below means the source reports no value for that field
  (droplet left the camera FOV, sensor did not record, or similar); a value
  of `not stated` in the He column specifically means the source's own table
  segment for that row's page did not carry a fourth composition column at
  all (see notes below).
- **Initial diameter** — droplet diameter at time zero (igniters ON), mm.
- **Extinction diameter** — droplet diameter when the visible flame
  extinguished, mm; `-` means the flame did not visibly extinguish (droplet
  burned to completion, or disruption ended the test).
- **Burning rate** — average burning-rate constant from a linear fit of
  droplet-diameter-squared vs. time, mm²/s.
- **Burn time** — seconds from ignition to the recorded end condition.
- **Test end** — how the test concluded: `Extinction` (visible flame went
  out with droplet remaining), `Disruption` (droplet broke apart, ending
  useful burning history), or `Completion` (droplet fully consumed).

| Test | Identifier | Date | GMT time | Fuel | Pressure (mmHg) | O2 | N2 | CO2 | He | Initial diameter (mm) | Extinction diameter (mm) | Burning rate (mm2/s) | Burn time (s) | Test end |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLEX-001 | 20CAL08 | 3/5/09 | 17:22:03 | Methanol | 757.7 | 0.21 | 0.79 | 0 | 0 | 1.69 | 0.89 | 0.52 | 4.3 | Disruption |
| FLEX-002 | 20CAL10 | 3/5/09 | 19:20:06 | Methanol | 762 | .21 | .79 | 0 | 0 | 1.86 | .94 | .6 | 5 | Extinction |
| FLEX-003 | 20CAL12 | 3/5/09 | 21:17:46 | Methanol | 764.2 | .21 | .79 | 0 | 0 | 1.61 | .92 | .58 | 3.2 | Extinction |
| FLEX-004 | 30CAL02 | 3/31/09 | 17:16:18 | Methanol | 760 | .21 | .79 | 0 | 0 | 2.06 | - | .6 | 7.64 | Extinction |
| FLEX-005 | 30CAL03 | 3/31/09 | 19:00:48 | Methanol | 760 | .21 | .79 | 0 | 0 | 1.92 | .81 | .48 | 6.34 | Extinction |
| FLEX-006 | 40CAL01 | 3/31/09 | 20:05:49 | Methanol | 760 | .21 | .79 | 0 | 0 | 2.54 | 1.53 | .51 | 9.6 | Extinction |
| FLEX-007 | 20CAL13 | 4/10/09 | 13:26:11 | Heptane | 761.3 | .21 | .79 | 0 | 0 | 1.87 | - | .67 | 5.3 | Disruption |
| FLEX-008 | 30CAL06 | 4/10/09 | 18:07:15 | Heptane | 762.4 | .21 | .79 | 0 | 0 | 2.95 | - | .79 | 14.8 | Disruption |
| FLEX-009 | 30CAL07 | 4/10/09 | - | Heptane | 760 | .21 | .79 | 0 | 0 | - | - | - | - | Disruption |
| FLEX-010 | 256F002 | 5/22/09 | 14:53:27 | Methanol | 2319.7 | .21 | .09 | .7 | 0 | 3.86 | - | .37 | 13.6 | Extinction |
| FLEX-011 | 256R001 | 5/22/09 | 15:33:47 | Methanol | 2318.8 | .21 | .09 | .7 | 0 | 3.03 | - | .4 | 16.5 | Extinction |
| FLEX-012 | 264F003 | 5/22/09 | 19:23:35 | Heptane | 2319.9 | .21 | .09 | .7 | 0 | 2.74 | - | - | - | Disruption |
| FLEX-013 | 256R002 | 6/25/09 | 15:33:05 | Methanol | 2074.2 | .21 | .09 | .7 | 0 | 2.59 | - | .49 | 10.8 | Extinction |
| FLEX-014 | 256F007 | 6/29/09 | 12:26:06 | Methanol | 2055.6 | .21 | .09 | .7 | 0 | 3.7 | - | - | 11.3 | Extinction |
| FLEX-015 | 256F008 | 6/29/09 | 13:56:06 | Methanol | 2066.6 | .21 | .09 | .7 | 0 | 4.42 | - | - | 23.1 | Extinction |
| FLEX-016 | 256F009 | 6/29/09 | 15:34:58 | Methanol | 2072.1 | .21 | .09 | .7 | 0 | 1.66 | 1 | .53 | 3.4 | Extinction |
| FLEX-017 | 240R003 | 7/1/09 | 12:28:41 | Methanol | 1545.7 | .21 | .09 | .7 | 0 | 2.67 | - | - | 2.4 | Disruption |
| FLEX-018 | 248F001 | 7/1/09 | 16:28:56 | Heptane | 1553.8 | .21 | .09 | .7 | 0 | 2.74 | 1.77 | .61 | 8.1 | Extinction |
| FLEX-019 | 196F001 | 8/26/09 | 19:07:28 | Heptane | 539.1 | .34 | .66 | 0 | 0 | 3.39 | - | .9 | 4.2 | Disruption |
| FLEX-020 | 192F001 | 10/24/09 | 14:09:04 | Methanol | 539.5 | .34 | .66 | 0 | 0 | 3.4 | 1.56 | .53 | 17.4 | Completion |
| FLEX-021 | 192F002 | 10/24/09 | 15:15:24 | Methanol | 540.6 | .34 | .66 | 0 | 0 | 3.49 | .95 | .66 | 17.8 | Disruption |
| FLEX-022 | 192F003 | 10/24/09 | 15:39:48 | Methanol | 540.5 | .34 | .66 | 0 | 0 | 3.5 | - | .65 | 18.2 | Disruption |
| FLEX-023 | 196F002 | 10/24/09 | 18:29:53 | Heptane | 541.8 | .34 | .66 | 0 | 0 | 3.01 | - | .73 | 13.1 | Disruption |
| FLEX-024 | 196F003 | 10/24/09 | 19:44:04 | Heptane | 542.8 | .34 | .66 | 0 | 0 | - | - | - | - | Disruption |
| FLEX-025 | 191R001 | 11/9/09 | 11:42:23 | Methanol | 537.3 | .3 | .7 | 0 | 0 | 2.6 | .59 | .65 | 10.3 | Completion |
| FLEX-026 | 191F001 | 11/9/09 | 11:59:59 | Methanol | 538.4 | .3 | .7 | 0 | 0 | 3.63 | .4 | .62 | 22.2 | Disruption |
| FLEX-027 | 195F001 | 11/9/09 | 14:04:11 | Heptane | 540.7 | .3 | .7 | 0 | 0 | 3.87 | - | .64 | 23.8 | Disruption |
| FLEX-028 | 195F002 | 11/9/09 | 14:56:05 | Heptane | 539.7 | .3 | .7 | 0 | 0 | 3.36 | - | .64 | 17.3 | Disruption |
| FLEX-029 | 178R001 | 11/13/09 | 13:11:23 | Methanol | 766.9 | .3 | .7 | 0 | 0 | 2.57 | - | .74 | 10.4 | Completion |
| FLEX-030 | 178F001 | 11/13/09 | 14:03:46 | Methanol | 769.2 | .3 | .7 | 0 | 0 | 3.26 | 1.32 | .59 | 15.6 | Extinction |
| FLEX-031 | 182F001 | 11/13/09 | 18:33:39 | Heptane | 770.5 | .3 | .7 | 0 | 0 | 3.39 | - | .85 | 18.4 | Disruption |
| FLEX-032 | 182F002 | 11/13/09 | 19:04:33 | Heptane | 771 | .3 | .7 | 0 | not stated | 3.07 | - | .68 | 14 | Completion |
| FLEX-033 | 177R002 | 11/27/09 | 10:02:15 | Methanol | 764.5 | .21 | .79 | 0 | not stated | 2.62 | 1.25 | .48 | 11.4 | Extinction |
| FLEX-034 | 177F001 | 11/27/09 | 11:15:38 | Methanol | 767.7 | .21 | .79 | 0 | not stated | 3.89 | 2 | .44 | 27.3 | Extinction |
| FLEX-035 | 181F001 | 11/27/09 | 13:01:24 | Heptane | 768.1 | .21 | .79 | 0 | not stated | 3.85 | 3.34 | .43 | 8.9 | Extinction |
| FLEX-036 | 190R002 | 12/15/09 | 10:39:35 | Methanol | 539 | .2 | .8 | 0 | not stated | 2.4 | 1.67 | .45 | 7.1 | Extinction |
| FLEX-037 | 220R001 | 1/7/10 | 19:08:46 | Methanol | 534.3 | .34 | .66 | 0 | not stated | 3.31 | - | .72 | 10.7 | Disruption |
| FLEX-038 | 220R002 | 1/7/10 | 19:20:38 | Methanol | 534.4 | .34 | .66 | 0 | not stated | 3.59 | - | .71 | 15.3 | Disruption |
| FLEX-039 | 224F001 | 1/7/10 | 21:51:19 | Heptane | 534.9 | .34 | .66 | 0 | not stated | 2.91 | 0 | .8 | 9.9 | Disruption |
| FLEX-040 | 219R001 | 1/8/10 | 5:02:52 | Methanol | 535.1 | .3 | .7 | 0 | not stated | 3.77 | - | .62 | 19.2 | Disruption |
| FLEX-041 | 219F001 | 1/8/10 | 4:41:55 | Methanol | 534.3 | .3 | .7 | 0 | not stated | 3.35 | - | .65 | 14.1 | Disruption |
| FLEX-042 | 223F001 | 1/8/10 | 1:02:04 | Heptane | 535 | .3 | .7 | 0 | not stated | 2.92 | - | .58 | 11.3 | Disruption |
| FLEX-043 | 223F002 | 1/8/10 | 3:16:16 | Heptane | 534.9 | .3 | .7 | 0 | not stated | 2.97 | 0 | .78 | 11.4 | Disruption |
| FLEX-044 | 206F001 | 1/11/10 | 10:33:22 | Methanol | 766.8 | .3 | .7 | 0 | not stated | 3.49 | - | .63 | 16.6 | Disruption |
| FLEX-045 | 206R001 | 1/11/10 | 10:54:25 | Methanol | 768.3 | .3 | .7 | 0 | not stated | 2.42 | 1.01 | .73 | 6.6 | Extinction |
| FLEX-046 | 205R001 | 1/12/10 | 13:14:25 | Methanol | 769.5 | .21 | .79 | 0 | not stated | 2.78 | 1.08 | .54 | 13.1 | Disruption |
| FLEX-047 | 209F001 | 1/12/10 | 15:48:17 | Heptane | 770.1 | .21 | .79 | 0 | not stated | 3.36 | - | .5 | 17.1 | Completion |
| FLEX-048 | 205F001 | 1/12/10 | 12:14:55 | Methanol | 768.7 | .21 | .79 | 0 | not stated | 3.66 | - | .27 | 23.5 | Disruption |
| FLEX-049 | 209F003 | 1/19/10 | 9:09:16 | Heptane | 764.9 | .21 | .79 | 0 | not stated | 3.46 | 2.78 | .59 | 8.6 | Extinction |
| FLEX-050 | 209F004 | 1/19/10 | 14:08:17 | Heptane | 770.1 | .21 | .79 | 0 | not stated | 3.57 | 2.98 | .52 | 8.4 | Extinction |
| FLEX-051 | 209F005 | 1/19/10 | 16:38:35 | Heptane | 771.4 | .21 | .79 | 0 | not stated | 2.41 | 0 | .65 | 8.2 | Completion |
| FLEX-052 | 210F002 | 1/11/10 | 13:46:44 | Heptane | 771.1 | .3 | .7 | 0 | not stated | 3.53 | 0 | .7 | 18.3 | Disruption |
| FLEX-053 | 209F002 | 1/12/10 | 16:29:37 | Heptane | 770.2 | .21 | .79 | 0 | not stated | - | - | - | 18.5 | Disruption |
| FLEX-054 | 190F003 | 1/29/10 | 11:27:01 | Methanol | 541.4 | .2 | .8 | 0 | not stated | 3.56 | - | .41 | 29 | Extinction |
| FLEX-055 | 218F001 | 1/29/10 | 16:06:50 | Methanol | 542.6 | .2 | .8 | 0 | not stated | 3.37 | 2.39 | .46 | 20.5 | Disruption |
| FLEX-056 | 194F001 | 1/29/10 | 19:13:22 | Heptane | 544.1 | .2 | .79 | 0 | not stated | 3.56 | 3.04 | .44 | 7.9 | Completion |
| FLEX-057 | 303F001 | 1/29/10 | 19:50:16 | Heptane | 544.4 | .2 | .79 | 0 | not stated | 3.1 | 2.49 | .54 | 6.8 | Extinction |
| FLEX-058 | 176F001 | 2/4/10 | 2:32:01 | Methanol | 773.3 | .18 | .82 | 0 | not stated | 3.69 | - | .42 | 29.1 | Extinction |
| FLEX-059 | 176R001 | 2/4/10 | 0:26:28 | Methanol | 769.2 | .18 | .82 | 0 | not stated | 2.93 | 1.39 | .43 | 17.7 | Extinction |
| FLEX-060 | 204F001 | 2/4/10 | 3:26:05 | Methanol | 773.7 | .18 | .82 | 0 | not stated | 3.43 | - | .45 | 23.2 | Extinction |
| FLEX-061 | 204R001 | 2/4/10 | 3:52:39 | Methanol | 774.1 | .18 | .82 | 0 | not stated | 3.68 | 2 | .41 | 25.7 | Extinction |
| FLEX-062 | 301F001 | 3/11/10 | 21:37:48 | Heptane | 761.8 | .18 | .82 | 0 | not stated | 3.43 | 3.17 | .39 | 4.8 | Extinction |
| FLEX-063 | 301F002 | 3/11/10 | 23:07:51 | Heptane | 767.6 | .18 | .81 | 0 | not stated | 2.15 | 0 | .51 | 9.6 | Completion |
| FLEX-064 | 302F001 | 3/11/10 | 22:12:39 | Heptane | 764.6 | .18 | .81 | 0 | not stated | 2.69 | 2.07 | .6 | 5.5 | Extinction |
| FLEX-066 | 189F001 | 3/19/10 | 9:26:45 | Methanol | 766.8 | .15 | .85 | 0 | 0 | 2.52 | 1.32 | .38 | 12.9 | Extinction |
| FLEX-067 | 189F002 | 3/19/10 | 10:17:06 | Methanol | 767.7 | .15 | .85 | 0 | 0 | 3.97 | 3.3 | .36 | 14.4 | Extinction |
| FLEX-068 | 189R003 | 3/19/10 | 12:04:45 | Methanol | 768.8 | .15 | .84 | 0 | 0 | 2.38 | 1.29 | .39 | 10.7 | Extinction |
| FLEX-069 | 193R002 | 3/23/10 | 10:23:00 | Heptane | 767.1 | .14 | .84 | 0 | 0 | 1.1 | 0 | .94 | 1.3 | Completion |
| FLEX-070 | 193F001 | 3/23/10 | 7:25:43 | Heptane | 761 | .15 | .84 | 0 | 0 | 4.67 | 4.6 | .41 | 1.6 | Extinction |
| FLEX-071 | 189R002 | 3/19/10 | 11:19:22 | Methanol | 768.3 | .15 | .84 | 0 | 0 | 2.25 | - | .4 | 8.4 | Extinction |
| FLEX-072 | 193R001 | 3/23/10 | 9:06:37 | Heptane | 765.2 | .15 | .84 | 0 | 0 | 1.13 | - | .52 | 2.5 | Completion |
| FLEX-073 | 193F001 | 3/23/10 | 7:25:43 | Heptane | 761 | .15 | .84 | 0 | 0 | 4.64 | 4.58 | .56 | 1.5 | Extinction |
| FLEX-074 | 221F001 | 3/23/10 | 9:44:36 | Heptane | 765.9 | .15 | .84 | 0 | 0 | 1.33 | - | .77 | 2.3 | Completion |
| FLEX-075 | 203R002 | 3/29/10 | 21:06:40 | Methanol | 770.8 | .13 | .85 | 0 | 0 | 2.54 | 1.78 | .37 | 9.1 | Extinction |
| FLEX-076 | 203F001 | 3/29/10 | 19:24:36 | Methanol | 769.5 | .13 | .85 | 0 | 0 | 3.21 | 2.78 | .37 | 8.9 | Extinction |
| FLEX-077 | 175R001 | 3/29/10 | 18:39:20 | Methanol | 768.4 | .14 | .85 | 0 | 0 | 3.33 | 2.91 | .34 | 8.5 | Extinction |
| FLEX-078 | 175F001 | 3/29/10 | 17:49:23 | Methanol | 766 | .14 | .85 | 0 | 0 | 2.66 | 1.66 | .35 | 12.9 | Extinction |
| FLEX-079 | 179F001 | 3/30/10 | 0:40:16 | Heptane | 768.1 | .13 | .85 | 0 | 0 | 2.92 | 2.86 | .25 | 1.5 | Extinction |
| FLEX-080 | 207F001 | 3/30/10 | 2:29:19 | Heptane | 770 | .13 | .85 | 0 | 0 | - | - | - | 1 | Extinction |
| FLEX-081 | 207F002 | 3/30/10 | 3:59:28 | Heptane | 770.2 | .13 | .85 | 0 | 0 | - | - | - | 1.5 | Extinction |
| FLEX-082 | 304F001 | 4/19/10 | 17:19:17 | Methanol | 764.6 | .13 | .87 | 0 | 0 | 2.84 | 2.39 | .35 | 7.5 | Extinction |
| FLEX-083 | 304F002 | 4/19/10 | 21:18:05 | Methanol | 772 | .12 | .87 | 0 | 0 | - | - | - | 5.45 | Extinction |
| FLEX-084 | 304R001 | 4/19/10 | 17:51:24 | Methanol | 767.2 | .12 | .87 | 0 | 0 | 2.35 | 1.42 | .35 | 10.8 | Extinction |
| FLEX-085 | 304R002 | 4/19/10 | 20:12:58 | Methanol | 771.2 | .12 | .87 | 0 | 0 | 2.4 | 1.77 | .35 | 9.3 | Extinction |
| FLEX-086 | 305F002 | 4/19/10 | 19:16:37 | Methanol | 770 | .12 | .87 | 0 | 0 | 3.07 | 2.56 | .35 | 9 | Extinction |
| FLEX-087 | 305F003 | 4/19/10 | 20:38:54 | Methanol | 771.2 | .12 | .87 | 0 | 0 | 2.64 | 1.92 | .38 | 9.3 | Extinction |
| FLEX-088 | 053R001 | 5/5/10 | 22:37:54 | Methanol | 537.5 | .25 | .6 | .15 | 0 | 3.01 | - | .53 | 14.8 | Disruption |
| FLEX-089 | 053F001 | 5/5/10 | 22:19:33 | Methanol | 537.4 | .25 | .6 | .15 | 0 | 3.7 | - | .51 | 24 | Disruption |
| FLEX-090 | 141R001 | 5/6/10 | 0:07:51 | Methanol | 539.2 | .25 | .6 | .15 | 0 | 3.62 | - | .53 | 20.1 | Disruption |
| FLEX-091 | 141F001 | 5/5/10 | 23:10:01 | Methanol | 538.3 | .25 | .6 | .15 | 0 | 3.51 | - | .51 | 18 | Disruption |
| FLEX-092 | 061F002 | 6/14/10 | 22:54:56 | Heptane | 536.3 | .25 | .6 | .15 | 0 | 3.41 | - | .55 | 21.7 | Disruption |
| FLEX-093 | 149F001 | 6/15/10 | 0:32:31 | Heptane | 537.3 | .25 | .6 | .15 | 0 | 2.48 | 0 | .71 | 8.3 | Disruption |
| FLEX-094 | C08H101 | 6/15/10 | 2:10:43 | Heptane | 533.6 | .24 | .56 | .2 | 0 | 3.53 | 2.76 | .51 | 10.1 | Extinction |
| FLEX-095 | C08H201 | 6/15/10 | 3:22:41 | Heptane | 534.4 | .24 | .56 | .2 | 0 | 3.6 | 3.04 | .58 | 8 | Extinction |
| FLEX-096 | C08H301 | 6/15/10 | 4:37:39 | Heptane | 534.4 | .24 | .56 | .2 | 0 | - | - | - | 5.2 | Disruption |
| FLEX-097 | C08M101 | 6/16/10 | 22:43:35 | Methanol | 534.2 | .23 | .56 | .2 | 0 | 4.25 | 2.6 | .45 | 26.5 | Completion |
| FLEX-098 | C09M201 | 6/21/10 | 14:21:26 | Methanol | 537.1 | .23 | .52 | .25 | 0 | 3.64 | 1.74 | .47 | 22.9 | Extinction |
| FLEX-099 | C09M101 | 6/21/10 | 12:57:34 | Methanol | 535 | .23 | .52 | .25 | 0 | 4.28 | 2.32 | .42 | 33 | Extinction |
| FLEX-100 | C09H101 | 6/29/10 | 8:30:46 | Heptane | 536.7 | .23 | .52 | .25 | 0 | 4.14 | 3.98 | .34 | 6.1 | Extinction |
| FLEX-101 | C09H201 | 6/29/10 | 9:38:10 | Heptane | 538.7 | .23 | .52 | .25 | 0 | 3.88 | 3.45 | .5 | 6.5 | Extinction |
| FLEX-102 | C10H101 | 6/29/10 | 11:21:09 | Heptane | 534.2 | .21 | .49 | .3 | 0 | 3.57 | 3.43 | .33 | 4.2 | Extinction |
| FLEX-103 | C10H201 | 6/29/10 | 11:56:02 | Heptane | 534.3 | .21 | .49 | .3 | 0 | 4 | 3.88 | .35 | 3.2 | Extinction |
| FLEX-104 | C08M201 | 6/16/10 | 23:04:00 | Methanol | 534.1 | .23 | .56 | .2 | 0 | 3.6 | 1.58 | .49 | 23.2 | Extinction |
| FLEX-105 | C08M301 | 6/16/10 | 23:29:19 | Methanol | 534.6 | .23 | .56 | .2 | 0 | 4.17 | 2 | .47 | 30.7 | Disruption |
| FLEX-106 | C09M401 | 6/21/10 | 15:52:51 | Methanol | 538.3 | .23 | .52 | .25 | 0 | 3.08 | 1.75 | .51 | 14.1 | Disruption |
| FLEX-107 | C08M401 | 6/16/10 | 23:51:26 | Methanol | 535 | .23 | .56 | .2 | 0 | 3.18 | - | .52 | 15.1 | Disruption |
| FLEX-108 | C09M301 | 6/21/10 | 15:35:57 | Methanol | 538.3 | .23 | .52 | .25 | 0 | 3.75 | - | .47 | 24.3 | Completion |
| FLEX-109 | C10M102 | 8/31/10 | 5:38:01 | Methanol | 536.5 | .21 | .49 | .3 | 0 | 3.56 | 1.92 | .42 | - | Extinction |
| FLEX-110 | C10M201 | 8/31/10 | 7:16:40 | Methanol | 537 | .21 | .49 | .3 | 0 | 2.83 | 1.57 | .45 | 13 | Extinction |
| FLEX-111 | C10M303 | 8/31/10 | 8:58:24 | Methanol | 536.9 | .21 | .49 | .3 | 0 | 3.37 | 2.1 | .45 | 16.4 | Completion |
| FLEX-112 | C10M401 | 9/1/10 | 15:27:44 | Methanol | 530.7 | .21 | .49 | .3 | 0 | 3.99 | 2.35 | .43 | 25.2 | Completion |
| FLEX-113 | C11M101 | 9/1/10 | 19:17:58 | Methanol | 534.6 | .2 | .45 | .35 | 0 | 4.2 | 2.85 | .49 | 18.2 | Extinction |
| FLEX-114 | C11M201 | 9/6/10 | 19:14:22 | Methanol | 0 | .2 | .45 | .35 | 0 | 3.23 | 1.68 | .42 | 18.9 | Extinction |
| FLEX-115 | C11M301 | 9/1/10 | 20:40:16 | Methanol | 535.8 | .2 | .45 | .35 | 0 | 3.97 | 2.61 | .41 | 22.9 | Extinction |
| FLEX-116 | C11M401 | 9/1/10 | 20:57:41 | Methanol | 536.3 | .2 | .45 | .35 | 0 | 3.16 | 1.57 | .46 | 16.9 | Extinction |
| FLEX-117 | C11H101 | 9/6/10 | 18:14:53 | Heptane | 531.1 | .2 | .45 | .35 | 0 | 3.84 | 3.77 | .25 | 2.4 | Extinction |
| FLEX-118 | C11H201 | 9/6/10 | 19:14:22 | Heptane | 532.8 | .2 | .44 | .35 | 0 | 3.03 | 2.93 | .38 | 2.5 | Extinction |
| FLEX-119 | C12H103 | 9/7/10 | 1:50:01 | Heptane | 532.6 | .18 | .42 | .4 | 0 | 2.6 | 2.48 | .37 | 1.3 | Extinction |
| FLEX-120 | C12H201 | 9/7/10 | 1:08:26 | Heptane | 532.5 | .18 | .42 | .4 | 0 | 2.45 | 2.39 | .38 | 1.43 | Extinction |
| FLEX-121 | C12M101 | 9/8/10 | 19:21:31 | Methanol | 526.3 | .18 | .42 | .4 | 0 | 4.25 | 3.92 | .34 | 8 | Extinction |
| FLEX-122 | C12M201 | 9/8/10 | 21:44:37 | Methanol | 531.2 | .18 | .42 | .4 | 0 | 3.46 | 2.58 | .41 | 13.9 | Extinction |
| FLEX-123 | C12M301 | 9/8/10 | 22:16:51 | Methanol | 532 | .18 | .42 | .4 | 0 | 4.13 | 3.79 | .35 | 8.7 | Extinction |
| FLEX-124 | C12M401 | 9/8/10 | 22:45:54 | Methanol | 532.4 | .18 | .42 | .4 | 0 | 2.87 | 2.74 | .3 | 2.4 | Extinction |
| FLEX-125 | C13M103 | 9/13/10 | 21:07:02 | Methanol | 537.2 | .17 | .38 | .45 | 0 | 3.63 | 3.37 | .35 | 5.7 | Extinction |
| FLEX-126 | C13M201 | 9/13/10 | 18:11:39 | Methanol | 536.1 | .17 | .38 | .45 | 0 | 2.8 | 1.84 | .4 | 11.7 | Extinction |
| FLEX-127 | C13M301 | 9/13/10 | 19:22:49 | Methanol | 536.7 | .17 | .38 | .45 | 0 | 3.22 | 2.53 | .38 | 11 | Extinction |
| FLEX-128 | C13M401 | 9/13/10 | 19:49:24 | Methanol | 537.3 | .17 | .38 | .45 | 0 | 2.91 | - | .39 | 11.5 | Extinction |
| FLEX-129 | C13H102 | 9/17/10 | 1:32:49 | Heptane | 536.2 | .17 | .38 | .45 | 0 | 3.33 | 3.34 | .33 | .55 | Extinction |
| FLEX-130 | C13H201 | 9/17/10 | 3:55:59 | Heptane | 537.2 | .17 | .38 | .45 | 0 | 2.91 | 2.89 | .05 | .6 | Extinction |
| FLEX-131 | C21H101 | 10/6/10 | 11:28:52 | Heptane | 763.9 | .24 | .56 | .2 | 0 | 1.72 | .52 | .61 | 4.9 | Disruption |
| FLEX-132 | C21H201 | 10/6/10 | 12:59:06 | Heptane | 765.2 | .24 | .56 | .2 | 0 | 2.63 | .53 | .6 | 12.4 | Disruption |
| FLEX-133 | C21H301 | 10/6/10 | 13:59:59 | Heptane | 766.7 | .24 | .56 | .2 | 0 | 3.25 | .55 | .56 | 19 | Disruption |
| FLEX-134 | C21H401 | 10/6/10 | 14:57:06 | Heptane | 767.2 | .24 | .56 | .2 | 0 | 3.66 | 2.88 | .56 | 9.2 | Extinction |
| FLEX-135 | C21H501 | 10/6/10 | 16:22:15 | Heptane | 768.2 | .24 | .56 | .2 | 0 | 2.78 | 0 | .59 | 10.8 | Completion |
| FLEX-136 | C21H302 | 10/6/10 | 17:30:58 | Heptane | 768.1 | .24 | .56 | .2 | 0 | 3.08 | - | .51 | 17 | Completion |
| FLEX-137 | C21H303 | 10/6/10 | 17:53:35 | Heptane | 768.2 | .24 | .56 | .2 | 0 | 3.13 | - | .55 | 17.5 | Disruption |
| FLEX-138 | C21H304 | 10/6/10 | 18:08:43 | Heptane | 768.6 | .24 | .56 | .2 | 0 | - | - | - | - | Disruption |
| FLEX-139 | C21H305 | 10/6/10 | 19:09:45 | Heptane | 768 | .24 | .56 | .2 | 0 | 1.75 | - | .63 | 5.4 | Disruption |
| FLEX-140 | C14M101 | 11/4/10 | 16:52:39 | Methanol | 533.5 | .15 | .35 | .5 | 0 | 3.98 | 3.95 | .2 | 1.3 | Extinction |
| FLEX-141 | C14M201 | 11/4/10 | 18:07:51 | Methanol | 534.1 | .15 | .35 | .5 | 0 | 2.86 | 2.73 | .3 | 2.3 | Extinction |
| FLEX-142 | C14M301 | 11/4/10 | 19:11:39 | Methanol | 534.5 | .15 | .35 | .5 | 0 | 1.86 | 1.48 | .39 | 3.4 | Extinction |
| FLEX-143 | C14M302 | 11/4/10 | 20:19:22 | Methanol | 534.7 | .15 | .35 | .5 | 0 | 2.25 | 2.06 | .36 | 2.7 | Extinction |
| FLEX-144 | C01M101 | 11/16/10 | 9:42:08 | Methanol | 761.9 | .2 | .75 | .05 | 0 | 3.53 | 1.53 | .45 | 23.8 | Extinction |
| FLEX-145 | C01M201 | 11/16/10 | 10:21:24 | Methanol | 763.5 | .2 | .75 | .05 | 0 | 3.33 | 1.61 | .45 | 20 | Extinction |
| FLEX-146 | C01M301 | 11/16/10 | 10:54:23 | Methanol | 765.5 | .2 | .75 | .05 | 0 | 4.35 | 1.95 | .41 | 39.2 | Extinction |
| FLEX-147 | C13M102 | 9/13/10 | 17:35:49 | Methanol | 535.7 | .17 | .38 | .45 | 0 | 3.02 | 2.49 | .4 | 7.8 | Extinction |
| FLEX-148 | C01H101 | 11/18/10 | 8:39:27 | Heptane | 764.4 | .2 | .75 | .05 | 0 | 2.58 | 1.15 | .54 | 11.8 | Disruption |
| FLEX-149 | C01H201 | 11/18/10 | 9:25:38 | Heptane | 766.2 | .2 | .75 | .05 | 0 | 2.21 | .82 | .53 | 8.9 | Disruption |
| FLEX-150 | C01H302 | 11/18/10 | 10:17:02 | Heptane | 767.6 | .2 | .75 | .05 | 0 | 3.18 | 2.54 | .46 | 8 | Extinction |
| FLEX-151 | C03M101 | 12/8/10 | 18:31:22 | Methanol | 762.5 | .18 | .67 | .15 | 0 | 3.86 | - | .36 | 31.3 | Completion |
| FLEX-152 | C03M201 | 12/8/10 | 20:10:32 | Methanol | 765 | .18 | .67 | .15 | 0 | 3.33 | 1.23 | .43 | 23.2 | Extinction |
| FLEX-153 | C03M301 | 12/8/10 | 21:08:17 | Methanol | 765.6 | .18 | .67 | .15 | 0 | 2.78 | 1.19 | .42 | 15.7 | Extinction |
| FLEX-154 | C03H101 | 12/9/10 | 16:02:14 | Heptane | 762.3 | .18 | .67 | .15 | 0 | 3.7 | 3.6 | .34 | 2.2 | Extinction |
| FLEX-155 | C03H201 | 12/9/10 | 17:49:08 | Heptane | 764.9 | .18 | .67 | .15 | 0 | 2.73 | 2.52 | .39 | 2.7 | Extinction |
| FLEX-157 | C03H401 | 12/9/10 | 19:12:27 | Heptane | 765.7 | .18 | .67 | .15 | 0 | 1.34 | .45 | .48 | 3.2 | Completion |
| FLEX-158 | C05M101 | 12/14/10 | 13:41:00 | Methanol | 762.1 | .16 | .59 | .25 | 0 | 4.24 | 3.96 | .3 | 7.6 | Extinction |
| FLEX-159 | C05M201 | 12/14/10 | 14:30:46 | Methanol | 764.4 | .16 | .59 | .25 | 0 | 3.7 | 3.22 | .37 | 10.1 | Extinction |
| FLEX-160 | C05M301 | 12/14/10 | 15:17:59 | Methanol | 765.5 | .16 | .59 | .25 | 0 | 2.71 | 1.34 | .38 | 14.9 | Extinction |
| FLEX-161 | C05M401 | 12/14/10 | 17:51:58 | Methanol | 767.6 | .16 | .59 | .25 | 0 | 2.77 | 1.52 | .38 | 14.8 | Extinction |
| FLEX-162 | C06M101 | 12/28/10 | 11:41:39 | Methanol | 763.3 | .15 | .54 | .32 | 0 | 3.72 | 3.5 | .28 | 6 | Extinction |
| FLEX-163 | C06M201 | 12/28/10 | 12:05:23 | Methanol | 764.4 | .15 | .53 | .32 | 0 | 3.05 | 2.54 | .37 | 8.5 | Extinction |
| FLEX-164 | C06M301 | 12/28/10 | 13:00:43 | Methanol | 765.9 | .15 | .53 | .32 | 0 | 2.59 | 1.63 | .37 | 11.6 | Extinction |
| FLEX-165 | C06M401 | 12/28/10 | 13:36:43 | Methanol | 766.1 | .15 | .53 | .32 | 0 | 2.59 | 1.79 | .42 | 8.9 | Extinction |
| FLEX-166 | C03H302 | 12/9/10 | 18:51:34 | Heptane | 765.4 | .18 | .67 | .15 | 0 | 1.96 | 1.39 | .54 | 3.9 | Extinction |
| FLEX-167 | C07M101 | 1/12/11 | 21:56:45 | Methanol | 760.8 | .14 | .5 | .36 | 0 | 3.22 | 3.08 | .28 | 3.4 | Extinction |
| FLEX-168 | C07M201 | 1/12/11 | 22:11:40 | Methanol | 761.6 | .14 | .5 | .36 | 0 | 2.32 | 1.84 | .37 | 5.9 | Extinction |
| FLEX-169 | C15M101 | 1/18/11 | 12:54:25 | Methanol | 763.4 | .21 | .64 | .15 | 0 | 3.03 | 1.57 | .48 | 15.6 | Disruption |
| FLEX-170 | C15M201 | 1/18/11 | 14:19:29 | Methanol | 766.1 | .21 | .64 | .15 | 0 | 3.05 | 1.28 | .51 | 16.7 | Extinction |
| FLEX-171 | C15M301 | 1/18/11 | 15:58:46 | Methanol | 766.7 | .21 | .64 | .15 | 0 | 3.53 | 1.59 | .46 | 23.6 | Extinction |
| FLEX-172 | C03H501 | 2/21/11 | 17:56:40 | Heptane | 759.9 | .18 | .67 | .15 | 0 | 3.74 | 3.68 | .35 | 2.8 | Extinction |
| FLEX-173 | C03H601 | 2/21/11 | 19:07:48 | Heptane | 762 | .18 | .67 | .15 | 0 | 2.4 | 1.96 | .46 | 4.4 | Extinction |
| FLEX-174 | C03H701 | 2/21/11 | 19:17:37 | Heptane | 762.1 | .18 | .67 | .15 | 0 | 1.35 | .47 | .5 | 3.6 | Disruption |
| FLEX-175 | C08H502 | 2/21/11 | 22:15:54 | Heptane | 531.7 | .24 | .56 | .2 | 0 | 2.5 | .21 | .56 | 11.2 | Disruption |
| FLEX-176 | C08H601 | 2/21/11 | 22:43:37 | Heptane | 532.1 | .24 | .56 | .2 | 0 | 2.88 | - | .55 | 15.6 | Disruption |
| FLEX-177 | C08M501 | 4/18/11 | 20:27:36 | Methanol | 536.9 | .24 | .56 | .2 | 0 | 4.53 | - | .46 | 38.2 | Extinction |
| FLEX-178 | C08M601 | 4/18/11 | 20:52:24 | Methanol | 537 | .24 | .56 | .2 | 0 | 3.02 | 1.35 | .52 | 14.5 | Extinction |
| FLEX-179 | C09H501 | 4/20/11 | 17:56:25 | Heptane | 533.6 | .23 | .52 | .25 | 0 | 3.32 | 2.61 | .5 | 8.9 | Extinction |
| FLEX-180 | C09H601 | 4/20/11 | 18:22:58 | Heptane | 534.4 | .23 | .52 | .25 | 0 | 2.07 | .48 | .57 | 7.5 | Disruption |
| FLEX-181 | C02H101 | 4/20/11 | 20:00:24 | Heptane | 758.4 | .19 | .71 | .1 | 0 | 3.4 | 3.13 | .41 | 4.5 | Extinction |
| FLEX-182 | C02H201 | 4/20/11 | 21:14:08 | Heptane | 759.1 | .19 | .71 | .1 | 0 | 2.48 | 1.68 | .49 | 7 | Extinction |
| FLEX-183 | C02H202 | 4/20/11 | 21:26:02 | Heptane | 759 | .19 | .71 | .1 | 0 | 1.64 | .49 | .54 | 5.1 | Disruption |
| FLEX-184 | C09M501 | 8/8/11 | 13:14:11 | Methanol | 534.4 | .23 | .52 | .25 | 0 | 3.72 | - | .53 | 26.2 | Extinction |
| FLEX-185 | C09M502 | 8/8/11 | 13:30:14 | Methanol | 535.1 | .23 | .52 | .25 | 0 | 3.42 | - | .51 | 15.8 | Extinction |
| FLEX-186 | C09M601 | 8/8/11 | 13:42:04 | Methanol | 535.2 | .23 | .52 | .25 | 0 | 2.8 | 1.33 | .51 | 12.7 | Extinction |
| FLEX-187 | C09M701 | 8/8/11 | 14:52:15 | Methanol | 536.2 | .23 | .52 | .25 | 0 | 2.47 | 1.21 | .52 | 9.2 | Extinction |
| FLEX-188 | C02M101 | 8/8/11 | 16:16:48 | Methanol | 758 | .19 | .71 | .1 | 0 | 3.38 | 1.29 | .47 | 21.8 | Extinction |
| FLEX-189 | C02M201 | 8/8/11 | 17:49:19 | Methanol | 758.1 | .19 | .71 | .1 | 0 | 2.47 | 1.08 | .46 | 11 | Extinction |
| FLEX-190 | C03M501 | 8/9/11 | 10:53:21 | Methanol | 761.2 | .18 | .67 | .15 | 0 | 3.77 | 1.78 | .42 | 30.5 | Extinction |
| FLEX-191 | C03M601 | 8/9/11 | 12:28:41 | Methanol | 764.6 | .18 | .67 | .15 | 0 | 2.74 | .95 | .5 | 14 | Extinction |
| FLEX-192 | C03M701 | 8/9/11 | 12:46:53 | Methanol | 765.3 | .18 | .67 | .15 | 0 | 1.76 | .81 | .46 | 5.5 | Extinction |
| FLEX-193 | C04M101 | 8/9/11 | 17:07:27 | Methanol | 759.5 | .17 | .63 | .2 | 0 | 3.46 | - | .39 | 21.8 | Extinction |
| FLEX-194 | C04M201 | 8/9/11 | 18:26:45 | Methanol | 759.1 | .17 | .63 | .2 | 0 | 2.77 | 1.27 | .4 | 15.6 | Extinction |
| FLEX-195 | C04H101 | 8/17/11 | 22:31:20 | Heptane | 752 | .17 | .63 | .2 | 0 | 3.76 | 3.71 | .29 | 1.6 | Extinction |
| FLEX-196 | C04H201 | 8/17/11 | 22:53:58 | Heptane | 752.5 | .17 | .63 | .2 | 0 | 2.9 | 2.79 | .36 | 1.9 | Extinction |
| FLEX-197 | C01H501 | 8/18/11 | 0:24:31 | Heptane | 758.4 | .2 | .75 | .05 | 0 | 3.06 | 2.28 | .52 | 8.9 | Extinction |
| FLEX-198 | C01H601 | 8/18/11 | 1:38:10 | Heptane | 759.8 | .2 | .75 | .05 | 0 | 3.04 | 2.33 | .49 | 8.1 | Extinction |
| FLEX-199 | C01H701 | 8/18/11 | 1:55:56 | Heptane | 760.1 | .2 | .75 | .05 | 0 | 2.12 | .13 | .53 | 8.7 | Disruption |
| FLEX-200 | C01M501 | 8/24/11 | 15:07:47 | Methanol | 754 | .2 | .75 | .05 | 0 | 3.37 | .98 | .49 | 21 | Extinction |
| FLEX-201 | C01M602 | 8/24/11 | 15:56:17 | Methanol | 756.1 | .2 | .75 | .05 | 0 | 2.57 | 1.13 | .47 | 11.7 | Extinction |
| FLEX-202 | C01M603 | 8/24/11 | 16:18:58 | Methanol | 756.9 | .2 | .75 | .05 | 0 | 2.4 | 1.05 | .48 | 10.2 | Extinction |
| FLEX-203 | N01M101 | 8/24/11 | 21:05:01 | Methanol | 760.2 | .21 | .79 | 0 | 0 | 3.3 | 1.42 | .47 | 19.5 | Extinction |
| FLEX-204 | N01M201 | 8/24/11 | 21:58:36 | Methanol | 761.6 | .21 | .79 | 0 | 0 | 2.75 | 1.11 | .52 | 12.8 | Extinction |
| FLEX-206 | N01H101 | 8/29/11 | 19:04:50 | Heptane | 756.5 | .21 | .79 | 0 | 0 | 3.56 | - | .43 | 23.9 | Disruption |
| FLEX-207 | N01H102 | 8/29/11 | 19:21:49 | Heptane | 757.3 | .21 | .79 | 0 | 0 | 3.58 | - | .42 | 24 | Disruption |
| FLEX-208 | N01H201 | 8/29/11 | 20:28:30 | Heptane | 760.2 | .21 | .79 | 0 | 0 | 2.96 | .47 | .5 | 17.1 | Disruption |
| FLEX-209 | N01H202 | 8/29/11 | 21:54:40 | Heptane | 762.7 | .21 | .79 | 0 | 0 | 2.72 | 1.13 | .54 | 11.5 | Completion |
| FLEX-210 | N01H301 | 8/29/11 | 22:19:47 | Heptane | 762.9 | .21 | .79 | 0 | 0 | 2.92 | - | .69 | 12.8 | Completion |
| FLEX-211 | N02H101 | 8/29/11 | 23:36:18 | Heptane | 759.8 | .16 | .84 | 0 | 0 | 3.34 | 3.18 | .34 | 3.4 | Extinction |
| FLEX-212 | N02H201 | 8/29/11 | 23:51:11 | Heptane | 759.8 | .16 | .84 | 0 | 0 | - | - | - | - | Extinction |
| FLEX-214 | N02H203 | 8/30/11 | 0:58:06 | Heptane | 759.9 | .16 | .84 | 0 | 0 | 2.52 | 2.13 | .42 | 4.5 | Extinction |
| FLEX-215 | N03H101 | 9/1/11 | 19:44:42 | Heptane | 764 | .15 | .85 | 0 | 0 | 2.55 | 2.31 | .37 | 3.4 | Extinction |
| FLEX-216 | N03H201 | 9/1/11 | 21:02:30 | Heptane | 766.2 | .15 | .85 | 0 | 0 | 1.77 | .33 | .47 | 6.7 | Completion |
| FLEX-217 | N04H101 | 9/1/11 | 22:54:16 | Heptane | 759.8 | .14 | .86 | 0 | 0 | 4.16 | 4.15 | .24 | 1.6 | Extinction |
| FLEX-218 | N04H201 | 9/1/11 | 23:17:17 | Heptane | 759.9 | .14 | .86 | 0 | 0 | 1.83 | - | .39 | 3.8 | Extinction |
| FLEX-219 | N04M101 | 9/8/11 | 17:00:27 | Methanol | 757.6 | .14 | .86 | 0 | 0 | 3.5 | - | .3 | 26 | Extinction |
| FLEX-220 | N04M201 | 9/8/11 | 17:21:15 | Methanol | 758.3 | .14 | .86 | 0 | 0 | 2.67 | 1.27 | .38 | 15.6 | Extinction |
| FLEX-221 | N05M101 | 9/8/11 | 19:00:48 | Methanol | 759.4 | .13 | .87 | 0 | 0 | 3.46 | 2.96 | .36 | 9.5 | Extinction |
| FLEX-222 | N05M201 | 9/8/11 | 20:24:20 | Methanol | 760.6 | .13 | .87 | 0 | 0 | 2.75 | 1.46 | .35 | 16.3 | Extinction |
| FLEX-223 | N06M101 | 9/9/11 | 13:09:53 | Methanol | 761.6 | .12 | .88 | 0 | 0 | 2.6 | 2.09 | .36 | 6.9 | Extinction |
| FLEX-224 | N06M201 | 9/9/11 | 13:28:43 | Methanol | 761.9 | .12 | .88 | 0 | 0 | 1.94 | 1.05 | .35 | 7.8 | Extinction |
| FLEX-225 | N06M202 | 9/9/11 | 14:26:07 | Methanol | 763.7 | .12 | .88 | 0 | 0 | 1.84 | 1.04 | .38 | 6 | Extinction |
| FLEX-226 | H01M102 | 9/9/11 | 17:41:47 | Methanol | 759.2 | .2 | .75 | 0 | .05 | 2.91 | 1.12 | .51 | 14.4 | Extinction |
| FLEX-227 | H01M104 | 9/9/11 | 18:27:14 | Methanol | 759.6 | .2 | .75 | 0 | .05 | - | - | - | ~6 | Extinction |
| FLEX-229 | H01H102 | 9/13/11 | 11:55:40 | Heptane | 755.3 | .2 | .75 | 0 | .05 | 2.25 | - | .57 | ~9 | Completion |
| FLEX-230 | H01H103 | 9/13/11 | 12:22:18 | Heptane | 756.5 | .2 | .75 | 0 | .05 | 2.3 | - | .58 | 9.8 | Disruption |
| FLEX-231 | H02M101 | 9/21/11 | 22:28:54 | Methanol | 753.4 | .19 | .71 | 0 | .1 | 2.78 | - | .57 | 12.5 | Extinction |
| FLEX-232 | H03M101 | 9/22/11 | 0:02:52 | Methanol | 759.2 | .18 | .67 | 0 | .15 | 2.79 | 1.3 | .51 | 12.5 | Extinction |
| FLEX-233 | H03M201 | 9/22/11 | 0:44:55 | Methanol | 760.3 | .18 | .67 | 0 | .15 | 2.95 | 1.67 | .53 | 11.7 | Extinction |
| FLEX-234 | N01H401 | 9/23/11 | 23:18:09 | Heptane | 767.4 | .21 | .79 | 0 | 0 | 3.32 | 1.37 | .52 | 17.5 | Extinction |
| FLEX-235 | N01H502 | 9/24/11 | 0:06:41 | Heptane | 768.1 | .21 | .79 | 0 | 0 | 2.39 | - | .57 | 10.6 | Disruption |
| FLEX-236 | N01H601 | 9/24/11 | 1:06:33 | Heptane | 769.2 | .21 | .79 | 0 | 0 | 3.65 | 2.85 | .57 | 9.6 | Extinction |
| FLEX-237 | H02H101 | 9/24/11 | 2:44:09 | Heptane | 758.8 | .19 | .71 | 0 | .1 | 2.59 | - | .54 | 12 | Disruption |
| FLEX-238 | H03H101 | 9/27/11 | 12:08:14 | Heptane | 763.7 | .18 | .67 | 0 | .15 | 3.52 | 3.28 | .41 | 4.1 | Extinction |
| FLEX-239 | H03H201 | 9/27/11 | 13:00:54 | Heptane | 765.9 | .18 | .67 | 0 | .15 | 2.3 | - | .49 | 9.1 | Completion |
| FLEX-240 | H03H202 | 9/27/11 | 13:25:07 | Heptane | 766.5 | .18 | .67 | 0 | .15 | 2.27 | - | .51 | 8.6 | Completion |
| FLEX-241 | H04H101 | 9/27/11 | 15:00:33 | Heptane | 759.3 | .17 | .63 | 0 | .2 | 2.85 | 2.6 | .46 | 3.2 | Extinction |
| FLEX-242 | H04H201 | 9/27/11 | 15:12:24 | Heptane | 759.3 | .17 | .63 | 0 | .2 | 2.12 | 1.39 | .59 | 4.5 | Extinction |
| FLEX-243 | H04H302 | 9/27/11 | 16:18:19 | Heptane | 759.6 | .17 | .63 | 0 | .2 | - | - | - | 1.7 | Disruption |
| FLEX-244 | H04H303 | 9/27/11 | 16:40:04 | Heptane | 759.8 | .17 | .63 | 0 | .2 | 1.61 | - | .91 | 2.7 | Completion |
| FLEX-245 | H04M101 | 10/1/11 | 0:34:58 | Methanol | 754.2 | .17 | .63 | 0 | .2 | 2.99 | - | .49 | 9.1 | Extinction |
| FLEX-246 | H04M202 | 10/1/11 | 1:21:41 | Methanol | 757 | .17 | .63 | 0 | .2 | 2.9 | 1.42 | .51 | 13.1 | Extinction |
| FLEX-247 | H05M102 | 10/1/11 | 2:58:40 | Methanol | 759.9 | .16 | .59 | 0 | .25 | 3.4 | 2.79 | .51 | 7.9 | Extinction |
| FLEX-248 | H05M202 | 10/1/11 | 4:26:52 | Methanol | 761 | .16 | .59 | 0 | .25 | - | - | - | 5 | Extinction |
| FLEX-249 | H05H103 | 10/5/11 | 14:58:32 | Heptane | 757.9 | .16 | .59 | 0 | .25 | 1.49 | .69 | .6 | 2.9 | Extinction |
| FLEX-250 | H06M102 | 10/7/11 | 12:12:14 | Methanol | 755.6 | .15 | .55 | 0 | .3 | 3.67 | 3.47 | .43 | 3.6 | Extinction |
| FLEX-251 | H06M201 | 10/7/11 | 13:00:56 | Methanol | 756.7 | .15 | .55 | 0 | .3 | 2.52 | 2.06 | .56 | 4 | Extinction |
| FLEX-252 | H07M101 | 10/7/11 | 14:25:42 | Methanol | 759.2 | .14 | .51 | 0 | .35 | 2.44 | 2.26 | .56 | 1.5 | Extinction |
| FLEX-253 | H07M202 | 10/7/11 | 15:06:17 | Methanol | 759.8 | .14 | .51 | 0 | .35 | 1.88 | 1.73 | .58 | 1 | Extinction |
| FLEX-254 | H08M101 | 10/11/11 | 12:11:56 | Methanol | 763.5 | .13 | .47 | 0 | .4 | 3.56 | 3.54 | .51 | .3 | Extinction |
| FLEX-255 | H10H101 | 10/12/11 | 20:16:43 | Heptane | 534 | .24 | .56 | 0 | .2 | 3.78 | 2.52 | .72 | 12.2 | Extinction |
| FLEX-256 | H11H101 | 10/12/11 | 21:58:55 | Heptane | 532.2 | .23 | .52 | 0 | .25 | 2.8 | .12 | .71 | 11.4 | Completion |
| FLEX-257 | H10M101 | 11/18/11 | 14:48:10 | Methanol | 534.3 | .24 | .56 | 0 | .2 | 2.82 | 1.03 | .62 | 11.2 | Extinction |
| FLEX-258 | H10M102 | 11/18/11 | 15:19:28 | Methanol | 534.6 | .24 | .56 | 0 | .2 | 2.79 | 1.53 | .7 | 8.1 | Disruption |
| FLEX-259 | H11M101 | 11/18/11 | 16:59:20 | Methanol | 531.7 | .23 | .52 | 0 | .25 | 2.45 | .86 | .6 | 8.3 | Extinction |
| FLEX-260 | H11M102 | 11/18/11 | 17:51:23 | Methanol | 531.8 | .23 | .52 | 0 | .25 | 2.61 | - | .73 | 6.3 | Disruption |
| FLEX-261 | H12M101 | 11/18/11 | 18:53:50 | Methanol | 531.9 | .21 | .49 | 0 | .3 | 3.22 | - | .56 | 10.4 | Extinction |
| FLEX-262 | H12M102 | 11/18/11 | 21:29:35 | Methanol | 531.2 | .21 | .49 | 0 | .3 | 3.25 | 1.78 | .65 | 12.1 | Extinction |
| FLEX-263 | H12M201 | 11/18/11 | 21:53:16 | Methanol | 531.2 | .21 | .49 | 0 | .3 | 2.67 | 1.42 | .7 | 7.6 | Extinction |
| FLEX-264 | H12H101 | 11/22/11 | 13:04:17 | Heptane | 529.6 | .21 | .49 | 0 | .3 | 3.23 | 2.33 | .67 | 7.5 | Extinction |
| FLEX-265 | H12H201 | 11/22/11 | 15:49:36 | Heptane | 529 | .21 | .49 | 0 | .3 | 2.86 | .71 | .7 | 11 | Extinction |
| FLEX-266 | H13H101 | 11/22/11 | 20:40:42 | Heptane | 532.5 | .2 | .45 | 0 | .35 | 3.69 | 3.32 | .61 | 4.3 | Extinction |
| FLEX-267 | H13H201 | 11/22/11 | 20:58:21 | Heptane | 532 | .2 | .45 | 0 | .35 | 3.08 | 1.69 | .67 | 5.4 | Extinction |
| FLEX-268 | H13M102 | 11/28/11 | 13:13:31 | Methanol | 527.6 | .2 | .45 | 0 | .35 | 3.87 | 2.24 | .6 | 17.4 | Extinction |
| FLEX-269 | H13M201 | 11/28/11 | 13:24:55 | Methanol | 527.9 | .2 | .45 | 0 | .35 | 2.95 | 1.5 | .63 | 10.6 | Extinction |
| FLEX-270 | H14M101 | 11/28/11 | 15:07:28 | Methanol | 532.4 | .18 | .42 | 0 | .4 | 3.5 | 2.67 | .59 | 7.8 | Extinction |
| FLEX-271 | H14M201 | 11/28/11 | 15:35:38 | Methanol | 532.9 | .18 | .42 | 0 | .4 | 2.7 | 1.92 | .63 | 5.9 | Extinction |
| FLEX-272 | H14M202 | 11/28/11 | 15:54:09 | Methanol | 533.2 | .18 | .42 | 0 | .4 | 1.84 | 1.3 | .62 | 2.3 | Extinction |
| FLEX-273 | H14H101 | 11/30/11 | 8:39:18 | Heptane | 528 | .18 | .42 | 0 | .4 | 2.27 | 1.64 | .71 | 3.5 | Extinction |
| FLEX-274 | H14H201 | 11/30/11 | 9:49:07 | Heptane | 530.3 | .18 | .42 | 0 | .4 | 1.86 | .84 | .77 | 3.5 | Extinction |
| FLEX-275 | H15H101 | 11/30/11 | 11:30:51 | Heptane | 532.2 | .17 | .38 | 0 | .45 | 2.22 | 1.86 | .76 | 1.9 | Extinction |
| FLEX-276 | H15H201 | 11/30/11 | 12:09:00 | Heptane | 532.5 | .17 | .38 | 0 | .45 | 1.61 | .91 | 1.06 | 1.4 | Completion |
| FLEX-277 | H15M102 | 12/5/11 | 22:54:10 | Methanol | 530.4 | .17 | .38 | 0 | .45 | 2.79 | 2.3 | .63 | 4 | Extinction |
| FLEX-278 | H15M201 | 12/5/11 | 23:39:04 | Methanol | 531.5 | .17 | .38 | 0 | .45 | 2.68 | 2.31 | .66 | 2.9 | Extinction |
| FLEX-279 | H19H101 | 12/8/11 | 22:29:44 | Heptane | 764.7 | .21 | .64 | 0 | .15 | 3.54 | 2.91 | .55 | 7.6 | Extinction |
| FLEX-280 | H19H201 | 12/8/11 | 23:41:45 | Heptane | 766.2 | .21 | .64 | 0 | .15 | 2.82 | .73 | .65 | 11.7 | Extinction |

**Table notes.** Five test numbers between FLEX-001 and FLEX-280 do not
appear as rows in the source's own Table IX — FLEX-065, FLEX-156, FLEX-205,
FLEX-213, and FLEX-228 — a gap in the source's own numbering, not an
omission introduced here. Two rows share identifier `193F001` and the same
date/time (FLEX-070 and FLEX-073); both are reproduced exactly as the source
lists them, since the source itself does not reconcile the apparent
duplicate. For 33 rows (FLEX-032 through FLEX-064), the source's own table
segment for that page carries only three ambient-composition columns rather
than four; those rows' He field is marked `not stated` here rather than
assumed to be zero, per this record's rule against guessing values the
source doesn't state.

## Data quality notes

A conformal coating (Dow Corning 1204 primer plus 3140 RTV) applied to the
fuel-dispensing needles during MDCA assembly was later found to dissolve and
flake into the fuel in both methanol and heptane; deployed droplets were not
always pure. After discovery, new uncoated needles were prepared for
subsequent flights. Based on extensive testing, numerical
modeling, and comparison with uncontaminated space-based data, the report
draws these specific assertions about the affected tests reported
herein:

1. Burning-rate constants and droplet history were minimally influenced —
   the contaminant was a trace, low-volatility compound against relatively
   high-volatility fuels.
2. Flame size and flame history were similarly minimally influenced.
3. Unusual flame features (minor disruptions, visual "sparklers") in a few
   tests were probably influenced, possibly caused, by the contaminant.
4. Disruptive extinction of methanol is probably due to the contaminant.
5. Disruptive extinction of heptane *may* be due to the contaminant — but
   subsequent clean-needle tests also showed disruptive extinction at small
   droplet sizes, so no conclusion can be drawn for heptane specifically.
6. Diffusive extinction droplet diameters for methanol (no disruption) were
   minimally influenced.
7. Radiative extinction droplet diameters were not influenced.
8. Distorted droplets in methanol tests (about four tests, e.g. FLEX-088) are
   probably a result of the contaminant.

Separately, camera shutter speed changed after FLEX-009: tests FLEX-001
through FLEX-009 used a 1/30 s shutter (matching the 30 fps frame rate),
during which broadband glow from the igniters affected droplet/background
discrimination; from FLEX-009 onward the shutter dropped to 1/1000 s with
increased illumination, reducing that distortion and improving droplet-size
accuracy. Where a droplet drifted out of a camera's field of
view (FOV) before extinction — common given droplets were rarely perfectly
motionless after deployment — the report either estimated (extrapolated) the
extinction diameter from the burning history when feasible, or left the
value unreported; some tests also show gaps where the droplet drifted out of
and back into the FOV (e.g. FLEX-013), or where a camera failed to record
entirely (e.g. FLEX-024, HiBMs).[^flex-tp-2015]

## What this report does not do

The source is explicit that it archives data rather than draws conclusions:
"It is not intended to interpret the data from those experiments or to draw
any scientific conclusions; that will occur through future NASA reports and
peer-reviewed journal articles that reference this report."[^flex-tp-2015]

## Open questions

- **Appendix B** ("Droplet and Flame Sizes," a separate, substantially longer
  section of the source) contains continuous droplet-diameter-squared-vs-time and
  flame-diameter-vs-time curves for each test — per-video-frame measurements,
  not discrete per-test facts — and is intentionally not transcribed here; it
  is a different kind of artifact (time-series curve data) from the per-test
  summary in Table IX above.
- The individual PI/science-team interpretation of any of these results
  (e.g. why a specific test disrupted rather than extinguished) is not
  available in this source, which explicitly defers interpretation to future
  papers.
- Because this source declines to interpret its data, no "Conclusions"
  section beyond the cataloguing/procedural material above exists to cite.

[^flex-tp-2015]: Detailed Results From the Flame Extinguishment Experiment (FLEX). Executive Summary: "The Flame Extinguishment Experiment (FLEX) program is a continuing set of experiments on droplet combustion, performed employing the Multi-User Droplet Combustion Apparatus (MDCA), inside the chamber of the Combustion Integrated Rack (CIR), which is located in the Destiny module of the International Space Station (ISS)... It also presents the results of the first 284 tests performed. The intent is not to interpret the experimental results but rather to make them available to the entire scientific community for possible future interpretations... The fuels studied in these experiments were methanol and n-heptane. The droplets had initial diameters between 2 and 5 mm, and they were burned in oxidizing atmospheres at ambient temperature and various pressures between 0.70 and 3.05 atm... Most of the tests were conducted at pressures between 0.7 and 1 atm, and many of the tests were in air... Observed LOI values for these fuels appear to be slightly lower than initially expected. Besides documenting both radiative extinction at higher dilutions and diffusive extinctions at lower dilutions for both fuels, the results exhibited disruptive extinctions." "Both flame diameter measurements are of the outer edge of the flame, and the diameters in the color-camera images are the smaller of the two, approximately three-fourths of the LLUV results." §1.0 Introduction: "Natural convection, however, destroys the spherical symmetry of combustion in normal gravity... The purpose of this report is to detail and permanently archive the results of a subset of the FLEX experiments, namely those occurring between March 2009 and the end of December 2011. It is not intended to interpret the data from those experiments or to draw any scientific conclusions; that will occur through future NASA reports and peer-reviewed journal articles that reference this report." §2.1 Experimental Hardware: "The MDCA facility, which is described in detail elsewhere (Robbins and Shinn, 2010), is based on the design of the space shuttle Droplet Combustion Experiment (DCE, Nayagam et al., 1998)." "The CIR facility... consists of a 90-liter combustion chamber that can operate at pressures of approximately 0 to 9 atm... For the FLEX experiments, this analysis reduced the maximum working pressures to approximately 3 atm... The FOMA consists of gas bottles, a connection for ISS nitrogen connected through a series of valves, pressure transducers, and mass flow controllers to the combustion chamber... Stainless-steel tubes with 250-µm outside diameters and specially treated ends are used for the deployment... The amount of fuel put in the syringe was a function of the detailed safety analysis, approximately 2.5 ml for methanol and 1.25 ml for heptane... The needles then slowly stretched to a distance slightly smaller than the distance where the fluid would pull off one of the needles. Just before ignition, the needles rapidly retracted, ideally leaving a motionless droplet floating in the middle of the CIR combustion chamber... Once the needles retracted, the control computer energized two hot-wire igniters located 180° to each other and in the same plane as the deployment needles. After a preset time, the control computer deenergized the igniters and activated the linear... For fiber-supported tests, the procedure was exactly the same, except that the droplets were deployed on a small 80-µm support fiber." §2.2 Experiment Diagnostics: "They included a backlit view of the droplet and an orthogonal view of the flame... The backlit view was the High-Bit-Depth Multispectral (HiBMs) imaging package. The HiBMs package had a telemetric imaging optical system and a high-resolution 12-bit output digital camera. They provided monochromatic illumination with a center wavelength between 650 to 660 nm... Almost all of the tests reported herein used the full 1024 by 1024 array with a fixed field of view (FOV) of approximately 30 mm on a side... a framing rate of approximately 30 frames per second (fps)... The CIR also provided a LLUV package to image the chemiluminescence from hydroxyl (OH•) emissions... a 1024 by 1024 monochrome frame-transfer charged-coupled device (CCD) array with 12-bit digital imaging capability. The CCD array was directly coupled to an 18-mm Gen II-UV microchannel plate intensifier to provide maximum response at short wavelengths... a spectral notch filter integrated to image the chemiluminescence at 310 nm (the filter had a 10-nm full width at half maximum (FWHM) bandwidth)... All of the tests reported herein used the 2 by 2 binned (512 by 512) array with a fixed FOV of approximately 50 mm on a side. The framing rate for the majority of the tests was 30 fps, with a smaller number at 15 fps... The white LED was turned on at this time to allow the operator to see the droplet formation process; immediately prior to droplet deployment and ignition, the camera zoomed out and the white LED turned off to provide an overview of the combustion process. The FOV of this camera was approximately 110 by 90 mm... For the tests reported herein, these radiometers were not sensitive enough to provide reliable quantitative information about flame radiometric output, so the data are not reported." §2.3 Experimental Procedures: "Personnel at the Telescience Support Center (TSC) at Glenn controlled all functions of the FLEX experiments. Test-point operations typically required three operators, two controlling the functions of the CIR, and one dedicated to the MDCA... immediately prior to test-point operations, the crew removed the alignment guides to the Passive Rack Isolation System (PaRIS). PaRIS isolated the CIR from the lower level, higher frequency vibrations or g-jitter of the ISS... For all of the experiments in this report, the g-environment was low enough that buoyant flow could be considered to be negligible; however, g-jitter was evident when the droplet began to move in a particular direction and potentially out of the camera FOV." §3.1 HiBMS Image Analysis: "The images were analyzed in a semiautomatic manner by using the commercially available image-processing packages, Image J... or Igor Pro... The measurement was converted to a flame size using the appropriate scale factor (32.5 pixels/mm) for most of the tests herein... the HiBMs operated at full frame (not binned), or 1024 by 1024 pixels. Therefore, the minimum spatial resolution was ±29.5 µm... we estimated the uncertainty in the droplet size to be ±50 µm." §3.2 LLUV Image Analysis: "The flame size is much more difficult to measure than the droplet size. The flames are quite dim... The flame dimension detailed in this report represents the outer edge of the OH• chemiluminescence... The measurement was converted to a droplet size using the appropriate scale factor (8.86 pixels/mm for most of the tests herein)... the LLUV operated with 2 by 2 binning or a resolution of 512 by 512 pixels. Therefore, the minimum spatial resolution was ±113 µm... we estimated the uncertainty in the flame size to be ±200 µm." §3.3 MDCA Color Camera Analysis: "The flame dimension detailed in this report represents the outer edge of the visible flame... The measurement was converted to a droplet size using the appropriate scale factor (6.87 pixels/mm for most of the tests herein)... the video camera has standard National Television System Committee (NTSC) resolution, or 640 by 480 pixels. Therefore, the minimum spatial resolution is ±146 µm... we estimated the uncertainty in the flame size to be ±250 µm." §4.2 Analyzed Data: "For almost all of the tests, the diameter measured by the LLUV is larger than that measured by the color camera. The flame diameters from the color camera are typically about three-fourths of those from the LLUV camera. This discrepancy is not unusual and is a result of the LLUV being sensitive to the OH• chemiluminescence, which typically peaks outside of the visible flame. For heptane tests, where there is significant soot luminosity (which is not visible in the LLUV, but dominates the color camera), the discrepancy is even larger because the peak of the soot luminosity is typically inside the blue flame envelope." §5.2 Fuel Needle Contamination: "During the assembly of the MDCA hardware, a conformal coating was applied to the fuel-dispensing needles. The product was applied in two layers, a primer (Dow Corning 1204) and a conformal coat (Dow Corning 3140 RTV (MIL-A-46146) coating). Subsequent testing showed that the coating can both dissolve and \"flake\" off in both methanol and heptane... Once this problem was discovered, the mitigation was to prepare and fly new uncoated needles... (1) Burning-rate constants were average, and the droplet history was minimally influenced by the contaminant... (2) The flame size and flame history were similarly minimally influenced by the contaminant. (3) In the few tests where unusual features were observed in the flame view, such as minor disruptions and visual \"sparklers,\" these features were probably influenced, and possibly caused, by the presence of the contaminant. (4) Disruptive extinction of methanol is probably due to the presence of the contaminant. (5) Disruptive extinction of heptane may be due to the presence of the contaminant. Subsequent tests with clean needles and fuel, however, also exhibited disruptive extinction at small droplet sizes, so no conclusion can be drawn regarding disruptive burning for heptane in the tests reported herein. (6) The diffusive extinction droplet diameters (smaller diameters) for methanol (where there is no disruption) were minimally influenced by the presence of the contaminant. (7) Radiative extinction droplet diameters (larger diameters) were not influenced by the presence of the contaminant. (8) Distorted droplets (e.g., the HiBMs video from the FLEX-088 test) for methanol droplet burning (approximately four tests) are probably the result of the contaminant." Also: "For tests where the droplet drifted out of the FOV of the camera, the data end abruptly (e.g., the droplet regression during the FLEX-011 test). This does not correspond to the end of the test, just to the end of the data from that particular view... For a minority of tests, the droplet drifted out of the HiBMs FOV as a result of the deployment, and/or g-jitter. However, it then actually drifted back into the FOV. In this case, there is a gap in the history of that view (e.g., the droplet history for the FLEX-013 test)... For some tests, some of the CIR cameras failed to record data for a portion of the test, and for other tests, none of the test was recorded... (e.g., the FLEX-024 test, for which the HiBMs failed to record any data)." Regarding shutter speed: "This was especially present from the FLEX-001 test to the FLEX-009 test. For these tests, the shutter speed (integration time of the array) was 1/30 s (inverse of the framing rate). After the FLEX-009 test, the shutter speed decreased to a much smaller value (1/1000 s) with a corresponding increase in the illumination level. This minimized the image distortion caused by the igniters and the broadband flame radiation... resulting in more accurate droplet size data." §6.0 Conclusions: "Histories of droplet and flame diameters, as well as burning-rate constants and extinction diameters, were obtained in Flame Extinguishment Experiment (FLEX) program experiments performed on the International Space Station for methanol and n-heptane droplets with initial diameters between 2 and 5 mm... More than 100 useful combustion histories were obtained."
