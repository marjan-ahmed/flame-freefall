---
type: Document
title: "LUCI: rotating-platform methods, flame tracking and comparison results"
description: Expanded source-based account of the LUCI apparatus, partial-gravity and ground observations, fitted spread rates and interpretation limits.
status: stable
generated: { by: "process:codex-source-review", at: 2026-10-31T13:38:56+00:00 }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-10-31T13:38:56+00:00 }
sources:
  - id: luci-2025
    title: "Lunar Combustion Investigation: Flammability Results from a Rotating Sounding Rocket"
    resource: https://ntrs.nasa.gov/citations/20250010653
---

> [!NOTE]
> LUCI describes a rotating platform simulating lunar gravity. The
> presentation's fitted observations are not a table of independently
> identified combustion runs.

## Purpose and demonstrated outcome

LUCI tested whether material flammability
experiments could be performed in partial gravity on a spinning Blue Origin
New Shepard vehicle. The source presents the possibility that some materials
may be more flammable in partial gravity than on Earth as a hypothesis
motivating the work, not as a universal experimental conclusion. Its explicit
demonstrated outcome is that material flammability testing at partial gravity
is feasible using a spinning vehicle.[^luci-2025]

The source describes the results as a bridge between ground experiments,
other simulated-gravity experiments, modeling and eventual experiments on the
lunar surface. It distinguishes the achieved feasibility demonstration from
potential follow-on work on oxygen limits, model comparisons and
pressure-gravity scaling. Those objectives do not establish that a predictive
model or a material-screening rule has already been validated.[^luci-2025]

## How the apparatus produces the test environment

Centrifugal acceleration supplies the simulated gravity. The presentation
reports a steady vehicle rotation of **11 RPM** and an effective rotation
radius of **1.22 m** at the experiment location. Its schematic places the
centrifugal gravity direction outward toward the vehicle hull; the flames
generally rise toward the axis of rotation. Sample orientation therefore has
to be interpreted in relation to the radial direction, not an ordinary
stationary laboratory vertical.[^luci-2025]

| Reported apparatus or procedure | Source description |
| --- | --- |
| Fabric sample | 5 cm wide x 30 cm long; cotton-fiberglass composite identified as SIBAL |
| Acrylic sample | 4-mm diameter rod of polymethyl methacrylate, identified as PMMA |
| Environment | Air at normal pressure, with chamber oxygen measured during burning |
| Imaging | Two orthogonal camera views used to determine flame spread and growth |
| Other measured quantities | Chamber pressure, temperature and centrifugal acceleration |
| Enclosure dimensions | Effective floor about 41 cm x 48 cm; available height in the gravity direction about 53 cm |

The overview describes the samples as burning simultaneously, while the
schematic says they were ignited with a slight pause between them. These
statements support overlapping burns with a staggered ignition; they do not
justify assigning an identical ignition time to both samples. The overview
states that burning lasted over two and a half minutes, but that campaign
description is not substituted for either specimen's individual burn
duration.[^luci-2025]

The oxygen observations below follow the presentation's sample-labeled
panels. Because the overview describes overlapping burns in the chamber,
those panels do not establish that the specimens were exposed to independent
atmospheres. Their time origins and sampling intervals need to be aligned
before interpreting different reported oxygen endpoints.[^luci-2025]

## Fabric: flame tracking and changing oxygen

For SIBAL, the partial-gravity slides describe linear spread of the char
front, flame base and flame tip, with semi-steady flame dimensions during part
of the burn. One slide gives a flame-base spread rate of **.92 mm/s** and a
flame-tip spread rate of **1.1 mm/s**. The later comparison table gives **.9**
for the partial-gravity flame base. Both printed values are retained rather
than silently treated as identical measurements with an inferred precision.
The source does not provide an uncertainty interval explaining their
relationship.[^luci-2025]

The backup slides report approximately **3.2 cm** flame width and **1.5 cm**
flame length during semi-steady spread, followed by decreasing dimensions
during extinction. They define preheat length as the difference between
flame-base and char-front fit equations. A separate slide reports a preheat
length shrink rate of **-0.094 mm/s**. These are distinct tracked quantities;
they must not all be labeled as the same flame spread rate.[^luci-2025]

The SIBAL oxygen observation is a decrease from **~20% to ~18%**, described as
roughly constant in rate over the experiment. Its gravity recap states that
gravity remains constant at lunar gravity and attributes extinction to other
factors. This preserves the source's account without turning the final oxygen
reading into a universally applicable limiting oxygen concentration for the
material.[^luci-2025]

## Acrylic rod: separate base motion, tip motion and flame growth

The PMMA slides state that steady flame-base spread was not achieved. Base
position is described as approximately quadratic; the instantaneous base
spread rate is the derivative of a fitted position equation. The reported
rate increases linearly from **0 to ~.6 mm/s** before gravity starts dropping
at **t = 125s**. That time-varying fitted rate is not a sequence of independent
experimental runs or an uncertainty band.[^luci-2025]

The same presentation describes approximately linear flame-tip motion and
prints **1.5 mm/s** for that rate. It also reports total base spread of
**~6cm** until extinction. Flame length becomes difficult to measure after
the tip is obscured by the sample holder. Consequently, a flame-tip rate,
flame-base rate, total base displacement and flame-length growth cannot be
substituted for one another.[^luci-2025]

For PMMA, oxygen decreases from **20% to 14.3%**, then rises back to **15.8%**.
The source says the rise was likely associated with a decrease in gravity and
buoyant flow at **125s**. A backup slide instead describes gravity as remaining
approximately constant for the duration of the burn. These statements cannot
be reconciled into a single time-independent gravity condition from the
presentation alone; synchronized acceleration and image records are needed
to establish the applicable time interval.[^luci-2025]

## Comparison with ground observations

The source provides fitted comparisons, while noting that ground tracking was
less clean, the ground flame burned out more quickly, and fewer data points
were available. The following tables reproduce the source's printed values
and its ratios; the ratios are not recalculated to imply additional
precision.[^luci-2025]

| SIBAL tracked feature | Partial-gravity fit (mm/s) | Ground fit (mm/s) | Printed ratio |
| --- | --- | --- | --- |
| Flame base | .9 | 1.5 | .6 |
| Flame tip | 1.1 | 2.8 | .39 |

The width-comparison slide states that ground extinction occurs **~45 seconds**
sooner. That observation describes the compared experiments; it is not a
general extinction-time correction or an isolated effect of gravity when
oxygen and tracking quality also differ.[^luci-2025]

| PMMA tracked feature | Partial-gravity fit (cm/s) | Ground fit (cm/s) | Printed ratio |
| --- | --- | --- | --- |
| Flame tip | .15 | .40 | .38 |

This PMMA comparison uses **cm/s**, whereas the separate flame-tip slide uses
**mm/s**. The units are retained exactly as printed. The ground slides also
describe the flame base as approximately stationary late in the experiment,
making tip motion an approximation to flame-length growth in that case.
They report ground oxygen decreasing approximately from **21% to 14.5%**.
These endpoint and atmosphere differences matter when interpreting the
comparison.[^luci-2025]

## Rotation effects and source ambiguities

A PMMA image caption identifies the Coriolis force as pulling the flame away
from the fuel axis, which is aligned with the centrifugal acceleration. That
observed deflection is part of the apparatus behavior. The presentation
does not establish an apparatus-independent correction that would turn these
observations into a prediction for a stationary lunar habitat.[^luci-2025]

The SIBAL slide also says that the tip moves slightly faster than the base,
“indicating a slowly shrinking flame length.” The relationship between that
wording and the tracked-coordinate convention is not explained. This document
retains the statement as a source ambiguity rather than silently changing
“shrinking” to another physical interpretation.[^luci-2025]

## What is established, and what remains open

| Question | Answer available in the presentation | Remaining evidence needed |
| --- | --- | --- |
| Can the rotating platform support partial-gravity flammability experiments? | Feasibility is the stated achieved outcome. | Repetition and identified run records are needed to quantify repeatability. |
| Which spread endpoint is being reported? | The slides distinguish char front, flame base and flame tip, with fitted comparisons for specified features. | Fit intervals, tracking definitions, residuals and uncertainties are needed to reproduce the estimates. |
| Was the atmosphere constant? | No; specimen-specific oxygen changes are reported. | Synchronized oxygen, pressure, temperature and image histories are needed for condition-matched interpretation. |
| Was gravity constant throughout the PMMA burn? | The slides contain both approximately constant-gravity wording and a reported late gravity decrease. | The acceleration trace and its time origin are needed to resolve the applicable interval. |
| How should rotation effects be separated from gravity effects? | The source identifies visible Coriolis deflection. | A quantified comparison or validated correction is needed before generalizing beyond the rotating apparatus. |
| Do the observations establish material certification or a universal gravity scaling? | The source states feasibility and identifies further comparison and modeling objectives. | Independent validation, uncertainty analysis and appropriate material-screening evidence remain necessary. |

These are specific evidence requirements for further use of the results. They
do not erase the reported observations or imply that absent run-level records
do not exist elsewhere.

[^luci-2025]: Lunar Combustion Investigation: Flammability Results from a Rotating Sounding Rocket. Objectives and Outcome: partial-gravity material testing using a spinning vehicle is feasible; follow-on objectives include oxygen limits, modeling and pressure-gravity scaling. Overview and Schematic: 11 RPM, effective radius 1.22 m, air at normal pressure, two orthogonal cameras, fabric 5 cm x 30 cm, 4-mm acrylic rod, chamber sensors and staggered ignition. Enclosure description: about 41 cm x 48 cm floor and 53 cm height. “LUCI: SIBAL fabric”: flame-base rate .92 mm/s, tip rate 1.1 mm/s and linear tracked-front spread. Partial-gravity recaps: approximately 3.2 cm width, 1.5 cm length, preheat-length shrink rate -0.094 mm/s, oxygen ~20% to ~18% and constant-gravity wording. “LUCI: PMMA”: non-steady base motion, ~6cm total base spread, 1.5 mm/s tip rate, oxygen 20% to 14.3% rising to 15.8%, and a reported gravity decrease at 125s. Backup PMMA slides: instantaneous rate is the derivative of a fitted position equation, increasing from 0 to ~.6 mm/s before t = 125s; another slide says gravity remains approximately constant. Ground results and combined-fit comparisons: SIBAL base .9 and 1.5 mm/s, printed ratio .6; tip 1.1 and 2.8 mm/s, printed ratio .39; PMMA tip .15 and .40 cm/s, printed ratio .38; ground tracking limitations and approximately 45 seconds earlier SIBAL extinction. PMMA image caption: Coriolis deflection away from the fuel axis. SIBAL wording states that faster tip motion indicates a shrinking flame length; the coordinate convention is not supplied with that statement.
