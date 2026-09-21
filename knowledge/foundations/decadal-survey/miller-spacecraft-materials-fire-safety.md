---
type: Document
title: "Spacecraft Materials Fire Safety"
description: Decadal Survey topical white paper by Fletcher Miller et al. on how NASA's ground-based flammability certification may not be conservative for microgravity and partial-gravity conditions.
status: stable
generated: { by: "claude-code/sonnet-5", at: 2026-09-21T19:56:58Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-21T19:56:58Z }
order: 11
sources:
  - id: miller-decadal-2023
    title: "Topical: Spacecraft Materials Fire Safety"
    resource: "https://science.nasa.gov/wp-content/uploads/2023/05/217_5dda37a2b088281953e769f275061ac8_MillerFletcherJ.pdf"
verified:
  - by: human:you
    at: 2026-09-21T19:56:58Z
---

This topical white paper, by Fletcher Miller (San Diego State University) and
coauthors including NASA Glenn's Sandra Olson and Michael Johnston, examines
whether NASA's ground-based flammability certification is actually
conservative once real microgravity and partial-gravity data are
available.[^miller-decadal-2023]

## The certification assumption this corpus tests

Materials are flight-qualified by passing NASA-STD-6001B Test #1 — an
ignition and upward flame-spread test in normal Earth gravity at the worst
end-use ambient oxygen concentration and pressure — historically assumed
conservative because Earth's buoyancy drives fast upward flame
spread. The paper states plainly that this assumption does not
always hold: "over the last decade, materials flammability testing in actual
low gravity and partial gravity conditions has shown that this is sometimes
not the case, at least for materials preferred by fire researchers, which
notably are often different than the actual materials used in
spacecraft." Flammable materials can also be granted waivers
from the normal control process out of necessity or crew comfort — clothing,
cotton towels, Delrin camera mounts, paper notebooks.[^miller-decadal-2023]

## What BASS/BASS-II and SAFFIRE showed

The BASS/BASS-II facility produced 70 conference and journal articles on
microgravity solid-fuel combustion, but was limited to 1 atmosphere and
oxygen concentrations below 22% by Microgravity Science Glovebox constraints
— not the conditions proposed for future exploration missions, which may
include oxygen concentrations up to 34%. Differences between
1g and 0g/partial-g flammability limits (Upward Limiting Oxygen Concentration
and Minimum Oxygen Concentration) "are largest for the Lunar g level,
indicating poor safety margins."[^miller-decadal-2023]

Larger-scale fire research began in 2016 with Saffire: launched dormant with
a Cygnus resupply vehicle, and burned only after the vehicle undocked and
departed the ISS, with data relayed to Earth before deorbit and destructive
reentry. As of this paper, five Saffire experiments had
been performed (one more awaiting launch), most increasing sample sizes by
one to two orders of magnitude over any previous test — some samples nearly a
meter long. The series found fires can keep burning for
extended periods after airflow is cut, driven by the thermal mass of thick
molten fuel; fuel vapor-bubble ruptures at the surface can generate local
flows that let a flame survive in an otherwise quiescent environment; charring
materials can smolder for extended periods and reignite when airflow resumes;
and flames can both ignite adjacent samples and extinguish downstream flames
by starving them of oxygen. Together, these mean the
ISS's standard first response — cutting ventilation — is not by itself enough
to guarantee a fire is extinguished, and more reliable mitigation is
needed.[^miller-decadal-2023]

## The Lunar-gravity flammability mechanism, and current test facilities

The paper gives a physical mechanism for why Lunar gravity is uniquely
dangerous: buoyancy at Lunar gravity may pump just the right amount of
oxidizer into the flame stabilization zone — enough to sustain burning,
without exceeding the entrainment velocity that would blow the flame
off. A centrifuge at NASA's Zero Gravity Research
Facility (ZGRF), recently revamped for solid-fuel experiments, confirmed
flammability limits depend on gravitational level and that the most flammable
upward flame-spread conditions for certain fuels sit near Lunar gravity —
though the centrifuge suffers Coriolis forces and is limited to very small
samples, motivating a proposed ZGRF upgrade for longer microgravity time and
true partial-gravity drops. Most partial-gravity work to
date has run on that centrifuge, with a few campaigns in parabolic
aircraft.[^miller-decadal-2023]

Coming work: the Solid Fuel Ignition and Extinction (SoFIE) insert for the
Combustion Integrated Rack (CIR) aboard the ISS, scheduled to launch in 2022,
supports five separate peer-reviewed NASA NRA-selected solid-fuel combustion
experiments — GEL, MIST, SMURF, RTDFS, and NCA (Narrow Channel Apparatus) —
studying idealized PMMA fuel's burning behavior and flammability limits
across geometries (in one case under an imposed heat flux), chosen because
idealized burning supports multiple test points per sample and permits
comparison to detailed numerical models. The CIR/SoFIE
facility studies solid-fuel combustion at a wider range of pressures and O₂
concentrations than MSG, extending to the 34%-oxygen exploration atmospheres
— though it cannot reach 100% O₂ (EVA suit) conditions due to hardware
limits.[^miller-decadal-2023]

## Recommendations

The paper calls for expanded research on real-world materials in more
realistic configurations (fiber mesh, exposed edges/corners, discrete fuel
configurations, parallel samples), noting that NASA's own samples have been
limited almost exclusively to small-scale, idealized-material flames — even
Saffire's larger-scale samples were still idealized fuels. It
also calls for more ground-based and flight tests with real flight materials
to determine the actual level of conservatism in NASA-STD-6001B Test
#1, continued cargo-vehicle-based large-scale fire research, and new work on
battery fires and other externally-energized flames that drive pyrolysis via
radiation and heat.[^miller-decadal-2023]

The paper's full list of needs identified for the coming decade:[^miller-decadal-2023]

1. Testing material flammability in partial gravity to support Lunar/Martian
   habitat fire safety, using facilities such as the ZGRF centrifuge (and its
   proposed upgrade), parabolic flight, an orbital/sub-orbital centrifuge, or
   a Lunar lander/habitat glovebox.
2. Testing more real-world materials (waivered and controlled borderline
   materials) in reduced gravity and exploration atmospheres (higher oxygen,
   lower pressure).
3. Continued access to long-duration microgravity for realistically thick
   materials, including flow effects (e.g. the planned Microgravity Wind
   Tunnel).
4. New materials, retardant additives, and coatings with reduced flammability
   in high-oxygen microgravity environments (e.g. safe clothing for 35%
   oxygen).
5. More testing of configurations that promote or inhibit flammability in
   microgravity, including externally-driven radiation and radiation feedback
   between surfaces.
6. Battery fire studies — batteries are rigorously screened but represent a
   high-energy-release risk, and reduced natural convection might affect
   battery life and overheating failure modes.
7. A new materials flammability standard that better represents low-gravity
   conditions.
8. Continued development of higher-throughput material screening tests (e.g.
   the Narrow Channel Apparatus) so materials can be tested faster under new
   exploration atmospheres and flow conditions closer to spacecraft reality —
   plus larger-scale flame/fire studies (ideally at actual hazard scale), a
   best-practices guidebook for low-/partial-gravity material selection, and
   improved analytical/numerical models incorporating real materials, actual
   fires, and partial-gravity effects.

## Open questions

- The paper references "Table 1" (ULOI/MOC differences by gravity level) and
  "Figure 2" (a flammability-boundary map). Only their surrounding narrative
  discussion is captured above — the underlying numeric table and figure
  appear to be image-based in the source PDF and did **not** convert to
  extractable text; no table data with that content was found anywhere in
  the converted extraction. This is a genuine source-format gap, not an
  extraction omission — a future pass would need the original PDF's actual
  image/table content (e.g. via a vision-capable read of that specific page)
  to fill it in.
- Reference [1] in this paper (cited in the recommendations section) is the
  BASS-II Summary Report itself (NASA-TM-202110011385) — consistent with
  this corpus's own `bass-ii.md` entry.

[^miller-decadal-2023]: Topical: Spacecraft Materials Fire Safety. Introduction: "Fire safety in spacecraft, and in future Lunar and Martian habitats, is of critical importance to the mission objectives of NASA... The physics of ignition, flammability, and fire in microgravity, and especially partial gravity (between 0g and 1g, such as on the Moon or Mars), are difficult to study in Earth gravity and therefore present unknown risks." "NASA's primary method of addressing this risk is through materials testing and controls... materials are flight-qualified by passing the NASA-STD-6001B Test#1, which is an ignition and upward flame spread test in normal Earth gravity at the worst end-use ambient oxygen concentration and pressure. Historically, this was thought to be a conservative estimate of the material flammability and fire spread potential in microgravity due to the fast upward accelerating spread of the flame in Earth's gravitational field as a result of fluid buoyancy. However, over the last decade, materials flammability testing in actual low gravity and partial gravity conditions has shown that this is sometimes not the case... flammable (sometimes very flammable) materials can be granted waivers from the normal control process for use out of necessity or crew comfort (i.e., clothing, cotton towels, Delrin camera mounts, hair length, paper notebooks, etc.)." Overview of Research on Solid Fuel Accomplished Since the Previous Decadal Survey: "As a solid fuel retrofit of the Smoke Point in Co-flow Experiment (SPICE) wind tunnel for the Burning and Suppression of Solids (BASS) and BASS-II reflight, BASS-M (commercial partner experiment), and BASS-Confined Combustion, hundreds of solid fuel test points were conducted in the Microgravity Science Glovebox (MSG) aboard ISS... The highly productive facility has produced 70 conference and journal articles on microgravity solid fuel combustion to date... The BASS series of experiments were limited to 1 atmosphere, and oxygen concentrations below 22% due to MSG constraints. While appropriate for ISS operations, these are not the conditions that are proposed for future exploration campaigns, which might include oxygen concentrations up to 34%." "As shown in Table 1, the differences in the 1g and 0g or partial g Upward Limiting Oxygen Concentration (ULOI) and Minimum Oxygen Concentration (MOC) are largest for the Lunar g level, indicating poor safety margins." "Larger scale fire research in spacecraft began in 2016 with the advent of the Saffire experiments. Saffire launched with a Cygnus resupply vehicle and remained dormant until the Cygnus undocked and departed the ISS. The Saffire tests used the air in the vehicle to burn the fuel samples, and the data were relayed to Earth prior to the vehicle deorbit and destructive reentry into the Earth's atmosphere. To date, five Saffire experiments have been performed with one more waiting for launch, some with multiple tests and in most cases increasing sample sizes by one to two orders of magnitude over any previous tests (some samples were close to a meter long). The tests showed that fires can continue to burn for extended periods of time after the flow is turned off, due to the thermal mass of thick molten fuel. The fuel can generate local flows due to fuel vapor bubble ruptures at the surface that entrain ambient air flow and allow the flame to survive in the otherwise quiescent environment. Charring materials can smolder for extended periods of time in a quiescent environment, and the smoldering spots can re-ignite the fuel when the air flow is turned on. Flames can ignite adjacent fuel samples, and flames can extinguish other flames that are downstream by starving them of oxygen. These results indicate that the ISS fire-safety first response to turn off the ventilation is not enough to guarantee a fire will be extinguished. Additional reliable mitigation and more research are needed." "Figure 2 depicts a flammability boundary as a function of oxygen mole fraction and ambient flow speed. Most materials in normal gravity blow off (like blowing out a candle) rather than quench due to heat losses. The minimum in the flammability boundary is where the flow speed is expected to be near Lunar gravity buoyant flow conditions." "Figure 2 Flammability map showing partial and microgravity regions being the most flammable." "A centrifuge for NASA's Zero Gravity Research Facility (ZGRF) capable of producing variable amounts of partial gravity was recently revamped for solid fuel experiments. This facility has shown that the limits of flammability clearly depend on gravitational level, and that the most flammable upward flame spread conditions for certain fuels are near Lunar gravity levels... The centrifuge, while useful, does suffer from Coriolis forces and is limited to very small samples. A proposed upgrade to the ZGRF to extend the microgravity time and to allow for partial gravity experiments would be a welcome addition to NASA's facilities... Most partial gravity work has been conducted in the Centrifuge drop rig in NASA's Zero Gravity Research Facility, which is very limited in size, but a few test campaigns have been performed in parabolic aircraft." "In coming work, the Solid Fuel Ignition and Extinction (SoFIE) insert for the Combustion Integrated Rack (CIR) aboard the ISS is scheduled to launch in 2022 to support five separate peer-reviewed NASA NRA-selected solid fuel combustion experiments (GEL, MIST, SMURF, RTDFS, NCA). These experiments are focused on understanding the burning behavior and flammability limits of idealized PMMA fuel in various geometries, and in one case under an imposed heat flux. This fuel was chosen for its idealized burning which can support multiple test points per sample to maximize results in the difficult-to-open CIR chamber, and to permit comparisons to detailed numerical models. The CIR/SoFIE facility is capable of studying solid fuel combustion at a wider range of pressures and oxygen concentrations compared to MSG, extending to the expected exploration atmospheres at 34% oxygen and reduced pressures. Note that this facility cannot reach Extra Vehicular Activity (EVA) oxygen concentrations of 100% due to hardware limitations." Outline of Recommended Research Areas: "It is imperative to the safety of the spacecraft crew and mission assurance that NASA expands research on fundamental fire research and flammability of real-world utilized materials, including more realistic configurations which promote flammability such as a fiber mesh, fuel samples with exposed edges and corners, discrete fuel configurations, and parallel samples... NASA's samples have necessarily been limited almost exclusively to flames on small-scale, model materials (Saffire did use some larger-scale samples, but they were still idealized fuels). More ground-based and flight tests are needed with real flight materials to determine the level of conservatism of the NASA-STD-6001B Test#1. Large scale fire research in spacecraft should continue to utilize cargo vehicles, and new research efforts should explore realistic fire scenarios of battery fires or other externally energized flames which drive pyrolysis via radiation and heat." "While material flammability in microgravity is still in its childhood, even less is understood about the flammability dangers in partial gravity (especially Lunar and Martian). Previous testing has shown that Lunar gravity may present a maximum flammable condition by buoyantly pumping a just the right amount of oxidizer into the flame stabilization zone (critical for continued burning) while not exceeding the entrainment velocity which causes flame blow-off... Additional work needs to be done with large enough sample sizes to reach steady flame sizes in Lunar g levels. Fuel configurations should be studied that have recirculation zones in the wake region which allow the flame to survive beyond the normal blow-off limit as they anchor in the recirculation wake. Realistic materials proposed for use on the Moon should be evaluated if they are either waivered or controlled but borderline passing 6001B Test 1, as they might become flammable in the new partial gravity conditions... Finally, the new exploration atmospheres of up to 34% oxygen will likely require the retest of many materials even under the current protocols, and potential new tests such as the Narrow Channel Apparatus (NCA) which have a much higher throughput, and better represent microgravity conditions, should continue to be developed." "In summary, we have identified the following needs for the coming decade: Testing of material flammability in partial gravity to support Lunar/Martian habitat fire safety. Potential test facilities/platforms include the ZGRF centrifuge, the ZGRF upgrade, parabolic flight, orbital or sub-orbital centrifuge, Lunar lander or habitat glovebox. Testing of more real-world materials (waivered and controlled borderline materials) in reduced gravity, exploration atmospheres (i.e., higher oxygen and lower pressure). Continued access to long-duration, microgravity for realistically thick materials, including tests of the effect of flow such as with the planned Microgravity Wind Tunnel. Need for new materials and retardant additives and coatings with reduced flammability in high oxygen microgravity environments (e.g., safe clothing for 35% oxygen). Need more testing of configurations which promote or inhibit flammability in microgravity, externally driven radiation, radiation feedback between surfaces, etc. Although batteries are rigorously screened, they represent the potential for high energy release. Battery fires should be studied to determine how the reduced natural convective environment might reduce battery life and cause overheating failures. A new materials flammability standard which better represents low gravity conditions. Continued development of higher throughput material screening tests such as the NCA so that materials can be tested faster under the new exploration atmospheres in flow conditions that better represent those on spacecraft. Larger flames and fires need to be studied to extrapolate to scales that pose a hazard (ideally, those actual scales would be tested). Establish best-practices guidebook for material selection and utilization in low-gravity and partial-gravity. Analytical and numerical models involving real materials, actual fires, and partial gravity effects need to be improved." Reference 1: "Olson, S.L., Ferkul, P.V., Bhattacharjee, S., Miller, F.J., Fernandez-Pello, C., Link, S., T'ien, J.S., Wichman, I.; Burning and Supression of Solids-II (BASS-II) Summary Report, NASA-TM-202110011385, 2021."
