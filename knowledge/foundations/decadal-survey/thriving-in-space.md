---
type: Document
title: "Thriving in Space (2023 Decadal Survey) — Combustion and Fire Safety"
description: The combustion-science and spacecraft fire-safety sections of the National Academies' 2023-2032 decadal survey for biological and physical sciences research in space.
status: stable
generated: { by: "claude-code/sonnet-5", at: 2026-09-21T19:56:58Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-21T19:56:58Z }
order: 10
sources:
  - id: thriving-in-space-2023
    title: "Thriving in Space: Ensuring the Future of Biological and Physical Sciences Research: A Decadal Survey for 2023-2032"
    resource: "https://doi.org/10.17226/26750"
verified:
  - by: human:you
    at: 2026-09-21T19:56:58Z
---

> [!NOTE]
> This entry covers only the combustion-science and fire-safety portions of
> "Thriving in Space" — a 322-page decadal survey spanning all of biological
> and physical sciences research in space. It is not a summary of the whole
> book.

"Thriving in Space" is the National Academies of Sciences, Engineering, and
Medicine's 2023 decadal survey for biological and physical sciences research
in space, covering 2023-2032. Its combustion science section
frames why microgravity combustion research matters for both spacecraft fire
safety and terrestrial energy: currently 86 percent of the world's energy
demand is met through combustion.[^thriving-in-space-2023]

## Why gravity matters for combustion research

The lack of buoyant flow in microgravity creates an opportunity for
fundamental combustion studies free of the dominating influence buoyancy has
in terrestrial laboratories — over the past three decades, researchers have
exploited reduced gravity to discover new combustion systems such as
"sofballs" and cool diffusion flames. Combustion science
within the space environment also directly informs spacecraft fire safety —
improved material qualification, fire detection, and fire
suppression.[^thriving-in-space-2023]

## Why past results may not transfer to Artemis-era missions

The survey states this directly: Artemis-program cabin atmospheres will have
lower cabin pressure with increased ambient oxygen concentration (to reduce
required prebreathing time for extravehicular activity), and because fires
are very sensitive to ambient oxygen mole fraction, reactants and materials,
diluents, pressure, and gravitational forces, "fire safety practices deemed
safe in the microgravity environment of the ISS... may no longer offer the
same factor of safety (or be completely inapplicable) for future exploration
missions." It also states plainly that existing microgravity
combustion and fire studies "have been limited in terms of flame and fire
sizes, diagnostics, pressures, and the effects of lunar and martian
gravity."[^thriving-in-space-2023]

## Fire safety and the flammability-index question

The survey's dedicated Fire Safety section traces this back to the *previous*
decadal survey (2011), which already flagged that "the understanding of
material flammability in reduced gravity is incomplete," with concerns about
fire detection/suppression systems designed for reduced gravity.
It compares material screening via a flammability index (maximum oxygen
concentration, MOC, or limiting oxygen index, LOI) against the pass/fail test
based on NASA-STD-6001B, and notes that material flammability in microgravity
— not just at 1g but in partial gravity — can be *higher* than in normal
Earth gravity, making quantification of that difference across partial-gravity
levels important. It cites BASS by name as having
investigated burning and extinction characteristics of a wide variety of fuel
samples in microgravity, covering part of that parameter space.[^thriving-in-space-2023]

## Cool flames: FLEX and ACME

The survey highlights FLEX and ACME together: prolonged "cool flame" burning
of isolated large-diameter droplets, observed under the FLEX program, showed
for the first time a two-stage (hotter and cooler) combustion
behavior.[^thriving-in-space-2023]

### Box 2-6: the cool-flame discovery in full

"Cool flame" combustion was not identified as a topic of study in the
*previous* decadal survey ("Recapturing a Future for Space Exploration") —
its accidental discovery aboard the ISS in the following decade triggered a
surge of research driven both by fundamental interest and by fire-safety
implications, since low-temperature cool-flame combustion cannot be visibly
observed. Onboard the ISS, the Multi-User Droplet
Combustion Apparatus (MDCA) in the Combustion Integrated Rack (CIR) — FLEX's
own hardware — was used for the isolated-droplet work, across a range of
initial droplet diameters, different single-component fuels (alcohols,
n-alkanes, primary reference fuel blends of n-heptane and iso-octane), over a
pressure range of 0.5–3 atm. The low-temperature
cool flame is self-sustaining for long durations — up to 40 seconds,
depending on fuel and droplet diameter. Mathematical
modeling of the FLEX experiments indicates the observed second-stage burning
occurs at temperatures between the turnover temperature and the hot-ignition
temperature, within the negative-temperature-coefficient regime, driven by
excessive heat loss during the first-stage high-temperature burn.
This research also connects to terrestrial engines: reducing emissions and
improving fuel efficiency at high pressure via low-temperature combustion
strategies (homogeneous charge compression ignition, HCCI; reactivity-controlled
compression ignition, RCCI) was a primary motivator for cool-flame
research.[^thriving-in-space-2023]

## Why NASA's current flammability standard has known gaps

A dedicated "Potential Research Areas" question — "What aspects of fluid
behavior will improve fire safety onboard spacecraft?" — states that the
present flammability standard accepted by NASA (NASA-STD-6001B) is a
pass/fail ground test in which an upward flame is spread over a material
sample, and identifies its known drawbacks directly: cabin-air conditions
onboard spacecraft (pressure, oxygen content) can change; natural convection
does not occur in microgravity, so the flow around the flame instead comes
from the HVAC system or astronaut movement and can be very low and/or
irregular in velocity; and combustion products remain around the area where
combustion took place rather than dispersing as they would under
buoyancy. It cites Fujita (2015) as a summary of
existing microgravity flammability studies and the shortcomings of existing
flammability tests, and concludes more systematic investigation is essential
to improve fire safety, develop predictive models, and develop new
fire-resistant materials.[^thriving-in-space-2023]

The same section notes that previous testing at microgravity and Lunar
gravity found some materials burn to *lower* oxygen concentrations in low
gravity than in normal gravity, and Martian-gravity data similarly suggested
a partial-gravity level at which materials burn more readily than on
Earth. Flames — especially in microgravity — can
also be strongly affected by electromagnetic fields, per preliminary studies
(Chien et al. 2022), connecting directly to ACME's Electric-Field Effects
sub-experiment. The section also names the ongoing
coflow laminar diffusion (CLD) flame research (Smooke et al. 1999) — ACME's
CLD Flame sub-experiment by name in substance — where, in orbit, coflow
velocity becomes an important control parameter for flame shape, stability,
and burning-product generation, a control impossible to isolate on Earth
where the coflow would be gravity-directed upward.[^thriving-in-space-2023]

## Chemical kinetics and combustion processes (priority research area)

A separate "Potential Research Areas" section, titled "Chemical Kinetics and
Combustion Processes," states that microgravity experiments have provided
unprecedented insight into chemical kinetic phenomena: the importance of
radiative loss in determining flammability limits; new steady-state regimes
of low- and intermediate-temperature fuel burning (cool and warm flames);
and insights into sooting and the formation of large soot agglomerates, with
implications for understanding wildfire effects on the environment and for
materials synthesis. Microgravity experiments have
also demonstrated that electric fields and charges (ions and electrons) can
affect energy transfer, reactions, and flow motion — but large buoyant flows
in terrestrial laboratories prevent the low-strain environment necessary to
study flame structures or reaction-wave fronts governed by chemical kinetics
and charged-particle motion. The section calls for
fundamental experiments to develop predictive tools for chemical kinetics
across fuels including biofuels, e-fuels, and low-carbon fuels.[^thriving-in-space-2023]

It further notes that large soot "super-agglomerates" are preferentially
formed in microgravity flames, where the absence of buoyancy allows the long
residence time these structures need to form — and that the low
stretch/strain environment reduced gravity provides is the strictest test of
chemical kinetic mechanisms available, since flame-structure limits there are
kinetically controlled rather than flow-controlled.[^thriving-in-space-2023]

## Open questions

- Figures 2-20 and 2-21 (SoFIE hardware and a BASS run onboard the ISS), and
  Figure 4-13 (a near-spherical orbital flame), are referenced by the source
  but the images themselves are not reproduced here.
- This entry does not extract the survey's top-level, cross-chapter
  prioritized findings/recommendations lists (e.g. numbered "Finding" or
  "Priority" statements outside the combustion-specific sections already
  covered) — only the combustion/fire-safety content itself.
- Citations within the source (e.g. "Farouk et al. 2017," "Chien et al.
  2022," "Fujita 2015") are named inline as the source names them, but this
  entry does not independently verify or expand on those cited papers.

[^thriving-in-space-2023]: Thriving in Space: Ensuring the Future of Biological and Physical Sciences Research: A Decadal Survey for 2023-2032. Front matter / suggested citation: "National Academies of Sciences, Engineering, and Medicine. 2023. Thriving in Space: Ensuring the Future of Biological and Physical Sciences Research: A Decadal Survey for 2023-2032. Washington, DC: The National Academies Press. https://doi.org/10.17226/26750." Combustion: "Combustion science involves fluid mechanics, heat transfer, phase change, transport phenomena, thermodynamics and chemistry... The lack of a buoyant flow, however, also creates a unique opportunity for researchers-the ability to perform fundamental studies of combustion phenomena without the complicating and dominating influence of the buoyancy-induced flow. Over the past 3 decades, combustion and fire researchers have exploited the reduced-gravity environment in ground-based and space-based facilities... Entirely new combustion systems, such as so-called sofballs (Ronney 1998) and cool diffusion flames (Ju 2021), have been developed... Currently, 86 percent of the world's energy demand is met through combustion (Ritchie et al. 2022)." "Combustion science within the space environment also informs spacecraft fire safety, leading to improved material qualification, fire detection, and fire suppression in spacecraft and outposts (Guibaud et al. 2022)." "NASA's future exploration goals are just beginning with the start of the Artemis program. The cabin atmospheres in the Artemis program will have lower cabin pressure with an increased ambient oxygen concentration (to minimize the required prebreathing time for extravehicular activities). Because fires are very sensitive to ambient oxygen mole fraction, reactants and materials, diluents, pressure, and gravitational forces, fire safety practices deemed safe in the microgravity environment of the ISS (with a cabin atmosphere identical to air on Earth) may no longer offer the same factor of safety (or be completely inapplicable) for future exploration missions." "While there have been dozens of microgravity combustion and fire studies in drop facilities, parabolic aircraft, and spacecraft (Kono et al. 1996; Sun et al. 2020), as well as the ISS (Dietrich et al. 2014), those studies have been limited in terms of flame and fire sizes, diagnostics, pressures, and the effects of lunar and martian gravity." Fire Safety: "The last decadal survey, Recapturing a Future for Space Exploration (NRC 2011), identified the development of fire safety protocols for spacecraft and space habitats-an important area that is integral to astronaut safety. It was also mentioned that the understanding of material flammability in reduced gravity is incomplete, and concerns existed about the effectiveness of fire detection and fire suppression systems designed for reduced gravity." "Reviews have emphasized the advantages of material screening methods based on a flammability index such as maximum oxygen concentration (MOC) or limiting oxygen index (LOI) in comparison to the pass/fail test based on NASA STD 6001B... Material flammability in microgravity (not just in 1 g but in partial gravity), however, can be higher than that in normal Earth's gravity. Therefore, the quantification of the difference as a function of partial gravity is important to universally use flammability index as the material screening method." "NASA's Burning and Suppression of Solids (BASS) program investigated the burning and extinction characteristics of a wide variety of fuel samples in microgravity and covered some of the parameter space." Cool Flames: "The recent observations of prolonged \"cool flame\" burning of isolated large-diameter droplets under the flame extinguishment (FLEX) experiments program on microgravity combustion and advanced combustion microgravity experiments (ACME) (Nayagam et al. 2012) have simulated substantial interest (Ju 2021)... The FLEX experiments for the first time showed two-stage (hotter and cooler) combustion behavior." Box 2-6, Combustion Science Required to Address a Flaming Surprise on the International Space Station: "Note that \"cool flame\" combustion was not identified as a topic of study in Recapturing a Future for Space Exploration. However, its accidental discovery onboard the International Space Station (ISS) in the past decade resulted in a surge in research that was not only driven by the goal of developing fundamental understanding of the phenomena, but also by its implication in the development of fire safety protocols, because low-temperature cool-flame combustion cannot be visibly observed. Onboard the ISS, the Multi-User Droplet Combustion Apparatus (MDCA) Combustion Integrated Rack (CIR) was utilized to conduct the isolated droplet work for a range of initial droplet diameters, with different fuels (single component: alcohols, n-alkanes, primary reference fuel (n-heptane + iso-octane)) over a very limited pressure range (0.5-3 atm)... Such observations changed the way fuel combustion is understood and predicted (Nayagam et al. 2012)." "low-temperature \"cool flame\" is self-sustaining for long durations (e.g., up to 40 seconds, depending on the choice of fuel and droplet diameter) (Farouk et al. 2017). Mathematical modeling of FLEX experiments indicates that the observed second-stage burning occurs at temperatures between the turnover temperature and the hot ignition temperature, within the negative temperature coefficient regime, and is driven by the excessive heat loss during the first-stage high-temperature burn." "Reducing emissions and improving fuel efficiency that can be achieved at high pressure by employing low-temperature combustion strategies has served as a primary motivator for cool flame research because homogeneous charge compression ignition (HCCI) and reactivity-controlled compression ignition (RCCI) had demonstrated the application of low-temperature combustion in engines (Dryer 2015; Reitz and Duraisamy 2015)." Potential Research Areas — What aspects of fluid behavior will improve fire safety onboard spacecraft?: "Another important issue is material flammability. The present flammability standard accepted by NASA establishes requirements for evaluation, testing, and selection of materials that are intended for use in space vehicles and associated ground support equipment (GSE). It is a pass/fail ground test, where an upward flame is spread over a material sample. The known drawbacks of such tests are as follows: First, cabin-air conditions onboard spacecraft (pressure, oxygen content) can change. Second, there are at least two factors that are known to change material flammability in microgravity. Natural convection does not occur, and the flow surrounding the flame may be owing to the HVAC system or movement by the astronauts and have a very low and/or irregular velocity. Second, combustion products remain around the area where combustion took place. While some studies of material flammability in microgravity exist-refer, for example, to Fujita (2015) for a summary along with a description of the shortcomings of existing flammability tests-more systematic investigations are essential to improve fire safety relevant to space missions and to develop predictive models and new fire-resistant materials." "Previous testing at microgravity and lunar gravity indicated that some materials burned to lower oxygen concentrations in low gravity than in normal gravity. Similarly, the data obtained under martian gravity conditions also suggested that there is a partial gravity level at which materials burn more readily than on Earth. Flames, especially in microgravity, can also be strongly affected by electromagnetic fields, as preliminary studies show (Chien et al. 2022)." "Ongoing experiments consider a coflow laminar diffusion (CLD) flame (Smooke et al. 1999), where the burning flame is surrounded by laminar flow of the oxidizing gas (e.g., air). In a gravity field, the coflow would be directed upward. In orbit, the velocity of the coflow becomes an important control parameter affecting the flame shape, stability, and burning product generation." Potential Research Areas — Chemical Kinetics and Combustion Processes: "Experiments in microgravity have provided unprecedented insights into chemical kinetic phenomena, highlighting the importance of radiative loss in determining flammability limits, new steady-state regimes of low-temperature and intermediate-temperature fuel burning phenomena (cool and warm flames) and insights into sooting and the formation of large soot agglomerates that has enormous impacts on understanding the effects of wildfires on the environment and applications to material synthesis. Microgravity experiments also demonstrated that electric field and charges (ions and electrons) can also affect the energy transfer, reactions, and flow motion. However, large buoyant flows present in terrestrial laboratories prevent the attainment of the low strain environment necessary to study systems where flame structures or reaction wave fronts are determined by chemical kinetics and motion of charged molecules and particles. Fundamental experiments are necessary for developing predictive tools for chemical kinetics over a range of environments and fuels including biofuels, e-fuels, and low-carbon fuels." "Microgravity studies have shown that large soot agglomerates (super agglomerates) are preferentially formed in microgravity flames where, in the absence of buoyancy, the long residence time necessary for the formation of these structures is easily attained... The low stretch/strain environment is readily attained in reduced gravity studies in the absence of the buoyant flow present in all terrestrial studies. This environment provides the strictest test of chemical kinetic mechanisms, as the flame structure limits are kinetically controlled and not determined by the flow environment, providing insights into the fundamental physics of the processes involved."
