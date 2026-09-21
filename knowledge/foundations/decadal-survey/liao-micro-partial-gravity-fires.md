---
type: Document
title: "Challenges and Research Needs for Micro- and Partial-Gravity Fires"
description: Decadal Survey topical white paper by Ya-Ting Liao et al. on fire dynamics research needs for microgravity and partial-gravity spaceflight, including a direct call for a comprehensive fire database.
status: stable
generated: { by: "claude-code/sonnet-5", at: 2026-09-21T19:56:58Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-21T19:56:58Z }
order: 12
sources:
  - id: liao-decadal-2021
    title: "Topical: Challenges and Research Needs for Micro- and Partial-Gravity Fires"
    resource: "https://ntrs.nasa.gov/citations/20210022403"
verified:
  - by: human:you
    at: 2026-09-21T19:56:58Z
---

This topical white paper, submitted by Ya-Ting Liao (Case Western Reserve
University) and coauthors as part of NASA's decadal survey process for
biological and physical sciences research in space, argues that fire safety
grows more urgent for
longer-duration missions — Artemis, and eventually Mars — where terrestrial
help is unavailable and partial-gravity conditions plus proposed high-oxygen
Lunar habitat atmospheres compound the risk.[^liao-decadal-2021]

## Why microgravity fire behavior differs from Earth's

On Earth, burning is always accompanied by buoyant flow — a
temperature-driven density gradient that accelerates as the flame grows and
increasingly entrains fresh air, which is why upward-spreading flames are
usually the most dangerous configuration. In microgravity,
buoyant flow is essentially eliminated and molecular diffusion controls
fuel/oxidizer mixing; spacecraft HVAC systems instead generate a low-speed
forced flow of roughly 10–20 cm/s that can bring fresh oxidizer to a fire
zone.[^liao-decadal-2021] Solid and gaseous fuels can even burn in quiescent
(no external flow) microgravity, especially in enhanced-oxygen environments —
useful for studying chemistry and heating without buoyancy's influence, but
not the worst-case fire-safety scenario because flame growth is relatively
slow at the oxygen concentrations proposed for Lunar missions.[^liao-decadal-2021]

For flame spread in low-speed forced flows, experiments show flames reach a
steady spreading state with constant flame length: for thin samples the
spread rate is controlled by burnout of the solid sample, while for thick
samples that don't burn out, a limiting length is set by the balance between
heat input from the flame and heat loss from the solid surface in the
preheat region. The steady spread rate depends on
forced-flow velocity, ambient pressure, oxygen percentage, flow confinement,
sample thickness, and sample arrangement.[^liao-decadal-2021]

### Extinction boundary: quenching limit vs. blowoff limit

The extinction (flammability) boundary consists of two limits.
The **low-velocity quenching limit** is where the rate of heat generation
during combustion becomes comparable to the heat loss (radiative loss on the
sample surface, radiative and conductive heat loss from the flame). The
**high-velocity blowoff limit** is due to insufficient residence time of the
reactants in the flame anchor zone — the residence time becomes smaller than
the reaction time (a low Damköhler number). As oxygen
percentage increases, the low-velocity quenching limit decreases and the
high-velocity blowoff limit increases; at a given ambient oxygen level, an
optimal flow rate exists for flame spread over a thick fuel.[^liao-decadal-2021]

Two further limitations the paper flags: most microgravity tests to date
have focused on idealized fuels (PMMA, cellulose-based materials) rather than
practical materials with non-ideal burning behaviors (melting, intumescence,
thick char layers); and smoke release is under-studied — in microgravity,
increased residence time modifies the flame's radiative structure, supporting
local extinction and massive smoke release, a major issue in an enclosed
spacecraft.[^liao-decadal-2021]

## Flame spread in partial gravity

In partial gravity, buoyancy flow is expected to be weaker than on Earth,
leading to smaller convective heat loss and longer reactant residence time in
the flame stabilization zone — implying a material may be combustible across
a wider range of oxygen and pressure than in normal gravity.[^liao-decadal-2021]
Limited existing data suggests a direct proportionality between flame spread
rate and gravity in the upward configuration for very thin fuels, depending
also on sample width and ambient pressure; downward-spreading flames instead
showed non-monotonic behavior with gravity, attributed to competition between
chemical kinetics and radiative losses.[^liao-decadal-2021]

This matters for certification: current materials-selection methods rely on
ground tests in Earth gravity (e.g. NASA 6001 tests), but different gravity
levels between ground tests and space missions can produce unexpected fire
behavior — studies of extinction limits as a function of gravity have shown
combustion sustained at partial-gravity levels where the same solid materials
extinguished at both micro- and normal gravity. Partial-gravity
fire behavior (Moon, Mars) cannot be assumed interpolable between normal- and
micro-gravity data, which themselves are not yet fully understood.[^liao-decadal-2021]

**Proposed exploration atmospheres, by name:** the Lunar modules are expected
to have an oxygen concentration of 34% and a pressure of 56.5 kPa; the Lunar
Gateway is expected to have an oxygen concentration of 26.5% and a pressure
of 73.5 kPa. Despite reduced ambient pressure slowing
flame chemical kinetics and increasing heat losses, ground-based experiments
of upward flame spread in normoxic conditions have shown higher flammability
proportional to oxygen concentration, even for fire-resistant fabric such as
Nomex. Scales and confinement in standard tests and prior
research also differ substantially from realistic spacecraft fire scales, so
it is uncertain whether existing knowledge applies to realistic fire
scenarios for future missions. The paper's proposed
next-decade focus is twofold: (1) advancing fire dynamics in micro and
partial gravity, and (2) developing reliable predictive tools — dimension
modeling, numerical modeling, and machine learning models.[^liao-decadal-2021]

## Scale modeling

Fire scale modeling dates to the 1960s; Williams identified 29 dimensionless
groups describing a fire system, on the assumption that fire phenomena in
different gravity fields can be correlated, at least partially, by
preserving some of those groups. Because complete
combustion modeling is practically impossible, successful fire modeling
instead uses **partial modeling** — identifying dominant invariant groups and
deliberately ignoring phenomena judged to least affect the fire in the
scenario of interest.[^liao-decadal-2021]

Two established partial-modeling approaches: **Froude modeling**, which holds
the dimensionless group gL/u² constant to relate small- and full-scale fires
through the buoyancy flow term; and **pressure modeling**, which holds P²L³
constant, replicating real-fire buoyancy flows by controlling density
(inversely proportional to pressure) in reduced-scale tests — on the
assumption that, compared to buoyancy/viscosity groups, other
density-containing dimensionless groups are insignificant.[^liao-decadal-2021]

A further approach uses reduced pressure (and consequently reduced density)
to reproduce partial/microgravity burning characteristics directly: as
pressure drops, flames move away from the fuel surface, the boundary layer
thickens, fuel-surface heating by the flame reduces, and spread rate/flame
length both drop — the same consequence reduced buoyant flow velocity has in
low gravity. Prior experiments suggest reduced pressures
of roughly 20–40 kPa may simulate microgravity flames in terms of spread rate
and flame length, at least for thin combustible materials, and models holding
a constant Grashof number (P²g ~ constant) have successfully correlated
partial-gravity results. There are limits to the
low-gravity/low-pressure comparison, though — pressure has a significant
effect on flame spread even without buoyant flow, pressure and gravity both
affect the laminar-to-turbulent transition (with implications for heat
release), radiation losses grow more important at reduced pressure, and
lower molecular density makes diffusion processes more important — together
these can change flame structure. Because several aspects
of fire behavior (laminar vs. turbulent flame, soot formation, thermal and
chemical processes) respond differently to ambient conditions depending on
the specific burning configuration, the paper concludes that long-term,
realistic partial-gravity experiments are required to develop robust scale
models and validate existing ones — a successful scale-modeling approach
would enable new flammability tests for future space exploration.[^liao-decadal-2021]

## The gap this corpus addresses

The paper states directly that the field's own data-access problem remains
unsolved: NASA's Physical Sciences Informatics (PSI) repository holds
experimental data from several past investigations, but "the current version
of the PSI is far from completion. Combustion investigations before the 2000s
are missing." It also identifies the same root cause this
corpus's structured-facts approach is built to address: limited, camera-based
diagnostics "prevent direct comparisons between different experiments."[^liao-decadal-2021]

## Recommendations

The paper's five research recommendations include, verbatim as its fourth:
"Comprehensive fire database. Such a database would accelerate model and
theory development, as well as allowing the application of machine learning
techniques that could lead to transformative discoveries in combustion and
fire science." The other four recommendations cover
microgravity fire science for practical (non-idealized) materials, partial-gravity
fire science (citing that materials are likely more flammable in partial
gravity due to longer residence times), scale modeling of gravity/buoyancy
effects, and new experimental platforms for partial-gravity testing —
including upgrading NASA Glenn's Zero Gravity Research Facility drop
tower.[^liao-decadal-2021]

## Open questions

- The paper's full numbered reference list (citations 1–64) is not
  reproduced — only the in-text claims themselves are extracted.
- The paper's Introduction paragraph on fire as a multi-physics process
  (fluid dynamics, thermal/species diffusion, gas radiation, chemical
  kinetics, solid decomposition, buoyancy) is not separately extracted here;
  it is implicit in the sections above.

[^liao-decadal-2021]: Topical: Challenges and Research Needs for Micro- and Partial-Gravity Fires. Introduction: "Spacecraft fire safety has always been an essential component for any successful space mission. The importance increases exponentially for longer duration missions, such as the upcoming Artemis missions to the Moon and the \"next giant leap\" to Mars. If fire occurs in the spacecraft, terrestrial help for recovery may not be possible... The partial gravity conditions after landing on the Moon or Mars, as well as the high oxygen concentration proposed for the Lunar habitat, bring in additional challenges for spacecraft fire safety." "On Earth, this burning process is always accompanied by buoyant flow, which is caused by a temperature-driven density gradient in a gravity field. The buoyant flow accelerates as the flame grows and entrains an increasing volume of fresh air... due to its acceleratory nature on Earth, the case of upward spreading flames is usually considered the most dangerous configuration." Flame spread over solid materials in microgravity: "In microgravity, the flow from buoyancy is essentially eliminated, and without an external flow, molecular diffusion controls the mixing of fuel and oxidizer. Research has indicated that solid and gaseous fuels can burn in quiescent microgravity, especially in enhanced oxygen environments. This quiescent environment is extremely important for studying the chemical and heating processes without the influence of buoyancy. However, from a fire safety point of view, this configuration does not necessarily represent the worst burning scenario due to the relatively slow flame growth, at least for the oxygen concentrations proposed for the Lunar missions. The heating, ventilation, and air conditioning (HVAC) systems onboard space vehicles generate a low speed forced flow (~ 10-20 cm/s), which can bring in fresh oxidizer to the combustion zone when a fire occurs." "For flame spread in low-speed forced flows, experiments showed that flames eventually reach a steady spreading state with a constant flame length. For thin samples, the flame spread rate is controlled by the burnout of the solid sample. For thick samples that do not burn out, the mechanism for a limiting length to be achieved is the balance between heat input from the flame and heat loss from the solid surface in the preheat region. The steady flame spread rate was shown to be a function of forced flow velocity, ambient pressure, oxygen percentage, flow confinement, sample thickness, and sample arrangement (e.g., discrete patterns)." "Some studies focused on characterizing the extinction limits of flame spread in terms of ambient oxygen percentage and flow velocity. The extinction (or the flammability) boundary consists of a low-velocity quenching limit and a high-velocity blowoff limit. The quenching limit is a condition at which the rate of heat generation during combustion becomes comparable to the heat loss (e.g., radiative loss on the sample surface, radiative and conductive heat loss from the flame). The blowoff limit is due to insufficient residence time of the reactants (the residence time is smaller than the reaction time i.e., low Damkohler number) in the flame anchor zone. As the oxygen percentage increases, the low-velocity quenching limit decreases and the high-velocity blowoff limit increases. At a given ambient oxygen level, there exists an optimal flow rate for flame spread over a thick fuel." "While previous studies provided abundant data, the majority of the microgravity tests have focused on idealized fuels (PMMA, cellulose-based materials). Practical materials that have non-ideal burning behaviors (such as melting, intumescence, thick char layers, or a combination of these burning behaviors) need to be studied to better understand how to mitigate fires in spacecraft. Another topic that is under-studied is the smoke release in fires. In microgravity, the increased residence time modifies the radiative structure of the flame, supporting local extinction of the flame and the massive release of smoke, which is a major issue in the enclosed environment of a spacecraft." Flame spread over solid materials in partial gravity: "In partial gravity, the buoyancy flow is expected to be weaker than that on Earth, leading to smaller convective heat loss and a longer residence time of reactants in the flame stabilization zone during flame spread. These may imply that a material is combustible in a wider range of oxygen and pressure in partial gravity than in normal gravity. The limited available experimental data obtained at different gravity levels suggest a direct proportionality between flame spread rate and gravity in the upward configuration for very thin fuels. The proportionality depended also on sample width and ambient pressure. On the other hand, downward spreading flames showed a non-monotonic behavior with gravity, which was attributed to the competition between chemical kinetics and radiative losses." "Current methods for materials selection for use in space vehicles rely on ground tests in Earth gravity (e.g., NASA 6001 tests). However, the different gravity levels between ground tests and space missions can result in unexpected fire behaviors. For instance, the study of extinction limits as a function of gravity has shown that combustion could be sustained at partial gravity levels, while extinction of the same solid materials occurred at both micro- and normal gravity. Fire behavior in partial gravity (e.g., on Moon and Mars) cannot be expected to be interpolated between the data obtained in normal and microgravity conditions (which themselves are not yet fully understood). In addition, the proposed atmosphere for habitable structures in future space missions requires an oxygen concentration higher than sea-level conditions and at a reduced pressure to lower the preparation time for Extravehicular Activities (EVA). The Lunar modules are expected to have an oxygen concentration of 34% and a pressure of 56.5 kPa and the Lunar Gateway is expected to have an oxygen concentration of 26.5% and a pressure of 73.5 kPa. Despite the reduced ambient pressure which can slow down the flame chemical kinetics and increase its heat losses, ground based experiments of upward flame spread in Normoxic conditions have shown higher flammability, proportional to the oxygen concentrations, even for fire resistant fabric such as Nomex." "Lastly, scales and confined conditions in standard tests and previous research are very different from realistic spacecraft fire scales. It is uncertain if the knowledge gained is applicable for realistic fire scenarios and for future space missions. To fill these knowledge gaps, in the next decade we propose to focus on: 1) advancing fire dynamics in micro and partial gravity, and 2) developing reliable predictive tools for fire in space. Such tools include dimension modeling, numerical modeling, and machine learning models." Scale Modeling: "Scale modeling and its fire applications were discussed as early as the 1960s. Williams identified 29 dimensionless groups constructed from the physical quantities that describe a fire system. Assumption here is that fire phenomena in different gravity fields can be correlated (at least partially) by preserving some of the dimensionless groups." "The complexity of combustion renders complete modeling practically impossible. Successful fire modeling requires identifying dominant invariant groups and deliberately ignoring some known phenomena that are deemed to least affect the fire under the scenario of interest. This approach is called partial modeling and has been successful in yielding empirical equations for various fire systems. For example, many studies employ Froude modeling where the dimensionless group gL/u2 is kept constant. This approach relates small and full-scale fires through the buoyancy flow term u. Rich data for empirical equations/correlations exists in literature for various fire scenarios. Some studies apply pressure modeling where P2L3 is kept constant. The concept is to replicate buoyancy flows encountered in real fires by controlling density (inversely proportional to pressure in the ideal gas approximation) in reduced-scale fire tests. This partial modeling technique is based on the assumption that, compared to dimensionless groups for buoyancy and viscosity, other dimensionless groups that contain density terms are insignificant." "Another possible approach is to use reduced pressure, and consequently reduced density, to reproduce the burning characteristics observed in partial and microgravity conditions. As the pressure is reduced, flames tend to move away from the fuel surface and the boundary layer along the solid fuel becomes thicker. Furthermore, this behavior causes a reduced heating of the fuel surface by the flame, which results in lower spread rate and flame length. Thus, the effect of reducing the ambient pressure has similar consequences as reducing the buoyant flow velocity in low gravity. Previous experiments suggest that reduced pressures ranging between 20-40 kPa may be able to simulate flames in microgravity in terms of flame spread rate and flame length, at least for thin combustible materials. Furthermore, models involving a constant Grashof number (P2g ~ constant) have been successful in correlating partial gravity results. However, there are some limitations to the comparison between low gravity and low pressure, especially since pressure showed a significant effect on flame spread even in the absence of buoyant flows. Moreover, pressure and gravity affect the laminar to turbulent transition of the flame, with implications on the heat released by the flame. Numerical studies and scaling analyses highlighted the importance of radiation losses in reduced pressure environments. At the same time, diffusion processes become more important because of the lower molecular density. This, in combination with different heating mechanisms and pressure effects on chemical kinetics, can change the flame structure." "Considering the multi-physics nature of fires, several aspects of the fire behavior (laminar vs turbulent flame, soot formation, theraml and chemical processes) are affected by the ambient conditions in different ways, depending on the specific burning configuration. Long-term and realistic experiments in partial gravity will be required to develop robust scale models of fires and to examine the validity of existing models. A successful scale modeling approach will allow the design of new flammability tests for future space exploration." Comprehensive Database and Machine Learning: "Several combustion and fire experiments from previous NASA investigations have been added in recent years to the Physical Sciences Informatics (PSI) repository... However, the current version of the PSI is far from completion. Combustion investigations before the 2000s are missing." Experimental Capabilities: "While many microgravity fire experiments exist, diagnostics were limited. For example, most of the past experiments relied on camera images for detecting the flame regions. However, these images pertained to the camera capabilities and settings and by no means fully resolved the flame structure... These limitation prevents direct comparisons between different experiments." Conclusions and Recommendations: "1. Microgravity fire science. Studying fire behaviors and their dependencies on ambient pressure, oxygen, and flow for practical (non-idealized) materials would lead to the best practices for preventing and minimizing risks for spacecraft fires. 2. Partial gravity fire science. Due to longer residence times materials are likely more flammable in partial gravity, giving the need to study flame spread in Lunar and Martian gravity... 3. Scale modeling in partial and microgravity flames... 4. Comprehensive fire database. Such a database would accelerate model and theory development, as well as allowing the application of machine learning techniques that could lead to transformative discoveries in combustion and fire science. 5. New platforms and techniques for partial gravity experiments. Upgrading the Zero Gravity Research Facility for partial gravity testing, in addition to parabolic flights, could be used to create new standardized flammability tests."
