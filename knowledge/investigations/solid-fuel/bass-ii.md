---
type: Document
title: "BASS-II: Burning and Suppression of Solids-II"
description: Full summary of the BASS-II solid-fuel combustion campaign in the ISS Microgravity Science Glovebox — overview, all six PI sub-reports, and their test matrices.
status: stable
generated: { by: "claude-code/sonnet-5", at: 2026-09-21T19:56:58Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-21T19:56:58Z }
order: 20
geometry_class: solid-fuel
sources:
  - id: bass-ii-tm-2021
    title: "Burning and Suppression of Solids-II (BASS-II) Summary Report"
    resource: "https://ntrs.nasa.gov/citations/20210011385"
verified:
  - by: human:you
    at: 2026-09-21T19:56:58Z
---

> [!NOTE]
> Geometry class: **large-scale solid-fuel burn** (small-duct scale). Directly
> comparable to [SAFFIRE](../solid-fuel/saffire.md), which shares this geometry
> class at a much larger physical scale. Not directly comparable to
> [FLEX](../droplet-combustion/flex.md) (droplet combustion) or
> [ACME](../gaseous-flames/acme.md) (gaseous laminar flames) without noting
> the geometry mismatch.

BASS-II tested solid-fuel combustion aboard the International Space Station
(ISS), using the Microgravity Science Glovebox (MSG) in the Destiny
laboratory, to determine whether materials burn as well as, or better than,
they do on Earth once ventilation and other conditions are controlled
for.[^bass-ii-tm-2021] The report is a compendium: an overview section
followed by six independent principal-investigator (PI) sub-reports —
Bhattacharjee, Fernandez-Pello, Miller/Wichman, Olson, and T'ien each
contribute their own objectives, methods, results, and conclusions, several
reproducing full journal articles. This entry covers all of them.

## Why it was run

NASA certifies spacecraft materials for flammability using an upward-burning
test in normal Earth gravity, treated as the worst-case geometry for
flammability on Earth — but this may not be conservative for flammability in
space. BASS-II set out to identify the actual worst case
for material flammability in spacecraft environments, and to compare it
against the terrestrial upward-burning screening test.[^bass-ii-tm-2021]

## Experiment setup (overview)

The BASS-II hardware — a flow duct, still and video cameras, and associated
plumbing — was installed in the MSG working volume aboard the ISS. The flow
duct was a black-anodized rectangular duct with rounded corners. Flow was
driven by a variable-speed fan, with two optional restrictors to reduce duct
velocity.

Ambient O₂ concentration in the MSG working volume was varied using ISS
gaseous nitrogen (GN2) to vitiate the atmosphere from standard ISS levels down
to near the flammability limit. A range of fuel geometries was tested: cast
PMMA rods, thin-to-thick PMMA slabs, a section of a PMMA sphere, and
cotton-fiberglass blended fabric.[^bass-ii-tm-2021]

## Structured facts (overview, §1)

### Experimental conditions

| Field | Value | Report section |
| --- | --- | --- |
| Facility | Microgravity Science Glovebox (MSG), ISS Destiny Lab | §1.2 |
| Flow duct dimensions | 7.6 by 7.6 by 17 cm, rounded corners | §1.2 |
| Max flow velocity, no restrictors | ~55 cm/s | §1.2 |
| Max flow velocity, two restrictors | ~35 cm/s | §1.2 |
| O₂ concentration range tested | ~21 percent (ambient ISS) down to ~14 percent (near-limit) | §1.2 |
| Fuel: PMMA rod diameter | 6.35 to 12.7 mm | §1.2 |
| Fuel: PMMA slab thickness | 0.125 to 5 mm | §1.2 |
| Fuel: PMMA sphere section | 4-cm-diameter sphere | §1.2 |
| Fuel: fabric width | 1 or 2 cm | §1.2 |
| Total tests conducted | 126 (more than the 103 planned) | §1.1 |

### Measured outcomes

| Field | Value | Report section |
| --- | --- | --- |
| Heat release rate, typical | well below 100 W | §1.4 |
| Heat release rate, highest recorded | close to 100 W (one long opposed thick-slab test); a briefer concurrent rod test released almost 110 W | §1.4 |
| CO:CO₂ ratio vs. efficient flue gas | efficient flue gases are typically below 0.004; most BASS-II data was well above that, indicating comparatively inefficient combustion | §1.4 |
| Global equivalence ratio (Φ) | 1.3 — fuel-rich / under-ventilated | §1.5 |
| Samples returned to Earth for analysis | 34 (of which 19 were usable for the global equivalence ratio estimate) | §1.5 |

### Overview conclusions

Sensor data showed O₂ burning nearly stoichiometrically to CO₂, with CO
levels depending on geometry and, in some cases, the flow-velocity/geometry
combination. Heat release, estimated via O₂-consumption calorimetry, stayed
well below 100 W for most tests. Using mass-loss and O₂-consumption data, the
average global equivalence ratio was estimated at 1.3, indicating the flames
burned fuel-rich under the low-velocity forced-flow conditions
tested.[^bass-ii-tm-2021]

---

## PI report: Bhattacharjee — opposed-flow flame spread and extinction

### §2.1 Residence Time Driven Flame Spread (RTDFS)

Objective: examine how thermal and species fields diverge to cause
microgravity flame extinguishment as fuel thickness varies, using 1- and
2-cm-wide thin PMMA films (0.1–0.4 mm thick). Twenty-two
test points were obtained.

**Extinction velocities by thickness** (opposed-flow, ~21% O₂): about 1 cm/s
for 100, 200, and 300 µm samples; about 1.5 cm/s for 400 µm — extinction
velocity was found to be independent of fuel thickness. At a lower O₂ level
of about 16%, extinction velocities rose to about 2.6 cm/s (100 µm) and about
4 cm/s (200 µm) — extinction velocity increases significantly as O₂ is
reduced, still independent of thickness.

Ground-truth comparison used the SDSU vertical flame tunnel (10 by 10 cm
cross-section, opposed flow up to 100 cm/s, rotatable to alter buoyancy
effects). The RTDFS work produced two archival journal
articles and several conference papers, and vindicated the theoretical/
computational finding that critical opposed-flow extinction velocity in
microgravity is independent of fuel thickness.[^bass-ii-tm-2021]

### §2.2 Critical flow velocity for radiative extinction (journal article, reproduced in full)

Abstract finding: a closed-form formula for the critical extinction flow
velocity was derived by combining scaling arguments with a 2D computational
model, and space-based test results confirmed the prediction.

**Key results:**

| Field | Value |
| --- | --- |
| Computational extinction velocity, all 4 thicknesses, 21% O₂ | 1.5 cm/s (identical across thicknesses) |
| Computational extinction velocity, 100-µm sheet, 16% O₂ | 3.5 cm/s |
| 1g quiescent downward spread rates (21% O₂), 100, 200, 300, 400 µm | 1.x, 1.6, 1.2, 0.9 mm/s respectively |

Conclusion: fuel thickness does not affect the critical extinction velocity,
though it does increase if O₂ is decreased; the derived closed-form
expression Vg,cr = εσ[(Tf⁴−T∞⁴)]/[cgρg(Tv−T∞)] (ε = surface emissivity, σ =
Stefan-Boltzmann constant, cg = gas specific heat, ρg = gas density at Tv, Tv
= vaporization temperature, T∞ = ambient temperature, Tf = adiabatic flame
temperature) agrees well with experiment and computation.[^bass-ii-tm-2021]

### §2.3 Opposed-flow flame spread: microgravity vs. normal-gravity comparison (journal article, reproduced in full)

Compares BASS-II opposed-flow spread data (varying PMMA thickness, ISS) with
downward-spreading 1g data from SDSU, to establish the thermal regime for
thin fuels.

**Key results:**

| Field | Value |
| --- | --- |
| Average 1g downward spread rate, 100-µm sample | 2.0 mm/s |
| Highest microgravity spread rate, 100-µm sample | 2.2 mm/s (opposing flow varied ~40 cm/s down to ~1 cm/s) |
| Experimentally determined de Ris flame coefficient F | 4.76 (21% O₂/79% N₂ mixture); ~3% greater using adiabatic flame temperature |
| Effective buoyancy-driven velocity, downward 1g spread | 1.9 cm/s (vs. 6 cm/s in earlier computational work using a different flame-coefficient definition) |
| Characteristic buoyancy-driven natural convection velocity (scaling estimate) | 10.2 cm/s |
| Thermally thin/thick transition thickness, downward spread in air | 5.2 mm (2τ) |

Conclusion: microgravity opposed-flow data and 1g downward-spread data agree
well within experimental uncertainty, establishing that the thermal-regime
limit extends to downward spreading in atmospheric Earth conditions — meaning
the thermal-spread theory validated in microgravity can also describe the
common 1g downward-burn case.[^bass-ii-tm-2021]

---

## PI report: Nomex flammability (§3.1)

Objective: evaluate Nomex® flammability (heavily used aboard the ISS as a
fire barrier) and burn any remaining BASS-I samples (a single wax
candle).

**Result:** all three Nomex® samples did not ignite — "an excellent result
for fire safety aboard the ISS."[^bass-ii-tm-2021] The wax candle test
successfully ignited in opposed flow and burned at five different flow
velocities; an ejected wax droplet during testing illustrated the flame-spread
hazard of melting plastics in microgravity (a low-viscosity burning droplet
can be ejected and ignite other materials).[^bass-ii-tm-2021]

---

## PI report: Fernandez-Pello — opposed-flow flame spread over PMMA rods (§4.1)

Objective: understand mechanisms controlling flame spread over solid
combustible surfaces in a spacecraft environment, using PMMA rods of
different diameters under different O₂ concentrations and low flow
velocities — plus the effect of transverse curvature (cylindrical
geometry).

### Test matrix (Table 4.1 — rod diameters tested, black vs. clear PMMA)

| Rod diameter | Black PMMA test conditions | Black PMMA samples burnt | Clear PMMA test conditions | Clear PMMA samples burnt |
| --- | --- | --- | --- | --- |
| 6.35 mm | 23 | 9 | 4 | 2 |
| 9.525 mm | 12 | 4 | 3 | 1 |
| 12.7 mm | 12 | 4 | 0 | 0 |
| **Total** | **47** | **17** | **7** | **3** |

Results are limited to black PMMA (the majority of tests; clear-PMMA data
was too limited to present).

### Test matrix (Table 4.2 — oxidizer/flow ranges by rod diameter)

| Rod diameter | O₂ concentration | Flow velocity |
| --- | --- | --- |
| 6.35 mm | 16.8 to 18.9 vol% | 0.0041 to 0.075 m/s |
| 9.525 mm | 17.5 to 20.9 vol% | 0.043 to 0.02 m/s |
| 12.7 mm | 17.6 to 20.7 vol% | 0.0137 to 0.0164 m/s |

For reference, the characteristic buoyant velocity induced by a heated sample
in 1g is approximately 0.50 m/s — an order of magnitude greater than the
largest forced-flow velocity tested in microgravity.

### Key results

- Sustained flame spread was not observed below ~4 mm/s opposed-flow velocity
  for the 6.35- and 9.525-mm rods.
- **Minimum O₂ for flame spread**: 17.5% in microgravity vs. 19% in normal
  gravity — flame spread was sustained at lower O₂ in microgravity, likely
  because the microgravity opposed-flow velocity is much lower than the
  buoyancy-induced flow in 1g.
- Decreasing rod diameter increases flame spread rate in both 1g and
  microgravity; flame spread in microgravity is appreciably faster than in 1g
  for the same rod diameter.
- Burn morphology differs qualitatively: in microgravity, the flame tail opens
  up and the rod extends past the flame as spreading continues (unique to
  microgravity); in 1g, the flame burns the rod in a conical regression with
  the rod tip always within the flame.
- Premixed flame oscillations along concurrent-geometry rods persist much
  longer in microgravity than in normal gravity, due to lower convective
  cooling — implying spacecraft fire suppression should continue until burning
  material has cooled and stopped emitting vapors.[^bass-ii-tm-2021]

---

## PI report: Miller and Wichman — narrow channel apparatus / thick-fuel flat samples (§5.0)

Objective: gather microgravity data for flame spread over thick PMMA fuel
(1–5 mm) and compare to normal-gravity narrow-channel-apparatus (NCA) data,
to help replace NASA-STD-6001 Test 1 as the spacecraft material screening
method. Institutions: Case Western Reserve University, UC
Berkeley, NASA Glenn Research Center, San Diego State University, and
Michigan State University.

### Full test matrix (Table 5.1 — all 20 flat-PMMA tests)

| Test | Thickness (mm) | Width (cm) | Sides burning | Velocity (cm/s) | Spread rate (mm/s) | Burn time (min) | Initial O₂ (%) | Final O₂ (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1 | 1 | 2.2 | 1 | 9 | 0.071 | 6.4 | 22.2 | 21.9 |
| M2 | 3 | 2.2 | 1 | 20 and 15 | 0.052 and 0.033 | 22.9 | 22.2 | 21.2 |
| M3 | 5 | 2.2 | 1 | 10 and 20 | 0.029 and 0.024 | 20.1 | 20.8 | 19.7 |
| M4 | 5 | 2.2 | 2 | 5 and 3 | 0.045 and 0.033 | 19.8 | 21.8 | 19.8 |
| M5 | 3 | 2.2 | 2 | 10 | 0.071 | 27.2 | 22.2 | 19 |
| M6 | 1 | 2.2 | 2 | 10 and 8 | Not tracked | 16.8 | 21.8 | 20.7 |
| M7 | 1 | 1.2 | 2 | 10, 6, 5, and 3 | 0.106, 0.099, 0.083, and 0.07 | 18.4 | 18.9 | 18.4 |
| M8 | 2 | 1.2 | 2 | 10, 6, and 5 | 0.057, 0.056, and 0.04 | 25.2 | 19.1 | 18.2 |
| M9 | 3 | 1.2 | 2 | 14 | 0.025 | 16.8 | 18 | 17.6 |
| M10 | 4 | 1.2 | 2 | 15 and 10 | 0.0373 and 0.03 | 30.5 | 20.1 | 18.6 |
| M11 | 5 | 1.2 | 2 | 21, 15, and 13 | 0.048, 0.028, and 0.022 | 28.5 | 20 | 18.5 |
| M12 | 2 | 2.2 | 2 | 12 and 10 | Not tracked | 16.2 | 21.7 | 20.4 |
| M13 | 4 | 2.2 | 2 | 6, 5, and 4 | 0.047, 0.035, and 0.033 | 20.5 | 20.8 | 19 |
| M14 | 2 | 2.2 | 1 | 15, 14, and 10 | 0.0624, 0.055, and 0.0353 | 15.4 | 22.2 | 21.6 |
| M15 | 4 | 2.2 | 1 | 20 | 0.045 | 22.0 | 21 | 20 |
| M16 | 1 | 2.2 | 2 | 5, 3, and 2 | 0.144, 0.1309, and 0.1062 | 8.4 | 19.2 | 18.7 |
| M17 | 2 | 2.2 | 2 | 5, 4, and 3 | 0.053, 0.042, and 0.026 | 30.7 | 18.8 | 17.1 |
| M18 | 3 | 2.2 | 2 | 10 and 8 | 0.026 and 0.013 | 25.5 | 17.9 | 16.8 |
| M19 | 4 | 2.2 | 2 | 10 and 6 | 0.027 and 0.0159 | 25.7 | 19 | 17.4 |
| M20 | 5 | 2.2 | 2 | 10 | 0.012 | 16.5 | 18 | 17.4 |

All flow was opposed; airflow ranged 3–20 cm/s across the campaign; MSG
working volume was 255 L.

### Key results

- At near-air O₂, flames spread over the fuel surface without burning
  through, for both one- and two-sided samples; as O₂ dropped to ~19%,
  two-sided samples could no longer spread across the surface and instead
  consumed fuel from the trailing edge.
- Spread rate decreases as thickness increases and as forced-flow velocity
  decreases. For one-sided samples, thicker fuel meant lower O₂ needed for
  extinction but higher forced-flow velocity needed for extinction. Two-sided
  extinction velocities were significantly lower than one-sided (less heat
  loss without a substrate). 1.2-cm-wide samples extinguished at ~1% higher O₂
  than 2.2-cm-wide samples (more relative heat loss to the sample
  holder).
- An FDS (Fire Dynamics Simulator) model of the same geometry over-predicts
  flame spread rate relative to experiment; chemical-kinetics and
  material-property refinement was identified as needed future
  work.[^bass-ii-tm-2021]

### Conclusions (§5.7)

"The Burning and Suppression of Solids (BASS) experiments gave some of the
first ever data regarding combustion of thick fuels in microgravity."
Two-sided burns spread faster than one-sided; thicker fuel takes longer to
spread and so has a lower spread rate.[^bass-ii-tm-2021]

---

## PI report: Olson — microgravity flammability boundary for PMMA rods (§6.1)

For the first time, a series of concurrent rod flammability tests were
conducted in microgravity aboard the ISS: 0–55 cm/s flows past three sizes of
clear and black PMMA rods, O₂ varied 13.6–22.2%.[^bass-ii-tm-2021]

### Key results

**Ignition delay**: at higher O₂, ignition occurred within ~40 s; below 16%
initial O₂, ignition delay increased significantly (up to 230 s for larger
rods). Below ~14.5% O₂, sustained ignition could not be achieved at all.
Critically: **NASA's Test 1 uses a fixed ~25 s ignition time — shorter than
many successful microgravity ignitions observed here, meaning materials that
would ignite given more time could pass Test 1 as non-flammable.** The
ignition delay in these tests could be up to almost 10 times longer than the
NASA-STD-6001 standard igniter on-time.[^bass-ii-tm-2021]

**Quenching extinction**: flames shrink to a hemispherical blue shape before
quenching; prequenching oscillations at 1.1 Hz were observed, similar to
quiescent candle-flame oscillations previously reported in
microgravity.[^bass-ii-tm-2021]

**Blowoff extinction**: initiated by a hole forming in the flame sheet at the
stagnation region; once blown more than one gas-phase thermal length (ℓ)
downstream, the flame cannot re-propagate upstream even if flow is reduced.
ISS blowoff limits agreed well with 5.18-s Zero Gravity Research Facility drop
tower limits.[^bass-ii-tm-2021]

**Flammability boundary**: minimum in the boundary occurs at stretch rate a
of 8 to 12 s⁻¹. Flames are globally stoichiometric at higher
O₂ but become more fuel-rich as O₂ approaches the minimum (excess pyrolyzate
leaking from the open tail of hemispherical flames); CO production and CO:CO₂
ratio both increase at low O₂, indicating O₂ — not fuel — is the limiting
reactant near the boundary.[^bass-ii-tm-2021]

**Energy balance**: on the blowoff branch, heat losses are negligible; in the
quenching region, surface radiative loss dominates. At the bottom of the
flammability map, heat losses are only 30 percent of total heating rate to the
surface — the blowoff-to-quenching transition occurs when convective and
diffusive flow magnitudes converge.[^bass-ii-tm-2021]

---

## PI report: T'ien — concurrent flame growth, spread, and extinction over SIBAL fabric (§7.1)

Studied flame growth, spread, and extinction of composite cotton-fiberglass
(SIBAL) fabric in low-speed concurrent forced flow — samples 1.2 and 2.2 cm
wide, 10 cm long; O₂ varied 21% down to 16%; flow speed 40 cm/s down to
1 cm/s. Quenching speeds were found between 1 and 5 cm/s,
with higher speed required in lower-O₂ atmosphere — "the first time that a
low-speed quenching boundary in concurrent spread is determined in a clean
and unambiguous manner."[^bass-ii-tm-2021]

### Full test matrix (Table 7.1 — 27 BASS-II tests + 4 BASS tests, all SIBAL fabric, concurrent flow)

| Test | Width (cm) | Flow (cm/s) | O₂ (vol%) | Comments |
| --- | --- | --- | --- | --- |
| GMT45-T1 | 2.2 | 10 | 18.5 (reading may be inaccurate) | — |
| GMT45-T2 | 2.2 | 10 to 5 | 18.5 (reading may be inaccurate) | — |
| GMT45-T4 | 2.2 | 10 to 2.2 | 18.7 | Quenched |
| GMT45-T15 | 2.2 | 10 to 29 | 18.7 | No blowoff |
| GMT100-T5 | 2.2 | 10 to 2.4 | 18.8 | — |
| GMT100-T6 | 2.2 | 4.5 to 2.6 | 18.8 | — |
| GMT100-T13 | 2.2 | 4 to 2.2 | 17.5 | Quenched |
| GMT100-T16 | 2.2 | 4 to 3 | 17.6 | — |
| GMT175-T9 | 2.2 | 10 | 16.4 | No ignition |
| GMT175-T10 | 2.2 | 5 | 16.4 | No ignition |
| GMT175-T18 | 2.2 | 5 to 2.6 | 17.4 | Quenched |
| GMT178-T11 | 2.2 | 4 | 17.1 | — |
| GMT178-T12 | 2.2 | 5 | 16.8 | No ignition |
| GMT178-T14 | 2.2 | 4 to 2.8 | 16.9 | Quenched |
| GMT178-T17 | 2.2 | 6 to 53 | 16.9 | No blowoff |
| GMT190-T19 | 1.2 | 11 | 17.2 | — |
| GMT190-T20 | 1.2 | 11 to 3 | 17.2 | Quenched |
| GMT190-T21 | 1.2 | 11 to 47 | 17.2 | Blow-off |
| GMT190-T22 | 1.2 | 10.5 to 5 | 17.1 | Quenched |
| GMT190-T23 | 2.2 | 10 | 17.2 | Reused, did not ignite |
| GMT190-T24 | 2.2 | 10 | 18.2 | Reused, one-sided flame |
| GMT216-T25 | 2.2 | 5 to 2.5 | 20.8 | Reused, ignited |
| GMT216-T26 | 2.2 | 5 to 2.5 | 20.8 | Reused, ignited |
| GMT216-T27 | 1.2 | 5 to 2 | 20.7 | Reused, ignited |
| GMT216-T28a | 1.2 | 5 | 20.7 | Reused, did not ignite |
| GMT216-T28b | 1.2 | 5 | 20.7 | Reused, did not ignite |
| GMT216-T29 | 1.2 | 5 to 2 | 20.7 | Reused, ignited |
| GMT96-T8 (BASS) | 2.2 | 5 | 21 | BASS series |
| GMT96-T7 (BASS) | 2.2 | 10 | 21 | BASS series |
| GMT131-T10 (BASS) | 1.2 | 11 | 21 | BASS series |
| GMT222-T11 (BASS) | 1.2 | 19 | 21 | BASS series |

### Key results

- A 2.2-cm sample at 10 cm/s, 21% O₂ reached steady spread (constant length)
  at ~19 s, lasting ~9 s, with total burnout at ~40 s.
- The same width sample at 5 cm/s took over 60 s to burn; steady spread
  lasted ~21 s (longer than the 10 cm/s case) with a shorter flame and slower
  spread.
- Flames spread more slowly across narrower samples, at lower flow
  velocities, and at lower O₂ percentages.[^bass-ii-tm-2021]

### Conclusions (§7.1.5)

Quenching velocities are small (1–5 cm/s); experimental data qualitatively
supports earlier theoretical predictions of solid flammability limits at low
flow velocities due to radiative and conductive losses. The flame image
sequence at quenching shows the flame shrinking in both length and width,
extinguishing three-dimensionally.[^bass-ii-tm-2021]

---

## Appendix A: full per-sample test matrices (data-quality note)

Appendix A of the source report contains six detailed test matrices — one per
PI (A.1 Bhattacharjee, A.2 Ferkul, A.3 Fernandez-Pello, A.4 Miller, A.5 Olson,
A.6 T'ien) — covering roughly 24, 6(+continuation), 29, 22, 26, and 31 table
rows respectively in the converted extraction (approximate; some tables
continue under a "Concluded" heading). Each row appears to record a single
test's date, timestamp, sample ID, fuel description, apparatus/flow
configuration, velocity settings, timing, O₂ readings, regression data, and
free-text observations.

**These tables are not reproduced row-by-row here.** The PDF-to-markdown
conversion lost every column header for all six tables — each header row
converted to empty cells, with only the final "Test observations and
anomalies" column retaining its label. Sample row from A.1 (Bhattacharjee),
verbatim, to show what survives without labels:

> `2/19/2014 GMT 2014 050 | 10:09:50 to 10:10:16 | 7 | B1 | 147 | 100-µm PMMA film, 2 cm wide | Integral 2 | Opposed | 62 | 5 | 50 | --- | 8 | NA N | CL A | -4 | off | --- | F2 | 1,000 | Cont | 7 | 57 | 22.2 | 22.2 | 20.6 | 20.6 | 0.44 | 0.44 | 0 | 6 | Ignited very quickly, turned flow off after spread halfway; flame extinguished very quickly; and sooty with blue leading edge`

Some columns are identifiable from context (date, sample ID, fuel
description, flow direction, free-text observations), but others (e.g. "NA
N", "CL A", "F2") are apparatus/setting codes whose meaning is not
recoverable from the surrounding text. Labeling them without that key would
be a guess, not a fact — inconsistent with this corpus's citation standard.
**Open item**: recovering these headers requires visual inspection of the
original PDF's Appendix A tables (where the header text may be rotated or
laid out in a way the text extraction couldn't capture), not a text-only
re-extraction. Flagged for a follow-up pass rather than fabricated here.

## Open questions

- Appendix A's ~140 individual per-test data rows are not transcribed with
  labeled columns, for the reason above.
- Appendix B (dilution model/verification), Appendix C (anomalies), and
  Appendix D (thermal analysis) are not covered in this entry.
- Figures throughout (flame images, spread-rate plots, flammability maps) are
  referenced in the prose above but not reproduced.

[^bass-ii-tm-2021]: BASS-II Summary Report (NASA/TM-20210011385). §1.1 Background: "BASS-II tests the hypothesis that materials in microgravity, with adequate ventilation, burn as well if not better than the same material in normal gravity with other conditions being identical... NASA tests and controls materials from a flammability perspective using an upward burning test in normal gravity, which is considered to be the worst-case geometry for flammability of the material on Earth. However, it may not be conservative for flammability in space." "A total of 126 tests were conducted as part of BASS-II. This is more than the planned 103 tests, since some samples were burned more than once." §1.2 Experiment Description: "The BASS-II hardware consists of a flow duct, still camera, video camera, video and power boxes, external control box and associated plumbing, and mounting systems." "The black anodized 7.6- by 7.6- by 17-cm rectangular flow duct with rounded corners was originally built to perform gas jet diffusion flame studies." "With no restrictors, the maximum flow velocity was ~55 cm/s, and with two restrictors this was reduced to ~35 cm/s." "O2 concentrations in the MSG working volume were varied during the testing from ambient ISS O2 levels (~21 percent O2) down to ~14 percent O2 for very near limit flames." "A number of sample geometries were used in BASS-II: cast polymethylmethacrylate (PMMA) samples were shaped as rods of various diameters (6.35 to 12.7 mm), thin to thick slabs (0.125 to 5 mm), or a section of a 4-cm-diameter sphere. In addition, flat cotton-fiberglass blended fabric samples were also burned... The flat samples were 1 or 2 cm wide." §1.4 Combustion Products: "we estimate the HRRs to be typically well below 100 W... The one long opposed thick slab test that caused the lower downstream corner of the front window damage released close to 100 W. A prior relatively brief concurrent rod test that released almost 110 W did not cause any damage." "For efficiently burned flue gases (boilers, furnaces, etc.), this ratio is typically less than 0.004. As can be seen, most of our data is well above that, indicating that microgravity flames are comparatively inefficient." §1.5 Global Equivalence Ratio: "Using the observed slope of 0.4582 O2 vol% per gram of fuel, and the molecular weight for PMMA of 100 g/gmol for the majority of the data, we can use the above equations to solve for the effective equivalence ratio for the tests: Φglobal = 1.3, which is fuel rich." "To date, 34 burned BASS-II samples have been returned to Earth for postflight analysis... For the remaining 19 samples, mass loss is compared to O2 consumption." §1.6 Overall Conclusions: "Sensor data from the tests showed that the O2 was burning nearly stoichiometrically to CO2, and that CO levels appear to be a function of geometry and, in some cases, the flow velocity and geometry combination... This showed that most of the tests released well below 100 W... the global equivalence ratio for the tests is estimated to be 1.3 on average, which indicates the flames were burning fuel rich under the low-velocity forced-flow conditions." §2.1 Residence Time Driven Flame Spread: "The objective of the Residence Time Driven Flame Spread (RTDFS) experiment of Burning and Suppression of Solids-II (BASS-II) was to examine how thermal and species fields can diverge and lead to microgravity flame extinguishment by varying fuel thickness." "Samples were 1- and 2-cm-wide thin films of plastic (PMMA (polymethylmethacrylate)). Thicknesses were between 0.1 and 0.4 mm." "Twenty-two test points were obtained with the BASS-II experiments." "When tests are repeated with samples of different thicknesses, the extinction velocities are found to be about 1 cm/s for 100, 200, and 300 μm and about 1.5 cm/s for 400 μm... It can be safely concluded that the extinction velocity does not depend on the fuel thickness. Tests were also conducted at a lower O2 level of about 16 percent for two different thicknesses and the extinction velocities were found to be about 2.6 cm/s for 100 μm and about 4 cm/s for 200 μm... it is clear that the extinction velocity significantly increases as the O2 level is reduced and is independent of the fuel thickness." "The SDSU vertical flame tunnel... has a cross section of 10 by 10 cm... and an opposed flow up to 100 cm/s can be created... One of the major improvements made to the tunnel is the ability to rotate it and set it at any desired angle." "The Residence Time Driven Flame Spread (RTDFS) experiment of Burning and Suppression of Solids-II (BASS-II) resulted in the publication of two archival journal articles, several conference papers... RTDFS vindicated the theoretical and computational findings that the critical opposed-flow velocity at which radiative extinction occurs in a microgravity environment is independent of fuel thickness." §2.2 Critical Flow Velocity for Radiative Extinction: "This report combines scaling arguments with computational results to predict a critical flow velocity for such flame extinction. Results from the recently conducted limited number of space-based tests, presented in this report, seem to confirm the prediction validating the closed-form formula for the critical extinction velocity." "[The critical velocity] where ε is surface emissivity, σ is Stefan-Boltzmann constant, cg is the specific heat of gas, ρg is gas density evaluated at Tv, Tv is the vaporization temperature, T∞ is ambient temperature, and Tf is adiabatic flame temperature. It establishes that even though the flame spread rate is inversely proportional to the fuel thickness, the critical velocity is independent of the fuel thickness. Prediction from this formula agrees remarkably well with the experimental and computational results." §2.2.6 Computational Results: "the extinction velocity is identical at 1.5 cm/s for all the four thicknesses studied... The extinction velocity is found to be 3.5 cm/s as opposed to 1.5 cm/s at 21 percent O2... when the computational model is used for downward spread configuration in a quiescent 1g environment, a steady spread results for 21 percent O2 with spread rates of 1.x, 1.6, 1.2, and 0.9 mm/s, for 100, 200, 300 and 400 µm, respectively." §2.2.8 Conclusions: "Results from four different fuel thicknesses indicate that fuel thickness does not affect the critical velocity, which increases if the O2 level is decreased. A two-dimensional computation model confirms this finding... Prediction from this formula agrees remarkably well with the experimental and computational results." §2.3.1 Abstract: "This work presents opposed-flow flame spread data over varying thicknesses of polymethylmethacrylate obtained in the International Space Station... It also presents a larger set of spread rate data for the downward spreading configuration at normal gravity." §2.3.7 Results and Discussion: "The average spread rate over the 100-µm-thick sample in the normal-gravity experiments is found to be 2.0 mm/s... the highest spread rate obtained is about 2.2 mm/s even though the opposing flow velocity was varied from about 40 cm/s to about 1 cm/s." "For the experimental value of Vf,thin = 2.2 mm/s for τ = 50 µm, the value of the de Ris flame coefficient F can be calculated from Equation (2.9) as 4.76." "Using the experimental value of Vf,thick = 0.044 mm/s, the effective value of the opposing flow created by natural convection can be calculated... as 0.019 m = 1.9 cm... In earlier computation work (Ref. 17), the effective velocity was calculated as 6 cm/s based on a more complex definition of the flame coefficient. The current experimental result, on the other hand, is based on F defined in terms of adiabatic flame temperature. The characteristic buoyancy-driven natural convection flow... VNC = 10.2 cm/s, which is about the same order as the effective velocity." "The transition thickness (2τtransition) can be calculated from this expression as 5.19 mm for downward flame spread in ambient air." §2.3.8 Conclusion: "A curve fit of maximum spread rate against fuel thickness using de Ris formula for the thermal regime was used to determine the de Ris coefficient F as 4.76 for an oxidizing mixture of 21 percent O2 and 79 percent N2. Based on adiabatic flame temperature, F is only about 3 percent greater... Data from downward spread in ambient air is shown to correlate well (within the experimental uncertainty) with the microgravity data, establishing that the thermal limit is extended to downward spreading configuration in atmospheric condition on Earth... the effective velocity induced by buoyancy as 1.9 cm/s... For PMMA in ambient air, this transition thickness is evaluated to be 5.2 mm." §3.1 Nomex® Flammability: "The objective of the Nomex® (DuPontTM) sample tests was to evaluate the flammability of Nomex®, since it is heavily used aboard the International Space Station (ISS) as a fire barrier." §3.1.1 Results: "The three Nomex® samples did not ignite, which is an excellent result for fire safety aboard the ISS. The wax candle test successfully ignited in an opposed flow (akin to holding a candle upside down) and burned at five different flow velocities... If the melt viscosity is low enough, burning droplets can be ejected and possibly ignite other materials." §4.1 Opposed-Flame Spread Task: "The scientific objective of the Burning and Suppression Solids-II (BASS-II) opposed-flow flame spread test is to further understand the mechanisms controlling the spread of flames over the surface of solid combustible materials, particularly in a spacecraft environment." §4.1.1: "The tests for the present task were conducted with rods of cast PMMA with diameters of 6.35, 9.525, and 12.7 mm (1/4, 3/8, and 1/2 in., respectively) and were 57.15 mm in length." Table 4.1: rod diameters 0.00635, 0.009525, and 0.0127 m; black PMMA test conditions 23, 12, and 12 (total 47), samples burnt 9, 4, and 4 (total 17); clear PMMA test conditions 4, 3, and 0 (total 7), samples burnt 2, 1, and 0 (total 3). Table 4.2: O2 concentration 16.8 to 18.9, 17.5 to 20.9, and 17.6 to 20.7 vol%; flow velocity 0.0041 to 0.075, 0.043 to 0.02, and 0.0137 to 0.0164 m/s, by diameter. "at the point of ignition it is approximately 0.50 m/s, which is an order of magnitude greater than the largest forced-flow velocity tested in the BASS-II experiments." §4.1.2 Results: "Sustained flame spread for the conditions tested was not observed for opposed-flow velocities below approximately 4 mm/s for the 0.00635- and 0.009525-m-diameter rods." "While in microgravity, flame spread was observed at O2 concentrations as low as 17.5 percent, in normal gravity, flame spread was not observed below 19 percent." "Decreasing the rod diameter increases the flame spread rate in both 1g and microgravity environments... flame spread in microgravity is appreciably faster than in 1g for cylindrical rods of PMMA." "This wide-open flame tail with rod remaining behind is unique to microgravity. In normal gravity, the flame burns away the rod in a conical regression, and the rod tip is always within the flame." "Premixed flame oscillations along the rod have been observed for the concurrent rod geometry that persist much longer in microgravity than in normal gravity due to the lower rate of convective cooling of the rod. This suggests that spacecraft fire suppression efforts should be maintained until the burning material has cooled and stopped emitting vapors." §5.0 / §5.1 Narrow Channel Apparatus: "Combustion of clear cast polymethylmethacrylate (PMMA) samples 10 cm long by either 1 or 2 cm wide with thicknesses ranging from 1 to 5 mm was investigated in opposed flow." §5.2 Introduction: "The institutions taking part in BASS-II operations are Case Western Reserve University; University of California, Berkeley; NASA Glenn Research Center; San Diego State University; and Michigan State University." §5.3 Experimental Setup and Summary: "The BASS-II flow duct is placed inside the Microgravity Science Glovebox (MSG) (255 L) onboard the International Space Station (ISS)... A total of 20 PMMA flat samples were burnt during the BASS-II experimentation (Table 5.1). The sample thickness varied from 1 to 5 mm thick... Airflow speeds ranging from as low as 3 cm/s up to 20 cm/s were used in the flow duct." Table 5.1 (20 tests M1–M20): as reproduced in the Full test matrix table above, verbatim from the source's own columns (Test no., Thickness mm, Width cm, One/two sides burning, Velocity cm/s, Spread rate mm/s, Burn time min, Initial O2 vol%, Final O2 vol%). "At near-air O2 concentrations, the flames spread over the fuel surface without burning through for both one-sided and two-sided samples. As O2 concentrations were reduced to approximately 19 percent however, the flames could no longer spread across the surface of the two-sided fuel, but rather completely consumed the fuel from the trailing edge." "Spread rates decrease as thickness increases, and also decrease as forced-flow velocity decreases... there was a clear trend that as thickness increased, the O2 concentration for extinction decreased but the forced-flow velocity for extinction increased... the extinction velocities were significantly lower than for the one-sided samples... the 1.2-cm-wide samples did extinguish approximately 1 percent O2 higher than the 2.2-cm-wide samples." §5.7 Conclusions: "The Burning and Suppression of Solids (BASS) experiments gave some of the first ever data regarding combustion of thick fuels in microgravity... In general, the flames spread faster for two-sided burns compared to one-sided burns. The greater the thickness of the fuel, the greater is the time taken for the flame to spread and so the lower is the spread rate... The model currently predicts much higher spread rates than those obtained in the experiment." §6.1.1 Abstract: "For the first time, a series of concurrent rod flammability tests were conducted in microgravity aboard the International Space Station. A small flow duct was used to create 0- to 55-cm/s flows past the three sizes of clear and black polymethylmethacrylate rods. The ambient O2 concentration in the Microgravity Science Glovebox was varied from 13.6 to 22.2 percent." §6.1.4.1 Ignition Delay Time: "At higher O2 concentrations, ignition occurred within approximately 40 s. Below an initial O2 concentration of 16 percent, the ignition delay time increased significantly. Larger rods take longer to ignite, especially at lower O2 concentrations (up to 230 s)... Below an initial O2 concentration of ~14.5 percent O2, a sustained ignition could not be achieved." "NASA's Test 1... is an upward flame spread test that has a fixed ignition time of ~25 s... If the material is not ignited by this time, it passes the test. However... a longer ignition time may successfully ignite the material, especially at the lower O2 concentrations." §6.1.4.2 Quenching Extinction: "These all-blue flames are roughly hemispherical in shape." "The radiometer signal oscillates at approximately 1.1 Hz... These oscillations are very similar to those observed for candle flames in a quiescent environment." §6.1.4.3 Blowoff Extinction: "Blowoff was defined as the instant when the stagnation region developed a hole... Blowoff extinction limits from the ISS experiments agree well with Zero Gravity Research Facility 5.18-s drop test limits." §6.1.4.4 / §6.1.6 Conclusions: "The minimum in the flammability boundary is at a of 8 to 12 s-1... Gas sensor data and rod mass loss estimates indicate that the flames are globally stoichiometric at higher O2 concentrations but become more globally fuel rich as the minimum O2 concentration is approached... CO production also increases significantly at low O2 levels... this data suggests that the limiting reactant at the lowest O2 concentrations is the O2 rather than the fuel." "in the blowoff branch, heat losses are negligible. In the quenching region, surface radiative loss dominates... At the bottom of the flammability map, heat losses are only 30 percent of the total heating rate to the surface." "The ignition delay time can be up to almost 10 times longer than the NASA STD-6001 standard igniter on time." §7.1.1 Abstract: "flame growth, spread, and extinction over a composite cotton-fiberglass fabric blend (referred to as the SIBAL... fabric) were studied in low-speed concurrent forced flows... The fuel samples measured 1.2 and 2.2 cm wide and 10 cm long. Ambient O2 was varied from 21 percent down to 16 percent and flow speed from 40 cm/s down to 1 cm/s... The quenching speeds were found to be between 1 and 5 cm/s with higher speed in lower O2 atmosphere... This is the first time that a low-speed quenching boundary in concurrent spread is determined in a clean and unambiguous manner." §7.1.4 Results and Discussion: "A total of 27 tests were carried out for the fabric samples in BASS-II, including six quenching tests, three nonignited tests, and one blowoff test... In addition, four tests from the BASS series were selected as listed at the bottom of Table 7.1." Table 7.1 (31 tests): as reproduced in the Full test matrix table above, verbatim from the source's own columns (Test number, Sample width cm, Flow cm/s, O2 vol%, Comments). "At about 19 s, the flame reached a limiting constant length and a steady spread rate relative to the laboratory. This steady spread state lasted for around 9 s... The whole combustion process took about 40 s." "Because the flow speed is lower, it took more than 60 s to burn the whole sample. Steady spread time lasts for about 21 s, much longer than the 10-cm/s flow case." "Flames spread more slowly across the narrower samples, at lower flow velocities and at lower O2 percentages." §7.1.5 Conclusions: "The quenching velocities are small (between 1 and 5 cm/s), and an accurate determination is necessary to resolve the slope of the quenching boundary. The experimental data obtained supports earlier theoretical predictions (at least qualitatively) of solid flammability limits at low flow velocities due to radiative and conductive losses. The flame image sequence at quenching shows the flame shrinks both in length and width and the flame goes out in a three-dimensional manner." Appendix A: "These summary test matrices are grouped by principal investigator with Bhattacharjee in Table A.1, Ferkul in Table A.2, Fernandez-Pello in Table A.3, Miller in Table A.4, Olson in Table A.5, and T'ien in Table A.6." Table A.1 sample row: "2/19/2014 GMT 2014 050 | 10:09:50 to 10:10:16 | 7 | B1 | 147 | 100-µm PMMA film, 2 cm wide | Integral 2 | Opposed | 62 | 5 | 50 | --- | 8 | NA N | CL A | -4 | off | --- | F2 | 1,000 | Cont | 7 | 57 | 22.2 | 22.2 | 20.6 | 20.6 | 0.44 | 0.44 | 0 | 6 | Ignited very quickly, turned flow off after spread halfway; flame extinguished very quickly; and sooty with blue leading edge."
