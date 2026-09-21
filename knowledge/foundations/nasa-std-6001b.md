---
type: Standard
title: "NASA-STD-6001B: Flammability, Offgassing, and Compatibility Requirements and Test Procedures"
description: The NASA technical standard governing materials evaluation, testing, and selection for flammability, offgassing, and fluid compatibility in space vehicles, including all core test procedures (Tests 1 through 18) and their pass/fail criteria.
status: stable
generated: { by: "claude-code/sonnet-5", at: 2026-09-21T19:56:58Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-21T19:56:58Z }
order: 13
sources:
  - id: nasa-std-6001b
    title: "NASA-STD-6001B w/Change 3: Flammability, Offgassing, and Compatibility Requirements and Test Procedures"
    resource: "https://standards.nasa.gov/standard/NASA/NASA-STD-6001"
verified:
  - by: human:you
    at: 2026-09-21T19:56:58Z
---

NASA-STD-6001B establishes NASA program requirements for evaluating, testing,
and selecting materials to preclude unsafe conditions related to
flammability, offgassing, and fluid compatibility.[^nasa-std-6001b] It is the
certification standard the investigation reports in this corpus repeatedly
reference — a material passing this standard's tests is treated as safe for
spacecraft use, which is the exact assumption BASS-II and SAFFIRE were
designed to test against actual microgravity behavior. This entry covers the
standard's full requirements structure — §4 (Evaluation and Testing),
§5 (Applicable Material Tests), §6 (System Evaluations), and §7 (all 18 Test
Methods) — not just Scope/Applicability/Tailoring.

## Scope and applicability

Materials intended for use in space vehicles, specified test facilities, and
contractually specified Ground Support Equipment (GSE) must meet this
standard's requirements; responsible NASA Centers' materials and processes
organizations must include its applicable requirements in their materials
control programs. The standard may also apply to the Jet Propulsion
Laboratory and other contractors to the extent specified in applicable
contracts.

The standard contains 425 numbered, verifiable requirement statements
(indicated by "shall"), with explanatory/guidance text set in italics from
Section 4 onward, and a Requirements Compliance Matrix in an appendix to
support selection and verification by NASA programs and projects.[^nasa-std-6001b]

## §4 Evaluation and Testing of Materials

| FOCR | Requirement | Section |
| --- | --- | --- |
| 7 | Materials in habitable areas of spacecraft (including stowed equipment and experiments) shall be evaluated for flammability and offgassing | §4.1 |
| 8 | All materials located in other (non-habitable) areas shall be evaluated for flammability | §4.1 |
| 9 | Materials exposed to LOX, GOX, and other reactive fluids shall be evaluated for compatibility with the fluid in their use application | §4.1 |
| 10 | Materials exposed to pressurized breathing gases shall also be evaluated for offgassing | §4.1 |
| 11 | Electrical insulation materials shall also be evaluated for arc tracking | §4.1 |
| 12 | Evaluation shall use the worst-case anticipated use environment (most hazardous pressure, temperature, material thickness, and fluid exposure) | §4.1 |
| 13 | Systems with materials that have not been tested, or that don't meet the required-test criteria, shall be verified acceptable by analysis or configurational testing via a Materials Usage Agreement (MUA) | §4.2 |
| 14 | An MUA shall be prepared per the MUA system in NASA-STD-6016 (flight hardware) or NASA-STD-5005 (GSE) | §4.2 |
| 15 | The MUA shall document the acceptance rationale | §4.2 |
| 16 | The MUA shall be submitted for approval per NASA-STD-6016, in accordance with the Program/Project Materials and Processes Selection, Control, and Implementation Plan | §4.2 |

Existing test data are compiled in NASA Marshall Space Flight Center's
Materials and Processes Technical Information System (MAPTIS).[^nasa-std-6001b]

## §5 Applicable Material Tests

Which test a material needs depends on its exposure environment: habitable
environments, LOX/GOX systems, breathing gases, or reactive fluids.[^nasa-std-6001b]

| FOCR | Requirement | Section |
| --- | --- | --- |
| 17 | Required tests shall be conducted on materials in worst-case exposure conditions and representative use thicknesses/product forms | §5 |
| 18 | To be accepted for unrestricted use, materials shall pass the required tests | §5 |
| 21 | Materials failing the required tests, if still candidates for use, shall be verified acceptable via analysis or test and approved through the MUA process | §5 |
| 22 | The responsible NASA program/project M&P organization shall determine when batch/lot testing is required | §5 |

**Table 1 — Required tests by environment**

| Environment | Required tests |
| --- | --- |
| Habitable Flight Compartments | Test 1 (Upward Flame Propagation), Test 4 (Electrical Wire Insulation Flammability), Test 7 (Determination of Offgassed Products), Test 18 (Arc Tracking) |
| Other Areas | Test 1, Test 4, Test 18 |
| LOX and GOX Environments | Test 1, Test 17 (Upward Flammability of Materials in GOX) |
| Breathing Gases | Test 1, Test 7 |
| Reactive Fluids | Test 15 (Reactivity of Materials in Hydrazine/MMH/UDMH/Aerozine 50/Nitrogen Tetroxide/Ammonia) |

**Table 2 — Supplemental tests by environment** (used to support system-level hazard evaluation, not required by default): Habitable Flight Compartments → Test 2 (Heat and Visible Smoke Release Rates), Test 3 (Flash Point of Liquids), Test 6 (Odor Assessment), Test 10 (Configurational Flammability), Electrical Arc (Appendix A.2.11); Other Areas → Test 2, Test 3; LOX/GOX Environments → Test 13A/13B (Mechanical Impact), ASTM G74 (Gaseous Fluid Impact), ASTM G72 (Autogenous Ignition), ASTM D240/D4809 (Heat of Combustion), ASTM G125 (Oxygen Index), Electrical Arc, Frictional and Particle Impact; Breathing Gases → Test 6; Reactive Fluids → Reactivity/Penetration testing (Appendix A.2.7), Test 3.

## §6 System Evaluations

| FOCR | Requirement | Section |
| --- | --- | --- |
| 23 | System evaluations shall demonstrate the acceptability of configurations resulting from flammable, incompatible, or offgassing materials | §6 |
| 24 | System evaluations shall address single-barrier failures that can expose materials to reactive fluids | §6 |
| 25 | A system flammability evaluation shall be conducted if materials failing Test 1 are proposed for use | §6.1 |
| 26 | If using the analytical approach, fire-control guidelines (fuel arrangement/isolation, ignition-source control, crew-habitable-module effects, pressure/temperature rise limits) shall be addressed and documented | §6.1 |
| 27 | If using the test approach, materials failing Test 1 shall be evaluated by a configuration test such as Test 10, covering worst-case failure modes and operating conditions | §6.1 |
| 28 | If evaluation results are inconclusive and a major assembly flammability test is required, a test plan shall be submitted for approval before testing | §6.1 |
| 29 | Materials/components/systems used in LOX and GOX environments shall be evaluated per the Figure 1 approach (pre-selection → flammability assessment → OCA) | §6.3 |
| 30 | If materials are determined flammable, an Oxygen Compatibility Assessment (OCA) shall be performed per NASA/TM-2007-213740 | §6.3 |
| 31 | The need for an OCA shall be addressed for compressed-air systems and pressurized systems with enriched oxygen (>21% O₂ by volume) | §6.3.3 |
| 32 | If an OCA is determined not required, concurrence shall be obtained from the responsible program/project M&P organization | §6.3.3 |
| 33 | Previously untested polymeric materials failing Test 1 or Test 17 shall, at minimum, undergo autogenous ignition temperature and heat-of-combustion testing | §6.3 |
| 34 | Data used to assess material flammability shall be applicable to the specific environment and part/component configuration | §6.3 |
| 35 | If flammability or configuration is unknown, the material shall be considered flammable | §6.3 |
| 36 | The responsible M&P organization shall approve that flammability-assessment data applies to the specific design configuration | §6.3 |
| 37 | OCA results shall be documented and submitted for M&P concurrence | §6.3 |
| 38 | An MUA, if applicable, shall be used to submit OCA results | §6.3 |
| 39 | The hardware developer shall verify OCA-assessed materials reflect the as-built design | §6.3 |
| 40 | A system evaluation shall be conducted for all systems containing reactive fluids | §6.4 |
| 41 | Materials used in system construction shall be evaluated for compatibility with the exposure fluid and its decomposition products | §6.4 |
| 42 | Evaluations shall be supported by analysis, Test 15 data, and (when necessary) configuration-specific testing | §6.4 |
| 43 | The analytical approach shall examine possible uncontrolled exothermic-reaction sources, develop controls, and document results | §6.4 |
| 44 | The rationale for using materials that fail Test 15 criteria shall be documented and submitted for M&P approval | §6.4 |

As pressure increases, materials such as metals, polymers, lubricants, and
contaminants become flammable in 100 percent oxygen — and almost all
polymers are flammable in 100 percent oxygen at atmospheric pressure;
flammability also depends heavily on configuration (thin-walled tubing or
finely divided forms like wire mesh are more flammable than bulk
material).[^nasa-std-6001b]

## §7 Test Methods — general requirements

| FOCR | Requirement | Section |
| --- | --- | --- |
| 45 | Tests shall be performed by test facilities certified per Appendix B | §7 |
| 46 | The test facility shall demonstrate good laboratory practices for accurate, repeatable data | §7 |
| 47 | Good laboratory practices shall include calibration and maintenance procedures | §7 |
| 48 | Test facilities shall demonstrate testing proficiency at least every 2 years to maintain certification | §7 |
| 49 | Properly identified test material shall be provided with a test request form (Appendix D format) | §7 |
| 50 | Materials shall be accompanied by Material Safety Data Sheets (MSDSs) per OSHA requirements | §7 |
| 51 | Material specimens shall be visually inspected and any flaws/contamination noted in the test report | §7 |
| 52 | Specimens shall be prepared in the proper dimensions | §7 |
| 53 | Specimens shall be weighed and identified individually | §7 |
| 54 | Specimens shall be cleaned to end-use specifications | §7 |
| 55 | Specimens shall be inspected after preparation for suitability to the specific test | §7 |
| 56 | All testing fluids shall meet or exceed user specifications, at minimum | §7 |
| 57 | Any deviation from standard test parameters shall be identified and results annotated as nonstandard | §7 |
| 58 | Test methods/quantities for material forms not listed in Table 3 shall be reviewed and approved by the responsible M&P organization | §7 |

**Table 3 (excerpt) — minimum material quantities per test**[^nasa-std-6001b]: solids for Test 1 need 6 specimens at 30×6.4 cm by required thickness; Test 7 needs 4000 cm² total area or 40 g; Test 15 needs 50 cm² or 20 g; Test 17 needs 15 specimens of 10.2 cm (min.) × 0.32 cm diameter rods; insulated wire for Test 1 needs 2 m length, for Test 4 needs 10 m, for Test 18 needs 70 m.

## Test 1 — Upward Flame Propagation

**Purpose:** determine whether a material, exposed to a standard ignition
source, self-extinguishes without transferring burning debris that could
ignite adjacent materials.

| FOCR | Requirement |
| --- | --- |
| 59 | Test 1 shall evaluate the material in the worst-case atmosphere it could be exposed to |
| 60 | Five specimens, 30 cm × 6.5 cm (12 × 2.5 in), tested one at a time, mounted vertically |
| 61 | Specimens ignited at the bottom, burned until each self-extinguishes |
| 62 | Burn length (linear distance consumed) measured and recorded |
| 63 | Whether ignition of the paper below occurred via burning-debris transfer shall be recorded |
| 64 | **Pass criteria**: no specimen burns >15 cm (6 in), AND no specimen propagates flame via burning-debris transfer |
| 65 | Test method follows ISO 14624-1:2003 with NASA-specific exceptions/additions |

Test atmosphere is a GOX/GN2 mixture at the highest O₂ level the material
could see in use; ambient conditions are defined as 20.9% O₂, 101.4 kPa
(14.7 psia), 23±5°C (73±9°F). Failure of any one specimen fails the material
in that environment.[^nasa-std-6001b]

## Test 4 — Electrical Wire Insulation Flammability

**Purpose:** determine whether wire insulation, exposed to a standard
ignition source, self-extinguishes without transferring burning
debris.[^nasa-std-6001b]

| FOCR | Requirement |
| --- | --- |
| 66 | Test shall evaluate the wire in the worst-case atmosphere anticipated |
| 67 | Five specimens, 1.2 m (48 in) wire with 30 cm (12 in) active area, mounted at 15° from vertical |
| 68 | Specimens ignited at the bottom, burned until self-extinguished |
| 69 | Burn length measured and recorded |
| 70 | Burning-debris ignition of the paper below recorded |
| 71 | **Pass criteria**: no specimen burns >15 cm (6 in), AND no burning-debris flame propagation (identical numeric threshold to Test 1) |
| 72 | Test method follows ISO 14624-2:2003 with NASA-specific exceptions/additions; Test B (gas-flow variant) is explicitly excluded |

## Test 7 — Determination of Offgassed Products

**Purpose:** identify and quantify volatile offgassed products from
materials and assembled articles.

| FOCR | Requirement |
| --- | --- |
| 73 | Test 7 shall determine offgassing characteristics under standardized conditions for habitable-environment materials/articles |
| 74 | Specimens placed in certified-clean sealed containers, thermally conditioned 72±1 hr at 50±3°C (122±5°F) |
| 75 | After conditioning, container atmosphere analyzed for offgassed compounds |
| 76 | Overall toxicity rating determined using the Spacecraft Maximum Allowable Concentration (SMAC) for each compound |
| 77 | The overall rating determines the quantity of material/number of articles that may fly concurrently |
| 78 | **Pass criteria**: total Toxic Hazard Index (T) for all volatile offgassed products < 0.5 |
| 79 through 85 | T-value accounting rules for assembled articles vs. materials-basis evaluation, multiple flight units, and bulk materials via MAPTIS ratings — all converge on the same T < 0.5 threshold |
| 86 | Test method follows ISO 14624-3:2005 with NASA-specific exceptions/additions |

T-value calculations use the habitable free volume of the spacecraft: Space
Shuttle Orbiter = 65 m³ (2300 ft³); ISS = 118 m³ (4170 ft³, the US
Laboratory/Destiny module volume); the Multipurpose Crew Vehicle Orion
vehicle = 15 m³ (530 ft³). SMAC values are reported in mg/m³, using 7-day
SMACs by default. MAPTIS weight-class ratings: K = 45 kg
(100 lb) or greater; H = 22.5 to 45 kg; A = 4.5 to 22.5 kg; V = 2.3 to 4.5 kg;
X = 0 to 2.3 kg. For
assemblies: A = T≤0.5, X = T>0.5.[^nasa-std-6001b]

## Test 15 — Reactivity of Materials in Hydrazine, MMH, UDMH, Aerozine 50, Nitrogen Tetroxide, and Ammonia

**Purpose:** a short-term exposure test identifying material/fluid
degradation or reactions that would raise pressure in a closed
system — a 2-hour screening test followed by a 48-hour immersion
test.

| FOCR | Requirement |
| --- | --- |
| 87 | Appropriate long-term tests shall be conducted for materials with long-term exposure to fuels/oxidizers/hazardous fluids |
| 88 | Screening test standard conditions: test facility ambient temperature and pressure |
| 89 | If used above test temperature, additional testing at max use temperature required |
| 90 | Immersion test (hydrazine, MMH, UDMH, Aerozine 50, N₂O₄/MON): 71±3°C (160±5°F) and the fluid's vapor pressure at that temperature |
| 91 | Immersion test (ammonia): 30±3°C (86±5°F) and the fluid's vapor pressure at that temperature |
| 92 through 97 | Test fluids shall meet MIL-PRF-26536 (hydrazine), MIL-PRF-27404 (MMH), MIL-PRF-25604 (UDMH), MIL-PRF-27402 (Aerozine 50), MIL-PRF-26539 (N₂O₄/MON-3); ammonia ≥99.99% purity (liquid phase) |
| 98 through 111 | Specimen preparation by material type: solids/foams cut to 4×1×0.15 cm (~25±5 cm² total area); greases/liquids on tared 304L stainless steel substrates (tare accuracy 1.0×10⁻⁴ g); wire insulation stripped to 25±5 cm²; inks/adhesives/coatings applied at end-use thickness (default 0.013 cm if unspecified); heat-shrink tubing pre-shrunk per manufacturer instructions; pressure-sensitive tapes and O-rings/irregular items sized to 25±5 cm² |
| 156 | **Failure criteria** (either test): burning/charring/fire; frothing; dissolution; crumbling/friability/particulate generation; >20% shape/dimension change; >20% degradation of selected physical properties; visible test-fluid appearance change; for N₂O₄, pressure rise >68.9 kPa (>10 psi); for polymers in N₂O₄, evidence of nitration (DSC/FTIR) |
| 157 | Quality control: pressure rise on the system reference side shall be <0.4 kPa (<0.06 psia)/hr for N₂O₄ and ammonia |
| 158 | Quality control: hydrazine-family gas evolution rate shall be <7.0×10⁻³ standard cm³/(cm²·hr) |

Screening test uses ≤0.25 g material with fluid added dropwise to screen for
gross reactivity; immersion test fully covers the specimen in a sealed,
pressure-monitored container for the test duration.[^nasa-std-6001b]

## Test 17 — Upward Flammability of Materials in GOX

**Purpose:** determine material flammability at use pressure in GOX, at
ambient or elevated temperature.[^nasa-std-6001b]

| FOCR | Requirement |
| --- | --- |
| 159 | Test 17 shall determine flammability at use pressure in GOX, ambient/elevated temp |
| 160 | Specimens: 0.32 cm (0.126 in) diameter rods, minimum 10.2 cm (4 in) length |
| 161 | Specimens mounted vertically, ignited at bottom, burned to self-extinguishment |
| 162 | Burn length (consumed length) measured |
| 163 and 164 | To find a non-flammable pressure: ≥10 specimens tested without any exceeding 3 cm (1.2 in) consumption |
| — | **Pass/fail criteria**: material is flammable at the max use pressure if ≥1 specimen burns >3 cm (1.2 in) |
| 165 | Test valid only if the ignition promoter ignites, burns, and detaches from the specimen |
| 166 | Test method follows ASTM G124 with NASA-specific exceptions; metallic-material promoter must release ≥3.0 kJ (717 cal) |

## Test 18 — Arc Tracking (Dry Arc Propagation Resistance)

**Purpose:** assess an insulation's ability to prevent damage in an
electrical arc environment, and to resist further arc propagation if
re-energized.[^nasa-std-6001b]

| FOCR | Requirement |
| --- | --- |
| 167 | At least 15 seven-wire bundles shall be tested to determine arc propagation resistance |
| 168 through 171 | **Pass criteria** (all required): at least 64 of the tested wires pass the dielectric test; no more than 3 wires fail the dielectric test in any one bundle; actual arc damage does not exceed 7.6 cm (3 in) in any one bundle |
| 172 | Test conditions per MIL-STD-2223 Method 3007 or SAE AS4373 Method 508 |
| 173 and 174 | Specimen: bundle of 7 wires, ≥35.6 cm (14 in) length; 15 bundles required for a full test (20 AWG recommended) |
| 175 through 178 | Specimen prep, test system, and pre-test/test procedures all follow MIL-STD-2223 Method 3007 or SAE AS4373 Method 508 |
| 179 | Test report shall include specimen ID, test conditions, total wires passing dielectric test, per-bundle pass counts, and per-wire damage length |

## Tests removed from the core requirement set

Several test numbers from earlier revisions are now either deleted outright
or demoted to supplemental status (Appendix A), and are not part of the
required Table 1 test set:[^nasa-std-6001b]

| Test | Status |
| --- | --- |
| Test 2 (Heat and Visible Smoke Release Rates) | Supplemental — Appendix A.2.1 |
| Test 3 (Flash Point of Liquids) | Supplemental — Appendix A.2.2 |
| Test 5 (Electrical Connector Potting/Conformal Coating Flammability) | Deleted in a previous version |
| Test 6 (Odor Assessment) | Supplemental — Appendix A.3 |
| Test 8 (Flammability Test for Materials in Vented or Sealed Containers) | Deleted |
| Test 9 (Electrical Overload for Sealed Containers) | Deleted in a previous version |
| Test 10 (Configurational Flammability, formerly Simulated Panel/Major Assembly Flammability) | Supplemental — Appendix A.2.4 |
| Test 11 (Simulated Crew Bay Configuration Flammability Verification) | Deleted in a previous version |
| Test 12 (Total Spacecraft Offgassing) | Deleted |
| Test 13A/13B (Mechanical Impact, ambient/variable-pressure LOX/GOX) | Supplemental — Appendix A.2.5 |
| Test 14 (Pressurized GOX Pneumatic Impact for Nonmetals) | Deleted (similar component-level test in Appendix A.2.6) |
| Test 16 (Determination of Offgassed Products from Assembled Article) | Deleted in a previous version |

## Tailoring

Tailoring this standard for a specific program or project must be formally
documented as part of program/project requirements and approved by the
responsible Technical Authority, per NPR 7120.5 (NASA Space Flight Program and
Project Management Requirements).[^nasa-std-6001b]

## Open questions

- **Appendices A through E are not covered here.** Appendix A holds the full
  procedures for every supplemental test (A.2.1 through at least A.2.13);
  Appendix B covers test-facility certification (FOCR 399 through 421); Appendix C is
  reference documents; Appendix D covers specimen submission and the test
  request form (FOCR 422+); Appendix E is the Requirements Compliance Matrix.
  These are a comparable volume of additional requirements to everything
  extracted above, and were out of scope for this pass.
- The granular ISO/ASTM-standard exceptions, clarifications, and additions
  within each test's "Test Method" subsection (equipment specifics, timing
  windows, material specs for igniters/paper/substrates) are summarized at
  the level needed for pass/fail comparison, not transcribed clause-by-clause
  — the source itself defers to the underlying ISO/ASTM/MIL-STD documents for
  full procedural detail.
- The current revalidation date on the document header is 2025-6-9 (w/Change
  3); this entry does not track whether a newer revision supersedes it.

[^nasa-std-6001b]: NASA-STD-6001B w/Change 3. §1.1 Purpose: "The purpose of this NASA Technical Standard is to establish National Aeronautics and Space Administration (NASA) program requirements for evaluation, testing, and selection of materials to preclude unsafe conditions related to flammability, offgassing, and fluid compatibility." §1.2 Applicability: "[FOCR 1] Materials intended for use in space vehicles, specified test facilities, and contractually specified Ground Support Equipment (GSE) shall meet the requirements of this NASA Technical Standard. [FOCR 2] Responsible NASA Centers' materials and processes (M&P) organizations shall include applicable requirements of this NASA Technical Standard in their materials control programs... It may also apply to the Jet Propulsion Laboratory and other contractors only to the extent specified or referenced in applicable contracts." "Verifiable requirement statements are numbered and indicated by the word \"shall\"; this NASA Technical Standard contains 425 requirements." §1.3 Tailoring: "[FOCR 3] Tailoring of this NASA Technical Standard for application to a specific program or project shall be formally documented as part of program or project requirements and approved by the responsible Technical Authority in accordance with NPR 7120.5, NASA Space Flight Program and Project Management Requirements." §4.1 and §4.2: material evaluation and MUA requirements FOCR 7 through 16, e.g. "Materials located in habitable areas of spacecraft, including the materials of the spacecraft, stowed equipment, and experiments, shall be evaluated for flammability and offgassing" and "The worst-case anticipated use environment (most hazardous pressure, temperature, material thickness, and fluid exposure conditions) shall be used in the evaluation of material suitability." §5: "The applicable material test depends on the environment to which the material is exposed... Table 1, Required Tests for Each Material Use, lists the required tests for each material use," with Table 1 mapping Habitable Flight Compartments to Tests 1, 4, 7, and 18, Other Areas to Tests 1, 4, and 18, LOX and GOX Environments to Tests 1 and 17, Breathing Gases to Tests 1 and 7, and Reactive Fluids to Test 15; Table 2 lists supplemental tests per environment. §6: "System evaluations shall demonstrate the acceptability of configurations resulting from the use of flammable, incompatible, or offgassing materials," plus the LOX/GOX selection approach (Figure 1), the OCA process per NASA/TM-2007-213740, and reactive-fluid system evaluation requirements (FOCR 23 through 44). "As pressure increases, materials such as metals, polymers, lubricants, and contaminants become flammable in 100 percent oxygen. In addition, almost all polymers are flammable in 100 percent oxygen at atmospheric pressure." §7 (general): "Tests shall be performed by test facilities certified in accordance with Appendix B," plus specimen handling/identification/quantity requirements (FOCR 45 through 58) and Table 3's minimum material quantities per test. §7.1 Test 1: "The purpose of this test is to determine if a material, when exposed to a standard ignition source, will self-extinguish and not transfer burning debris, which can ignite adjacent materials." "The material shall meet the test acceptance criteria and be considered self-extinguishing if both of the following conditions are met: No test specimen of the five standard-sized specimens burns >15 cm (6 in). No test specimen propagates a flame by the transfer of burning debris." "The term \"ambient conditions\" refers to an oxygen concentration of 20.9 percent, a pressure of 101.4 kPa (14.7 psia), and a temperature of 23 (±5) °C (73 (±9) °F)." §7.4 Test 4: "The purpose of this test is to determine whether an electrical wire insulation material, when exposed to a standard ignition source, will self-extinguish and not transfer burning debris." "No test specimen of the five tested burns >15 cm (6 in)." §7.7 Test 7: "The purpose of this test is to determine the identity and quantity of volatile offgassed products from materials and assembled articles." "Specimens shall be placed into certified-clean sealed containers and thermally conditioned for 72 (±1) hr at 50 (±3) °C (122 (±5) °F)." "For a material or assembled article, the total Toxic Hazard Index (T) values for all volatile offgassed products shall be less than 0.5." "For the Space Shuttle Orbiter, this volume is 65 m3 (2300 ft3); for the International Space Station (ISS)... the volume used in T value calculation is set at 118 m3 (4170 ft3), which is the volume of the US Laboratory (Destiny) Module; and for the Multipurpose Crew Vehicle Orion vehicle, this volume is anticipated to be 15 m3 (530 ft3)." §7.15 Test 15: "Test 15 is a short-term exposure test that identifies changes resulting from exposure to fluids that degrade either the material or the fluid or produce a reaction, which would cause the pressure in a closed system to rise... This test is comprised of a screening test lasting 2 hr, followed by an immersion test lasting 48 hr." "For hydrazine, monomethylhydrazine (MMH), unsymmetrical dimethylhydrazine (UDMH), aerozine 50, and nitrogen tetroxide and the mixed oxides of nitrogen, the standard test conditions for the immersion test shall be 71 (±3) °C (160 (±5) °F)... For ammonia, the standard test conditions for the immersion test shall be 30 (±3) °C [86 (±5) °F]." "The material shall be considered to have failed this test if any of the following occur... The material changes shape or physical dimensions by more than 20 percent. The material suffers more than 20 percent degradation of the physical properties... For nitrogen tetroxide, a pressure rise >68.9 kPa (>10 psi)." "The pressure rise on the system reference side shall be <0.4 kPa (<0.06 psia)/hr for nitrogen tetroxide and ammonia... the gas evolution rate shall be <7.0 x 10-3 standard cm3/(cm2 hr)." §7.17 Test 17: "The purpose of this test is to determine the flammability of materials at the use pressure in GOX at ambient or elevated temperatures." "A material is considered flammable at the maximum use pressure if at least one specimen burns >3 cm (>1.2 in)." "For metallic materials, the promoter shall consist of a sufficient quantity of aluminum or magnesium to release at least 3.0 kJ (717 cal)." §7.18 Test 18: "The purpose of this test is to provide an assessment of the ability of an insulation to prevent damage in an electrical arc environment. This test also evaluates the ability of the insulation to prevent further arc propagation when the electrical arc is re-energized." "At least 64 wires shall pass the dielectric test... Three wires or less shall fail the dielectric test in any one bundle... Actual damage to the wire shall not be more than 7.6 cm (3 in) in any one bundle." Test status notes throughout §7.2 through §7.16: "Test 2 is now a supplemental test," "Deleted in previous version" (Tests 5, 9, 11), "Deleted" (Tests 8, 12, 14, 16), "Tests 13A and 13B are now supplemental tests."
