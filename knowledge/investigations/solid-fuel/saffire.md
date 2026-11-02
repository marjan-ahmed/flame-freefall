---
type: Document
title: "SAFFIRE VI: Preliminary Results from the Spacecraft Fire Experiment"
description: Preliminary results from the final flight (Saffire VI) of NASA's Spacecraft Fire Safety Demonstration Project, with the earlier Saffire-1/Saffire-2 large-scale flammability tests as supporting background and comparison.
status: stable
generated: { by: "codex", at: 2026-11-02T12:49:15Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-11-02T12:49:15Z }
order: 21
geometry_class: solid-fuel
sources:
  - id: saffire-vi-ices-2024
    title: "Preliminary Results from the Saffire VI Experiment"
    resource: "https://ntrs.nasa.gov/citations/20240002981"
  - id: saffire-results-2017
    title: "Results of Large-Scale Spacecraft Flammability Tests"
    resource: "https://ntrs.nasa.gov/citations/20170008805"
verified:
  - by: human:you
    at: 2026-09-21T19:56:58Z
---

> [!NOTE]
> Geometry class: **large-scale solid-fuel burn**. Directly comparable to
> [BASS-II](../solid-fuel/bass-ii.md), which shares this geometry class at a
> much smaller physical scale. Not directly comparable to
> [FLEX](../droplet-combustion/flex.md) (droplet combustion) or
> [ACME](../gaseous-flames/acme.md) (gaseous laminar flames) without noting
> the geometry mismatch. This document is centered on **Saffire VI**, the
> final flight in the Saffire series; the earlier **Saffire-1** and
> **Saffire-2** flights (2017 report) are included as background and
> comparison, not as the primary subject. **Even within the Saffire series**,
> flights differ substantially in ambient pressure and oxygen concentration
> (see the tables below) — a Saffire VI result is not automatically
> comparable to a Saffire-1 or Saffire-2 result without checking those
> conditions.

Saffire VI was the sixth and final flight of NASA's Spacecraft Fire Safety
Demonstration Project, conducted on an orbiting Cygnus resupply vehicle after
it departed the ISS. It examined concurrent flame spread over large samples —
all 41 cm wide — including a thin cotton/fiberglass sheet (50 cm long),
two-sided PMMA (1 cm thick, 18 cm long), one-sided PMMA (0.5 cm thick, 18 cm
long), and Nomex fabric (7 cm long); the flame heat release was determined
and compared against the overall spacecraft temperature rise and the change
in CO₂/CO concentration. These experiments directly
address the risk that, absent this kind of data, "spacecraft designers
[have been forced] to base their designs and safety precautions on 1-g
understanding of flame spread, flame self-extinguishment, fire detection,
and suppression."[^saffire-vi-ices-2024]

## Program context

NASA's Spacecraft Fire Safety Demonstration Project was formulated to
conduct a series of large-scale experiments in spacecraft environments
representative of practical spacecraft fires; across the program, tests
spanned 1.5 to 3.2 kW in intensity with free air volumes of 17 to 19 cubic
meters.[^saffire-vi-ices-2024] The earlier Saffire-1 and Saffire-2 flights —
covered in detail under "Background: the earlier Saffire flights" below —
established the program's baseline before Saffire VI extended it to lower
ambient pressure and higher oxygen concentration, conditions closer to
proposed future exploration atmospheres.

## Structured facts — Saffire VI

### Experimental conditions

| Field | Value | Report section |
| --- | --- | --- |
| Facility | Saffire Flow Unit (SFU), positioned near the end cone of the Cygnus vehicle; Far Field Diagnostics (FFD) unit in a mid-deck locker near the hatch | §II Experimental Hardware |
| Duct geometry (Saffire IV–VI) | 45 cm wide, duct half-height reduced from 25 cm (Saffire I–III) to 15 cm, to accommodate a second set of cameras | §II |
| Materials tested | SIBAL cloth, two-sided PMMA, one-sided PMMA (Nomex sample did not ignite and was excluded from the paper) | §II |
| Fuel composition | SIBAL fabric: 75% cotton / 25% fiberglass, area density 18.05 mg/cm²; PMMA: flat, cast, one-sided (5 mm thick) or two-sided (10 mm thick) | §II |
| Sample length (this paper's samples) | SIBAL cloth 50 cm; two-sided PMMA 18 cm; one-sided PMMA 18 cm | §II, abstract |
| Sample width (all Saffire IV-VI samples) | 41 cm | Abstract |
| Air flow rate | 20 cm/s for all tests in Table 1 | §II, Table 1 |

### Full test matrix (Table 1: Saffire IV, V and VI tests considered in this paper)

| Flight/Sample | Material | Length (cm) | Air flow rate (cm/s) | Flow direction | Ambient pressure (kPa) | Oxygen concentration (mol %) | Free volume (m³) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IV-1 | SIBAL Cloth | 50 | 20 | Concurrent | 100.0 | 22.0 | 17.9 |
| V-2 | Cotton Jersey | 50 | 20 | Concurrent | 70.7 | 26.2 | 19.0 |
| VI-2 | SIBAL Cloth | 50 | 20 | Concurrent | 54.1 | 31.0 | 16.7 |
| VI-3 | Two-Sided PMMA | 18 | 20 | Concurrent | 54.6 | 30.3 | 16.7 |
| VI-4 | One-Sided PMMA | 18 | 20 | Concurrent | 55.2 | 28.8 | 16.7 |

Note: this table (and the outcomes table below) includes the thin-cotton
results from the earlier Saffire IV and V flights alongside Saffire VI,
because the source paper analyzes them together — heat release can be
estimated from spread rate for thin fuels the same way across all three
flights.[^saffire-vi-ices-2024]

### Measured outcomes (Table 2: burn duration, heat release, temperature, and gas increase)

| Flight/Sample | Material | Burn duration (s) | Peak heat release (W) | Total heat release, imaging method (kJ) | Average heat release, O₂-consumption method (W) | Total heat release, O₂-consumption method (kJ) | Max temp at SFU outlet (°C) | Max temp at FFD/nearest location (°C) | FFD inlet CO₂ increase (ppm) | CO₂ partial pressure increase (mmHg) | FFD inlet CO increase (ppm) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IV-1 | SIBAL | 130 | — | — | 3,150 | 409 | 45 | 25 | 1390 | 1.03 | 80 |
| V-2 | Cotton | 200 | — | — | 2,800 | 560 | 46 | 23 | 2360 | 1.26 | 83 |
| VI-2 | SIBAL | 112 | 3217 | 580 | 3,650 | 409 | 48 | 20 | 2800 | 1.15 | 120 |
| VI-3 | 2-sided PMMA | 780 | 3080 | 1280 | — | — | 77 | 21 | 8539 | 3.51 | 308 |
| VI-4 | 1-sided PMMA | 1200 | 1507 | 830 | — | — | 57 | 21 | 8117 | 3.37 | 320 |

Empty cells are cases where the source reports the corresponding
measurement was not available. The VI-2 (SIBAL)
sample is the one case where both the imaging-based and O₂-consumption-based
heat-release methods were used and cross-checked — they agreed within
15%.[^saffire-vi-ices-2024]

### Additional findings from this flight

- **Fire intensity**: "generally of 1.5 to 3 kW," described as "a small fire
  by terrestrial standards."
- **Temperature vs. gas hazard**: overall spacecraft temperature and
  pressure rise were found to be *less* significant than the rise in CO₂ and
  CO concentration. The outlet duct temperature
  reached a significant 70°C at the SFU outlet, while the temperature near
  the FFD (zenith) changed only slightly from baseline.
- **Toxicology limits exceeded**: NASA's Spacecraft Maximum Allowed
  Concentration (SMAC) for carbon monoxide is 425 ppm (1-hour) and 100 ppm
  (24-hour); for carbon dioxide, NASA-STD-3001 limits the 1-hour average CO₂
  partial pressure to no more than 3 mmHg. Both PMMA tests on Saffire VI
  exceeded the allowable CO₂ level, and CO levels were well above the
  24-hour SMAC and close to the 1-hour SMAC.
- **Smoke detection timing**: FFD smoke concentrations rose rapidly then
  decreased (attributed to particle loss from surface impaction). Using 1
  mg/m³ as a relatively tight alarm threshold, the FFD ionization detector
  reached that threshold at 981 seconds — by which point much of the
  hazardous gas release had already occurred.
- **Flow reduction**: for VI-3 (two-sided PMMA), duct flow was reduced from
  20 cm/s to 5 cm/s at 1120 s and terminated at 1420 s; the lower flow rate
  caused outlet CO₂ and CO levels to increase further due to reduced ambient
  dilution.[^saffire-vi-ices-2024]

## Background: the earlier Saffire flights (Saffire-1 / Saffire-2)

Saffire-1 and Saffire-2, reported in 2017, established the program before
Saffire VI: Saffire-1 assessed flame spread of a large-scale microgravity
fire (spread rate, mass consumption, heat release) and verified oxygen
flammability limits in low gravity; Saffire-2 repeated this at a higher flow
speed and with additional materials, intended to validate spacecraft
fire-response modeling and evaluate NASA's normal-gravity material
flammability screening test for low-gravity conditions.[^saffire-results-2017]

### Experimental conditions — Saffire-1 / Saffire-2

| Field | Value | Report section |
| --- | --- | --- |
| Facility | Saffire flow duct (18 in x 20 in), inside an unoccupied Cygnus resupply vehicle | Experiment |
| Saffire-1 fuel | SIBAL fabric — 75% cotton, 25% fiberglass, simple weave (60 x 40 threads/in), area density 18 mg/cm² | Saffire-I Description |
| Saffire-1 sample size | 40.6 cm wide x 94 cm long | Saffire-I Description |
| Saffire-1 flow velocity | 20 cm/s | Saffire-I Description |
| Saffire-1 initial O₂ | 21.7% (ISS reading) | Saffire-I Description |
| Saffire-2 sample size | 5 cm wide x 29 cm long (9 samples) | Saffire-2 Description |
| Saffire-2 flow velocity | 20 cm/s (all samples except 2-6, at 25 cm/s) | Saffire-2 Description |
| Saffire-2 initial O₂ | 22.1% (slightly higher than Saffire-1's 21.7%) | Saffire-2 Description |
| Saffire-2 materials | silicone sheets (0.27–1.03 mm), cotton-fiberglass fabric, PMMA/Nomex® composite, PMMA slabs (~1 cm) | Saffire-2 Description |

### Full sample matrix — Saffire-1 / Saffire-2 (Table I, conditions)

Every sample tested across both flights, with its exact geometry, flow, and
initial O₂ (as a Δ range where the source reports one — O₂ is derived from
measured CO₂ production referenced to the initial ISS O₂ reading).

| Sample | Material | Width | Thickness | Length | Flow | Direction | Initial O₂ (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1-1 | Cotton-Fiberglass | 40.6 cm | 0.37 mm | 94 cm | 20 cm/s | Concurrent | 21.7 to 21.5 |
| 1-2 | Cotton-Fiberglass | 40.6 cm | 0.37 mm | ~10 cm | 20 cm/s | Opposed | ~21.5 |
| 2-1 | Silicone | 5 cm | 0.27 mm | 29 cm | 20 cm/s | Concurrent | ~22.1 |
| 2-2 | Silicone | 5 cm | 0.61 mm | 29 cm | 20 cm/s | Concurrent | ~22.1 |
| 2-3 | Silicone | 5 cm | 1.03 mm | 29 cm | 20 cm/s | Concurrent | ~22.1 |
| 2-4 | Silicone | 5 cm | 0.37 mm | 29 cm | 20 cm/s | Opposed | ~22.1 |
| 2-5 | Cotton-Fiberglass | 5 cm | 0.37 mm | 29 cm | 20 cm/s | Concurrent | ~22.1 |
| 2-6 | Cotton-Fiberglass | 5 cm | 0.37 mm | 29 cm | 25 cm/s | Concurrent | ~22.1 |
| 2-7 | PMMA & Nomex | 5 cm | 0.85 & 0.37 mm | 5 & 24 cm | 20 cm/s | Concurrent | ~22.1 |
| 2-8 | PMMA | 5 cm | see Fig. 5 (source) | 29 cm | 20 cm/s | Concurrent | 22.1 to 22.0 |
| 2-9 | PMMA | 5 cm | 1 cm | 29 cm | 20 cm/s | Concurrent | 22.0 to 21.9 |

### Full sample matrix — Saffire-1 / Saffire-2 (Table I, ignition and results)

Same sample rows, ignition parameters and burn/spread results in microgravity
(µ-g) vs. the equivalent normal-gravity (1-g) result the source reports for
comparison. Footnote markers reproduce the source's own table notes.

| Sample | Ignition power | Ignition time | µ-g burn duration | µ-g spread extent | µ-g spread rate | 1-g burn extent | 1-g spread rate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1-1 | 182 W | 8 s | 420 s | ~84 cm | 1.8 mm/s | Complete | Acceleratory |
| 1-2 | 182 W | 8 s | 70 s | ~10 cm | 1.3 mm/s | ~0 | n/a |
| 2-1 | 80 W | 9.2 s | Insignificant | ~0 | n/a | ~Complete | Acceleratory |
| 2-2 | 80 W | 9.2 s | Insignificant | ~0 | n/a | 7.6 cm | 1.2 mm/s |
| 2-3 | 80 W | 9.2 s | Insignificant | ~0 | n/a | ~0 | n/a |
| 2-4 | 80 W | 9.2 s | Insignificant | ~0 | n/a | Complete | 0.6 mm/s |
| 2-5 | 80 W | 9.2 s | 145 s | 29 cm | 2.1 mm/s | Complete | Acceleratory |
| 2-6 | 80 W | 9.2 s | 115 s | 29 cm | 2.6 mm/s | Complete | Acceleratory |
| 2-7 | 80 W | 9.2 s | 140 s | 5 cm & 0 (ii) | n/a (Nomex) | ~0 (Nomex) | n/a (Nomex) |
| 2-8 | 97 W | 30 s | 600 s | ~10 cm (iii) | (iv) | Complete | Acceleratory |
| 2-9 | 97 W | 30 s | 900 s | ~10 cm (iii) | (iv) | Complete | Acceleratory |

Table notes: (ii) the PMMA portion was completely consumed but the Nomex was
not ignited; (iii) this is the length of fuel with significant visible
damage; (iv) the flames remain anchored at the base of the sample, which has
a very slow regression rate (0.01 to 0.04 mm/s).

### Measured outcomes — Saffire-1 / Saffire-2 (narrative)

| Field | Value | Report section |
| --- | --- | --- |
| Saffire-1 average flame spread rate | 1.8 mm/s (concurrent-flow), 1.3 mm/s (opposed-flow) | SIBAL Fabric Results |
| Saffire-1 average flame power | 1200 ± 300 W | Configurations |
| Saffire-1 total burn time | 420 s | SIBAL Fabric Results |
| Saffire-2 SIBAL fabric spread rate | 2.1 mm/s (20 cm/s flow) to 2.6 mm/s (25 cm/s flow, Table I) | SIBAL Fabric Results, Table I |
| Saffire-2 flame power, SIBAL fabric | 200 ± 50 W | Configurations |
| Saffire-2 flame power, thick PMMA | 600 ± 100 W | Configurations |
| Saffire-2 silicone result | none of the silicone samples burned in microgravity, though two of the three upward-burning thicknesses burned readily in normal gravity | Silicone Results |
| Saffire-2 PMMA/Nomex composite | PMMA portion fully consumed (flame power 460 ± 50 W, ~2 min); Nomex fabric did not ignite despite the heating load | Composite PMMA-Nomex® Results |

## Conclusions

**Saffire VI (primary):** practical-scale fires ranging from 1.5 to 3.2 kW
were tested in unmanned spacecraft with free air volumes of 17 to 19 cubic
meters; ambient CO₂ and CO concentrations rose significantly, with the PMMA
tests exceeding the 1-hour CO₂ limit and the 24-hour CO limit. Collectively,
these results demonstrate that human hazard from a spacecraft fire is
similar to terrestrial fires in one respect: heat from the fire is not the
principal hazard, and smoke/gaseous products are a much greater
concern. Further work will be needed to extend these
results to the partial-gravity environment expected on future Moon and Mars
missions.[^saffire-vi-ices-2024]

**Saffire-1 / Saffire-2 (background):** unlike in normal gravity, a steady
flame was achieved even for a wide sample burning in concurrent flow, though
flames spread more slowly than in prior tests using smaller ducts. Silicone
flammability in microgravity appeared reduced compared to normal gravity for
the flow speeds tested, and Nomex — rated "safe" on Earth — could not be
ignited even under a sustained pilot flame.[^saffire-results-2017]

## Open questions

- The primary source (Saffire VI) presents results for only one test each of
  a limited sample set; it explicitly states these are *preliminary* results
  from *one test* of the final flight, not the complete Saffire VI dataset.
- Some figures referenced in both sources' text (spread-rate plots,
  thermocouple traces, the oxygen-concentration/heat-release time series in
  Figure 5) are not machine-readable from the converted text and are not
  reproduced here beyond the tabulated summary data (Table 2).
- Saffire VI's much lower ambient pressure and higher O₂ than Saffire-1 and
  Saffire-2 means its outcomes are not directly comparable to the earlier
  flights' without accounting for that difference — flagged throughout
  rather than merged into one comparison.

[^saffire-vi-ices-2024]: Preliminary Results from the Saffire VI Experiment. Abstract: "Preliminary results are presented for one test of the last flight of the Spacecraft Fire Experiment (Saffire VI) which was conducted on an orbiting Cygnus spacecraft. These experiments directly address the risks associated with our understanding of spacecraft fire behavior at practical length scales and geometries. The lack of this experimental data has forced spacecraft designers to base their designs and safety precautions on 1-g understanding of flame spread, flame self-extinguishment, fire detection, and suppression... NASA's Spacecraft Fire Safety Demonstration Project was formulated with the goal of conducting a series of large-scale experiments in spacecraft environments that represent practical spacecraft fires. These tests spanned 1.5 to 3.2 kW with free air volumes of 17 to 19 cubic meters. The final flight in the series of six experiments examined concurrent spread over large samples (all 41 cm wide) including a thin sheet of flammable fuel (cotton/fiberglass 50 cm long); 2-sided spread over 1 cm thick polymethyl methacrylate (PMMA) (18 cm long); 1-sided spread over 0.5 cm thick (18 cm long); and Nomex fabric (7 cm long). Results are presented for the PMMA samples, the SIBAL sample, and the thin cotton samples from Saffire IV and V. The flame heat release is determined and compared to the overall temperature rise in the spacecraft and the change in the concentration of carbon dioxide and carbon monoxide in the spacecraft. Overall, the temperature and pressure rise in the spacecraft were found to be less significant than the increase in carbon dioxide and carbon monoxide." §II Experimental Hardware: "The Saffire Flow Unit (SFU) for flights IV - VI was very similar to that used for Saffire I-III... To accommodate the second set of cameras, the duct half-height was reduced from 25 cm (for Saffire I-III) to 15 cm for Saffire IV-VI (perpendicular to the sample surface) preserving the 45 cm width... the Far Field Diagnostics (FFD) containing the smoke cleanup system and smoke sensors was installed in a mid-deck locker accommodation location adjacent to the hatch." "The Saffire VI sample card contained four samples and was configured for four ignitions... The Nomex sample did not ignite and so it will not be included in this paper." "Similar to Saffire IV & V, the sample materials were: \"SIBAL\" fabric (75% cotton and 25% fiberglass) with a total area density of 18.05 mg/cm2; or flat, cast, polymethyl methacrylate (PMMA) (either one-sided 5 mm thick or two-sided (10 mm thick)." Table 1 (Saffire IV-VI Test considered in paper): Flight/Sample IV-1, V-2, VI-2, VI-3, VI-4; Material SIBAL Cloth, Cotton Jersey, SIBAL Cloth, Two-Sided PMMA, One-Sided PMMA; Length (cm) 50, 50, 50, 18, 18; Air Flow Rate (cm/s) 20 for all; Ambient Pressure (kPa) 100.0, 70.7, 54.1, 54.6, 55.2; Oxygen Concentration (mol%) 22.0, 26.2, 31.0, 30.3, 28.8; Free volume (m3) 17.9, 19.0, 16.7, 16.7, 16.7. §III Results and Their Fire Safety Implications: "The fires were generally of 1.5 to 3 kW in intensity which is a small fire by terrestrial standards." "At the same time the temperatures and gas temperature at the outlet of the SFU outlet is significant (70 °C) the temperature near the FFD (zenith) only changes slightly from the prior baseline." "Figure 5 presents the heat release calculated from the oxygen consumption using the method of Huggett where the heat release is estimated for a wide range of combustibles to be 13.1 kJ per gram of oxygen consumed... These results are tabulated in Table 2 with the thin fuel results from Saffire IV and V and all the successful ignitions from Saffire VI... For the VI-2 sample (SIBAL) both methods were used and agree within 15% which is reasonable for this type of analysis." Table 2 (Saffire flight/sample data): IV-1 SIBAL, burn duration 130 s, average heat release 3,150 W, total heat release 409 kJ, max temp at SFU outlet 45°C, max temp at FFD 25°C, FFD inlet CO2 increase 1390 ppm, CO2 partial pressure increase 1.03 mmHg, FFD inlet CO increase 80 ppm. V-2 Cotton, burn duration 200 s, average heat release 2,800 W, total heat release 560 kJ, max temp at SFU outlet 46°C, max temp at FFD 23°C, CO2 increase 2360 ppm, CO2 partial pressure increase 1.26 mmHg, CO increase 83 ppm. VI-2 SIBAL, burn duration 112 s, peak heat release 3217 W, total heat release (imaging) 580 kJ, average heat release (O2 consumption) 3,650 W, total heat release (O2 consumption) 409 kJ, max temp at SFU outlet 48°C, max temp at FFD 20°C, CO2 increase 2800 ppm, CO2 partial pressure increase 1.15 mmHg, CO increase 120 ppm. VI-3 2-sided PMMA, burn duration 780 s, peak heat release 3080 W, total heat release (imaging) 1280 kJ, max temp at SFU outlet 77°C, max temp at FFD 21°C, CO2 increase 8539 ppm, CO2 partial pressure increase 3.51 mmHg, CO increase 308 ppm. VI-4 1-sided PMMA, burn duration 1200 s, peak heat release 1507 W, total heat release (imaging) 830 kJ, max temp at SFU outlet 57°C, max temp at FFD 21°C, CO2 increase 8117 ppm, CO2 partial pressure increase 3.37 mmHg, CO increase 320 ppm. "Figure 7 presents the smoke concentrations at the FFD and the response of a terrestrial ionization detector. The smoke levels can be seen to rise rapidly and subsequently decrease, presumably due to particle loss from impaction on multiple surfaces. Selecting 1 mg/m3 as a relatively tight alarm threshold, the FFD detector reached that threshold at 981 seconds. By this point, much of the hazardous gas release had occurred... For carbon monoxide, NASA establishes a Spacecraft Maximum Allowed Concentration (SMAC) value based on the exposure duration. For carbon monoxide, the 1-hour SMAC is 425 ppm, and the 24-hour SMAC is 100 ppm. For carbon dioxide, which is prevalent in manned spacecraft, the limits are established differently in NASA-STD-3001 which limits the 1-hour average CO2 partial pressure to no more than 3 mm Hg. As can be seen in Table 2, the allowable CO2 level was exceeded by both of the PMMA tests on Saffire VI. For carbon monoxide the levels were well above the 24-hour SMAC and quite close to the 1-hour level." "Figure 5. Inlet and outlet oxygen concentrations for Saffire VI-3 (two-sided PMMA) with the calculated heat release based on the oxygen consumption. The flow was changed from 20 cm/s to 5 cm/s at 1120 s and terminated at 1420 s." "Figure 6. CO and CO2 concentrations for Saffire VI-3 (two-sided PMMA). The duct flow terminated at 1420 s so the outlet traces end. The flow was changed from 20 cm/s to 5 cm/s at 1120 s. At this lower flow rate, the outlet CO2 and CO levels increased due to the lower ambient flow." §IV Conclusion: "Practical scale fires ranging from 1.5 to 3.2 kW were tested in unmanned spacecraft with free air volumes of 17 to 19 cubic meters... the ambient concentrations of carbon monoxide and carbon dioxide rose significantly with the PMMA tests exceeding the 1-hour carbon dioxide limit and the 24-hour carbon monoxide limit. The smoke from the fire event was readily detected by an ionization detector and a light scattering system but a typical alarm threshold was only achieved at 981 seconds. By this time most of the hazardous gas release had occurred... Collectively these results demonstrate that the human hazard from a fire in a spacecraft is very similar to terrestrial fires where the heat from the fire is not the principal hazard and rather the smoke and gaseous products are a much greater concern... Further work will be needed to extend these results to the partial gravity environment expected on future mission to the moon and Mars."
[^saffire-results-2017]: Results of Large-Scale Spacecraft Flammability Tests. Introduction/Experiment: "The Saffire experiments investigated intentionally-set, large-scale fires inside a spacecraft. For safety, they were conducted in unoccupied resupply vehicles for the International Space Station (ISS)... Although large-scale fire tests on Earth are common, they had never been attempted in a space experiment for obvious reasons of practicality and safety." "The vehicles launched to the ISS with Saffire stowed onboard. Saffire stayed in the resupply vehicle and remained dormant while the vehicle was berthed with the ISS and its supplies were unloaded... Once the vehicle departed ISS, the Saffire tests were completed and all data was relayed to Earth. Finally, the vehicle was guided for destructive re-entry into the Earth's atmosphere." Saffire Objectives: "Saffire 1: Assess flame spread of large-scale microgravity fire (spread rate, mass consumption, heat release) / Verify oxygen flammability limits in low gravity... Data obtained from the experiment will be used to validate modeling of spacecraft fire response scenarios / Evaluate NASA's normal-gravity material flammability screening test for low-gravity conditions." Experiment (figure caption): "The Saffire flow duct (18\" x 20\")." Saffire-I Description: "Fuel characteristics (\"SIBAL\" fabric) — 75% cotton, 25% fiberglass blend — Simple weave pattern (60 x 40 threads per inch) — Overall area density: 18 mg/cm2 — Fuel sizes (W x L): 40.6 x 94 cm and 5 x 29 cm." "Large sample (40.6 cm x 94 cm) / Flow speed of 20 cm/s / Initial oxygen concentration 21.7% (ISS reading)." Saffire-2 Description: "Nine samples; 5 cm wide by 29 cm long / 20 cm/s flow for all tests except for Sample 2-6 (25 cm/s) / All upward burns except Sample 2-4 was downward / Initial oxygen concentration 22.1% (ISS reading, slightly higher than Saffire-1's 21.7%)." "Samples 2-1 to 2-4 were silicone sheets 0.27, 0.61, 1.03, and 0.37 mm thick. Samples 2-5 and 2-6 were cotton-fiberglass fabric identical to that used in Saffire-1. Sample 2-7 had a composite construction, the first 5 cm of which was a thin (0.8 mm) sheet of PMMA and the remainder Nomex® fabric (HT90-40). Samples 2-8* and 2-9* were PMMA slabs with a nominal thickness of 1 cm." SIBAL Fabric Results (Saffire 1 video caption): "Average flame spread rate is 1.8 mm/s; estimated average flame power is 1200 +/- 300 W. Total burn time is 420 s." SIBAL Fabric Results (con't): "The average concurrent-flow flame spread rate is 1.8 mm/s. The opposed-flow flame average spread rate 1.3 mm/s. The flame spread rate for the 5-cm-wide sample is marginally faster compared to the spread rate for the 40.6-cm-wide sample for the same flow speed of 20 cm/s (2.1 compared to 1.8 mm/s)." (The 2.6 mm/s figure for the 25 cm/s flow condition, Sample 2-6, is reported in Table I of the same source.) Configurations: "Average flame power: Saffire 1: 1200 +/- 300 W / Saffire 2: (SIBAL fabric) 200 +/- 50 W / Saffire 2: (Thick PMMA) 600 +/- 100 W." Silicone Results: "Results were convincing although rather anticlimactic as none of the silicone samples burned... It was surprising that not even the thin sample could permit any flame spread, given that it was entirely consumed in normal gravity." Composite PMMA-Nomex® Results: "It took about two minutes for the PMMA to be consumed... The average flame power from the PMMA (assuming complete conversion of the fuel) was 460 + 50 W. Despite this significant heating load, the fabric was not ignited." Summary and Conclusions: "Unlike 1-g, the results revealed that a steady flame could be achieved even for a wide sample burning in concurrent-flow. The flames spread more slowly than prior tests in smaller ducts... Flammability of silicone in microgravity appears to be reduced compared to normal gravity, at least for the flow speeds tested. Nomex®, a common material used on the ISS and rated \"safe,\" could not be ignited even when bathed by a pilot flame."
