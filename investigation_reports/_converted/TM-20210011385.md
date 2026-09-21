

NASA/TM-20210011385


# Burning and Suppression of Solids-II (BASS-II) Summary Report


Sandra L. Olson
Glenn Research Center, Cleveland, Ohio


Paul V. Ferkul
Universities Space Research Association, Cleveland, Ohio


Subrata Bhattacharjee and Fletcher J. Miller
San Diego State University, San Diego, California


Carlos Fernandez-Pello and Shmuel Link
University of California, Berkeley, Berkeley, California


James S. T'ien
Case Western Reserve University, Cleveland, Ohio


Indrek Wichman
Michigan State University, East Lansing, Michigan


October 2021




## NASA STI Program . . . in Profile


Since its founding, NASA has been dedicated • CONTRACTOR REPORT. Scientific and
to the advancement of aeronautics and space science. technical findings by NASA-sponsored
The NASA Scientific and Technical Information (STI) contractors and grantees.
Program plays a key part in helping NASA maintain
this important role.


• CONFERENCE PUBLICATION. Collected
papers from scientific and technical
conferences, symposia, seminars, or other
meetings sponsored or co-sponsored by NASA.


The NASA STI Program operates under the auspices
of the Agency Chief Information Officer. It collects,
organizes, provides for archiving, and disseminates
NASA's STI. The NASA STI Program provides access
to the NASA Technical Report Server-Registered
(NTRS Reg) and NASA Technical Report Server-
Public (NTRS) thus providing one of the largest
collections of aeronautical and space science STI in
the world. Results are published in both non-NASA
channels and by NASA in the NASA STI Report
Series, which includes the following report types:


- SPECIAL PUBLICATION. Scientific, technical, or historical information from NASA programs, projects, and missions, often concerned with subjects having substantial public interest.

- TECHNICAL TRANSLATION. English- language translations of foreign scientific and technical material pertinent to NASA's mission.


For more information about the NASA STI
program, see the following:


- TECHNICAL PUBLICATION. Reports of completed research or a major significant phase of research that present the results of NASA programs and include extensive data or theoretical analysis. Includes compilations of significant scientific and technical data and information deemed to be of continuing reference value. NASA counter-part of peer-reviewed formal professional papers, but has less stringent limitations on manuscript length and extent of graphic presentations.

- Access the NASA STI program home page at http://www.sti.nasa.gov

- E-mail your question to help@sti.nasa.gov

- Fax your question to the NASA STI Information Desk at 757-864-6500

- Telephone the NASA STI Information Desk at 757-864-9658

- TECHNICAL MEMORANDUM. Scientific and technical findings that are preliminary or of specialized interest, e.g., "quick-release" reports, working papers, and bibliographies that contain minimal annotation. Does not contain extensive analysis.

- Write to: NASA STI Program Mail Stop 148 NASA Langley Research Center Hampton, VA 23681-2199




NASA/TM-20210011385


# Burning and Suppression of Solids-II (BASS-II) Summary Report


Sandra L. Olson
Glenn Research Center, Cleveland, Ohio


Paul V. Ferkul
Universities Space Research Association, Cleveland, Ohio


Subrata Bhattacharjee and Fletcher J. Miller
San Diego State University, San Diego, California


Carlos Fernandez-Pello and Shmuel Link
University of California, Berkeley, Berkeley, California


James S. T'ien
Case Western Reserve University, Cleveland, Ohio


Indrek Wichman
Michigan State University, East Lansing, Michigan


National Aeronautics and
Space Administration


Glenn Research Center
Cleveland, Ohio 44135


October 2021




## Acknowledgments


The authors would like to thank the members of the BASS team who have supported ops and hardware development, especially
Bob Hawersaat, Jay Owens, Tibor Lorik, Chuck Bunnell, and Carol Reynolds. We also want to thank our lab partner Astronauts
Don Pettit, Joe Acaba, Suni Williams, Chris Cassidy, Rich Mastracchio, Reid Wiseman, Alex Gerst, and Tim Kopra for their work
to conduct the experiments on the ISS.


Trade names and trademarks are used in this report for identification
only. Their usage does not constitute an official endorsement,
either expressed or implied, by the National Aeronautics and
Space Administration.


Level of Review: This material has been technically reviewed by technical management.


NASA STI Program
Mail Stop 148
NASA Langley Research Center
Hampton, VA 23681-2199


Available from


National Technical Information Service
5285 Port Royal Road
Springfield, VA 22161


703-605-6000


This report is available in electronic form at http://www.sti.nasa.gov/ and http://ntrs.nasa.gov/




### Contents


Summary ....................................................................................................................................................... 1
Acronyms ............................................................................................................................................. 2
Symbols ................................................................................................................................................ 2


1. Summary of Burning and Suppression of Solids-II Experiments ...................................................... 3 1.1 Background .................................................................................................................................. 3 1.2 Experiment Description ............................................................................................................... 3 1.3 Validation of Microgravity Science Glovebox Dilution-Continuously Stirred Tank Reactor Model ............................................................................................................................. 6 1.4 Combustion Products ................................................................................................................... 6 1.5 Global Equivalence Ratio .......................................................................................................... 10 1.6 Overall Conclusions ................................................................................................................... 11 1.7 Acknowledgments ..................................................................................................................... 11 1.8 References.................................................................................................................................. 12

2. Individual Principal Investigator Report: Bhattacharjee .................................................................... 13 2.1 Residence Time Driven Flame Spread ...................................................................................... 13 2.1.1 Test Matrix ...................................................................................................................... 13 2.1.2 Results ............................................................................................................................. 13 2.1.3 Concluding Remarks ....................................................................................................... 17 2.1.4 References ....................................................................................................................... 17 2.1.5 Publications Resulting from This Work .......................................................................... 17 2.2 Critical Flow Velocity for Radiative Extinction in Opposed-Flow Flame Spread in Microgravity Environment: Comparison of Experimental, Computational, and Theoretical Results .................................................................................................................... 19 2.2.1 Abstract ........................................................................................................................... 19 2.2.2 Introduction ..................................................................................................................... 20 2.2.3 Experimental Setup ......................................................................................................... 21 2.2.4 Data Analysis .................................................................................................................. 22 2.2.5 Extinction Velocity ......................................................................................................... 23 2.2.6 Computational Results .................................................................................................... 25 2.2.7 Scale Analysis: Expression for Extinction Velocity Vg,cr ................................................ 26 2.2.8 Conclusions ..................................................................................................................... 28 2.2.9 Acknowledgment ............................................................................................................ 28 2.2.10 References ....................................................................................................................... 29 2.3 Opposed-Flow Flame Spread: Comparison of Microgravity and Normal-Gravity Experiments to Establish Thermal Regime ............................................................................... 31 2.3.1 Abstract ........................................................................................................................... 31 2.3.2 Introduction ..................................................................................................................... 32 2.3.3 Scale Analysis ................................................................................................................. 33 2.3.4 Onset of Kinetic Effect ................................................................................................... 36 2.3.5 Microgravity and Normal-Gravity Experiments ............................................................. 37 2.3.6 Data Analysis .................................................................................................................. 39 2.3.7 Results and Discussion.................................................................................................... 40 2.3.8 Conclusion ...................................................................................................................... 43 2.3.9 Acknowledgment ............................................................................................................ 44


NASA/TM-20210011385 iii




1. References ....................................................................................................................... 44

2. Project Scientist Report: Ferkul .......................................................................................................... 46 3.1 Nomex® Flammability ............................................................................................................... 46 3.1.1 Results ............................................................................................................................. 46

3. Individual Principal Investigator Report: Fernandez-Pello ................................................................ 47 4.1 Opposed-Flame Spread Task ..................................................................................................... 47 4.1.1 Experiment and Test Matrix ........................................................................................... 47 4.1.2 Results ............................................................................................................................. 48 4.1.3 References ....................................................................................................................... 53 5.0 Individual Principal Investigator Report: Miller and Wichman ......................................................... 55 5.1 Narrow Channel Apparatus as Microgravity Flame Spread Surrogate...................................... 55 5.2 Introduction................................................................................................................................ 55 5.3 Experimental Setup and Summary ............................................................................................ 56 5.4 Oxygen Concentration Analysis ................................................................................................ 60 5.5 Numerical Modeling .................................................................................................................. 60 5.6 Experimental and Modeling Results .......................................................................................... 61 5.7 Conclusions................................................................................................................................ 63 5.8 Acknowledgments ..................................................................................................................... 63 5.9 References.................................................................................................................................. 63 6.0 Individual Principal Investigator Report: Olson ................................................................................. 64 6.1 Microgravity Flammability Boundary for Polymethylmethacrylate Rods In Axial Stagnation Flow: Experimental Results and Energy Balance Analyses .................................... 64 6.1.1 Abstract ........................................................................................................................... 64 6.1.2 Introduction ..................................................................................................................... 65 6.1.3 Experimental Setup ......................................................................................................... 66 6.1.4 Experimental Results ...................................................................................................... 68 6.1.5 Analyses .......................................................................................................................... 81 6.1.6 Conclusions ..................................................................................................................... 89 6.1.7 Acknowledgments ........................................................................................................... 90 6.1.8 References ....................................................................................................................... 90 6.1.9 Primary Microgravity and Normal-Gravity Research Citations for This Project ........... 92 7.0 Individual Principal Investigator Report: T'ien .................................................................................. 93 7.1 Concurrent Flame Growth, Spread, and Extinction Over Composite Fabric Samples in Low-Speed Purely Forced Flow in Microgravity ...................................................................... 93 7.1.1 Abstract ........................................................................................................................... 93 7.1.2 Introduction ..................................................................................................................... 93 7.1.3 Experimental ................................................................................................................... 94 7.1.4 Results and Discussion.................................................................................................... 95 7.1.5 Conclusions ................................................................................................................... 101 7.1.6 References ..................................................................................................................... 101 Appendix A.-Test Matrices for Burning and Suppression Solids-II (BASS-II) ..................................... 103 A.1 Bhattacharjee Test Matrix ........................................................................................................ 103 A.2 Ferkul Test Matrix ................................................................................................................... 105 A.3 Fernandez-Pello Test Matrix ................................................................................................... 106 A.4 Miller Test Matrix .................................................................................................................... 108 A.5 Olson Test Matrix .................................................................................................................... 110


NASA/TM-20210011385 iv




1. T'ien Test Matrix ..................................................................................................................... 112


Appendix B.-Microgravity Science Glovebox Work Volume Nitrogen Dilution Continuously
Stirred Tank Reactor Model and On-Orbit Verification Testing of Model ..................................... 115


1. Symbols ................................................................................................................................... 115


B.2 Information .............................................................................................................................. 115


B.3 References................................................................................................................................ 117


Appendix C.-List of Preflight, In-flight, and Postflight Anomalies ....................................................... 119
Appendix D.-Heat Release Rate and Hardware Temperature Rise Estimates for Burning and
Suppression of Solids-II Thick Polymethylmethacrylate Slab Samples ........................................ 121


1. Symbols ................................................................................................................................... 121


D.2 Introduction.............................................................................................................................. 121


1. Purpose of the Analysis ........................................................................................................... 121


D.4 Background .............................................................................................................................. 122


1. Analysis ................................................................................................................................... 122


D.6 References................................................................................................................................ 126


D.7 Appendix-Polymethylmethacrylate Growth to Steady Size .................................................. 127


Appendix E.-Burning and Suppression Solids (BASS) and BASS-II Papers and Presentations .......... 129


NASA/TM-20210011385 v






#### Burning and Suppression of Solids-II (BASS-II) Summary Report


Sandra L. Olson
National Aeronautics and Space Administration
Glenn Research Center
Cleveland, Ohio 44135


Paul V. Ferkul
Universities Space Research Association
Cleveland, Ohio 44135


Subrata Bhattacharjee and Fletcher J. Miller
San Diego State University
San Diego, California 92182


Carlos Fernandez-Pello and Shmuel Link
University of California, Berkeley
Berkeley, California 94720


James S. T'ien
Case Western Reserve University
Cleveland, Ohio 44106


Indrek Wichman
Michigan State University
East Lansing, Michigan 48824


##### Summary


The Burning and Suppression of Solids (BASS) experiment hardware is a small flow duct that
provides containment for small scale burning of solid samples within the Microgravity Science Glovebox
(MSG) aboard the International Space Station (ISS). A video camera with a data overlay and a 35-mm
still camera record the combustion events. The controls (ignition, fan speed, etc.) are operated by an
astronaut while the principal investigator team monitors the experiment from the ground and
communicates directly with the astronaut. For the first time on ISS, BASS-II utilized MSG working
volume dilution with gaseous N2. We developed a perfectly stirred reactor model to determine the N2 flow
time and flow rate to obtain the desired reduced O2 concentration in the working volume for each test. We
calibrated the model with the Compound Specific Analyzer-Combustion Products (CSA-CP) O2 readings
offset using the Major Constituents Analyzer reading of the ISS ambient atmosphere data for that day.
This worked out extremely well for operations, and added a new vital variable, ambient O2 level, to our
test matrices. The main variables tested in BASS-II were ambient O2 concentration, ventilation flow
velocity, and fuel type, thickness, and geometry. BASS-II also utilized the onboard CSA-CP for O2 and
CO readings, and the Carbon Dioxide Monitor for CO2 readings before and after each test. Readings from
these sensors allow us to evaluate the completeness of the combustion. The O2 and CO2 readings before


NASA/TM-20210011385 1




and after each test were analyzed and compared very well to stoichiometric ratios for a one-step gas-phase
reaction. The CO versus CO2 followed a linear trend for some datasets, but not for all the different
geometries of fuel and flow tested. We calculated the heat release rates during each test from the O2
consumption and burn times, using the constant 13.1 kJ of heat released per gram of O2 consumed. The
results showed that most of the tests had heat release rates well below 100 W. Lastly, the global
equivalence ratio for the tests is estimated to be fuel rich, 1.3 on average using mass loss and O2
consumption data.


##### Acronyms


1D one dimensional
2D two dimensional
3D three dimensional
BASS-II Burning and Suppression of Solids-II experiment in the MSG aboard ISS (Refs. 1 to 3)
CDM Carbon Dioxide Monitor, sensor aboard ISS (CO2) (Ref. 4)
CSA-CP Compound Specific Analyzer-Combustion Products, sensor aboard ISS (O2, CO, and others)
(Refs. 5 and 6)
CSTR continuously stirred tank reactor
DNS direct numerical simulation
FDS fire dynamic simulator
GMT Greenwich Mean Time, standard time on ISS
GN2 Gaseous nitrogen
HDPE high-density polyethylene
HRR heat release rate, W
ISS International Space Station
LPM liters per minute
MCA Major Constituents Analyzer, a mass spectrometer-based system that measures the major
atmospheric constituents on ISS, calibrated O2 reference (Refs. 7 and 8)
MSG Microgravity Science Glovebox, a facility aboard ISS (Ref. 9)
NCA narrow channel apparatus
NIST National Institute of Standards and Technology
PMMA polymethylmethacrylate (acrylic)
RGB red green blue
RTD resistance thermal detector
RTDFS Residence Time Driven Flame Spread
SDSU San Diego State University
SIBAL Solid Inflammability Boundary at Low Speeds
SMAC spacecraft maximum allowable concentration


##### Symbols


P pressure
R gas constant; 82.05 cc∙atm/gmol∙K
T temperature
V volume of MSG working volume, 0.25 m3
r flow rate of gaseous N2, 0.0005 m3/min maximum, adjustable
t time
Φglobal global equivalence ratio, Equation (1.2)


NASA/TM-20210011385 2




### 1.0 Summary of Burning and Suppression of Solids-II Experiments


The first section of the report provides an overview of the experiment operations and results. Each of
the five principal investigators (PIs) for Burning and Suppression of Solids-II (BASS-II), in
alphabetical order, have summarized their research in separate sections of this report. Appendix A
includes test matrices from each PI, Appendix B describes the dilution model and verification testing,
Appendix C describes the anomalies encountered, Appendix D describes a thermal analysis, while
Appendix E contains the BASS and BASS-II current papers and presentations created through the
summer of 2020.


#### 1.1 Background


BASS-II tests the hypothesis that materials in microgravity, with adequate ventilation, burn as well if
not better than the same material in normal gravity with other conditions being identical (pressure, O2
concentration, temperature, etc.). NASA tests and controls materials from a flammability perspective
using an upward burning test in normal gravity, which is considered to be the worst-case geometry for
flammability of the material on Earth. However, it may not be conservative for flammability in space.
One objective of the BASS-II tests is to identify what is the worst case for material flammability in
spacecraft environments, and how does that compare to the terrestrial upward burning used to screen the
materials for safe use aboard spacecraft.
Detailed combustion models can be validated by data obtained in the simpler flow environment in
microgravity. Once validated, they can be used to build more complex combustion models needed to
capture the important details of flames burning in normal gravity. These models have wide applicability
to the general understanding of many terrestrial combustion problems.
The main variables tested were the effects of ambient O2 concentration, ventilation flow velocity, and
fuel type, thickness, and geometry. Many of the tests focused on finding a minimum O2 concentration or
flow velocity where a material will burn in space, to compare with the Earth-based limits. Flame growth
rates are also of interest, to determine how quickly a fire in space can grow and if the flames reach a finite
size or continue to grow. This has implications for firefighting strategies in spacecraft.
BASS-II utilized the gaseous nitrogen (GN2) available on International Space Station (ISS) to vitiate
the atmosphere in the Microgravity Science Glovebox (MSG) from standard ISS "air" down to the low O2
flammability limits. BASS-II also utilized onboard O2, CO, and CO2 sensors to evaluate the completeness
of the combustion.
A total of 126 tests were conducted as part of BASS-II. This is more than the planned 103 tests, since
some samples were burned more than once. There are some samples that could be burned further, should
future operational time become available.
For the first time on ISS, BASS-II utilized MSG working volume vitiation with GN2. We developed
a perfectly stirred reactor model to determine the GN2 flow time and flow rate to obtain the desired
reduced O2 concentration in the working volume for the tests. This worked out extremely well for
operations, and added a new vital variable, ambient O2 level, to our test matrices.


#### 1.2 Experiment Description


The MSG in the Destiny Lab of the ISS provides a contained atmosphere in which fire safety
experiments can be conducted (Ref. 9). The MSG, shown in Figure 1.1, has a set of filter banks that
capture particulates and convert the CO to CO2 using an ambient temperature catalyst. The BASS-II
hardware is shown inside the MSG working volume in Figure 1.1.


NASA/TM-20210011385 3




Figure 1.1.-Microgravity Science Glovebox Facility (MSG) working volume aboard the
International Space Station (ISS) with the Burning and Suppression of Solids-II (BASS-


II) experiment hardware installed. Working volume of MSG was diluted using ISS N2 gas.
Compound Specific Analyzer-Combustion Products (O2 and CO) and Carbon Dioxide


Monitor (CO2) sensors were used to obtain before and after burn gas concentrations.


The BASS-II hardware consists of a flow duct, still camera, video camera, video and power boxes,
external control box and associated plumbing, and mounting systems. The black anodized 7.6- by 7.6- by


17-cm rectangular flow duct with rounded corners was originally built to perform gas jet diffusion flame


studies (Ref. 10). It was adapted to accommodate solid samples for the BASS experiments.
The flow was blown through the duct using a variable speed fan. Two additional flow restrictors
could be used at the fan inlet to increase the pressure drop and thus reduce the flow through the duct to
the desired value for the test point. With no restrictors, the maximum flow velocity was ~55 cm/s, and
with two restrictors this was reduced to ~35 cm/s. The flow then passed through a honeycomb flow
straightener and an inlet screen to reduce swirl. An omnidirectional spherical airspeed transducer (TSI
Incorporated 8475) was positioned between the honeycomb and the screen and was used to measure the
steady-state flow through the duct. The air velocity transducer probe had a response time of
approximately 1 minute.
The test section was 17 cm long. Inside the test section was a nozzle for N2 flow, a movable scale,
and an Oriel® 71768 thermopile detector (Newport Corporation) with a CaFl window (spectral range of
0.13 to 11 µm) in the downstream top back corner of the duct viewing the upstream direction. The test
section of the duct had two orthogonal windows; the top one was replaced for BASS to provide a
mounting rail system for the solid samples. The top window was used by a Nikon D300s 12.3-megapixel
digital color still camera with a 60-mm lens that provided 4,320- by 2,968-pixel images. The duct exit
contained a perforated copper plate followed by a brass screen to provide heat rejection and a cold surface
for soot deposition. The flow turned 90° to exit the duct, which facilitated mixing of the hot combustion
gases with the cool ambient air.
The front window opened to provide access to the test section for sample and igniter change out. The
front window also had interlocks for the igniter and N2 flow. A Panasonic Corporation color video camera


NASA/TM-20210011385 4




WV-CP654 (760- by 480-pixel array) with a turning mirror looked in the front window. The video
camera had an overlay that displayed the N2 flow rate (cm3/min), fan voltage (10× V), air velocity
transducer reading (cm/s), and the radiometer signal. The fan voltage was calibrated with the airspeed
transducer at the end of every operations day. The radiometer signal was not calibrated but provided a
measure of the flame dynamics and steadiness. The external control box had controls for the fan voltage,
N2 flow rate, enable switches for the igniter and N2 flow, and a radiometer gain level setting.
A number of sample geometries were used in BASS-II: cast polymethylmethacrylate (PMMA)
samples were shaped as rods of various diameters (6.35 to 12.7 mm), thin to thick slabs (0.125 to 5 mm),
or a section of a 4-cm-diameter sphere. In addition, flat cotton-fiberglass blended fabric samples were
also burned. These samples could generally be mounted so that they could be burned in either the opposed
or concurrent flow direction. The flat samples were 1 or 2 cm wide. The samples were manually ignited
with a Kanthal® A-1 29-gauge hot-wire igniter coil with a nominal hot wire resistance of 0.8 to 1 Ω,
powered by 3.5 to 3.8 amps when the astronaut manually pulled the deployment lever to move the igniter
into position. Samples were burned within the duct and the combustion products exited the duct and
mixed with the gas in the work volume. Example flame images are shown in Figure 1.2. Samples were
returned to Earth and evaluated for mass loss.
To evaluate the levels of combustion products produced during microgravity fires, BASS-II
requested the use of available onboard sensors to measure the O2 depletion and the completeness of
combustion (CO and CO2) for microgravity combustion tests under spacecraft ventilation flow rates to
provide scientific data on the stoichiometry of the diffusion flame reactions and heat release rates
(HHRs). The data reported here is the first extensive data on the stoichiometry and toxicity of combustion
products in microgravity.


Figure 1.2.-Flame geometries tested in Burning and Suppression of Solids-II
(BASS-II). Sample images from different geometries: (a) opposed thin slab,


(b) spherical section, (c) opposed rod higher flow, (d) flat fabric sample at


higher flow, (e) opposed thick slab, (f) concurrent rod, (g) opposed rod at low
flow with open tip (similar to concurrent rod), and (h) flat fabric sample at low
flow. Forced flow is up in all images.


NASA/TM-20210011385 5




The O2, CO2, and CO measurements required two portable, battery powered instruments in the
working volume during testing: Carbon Dioxide Monitor (CDM), and Compound Specific Analyzer-


Combustion Products (CSA-CP) (Refs. 3 to 5). The O2 sensor (CSA-CP) is not recalibrated on orbit, so
we also used the Major Constituents Analyzer (MCA) (Refs. 6 and 7) data to determine the O2 sensor
offset on a daily basis. The resolution of the O2 sensor in the CSA-CP was 0.1 percent O2. O2
concentrations in the MSG working volume were varied during the testing from ambient ISS O2 levels
(~21 percent O2) down to ~14 percent O2 for very near limit flames. The CO sensor in the CSA-CP is
zero calibrated every 60 days, with a range of 0 to 1,000 ppm and a resolution of 1 ppm. The CO2 sensor
was within its calibration window and had a range of 0 to 5 percent and a resolution of 0.1 percent by
volume of CO2. The sensor data provided initial and final conditions for repeated tests in a sealed working
volume and allowed us to determine when the working volume needed to be purged. The O2 decreased
during each burn and the CO and CO2 increased accordingly.
Many of the BASS-II tests required a diluted atmosphere, which typically took 1 to 3 h to achieve by
dilution of the MSG working volume using ISS N2 (from the hose connecting the BASS-II duct to the
back wall of MSG in Figure 1.1). The N2 was regulated with a small (<0.5 liters per minute (LPM)) MKS
Instruments 179A mass flowmeter and entered the flow duct through a small nozzle just downstream of
the fan. The fan in the flow duct was turned to maximum (>100 LPM) during the N2 flow to mix and
blow the gas into the working volume and circulate it continuously throughout the hours-long dilution.


#### 1.3 Validation of Microgravity Science Glovebox Dilution-Continuously Stirred Tank Reactor Model


To utilize the capabilities of MSG to reduce the O2 in the working volume in a controlled manner, a
dilution model based on a continuously stirred tank reactor (CSTR) model was developed. In this model,
the mixing in the working volume (via the BASS-II duct fan) is assumed to be "instantaneous," so that
the outflow "leak" concentration from the MSG work volume to the ISS cabin is the perfectly mixed
instantaneous concentration. This perfect mixing approximation is valid as long as the residence time
(volume per flow rate or V/R) is at least 5 to 10 times as long as the mixing time, which is met by the
100 LPM N2 flow rate during dilution (250 liters/100 LPM ~ 2.5 min mixing time). For the MSG volume
and N2 flow rates, the working volume residence time is V/R = 500+ min, and the mixing time is shorter
than 50 min, so the assumption is valid. The model assumes the work volume is at constant pressure and
temperature and constant volume. Thus, the leak rate out of the work volume is equal to the rate of N2
supplied (r). The details of the model and the on-orbit validation testing using the Major Constituents
Analyzer (MCA) (Ref. 11) are provided in Appendix B.


#### 1.4 Combustion Products


Sensor readings were taken before and after each BASS-II test. The sensor data is used to measure
the O2 depletion and the completeness of combustion (CO and CO2) for each microgravity combustion
test under spacecraft ventilation flow rates.
The O2 depletion data is compared to the CO2 production for each BASS-II test that used PMMA as
the fuel.
The PMMA stoichiometric equation is


C5H8O2 + 6 O2 > 5 CO2 + 4 H2O (1.1)


NASA/TM-20210011385 6




The data, taken over a wide range of initial O2 concentrations, forced opposed or concurrent flow
velocities, and using various sample geometries, is compared with this 6:5 stoichiometric ratio of O2 to
CO2 in Figure 1.3. As shown, the data agrees very well with stoichiometric ratios for the wide range of
test conditions.
Other than unburned fuel (primarily methylmethacrylate vapor), which does contain some O2 as
shown in Equation (1.4), the only other (nontrace quantity) potential species with O2 is CO, which was
also measured, as shown in Figure 1.4 to Figure 1.6. Figure 1.4 shows that the concurrent rods produced
on average 550 ppm of CO for every 1 percent of CO2. The opposed rods had a very nonlinear response,
which may be indicative of a flow effect.
The longer the burn, the more CO2 was formed, and the nominal test procedure for most samples was
to turn the flow down in increments. At very low velocities, the tail region of the opposed-flow flames
opened up, which presumably allowed incomplete combustion products to escape the flame zone.
Interestingly, the concurrent procedure was very similar, but the concurrent flame always had an open
tail, allowing incomplete combustion products to exit throughout the burn. The opposed thick slabs fall
somewhere in between, producing on average 370 ppm of CO for every 1 percent of CO2.
The one outlier point from Figure 1.3 at 2.8 percent CO2 is not included in Figure 1.4 since the CO
sensor was over-ranged for this test (>1,000 ppm full scale), so we have no quantitative value for CO for
this test. During this test, the long burn of the relatively strong flame caused overheat damage to the
downstream lower corner of the front window in the area where a flow duct leak was occurring. The leak
was repaired on orbit, and operations proceeded without further incident.


Figure 1.3.-O2 depletion and CO2 production during Burning and
Suppression of Solids-II (BASS-II) tests with polymethylmethacrylate
fuel. Data from different geometries, flows, and initial O2 concentrations
all agree with expected stoichiometric trend (shown by dashed line).


NASA/TM-20210011385 7




Figure 1.4.-CO generated compared to CO2 generated in each test. CO
generated appears to be clustered by geometric and flow configurations.
Concurrent rod geometry produced most CO per CO2, and opposed rods
showed very nonlinear trend of CO versus CO2 production. Thick opposed-flow
slabs fell in between the two.


Of interest to the combustion community is the ratio of CO to CO2, a measure of completeness of
combustion, which is plotted in Figure 1.5 as a function of the initial O2 concentration in the working
volume. For efficiently burned flue gases (boilers, furnaces, etc.), this ratio is typically less than 0.004. As
can be seen, most of our data is well above that, indicating that microgravity flames are comparatively
inefficient. A similarly sized smoldering event would produce significantly more CO. On the Mir space
station, a smoldering carbon bed in the Trace Contaminant Control System caused very high CO levels
throughout the space station before it was detected.
Although the absolute values of CO are very high in the 250-L MSG free working volume, the MSG
contained and converted the CO to CO2 during the posttest work volume purge. Since the ISS is quite
large, the combustion products from a fire of the scale of a BASS-II test would quickly be diluted, so that
even within just the U.S. Lab (106-m3 pressurized volume), the CO levels in the lab would only be


1.5 ppm, well below spacecraft maximum allowable concentration (SMAC) values for even long-term


exposure (10 ppm), let alone the 1 hour SMAC of 55 ppm (Ref. 12).
Lastly, the HRRs from these small microgravity fires can be estimated using Huggett's O2
consumption calorimetry (Ref. 13) and the burn time for each test. Using his constant of 13.1 kJ/g O2, we
estimate the HRRs to be typically well below 100 W, as shown in Figure 1.6. There is a trend of
increasing HRR with increasing ambient O2 concentration, and the scatter is attributed to the different
duct flows between and even within the tests.
The one long opposed thick slab test that caused the lower downstream corner of the front window
damage released close to 100 W. A prior relatively brief concurrent rod test that released almost 110 W
did not cause any damage.


NASA/TM-20210011385 8




Figure 1.5.-CO to CO2 ratio as function of initial O2 concentration for
each test. There is some clustering apparent in data, which shows
that lower O2 concentrations produce higher levels of CO per CO2
for concurrent rods, especially when compared to opposed rods,
which show opposite trend. Opposed slab data has similar trend to
concurrent rod data, although scatter is large.


Figure 1.6.-Heat release rate (HRR) during each test using O2
consumption calorimetry. Data from Figure 1.3 is converted to watts
using burn time and Huggett's constant, plotted against initial O2,
showing HRR generally increases with increasing ambient O2
concentration. Magnitude of HRR is modest for these small flames
under conditions tested.


NASA/TM-20210011385 9




Figure 1.7.-O2 consumed, CO2 and CO generated per gram of fuel mass loss
for two different fuels tested (cellulose (small circles) and
polymethylmethacrylate (large circles)).


#### 1.5 Global Equivalence Ratio


To date, 34 burned BASS-II samples have been returned to Earth for postflight analysis. Eight of
those samples had been used for multiple tests and were altered on orbit by having their burned fuel cut
off and/or their built-in igniter leads removed. As a result, the preflight and postflight weights for these
modified samples cannot be used to determine the mass loss due to combustion. Also, seven additional
samples had burns that were so short that no O2 consumption was measured, so are not usable for the
global equivalence ratio estimates.
For the remaining 19 samples, mass loss is compared to O2 consumption, as shown in Figure 1.7.
There are clear trends observed for O2 consumption and CO2 generation relative to measured fuel
mass loss. Given the previous stoichiometric relation between O2 and CO2, it is not surprising that the two
trends mirror each other. The CO data is more scattered, but CO generation generally increases with
increasing fuel mass loss and O2 consumption. The 7-g fuel mass loss test had over 1,000 ppm of CO
(above the range of the sensor).
We can evaluate the fuel to O2 ratio based upon these test results. The global equivalence ratio Φglobal
can be expressed for either cellulose or PMMA fuel stoichiometry as


gm olfuel
gmol


- = O2 1 6

- Φ (1.2)

- global


NASA/TM-20210011385 10




Using the ideal gas law, the free volume of the MSG V = 250,000 cc, ideal gas constant
R = 82.05 cc∙atm/gmol K, pressure P = 1 atm, the change of O2 percent volume, and temperature
T = 300 K, the gmol of O2 consumed is calculated as


 ∆O2 vol%


1 250,000 

PV 100 


=


RT 82.05 ⋅300


gm olO2 consumed =


The gmol of fuel consumed is simply:


(1.3)


gm olfuel = (1.4)


grams of fuel
molecular weight


Using the observed slope of 0.4582 O2 vol% per gram of fuel, and the molecular weight for PMMA
of 100 g/gmol for the majority of the data, we can use the above equations to solve for the effective
equivalence ratio for the tests: Φglobal = 1.3, which is fuel rich. So, in general, the flames were under-
ventilated and did not burn all of the vaporized fuel. Some fuel ended up as soot, some as CO, and some
as unburned hydrocarbons.


#### 1.6 Overall Conclusions


As part of the Burning and Suppression of Solids-II (BASS-II) experiment, we conducted a number
of tests with different geometries, flow velocities, and initial O2 concentrations. The last variable was
enabled using gaseous N2 to dilute the working volume. To adequately characterize this dilution, we
developed a continuously stirred tank reactor model and verified it against sensor readings.
Sensor data from the tests showed that the O2 was burning nearly stoichiometrically to CO2, and that
CO levels appear to be a function of geometry and, in some cases, the flow velocity and geometry
combination. The CO to CO2 ratios for these fires are an order of magnitude higher than for efficient flue
gases, indicating that these flames are not efficient. The heat release was estimated for the tests using O2
consumption calorimetry. This showed that most of the tests released well below 100 W. In the one long
test that released close to 100 W, we sustained some damage to the downstream corner of the front
window, due to a leak that directed the heat from this energetic flame to that location during the
prolonged burn. Using the mass loss and O2 consumption data, the global equivalence ratio for the tests is
estimated to be 1.3 on average, which indicates the flames were burning fuel rich under the low-velocity
forced-flow conditions.


#### 1.7 Acknowledgments


We want to acknowledge the invaluable assistance of the International Space Station crew in
obtaining these research results. Their meticulous operation and observations during the testing
contributed significantly to the quality and quantity of the results. Rick Mastracchio made an excellent
repair to the door that maintained the door seal integrity and interlock switch functionality throughout the
rest of the Burning and Suppression of Solids-II (BASS-II) operations. Alex Gerst and Reid Wiseman
repaired the video cable to provide the critical video overlay data only obtainable with that camera.
The crew was able to observe and describe some transient phenomena during ignition attempts and
near extinction that we could not observe on the ground, and they were able to adapt to new flow
variations such as blowoff extinctions, that proved to be very valuable data in outlining the U-shaped
flammability boundary.


NASA/TM-20210011385 11




This work could not have been done without the intense efforts of the BASS operations team (Jay
Owens, Chuck Bunnell, Tibor Lorik, and Carol Reynolds). We also want to acknowledge the ground
support teams at Glenn Research Center, Johnson Space Center, and Marshall Space Flight Center
(especially the Microgravity Science Glovebox team) that supported the BASS-II operations and assisted
in the anomaly resolutions.


#### 1.8 References


1. Olson, S.L., et al.: Burning and Suppression of Solids-II Fire Safety Investigation for the Microgravity Science Glovebox. Presented at the 29th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR) and the 5th International Symposium on Physical Sciences in Space (ISPS), Orlando, FL, 2013. https://www.researchgate.net/publication/265684820_Burning_and_Suppression_of_Solids_- _II_Fire_Safety_Investigation_for_the_Microgravity_Science_Glovebox Accessed June 17, 2021.

2. National Aeronautics and Space Administration: Burning and Suppression of Solids-II. Space Station Research Explorer on NASA.gov. http://www.nasa.gov/mission_pages/station/research/experiments/1262.html Accessed June 16, 2021.

3. National Aeronautics and Space Administration: Burning and Suppression of Solids. Space Station Research Explorer on NASA.gov. http://www.nasa.gov/mission_pages/station/research/experiments/735.html Accessed June 17, 2021.

4. Limero, Thomas; Beck, Steve; and James, John T.: Evaluation of a Portable Carbon Dioxide Monitor for Use Aboard the International Space Station. SAE Technical Paper 2000-01-2433, 2000.

5. Limero, Thomas; Beck, Steve; and James, John T.: Development and Performance of the Oxygen Sensor in the CSA-CP Aboard the International Space Station. SAE Technical Paper 2004-01-2337, 2004. 6. Limero, Thomas; Beck, Steve W.; and James, John T.: The Portable Monitor for Measuring Combustion Products Aboard the International Space Station. SAE Technical Paper 2002-01-2298, 2002. 7. Steiner, G., et al.: Assessment of the Major Constituent Analyzer. SAE Technical Paper 2005-01- 2893, 2005. 8. Reysa, R., et al.: International Space Station (ISS) Major Constituent Analyzer (MCA) On-Orbit Performance. SAE Technical Paper 2004-01-2546, 2004.


9. Spivey, Reggie A.; Sheredy, William A.; and Flores, Ginger: An Overview of the Microgravity
Science Glovebox (MSG) Facility, and the Gravity-Dependent Phenomena Research Performed in the
MSG on the International Space Station (ISS). AIAA 2008-812, 2008.


1. Dotson, K.T., et al.: Laminar Smoke Points of Coflowing Flames in Microgravity. Fire Saf. J., vol. 46, 2011, pp. 550-555.

2. Mass Constituents data from ISS, data available online at https://mod2.jsc.nasa.gov/di/di52/constituentmonitor/

3. National Aeronautics and Space Administration: Spacecraft Maximum Allowable Concentrations for Airborne Contaminants. JSC 20584, 1999.

4. Huggett, Clayton: Estimation of Rate of Heat Release by Means of Oxygen Consumption Measurements. Fire Mater., vol. 4, no. 2, 1980, pp. 61-65.


NASA/TM-20210011385 12




### 2.0 Individual Principal Investigator Report: Bhattacharjee


#### 2.1 Residence Time Driven Flame Spread


The objective of the Residence Time Driven Flame Spread (RTDFS) experiment of Burning and
Suppression of Solids-II (BASS-II) was to examine how thermal and species fields can diverge and lead
to microgravity flame extinguishment by varying fuel thickness.


#### Symbols


t time, s
Vg opposed-flow


velocity


#### 2.1.1 Test Matrix


Samples were 1- and 2-cm-wide thin films of plastic (PMMA (polymethylmethacrylate)).
Thicknesses were between 0.1 and 0.4 mm. The test matrix is listed in Appendix A.


#### 2.1.2 Results


Twenty-two test points were obtained with the BASS-II experiments. The wealth of data has been
catalogued at http://flame.sdsu.edu.


#### 2.1.2.1 Extinction Velocity


Each test is started by establishing a steady flame spread in the presence of a forced flow and then
reducing the flow velocity in a gradual manner, as shown in Figure 2.1. In the first test, a steady flame
was established over a 100-μm sample. After the flame propagated across half the sample length at a
steady spread rate of 2.2 mm/s, the flow was abruptly cut off and the flame was observed to extinguish
within 2 s, as shown by the radiometer signal drop in Figure 2.2. To pin down the extinction flow
velocity, a second test was done under the same conditions except the flow velocity was set at 3 cm/s and
after the flame propagated about half the sample length, the flow was gradually reduced. The flame
spread rate of the leading edge, as plotted in Figure 2.3, shows that the flame extinguishes at about 30 s
after ignition. The fan voltage at that time indicates a flow velocity of about 1.1 cm/s. The sequence of
images in Figure 2.1 shows the pathway to radiative extinction. As the flow speed is gradually reduced
from about t = 27 s, the flame size starts shrinking and the orange color disappears and the flame becomes
completely blue, most possibly because of the temperature drop brought about by radiative losses, which
is enhanced by the increased residence time at low flow velocity. The signal from the radiometer, shown
in Figure 2.2, is also consistent with a cooling and shrinking flame as the signal starts decreasing from
right about t = 27 s. After t = 30 s, there is no visible flame and the radiometer data (Figure 2.2) indicate a
sudden change in slope at that time, possibly because the radiation is emitted mostly by the sample holder
with the combustion products swept away by the flow.
When tests are repeated with samples of different thicknesses, the extinction velocities are found to
be about 1 cm/s for 100, 200, and 300 μm and about 1.5 cm/s for 400 μm. At all these thicknesses, the
fuel can be considered thermally thin because the maximum spread rate was found to be inversely
proportional to fuel thickness (Ref. 1), a hallmark of a thermally thin regime. However, it must be
mentioned that there are significant uncertainties in these values as the calibration at such low velocity
has high error bars. The boundary layer formed by the fuel and the tunnel walls would influence the flow
velocity seen by the flame. Also, there is a time lag between when the velocity is reduced and when the
reduced velocity reaches the flame. However, we assume that the time lag works the same way when the


NASA/TM-20210011385 13




Figure 2.1.-Flame images as function of opposed-
flow velocity Vg during radiative extinction.


(a) Time (t) = 27 s; Vg = 3.0 cm/s. (b) t = 28 s;


Vg = 1.5 cm/s. (c) t = 29 s; Vg = 1.1 cm/s.


(d) t = 30 s; Vg = 1.1 cm/s.


Figure 2.2.-Radiometer signal for entire duration of test. Discontinuity at time


(t) = 30 s coincides with disappearance of visible flame.


NASA/TM-20210011385 14




Figure 2.3.-Flame spread rate obtained by tracking leading edge and location of
peak intensity.


fuel thickness is changed. When a few of these tests were repeated, the results were very similar. It can be
safely concluded that the extinction velocity does not depend on the fuel thickness. Tests were also
conducted at a lower O2 level of about 16 percent for two different thicknesses and the extinction
velocities were found to be about 2.6 cm/s for 100 μm and about 4 cm/s for 200 μm. It should be
mentioned that the width of the sample was different, 20 mm for the 100-μm sample and 10 mm for the


200-μm sample. Even though there is insufficient data at the lower O2 level, it is clear that the extinction


velocity significantly increases as the O2 level is reduced and is independent of the fuel thickness.


#### 2.1.2.2 Complementary Normal-Gravity Data


RTDFS acquired further ground data from the San Diego State University (SDSU) flame stabilizer on
downward flame spread over PMMA (with thickness varying from the thin to the thick regime). The results
were compared with data obtained from the BASS-II experiments. A manuscript written on this comparison
was published in the Fire Safety Journal. The manuscript is included in its entirety in Section 2.3.
SDSU Flame Tunnel-While the flame stabilizer is ideal for experiments with downward spreading
flame (Ref. 2), it is difficult to create a forced opposed flow, given the diagnostic probes around the setup.
The flame tower (Ref. 3) helps create an opposing (or concurrent) flow by moving the sample. However,
given the fixed height (8 m) of the tower, the total time available is inversely proportional to the relative
flow created; therefore, sufficient time is not available to study flame extinction due to blowoff.
The SDSU vertical flame tunnel (see Figure 2.4) has a cross section of 10 by 10 cm, similar to the
combustion tunnel used by Hirano (Ref. 4) at the test section and an opposed flow up to 100 cm/s can be
created by an array of fans controlled by a microcontroller. Two resistance thermal detectors (RTDs), one
actively heated and one used as reference, are placed right below the sample holder to monitor the flow
velocity. The RTDs were calibrated using the flame tower, where the velocity probe can be traversed in
stationary air at any prescribed velocity.
One of the major improvements made to the tunnel is the ability to rotate it and set it at any desired
angle (see Figure 2.5).
We have collected data for both cellulosic fuels and PMMA sheets.


NASA/TM-20210011385 15




Figure 2.4.-San Diego State University
flame tunnel has same dimensions as
Hirano tunnel.


Figure 2.5.-San Diego State University flame tunnel can be
turned to different angles to alter effect of buoyancy-
induced flow.


NASA/TM-20210011385 16




To establish the boundary layer effect on flame spread rate, experiments were carried out with ashless
filter paper with the opposing flow velocity as the control variable. While the blowoff extinction velocity
is assumed to be only a function of chemical kinetics, these experiments clearly establish the boundary
layer development as an important parameter. The experiments are quite repeatable, and a correlation has
been obtained for cellulosic fuel.


#### 2.1.3 Concluding Remarks


The Residence Time Driven Flame Spread (RTDFS) experiment of Burning and Suppression of
Solids-II (BASS-II) resulted in the publication of two archival journal articles, several conference
papers, and two manuscripts submitted to the 36th International Symposium on Combustion. RTDFS
vindicated the theoretical and computational findings that the critical opposed-flow velocity at which
radiative extinction occurs in a microgravity environment is independent of fuel thickness, the manuscript
published in Combustion and Flame is included in its entirety in Section 2.2.


#### 2.1.4 References


<table>
 <tr>
  <th>Fernandez-Pello, A.C.; and Hirano, T.: Mechanisms of Flame Combust. Sci.</th>
 </tr>
 <tr>
  <td>Technol., vol. 32, nos. 1-4, 1983, pp. 1-31.</td>
 </tr>
 <tr>
  <td>Bhattacharjee, Subrata, et al.: A Novel Apparatus for Flame Spread Study. Proc. Combust. Inst., vol.</td>
 </tr>
 <tr>
  <td>34, no. 2, 2013, pp. 2513-2521.</td>
 </tr>
 <tr>
  <td>Paolini, Christopher, et al.: Flame Tower: A Novel Apparatus to Study Flame Spread at Low</td>
 </tr>
 <tr>
  <td>Concurrent or Opposed Flow Velocity. Presented at the 8th U.S. National Combustion Meeting,</td>
 </tr>
 <tr>
  <td>070FR-0141, 2013. https://sutherland.che.utah.edu/USCI2013/PAPERS/2H04-070FR-</td>
 </tr>
 <tr>
  <td>0141.pdf Accessed June 18, 2021.</td>
 </tr>
 <tr>
  <td>Hirano, T.: Flame Spread. Fire Safety Science. Proceeding, 5th AOSFST, Newcastle, Australia,</td>
 </tr>
</table>


1.  Controlling Spread.

2. 

3.  paper

4.  2001, pp. 40-54.


2.1.5 Publications Resulting from This Work
Journal Articles
• Bhattacharjee, S., et al.: Opposed-Flow Flame Spread: A Comparison of Microgravity and
Normal Gravity Experiments to Establish the Thermal Regime. Fire Saf. J., vol. 79, 2016, pp.
111-118. DOI: 10.1016/j.firesaf.2015.11.011 Accessed June 18, 2021.
• Bhattacharjee, S., et al.: The Critical Flow Velocity for Radiative Extinction in Opposed-Flow
Flame Spread in a Microgravity Environment: A Comparison of Experimental, Computational,
and Theoretical Results. Combust. Flame, vol. 163, 2016, pp. 472-477. DOI:
10.1016/j.combustflame.2015.10.023 Accessed June 18, 2021.
Conference Articles and Presentations
• Bhattacharjee, S., et al.: The Critical Flow Velocity for Radiative Extinction in Opposed-Flow
Flame Spread in a Microgravity Environment: A Comparison of Experimental, Computational,
and Theoretical Results. Presented at the 9th Mediterranean Combustion Symposium, Rhodes,
Greece, 2015.
• Olson, Sandra L., et al.: Results From On-Board CSA-CP and CDM Sensor Readings During the
Burning and Suppression of Solids-II (BASS-II) Experiment in the Microgravity Science
Glovebox (MSG). ICES-2015-196, 2015.
• Bhattacharjee, S.; and Carmignani, L.I.: The Effect of Boundary Layer on Blow-Off Extinction in
Opposed-Flow Flame Spread: Results of Experiments and Simplified Analysis. ATEM'15:


NASA/TM-20210011385 17




International Conference on Advanced Technology in Experimental Mechanics 2015, Toyohashi,
Japan, 2015.


• Bhattacharjee, S.; Simsek, A.; and Ivisic, I.: The Role of Fuel Thickness in Opposed-Flow Flame
Spread in a Quiescent Microgravity Environment. Western States Section (WSS) Technical
Meeting of the Combustion Institute, Provo, UT, 2015.
• Grayson, L.; Kievens, K.; and Bhattacharjee, S.: Measurement of Thermal Radiation in Stabilized
Downward Spreading Flame. Western States Section (WSS) Technical Meeting of the
Combustion Institute, Provo, UT, 2015.
• Simsek, A.; and Bhattacharjee, S.: Effect of Boundary Layer on Blow-Off Extinction in Opposed-
Flow Flame Spread: A Computational Study. Presented at the 9th So Cal Fluids Symposium, San
Diego, CA, 2015.
• Laue, M.; Ivisich, I.; and Bhattacharjee, S.: A Comparison of Radiation Signature From
Spreading Flames in Normal and Zero Gravity Environment. Presented at the 8th Annual Student
Research Symposium, San Diego, CA, 2015.
• Bhattacharjee, S., et al.: Opposed-Flow Flame Spread: A Comparison of Microgravity and
Normal Gravity Experiments Establishing the Thermal Regime. Presented at the 8th International
Symposium for Physical Sciences in Space, Alexandria, VA, 2015.


NASA/TM-20210011385 18




1. Critical Flow Velocity for Radiative Extinction in Opposed-Flow Flame Spread in Microgravity Environment: Comparison of Experimental, Computational, and Theoretical Results1


#### 2.2.1 Abstract


The effect of opposing flow on flame spread rate over thin solid fuel is investigated with the help of
scaling theory, a comprehensive computational model, and experiments conducted aboard the
International Space Station. While spread rate over thin fuels is independent of the opposing flow velocity
in the thermal regime, in the microgravity regime, where the opposing flow can be very mild or even
completely absent in the absence of buoyancy-induced flow, the spread rate is known to decrease as the
opposed flow is reduced. Under certain conditions, this can lead to flame extinguishment at a low enough
flow velocity. This report combines scaling arguments with computational results to predict a critical flow
velocity for such flame extinction. Results from the recently conducted limited number of space-based
tests, presented in this report, seem to confirm the prediction validating the closed-form formula for the
critical extinction velocity.


#### Symbols


c specific heat at constant pressure, kJ/kg.K
F de Ris flame coefficient
L length scale, m
T temperature, K
t time, s
Vf absolute spread rate
Vg opposed-flow velocity
Vr velocity relative to the flame, Vr = Vg + Vf
W width
αg thermal diffusivity of gas, evaluated at Tv, m2/s


ε surface emissivity


λg gas-phase conductivity evaluated at Tv, kW/m∙K
ηf nondimensional spread rate
ηg nondimensional flow velocity
ρg gas density evaluated at Tv, kg/m3
ρs solid density, kg/m3


τ fuel half-thickness, m
σ Stefan-Boltzmann constant, kW/(m2K4)
ℜ0 nondimensional radiation number


1Previously published as: Bhattacharjee, S., et al.: The Critical Flow Velocity for Radiative Extinction in Opposed-
Flow Flame Spread in a Microgravity Environment: A Comparison of Experimental, Computational, and
Theoretical Results. Combust. Flame, vol. 163, 2016, pp. 472-477. DOI: 10.1016/j.combustflame.2015.10.023


NASA/TM-20210011385 19




##### Subscripts


cr critical
f adiabatic flame
g gas phase
radiative
res residence
s solid phase
thermal
v vaporization
x, y coordinates


∞ ambient


#### 2.2.2 Introduction


Opposed-flow flame spread over thermally thin fuels is one of the most fundamental topics in the
study of fire spread. The physics of flame spread is considerably simplified in this configuration because
the flame spreads steadily and the fuel can be assumed to be uniformly heated across its thickness.
Moreover, in the thermal regime, gas-phase and pyrolysis chemistry can be considered infinitely fast
compared to the resident time 2 , the time spent by the oxidizer as it passes through
t res ≈LVg g ≈αg V g
the length ≈α ggg LV of the flame leading edge for thermal diffusivity αg, producing a simplified
closed-form expression for the thermal limit (Refs. 1 and 2) of the flame spread rate. The spread rate is
independent of flow velocity Vg, inversely proportional to the fuel thickness, and directly proportional to a
nondimensional coefficient known as the de Ris coefficient - - =TT F(fv ) ( TTv∞ ) , where Tf is the
adiabatic flame temperature, Tv is the fuel vaporization temperature, and T∞ is the ambient and virgin fuel
temperature. As the opposed-flow velocity is increased, the residence time being inversely proportional to
the square of velocity, finite-rate kinetics in the gas phase becomes important leading ultimately to the
blowoff extinction. This kinetic regime has been experimentally (Ref. 3) and computationally (Ref. 4)
studied and the spread rate, normalized by its thermal limit, has been correlated to the nondimensional
Damköhler number, the ratio of the chemical and residence time. The downward spread in a quiescent 1g
environment can be considered a special case of opposed-flow flame spread with buoyancy-induced flow
providing the opposing flow velocity (Ref. 5).
In a microgravity environment, the opposing flow can be very mild and even completely absent in the
perfectly quiescent situation of zero gravity. Numerical (Refs. 6 and 7) and experimental (Refs. 8 and 9)
studies have established the radiative regime in the mild opposed-flow environment in which the flame
spread rate decreases as the opposed-flow velocity is reduced leading to flame extinguishment (Ref. 10) if
the flow velocity is sufficiently low. This result is also dependent on other ambient conditions as steady
spread over thin fuels in a perfectly quiescent environment has been established at higher O2 levels
(Ref. 11). The critical velocity, defined as the opposed-flow velocity below which steady spread rate is
not observed in a microgravity environment, has been shown to depend on O2 level, but its dependence on
other parameters such as fuel thickness are still not well known. There is no closed-form formula, verified
by experimental results that can be used to predict the critical velocity.
In this work, recent experimental work for flame spread over thin sheets of polymethylmethacrylate
(PMMA) performed in the International Space Station (ISS) is reported. The experimental results are
analyzed to determine the critical velocity for different fuel thicknesses and ambient O2 levels. The results
are compared with predictions from a simplified analysis and computational results from a two-


NASA/TM-20210011385 20




dimensional (2D) steady-state flame spread model. A predictive formula for the critical velocity is
proposed in this work.


#### 2.2.3 Experimental Setup


The Burning and Suppression of Solids-II (BASS-II) apparatus (Ref. 12) in the ISS is depicted in
Figure 2.6. It is a combustion tunnel, a 76-mm square duct, where the PMMA fuel samples, 20 mm wide
and about 95 mm long with the thickness ranging from 100 to 400 µm, are burned in an opposed-flow
configuration. A fan forces a flow of an O2-N2 mixture through flow straighteners from the right to the
left and the sample is ignited at the left end. Depending on the flow velocity and O2 concentration, a
steady flame is established that spreads from the left end of the sample towards the right end. The O2 level
can be adjusted to 21 percent or below and the flow velocity can range from 0 to 50 cm/s. A hot wire
anemometer is used to calibrate the flow velocity with fan voltage, which is used to determine the flow
velocity.
Experiments were conducted in the Microgravity Science Glovebox of the ISS by two crew members.
Operation instructions were communicated from NASA Glenn Operations Center in realtime as the
experiment progressed. Each test starts by creating a desired opposing flow by adjusting the fan voltage.
After the flow stabilizes, the igniter is turned on until a visible flame is observed. The igniter is then
turned off and the flame is photographed with a high-resolution digital still camera with a frame rate of
1 per second. A radiometer is used to confirm flame extinction when the visible flame goes out. In some
of the tests, the flow velocity is changed during the spread to maximize the test matrix without having to
burn additional samples.


Figure 2.6.-Schematic of Burning and Suppression of Solids-II (BASS-II) combustion tunnel.
Absolute spread rate (Vf). Opposed-flow velocity (Vg).


NASA/TM-20210011385 21




##### 2.2.4 Data Analysis


An image processing application that is based on MATLAB® (The MathWorks, Inc.) has been
developed at San Diego State University to obtain flame spread rate and other information from the
sequence of top-view digital photographs. A typical color image of the top view 10 s after ignition is
shown in Figure 2.7(a) for flame spread over 100-µm-thick PMMA sheet for the ambient conditions of


20.7 percent O2, 1 atm, and an opposed-flow velocity of 2.5 cm/s. The dots along the axis, 6 mm apart,
are superimposed on the image to help display the spatial resolution of the image. The ignition wire,
glowing red at x = 36 mm, and the burnout location, the black line at x = 42 mm are visible in this picture.
To eliminate the effect of edge propagation, the central part of the flame, bracketed between the two
white lines parallel to the axis and about 14 mm apart, is isolated. The red green blue (RGB) values of
each pixel of the central slice are then converted to an intensity value using built-in MATLAB® tools.


Across the width of the section, these intensity values are averaged, producing a 2D representation of the
flame as shown in Figure 2.7(b). The variation of the width-averaged intensity along the x direction (axis)
is shown in Figure 2.7(c). The leading edge of the flame is determined by locating a fixed threshold
intensity. A value of 30 for the threshold value was found to work well for tracking the flame leading
edge for almost all the tests. The location of the maximum intensity is identified by finding the maxima of
the intensity curve (Figure 2.7(c)).
A number of consecutive locations are used to obtain the flame spread rate by finding the slope of the
linear regression analysis. The uncertainty in the spread rate calculations through this method depends on
the sample size, but five consecutive locations have been found to be a good compromise between noise
and temporal precision. Spread rates obtained by tracking the leading edge and bright edge (the maximum
intensity location) are shown in Figure 2.8. The result has been found to be reproducible within 5 percent
uncertainty regardless of how the flame movement is tracked.


Figure 2.7.-Image processing of top view. (a) Color image. (b) Image averaged over
central section between white lines. (c) Variation of intensity along dotted line.
Leading edge is located at x = 887 pixel for a threshold intensity of 30.


NASA/TM-20210011385 22




Figure 2.8.-Flame spread rate obtained by tracking leading edge and location of
peak intensity.


#### 2.2.5 Extinction Velocity


Each test is started by establishing a steady flame spread in the presence of a forced flow and then
reducing the flow velocity in a gradual manner. In the first test, a steady flame was established over a


100-µm sample. After the flame propagated across half the sample length at a steady spread rate of
2.2 mm/s, the flow was abruptly cut off and the flame was observed to extinguish within 2 s. To pin down
the extinction flow velocity, a second test was done under the same conditions except the flow velocity
was set at 3 cm/s and after the flame propagated about half the sample length, the flow was gradually
reduced. The flame spread rate of the leading edge, as plotted in Figure 2.8, shows that the flame
extinguishes at about 30 s after ignition. The fan voltage at that time indicates a flow velocity of about
1.1 cm/s. The sequence of images in Figure 2.9 shows the pathway to radiative extinction. As the flow
speed is gradually reduced from about t = 27 s, the flame size starts shrinking and the orange color
disappears and the flame becomes completely blue, most possibly because of the temperature drop
brought about by radiative losses, which is enhanced by the increased residence time at low flow velocity.
The signal from the radiometer, shown in Figure 2.10, is also consistent with a cooling and shrinking
flame as the signal starts decreasing from right about t = 27 s. After t = 30 s, there is no visible flame and
the radiometer data (Figure 2.10) indicate a sudden change in slope at that time, possibly because the
radiation is emitted mostly by the sample holder with the combustion products swept away by the flow.
When tests are repeated with samples of different thicknesses, the extinction velocities are found to
be about 1 cm/s for 100, 200, and 300 µm and about 1.5 cm/s for 400 µm. At all these thicknesses, the
fuel can be considered thermally thin because the maximum spread rate was found to be inversely
proportional to fuel thickness (Ref. 13), a hallmark of thermally thin regime. However, it must be
mentioned that there are significant uncertainties in these values as the calibration at such low velocity
has high error bars. The boundary layer formed by the fuel and the tunnel walls would influence the flow
velocity seen by the flame. Also, there is a time lag between when the velocity is reduced and when the
reduced velocity reaches the flame. However, we assume that the time lag works the same way when the
fuel thickness is changed. When a few of these tests were repeated, the results were very similar. It can be
safely concluded that the extinction velocity does not depend on the fuel thickness. Tests were also
conducted at a lower O2 level of about 16 percent for two different thicknesses and the extinction


NASA/TM-20210011385 23




Figure 2.9.-Flame images as function of opposed-
flow velocity (Vg) during radiative extinction. (a)
Time (t) = 27 s; Vg = 3.0 cm/s. (b) t = 28 s; Vg =


1. cm/s. (c) t = 29 s; Vg = 1.1 cm/s.


(d) t = 30 s; Vg = 1.1 cm/s.


Figure 2.10.-Radiometer signal for entire duration of test. Discontinuity at time
t = 30 s coincides with disappearance of visible flame.


NASA/TM-20210011385 24




velocities are found to be about 2.6 cm/s for 100 µm and about 4 cm/s for 200 µm. It should be mentioned
that the width of the sample was different, 20 mm for the 100-µm sample and 10 mm for the 200-µm
sample. Even though there is insufficient data at the lower O2 level, it is clear that the extinction velocity
significantly increases as the O2 level is reduced and is independent of the fuel thickness.


#### 2.2.6 Computational Results


The mathematical model consists of the 2D, steady, elliptic, partial differential equations describing
conservation of energy, species mass, total mass, and momentum in the gas phase and ordinary differential
equations for the conservation of mass and energy in the solid phase. In the numerical model, the gas and
solid phases, coupled through interface conditions, are solved sequentially using the SIMPLER algorithm
(Ref. 14). A single-step global reaction with second-order kinetics in the gas phase and a first-order
pyrolysis kinetics is used in modeling fuel vaporization. Details of the model, including the properties used,
can be found elsewhere (Ref. 15), but the model has been validated by reproducing (Ref. 4) several
analytical solutions including Emmons problem and de Ris solution for thin and thick fuels.
The global-balance radiation model (Ref. 6) is used for modeling gas and surface radiation. While the
computational fluids dynamics solution is 2D, the radiation model calculates the Planck mean absorption
coefficient, used in calculating the radiative source term, by equating the thin-gas expression for radiative
losses from the entire computational domain to three-dimensional radiative loss from the domain,
accurately calculated using a narrow band model (Ref. 16). The radiation calculation (Ref. 17) accounts
for losses due to the finite width of the sample.
A large set of computations is carried out by varying opposed-flow velocity and fuel thicknesses for
the ambient conditions of 21/79 (percent by volume) mixture of O2 and N2 at 1 atm pressure. The
resulting spread rates are shown in Figure 2.11. At relatively large values of the opposed-flow velocity Vg,
the spread rate Vf can be seen to be relatively independent of the opposing flow velocity and inversely
proportional to the fuel thickness as predicted by the thermal theory (Ref. 1). However, as Vg is reduced,
Vf decreases, leading to flame extinguishment that is seen in the experiments. Moreover, the extinction
velocity is identical at 1.5 cm/s for all the four thicknesses studied. This finding has been ascertained by
making sure that the results are independent of grid density and the computational domain. The
computational results also reproduce the experimental trend of the increase of the extinction velocity at


Figure 2.11.-Computational spread rate for flame spread over thin
polymethylmethacrylate. Although spread rate can be seen to be function of fuel
thickness, extinction velocity is same at 1.5 cm/s for each thickness. Spread
rates for downward spread configuration are indicated by empty symbols.
Absolute spread rate (Vf). Opposed-flow velocity (Vg).


NASA/TM-20210011385 25




Figure 2.12.-Computational spread rate for flame spread over 100-µm-thick
sheet of polymethylmethacrylate at two different O2 levels. Extinction velocity
increases from 1.5 cm/s at 21 percent O2 to 3.5 cm/s at 16 percent, closely
matching experimental results.


lower O2 levels. For flame spread over 100-µm-thick sheet of PMMA, the calculations were repeated at a
lower O2 level of 16 percent and the two sets of spread rates are compared in Figure 2.12. At a lower O2
level, the spread rate can be seen to significantly lower and the kinetic effect sets in early for Vg greater
than 16 cm/s. The extinction velocity is found to be 3.5 cm/s as opposed to 1.5 cm/s at 21 percent O2.
This is consistent with the experimental finding discussed in the previous section.
It should be mentioned that when the computational model is used (Ref. 15) for downward spread
configuration in a quiescent 1g environment, a steady spread results for 21 percent O2 with spread rates of


1. , 1.6, 1.2, and 0.9 mm/s, for 100, 200, 300 and 400 µm, respectively, as shown in Figure 2.11. At 16 percent O2, however, the buoyancy-created flow is strong enough to cause blowoff extinction.


2.2.7 Scale Analysis: Expression for Extinction Velocity Vg,cr
In a microgravity environment, an opposing flow can be quite mild or even absent, raising the
residence time to the point that both gas and surface radiation can become significant compared to other
heat transfer mechanisms. Numerical studies (Refs. 6 and 7) have shown that both gas and surface
radiation primarily act as a loss mechanism, depressing the flame temperature. As Vg decreases, the
radiative loss effect intensifies and Vf, deviating from its thermal limit, decreases as shown in Figure 2.11
and Figure 2.12. If N2 in the oxidizer is replaced with highly radiating species such as CO2, the gas


radiation feedback may become important (Ref. 18). It can be shown that the surface radiation loss, gas-
phase radiation loss, and gas to surface radiation feedback (see Figure 2.13) scale the same way with the
residence time 2
tV res ≈αg g, ha is, as Vg decreases, all these radiative effects become more severe.
Assuming radiation feedback to be negligible (Ref. 19), the surface radiation loss can be used as a
representative radiation term in the energy balance on the surface. It is well known that forward
conduction through the thin solid with density ρs and heated layer Lsy is negligible (Ref. 20), leaving the
difference between the conduction from the gas phase and radiative losses supplying the net forward heat
transfer necessary to raise the temperature of the virgin fuel from T∞ to Tv. The thermal conductivity of
the gas is λg, cs is the heat capacity of the solid, and ε is the surface emissivity.


- - TT

- ) ( ) ~ fv


T v -T λg LgxW-εσ


- ∞ Lgy

- ( 4 ) 4 T v -T LsxW (2.1) ∞


#### (


V f ρsc s LsyW


NASA/TM-20210011385 26




Here W is an arbitrary width, and the solid-phase horizontal and vertical-length scales, Lsx, and Lsy,
and gas phase vertical and horizontal length scales Lgx and Lgy are shown in Figure 2.13. Because the gas
phase is the only source of heating, the gas-phase length scales are comparable: Lgx ~ Lgy. Also, by
equating (in the scaling sense) the convective term with x and y conduction in the gas phase at the leading
edge, we can establish that LLgx gy αg g V provided  VVgf. Introducing these simplifications into
Equation (2.1) and substituting Lsy, the heated layer thickness in Figure 2.13, with the half-thickness τ of
the fuel, which is uniformly heated across its thickness (an assumption that defines thermally thin fuels),
and neglecting the radiative loss, we obtain the thermal limit:


TT
(fv ) -


( )
v T - T∞


λg
 V where F F=
f ,thermal
ρτ s sc


(2.2)


Using the thermal limit expression for the spread rate as the velocity scale, Equation (2.1) can be
made nondimensional as follows:


where


ℜ ℜ 
00
; ⇒Vf,radiative ~V f,thermal 1-  (2.3)
ηg  gη


ηfg~ ηg- ℜ0; ⇒ ηf~1-


4 4
v - TTV


- ∞

-  , g


ρλ g η≡
gg g v T T∞ Vf -,


1 ρ c ssεστ
ℜ≡
0 2 F c


V
f
η≡ f
Vf, thermal


,


thermal


and cg is the specific heat of gas.


(2.4)


Figure 2.13.-Different modes of heat transfer and length scales (L) at leading edge of flame. For
thermally thin fuel, Lsy ≤ τ. Solid (s). Gas phase (g). Absolute spread rate (Vf). Opposed-flow velocity
(Vg). Velocity relative to flame (Vr). Fuel half thickness (τ).


NASA/TM-20210011385 27




TABLE 2.1.-COMPARISON OF EXTINCTION VELOCITY Vg,cr
FOR THIN POLYMETHYLMETHACRYLATE AT 1 atm
Vg,cr,


<table>
 <tr>
  <th></th>
  <th></th>
  <th>mm/s</th>
  <th></th>
 </tr>
 <tr>
  <td>O2,<br/>percent</td>
  <td>Experiment</td>
  <td>Computation</td>
  <td>Theory,<br/>Equation (2.5)</td>
 </tr>
 <tr>
  <td>21</td>
  <td>10±5</td>
  <td>15</td>
  <td>7.5</td>
 </tr>
 <tr>
  <td>16</td>
  <td>30±5</td>
  <td>35</td>
  <td>10</td>
 </tr>
</table>


Equation (2.3) establishes that the spread rate in the radiative regime decreases with an increase in the
radiation number ℜ0 and a decrease in the nondimensional flow velocity ηg. Note that the fuel thickness
does not affect the ratio ℜη 0 g ; therefore, the inverse relation between flame spread rate and fuel
thickness, a typical thermal regime behavior, also extends to the radiative regime. Setting the
nondimensional spread rate ηf to zero in Equation (2.3), we obtain the condition for radiative extinction as


- ( 4 ) 4 εσ v - TT

- η ≤ℜ ⇒VV V≡ ∞ g ; g ~ g cr where g cr 0,, cgg( TTf v ) ρ -

1. 


As found in the experiments and computations, Equation (2.3) confirms that the extinction velocity is
not a function of fuel thickness. Using the properties used in the numerical simulation (which produces a
linearized flame temperature of 2,199 K) and a vaporization temperature of 673 K, the critical extinction
velocity Vg,cr can be evaluated at different O2 levels. Table 2.1 compares the prediction from this formula
with computational and experimental results. Given the uncertainties associated with the experiments,
simplified nature of the mathematical model, and errors associated with scale analysis, the agreement
seems reasonable.


#### 2.2.8 Conclusions


Recently conducted space-based experimental results on flame extinction at low opposing flow
velocity are presented in this report. A critical flow velocity below which steady spread cannot be
sustained is experimentally determined for various fuel thicknesses and two O2 levels. Results from four
different fuel thicknesses indicate that fuel thickness does not affect the critical velocity, which increases
if the O2 level is decreased. A two-dimensional computation model confirms this finding. A simplified
scale analysis produces a closed-form expression , ( ) [( 44 ) ( TTf- v )] for the critical
V g cr ≡ εσ c g ρg v T - T∞
velocity, where ε is surface emissivity, σ is Stefan-Boltzmann constant, cg is the specific heat of gas, ρg is
gas density evaluated at Tv, Tv is the vaporization temperature, T∞ is ambient temperature, and Tf is
adiabatic flame temperature. It establishes that even though the flame spread rate is inversely proportional
to the fuel thickness, the critical velocity is independent of the fuel thickness. Prediction from this formula
agrees remarkably well with the experimental and computational results.


#### 2.2.9 Acknowledgment


This work was funded by the NASA International Space Station Research Project Office with Dr.
David Urban serving as the contract monitor. We want to acknowledge the invaluable assistance of
Burning
Suppression
(BASS-


<table>
 <tr>
  <th>astronauts Reid Wiseman and Alex Gerst, who ran these and of Solids-II</th>
 </tr>
 <tr>
  <th>II) experiments. This work could not have been done without the intense efforts of the BASS operations</th>
 </tr>
 <tr>
  <th>team Chuck Tibor and Carol We also want to the</th>
 </tr>
</table>


NASA/TM-20210011385 28




NASA ground support teams at Glenn Research Center, Johnson Space Center, and Marshall Space Flight
Center that supported the BASS-II operations.


#### 2.2.10 References


1. De Ris, J.N.: Spread of a Laminar Diffusion Flame. Proc. Combust. Inst., vol. 12, no. 1, 1969, pp. 241-252.

2. Delichatsios, Michael A.: Flame Heights in Turbulent Wall Fires With Significant Flame Radiation. Combust. Sci. Technol., vol. 39, nos. 1-6, 1984, pp. 195-214. 3. Fernandez-Pello, A.C.; Ray, S.R.; and Glassman, I.: Flame Spread in an Opposed Forced Flow: The Effect of Ambient Oxygen Concentration. Proc. Combust. Inst., vol. 18, no. 1, 1981, pp. 579-589.


4. West, Jeffrey S.: Forced Opposed-Flow Flame Spread Over Flat Solid Fuels in the Thermal, Near-
Quiescent and Chemical Kinetic Regimes. Ph.D. Dissertation, Univ. of California, San Diego, 1998.
5. Bhattacharjee, Subrata, et al.: Downward Flame Spread Over Poly(methyl)methacrylate. Proc.
Combust. Inst., vol. 28, no. 2, 2000, pp. 2891-2897.
6. Bhattacharjee, Subrata; and Altenkirch, Robert A.: Radiation-Controlled, Opposed-Flow Flame
Spread in a Microgravity Environment. Proc. Combust. Inst., vol. 23, no. 1, 1991, pp. 1627-1633.


1. Kumar, Chenthil; and Kumar, Amit: On the Role of Radiation and Dimensionality in Predicting Flow Opposed Flame Spread Over Thin Fuels. Combust. Theory Model., vol. 16, no. 3, 2012, pp. 537-569.

2. Takahashi, Shuhei, et al.: Effect of Radiation Loss on Flame Spread Over a Thin PMMA Sheet in Microgravity. Proc. Combust. Inst., vol. 29, no. 2, 2002, pp. 2579-2586. 9. Olson, S.L.: Mechanisms of Microgravity Flame Spread Over a Thin Solid Fuel: Oxygen and Opposed Flow Effects. Combust. Sci. Technol., vol. 76, nos. 4-6, 1991, pp. 233-249.


10. Olson, Sandra; Ferkul, Paul V.; and T'ien, James S.: Near-Limit Flame Spread Over a Thin Solid
Fuel in Microgravity. Proc. Combust. Inst., vol. 22, no. 1, 1989, pp. 1213-1222.
11. Bhattacharjee, Subrata; Altenkirch, Robert A.; and Sacksteder, Kurt: Implications of Spread Rate and
Temperature Measurements in Flame Spread Over a Thin Fuel in a Quiescent, Microgravity, Space-
Based Environment. Combust. Sci. Technol., vol. 91, 1993, pp. 225-231.
12. Reckart, T.A.: Space Flight System at GRC: Burning and Suppression of Solids (BASS). National
Aeronautics and Space Administration, 2014. https://www1.grc.nasa.gov/space/iss-
research/msg/bass/ Accessed June 21, 2021.
13. Bhattacharjee, S., et al.: Opposed-Flow Flame Spread: A Comparison of Microgravity and Normal
Gravity Experiments to Establish the Thermal Regime. Fire Saf. J., vol. 79, 2016, pp. 111-118. DOI:
10.1016/j.firesaf.2015.11.011 Accessed June 18, 2021.
14. Patankar, Suhas V.: Numerical Heat Transfer and Fluid Flow. McGraw Hill, New York, NY, 1980.
15. Bhattacharjee, Subrata; King, Matthew D.; and Paolini, Chris: Structure of Downward Spreading
Flames: A Comparison of Numerical Simulation, Experimental Results and a Simplified Parabolic
Theory. Combust. Theory Model., vol. 8, no. 1, 2004, pp. 23-39.


1. Grosshandler, W.: Radcal: A Narrow-Band Model for Radiation Calculations in a Combustion Environment. NIST Technical Note 1402, 1993.

2. Ivisic, Ivan: Application of a Validated Radiation Model in Flame Spread Rate Over Solid Fuels. M.S. Thesis, San Diego State Univ., 2016.

3. Son, Youngjin; and Ronney, Paul D.: Radiation-Driven Flame Spread Over Thermally Thick Fuels in Quiescent Microgravity Environments. Proc. Combust. Inst., vol. 29, no. 2, 2002, pp. 2587-2594.

4. Bhattacharjee, S., et al.: The Critical Flow Velocity for Radiative Extinction in Opposed-Flow Flame Spread in a Microgravity Environment: A Comparison of Experimental, Computational, and


NASA/TM-20210011385 29




Theoretical Results. Combust. Flame, vol. 163, 2016, pp. 472-477. DOI:


1. /j.combustflame.2015.10.023 Accessed June 18, 2021.


20. Ito, Akihiko; and Kashiwagi, Takashi: Temperature Measurements in PMMA During Downward
Flame Spread in Air Using Holographic Interferometry. Proc. Combust. Inst., vol. 21, no. 1, 1988, pp.
65-74.


NASA/TM-20210011385 30




## 2.3 Opposed-Flow Flame Spread: Comparison of Microgravity and Normal-Gravity Experiments to Establish Thermal Regime2


### 2.3.1 Abstract


The thermal regime of flame spread over solid fuels constitutes the reference condition for all other
flame spread research. Although the theory of flame spread in the thermal regime is well understood, the
well-known closed-form formulas for flame spread do not compare well with available experimental data.
The comparison is further complicated by the fact that establishing a thermal regime in a normal-gravity
environment is difficult because of the buoyancy-induced flow, which may usher in finite-rate kinetics
effect. As a result, even the transition thickness, when a fuel can be considered a thermally thick fuel, still
lacks a widely accepted formula.
This work presents opposed-flow flame spread data over varying thicknesses of
polymethylmethacrylate obtained in the International Space Station where the opposing flow velocity can
be reduced arbitrarily without any interference from the gravity-induced flow. It also presents a larger set
of spread rate data for the downward spreading configuration at normal gravity. A comparison between
the two datasets allow us to establish the thermal limit for thin fuel for which the spread rate is
independent of the opposing flow velocity. The classical thin fuel spread rate formula is shown to fit well
with the experimental results provided the adiabatic flame temperature is used in the flame coefficient
that appears in the formula. The experimentally determined flame coefficient along with downward flame
spread data for thick fuels are used to develop a closed-form expression for the transition thickness
between thermally thin and thick fuels for downward spread in the thermal regime.


### Symbols


aP
c
F
f
g
g,rad
gy,cond
Lg
Lsy
s,rad
sx,cond
T
t
Vf
Vg
Vr
αg
αs


ε


Planck mean absorption coefficient
specific heat, kJ/kg.K
flame constant, Equation (2.12)
radiation view factor for the gas to the solid preheat region
gravity
gas radiation feedback
conduction through gas
gas-phase diffusion length scale, m
fuel thickness
surface radiation
conduction through solid
temperature, K
time
absolute spread rate, m/s
velocity of the oxidizer, m/s
velocity relative to the flame, Vr = Vg + Vf
thermal diffusivity of gas, evaluated at Tv, m2/s
thermal diffusivity of solid
surface emissivity


2Previously published as: Bhattacharjee, S., et al.: Opposed-Flow Flame Spread: A Comparison of Microgravity and
Normal Gravity Experiments to Establish the Thermal Regime. Fire Saf. J., vol. 79, 2016, pp. 111-118. DOI:


10.1016/j.firesaf.2015.11.011


NASA/TM-20210011385 31




λg
λs
Ω
ρg
ρs


σ
τ
 ω′′′F


gas-phase conductivity evaluated at Tv, kW/m.K
solid thermal conductivity
ratio (ρcpλ)g /(ρcpλ)s
gas density evaluated at Tv, kg/m3
solid density, kg/m3
Stefan-Boltzmann constant, kW/(m2K4)
fuel half-thickness, m
fuel consumption rate


### Subscripts


adb
chem
cond
cr
de Ris
eff
eql
expt
f
g
lin
NC
rad
res
s
th
thick
thin
transition
v
x, y


∞


adiabatic
chemical
conduction
critical


effective
equal
experimental
flame
gas phase
linear
natural convection
radiation
residence
solid phase
thermal


vaporization
coordinates
ambient


### 2.3.2 Introduction


Opposed-flow flame spread over solid fuels has been under investigation for about four decades
(Refs. 1 to 3). Researchers have long desired to understand and predict the behavior of fire in different
situations and under different conditions. While flame spread in the upward configuration is closely
related to fire safety studies, it is also quite complex to model because the flame spread process is not
steady and the flame size quickly becomes very large. In the downward configuration, where a flame
spreads down a solid fuel sample vertically downward, the flame behaves in a two-dimensional (2D),
quasi-steady (while the flame spread rate is constant, the flame shape may evolve in an unsteady manner),
quasi-laminar (the flame trailing edge may show fluctuating pattern) manner with the steady flame spread
rate being a function of fuel and environmental conditions. Because experiments on downward spread can
be inexpensive to perform (Ref. 4), theories to describe the mechanism of flame spread in a quantitative
manner can be tested and refined. Findings from this simplified configuration can be useful for more


NASA/TM-20210011385 32




practical configurations, such as upward or horizontal spread, given the commonality of various physics
that participate in the mechanism of flame spread (Ref. 5).
Even in this simplified configuration a number of complexities can arise. Based on the thickness of
the fuel sample, it may or may not be uniformly heated across its thickness. The pyrolysis chemistry to
predict the burning rate of the fuel may not be well known (Ref. 6). The gas-phase chemistry used in
computational models mostly assumes an overall single-step reaction. If the buoyancy-generated flow is
strong enough or the O2 level is low enough (or both), a competition between the combustion time and
residence time may usher in chemical kinetics effect (Ref. 7) on the flame, leading to a reduction of
spread rate or even extinction. Yet another complication can arise if the opposing flow velocity is too low,
as in the case of a microgravity environment. A higher residence time makes both surface and gas
radiative effects increasingly important (Ref. 8). Obviously, despite the simplification that the assumption
of a 2D laminar flow brings in, a theory that includes gas-phase radiation, chemical kinetics in the gas
phase, and pyrolysis kinetics is still too complicated to yield a solution without the application of
numerical analysis. This is why de Ris (Ref. 9) introduced the thermal regime, where the theory is
drastically simplified by assuming that the opposing flow velocity is not too small or not too large so that
neither radiation nor chemistry play any significant role in the mechanism of flame spread. As a result an
analytical solution of the governing equations is possible with the neglect of radiation and assumption of
infinite-rate kinetics; the closed-form spread rate formulas by de Ris and Delichatsios (Refs. 9 and 10) in
the thermal regime provide a baseline for nondimensionalizing experimental data and understanding the
parametric dependence of flame spread with fuel and environmental conditions.
These well-known formulas for opposed-flow spread rate, however, have some drawbacks. The flame
temperature used in the formula is based on a linearized mass diffusion theory and can be quite different
than the thermodynamic adiabatic flame temperature. Also, use of constant properties in the theory allows
room for significant variability in how properties such as thermal conductivity of air, specific heat, etc.,
are evaluated. As a result, when an experimental spread rate does not agree reasonably well with the
theoretical prediction, it is not clear whether the disagreement is due to incorrect use of properties in the
formula or due to more fundamental reason such as the flame spread is not in the thermal regime.
The opposed-flow flame spread experiments, where the opposing flow velocity can be directly
controlled in a flow tunnel (Refs. 11 and 12) can easily create a high flow velocity where gas-phase
chemistry becomes important due to shortened residence time. However, the opposed flow cannot be
arbitrarily reduced. Even in a quiescent environment, there is no guarantee that the buoyancy-created flow
is weak enough to justify an assumption of infinite-rate kinetics.
In this work, we use the gravity-free environment of the International Space Station (ISS) to continue
the opposed-flow flame spread experiment to its logical conclusion by reducing the opposing flow
velocity to any desired value without any interference from buoyancy in search of the elusive thermal
regime. We present data from both downward experiments and microgravity experiments for the same
fuel under the same environmental conditions (except for gravity level of course) for the first time. A
simplified scale analysis is carried out to establish the elusive thermal regime experimentally. The results
also help us determine the transition thickness between thermally thin and thermally thick fuels for
downward flame spread.


### 2.3.3 Scale Analysis


Flame spread is determined by the competing physics at the flame leading edge. To establish the
thermal regime through a scale analysis, a comprehensive sketch of all the major participants is presented
in Figure 2.14, where different types of heat transfers are shown in bold arrows, length scales at the
leading edge, and competing timescales with the subscripts g indicating gas phase and s indicating the


NASA/TM-20210011385 33




solid phase. The heat transfer to the virgin fuel, the driving mechanism of any flame spread (Ref. 5),
involves conduction through the gas (gy,cond), conduction through the solid (sx,cond), surface radiation
(s,rad), and gas radiation feedback (g,rad). Of these, forward conduction through the solid has been
shown to be relatively unimportant theoretically (Ref. 9) and experimentally (Ref. 13). It should be
mentioned that high lateral (perpendicular to spread rate) thermal conductivity, which can be different
from the forward conductivity in composite materials, has been experimentally (Ref. 14) shown to
influence the spread process strongly. In this analysis, however, the focus will be on homogeneous fuel
such as polymethylmethacrylate (PMMA) (C2H8O2). The radiative effects are also neglected (the rational
to be discussed later), leaving gas to solid conduction as the dominant heat transfer mode.
By comparing the forward heat conduction to the advection term at the flame leading edge, the
diffusion length scale can be established as Lg ≈ αg/Vg, where αg is the thermal diffusivity and Vg is the
opposing flow velocity. Therefore, the gas residence time, time spent by the oxidizer at the leading edge,
is given as t g, ≈ es LVgg r//2ggV≈α. Assuming gas-phase conduction is the primary heating mechanism
of the preheat zone, Lg must also be the solid-phase heating length. The fuel residence time, time spent by
the fuel at the leading edge, is then given by ts,res ≈ Lg/Vf ≈ αg/(VgVf), where Vf is the flame spread rate, the
desired unknown.
The first assumption of the thermal regime is that  VVfg so that ttre g s,  ,res . The combustion
timescale in the gas phase, tg,chem, can be defined as the time necessary for the combustion reaction to be
complete at the flame leading edge raising the gas temperature to Tf,adb, the adiabatic flame temperature.
Similarly, the chemical timescale in the solid phase for the pyrolysis of fuel, ts,chem, can be defined as the
time necessary for the fuel temperature to reach a vaporization temperature Tv. By assuming ttres g,  ,chem
and ttre g s,,,chem finite-rate kinetics (Ref. 12) in the gas and solid phases can be


Figure 2.14.-Various time t and length scales L at leading edge. In thermal regime, fuel preheating rad
and transverse conduction cond through gas g and solid s are of same order. Chemical (chem). Absolute
spread rate (Vf). Velocity of the oxidizer (Vg).


NASA/TM-20210011385 34




eliminated. Tf,adb and Tv, therefore, can be considered thermodynamic properties. However, when tg,res is
too large, which is a possibility in a microgravity environment where in the absence of buoyancy-induced
flow Vg can be quite small or even absent, gas and surface radiation can become important (Ref. 15). In
the thermal regime, tg,res is considered large compared to tg,chem but not large enough for the radiative
effects to be significant. If the opposed flow is not a fully developed flow, the presence of a boundary
layer upstream of the flame leading edge can alter the effective velocity the flame encounters (Ref. 12).
For a theoretical solution, the boundary layer effect is routinely neglected, and the opposing flow is
considered a slug flow. The remaining assumptions include the neglect of finite width, effect of humidity,
and variability of properties with temperature.
With the complications of kinetics and radiation eliminated, the essential mechanism for steady
spread rate in the thermal regime reduces to heating up a layer of fuel of thickness Lsy (to be determined)
from ambient temperature T∞ to vaporization temperature Tv within the solid-phase residence time ts,res.
The gas layer of thickness Lg responsible for supplying this heat must itself be heated up from T∞ to Tf,adb
in the available time tg,res at the leading edge. As already mentioned, the combustion time, defined as the
time to consume the fuel vapor with mass fraction xF at density (ρxF) in the volume L2
g at the leading
edge tg,chem ≈ρ( x F ) /  ω′′′F , is considered small compared to the residence time tg,res in the thermal regime.
If the O2 level is reduced, the fuel consumption rate  ω′′′F decreases increasing tg,chem and finite-rate
chemistry becomes important, leading to flame extinction, when tg,chem becomes comparable to tg,res. Even
if there is sufficient O2, if Vg is high enough, tg,res can decrease to the point that it becomes comparable to
tg,chem and finite-rate kinetics becomes important leading to blowoff extinction.
The timescale for a heat transfer mechanism can be defined as the time it takes to supply or remove
the characteristic amount of heat, ρs Lsy Lc g s (T v ∞ T), ne - cessary to heat up the fuel layer Lsy with density
ρs at the leading edge from T∞ to Tv. The gas radiation timescale, tg,rad ≈ [[ρ s Lsy Lc g s (T v -∞ T )]
4 a( σ-T4 TL) 42


  P f ∞ , wh g ere ap is the Planck mean absorption coefficient, σ is the Stefan-Boltzmann


constant, and Tf, is the flame temperature, can be shown to be much larger than tg,res as long as Vg is not
too small; it means gas radiation, both radiative losses and radiative feedback to the fuel, is not a
significant participant within the short residence time tg,res of the thermal regime.
In the solid phase, the residence time depends on the gas-phase length and spread rate: ts,res ≈ Lg/Vf.
Within this time, the fuel must start pyrolyzing. It can be shown that the characteristic pyrolysis time is
much shorter than ts,res so that Tv can be considered a thermodynamic property of the fuel (Ref. 16). The
timescale for surface radiation, , [ ( )] [ ( 44
v )L g ] , where solid density ρ
t s rad ≈ ρs Lsy Lc g s T v - ∞ ∞ T εσ T -T s,
specific heat of the solid cs, and emissivity ε are constant while Lsy varies, can be shown to be much larger
than ts,res for a large enough Vg, meaning surface radiation also can be neglected in the thermal regime.
The forward conduction through solid with thermal conductivity λs and thermal diffusivity αs is also
neglected in the thermal regime as ≈ t, [ ρL L (c - TT)] [ λ( - TT)(L L)]≈ 2 Lα
sx cond s sy s v ∞ ∞ g s v sy g g s t re s,
as long as LVg αs f, which is true except for very high Vg.
The surviving timescales, time for gas tgy,cond to solid conduction tsy,cond, and interior conduction loss
through solid, must be of the same order as the solid residence time (see Figure 2.14). That is,


t re ≈ ≈ t gy cond s,,,ycond t (2.6)


Equating the first two timescales produces an expression for Vf in terms of Lsy:


L LLcT ∞
g ρs sy g s ( v -T) λ T


- ( ) / ; g , where f T v -

- ≈ ⇒≈ f VF ≡ F


V f λg T f -T v L g L g ρsLc sy s T v T ∞ -


(2.7)


NASA/TM-20210011385 35




A thermally thin fuel, by definition, is heated across its thickness so that Lsy ≈ τ, where τ is the half-
thickness of the fuel (only the symmetric half of the leading edge is depicted in Figure 2.14). The familiar
expression of thin-limit spread rate (Ref. 10) (except for the factor of π/4) is obtained by substituting Lsy ≈


τ in Equation (2.7). For a thick fuel, the last two timescales in Equation (2.6) are equated to produce


ρLLcT -T ρLLcT -T L
s sy g s ( v ∞ ) s sy g s ( v ∞ ) s g λ


- ≈ ⇒L s

- ( ) / ( ) ; / sy ≈ ≈

- λ g T f -T v LLg g λ s T v - ∞ T LLg sy λgF ρgc g g VF

1. 


Substituting this expression in Equation (2.7) produces the familiar de Ris thick limit (Ref. 9):


λ g ρλc ggg
, 2
Vfthin ≈ ≈ F; and Vf,thick VFg (2.9)


ρssτ cssscρλ


One of the remarkable aspects of these expressions is that the spread rate is independent of opposing
flow velocity Vg for thin fuels while it is proportional to Vg for thick fuels. An increase in Vg obviously
raises the heat flux (W/m2) from the gas to the solid, but it also shortens the preheat zone length, making
the heat flow (W) independent of flow velocity. This heat is used to raise the temperature of the heated
layer, which is the physical half-thickness of a thin fuel sample. For a thick fuel, on the other hand, the
heated layer thickness depends on the heat flux: a higher temperature gradient in the solid (in the y
direction) and, hence, a thinner heated layer, is necessary to sustain a higher heat flux from the gas and
hence the flow velocity. That is how the velocity dependence is introduced for a thermally thick fuel.
Equation (2.8) also provides a simple criterion for transition thickness. A fuel can be considered
thermally thin when


τ< τcr ; where τcr ≈ (2.10)


λs
ρ cV gggF


Although Equations (2.9) and (2.10) are remarkable in their simplicity, there is no universally
accepted procedure for evaluating various parameters. The temperature at which gas properties are
evaluated, the value of Tf and Tv to be used in determining F, and how to include the effect of the
boundary layer on Vg are all subject to differing interpretation (Refs. 1, 10, and 12).


### 2.3.4 Onset of Kinetic Effect


One of the major challenges in acquiring data in the thermal regime is the onset of gas-phase kinetic
effect when tg,res decreases to the level of the combustion time tg,chem. Their ratio, called the Damköhler
number, decreases the same as the opposed-flow velocity is increased (at a given O2 level), leading to
blowoff extinction. In the downward spreading configuration in a normal-gravity environment, buoyancy-
generated flow, which scales with VNC ≈α [ ggT ( g -T) ∞T]13∞ (Ref. 17) creates a constant opposing flow
for a given O2 level. When a forced opposing flow is superposed, the forced flow cannot have much
impact on the flame spread until the strength of forced convection becomes comparable to that of natural
convection due to gravity.
To illustrate this, average spread rate data acquired in a vertical combustion tunnel (Ref. 18) for
various opposing airflow velocity for spread over a thin sheet of PMMA (50-µm-thick, 2-cm-wide) is
plotted in Figure 2.15. The spread rate can be seen to remain relatively independent of the forced
opposing flow velocity until it reaches a value of 40 cm/s. Similar behavior has been observed in flame
spread over thin cellulosic fuel (Ref. 12). For thermally thin fuel in the thermal regime, the spread rate is


NASA/TM-20210011385 36




Figure 2.15.-Downward flame spread over polymethylmethacrylate sheets of 50-µm
thickness in presence of forced opposed flow of air. Filled symbols represent blowoff
extinction.


expected to be independent of opposing flow velocity as dictated by Equation (2.9). So, does the constant
spread rate for up to a velocity of 40 cm/s in Figure 2.15 indicate the existence of thermal regime? Based
on computational work (Ref. 17) that used a one-step second-order global kinetics model, it was
concluded that kinetic effect may be present even at 21 percent O2 level. The independence of spread rate
with opposing flow velocity was interpreted as a constant kinetic effect by the buoyancy-generated flow.
However, given the simplicity of the chemical kinetic model (one-step overall reaction) used in the
computational model, a definitive conclusion cannot be made from computational results alone.
One way to experimentally establish if there is kinetic effect in downward spread rate is to reduce the
strength of the buoyancy-generated flow or eliminate it altogether as in a microgravity environment. If the
flow velocity is reduced below 40 cm/s, the increased residence time would reduce and weaken the
kinetic effect and the spread rate can be expected to increase (in a kinetically controlled flame) until the
thermal limit is reached. On the other hand, if the thermal limit is already established in the downward
experiment (see Figure 2.14), then the spread rate is expected to remain unaltered as the opposing flow
velocity is reduced in the absence of buoyancy. A comparison of experiments in the downward
configuration with that in a microgravity environment, therefore, can be used to establish the thermal
regime for a given O2 level.


### 2.3.5 Microgravity and Normal-Gravity Experiments


There are only a handful of experiments conducted on flame spread in a microgravity environment,
an excellent review of which can be found as a book chapter by T'ien (Ref. 19). The only long-duration
opposed-flow experimental facility is offered by the BASS-II apparatus (Ref. 20) in the ISS. It is depicted
in Figure 2.16. It is a combustion tunnel, a 76-mm square duct, where the PMMA (C2H8O2) fuel samples,
20 mm wide and about 95 mm long with the thickness ranging from 100 to 400 µm, are burned in an
opposed-flow configuration. A fan forces a flow of an O2-N2 mixture through flow straighteners from the
right to the left and the sample, 2 cm wide, is ignited at the left end. Depending on the flow velocity and
O2 concentration, a steady flame is established that spreads from the left end of the sample towards the
right end. The oxidizer mixture consists of O2 and N2 where the O2 level can be adjusted at 21 percent or
below. During the experiment, an O2 sensor monitors the O2 level, which has been found to drift by less


NASA/TM-20210011385 37




than 0.1 percent. A hot wire anemometer is used to calibrate the flow velocity with the voltage of the fan
(see Figure 2.16) used for creating a flow of 50 cm/s or below. The total pressure is also monitored, which
varied from 99.2 to 99.5 kPa in the tests reported.
Experiments were conducted in the Microgravity Science Glovebox of ISS by two crew members.
Operation instructions were communicated from NASA Glenn Operations Center in realtime as the
experiment progressed. Each test starts by creating a desired opposing flow by adjusting the fan voltage.
After the flow stabilizes, the igniter is turned on until a visible flame is observed. The igniter is then
turned off and the top view of the flame propagation is photographed with a high-resolution digital still
camera with a frame rate of 1 per second. A video camera captures the side view of the flame
propagation. In some of the tests, the flow velocity is changed during the spread to maximize the test
matrix without having to burn additional samples.
For downward spreading experiments, the Flame Stabilizer apparatus (Ref. 4) is used, where a 2-cm-
wide sample of PMMA is held vertically by a stainless steel sample holder and ignited at the top with a
top-view camera recording the flame spread. The sample holders used in the microgravity and downward
experiments are shown in Figure 2.17. While the BASS sample holder has a built-in igniter, piloted
ignition is used in the downward experiments. The downward experiments were performed in the
atmospheric condition (pressure 101 kPa, O2 level 21 percent).
Ideally, the controllable parameters in a flame spread experiments include oxidizer mixture (percent
of O2 by volume), oxidizer pressure, oxidizer velocity, fuel type, fuel thickness, fuel width, fuel length,
and external radiation. In the data presented, the fuel thickness is the most important parameter of interest.


Figure 2.16.-Experimental setup aboard International Space Station used for opposed-flow flame
spread research. Absolute spread rate (Vf). Velocity of the oxidizer (Vg).


NASA/TM-20210011385 38




Figure 2.17.-Sample holder used for downward (left) and microgravity Burning and
Suppression of Solids (BASS) (right) experiments.


### 2.3.6 Data Analysis


The still images from the BASS experiments are converted to videos and posted along with those
from the downward experiments at http://flame.sdsu.edu. A MATLAB®- (The MathWorks, Inc.) based
image processing application called Flame Analyzer has been developed at San Diego State University
(SDSU) to obtain flame spread rate and other information from a top-view video. Video analysis has been
used in fire research for a long time not just for tracking flame spread (Ref. 21) but also for estimating
flame temperature (Ref. 22). But the Flame Analyzer is designed to automate the process of finding
instantaneous flame spread rate.
A typical color image of the top view 18 s after ignition is shown in Figure 2.18(a) for downward
flame spread over a 75-µm-thick sample. The dots along the axis, 6 mm apart, are superimposed on the
image to help display the spatial resolution of the image. The red green blue (RGB) values of each pixel
of the central slice are then converted to an intensity value using built-in MATLAB® tools. Across the
width of the section, these intensity values are averaged, producing a 2D representation of the flame as
shown in Figure 2.18(b). The variation of the width-averaged intensity along the x direction (axis) is
shown in Figure 2.18(c). The leading edge of the flame is determined by deciding on a fixed threshold
intensity. A value of 70 for the threshold value was found to work well for tracking the flame leading
edge for this test.
For flame spread over 100-µm-thick samples, the leading edge locations during microgravity and
downward spreads are shown in Figure 2.19(a). Most conditions are kept similar between the
microgravity and downward experiments except in the microgravity experiment, the opposing flow
velocity is 3 cm/s. A number of consecutive leading edge locations are used to obtain the flame spread
rate by finding the slope of the linear regression analysis. The resulting spread rates are plotted in
Figure 2.19(b). The uncertainty in the spread rate calculations by tracking the leading edge in this manner
has been shown to be less than 5 percent except near ignition time when the flame bursts into its
spreading form (Ref. 4). Once away from the ignition zone, averaging over 5 s of propagation have been
found to produce spread rates that are reproducible within 5 percent variability. The error bar remains the
same (at 5 percent or under) for all the data reported.


NASA/TM-20210011385 39




Figure 2.18.-Flame data. (a) Top view of flame 18 s into video, (b) two-dimensional representation of
flame from averaged intensity values, and (c) variation of width-averaged intensity in x direction.


Figure 2.19.-Microgravity and downward configuration results. (a) Leading edge location versus time in microgravity
(solid line) and downward configurations. (b) Spread rate versus time in microgravity (solid line) and downward
configurations.


### 2.3.7 Results and Discussion


The average spread rate over the 100-µm-thick sample in the normal-gravity experiments is found to
be 2.0 mm/s (see Figure 2.19(b)). Although the instantaneous spread rate fluctuates slightly, the average
spread rate and the flame shape remain relatively steady throughout the experiment. The opposed flow
being generated by buoyancy, a steady spread is expected. Any variation is probably due to surface
irregularities and other random factors. In a microgravity environment, the opposed flow is much lower
with experiments conducted mostly at very mild opposed-flow velocities. For the same fuel thickness, the
highest spread rate obtained is about 2.2 mm/s even though the opposing flow velocity was varied from


NASA/TM-20210011385 40




about 40 cm/s to about 1 cm/s. At very high flow velocity, kinetically driven blowoff extinction was
observed and at very low velocity (at about 1 cm/s) radiative extinction was observed. The highest spread
rate in the microgravity environment, 2.2 mm/s, is about the same as the downward spread rate. The
overall flame shapes are also quite similar as shown in Figure 2.20(a) and (b) where flame images for
spread over samples of different thicknesses are compared. The leading edges in the downward spread
show slight dripping effect and the flame is sootier, but the overall shape and size are quite similar as are
the spread rates. This indicates that at 21 percent O2 level, downward spread over PMMA can be
considered thermally controlled with minimal kinetic effect.
Because gas-phase kinetics (or precisely, the Damköhler number, the ratio of the residence time to the
gas-phase combustion time) is independent of fuel thickness, downward or microgravity spread over
different fuel thicknesses should follow Equation (2.9). Using properties as listed in the nomenclature, de
Ris formula for the thin limit, Equation (2.9) modified with a factor of π/4, can be expressed as


ρλc
ggg 29.72 10 52 =  -
=VF
g  (2.11)


F m
8
; = and Vf,thick
τ cssscρλ


×VFgs


π λ g


,
Vfthin =F 2.34× 10-
4
ρssτ


Figure 2.20.-Image array comparing microgravity and downward flame spread for
different thicknesses of polymethylmethacrylate (PMMA). Velocity of oxidizer (Vg).
Absolute spread rate (Vf). PMMA (NASA) in 0g on International Space Station, 2-cm
sample with 10.x cm in 20.7 percent O2 and 79 percent N2 at 1 atm. (a) Burning and
Suppression of Solids-II (BASS-II) B03 sample; 100 µm thick. (b) BASS-II B11;
200 µm thick. (c) BASS-II B4; 300 µm thick. (d) BASS-II B13; 400 µm thick. PMMA
(NASA and Astra) in 1g at San Diego State University, 2-cm sample with 10.x cm in


20.7 percent O2 and 79 percent N2 at 1 atm. (e) PMMA at NASA; 100 µm thick.
(f) PMMA at Astra; 200 µm thick. (g) PMMA at NASA; 300 µm thick. (h) PMMA at
NASA; 400 µm thick.


NASA/TM-20210011385 41




For the experimental value of Vf,thin = 2.2 mm/s for τ = 50 µm, the value of the de Ris flame
coefficient F can be calculated from Equation (2.9) as 4.76. This experimentally (expt) determined value
compares with different values used in literature as follows:


τV ,thin TT, , ,


f 4.76; f lin - v T f adb - - v T TT
expt 8 de Ris ≡ 5.54; F F 4.89; f eql v


= F =F= 4.41 =
2.34 10 adb ≡ = eql ≡
×- TTvvv
-∞∞∞(2.12)
Although de Ris expression for spread rate is based on the linearized (lin) flame temperature (the


theory neglects advection in the normal direction to the fuel bed, replacing it with enhanced linearized
diffusion that leads to the closed-form expression for flame spread rate in terms of a linearized flame
temperature), the adiabatic (adb) flame temperature is easier to compute and can be seen to produce good
agreement with the experimentally (expt) determined value of the equilibrium (eql) flame coefficient.
Using Fadb in Equation (2.11), spread rates calculated for different fuel thicknesses are plotted in
Figure 2.21. Spread rate data for all four different fuel thickness studies are superposed along with data
from downward experiments with nine different fuel thicknesses. The thermal regime formula for the thin
fuel, Equation (2.11), seems to fit the experimental results quite well. Further downward experiments are
conducted with progressively higher fuel thicknesses. Use of extruded PMMA produces considerable
dripping (possibly because the methylmethacrylate chains are broken during extrusion making it easier
for PMMA to drip) producing unsteady spread, while cast PMMA is less susceptible to dripping,
producing a steady spread. Data for 2-cm-wide samples are added in Figure 2.22 with the purpose of
creating a thick limit and delineating thermally thin fuel. Although for thicker fuels, the spread rate is
slightly width dependent, a value of 0.042 mm/s for a 10-cm-wide sample (Ref. 23) as opposed to
0.044 mm/s for the 2-cm-wide sample, an average value of 0.044 mm/s is selected as the average spread
rate for downward spread over PMMA in the thick limit.
The value of the flame coefficient F is not affected by the fuel thickness; therefore, Fadb that works so
well with the thin fuel formula can also be applied to the thick-limit formula of Equation (2.11). However,
the flow velocity Vg is an unknown for downward spread and should be replaced by an effective velocity.


Figure 2.21.-Comparison of microgravity and downward flame spread at different
thicknesses of polymethylmethacrylate. Absolute spread rate (Vf). Specific heat (cs).
Flame constant for Burning and Suppression of Solids (FBASS). Gas-phase conductivity
(λg). Solid density (ρs). Fuel half-thickness (τ).


NASA/TM-20210011385 42




Figure 2.22.-Comparison of microgravity, downward flame spread, and Fernandez-Pello
and Williams experimental data at different thicknesses of polymethylmethacrylate. Also
showing thin and thick fuel theoretical thermal limits.


Using the experimental value of Vf,thick = 0.044 mm/s, the effective value of the opposing flow created by
natural convection can be calculated from Equation (2.11) as


V
,thick,expt m cm
f
V = = 0.019 =1.9
g,eff ΩF2 ss
adb


(2.13)


where Ω is the ratio (ρcpλ)g/(ρcpλ)s.
In earlier computation work (Ref. 17), the effective velocity was calculated as 6 cm/s based on a more
complex definition of the flame coefficient. The current experimental result, on the other hand, is based
on F defined in terms of adiabatic flame temperature. The characteristic buoyancy-driven natural
convection flow can be shown to scale with VNC ≈α [ ggT ( g -T) ∞T]13∞. Using Tv as the characteristic
gas temperature near the flame leading edge, we calculate VNC = 10.2 cm/s, which is about the same order
as the effective velocity.
The transition thickness between the thermally thin and thick fuels can be obtained by equating the
experimentally verified thin and thick fuel spread rate expressions.


π λ
V =V ⇒τ = s


f,thin,expt f,thick,expt ; transition
4 ρgcV g g,eff Fadb


( m) (2.14)


The transition thickness (2τtransition) can be calculated from this expression as 5.19 mm for downward
flame spread in ambient air. In a general opposed-flow environment, the transition thickness will vary
with the opposing flow velocity and the boundary layer development length through its dependence on
Vg,eff, with pressure through its dependence on ρg, and O2 level through its dependence on Fadb.


### 2.3.8 Conclusion


In this work, results of experiments on flame spread over thin sheets of polymethylmethacrylate
(PMMA) in the quiescent downward configuration and opposed-flow configuration in the microgravity
environment are compared. A curve fit of maximum spread rate against fuel thickness using de Ris


NASA/TM-20210011385 43




formula for the thermal regime was used to determine the de Ris coefficient F as 4.76 for an oxidizing
mixture of 21 percent O2 and 79 percent N2. Based on adiabatic flame temperature, F is only about
3 percent greater. Data from downward spread in ambient air is shown to correlate well (within the
experimental uncertainty) with the microgravity data, establishing that the thermal limit is extended to
downward spreading configuration in atmospheric condition on Earth. With F evaluated, experimental
data for flame spread over thick PMMA is used to determine the effective velocity induced by buoyancy
as 1.9 cm/s. Equating the thermal regime spread rate expressions for thin and thick limits, a formula for
the transition between thin and thick fuels for downward spread in ambient atmosphere is obtained. For
PMMA in ambient air, this transition thickness is evaluated to be 5.2 mm.


### 2.3.9 Acknowledgment


<table>
 <tr>
  <th>This work was funded by the NASA International Space Station Research Project Office with</th>
 </tr>
 <tr>
  <th>Dr. Sandra Olson serving as the contract monitor. We want to acknowledge the invaluable assistance of</th>
 </tr>
 <tr>
  <th>astronauts Reid Wiseman and Alex Gerst, who ran these and of Solids-II</th>
 </tr>
 <tr>
  <th>This work could not have been done without the intense efforts of the BASS</th>
 </tr>
 <tr>
  <th>team Owens, Chuck Bunnell, Tibor Lorik, and Carol We also want to the</th>
 </tr>
 <tr>
  <th>teams at Glenn Research Center, Johnson Center, and Marshall</th>
 </tr>
</table>


(Jay
Reynolds).
acknowledge
NASA ground support
Space
Space Flight
Center that supported the BASS-II operations.


### 2.3.10 References


1. Wichman, Indrek S.: Theory of Opposed-Flow Flame Spread. Prog. Energy Combust. Sci., vol. 18, no. 6, 1992, pp. 553-593. 2. Blasi, C.D.: Modeling and Simulation of Combustion Processes of Charring and Non-Charring Solid 3. Controlling Spread. Technol., vol. 32, nos. 1-4, 1983, pp. 1-31. 4. Bhattacharjee, S., et al.: A Novel Apparatus for Flame Spread Study. Proc. Combust. Inst., vol. 34, no. 2, 2013, pp. 2513-2521. 5. Williams, F.A.: Mechanism of Fire Spread. Proc. Combust. Inst., vol. 16, no. 1, 1977, pp. 1281-1294. 6. Torero, J.L., et al.: The Effect of Gravity on a Laminar Diffusion Flame Established Over a Horizontal Flat Plate. Proc. Combust. Inst., vol. 25, no. 1, 1994, pp. 1701-1709. 7. Altenkirch, R.A.; Eichron, R.; and Shang, P.C.: Buoyancy Effects on Flames Spreading Down Thermally Thin Fuels. Combust. Flame, vol. 37, 1980, pp. 71-83. 8. Bhattacharjee, Subrata, et al.: Opposed-Flow Flame Spread in Microgravity-Theoretical Prediction of Spread Rate and Flammability Map. Proc. Combust. Inst., vol. 30, no. 2, 2005, pp. 2279-2286. 9. De Ris, J.N.: Spread of a Laminar Diffusion Flame. Proc. Combust. Inst., vol. 12, no. 1, 1969, pp. 241-252.


<table>
 <tr>
  <th>Fuels. Prog. Energy. Combust. Sci., vol. 19, 1993, pp. 71-104.</th>
 </tr>
 <tr>
  <th>Fernandez-Pello, A.C.; and Hirano, T.: Mechanisms of Flame Combust. Sci.</th>
 </tr>
</table>


10. Delichatsios, M.A.: Exact Solution for the Rate of Creeping Flame Spread Over Thermally Thin
Materials. Combust. Sci. Technol., vol. 44, nos. 5-6, 1986, pp. 257-267.


11. Hirano, Toshisuke; and Sato, Kenji: Effects of Radiation and Convection on Gas Velocity and
Temperature Profiles of Flames Spreading Over Paper. Proc. Combust. Inst., vol. 15, no. 1, 1975, pp.
233-241.
12. Bhattacharjee, Subrata; Nagarkar, Rohit; and Nakamura, Yuji: A Correlation for an Effective Flow
Velocity for Capturing the Boundary Layer Effect in Opposed-Flow Flame Spread Over Thin Fuels.
Combust. Sci. Technol., vol. 186, no. 8, 2014, pp. 975-987.


NASA/TM-20210011385 44




1. Ito, Akihik; and Kashiwagi, Takashi: Measurement Technique for Determining the Temperature Distribution in a Transparent Solid Using Holographic Interferometry. Appl. Optics, vol. 26, no. 5, 1987, pp. 954-958.

2. Di Blasi, C.; and Wichman, I.S.: Effects of Solid-Phase Properties on Flames Spreading Over Composite Materials. Combust. Flame, vol. 102, no. 3, 1995, pp. 229-240. 15. Bhattacharjee, Subrata; and Altenkirch, Robert A.: Radiation-Controlled, Opposed-Flow Flame Spread in a Microgravity Environment. Symposium (International) on Combustion, vol. 23, no. 1, 1991, pp. 1627-1633.


16. Bhattacharjee, S.; Bhaskaran, K.K.; and Altenkirch, R.A.: Effects of Pyrolysis Kinetics on Opposed-
Flow Flame Spread Modeling. Combust. Sci. Technol., vol. 100, nos. 1-6, 1994, pp. 163-182.


1. Bhattacharjee, Subrata, et al.: Downward Flame Spread Over Poly(methyl)methacrylate. Proc. Combust. Inst., vol. 28, no. 2, 2000, pp. 2891-2897. 18. Carmignani, Luca: Flame Spread Over Solid Fuels Facing an Opposing Flow: Experimental Investigation of the Aerodynamic Effects on Spread Rate and Extinction. M.S. Thesis, Univ. of Pisa, 2015.


19. Ross, H.D.: Microgravity Combustion: Fire in Free Fall. Appl. Mech. Rev., vol. 55, no. 6, 2002, pp.
B116-B117.


1. Reckart, T.A.: Space Flight System at GRC: Burning and Suppression of Solids (BASS). National Aeronautics and Space Administration, 2014. https://www1.grc.nasa.gov/space/iss- research/msg/bass/ Accessed June 21, 2021.

2. Klimek, Robert; and Wright, Ted: Spotlight-8 Image Analysis Software. NASA/TM-2006-214084, 2006. https://ntrs.nasa.gov

3. Audoin, L., et al.: Average Centreline Temperatures of a Buoyant Pool Fire Obtained by Image Processing of Video Recordings. Fire Saf. J., vol. 24, no. 2, 1995, pp. 167-187.

4. Fernandez-Pello, A.C.; and Williams, F.A.: Laminar Flame Spread Over PMMA Surfaces. Proc. Combust. Inst., vol. 15, no. 1, 1975, pp. 217-231.


NASA/TM-20210011385 45




#### 3.0 Project Scientist Report: Ferkul


### 3.1 Nomex® Flammability


The objective of the Nomex® (DuPontTM) sample tests was to evaluate the flammability of Nomex®,
since it is heavily used aboard the International Space Station (ISS) as a fire barrier. A secondary
objective was to burn any unused Burning and Suppression Solids-I (BASS-I) samples, of which there
was a single wax candle. The test matrix is in Appendix A.


### 3.1.1 Results


The three Nomex® samples did not ignite, which is an excellent result for fire safety aboard the ISS.
The wax candle test successfully ignited in an opposed flow (akin to holding a candle upside down)
and burned at five different flow velocities corresponding to the test matrix potentiometer settings as
shown in Figure 3.1. At the initial 3 cm/s, the sooty flame has an aspect ratio that is longer rather than
wide. As the flow reduced, the flame became hemispherical. At the lowest pot setting, the flame becomes
short rather than wide and turns mostly blue.
The ejected wax droplet shown in Figure 3.1(b) typifies the flame spread hazard associated with
melting plastics in microgravity. If the melt viscosity is low enough, burning droplets can be ejected and
possibly ignite other materials.


Figure 3.1.-Candle wick burning with opposed flow (upward flow). (a) Postignition at 3 cm/s (potentiometer or pot
0.6); (b) Pot 0.4, wick ejects droplet of wax directly upstream; (c) Pot 0.35; (d) Pot 0.32; and (e) Pot 0.31.


NASA/TM-20210011385 46




#### 4.0 Individual Principal Investigator Report: Fernandez-Pello


### 4.1 Opposed-Flame Spread Task


The scientific objective of the Burning and Suppression Solids-II (BASS-II) opposed-flow flame
spread test is to further understand the mechanisms controlling the spread of flames over the surface of
solid combustible materials, particularly in a spacecraft environment. For this purpose, experiments were
conducted aboard the International Space Station (ISS) to determine the effects of microgravity on the
spread of flames over polymethylmethacrylate (PMMA) rods of different diameters subjected to different
O2 concentrations and low flow velocities. These are parameters that in addition to low pressure are
expected in spacecraft environments. By conducting these tests aboard the ISS and then comparing the
results to ground-based data, it is expected that a better understanding of the governing mechanisms of
flame spread in microgravity can be obtained. In addition, by conducting the tests with cylindrical
samples, the effect on the flame spread process of geometrical factors such as the transverse curvature of
the surface can be better studied.


### 4.1.1 Experiment and Test Matrix


The tests were conducted in the BASS-II hardware placed inside the Microgravity Science Glovebox
(MSG) in the Destiny Lab of the ISS. The BASS-II hardware consists of a flow duct, still camera, video
camera, external control box, and associated plumbing and mounting systems along with the fuel samples
for the BASS-II experiments.
The tests for the present task were conducted with rods of cast PMMA with diameters of 6.35, 9.525,
and 12.7 mm (1/4, 3/8, and 1/2 in., respectively) and were 57.15 mm in length. All cylindrical rods tested
started with rounded (hemispherical) ends in order to minimize the flow disturbance associated with the
abrupt bluff body transition at the sample's downstream edge. Ignition of the PMMA was accomplished
by using a hot wire placed to heat the PMMA surface in the downstream edge of the rods.
Table 4.1 and Table 4.2 present the test conditions for the opposed-flow flame spread tests conducted
in this task. The majority of the tests were conducted with black PMMA, because rods of black PMMA
are also used in the Material Ignition and Suppression Test (MIST) project to reduce effects of in-depth
absorption of thermal radiation. For this reason, the results presented in this report are limited to those for
black PMMA. A few tests were conducted with clear PMMA for comparison purposes, but the data is too
limited to present it here.


TABLE 4.1.-ROD DIAMETERS TESTED FOR BOTH CLEAR AND BLACK POLYMETHYLMETHACRYLATE (PMMA)
ABOARD INTERNATIONAL SPACE STATION AS PART OF BURNING AND
SUPPRESSION SOLIDS-II (BASS-II) CAMPAIGN


<table>
 <tr>
  <th>Size, m</th>
  <td>0.00635</td>
  <td>0.009525</td>
  <td>0.0127</td>
  <td>Total</td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td>Black PMMA</td>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>Test conditions</th>
  <td>23</td>
  <td>12</td>
  <td>12</td>
  <td>47</td>
 </tr>
 <tr>
  <th>Samples burnt</th>
  <td>9</td>
  <td>4</td>
  <td>4</td>
  <td>17</td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td>Clear PMMA</td>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>Test conditions</th>
  <td>4</td>
  <td>3</td>
  <td>0</td>
  <td>7</td>
 </tr>
 <tr>
  <th>Samples burnt</th>
  <td>2</td>
  <td>1</td>
  <td>0</td>
  <td>3</td>
 </tr>
</table>


NASA/TM-20210011385 47




TABLE 4.2.-RANGE OF OXIDIZER AND ESTIMATED MIXED (FORCED AND FREE) FLOW CONDITIONS BY
DIAMETER EMPLOYED ABOARD INTERNATIONAL SPACE STATION AS PART OF BURNING
AND SUPPRESSION SOLIDS-II (BASS-II) CAMPAIGN


<table>
 <tr>
  <th>Sample diameter, m</th>
  <td>0.00635</td>
  <td>0.009525</td>
  <td>0.0127</td>
 </tr>
 <tr>
  <th>O2 concentration, vol%</th>
  <td>16.8 to 18.9</td>
  <td>17.5 to 20.9</td>
  <td>17.6 to 20.7</td>
 </tr>
 <tr>
  <th>Flow velocity, m/s</th>
  <td>0.0041 to 0.075</td>
  <td>0.043 to 0.02</td>
  <td>0.0137 to 0.0164</td>
 </tr>
</table>


Table 4.2 exhibits the range of oxidizer and flow conditions employed in these tests. The focus of
these experiments was on low O2 concentrations and characteristic flow velocities below those achievable
in 1g environments due to the effects of buoyancy. The low-flow velocities in microgravity environments
allow for the investigation of conditions unachievable in a 1g environment. As a means of comparison,
from standard Grashof number arguments one can derive a characteristic buoyant velocity induced by the
heated sample (Ref. 1), and at the point of ignition it is approximately 0.50 m/s, which is an order of
magnitude greater than the largest forced-flow velocity tested in the BASS-II experiments, as can be seen
in Table 4.2.


### 4.1.2 Results


Multiple test conditions were accomplished for each PMMA sample by igniting the sample at a high
opposed-flow velocity and then subsequently reducing the opposed-flow velocity until extinction was
observed, pausing along the way to allow steady-state flame spread. The results presented herein
comprise the effects of O2 concentration and flow velocity on the rate of microgravity opposed-flame
spread over black PMMA rods in microgravity. Figure 4.1(a) presents a summary of the results of the
effect of flow velocity on the opposed-flow flame spread rate for 0.00635-, 0.009525-, and 0.0127-m-
diameter rods of black cast PMMA. The data points are at different O2 concentrations, which explains
some of the scatter in the data. Figure 4.1(b) presents the effect of O2 concentration at different flow
velocities.
As can be seen in Figure 4.1(a), the average flame spread rate increases with opposed-flow velocity,
even within the small range of flow velocities tested. Sustained flame spread for the conditions tested was
not observed for opposed-flow velocities below approximately 4 mm/s for the 0.00635- and 0.009525-m-
diameter rods. Visually it was observed that at very low flow velocities the flames appear to be very
small, blue, faint, and open at their downstream ends. As the flow velocity rises towards 20 mm/s and
above, the flames become much more luminous, with bright yellow flames, and a closed downstream tip.
In Figure 4.1(b), the data exhibits an upward trend in spread rate with increasing O2 concentration,
which is especially marked in the results of the 6.35-mm-diameter rods.  Both of these sets of
observations are similar to those of previous work on flame spread in microgravity. Near the quenching
limit, not only is diffusion playing a bigger role in providing the oxidizer flow to the flame, but also, the
flame becomes very faint and the reradiation from the sample surface becomes increasingly important
(Refs. 2 and 3).
To facilitate the comparison of the data for the different conditions, all the data points are presented in
Figure 4.2. Figure 4.2 presents the same data as Figure 4.1, but presents all three rod diameters in one
plot, and colors the data points by their respective O2 concentration (Figure 4.2(a)) or flow velocity
(Figure 4.2(b)).


NASA/TM-20210011385 48




Figure 4.1.-Flame spread rate versus opposed-flow velocity and O2 concentration for three diameters of black
polymethylmethacrylate rods in microgravity. (a) Opposed-flow velocity. (b) O2 concentration.


In comparing the experimental results from ground-based experiments with those conducted aboard
the ISS, a number of complications arise. First and foremost, due to the effect of buoyancy, the effective
opposed-flow velocity felt by the flame in the 1g experiments is an order of magnitude greater than the
velocities tested in microgravity experiments. As has been shown elsewhere, the difference in flame
spread rate between natural convective conditions and an opposed-flow velocity of 0.25 m/s in 1g is
relatively negligible. On the other hand, for the microgravity tests presented herein, the flow velocities
under investigation are near the quenching limit, below those normally expected from the air supply and
recirculation systems currently employed on the ISS.
In addition to difficulties regarding the use of comparable flow velocities, in the microgravity
experiments only the two largest diameter rods were tested at near 21 percent O2 by volume, with the
highest O2 concentration tested for the 6.35-mm-diameter rods being approximately 19 percent by
volume. The only O2 concentration at which all three rod diameters employed in the microgravity
experiments were tested was at approximately 17.5 percent O2 by volume. In the 1g experiments, the
lowest O2 concentration at which all four tested rod diameters were successfully burnt without the
addition of an external radiant heat source was 19 percent by volume.
Thus, in comparing the datasets, some compromises were made. In particular, as can be seen in
Figure 4.3, the ranges of O2 concentrations and rod diameters employed do not completely overlap. Yet,
the trend in flame spread rate in terms of both O2 concentration and rod diameter are still quite apparent
even after discounting the fact that the flow velocities are not strictly comparable.


NASA/TM-20210011385 49




The most important result of the comparison is that of the minimum O2 concentration for flame
spread in normal and microgravity. While in microgravity, flame spread was observed at O2
concentrations as low as 17.5 percent, in normal gravity, flame spread was not observed below 19
percent. This result is probably due to the lower opposed-flow velocity in the microgravity tests in
comparison with those induced by buoyancy in normal gravity.


Figure 4.2.-Flame spread rate versus opposed-flow velocity and O2 concentration for
three diameters of black polymethylmethacrylate rods in microgravity where
independent variable not on abscissa is represented as color of data point.


(a) Opposed-flow velocity. (b) O2 concentration.


NASA/TM-20210011385 50




Figure 4.3.-Comparison of flame spread rates for black cast
polymethylmethacrylate (PMMA) rods as function of gravity, O2 concentration,
and rod diameter. All data are for experiments carried out in absence of external
radiant heating. All O2 concentrations and flow velocities for microgravity
experiments are averaged over associated test conditions.


Decreasing the rod diameter increases the flame spread rate in both 1g and microgravity
environments, as shown in Figure 4.3. It is also apparent that flame spread in microgravity is appreciably
faster than in 1g for cylindrical rods of PMMA. These results agree well with similar comparisons of 1g
and microgravity results for opposed-flow flame spread on wire insulation (Refs. 4 and 5), as well as
theoretical considerations of the problem (Ref. 6).
The rods were ignited at the downstream end, and the flame was allowed to spread across the rod for
a period of time at each velocity. A typical test is shown in Figure 4.4(a) to (e), where the flame is
initially sooty. As the flow velocity is reduced, the sooting decreases and then disappears. The flame tail
opens up as it continues to spread along the rod. The rod extends past the end of the flame as the
spreading continues. This wide-open flame tail with rod remaining behind is unique to microgravity.
In normal gravity, the flame burns away the rod in a conical regression, and the rod tip is always
within the flame. The regression angle of the cone increases as the forced-flow velocity increases (Ref. 6).
At relatively high flow rates (120 cm/s and higher) (Refs. 6 and 7), the flame is small and flat behind a
flat rod tip (regression angle 90°). In other words, the flame is stabilized in the recirculation zone behind
the rod. It is quite difficult to blowoff this flame, as was predicted (Ref. 8). The distinction between flame
spread and regression is important when one considers the classic limiting O2 index test (Ref. 9), where a
small sample is burned like a candle flame in a 4-cm/s oxidizer flow velocity, and the O2 concentration is
reduced until the flame extinguishes. The small flames in 1g sit at the top of the sample instead of
spreading down the sample near the extinction limit.
A similar shaped flame is observed at very low O2 concentration in the space experiment, as shown in
Figure 4.4(f). The flame survived under the low-O2 conditions until the initially hemispherical rod tip
regressed to a flat surface. It never spread along the outer surface of the rod. It is hypothesized that the
flame quenched when the local flow velocity in the flame zone decreased as the flame transitioned to a
wake flame, and the sample thickness that needed heating exceeded the ability of the weakened flame to
heat it.


NASA/TM-20210011385 51




Figure 4.4.-Two flame sequences showing very different burning behavior. Black polymethylmethacrylate (PMMA)
rod, 4.76 mm, 18.5 percent O2, with decreasing flow at (a) 1.9 cm/s, (b) 1.7 cm/s, (c) 1.6 cm/s, and (d) 1.5 cm/s.


1. Posttest rod, showing general conical burn shape except blunt melted tip of the rod. (f) Black PMMA rod,


3.18 mm, 16.3 percent O2, at 5 cm/s. Cap-shaped flame burned away initial hemispherical tip of rod to flat surface
and then extinguished.


The postburn rod samples in Figure 4.5 preserve bubble layers for the opposed flow and for
concurrent flow (Olson tests). The opposed-flow rod exhibits a dense white bubble layer starting abruptly
near the flame leading edge and extends downstream as the rod regresses symmetrically until the full
thickness of the rod is heated to the point that the molten tip forms a sphere to minimize surface tension.
At the leading edge of the flame, the upstream solid-phase preheat length is relatively short, and the flame
must provide an adequate heat flux to preheat the upstream rod.
In contrast, the concurrent PMMA rod molten tip is upstream, and the dense bubble layer varies with
the flame length. Due to the convective heating of the downstream rod, large widely spaced internal
bubbles are formed well downstream of the flame. These bubbles are full of methylmethacrylate vapor
under pressure from polymer chain scission. When they reach the surface of the material, they rupture and
form a vapor jet that ignites in the presence of a flame. After extinction, the hot material can continue to
produce fuel for some time until it cools. Premixed flame oscillations along the rod have been observed
for the concurrent rod geometry that persist much longer in microgravity than in normal gravity due to the
lower rate of convective cooling of the rod. This suggests that spacecraft fire suppression efforts should
be maintained until the burning material has cooled and stopped emitting vapors.


NASA/TM-20210011385 52




Figure 4.5.-Polymethylmethacrylate rod bubble layers (a) opposed and


(b) concurrent.


### 4.1.3 References


1. Schlichting, Herrmann; and Gersten, Klaus: Boundary-Layer Theory. Springer, Berlin, Germany, 2001.

2. Altenkirch, Robert A., et al.: Opposed-Flow Flame Spreading in Reduced Gravity. The Second International Microgravity Combustion Workshop Proceedings, NASA CP-10113, 1993, pp. 237- 243. https://ntrs.nasa.gov

3. Bhattacharjee, Subrata, et al.: Extinction Criteria for Opposed-Flow Flame Spread in a Microgravity Environment. Seventh International Workshop on Microgravity Combustion and Chemically Reacting Systems Proceedings, NASA/CP-2003-212376/REV1, 2003, pp. 201-204. https://ntrs.nasa.gov

4. Kikuchi, Masao et al.: Experimental Study on Flame Spread Over Wire Insulation. Proc. Combust. Inst., vol. 27, no. 2, 1998, pp. 2507-2514.

5. Fujita, Osamu; Nishizawa, Katsuhiro; and Ito, Kenichi: Effect of Low External Flow on Flame Spread Over Polyethylene-Insulated Wire in Microgravity. Proc. Combust. Inst., vol. 29, no. 2, 2002, pp. 2545-2552.

6. Higuera, F.; and Linan, A.: Flame Spread Along a Fuel Rod in the Absence of Gravity. Combust. Theory Model., vol. 3, no. 2, 1999, pp. 259-265.


NASA/TM-20210011385 53




1. Bhattacharjee, Subrata; and Carmignani, Luca: Burn Angle in Forced and Natural Convection: A Simplified Scaling Approach. Combust. Theory Model., vol. 23, no. 5, 2019, pp. 956-968.

2. Link, Shmuel, et al.: The Effect of Gravity on Flame Spread Over PMMA Cylinders. Sci. Rep., vol. 8, no. 120, 2018. 9. Ikeda, G.: Oxygen Index Tests to Evaluate the Suitability of a Given Material for Oxygen Service. Flammability and Sensitivity of Materials in Oxygen-Enriched Atmospheres, ASTM STP812, B. Werley, American Society for Testing and Materials, West Conshohocken, PA, 1983, pp. 56-67.


<table>
 <tr>
  <th></th>
 </tr>
 <tr>
  <th>ed.,</th>
 </tr>
</table>


NASA/TM-20210011385 54




#### 5.0 Individual Principal Investigator Report: Miller and Wichman


### 5.1 Narrow Channel Apparatus as Microgravity Flame Spread Surrogate


Combustion of clear cast polymethylmethacrylate (PMMA) samples 10 cm long by either 1 or 2 cm
wide with thicknesses ranging from 1 to 5 mm was investigated in opposed flow. Tests included both
one-sided and two-sided burns. The samples were burned in a flow duct within the Microgravity Science
Glovebox (MSG) on the International Space Station (ISS) to ensure true microgravity conditions. The
experiment took place in opposed flow with a varying O2 concentration (uncontrolled) and varying flow
velocities (controlled). Flames are recorded on two cameras and later tracked to determine spread rate.
Assuming a linear profile between O2 concentration at the start and the end of each test, we made
graphs of O2 concentration versus time for each test. From these, we created flammability maps showing
the flame behavior at different O2 concentrations and flow velocities. Additionally, we have conducted an
extinction analysis, plotting the O2 concentration against the flow velocity at the time of extinction with
respect to type of test (one sided or two sided). Currently we are modeling combustion of flat PMMA
samples in microgravity using Fire Dynamic Simulator (FDS; v5.5.3; National Institute of Standards and
Technology (NIST)). The entire modeling for Burning and Suppression of Solids-II (BASS-II) is
performed in Direct Numerical Simulation (DNS) mode because of the laminar conditions and small
domain. The model employs the same test sample and MSG geometry as the experiment. The model
predicts a higher flame spread rate than that observed in experiments. So, we look to modify the chemical
kinetics and materials properties to improve the model. Also, we plan to do a domain study and grid
sensitivity analysis in future.


### 5.2 Introduction


The NASA Burning and Suppression of Solids-II (BASS-II) tests examine the combustion of
different solid materials and geometries in microgravity. While flames in microgravity are driven by
diffusion and weak advection due to ventilation systems and crew movement, the current NASA
spacecraft material selection test method (NASA-STD-6001 Test 1) (Ref. 1) is driven by buoyant forces
since gravity is present. So, the BASS-II results will be used in comparison with ground-based
experimental setups aimed at replacing NASA's current test method for screening materials used onboard
spacecraft. The data gathered will also help us understand and know more about behavior of fires in space
so that space travel can be made safer in the future. The BASS-II experiments have provided us with an
extensive thick fuel microgravity database that did not exist previously. Previously, thick-fuel true
microgravity data was obtained by Olson and others in a study involving Sounding Rocket experiments
(Ref. 2). The study comprised a series of combustion experiments on polymethylmethacrylate (PMMA) at
very low velocity opposed flow and external radiant flux.
The institutions taking part in BASS-II operations are Case Western Reserve University; University
of California, Berkeley; NASA Glenn Research Center; San Diego State University; and Michigan State
University (Ref. 3). There are three categories of samples: flat samples, rod samples, and a section of a
large solid sphere. The flat sample materials will include acrylic films and sheets of different thicknesses,
and a cotton-fiberglass fabric blend Solid Inflammability Boundary at Low-Speeds (SIBAL) fuel. The rod
samples are made of black or clear acrylic and will provide solid fuel regression rates and extinction
limits for both opposed and concurrent flow. The large solid spherical section, also made of acrylic, will
be used to study ignition of thick materials and flame growth over the thick material.


NASA/TM-20210011385 55




## 5.3 Experimental Setup and Summary


The BASS-II hardware shown in Figure 5.1 comprises a small flow duct with an igniter and a small
nozzle along with exchangeable fuel samples. The BASS-II flow duct is placed inside the Microgravity
Science Glovebox (MSG) (255 L) (Ref. 5) onboard the International Space Station (ISS). A radiometer
placed at the top measures the intensity of the flame. A fan is used to produce forced flow of air in the
duct. Also present is an anemometer that measures the velocity of air entering into the duct. A Nikon
digital camera (Nikon Corporation) looks through the top of the flow duct normal to the sample surface
and a high-definition video camera uses a mirror to look through the front door of the duct at the edge of
the flat sample (orthogonal to the high-definition camera). A total of 20 PMMA flat samples were burnt
during the BASS-II experimentation (Table 5.1). The sample thickness varied from 1 to 5 mm thick. The
samples burnt were all either 1 or 2 cm wide. All the burns are either one sided or two sided. The airflow
was always opposed. Airflow speeds ranging from as low as 3 cm/s up to 20 cm/s were used in the flow
duct.
Prior to the start of testing at each session, a crew member installs the hardware in the MSG. The fan
calibration is set before the flame is ignited. Once ignited, the flame is allowed to stabilize at first and
then the airflow is adjusted throughout the test. Fan speed, radiometer reading, and the time is monitored
during the entire test. The airflow is turned off after the test. Videos and data are downlinked to Earth
(Ref. 3). The still images and videos from the data are tracked using Spotlight-16 (NASA image tracking
software) (Ref. 6). Data are then imported to Excel® (Microsoft®) to obtain flame spread rates. A graph of
the position versus time for one of the tests is found in Figure 5.2. The black line in the plot represents the
O2 concentration profile during the duration of the test. A secondary y-axis shows the O2 concentration in
percent by volume. The red portion on the graph represents the part of experiment where the opposed-
flow velocity was 10 cm/s. Similarly, the green and purple regions represent flow speeds of 6 and 5 cm/s,
respectively.


Figure 5.1.-BASS-II duct (Ref. 4). Absolute spread rate (Vf). Opposed-flow velocity (Vg).


NASA/TM-20210011385 56




TABLE 5.1.-TWENTY BURNING AND SUPPRESSION OF SOLIDS-II (BASS-II) TESTS


<table>
 <tr>
  <th>Test<br/>no.</th>
  <th>Thickness,<br/>mm</th>
  <th>Width,<br/>cm</th>
  <th>One or<br/>two sides<br/>burning</th>
  <th>Velocity,<br/>cm/s</th>
  <th>Spread rate,<br/>mm/s</th>
  <th>Burn time,<br/>min</th>
  <th>Initial O2,<br/>vol%</th>
  <th>Final O2,<br/>vol%</th>
 </tr>
 <tr>
  <td>M1</td>
  <td>1</td>
  <td>2.2</td>
  <td>1</td>
  <td>9</td>
  <td>0.071</td>
  <td>6.4</td>
  <td>22.2</td>
  <td>21.9</td>
 </tr>
 <tr>
  <td>M2</td>
  <td>3</td>
  <td>2.2</td>
  <td>1</td>
  <td>20 and 15</td>
  <td>0.052 and 0.033</td>
  <td>22.9</td>
  <td>22.2</td>
  <td>21.2</td>
 </tr>
 <tr>
  <td>M3</td>
  <td>5</td>
  <td>2.2</td>
  <td>1</td>
  <td>10 and 20</td>
  <td>0.029 and 0.024</td>
  <td>20.1</td>
  <td>20.8</td>
  <td>19.7</td>
 </tr>
 <tr>
  <td>M4</td>
  <td>5</td>
  <td>2.2</td>
  <td>2</td>
  <td>5 and 3</td>
  <td>0.045 and 0.033</td>
  <td>19.8</td>
  <td>21.8</td>
  <td>19.8</td>
 </tr>
 <tr>
  <td>M5</td>
  <td>3</td>
  <td>2.2</td>
  <td>2</td>
  <td>10</td>
  <td>0.071</td>
  <td>27.2</td>
  <td>22.2</td>
  <td>19</td>
 </tr>
 <tr>
  <td>M6</td>
  <td>1</td>
  <td>2.2</td>
  <td>2</td>
  <td>10 and 8</td>
  <td>Not tracked</td>
  <td>16.8</td>
  <td>21.8</td>
  <td>20.7</td>
 </tr>
 <tr>
  <td>M7</td>
  <td>1</td>
  <td>1.2</td>
  <td>2</td>
  <td>10, 6, 5, and 3</td>
  <td>0.106, 0.099, 0.083, and 0.07</td>
  <td>18.4</td>
  <td>18.9</td>
  <td>18.4</td>
 </tr>
 <tr>
  <td>M8</td>
  <td>2</td>
  <td>1.2</td>
  <td>2</td>
  <td>10, 6, and 5</td>
  <td>0.057, 0.056, and 0.04</td>
  <td>25.2</td>
  <td>19.1</td>
  <td>18.2</td>
 </tr>
 <tr>
  <td>M9</td>
  <td>3</td>
  <td>1.2</td>
  <td>2</td>
  <td>14</td>
  <td>0.025</td>
  <td>16.8</td>
  <td>18</td>
  <td>17.6</td>
 </tr>
 <tr>
  <td>M10</td>
  <td>4</td>
  <td>1.2</td>
  <td>2</td>
  <td>15 and 10</td>
  <td>0.0373 and 0.03</td>
  <td>30.5</td>
  <td>20.1</td>
  <td>18.6</td>
 </tr>
 <tr>
  <td>M11</td>
  <td>5</td>
  <td>1.2</td>
  <td>2</td>
  <td>21, 15, and 13</td>
  <td>0.048, 0.028, and 0.022</td>
  <td>28.5</td>
  <td>20</td>
  <td>18.5</td>
 </tr>
 <tr>
  <td>M12</td>
  <td>2</td>
  <td>2.2</td>
  <td>2</td>
  <td>12 and 10</td>
  <td>Not tracked</td>
  <td>16.2</td>
  <td>21.7</td>
  <td>20.4</td>
 </tr>
 <tr>
  <td>M13</td>
  <td>4</td>
  <td>2.2</td>
  <td>2</td>
  <td>6, 5, and 4</td>
  <td>0.047, 0.035, and 0.033</td>
  <td>20.5</td>
  <td>20.8</td>
  <td>19</td>
 </tr>
 <tr>
  <td>M14</td>
  <td>2</td>
  <td>2.2</td>
  <td>1</td>
  <td>15, 14, and 10</td>
  <td>0.0624, 0.055, and 0.0353</td>
  <td>15.4</td>
  <td>22.2</td>
  <td>21.6</td>
 </tr>
 <tr>
  <td>M15</td>
  <td>4</td>
  <td>2.2</td>
  <td>1</td>
  <td>20</td>
  <td>0.045</td>
  <td>22.0</td>
  <td>21</td>
  <td>20</td>
 </tr>
 <tr>
  <td>M16</td>
  <td>1</td>
  <td>2.2</td>
  <td>2</td>
  <td>5, 3, and 2</td>
  <td>0.144, 0.1309, and 0.1062</td>
  <td>8.4</td>
  <td>19.2</td>
  <td>18.7</td>
 </tr>
 <tr>
  <td>M17</td>
  <td>2</td>
  <td>2.2</td>
  <td>2</td>
  <td>5, 4, and 3</td>
  <td>0.053, 0.042, and 0.026</td>
  <td>30.7</td>
  <td>18.8</td>
  <td>17.1</td>
 </tr>
 <tr>
  <td>M18</td>
  <td>3</td>
  <td>2.2</td>
  <td>2</td>
  <td>10 and 8</td>
  <td>0.026 and 0.013</td>
  <td>25.5</td>
  <td>17.9</td>
  <td>16.8</td>
 </tr>
 <tr>
  <td>M19</td>
  <td>4</td>
  <td>2.2</td>
  <td>2</td>
  <td>10 and 6</td>
  <td>0.027 and 0.0159</td>
  <td>25.7</td>
  <td>19</td>
  <td>17.4</td>
 </tr>
 <tr>
  <td>M20</td>
  <td>5</td>
  <td>2.2</td>
  <td>2</td>
  <td>10</td>
  <td>0.012</td>
  <td>16.5</td>
  <td>18</td>
  <td>17.4</td>
 </tr>
</table>


Figure 5.2.-Position versus time graph for test M8. Red, green, and purple symbols at
constant flow are overlaid on overall test sequence blue symbols.


NASA/TM-20210011385 57




Figure 5.3.-M17 still images at different flow velocities. Last image is just before extinction as flow is turned off.


Figure 5.3 shows flame still images taken by the Nikon camera during one experiment as the flow is
turned down incrementally. O2 is also decreasing slightly during the experiment. Soot decreases as flow
decreases, and flame is all blue prior to extinction.
Flat PMMA samples have been burned in the narrow channel apparatus (NCA) to simulate microgravity
conditions (Refs. 7 and 8). In the flight experiment, five thicknesses of PMMA slab (1 to 5 mm), in two
widths (1.2 and 2.2 cm), and one-sided versus two-sided burning were studied in various O2 concentrations
(Refs. 9 to 11). Flow velocity was varied to obtain spread rates at different flow conditions. Some tests
lasted more than 30 min. The goal of these experiments is to begin gathering data for sample materials of
finite thickness, in which case the sample regression and consumption plays a more important role than
when the sample is extremely thin (Refs. 7 and 8). The objective was to obtain microgravity data for flame
spread over a thick fuel and compare the results to data from the normal-gravity NCA that uses a small-
height flow duct to suppress buoyant flow. Quenching extinction data was also obtained at finite flow rates
for most of the tests. Preliminary comparisons have been published (Refs. 7 and 10).
There was a clear difference in how the material burned as ambient O2 concentration was decreased.
At near-air O2 concentrations, the flames spread over the fuel surface without burning through for both
one-sided and two-sided samples. As O2 concentrations were reduced to approximately 19 percent
however, the flames could no longer spread across the surface of the two-sided fuel, but rather completely
consumed the fuel from the trailing edge. This is shown in Figure 5.4 for 2-mm-thick by 2.2-cm-wide
samples. Note that the velocities listed are the quenching velocities.
Figure 5.4(a) and (b) show regression behavior that is similar to what is found in normal-gravity
downward flame spread experiments. The fuel is completely consumed a few millimeters downstream of
the leading edge of the flame. The curved shape of the melt layer occurs because of heat losses to the
holder sides. There is a similarity to the last image in Figure 5.3 for a much thinner material, down to the
ring-shaped tail. The flame shape in Figure 5.4 also shows curvature due to heat losses to the sample
holder, increasing as the forced-flow velocity decreases.
Figure 5.4(c) and (d) are of a higher O2 level, showing how the flame spread across the material,
leaving behind a very long bubbled sample. The two sides of the flame extinguished separately on each
side of the sample, within a few seconds of each other. Figure 5.4(e) and (f) is a single-sided sample
whose flame was quite weak despite the high flow rate and the high O2 concentration. Heat loss to the
metal substrate clearly weakened this flame. It too left behind a long bubbled sample.
Spread rates decrease as thickness increases, and also decrease as forced-flow velocity decreases
(Ref. 10). Figure 5.5 shows that, for the one-sided samples, there was a clear trend that as thickness
increased, the O2 concentration for extinction decreased but the forced-flow velocity for extinction
increased. For the two-sided samples that spread across the surface, there was not a clear trend with
thickness, but the extinction velocities were significantly lower than for the one-sided samples, indicating
that heat loss to the substrate for the one-sided flame was significantly greater than the two-sided flame
without a substrate. There was no clear dependence on thickness for the extinction limits for both the 1- and


2.2-cm-wide regressing samples, but the 1.2-cm-wide samples did extinguish approximately 1 percent O2
higher than the 2.2-cm-wide samples, most likely due to increased relative heat losses to the sample holder.


NASA/TM-20210011385 58




Figure 5.4.-Polymethylmethacrylate (PMMA) slab tests. 2-mm-thick by 2.2-cm-wide PMMA slab tests.


(a) Preextinction flame, two sided, 18.8 percent O2, 3 cm/s. (b) Postburn sample from (a). (c) Preextinction flame,


two sided, 21.7 percent O2, <1 cm/s. (d) Postburn sample from (c). (e) Preextinction flame, two sided, 22.2 percent
O2, 11 cm/s. (f) Postburn sample from (e).


Figure 5.5.-Extinction limits for Miller and Wichman tests. Symbol sizes and numbers
reflect fuel thickness, and other geometry variations are noted in legend.


NASA/TM-20210011385 59




## 5.4 Oxygen Concentration Analysis


The BASS hardware does not have a provision to measure O2 concentration throughout the entire
experiment. We have O2 data available at only the start and end of the test. Assuming a linear profile
between these two points; we made O2 concentration graphs for each test (see Figure 5.2 for an example).
This helps us estimate the O2 concentration at any given time during the experiment. Next, the average O2
concentration was calculated for each flow speed. Plots were created summarizing the average O2
concentration (vol%) versus opposed-flow speed (cm/s) for the one-sided and two-sided tests separately.
The data points on these graphs are characterized according to the flame spread rate. Additionally, the
data points at which the flame extinguishes are also added to the summary graphs to see the effects of
varying O2 concentration through the duration of test. This analysis will serve as a reference point when
more BASS operations are conducted in the future.


### 5.5 Numerical Modeling


We are modeling combustion of flat PMMA samples in microgravity using Fire Dynamics Simulator
(FDS; v5.5.3; National Institute of Standards and Technology (NIST)) (Ref. 12), which is a
computational fluid dynamics model of fire-driven fluid flow. The entire modeling for BASS-II is done
in Direct Numerical Simulation (DNS) mode because of the laminar conditions and small domain. The
model employs the same test sample and approximate BASS flow duct geometry as the experiment. The
results are viewed in Smokeview (NIST), which is a visualization package that goes with FDS. The
experimental data gave upstream velocity at several points using an anemometer. A flow profile for the
inlet velocity is obtained using MATLAB® (The MathWorks, Inc.) and input into the model (note that the
measured flow profile for the BASS-II duct is quite irregular). Figure 5.6 shows the geometry setup for
the model.


Figure 5.6.-Geometry setup for two-dimensional model. Polymethylmethacrylate (PMMA).


NASA/TM-20210011385 60




Figure 5.7.-Smokeview (National Institute of Standards and Technology (NIST)) heat release rate in kW/m2.


this case, the fuel sample used was 3 mm thick. The averaged opposed-flow rate is 10 cm/s. A


For


grid size of 0.389 mm in the x direction and 0.376 mm in the z direction was used for the computation. At
the start of simulation, we have only cold flow. The flow is allowed to stabilize for 1 s of simulation time
and then the igniter is turned on. It is on for around 5 s and then ramped down and finally turned off.
Figure 5.7 shows the heat release rate (HRR) per unit area profile for this case. The maximum HRR
obtained in the two-dimensional simulation was 225 kW/m2. Smokeview can also be used to obtain
quantities like temperature, mass flux, net heat flux, etc.


### 5.6 Experimental and Modeling Results


Currently, we have formed summary graphs for one-sided and two-sided BASS-II experiments that
show certain behaviors. Shown in Figure 5.8 is a summary graph for two-sided burns with data from the
model as well.
As you see, the graph illustrates that the higher the flow velocity, or the thinner the sample, the
higher the spread rate is. The triangles represent the two model data points, which show a much higher
spread rate than experiments (Refs. 9 and 10). On further observation, we can see that the plot exhibits a
clear width effect. For thin fuels (1-mm-thick), especially, the 2-cm-wide samples show a higher spread
rate than the 1-cm-wide samples. These trends will help researchers decide sample sizes for future
planned experimentation aboard ISS.
As shown in Figure 5.9, the one-sided samples burned more slowly than the two-sided samples, and
also needed a higher opposed-flow rate to keep burning. Symbol size reflects the estimated O2
concentration at the velocity, based on an assumed linear O2 decay during the test.


NASA/TM-20210011385 61




Figure 5.8.-Flame spread rate versus opposed-flow velocity (two-sided tests).


Figure 5.9.-Flame spread rate versus opposed-flow speed (one-sided tests).


NASA/TM-20210011385 62




## 5.7 Conclusions


The Burning and Suppression of Solids (BASS) experiments gave some of the first ever data
regarding combustion of thick fuels in microgravity. The two-sided summary graphs show that for thin
fuels, sample width affects the spread rate. In general, the flames spread faster for two-sided burns
compared to one-sided burns. The greater the thickness of the fuel, the greater is the time taken for the
flame to spread and so the lower is the spread rate. This is clearly evident in the different thicknesses that
we have tested. The model currently predicts much higher spread rates than those obtained in the
experiment. We need to modify chemical kinetics and material properties to improve model accuracy and
results.


### 5.8 Acknowledgments


The research at San Diego State University was funded by NASA Grant NNX10AD96A. We thank
Dr. Subrata Bhattacharjee for his helpful discussions and advice regarding the Burning and Suppression
of Solids (BASS) data collected. Recognition is also due to graduate students Garrett Bornand and Greg
Sullivan for their help and contribution.


### 5.9 References


1. National Aeronautics and Space Administration: Flammability, Offgassing, and Compatibility Requirements and Test Procedures. NASA-STD-6001B, 2011.

2. Olson, S.L., et al.: Sounding Rocket Microgravity Experiments Elucidating Diffusive and Radiative Transport Effects on Flame Spread Over Thermally Thick Solids. Combust. Sci. Technol., vol. 176, no. 4, 2004, pp. 557-584.

3. Reckart, T.A.: Space Flight System at GRC: Burning and Suppression of Solids (BASS). National Aeronautics and Space Administration, 2014. https://www1.grc.nasa.gov/space/iss- research/msg/bass/ Accessed June 21, 2021. 4. Bhattacharjee, S.: Research on Flame Spread at SDSU: The Bhattacharjee Group. http://flame.sdsu.edu/ Accessed August 27, 2015. 5. Wikipedia contributors: Microgravity Science Glovebox. Wikipedia, The Free Encyclopedia, 2021. https://en.wikipedia.org/wiki/Microgravity_Science_Glovebox Accessed June 22, 2021. 6. Klimek, Robert; and Wright, Ted: Spotlight-8 Image Analysis Software. NASA/TM-2006-214084, 2006. https://ntrs.nasa.gov 7. Bornand, G.R., et al.: Opposed-Flow Flame Spread in a Narrow Channel Apparatus Over Thin PMMA Sheets. Presented at the 8th U.S. National Combustion Meeting, paper 070FR-0418, 2013. 8. Bornand, Garrett Randall: Polymethylmethacrylate Combustion in a Narrow Channel Apparatus Simulating a Microgravity Environment. M.S. Thesis, San Diego State Univ., 2015. 9. Winter, Kelsey Gloria: Experimental Measurements of PMMA Combustion in Simulated Microgravity Along the Normoxic Curve. M.S. Thesis, San Diego State Univ. 2019.


10. Shah, Tirthesh J., et al.: Modeling and Analysis of Intermediate Thickness PMMA Sheets Burning in
Microgravity Opposed Flow. Presented at the Western States Section of the Combustion Institute-
Fall 2015 Meeting, paper 134HC-0056, 2015.


11. Shah, Tirthesh Jayesh: Flame Spread Over Thick Polymethylmethacrylate Samples in a Simulated
and Actual Microgravity Environment. M.S. Thesis, San Diego State Univ., 2016.
12. McGrattan Kevin, et al.: Fire Dynamics Simulator (Version 5) User's Guide. NIST Special
Publication 1019-5, 2007.


NASA/TM-20210011385 63




1. Individual Principal Investigator Report: Olson


6.1 Microgravity Flammability Boundary for Polymethylmethacrylate Rods in Axial
Stagnation Flow: Experimental Results and Energy Balance Analyses


### 6.1.1 Abstract


For the first time, a series of concurrent rod flammability tests were conducted in microgravity aboard
the International Space Station. A small flow duct was used to create 0- to 55-cm/s flows past the three sizes
of clear and black polymethylmethacrylate rods. The ambient O2 concentration in the Microgravity Science
Glovebox was varied from 13.6 to 22.2 percent. O2, CO2, and CO gas sensors provided initial and final
readings for each test and indicate that the flames are globally stoichiometric at higher O2 concentrations,
but become more globally fuel rich as the minimum O2 concentration is approached due to excess
pyrolyzate leakage out of the open tail of the hemispherical flames. Quenching extinction occurs at very low
forced flows, where the flame shrinks to a hemispherical blue flame and oscillates with increasing amplitude
just before going out. Blowoff extinction is initiated by the formation of a hole in the flame sheet in the
stagnation region of the flame. A critical Damköhler number formulation is applied across the flammability
boundary, and the critical flame temperature is derived. This critical flame temperature is then used in a
Nusselt number correlation to estimate the convective heat flux to the stagnation region of the rod. A model
of surface energy balance is formulated that uses the critical flame temperature and convective heat flux to
derive the mass burning rate along the boundary. The rod regression rates calculated from this model
compare favorably with the experimental measurements. The surface energy balance reveals that along the
blowoff branch, heat losses are negligible whereas in the quenching region, surface radiative loss dominates.
At the bottom of the flammability map, the transition from blowoff to quenching occurs when the
convective flows become the same order of magnitude as diffusive flows, shifting the critical Damköhler
number from residence time limitations to diffusive time limitations.


### Symbols


a stretch rate, 3/2 U/r (r/ro)1/2, s-1
as absorptivity of the PMMA surface
A area, cm2
Ar cross section of rod
Ah hemispherical rod tip surface area = 2 Ar
Bi Biot number, h r/ λs
D diameter
Da Damköhler number, Equation (6.2), normalized by 7.35×107 (Ref. 1)
E activation energy, 1.45×105 J/mol
F surface to flame hemispherical radiative view factor, = 0.93
h heat transfer coefficient
L length of the flame, stagnation standoff to flame tails, cm, or rod initial length
Lo rod initial length, 5.9 cm
Lv latent heat of vaporization, 1700 J/g
 m′′ hemispherical surface average burning rate, g/cm2 s, =Vr ρs∙Ar/Ah
Nu Nusselt number, convective heat flux and conductive heat flux, Equation (6.3)
Pe Peclet number, LoV/αs
Pr Prandtl number of air at Tm, 0.69
 q′′ heat flux, W/cm2, Equation (6.4)


NASA/TM-20210011385 64




q
r
R
Re
s
T
t
ts
∆T
U
UD
Vr
X
Y
y
α
β
ε
λ
ν
ρ


θ


σ
ℓ
τ


heating rate, W, Equation (6.4)
radius, cm
ideal gas constant, 8.314 J/(gmol K)
Reynolds number, UD/ν
flame standoff distance, measured to outer bright cyan zone of flame, cm
temperature, Tm = 800 °C
time, s
solid-phase response time, 0.7 r2/αs, s
Tcrit - Ts
forced-flow velocity, cm/s
diffusion velocity, 2 cm/s
measured rod tip regression velocity, cm/s
percent by volume (mole percent)
nondimensional y = y/L
distance along the rod, cm
thermal diffusivity of air at Tm, 1.19 cm2/s, of PMMA 1.2×10-3 cm2/s
preexponential constant, 1.3×1016 cm3/ gmol s
surface emissivity, 0.8 surface, 0.02 gas, also surface absorptivity via Kirchhoff's law
thermal conductivity of air at Tm, 0.000577 W/cm K, or of solid at T∞, 2.09×10-3 W/cm K
kinematic viscosity at Tm, 0.822 cm2/s
gas density of air at Tm, 0.0441 g/cc, solid density 1.19 g/cc
nondimensional temperature
Stefan-Boltzmann constant, experimental, 5.729×10-12 W/cm2 K4
thermal length scale, cm, (αg/a)1/2
nondimensional solid phase response time, = t/ts


### Subscripts


conv convective
crit flame extinction condition
D diffusion
f fuel, assumed unity at the fuel surface
g gas
ign ignition
m mean, at 800 K
o base size of rod, 0.318 cm
O2 oxygen
rad radiative
s surface, at 675 K, or solid
tot total feedback to surface
vap vaporization


- ∞ ambient, at 300 K

1. Introduction Early work (Ref. 2) on flammability limits has demonstrated that using a hemispherical stagnation flow geometry provides a good way to obtain the flammability limits of various fuels as a function of upward flowing oxidizer gas. Similar limiting O2 concentrations (13 to 14 percent) and flame temperatures (1,450 to


NASA/TM-20210011385 65




1,500 °C) have been noted for many heavier hydrocarbons. The stagnation flow geometry is amenable to
asymptotic analyses (Refs. 3 and 4), numerical modeling (Refs. 5 to 7), and experimental blowoff extinction
work for both axisymmetric and two-dimensional geometries (Refs. 8 to 11).
The importance of radiative heat loss was examined (Refs. 4 and 5) and found to primarily reduce the
flame temperature. The flammability map in terms of O2 and stretch rate a (Ref. 5) was shown to consist
of a blowoff and new quenching branch where the low power flame (due to the reduced temperature) is
too weak to compensate for the surface radiative heat loss. It was pointed out that this is likely only
observable in microgravity. Experimentally, the first observed solid fuel quenching extinction limits were
observed in microgravity opposed-flow flame spread tests over thermally thin cellulose fuel (Ref. 12).
Very few solid fuel stagnation flow extinction studies have been performed in reduced gravity to
eliminate buoyant flow effects. Concurrent-flow flame spread with plastic rods was tested aboard the Mir
Space Station in the Skorost hardware (Ref. 13). The extruded polymethylmethacrylate (PMMA),
polyoxymethylene (POM), and high-density polyethylene (HDPE) rods all showed the same tendency to
melt beneath the flame and form accumulating molten balls on the stagnation end of the rod, with the
flame wrapped around the molten ball. At low flows, the small hemispherical flame at the stagnation tip
of the rod propagated simply through rod regression (bulk burning) rather than through a concurrent
flame spread along the rod. Flames survived at airflow less than 1 cm/s.
This stagnation geometry was selected for this work to study material flammability in microgravity.
Concurrent-flow flame spread tests burned an axisymmetric cylindrical PMMA rod having low heat
losses to the downstream sample support pin. Other intrinsic heat losses (surface radiation loss and
conduction along the rod axis) will be estimated in Section 6.1.5.5. The objective of these tests was to
obtain the lower portion of the concurrent microgravity flammability map as a function of ventilation
flow and ambient O2 concentration.


### 6.1.3 Experimental Setup


The BASS-II hardware used for these tests has been described in detail in Reference 14. It consists of
a black-anodized flow duct that provides a low-reflection backdrop for imaging flames with a color video
camera at 30 frames per second and an orthogonal digital still camera (4,320 by 2,968 pixel images) at
~1 frame per second. The tests were performed in the 250-L free volume Microgravity Science Glovebox
(MSG) in the Destiny Lab of the International Space Station (ISS). The hardware setup is shown in
Figure 6.1. The flow duct measured 7.6 by 7.6 by 17 cm with rounded internal corners for smooth laminar
flow through the duct. The front window opened to install samples and igniters. A top window allowed
still camera imaging. A noncalibrated radiometer in the downstream top back corner of the flow duct
provided a relative flame strength reading at 5 Hz. The three primary variables were flow velocity
through the duct, PMMA rod radius, and O2 concentration of the working volume.
The flow was generated using a small variable-speed fan at the upstream end of the duct. The voltage
to the fan was displayed and could be set. Up to two flow restrictors could be used at the fan inlet to
increase the pressure drop and thus change the output flow range. With no restrictors, the maximum flow
velocity was ~55 cm/s, and with two restrictors this was reduced to a maximum of ~35 cm/s. The flow
then passed through a honeycomb flow straightener and an inlet screen to reduce swirl. An
omnidirectional spherical air velocity transducer (TSI Incorporated 8475) was positioned between the
honeycomb and the screen and was used to measure the steady-state flow through the duct. The air
velocity transducer probe had a response time of approximately 1 min and its digital display only read out
to the units place (no decimals) yielding an effective resolution of ±0.5 cm/s. A fan calibration was
performed at the end of each operational day to associate the fan voltage with the flow velocity for each
flow restrictor, after the fan had adequate time for warmup.


NASA/TM-20210011385 66




To obtain the desired O2 concentration for the test, the initial ISS air filling the MSG working volume
was diluted using N2 as described in Reference 14. A continuously stirred tank reactor (CSTR) model was
used to time the N2 flow to obtain the desired initial O2 concentrations down to as low as 13.6 percent O2.
O2 sensor readings, calibrated with the onboard mass spectrometer, provided initial and final O2
concentrations for each test. The readings were used to verify the CSTR model and measure the O2
consumption within the test. Onboard CO and CO2 sensors were also used to provide initial and final
product gas concentrations for each test, to evaluate the average burning efficiency for each test.
Clear cast PMMA rods, shown in the top left corner of Figure 6.1, were mounted inside the flow duct
for each test. The stagnation tips of the rods were initially hemispherical. Three radii r of clear cast
PMMA cylindrical rods were tested (primarily 0.318 cm; but also 0.476 and 0.635 cm). Two black
PMMA rods (r = 0.318 cm, blackened with a small amount of soot during polymerization) were also
tested, but no obvious differences in flammability were noted compared to the clear rods.
A control box external to the MSG allowed the astronaut to dynamically change the fan voltage, set
the N2 flow, turn the igniter on and off, and adjust the radiometer gain, as shown in the lower right corner
of Figure 6.1. The Burning and Suppression of Solids-II (BASS-II) science team monitored the real-
time video on the ground and talked directly to the astronaut running the experiment, calling up real-time
flow changes, still camera imaging adjustments, ignition instructions, etc.
The samples were ignited manually by the astronaut at the initially hemispherical stagnation tip with a
hot-wire igniter, typically at a flow speed of 5 cm/s. The hook-shaped 29-gauge Kanthal® wire igniter had
a resistance of 1 Ω and was powered by a 4-A circuit. Ignition times to achieve sustained flames varied
and could be as long as 230 s. At very low O2 concentrations, even longer ignition times (up to 500 s) did
not result in a sustained flame even when the initial flow was varied up to 10 cm/s and down to 2 cm/s.
Once successfully ignited, the flow was reduced incrementally until the flame extinguished via


Figure 6.1.-Hardware used for Burning and Suppression of Solids-II (BASS-II)
tests. Gas sensors are not shown. Polymethylmethacrylate (PMMA). Microgravity
Science Glovebox (MSG).


NASA/TM-20210011385 67




quenching. For blowoff tests, the flow was increased until blowoff occurred. After each test, there was a
minimum of 9 min for cooldown to safe sample touch temperatures before the setup of the next
experiment could begin.
Complementary 5.18-s Zero Gravity Research Facility blowoff drop tests were conducted to compare
with long-duration microgravity, using the microgravity wind tunnel drop rig (Ref. 15). The rod was
ignited in 1g to establish a flame at a flammable O2 flow. The gas flow source was switched to a reduced
O2 level and the package dropped just as this test oxidizer flow reached the flame zone. Blowoff
extinction could be observed in the drop tests because the characteristic time for extinction was less than
the available drop time. However, it was not possible to observe quenching extinction because its
characteristic time was substantially longer than the available drop time.


### 6.1.4 Experimental Results


### 6.1.4.1 Ignition Delay Time


The astronaut would manually position the igniter within a millimeter of the tip of the rod and
activate the igniter until a stable flame was achieved. It could be difficult to see the flame in the glare of
the igniter, so the astronaut would turn off the igniter to assess flame viability. If the flame appeared to be
going out, the astronaut would quickly turn the igniter back on to strengthen the flame and again check
flame viability after a few seconds of applying power. This igniter on and off cycle might occur several
times in a given test. The ignition delay (tign) in each test was defined as the time from when the igniter
was first turned on to the last time the igniter was turned off and a stable flame persisted. Ignition
generally occurred at a forced flow of 5 cm/s, so the ignition delay is plotted in Figure 6.2 against the
initial O2 concentration alone. The symbol sizes reflect the initial rod radius. Because the igniter is
positioned and activated manually, there is some inherent scatter in the ignition time, but some trends are
clear.
At higher O2 concentrations, ignition occurred within approximately 40 s. Below an initial O2
concentration of 16 percent, the ignition delay time increased significantly. Larger rods take longer to
ignite, especially at lower O2 concentrations (up to 230 s). This suggests that the weaker flames at low O2
cannot be sustained when the fuel rod is cold because too much of the heat from the flame is lost to
conduction into the fuel. Only after a significant ignition time does the initially cold fuel rod become
warm enough to allow the flame to persist. Section 6.1.5.5 examines the importance of conductive heat
loss down the rod.
Below an initial O2 concentration of ~14.5 percent O2, a sustained ignition could not be achieved even
though flames were observed when the igniter was on and briefly after the igniter was turned off before
extinguishing.
On the right axis of Figure 6.2, the ignition delay is normalized by the characteristic solid phase
response time (ts = 0.7 r2/αs) where α is the thermal diffusivity of the solid. If the sample is not ignited within
this nondimensional time τ (the empirical factor 0.7 is selected so that τ = 1 at the ignition limit), it is likely
not flammable, as shown for all values τ ≥ ~1 that fall below the ignition limit of ~14.5 percent O2.
Despite this limiting O2 concentration for ignition, flames ignited at a higher O2 survived to final O2
concentrations as low as 13.6 percent O2, indicating that the high heat loss to the initially cold rod will
quench a postignition flame while a developed solid phase temperature profile allows a sustained flame
down to these low ambient O2 concentrations.
This difference between O2 ignition limits and O2 extinction limits is an important factor to consider
for a flammability test. For example, NASA's Test 1 (Ref. 16) is an upward flame spread test that has a
fixed ignition time of ~25 s, which is shown in Figure 6.2 as the bottom shaded region. If the material is


NASA/TM-20210011385 68




not ignited by this time, it passes the test. However, as one can see from Figure 6.2, a longer ignition time
may successfully ignite the material, especially at the lower O2 concentrations.


Figure 6.2.-Ignition delay time (left axis) and nondimensional ignition delay time τ
(right axis) as function of initial O2 concentration. Successful ignitions occur in
nondimensional ignitable region, and with ignition delay times as long as 230 s.
NASA Test 1 25-s ignition time may be too short for flammability test and so may
be an ignition test.


### 6.1.4.2 Quenching Extinction


Samples burned within the flow duct and the combustion products exited the duct and mixed with the
gas in the 250-L free working volume of the MSG, so the O2 very gradually decreased during the test. To
determine the quenching limit, the flow was decreased incrementally, and the solid-phase temperature
distribution was allowed to equilibrate to the new flame for at least 100 s before the flow was changed
again, to ensure each flame was steady. Quench tests lasted up to 28 min. Near-quenching flames for each
rod size are shown in Figure 6.3(a) to (c). Flow and O2 are not the same, but each represent the lowest O2
test for that rod size. These all-blue flames are roughly hemispherical in shape.
Figure 6.4 shows a detailed time history of flame measurements (flame length, width, standoff
distance, aspect ratio, rod tip position, and radiometer reading) of the lowest O2 quenching test, where the
initial O2 setting was 14.8 percent O2 (by volume) and the final O2 reading was 13.6 percent O2. The
prequenching flame from this r = 0.476 cm rod radius test is the center top image in Figures 6.3. The flow
was incrementally decreased throughout the test, as shown by the red stepped line. The flame length
stopped growing at the 2- to 1.5-cm/s flow change, and shortly thereafter the rod regression reached an
apparently steady-state regression rate of 0.0385 mm/s.
Flame measurements show that the flame standoff distance is nearly constant. The flame length
asymptotes down to nearly constant length at each subsequent flow until the last one leading to extinction.
The flame length and radiometer signal track each other very closely. The flame width shows a smooth


NASA/TM-20210011385 69




increase up to the 2- to 1.5-cm/s flow change, and then a slow decrease until the last flow change where it
decreases more quickly. The aspect ratio (L/W) decreases incrementally to 0.5 at extinction, indicating a
hemispherical flame at the quenching limit. Quenching occurred over 100 s after the last flow change,
which is on the order of the solid-phase response time ts. The cause of quenching extinction is evaluated
further in Section 6.1.5.3.


Figure 6.3.-Representative limit flames for three rod sizes tested. Near-quenching limit
flame (a) Radius r = 0.318 cm. (b) r = 0.476 cm. (c) r = 0.635 cm. Blowoff after
stagnation tip opens up. (d) r = 0.318 cm. (e) r = 0.476 cm. (f) r = 0.635 cm.


NASA/TM-20210011385 70




Figure 6.4.-Time history of flame measurements and flow from lowest O2
quenching test for 0.476-cm-radius rod.


Figure 6.5.-Flame length compared to clear bubble layer length. Inset flame image
shows bubble layer length. Data is from same test as Figure 6.4.


NASA/TM-20210011385 71




Figure 6.6.-Flame oscillations prior to quenching extinction, detected by radiometer. Data is from same test as
Figure 6.4. Inset graph shows oscillation frequency to be steady at 1.1 Hz.


The flame length minus the standoff distance matches the clear bubble layer length just before each
flow change, as shown in Figure 6.5, indicating that the bubble layer formation is due to heat flux from
the flame, as shown in the flame image inset in Figure 6.5 (at 1,100 s). The dense small clear bubble layer
(indicated by the arrow in the flame inset image) tracks the length closely except just after the flow is
turned down. The flame adjusts immediately to the flow change, but the bubble layer length can only
shrink at the rate of the tip regression. It is interesting that at quenching extinction, the bubble layer length
has shrunk to approximately the same length as the rod diameter, which is another indication of the
hemispherical shape of the flame prior to quenching extinction.
After the last flow change, the flame length does not reach a steady size, but shrinks and begins to
oscillate. The radiometer signal provides the best temporal reading of these oscillations. The radiometer
reading for the last 30 s of the test are shown in Figure 6.6. The radiometer signal oscillates at
approximately 1.1 Hz as shown in the inset to Figure 6.6, and drops to a value of 1.05 over a period of a
few seconds followed by a large oscillation. The flame appears to recover back to smaller scale
oscillations. After a few seconds, the radiometer signal again drops to 1.05 followed by another large
oscillation. The flame then extinguishes. A still flame image also inset into Figure 6.6 shows a similar test
that captured a flame just prior to extinction, showing the flame length shrinks forward to basically the
flame standoff distance on its way to quenching extinction.
These oscillations are very similar to those observed for candle flames in a quiescent environment
(Ref. 17), since the ~1-cm/s convective flow is at the level of diffusive flows. The open tail of the small
hemispherical flame allows fuel vapor to escape downstream. This mixes with O2 and forms a flammable


NASA/TM-20210011385 72




mixture. The flame flashes downstream through this mixture and consumes the reactants. This larger
flame locally depletes the O2 concentration, weakening the flame briefly. For a large amplitude
oscillation, the local O2 depletion becomes low enough to destabilize the flame anchor at the stagnation
region, and the flame extinguishes entirely. The oscillation frequency is controlled by the diffusive
transport (mixing) rates of the reactants and the inherent heat losses (Ref. 17). The radiative loss has been
shown to have the same effect as changing the thermal-diffusivity of the reactants (Ref. 18) resulting in
oscillations with thermodiffusive characteristics even for unity Lewis number.


### 6.1.4.3 Blowoff Extinction


Blowoff limits were typically determined after a stable rod regression was established at a modest
flow speed. The astronaut would then turn up the flow to obtain blowoff. Blowoff was defined as the
instant when the stagnation region developed a hole (Ref. 19) as shown in the lower row of flame images
in Figure 6.3. The center blowoff image is of a 5.18-s Zero Gravity Research Facility drop test since no
ISS blowoff tests were obtained with the intermediate rod size. A green light-emitting diode (LED)
illuminates the drop test rod. The flames in the drop tower blowoff tests are significantly smaller than the
ISS flames, as can be seen in Figure 6.3, due to the reduced level of fuel preheating resulting from the
short burn time prior to blowoff. Previous research (Refs. 6, 7, 20, and 21) and Section 6.1.5.5 indicate
that blowoff extinction is not sensitive to heat losses.
After the stagnation region blows off, the subsequent annular flame leading edge would oscillate
upstream and downstream multiple times before completely blowing off. During one test, we attempted to
reestablish the envelope flame after local blowoff. Only once could we successfully reestablish the
stagnation region after local blowoff by quickly reducing the flow to a value below the blowoff velocity.
A second attempt was not successful.
The a and radiometer data from these blowoffs are shown in Figure 6.7. In each blowoff, the
astronaut quickly turns up the flow from a low a to a high a and the flame blows downstream. The
astronaut then quickly turns the flow down to a near the minimum flammability (discussed in
Section 6.1.4.4). Figure 6.7 shows that the two attempts were quite similar, but the results were not. For
the first blowoff, the flame hole is initially about 9 mm in diameter, but within 2 s moves back forward of
the rod tip position (yellow line in Figure 6.8) and closes up in 7 s after the flow is turned down, as shown
in Figure 6.8(a). The radiometer signal is higher since the flow is slightly higher and the flame is visibly
longer than the preblowoff flame.
A subsequent attempt 55 s later resulted in a slightly larger initial flame hole of 10 mm that was not
able to move forward of the flame tip and reestablish the stagnation region, as shown in Figure 6.8(b).
This 10-mm flame hole persisted for over a minute even after the flow was turned down again to the
initial flow before the flame destabilized and blew off completely.
While the flow profile was quite similar for the two blowoffs, the O2 had depleted more by the second
blowoff. This is apparent in the reduced sooting for the second preblowoff flame. This second blowoff is
interpreted as indicating that once the flame is stabilized farther than the thermal length downstream of
the stagnation region (ℓ = 2 mm), the flame is unable to repropagate upstream for the low O2 levels tested
(XO2 final = 14.5 percent for this test) even though the fuel is already preheated. This is consistent with
tests for opposed-flow flame spread over rods that were also done as part of BASS-II (Ref. 14), where
opposed-flow flame spread was not observed below 16.4 percent O2 at any flow.


NASA/TM-20210011385 73




Figure 6.7.-Time history of stretch rate a and radiometer signal for two local blowoffs for
0.318 cm rod.


Figure 6.8.-Sequence of still flame images from two local blowoffs. Images in each set are 1 s apart. Yellow
horizontal lines reflect position of rod tip. (a) Blowoff 1. (b) Blowoff 2.


### 6.1.4.4 Flammability Boundary


For each test, the flow speed at which the flames extinguished and the last flow speed at which a
stable flame was observed (or the flow at which the flame did not blow out in the drop time for drop


NASA/TM-20210011385 74




tests), along with the postburn O2 sensor reading were used to generate a flammability boundary, shown
in Figure 6.9. Error bars reflect the uncertainties in O2 and flow and are mostly smaller than the symbols.
The x-axis of Figure 6.9 uses a forced a, which is defined as a = (3/2)(U/r)(r/ro)½ where U is the free
stream velocity. The square root modifying factor is used to correct for the different rod sizes. The gas
phase ℓ scale (Ref. 7) is defined as ℓ = (α/a)1/2, which is proportional to r1/2 for a given velocity. All a are
normalized to the base rod radius (ro = 0.318 cm) using the ratio of these ℓ s.
The thick gray flammability boundary in Figure 6.9 represents the border between stable flames and
extinguished flames. Along this boundary, the flame is sensitive to stochastic perturbations that can lead
to extinguishment (Ref. 22). The O2 concentration (XO2) versus a boundary is defined by the combined
empirical equations shown by the red (quenching branch, exponential expression) and black (blowoff
branch, linear expression) dashed lines.


X O2 =6e xp( -0.5 a) +0.0167 +13.4 a (6.1)


The minimum in this boundary occurs at a = 8 to 12 s-1 at approximately 13.5 percent O2, in good
agreement with the predicted a at the minima in the flammability boundary (Refs. 6, 7, 20, and 21).
The drop tower blowoff data, given by the purple dashed line, agrees very well with the flight data.
The fact that the blowoff boundary is linear with flow makes it possible to extrapolate blowoff data down
to zero a and use that O2 value as an accurate but conservative estimate of the minimum O2 concentration
for material flammability in space. This may provide a consistent methodology to derate materials based
on normal-gravity flammability tests accounting for buoyant flow to ensure the material will not burn in
space.


Figure 6.9.-Flammability boundary obtained in Burning and Suppression of Solids-II
(BASS-II) tests with linear axis. Complementary drop tower test results are also shown.
International Space Station (ISS). Stretch rate (a). Final O2 concentration (XO2). Forced-
flow velocity (U). Rod radius (r).


NASA/TM-20210011385 75




The quenching branch is fitted using an exponential decay (red dashed curve). In this region, heat
losses dominate to cool the flame to extinction through the strong dependence of reaction rate in the
Arrhenius term, as was modeled by References 6, 7, 20, and 21, and will be evaluated in Section 6.1.4.3.
This boundary is very steep for small a when plotted on a linear x-axis as shown in Figure 6.9.
Figure 6.10 replots the same data as Figure 6.9 but with a logarithmic x-axis. Note that the classic U-
shaped flammability boundary is evident when a logarithmic x-axis is used. This expands the quenching
branch while making the linear blowoff branch appear curved. It also emphasizes the uncertainty in the
flow at the very low velocities (<1 cm/s) along the quenching branch. The minimum O2 concentration of


13.5 percent O2 at a of 8 to 12 s-1 is significantly lower than the observed upward flame spread limit of
15.4 percent O2 (in normal gravity with an additional 4-cm/s forced flow (Ref. 23)), indicating the
material remains flammable under the weak ventilation only obtainable in microgravity. This
"Goldilocks" zone of flow is unfortunately typical of spacecraft ventilation flows near surfaces.
Earthbound flammability tests need a reliable method to account for this extension of flammability in
microgravity environments. Extrapolation of the normal-gravity blowoff boundary to zero stretch may be
a viable method to estimate this enhanced flammability if a buoyant stretch can be included.


Figure 6.10.-Flammability boundary shown with logarithmic x-axis, which expands
quenching region and exhibits classic U-shaped flammability map. International Space
Station (ISS). Stretch rate (a). Final O2 concentration (XO2). Forced-flow velocity (U).
Rod radius (r).


NASA/TM-20210011385 76




#### 6.1.4.5 Flame Standoff Distance


The flame standoff distance at the stagnation point, just prior to extinction (blowoff or quenching),
was measured for each test using the high-resolution digital still images. These measurements are used in
Section 6.1.5.2 to estimate the convective heat flux from the flame to the rod in the stagnation region. The
standoff distances measured are at the outer boundary of the bright cyan edge (peak temperature) of the
flames shown in Figure 6.3.
The measured standoff distance as a function of O2 concentration is shown in Figure 6.11 for all three
radii and also for the type of extinction, quenching, or blowoff. The flame standoff distance shows a trend
reversal on the two sides of the flammability boundary. On the blowoff side, as O2 is reduced, the
standoff distance increases. There is a turning point at a minimum O2 concentration, and on the quenching
side, as O2 increases, the standoff distance also increases.
Figure 6.12 shows the same measured standoff distance data plotted against the a. The standoff
distance shows a seven-fold increase as a is reduced by two orders of magnitude. Error bars reflect the
uncertainty of the a at very low values due to the resolution limitations of the flow velocity sensor. A
power law curve fit to the data shows the standoff distance is approximately proportional to cube root of
the a, not the square root dependence of the characteristic ℓ predicted by theory (Ref. 7). The square root
dependence (dotted line in Figure 6.12) appears to capture the trend in the blowoff region, but not in the
quenching region.


Figure 6.11.-Flame standoff distance as function of oxygen, showing both
quenching and blowoff branches. O2 concentration (XO2).


NASA/TM-20210011385 77




Figure 6.12.-Flame standoff distance as function of stretch rate
a with power law fit. Forced-flow velocity (U). Rod radius (r).


Figure 6.13.-O2 consumed compared to CO2 generated.


NASA/TM-20210011385 78




#### 6.1.4.6 Gas Sensor Results


The initial and final O2, CO2, and CO readings were recorded for each test. Although flow and O2
concentrations do change within each test, the averages still provide insight into the overall processes.
The O2 consumed can be compared to the CO2 generated, as shown in Figure 6.13. While there is scatter
in the data, the linear trend agrees very well with the stoichiometric ratio for PMMA (6 O2 to 5 CO2). This
indicates that the O2 was burning primarily to the expected CO2 and water.
The CO produced is plotted against CO2 in Figure 6.14. There is a fairly linear relationship between
the two, with approximately 600 ppm of CO produced for every 1 vol% of CO2 produced. The CO to CO2
ratio is plotted against the initial O2 concentration in Figure 6.15, and shows that as the initial O2
concentration decreases, the CO to CO2 ratio increases. These values are an order of magnitude greater
than the 1g values found in the cone calorimeter for PMMA (Ref. 24), indicating very inefficient burning
at low ambient O2 levels in microgravity.
The O2 consumed and the fuel burned were used to estimate the global stoichiometry for each test.
The amount of rod burned away was measured from the still images in each test. The bubble layer effect
on density was not accounted for, so there is scatter in the data most likely due to this factor. The O2
consumed was calculated by using the MSG free work volume of 250 L (Ref. 14) and the ideal gas law.
The fuel to oxidizer molar ratio is divided by the stoichiometric ratio (1 monomer unit per 6 O2). The
resulting global stoichiometric ratios for each test are shown in Figure 6.16. At higher O2 concentrations,
the flames are nearly stoichiometric. At lower O2 concentrations, the global equivalence ratio increases.
This indicates that the limiting reactant is the O2 rather than the fuel. It is likely that at the low O2 levels
(and low flow rates) that there is significant fuel leakage out the open back of the flame. This is consistent
with the near-extinction oscillation mechanism of fuel leakage downstream, mixing, and flame flashback
through the premixed region. This is also consistent with the CO to CO2 ratio trend of inefficient burning.


Figure 6.14.-CO generated compared to CO2 generated.


NASA/TM-20210011385 79




Figure 6.15.-CO to CO2 ratio as function of final O2 concentration.


Figure 6.16.-Global equivalence ratio as function of initial O2 concentration.


NASA/TM-20210011385 80




#### 6.1.5 Analyses


In this section, the experimental flammability boundary (Eq. (6.1)) is applied to a constant critical
Damköhler number formulation (Section 6.1.5.1) to estimate the critical flame temperatures along the
extinction boundary. The critical temperatures and measured flame standoff distances are then used in a
Nusselt number correlation (Section 6.1.5.2) to estimate the convective heat flux to the rod from the flame
along the flammability boundary. A surface energy balance (Section 6.1.5.3) utilizes the deduced
convective heat flux to evaluate the importance of radiative exchange and heat losses on the blowoff
versus quenching sides of the extinction boundary. A comparison of measured versus predicted rod
regression rates is presented (Section 6.1.5.4). Lastly, the relative heat losses across the flammability
boundary are examined to understand the physics of the transition from blowoff to quenching. It should
be noted that a constant base rod size is used in all subsequent analysis so the correction factor for radius
in the a expression is unity.


### 6.1.5.1 Damköhler Number Analysis


The critical Damköhler number (Dacrit) analysis presented here is applied to both blowoff and
quenching sides of the flammability boundary since finite rate chemistry applies along the entire
flammability boundary. For both blowoff and quenching, the Dacrit becomes too small. At blowoff, the
flow rate is too large to allow the relatively fast reactions to occur, while at quenching, the reaction rate
becomes too small due to slow mixing of the reactants.
A critical Damköhler number (Dacrit) is defined as


- ( )( ) ( -E RTcrit ) reaction rate βρ X f X O2 e

- =


flow rate a


Dacrit =  (6.2)


flow time
reaction time


where β is the preexponential factor, ρ is the gas density at the mean temperature, Xf and XO2 are the fuel
and oxidizer concentrations, E is the activation energy, R is the ideal gas constant, and Tcrit is the critical
temperature.
The Dacrit is assumed to be constant along the entire flammability boundary (Ref. 1), and equal to
unity to reflect a critical balance in the flow and reaction times. The reaction constants are close to those
for extinction conditions given by Reference 8 and their β is normalized with a reported blowoff Da from
Reference 1 to obtain the unity Da. The fuel concentration is assumed to be unity at the fuel surface.
Equation (6.2) is solved for the temperature along the extinction boundary, Tcrit (not a constant) by using
the O2 and stretch dependence from Equation (6.1).
The resultant critical flame temperature along the flammability boundary is shown in Figure 6.17 as a
function of a. The critical temperature drops as a decreases. For quenching extinction (a < ~10 s-1), the
critical flame temperature drops more precipitously. This is due to the reduction in heat flux from the
flame relative to the intrinsic heat losses, as will be shown in Section 6.1.5.3. Critical flame temperature is
used in the next section to estimate heat flux from the flame to the fuel.


NASA/TM-20210011385 81




Figure 6.17.-Predicted temperature along extinction boundary Tcrit (Eq. (6.2)), Nusselt
number Nu (Eq. (6.3)), decay of heating rate  q′′ with stretch rate a (Eq. (6.4)), and


radiative heat qrad and total heat qtot from Equation (6.5). Solid temperature (Ts).
Convective heating rate  qconv .


### 6.1.5.2 Heat Transfer Estimates


To estimate the heat transfer rates to the stagnation region of the rod, the Nusselt number Nu
correlation developed by Sibulkin (Ref. 25) is used, which evaluates the convective heat transfer near the
forward stagnation point of a hemispherically tipped body of revolution as a function of Reynolds (Re)
and Prandtl (Pr) numbers.


Nu =1.32R e0.5 P r0.4 (6.3)


This correlation neglects dissociation (thermochemical heat release) for the low temperatures and high
nitrogen dilution levels along the flammability boundary (Ref. 26), and neglects gas radiation for the
nonluminous flames per Reference 27. The Re is based on the diameter. The convective heat flux  qconv to
the stagnation region is thus:


### (


crit s so, q = q ′′ A = h T
conv conv h crit
s


λ-


( TT)


### - )


Ts Ah


q ′′ = Nu
conv


(6.4)


Where λ is the thermal diffusivity at the mean gas temperature, Ts is the surface temperature, s is the
flame standoff distance, h is the convective heat transfer coefficient, and Ah is the hemispherical rod tip
surface area.


NASA/TM-20210011385 82




The Tcrit from Figure 6.17 are used with the measured s power law fit from Figure 6.12 to solve for
the  qconv to the stagnation region. The convective heating rate is linear with a, as shown in Figure 6.17.
This is an interesting combination of a terms in Equation (6.4): the square root Nu flow dependence
(Eq. (6.3)), the approximate minus cube root s dependence (0.334 power from Figure 6.12), and the
approximate seventh root temperature difference (Tcrit - Ts) dependence on a (0.16 power from
Figure 6.17). The sum of the powers is thus 0.5 + 0.33 + 0.16 = 0.99 ~ 1, which means that  qconv depends
linearly on a.


### 6.1.5.3 Surface Energy Balance


To examine the role of radiation- and solid-phase conductive losses on the flame, a surface energy
balance is developed. A two-zone surface energy balance schematic for the rod tip is formulated and
shown in Figure 6.18 to account for the three-dimensional (3D) nature of the flame over the nearly
spherical tip of the rod. Zone 1 is the area defined by the hemispherical tip of the rod. The entire zone is
assumed to be at the pyrolysis temperature Ts, consistent with the observed bubble layer length from
Figure 6.5, and consistent with the Biot number Bi << 1 from Equation (6.4) heat flux levels. Zone 2 is
the cylindrical rod, with an interface to Zone 1 at the base of the hemisphere. Only solid conduction loss
out of Zone 1 into Zone 2 is considered, using the rod cross-sectional area while the other terms use the
tip hemispherical surface area, which is twice as large.


Figure 6.18.-Two-zone surface energy balance.


NASA/TM-20210011385 83




A surface energy balance is defined as


4 ( 44 )
qtot =qconv′′ Ah +εg as σFTcrit Ah =m′′ Lvap Ah +εsσ Ts -T Ah +λs


- ∞

- Ar (6.5)


∂Tsolid
∂y


0


The total energy  qtot transferred from the flame to Ah includes convection  qconv′′ from Equation


(6.4) along with an estimate of the gas-phase radiative feedback to the surface. In the gas-phase radiation


term, εg is the gas-phase emissivity, αs is the surface absorptivity, σ is the Stefan-Boltzmann constant, and
F is the view factor. Gas-phase flame radiation is included in the surface energy balance because it
becomes an important source of energy in the quenching region, as will be shown. Kirchhoff's law is
applied to the surface where absorptivity equals emissivity (as = εs), and εg is estimated to be 0.02,
primarily from CO2 and H2O.
The energy from the flame to the surface goes into vaporizing the fuel, where  m′′ is the burning rate
and Lvap is the latent heat of vaporization, surface radiative loss is estimated using the surface and ambient
temperatures Ts and T∞, and conduction into the rod (Zone 2) for a solid-phase thermal diffusivity λs and
the solid-phase temperature gradient Tsolid at the surface through the cross-sectional area of the rod Ar. To
estimate surface radiative loss, we assume a constant surface pyrolysis temperature, but this assumption
may break down very near quenching.
To solve for the conductive loss to Zone 2, for long burn times with slow convective flow, the solid-
phase thermal profile is assumed to have reached an approximate steady state, and we can approximate a
one-dimensional (1D) temperature profile along the rod axis. It is assumed that no vaporization occurs in
this zone. We also assume for simplicity that the surface radiative loss is counteracted by a convective
heat flux from the hot gases flowing slowly past the rod.
There is a balance of heat transfer through the rod via conduction and convection. The convective
term is due to the steady surface regression of the rod (measured from the experiment), Vr. It is assumed
in this steady analysis that Vr is so small that the length of the sample does not change significantly over
the timeframe of interest ts, over which ΔL << L, where L is the characteristic length of the rod. For
example, using the regression rate measured in Figure 6.4 for the 0.476-cm radius rod, ts = 132 s and thus
∆L = Vrts = 0.5 cm << Lo = 5.9 cm. This means that changes in the temperature profiles are quasi-steady
for a slowly changing L. However, as the rod shortens significantly, this assumption breaks down.
The 1D steady conduction-convection energy balance in the solid can be nondimensionalized with
Y = y/L, θ = (T - T∞)/(Ts - T∞), and the solid-phase Peclet number Pe = LVr/αs.


∂θ ∂2θ
0 = Pe s + s
YY2 ∂∂


(6.6)


Boundary conditions for the solid model include the surface temperature T = Ts at y = 0 (circular
interface between Zone 1 and Zone 2) and T = T∞ at y = L. Boundary conditions become θ(0) = 1 and
θ(1) = 0. This equation is a linear, homogeneous, second-order ordinary differential equation with
constant coefficients, with roots 0 and -Pe for the general solution. Using the boundary conditions to
evaluate the constants of integration, the solution is


( ) ex p( -Pe Y) --ex p( Pe)


Y θ= (6.7)
1 --ex p( Pe)


NASA/TM-20210011385 84




Differentiating this solution, one can evaluate the steady-state temperature gradient at the regressing
surface (Y = 0) with decreasing Pe. The temperature gradient at the surface as a function of Pe is obtained
in dimensional terms:


- = ∞ (6.8)

- ( TTs- 1 L o


Pe
ex p( --Pe)


d Ts
dy


### )


y =0


We can use this to evaluate the conductive loss down the rod in Equation (6.5).
For large Peclet numbers (Pe >> 1), the temperature gradient at the pyrolysis interface is steep since
heat conducted along the rod is quickly convected back toward the burning tip via rod regression so that
heat cannot penetrate too deeply along the rod. For small Peclet numbers (Pe ≤ 1), conduction dominates,
and the temperature profiles are nearly linear. It is counterintuitive that the slowest burning samples will,
in this steady-state, have the least heat loss into the solid.
Using Equations (6.4) and (6.8), we can solve Equation (6.5) for the mass burning rate  m′′ as a
function of a. The mass flux from the burning tip of the rod is the only unknown in Equation (6.5). It
should be noted that as expressed in Equation (6.5), the fuel vaporization rate is from the hemispherical
surface, whereas the experiments measure the average rod regression rate. The difference is a factor of 2
due to the different areas.


### 6.1.5.4 Rod Regression Rates


The predicted 3D average rod regression rates using the two-zone model are compared with the
measured average regression rates, as shown in Figure 6.19. There is significant scatter in the measured
average regression rates since the flow and O2 varied during each test, but the values are of the correct
magnitude compared to the predicted 3D rod regression rates.
It is also possible to compare the 1D solution to Equation (6.5) with prior pseudo-1D flat flame
experiments (Refs. 28 to 30) by assuming all areas for heat transfer are the same and then solving the
equation for the regression rate Vr, also shown in Figure 6.19. Stretch rates are also defined as flow
velocity U/D for the 1D geometry, using the base rod size. The 1D predicted regression rates agree quite
well with existing data (Refs. 28 to 30) where the scale of the flames is much wider than the flame
standoff distance, resulting in pseudo-1D flames. The burning rates for the two-zone model are
significantly higher than the 1D solution for a given a due to the increased surface area for heat flux and
fuel vaporization in the 3D cylindrical geometry.


NASA/TM-20210011385 85




Figure 6.19.-Predicted regression rates from two-zone and one-
dimensional (1D) models as function of stretch rate a compared with
measured rod regression rates and published pseudo-1D experimental
data.


### 6.1.5.5 Estimate of Heat Loss Along Flammability Boundary


The terms of Equation (6.5) are plotted in Figure 6.20 as a function of a. The graph is plotted with
logarithmic axes to expand the quenching region (a < 10 s-1) where the heat losses become important. The
total flame heating rate to the surface drops linearly with decreasing a as was shown in Figure 6.17. The
minimum heat flux at unity a is 1 W/Ah = 1.57 W/cm2, which is in the range of literature values for the
critical heat flux for ignition of PMMA (Ref. 31). Along the blowoff branch (a > 10 s-1), fuel vaporization
parallels the total flame to surface heat flux. Heat loss is relatively small, with the solid conduction from
the surface in depth being most significant, but it decreases with decreasing a, mirroring the Peclet
number. Flame radiative feedback to the surface is comparable to surface radiative loss at high a but
decreases with decreasing a as the flame temperature decreases. Along the quenching branch, fuel
vaporization drops precipitously as the total heat flux to the surface drops and the losses become a
significant fraction of the total heat flux to the surface.


NASA/TM-20210011385 86




Figure 6.20.-Surface energy balance terms as function of stretch rate a along flammability
boundary from Equation (6.5) using the convective heating rate (Eq. (6.4)) and solid
conduction (Eq. (6.8)) as input.


Figure 6.21.-Ratio of energy balance terms to total heat flux from flame to
surface, to show relative importance of each term along flammability boundary.
Stretch rate (a).


NASA/TM-20210011385 87




This is shown more clearly in Figure 6.21, which plots the ratio of each term divided by the total
energy to the surface (convective plus gas radiative feedback). It is interesting that across the entire
blowoff branch, the vaporization ratio is ~70 percent, whereas it drops precipitously to 20 percent at low
a along the quenching branch. As a is reduced, the solid-phase conductive loss ratio surprisingly
decreases for this geometry, which is consistent with the observation that the slowest burning rods have
the least conductive loss. The surface radiative loss ratio becomes increasingly significant as a decreases,
not due to an increase in surface loss, but due to the decrease in total energy from the flame to the surface,
consistent with Reference 6.
Above a ~ 10 s-1, corresponding to the blowoff side of the flammability map (Figure 6.9 and
Figure 6.10), the surface radiative loss is comparable to the flame radiative feedback, and so radiative
exchange in general can be neglected. Interestingly, the flame radiative feedback increases from an
insignificant 1 percent (in agreement with Ref. 26) to over 13 percent of the total flame to surface
feedback, and thus becomes a significant fraction of the total flame to surface feedback at low a, in
general agreement with the more rigorous radiation analysis of Rhatigan et al. (Ref. 20). This additional
source of energy extends the flammability to lower a. It is only in the quenching region where surface
radiative loss becomes a significant fraction of the total heat release from the flame to the surface. At the
lowest a, the total heat loss fraction exceeds 60 percent of the total flame to surface feedback.
It is interesting to note that at the bottom of the flammability map (a ~ 10 s-1), the losses account for
only ~30 percent of the total flame to surface feedback, and yet the transition from blowoff to quenching
extinction begins in this region. What causes this transition? As shown in Figure 6.22, the experimental
flammability boundary is replotted with the x-axis as forced-flow velocity U divided by a diffusive
velocity UD = 2 cm/s. The transition from blowoff to quenching occurs when the forced-flow velocity
becomes the same order as the diffusive velocity (U/UD = 1) for this geometry.


Figure 6.22.-Flammability boundary (Eq. (6.1)) using forced-flow velocity U divided
by diffusive velocity UD in lieu of stretch rate a. XO2 is O2 concentration in vol%.
Normal-gravity flammability limit (Ref. 23) is graphed for comparison.


NASA/TM-20210011385 88




The normal-gravity upward limiting O2 concentration of 15.4 percent O2 (Ref. 23) is plotted for
comparison, assuming linear superposition of the buoyant flow velocity at the base of the flame (20 cm/s
(Ref. 32)) and the 4-cm/s forced-flow velocity. The normal-gravity upward flammability limit falls within
the stochastic boundary. If multiple limits at different forced plus buoyant flows were obtained along the
blowoff boundary, one could linearly extrapolate to zero flow velocity and get a reasonable yet
conservative estimate of the minimum flammability.
On the quenching branch of Figure 6.22, as the U is reduced, the ambient O2 concentration at the limit
has to increase to create an adequate O2 gradient for diffusion of O2 to the flame. The 3D diffusive
transport becomes significant. The flow time shifts from the residence time limitations to diffusive time
limitations. The flames near quenching are starved for O2, which is the limiting reactant. Fuel is leaking
out of the open tail of the flame. Oscillations begin and mixing layers form and the flame flashes through
them, locally depleting the already low ambient O2 as discussed previously. Ultimately, the flame
extinguishes due to the resulting reduced reaction rate that lowers the flame temperature to quenching.


### 6.1.6 Conclusions


For the first time, a series of concurrent rod flammability tests were conducted in microgravity aboard
the International Space Station (ISS). A small flow duct was used to create 0- to 55-cm/s flows past the
three sizes of clear and black PMMA rods.
Ignition delay time increased significantly as the minimum limiting O2 concentration is approached.
Ignition limits are found to be at higher O2 concentrations than the flammability limits due to the added
heat loss to the initially cold fuel rod present at ignition. The ignition delay time can be up to almost 10
times longer than the NASA STD-6001 standard igniter on time.
Detailed observations of near-quenching flames are described, including flame standoff distance trend
with O2 and stretch rate a. The flame shrinks to a hemispherical blue shape just before quenching.
Prequenching extinction oscillations at 1.1 Hz are observed with a radiometer and are similar to
previously reported quiescent candle flame oscillations in microgravity.
As flow speed is increased, blowoff extinction is initiated by the formation of a hole in the flame
sheet in the stagnation region of the flame. Once the stagnation region is blown far enough downstream of
the stagnation region (greater than one gas-phase thermal length ℓ), the flame is unable to propagate back
upstream even when the flow is reduced. This is consistent with observations that at the low O2
concentrations of interest, an opposed-flow flame cannot be established. Blowoff extinction limits from
the ISS experiments agree well with Zero Gravity Research Facility 5.18-s drop test limits.
The lower portion of the flammability boundary, with O2 concentration and a as coordinates, was
outlined as stochastic region between stable flames and extinguished flames. A curve fit including an
exponential and linear term was used to empirically define the boundary. The minimum in the
flammability boundary is at a of 8 to 12 s-1, where the a is modified to account for the various rod sizes
tested through the gas-phase ℓ scale. The linear blowoff branch may lend itself to extrapolation of
normal-gravity flammability testing to zero stretch to estimate the lower microgravity flammability limit.
Gas sensor data and rod mass loss estimates indicate that the flames are globally stoichiometric at
higher O2 concentrations but become more globally fuel rich as the minimum O2 concentration is
approached. This is due to excess pyrolyzate leakage out of the open tail of the hemispherical flames. CO
production also increases significantly at low O2 levels. The CO to CO2 ratio increases as well at low O2
concentrations. This data suggests that the limiting reactant at the lowest O2 concentrations is the O2
rather than the fuel.
A critical Damköhler number formulation is applied across the flammability boundary, and the
critical flame temperature is derived. This critical flame temperature is used in a Nusselt number


NASA/TM-20210011385 89




correlation to estimate the convective heat flux to the stagnation region of the rod. A surface energy
balance is formulated that uses the critical flame temperature and convective heat flux to derive the mass
burning rate along the boundary. The rod regression rates calculated from this model compare favorably
with the experimental measurements.
The terms of the surface energy balance are compared and reveal that in the blowoff branch, heat
losses are negligible. In the quenching region, surface radiative loss dominates. Solid conductive loss
down the rod is lower and decreases with decreasing stretch due to the low Peclet number. Gas-phase
radiative feedback becomes an important heat transfer process that extends the flammability limit to lower


a. At the bottom of the flammability map, heat losses are only 30 percent of the total heating rate to the


surface, so the transition from blowoff to quenching occurs when the convective flows become the same
order of magnitude as diffusive flows, shifting the critical Damköhler number residence time limitations
to diffusive time limitations. The transport of the limiting reactant O2 is limited by concentration
gradients, causing the needed ambient O2 to increase as the a is reduced.


### 6.1.7 Acknowledgments


This work was funded by the International Space Station (ISS) Research Project Office. We want to
acknowledge astronauts Reid Wiseman and Alex Gerst, who ran these Burning and Suppression of
Solids-II (BASS-II) experiments; the BASS operations team (Jay Owens, Chuck Bunnell, Tibor Lorik,
Carol Reynolds and the ground support teams at Glenn Research Center, Johnson Space Center, and
Marshall Space Flight Center); and the NASA Glenn Zero Gravity Research Facility personnel, led by
Eric Neumann.


### 6.1.8 References


1. Alkidas, A.; and Durbetaki, P.: Stagnation-Point Heat Transfer: The Effect of the First Damkohler Similarity Parameter. J. Heat Transfer, vol. 94, no. 4, 1972, pp. 410-414. 2. Simmons, R.F.; and Wolfhard, H.G.: Some Limiting Oxygen Concentrations for Diffusion Flames in Air Diluted With Nitrogen. Combust. Flame, vol. 1, no. 2, 1957, pp. 155-161. 3. Linan, Amable: The Asymptotic Structure of Counterflow Diffusion Flames for Large Activation Energies. Acta Astronaut., vol. 1, nos.7-8, 1974, pp. 1007-1039.


4. Sohrab, S.H.; Linan, A.; and Williams, F.A.: Asymptotic Theory of Diffusion-Flame Extinction With
Radiant Loss From the Flame Zone. Combust. Sci. Technol., vol. 27, nos. 3-4, 1982, pp. 143-154.
5. T'ien, James S.; and Bedir, Hasan: Radiative Extinction of Diffusion Flames-A Review.
Proceedings of the First Asia-Pacific Conference on Combustion, Osaka, Japan, 1997.
6. T'ien, James S.: Diffusion Flame Extinction at Small Stretch Rates: The Mechanism of Radiative
Loss. Combust. Flame, vol. 65, no. 1, 1986, pp. 31-34.
7. T'ien, James S.: Some Partial Scaling Considerations in Microgravity Combustion Problems.
Progress in Scale Modeling, Springer, Dordrecht, 2008, pp. 281-292.
8. Sohrab, S.H.; and Williams, F.A.: Extinction of Diffusion Flames Adjacent to Flat Surfaces of
Burning Polymers. J. Polym. Sci., Polym. Chem. Ed., vol. 19, no. 11, 1981, pp. 2955-2976.
9. Krishnamurthy, L.: Diffusion-Flame Extinction in the Stagnation-Point Boundary Layer of PMMA in
O2/N2 Mixtures. Combust. Sci. Technol., vol. 10, nos. 1-2, 1975, pp. 21-25.


1. Tsuji, Hiroshi: Counterflow Diffusion Flames. Prog. Energy Combust. Sci., vol. 8, no. 2, 1982, pp. 93-119.

2. Halli, Y.; and T'ien, J.S.: Effect of Convective Velocity on Upward and Downward Burning Limits of PMMA Rods. NBS-GCR-86-507, 1986. Available from National Technical Information Services.


NASA/TM-20210011385 90




1. Olson, Sandra L.; Ferkul, Paul V.; and T'ien, James S.: Near-Limit Flame Spread Over a Thin Solid Fuel in Microgravity. Proc. Combust. Inst., vol. 22, no. 1, 1989, pp. 1213-1222.

2. Ivanov, A.V., et al.: Experimental Verification of Material Flammability in Space. NASA/CR-1999- 209405, 1999. https://ntrs.nasa.gov

3. Olson, Sandra L., et al.: Results From On-Board CSA-CP and CDM Sensor Readings During the Burning and Suppression of Solids-II (BASS-II) Experiment in the Microgravity Science Glovebox (MSG). ICES-2015-196, 2015. 15. Olson, S.L.; and Miller, F.J.: Experimental Comparison of Opposed and Concurrent Flame Spread in a Forced Convective Microgravity Environment. Proc. Combust. Inst., vol. 32, no. 2, 2009, pp. 2445- 2452. 16. National Aeronautics and Space Administration: Flammability, Offgassing, and Compatibility Requirements and Test Procedures. NASA-STD-6001B, 2011.


17. Dietrich, D.L., et al.: Candle Flames in Non-Buoyant Atmospheres. Combust. Sci. Technol., vol. 156,
no. 1, 2000, pp. 1-24.


1. Wang, H.Y.; and Law, C.K.: On Intrinsic Oscillation in Radiation-Affected Diffusion Flames. Proc. Comb. Inst., vol. 31, no. 1, 2007, pp. 979-987. 19. Nayagam, Vedha; Balasubramaniam, R.; and Ronney, Paul D.: Diffusion Flame-Holes. Combust. Theory Model., vol. 3, no. 4, 1999, pp. 727-742. 20. Rhatigan, Jennifer L.; Bedir, Hasan; and T'ien, James S.: Gas-Phase Radiative Effects on the Burning and Extinction of a Solid Fuel. Combust. Flame, vol. 112, nos. 1-2, 1998, pp. 231-241.


21. Rhatigan, J.L.; Sung, C.J.; and T'ien, J.S.: On Solid Trioxane Combustion in Stagnation Point Flows.
Proc. Comb. Inst., vol. 29, no. 2, 2002, pp. 1645-1652.


22. T'ien, James S.: The Effects of Perturbations on the Flammability Limits. Combust. Sci. Technol.,
vol. 7, no. 4, 1973, pp. 185-188.
23. Hirsch, D., et al.: Issues Related to the Flammability Assessment of Polymers for Hazard Analyses of
Oxygen Systems. Flammability and Sensitivity of Materials in Oxygen-Enriched Atmospheres: 10th
Volume, ASTM STP1454, T. Steinberg, B. Newton, and H. Beeson, eds., American Society for
Testing and Materials, West Conshohocken, PA, 2003, pp. 21-26.
24. Mulholland, G.W.: The Effect of Oxygen Concentration on CO and Smoke Produced by Flames. Fire
Saf. Sci., vol. 3, 1991, pp. 585-594.
25. Sibulkin, M.: Heat Transfer Near the Forward Stagnation Point of a Body of Revolution. J. Aeronaut.
Sci., vol. 19, no. 8, 1952, pp. 570-571.
26. Baukal, C.E.; and Gebhart, B.: Surface Condition Effects on Flame Impingement Heat Transfer. Exp.
Therm. Fluid Sci., vol. 15, no. 4, 1997, pp. 323-335.
27. Chander, Subhash; and Ray, Anjan: Flame Impingement Heat Transfer: A Review. Energy Convers.
Manag., vol. 46, nos. 18-19, 2005, pp. 2803-2837.
28. Olson, Sandra L.; and T'ien, James S.: Buoyant Low-Stretch Diffusion Flames Beneath Cylindrical
PMMA Samples. Combust. Flame, vol. 121, no. 3, 2000, pp. 439-452.
29. Ohtani, Hideo; Akita, Kazuo; and Hirano, Toshisuke: An Analysis of Bottom Stagnation Region
Combustion of Polymeric Material Pieces Under Natural Convection. Combust. Flame, vol. 53, 1983,
pp. 33-40.
30. T'ien, J.S., et al.: Combustion and Extinction in the Stagnation-Point Boundary Layer of a Condensed
Fuel. Combust. Flame, vol. 33, 1978, pp. 55-68.
31. Lyon, Richard E.; and Quintiere, James G.: Criteria for Piloted Ignition of Combustible Solids.
Combust. Flame, vol. 151, no. 4, 2007, pp. 551-559.


NASA/TM-20210011385 91




1. Hirano, Toshisuke; Noreikis, Stanley E.; and Waterman, Thomas E.: Measured Velocity and Temperature Profiles Near Flames Spreading Over a Thin Combustible Solid. Combust. Flame, vol. 23, no. 1, 1974, pp. 83-96.


6.1.9 Primary Microgravity and Normal-Gravity Research Citations for This Project


• Olson, Sandra; and Ferkul, Paul V.: Microgravity Flammability Boundary for PMMA Rods in
Axial Stagnation Flow: Experimental Results and Energy Balance Analyses. Combust. Flame,
vol. 180, 2017, pp. 217-229.
• Marcum, Jeremy W.; Ferkul, Paul V.; and Olson, Sandra L.: PMMA Rod Stagnation Region
Flame Blowoff Limits at Various Radii, Oxygen Concentrations, and Mixed Convection Stretch
Rates. Proc. Comb. Inst., vol. 37, no. 3, 2019, pp. 4001-4008.
• Olson, Sandra L.; Ferkul, Paul V.; and Marcum, Jeremy W.: High-Speed Video Analysis of
Flame Oscillations Along a PMMA Rod After Stagnation Region Blowoff. Proc. Comb. Inst.,
vol. 37, no. 2, 2019, pp. 1555-1562
• Marcum, J.W., et al.: Low Pressure Flame Blowoff of the Stagnation Region of Cast PMMA
Cylinder in Axial Mixed Convective Flow. Combust. Flame, vol. 216, 2020, pp. 385-397.


NASA/TM-20210011385 92




1. Individual Principal Investigator Report: T'ien


7.1 Concurrent Flame Growth, Spread, and Extinction Over Composite Fabric Samples
in Low-Speed Purely Forced Flow in Microgravity3


### 7.1.1 Abstract


As a part of the NASA Burning and Suppression of Solids (BASS) and BASS-II experimental
projects aboard the International Space Station, flame growth, spread, and extinction over a composite
cotton-fiberglass fabric blend (referred to as the SIBAL (Solid Inflammability Boundary at Low Speed)
fabric) were studied in low-speed concurrent forced flows. The tests were conducted in a small flow duct
within the Microgravity Science Glovebox. The fuel samples measured 1.2 and 2.2 cm wide and 10 cm
long. Ambient O2 was varied from 21 percent down to 16 percent and flow speed from 40 cm/s down to
1 cm/s. A small flame resulted at low flow, enabling us to observe the entire history of flame development
including ignition, flame growth, steady spread (in some cases), and decay at the end of the sample. In
addition, by decreasing flow velocity during some of the tests, low-speed flame quenching extinction
limits were found as a function of O2 percentage. The quenching speeds were found to be between 1 and
5 cm/s with higher speed in lower O2 atmosphere. The shape of the quenching boundary supports the
prediction by earlier theoretical models. These long-duration microgravity experiments provide a rare
opportunity for solid fuel combustion since microgravity time in ground-based facilities is generally not
sufficient. This is the first time that a low-speed quenching boundary in concurrent spread is determined
in a clean and unambiguous manner.


### 7.1.2 Introduction


Flame spread and extinction over condensed fuels in a microgravity environment has been the subject
of extensive theoretical and experimental studies due to the importance of fire safety in human space
missions (Refs. 1 to 4). Compared with burning in normal gravity, diffusion flames in microgravity are
not affected by buoyancy-induced flow, thus providing a chance to study the fundamental mechanism(s)
of low-speed flame quenching (Ref. 5). Transition from solid diffusion flame spreading to quenching
extinction is a slow heat loss process characterized by a relative increase in the rates of radiative and
conductive heat losses compared to the rate of heat generation (Ref. 3). Long-duration microgravity time
is desired for such studies, which in general cannot be achieved by ground-based facilities.
Recently, NASA's Burning and Suppression of Solids (BASS and BASS-II) project examined the
burning and extinction characteristics of a variety of solid fuel samples aboard the International Space
Station (ISS). Different thermally thin and thermally thick solid fuels were burned in concurrent, opposed,
or stagnation flow configurations in a small flow duct. Each experimental run took tens of seconds to
minutes, depending on the sample type and flow conditions. The challenge with thin solid samples in
concurrent flow, compared with other configurations, is that flame spreads much faster, and flames can
become quite long. Because of size limitations, the fuel sample is relatively short and so a concurrent
spreading flame may not reach fully steady spread within the sample length. The transient ignition and
flame growth process, however, provides a flame spread history that can be useful for the development of
transient flame models (Ref. 6). In BASS-II, a N2 dilution scheme is used whereby the O2 percentage in
the Microgravity Science Glovebox (MSG) can be decreased to a preset value so that flame spread can be


3Previously published by: Zhao, Xiaoyang; and T'ien, James S.: A Three-Dimensional Transient Model for Flame
Growth and Extinction in Concurrent Flows. Combust. Flame, vol. 162, no. 5, 2015, pp. 1829-1839.
http://dx.doi.org/10.1016/j.combustflame.2014.12.003


NASA/TM-20210011385 93




studied with O2 percentage as an additional variable parameter (Ref. 7). This facilitates the determination
of the O2-flow-velocity flammability boundary of materials.
In this report, BASS and BASS-II results will be discussed in detail. Flame growth, spread, and
quenching extinction will be presented for a thin composite cotton-fiberglass fabric burning in various O2
concentrations and concurrent flow speeds.


### 7.1.3 Experimental


All tests were conducted in a small flow duct (shown in Figure 7.1) within the MSG aboard the ISS.
The sample used is a composite cotton-fiberglass fabric blend (75 percent cotton and 25 percent
fiberglass). The thickness of the sample is about 0.32 mm with an area density of 18.2 mg/cm2. The fabric
is custom made for a previous project Solid Inflammability Boundary at Low Speeds (SIBAL) (Ref. 8),
hence it is referred to here as the SIBAL fabric. One major advantage of this fuel sample is the retention
of sample structure integrity after the combustible (i.e., cotton cellulose) is consumed because of the
fiberglass mesh. It does not crack or produce curly ash typically seen in pure cellulose samples such as
paper or cloth. In addition to Reference 8, experimental studies using SIBAL fabric can be found in
References 9 and 10.
In the experiment, SIBAL fuel samples of two different widths, 1.2 and 2.2 cm, were used. Both have
an exposed length of 10 cm. The samples were mounted in stainless steel sample holders. The fuel sample
mounted to the holder was placed in the small flow duct of cross-sectional size 7.6 by 7.6 cm. The flow
speed could be varied from 1 to 55 cm/s. The tests were conducted in ambient O2 molar fraction of 16 to
21 percent. Ambient pressure was 1 atm. It should be noted that for a given test the O2 concentration was
fixed while the flow speed could be varied.
A Kanthal® hot wire was used to ignite the fuel sample leading edge so that the flame can spread in a
concurrent configuration. The flame growth process was recorded by two cameras. The side-view video
camera provided edge-on images of the flat samples at standard video framing rates (29.97 frames per
second). The top-view digital camera looked down on the top fuel surface and provided high-resolution
still images of the flame at a rate of about one image every 1.2 s. When flow speed and O2 concentration
were low, the flame became very dim blue and was difficult to see in the side video camera. The top-view


Figure 7.1.-Experimental setup. (a) Small flow duct. (b) Fuel sample, sample holder, and igniter.


NASA/TM-20210011385 94




camera exposure times were long enough (1/8 to 1/4 s) to easily capture high-quality flame images even
for dim flames right before quenching. These still images provide a time history of flame quenching that
can be used to compare with transient model results.


### 7.1.4 Results and Discussion


A total of 27 tests were carried out for the fabric samples in BASS-II, including six quenching tests,
three nonignited tests, and one blowoff test. These are listed in Table 7.1. In addition, four tests from the
BASS series were selected as listed at the bottom of Table 7.1. These four tests are all 21 percent O2 cases
at a fixed flow velocity during each test. For those cases with flow velocity variations, the starting and the
final velocities are indicated in the velocity column. The rate of velocity change varies from case to case
depending on the communication between the astronauts and the ground crews and the manual adjustment
time by the crew. Many of these tests were used to determine the low-speed quenching limits as a
function of O2 percentage. In some tests, the flame quenched quickly or was not ignited. These samples
were reused in additional tests as indicated in Table 7.1. These partially burned samples were ignited with
a retractable igniter on one side of the sample at the fuel burnout position. These reused samples in
general had a short unburned length and provided less quantitative data, thus will not be discussed in this
report.
Figure 7.2 shows flame development stages of a 2.2-cm sample in 10-cm/s flow and 21 percent O2.
Figure 7.2(a) shows side-view flame tracking of flame tip, flame base, and flame length. Figure 7.2(b)
shows flame edge-view video still images at different stages. Note in the figure, flow is from right to left.
After the igniter was turned on, a strong flame was initiated on both sides of the solid fuel. The flame was
stabilized and started to grow and move downstream. At about 19 s, the flame reached a limiting constant
length and a steady spread rate relative to the laboratory (Ref. 11). This steady spread state lasted for
around 9 s. The flame images look almost identical during this stage, as can be seen at 20.17 and 24.83 s
in Figure 7.2(b). Then the flame tip (or more precisely the flame preheating front) moved close to the end
of the fuel sample, and the flame decayed in size until complete burnout. The whole combustion process
took about 40 s.
Figure 7.3 shows flame development stages of a 2.2-cm sample in 5-cm/s flow and 21 percent O2.
Unlike the flame in 10-cm/s flow in Figure 7.2, the flame from the side-view video is very dim in this
case. Figure 7.3 thus shows the top-view images and tracking from those images. Because the flow
speed is lower, it took more than 60 s to burn the whole sample. Steady spread time lasts for about 21 s,
much longer than the 10-cm/s flow case. Virtually identical images at 35.59 and 45.59 s are shown in
Figure 7.3(b). In the top-view images, we can find bright spots behind the flame base when the flame
passes. The spots come from the smoldering of a small amount of fuel that is not completely consumed by
the flaming combustion. Compared with the 10-cm/s case, the 5-cm/s case has a shorter flame and spreads
more slowly.
Steady flame spread rates in different flow speeds and O2 percentages are plotted in Figure 7.4 for
both 2.2- and 1.2-cm samples. Note in some cases flow speed was varied during the test. Steady flame
spread here means the flame reached a constant spread rate for more than 20 s. Flames spread more
slowly across the narrower samples, at lower flow velocities and at lower O2 percentages. The trends are
consistent with our physical intuition.


NASA/TM-20210011385 95




TABLE 7.1.-TEST SUMMARY OF FLAT SIBALa FABRICS IN CONCURRENT FLOW IN
BURNING AND SUPPRSSION SOLIDS (BASS AND BASS-II)


<table>
 <tr>
  <th>Test<br/>number</th>
  <th>Sample width,<br/>cm</th>
  <th>Flow,<br/>cm/s</th>
  <th>O2,<br/>vol%</th>
  <th>Comments</th>
 </tr>
 <tr>
  <td>GMT45-T1</td>
  <td>2.2</td>
  <td>10</td>
  <td>18.5b</td>
  <td>-----------------------------</td>
 </tr>
 <tr>
  <td>GMT45-T2</td>
  <td>2.2</td>
  <td>10 to 5</td>
  <td>18.5b</td>
  <td>-----------------------------</td>
 </tr>
 <tr>
  <td>GMT45-T4</td>
  <td>2.2</td>
  <td>10 to 2.2</td>
  <td>18.7</td>
  <td>Quenched</td>
 </tr>
 <tr>
  <td>GMT45-T15</td>
  <td>2.2</td>
  <td>10 to 29</td>
  <td>18.7</td>
  <td>No blowoff</td>
 </tr>
 <tr>
  <td>GMT100-T5</td>
  <td>2.2</td>
  <td>10 to 2.4</td>
  <td>18.8</td>
  <td>-----------------------------</td>
 </tr>
 <tr>
  <td>GMT100-T6</td>
  <td>2.2</td>
  <td>4.5 to 2.6</td>
  <td>18.8</td>
  <td>-----------------------------</td>
 </tr>
 <tr>
  <td>GMT100-T13</td>
  <td>2.2</td>
  <td>4 to 2.2</td>
  <td>17.5</td>
  <td>Quenched</td>
 </tr>
 <tr>
  <td>GMT100-T16</td>
  <td>2.2</td>
  <td>4 to 3</td>
  <td>17.6</td>
  <td>-----------------------------</td>
 </tr>
 <tr>
  <td>GMT175-T9</td>
  <td>2.2</td>
  <td>10</td>
  <td>16.4</td>
  <td>No ignition</td>
 </tr>
 <tr>
  <td>GMT175-T10</td>
  <td>2.2</td>
  <td>5</td>
  <td>16.4</td>
  <td>No ignition</td>
 </tr>
 <tr>
  <td>GMT175-T18</td>
  <td>2.2</td>
  <td>5 to 2.6</td>
  <td>17.4</td>
  <td>Quenched</td>
 </tr>
 <tr>
  <td>GMT178-T11</td>
  <td>2.2</td>
  <td>4</td>
  <td>17.1</td>
  <td>-----------------------------</td>
 </tr>
 <tr>
  <td>GMT178-T12</td>
  <td>2.2</td>
  <td>5</td>
  <td>16.8</td>
  <td>No ignition</td>
 </tr>
 <tr>
  <td>GMT178-T14</td>
  <td>2.2</td>
  <td>4 to 2.8</td>
  <td>16.9</td>
  <td>Quenched</td>
 </tr>
 <tr>
  <td>GMT178-T17</td>
  <td>2.2</td>
  <td>6 to 53</td>
  <td>16.9</td>
  <td>No blowoff</td>
 </tr>
 <tr>
  <td>GMT190-T19</td>
  <td>1.2</td>
  <td>11</td>
  <td>17.2</td>
  <td>-----------------------------</td>
 </tr>
 <tr>
  <td>GMT190-T20</td>
  <td>1.2</td>
  <td>11 to 3</td>
  <td>17.2</td>
  <td>Quenched</td>
 </tr>
 <tr>
  <td>GMT190-T21</td>
  <td>1.2</td>
  <td>11 to 47</td>
  <td>17.2</td>
  <td>Blow-off</td>
 </tr>
 <tr>
  <td>GMT190-T22</td>
  <td>1.2</td>
  <td>10.5 to 5</td>
  <td>17.1</td>
  <td>Quenched</td>
 </tr>
 <tr>
  <td>GMT190-T23</td>
  <td>2.2</td>
  <td>10</td>
  <td>17.2</td>
  <td>Reused, did not ignite</td>
 </tr>
 <tr>
  <td>GMT190-T24</td>
  <td>2.2</td>
  <td>10</td>
  <td>18.2</td>
  <td>Reused, one-sided flame</td>
 </tr>
 <tr>
  <td>GMT216-T25</td>
  <td>2.2</td>
  <td>5 to 2.5</td>
  <td>20.8</td>
  <td>Reused, ignited</td>
 </tr>
 <tr>
  <td>GMT216-T26</td>
  <td>2.2</td>
  <td>5 to 2.5</td>
  <td>20.8</td>
  <td>Reused, ignited</td>
 </tr>
 <tr>
  <td>GMT216-T27</td>
  <td>1.2</td>
  <td>5 to 2</td>
  <td>20.7</td>
  <td>Reused, ignited</td>
 </tr>
 <tr>
  <td>GMT216-T28a</td>
  <td>1.2</td>
  <td>5</td>
  <td>20.7</td>
  <td>Reused, did not ignite</td>
 </tr>
 <tr>
  <td>GMT216-T28b</td>
  <td>1.2</td>
  <td>5</td>
  <td>20.7</td>
  <td>Reused, did not ignite</td>
 </tr>
 <tr>
  <td>GMT216-T29</td>
  <td>1.2</td>
  <td>5 to 2</td>
  <td>20.7</td>
  <td>Reused, ignited</td>
 </tr>
 <tr>
  <td>GMT96-T8</td>
  <td>2.2</td>
  <td>5</td>
  <td>21</td>
  <td>BASS</td>
 </tr>
 <tr>
  <td>GMT96-T7</td>
  <td>2.2</td>
  <td>10</td>
  <td>21</td>
  <td>BASS</td>
 </tr>
 <tr>
  <td>GMT131-T10</td>
  <td>1.2</td>
  <td>11</td>
  <td>21</td>
  <td>BASS</td>
 </tr>
 <tr>
  <td>GMT222-T11</td>
  <td>1.2</td>
  <td>19</td>
  <td>21</td>
  <td>BASS</td>
 </tr>
</table>


aSolid Inflammability Boundary at Low Speeds.
bO2 reading in these two tests might be inaccurate.


NASA/TM-20210011385 96




Figure 7.2.-Flame development on 2.2-cm sample in 10-cm/s concurrent flow, 21 percent O2. (a) Side-view flame
tracking. (b) Side-view image sequence over time t. Flow is from right to left.


Figure 7.3.-Flame development on 2.2-cm sample in 5-cm/s flow, 21 percent O2. (a) Top-view flame tracking.


(b) Top-view image sequence over time t. Flow is from right to left.


NASA/TM-20210011385 97




Figure 7.4.-Steady flame spread rate for both 2.2- and 1.2-cm-wide samples.


Figure 7.5 shows a typical flame quenching sequence in the BASS-II experiment. A 2.2-cm-wide
sample in 18.7 percent O2 was first ignited at 10-cm/s flow. Flow speed was decreased to 2.2 cm/s
incrementally after ignition. Figure 7.6 shows flame tracking and flow speed versus time. After ignition,
the flame started to grow. As the flow speed was reduced, both flame length and flame width dropped
accordingly with flow. After 25 s, flow velocity was reduced to 2.2 cm/s and held there for the remainder
of the test. As shown in Figure 7.5, both the flame length and flame width continued to decrease
approaching a circular-shaped blue flame seen from the top. The size of the flame continues to shrink
until extinction is reached. This is typical in a quenching extinction sequence. As the quenching limit is
approached (in this case by turning down the flow velocity), the fuel pyrolysis rate and combustion heat
release rate (HRR) are reduced, and radiation loss becomes a significant fraction of the HRR from the
shrinking flame. When the flame becomes small enough, conduction becomes the additional heat loss.
The postburn photo of the sample in Figure 7.5 shows the narrowing of the burnt region as the flame
shrinks toward extinction with a substantial part of the fuel left unburnt along the two sides of the sample
holder. Although this is a concurrently spreading flame, the quenching sequence shows similar
characteristics in opposed flow (Ref. 2); the flame becomes circular, indicating the importance of three-
dimensional (3D) heat and mass transfer near the limit.


NASA/TM-20210011385 98




Figure 7.5.-Top view of flame quenching sequence. 2.2-cm-wide sample in 18.7 percent O2. Ignited at 10-cm/s
flow, reduced to 2.2 cm/s. Flow is from right to left. (a) Time t is 6.7 s, velocity V is 8 cm/s. (b) t = 32.6 s.
V = 2.2 cm/s. (c) t = 15.7 s. V = 4 cm/s. (d) t = 45.0 s. V = 2.2 cm/s. (e) t = 25.8 s. V = 2.2 cm/s. (f) t = 54.0 s.
V = 2.2 cm/s. (g) t = 29.2 s. V = 2.2 cm/s. (h) Postburn.


Figure 7.6.-Flame tracking and flow speed U0 versus time for


2.2-cm-wide sample in 18.7 percent O2, ignited at 10-cm/s flow,


then reduced to 2.2 cm/s.


NASA/TM-20210011385 99




For this thin fabric fuel in concurrent flow, flame spread rate is relatively large and the sample is not
long enough to fine tune the flow speed during the 1 to 2 min of experimental run time. It is difficult to
get to the desired near-quenching-limit state every time. Six quenching cases were achieved during
BASS-II for the SIBAL sample, four of them were for the 2.2-cm-width samples. Along with the near-
limit stable flame data, we were able to draw part of the quenching branch of the flammability boundary
as shown in Figure 7.7 for 2.2-cm-wide SIBAL fabric. Quenching flow velocities were found to be
between 1 and 5 cm/s with higher velocity at lower O2 percentage. This trend of the quenching boundary
supports the prediction by earlier theoretical models (Refs. 1 and 8). Recently, a 3D transient numerical
model has been published (Ref. 6) that is suitable to simulate the present experiment. The model contains
many material properties including kinetic rate constants. The bottom part of the flammability boundary
that supports combustion in the lowest O2 environment is expected to be flat in this figure and cannot be
determined accurately by this velocity-varying procedure. Very near the boundary, ignition of the sample
is sporadic. A procedure with gradually decreasing O2 is needed. In addition, because of the limited
number of tests, the quenching limit for the 1.2-cm-wide sample was not resolved. But it can be seen that
the narrow sample has a smaller flammable domain, as expected.


Figure 7.7.-Flammability map for Solid Inflammability Boundary at Low Speeds (SIBAL)
fabric in concurrent flow in microgravity. Dotted line marks experimental quenching
boundary for 2.2-cm-wide sample. Flow speed (U0).


NASA/TM-20210011385 100




#### 7.1.5 Conclusions


Concurrent flame growth and extinction over a thin flat cotton-fiberglass composite fabric sample
was studied as part of the Burning and Suppression of Solids (BASS) and BASS-II space experiments
aboard the International Space Station. These long-duration microgravity experiments provided rare
opportunities for solid fuel combustion studies. By reducing the flow velocity during the tests, quenching
extinction limits were obtained accurately. The quenching velocities are small (between 1 and 5 cm/s),
and an accurate determination is necessary to resolve the slope of the quenching boundary. The
experimental data obtained supports earlier theoretical predictions (at least qualitatively) of solid
flammability limits at low flow velocities due to radiative and conductive losses. The flame image
sequence at quenching shows the flame shrinks both in length and width and the flame goes out in a
three-dimensional manner.
In addition to obtaining quenching limits, the sequence of sample ignition, flame growth, and steady
spread to final decay across the entire sample in low-speed purely forced flows were experimentally
recorded. These are precious data to help us to understand the entire process of flame development in
microgravity. They also provide the basis to check the theoretical model development. Currently, we are
measuring and deducing the pyrolysis rate constants for Solid Inflammability Boundary at Low Speeds
(SIBAL) fabric in order to perform quantitative comparisons between the model and experiment.


### 7.1.6 References


1. Ferkul, P.V.; and T'ien, J.S.: A Model of Low-Speed Concurrent Flow Flame Spread Over a Thin Fuel. Combust. Sci. Technol., vol. 99, nos. 4-6, 1994, pp. 345-370.

2. Olson, Sandra L.; Ferkul, Paul V.; and T'ien, James S.: Near-Limit Flame Spread Over a Thin Solid Fuel in Microgravity. Proc. Comb. Inst., vol. 22, no. 1, 1989, pp. 1213-1222.

3. T'ien, J.S., et al.: Mechanisms of Flame Spread and Smolder Wave Propagation. Microgravity Combustion-Fire in Free Fall. H.D. Ross, ed., Academic Press, San Diego, CA, 2001, pp. 299-345.

4. Ferkul, P.V., et al.: Aspects of Fabric in Opposed and Concurrent Air Flow in Microgravity. Presented at the 8th U.S. National Combustion Meeting, Park City, UT, 2013. 5. T'ien, James S.: Diffusion Flame Extinction at Small Stretch Rates: The Mechanism of Radiative Loss. Combust. Flame, vol. 65, no. 1, 1986, pp. 31-34. 6. Zhao, Xiaoyang; and T'ien, James S.: A Three-Dimensional Transient Model for Flame Growth and Extinction in Concurrent Flows. Combust. Flame, vol. 162, no. 5, 2015, pp. 1829-1839. http://dx.doi.org/10.1016/j.combustflame.2014.12.003 Accessed June 23, 2021.


7. Olson, Sandra L., et al.: Results From On-Board CSA-CP and CDM Sensor Readings During the
Burning and Suppression of Solids-II (BASS-II) Experiment in the Microgravity Science Glovebox
(MSG). ICES-2015-196, 2015.
8. Ferkul, Paul V., et al.: Solid Fuel Combustion Experiments in Microgravity Using a Continuous Fuel
Dispenser and Related Numerical Simulations. Microgravity Sci. Tec., vol. 15, no. 2, 2004, pp. 3-12.
9. Kleinhenz, Julie, et al.: One-Sided Flame Spread Phenomena of a Thermally Thin Composite
Cotton/Fiberglass Fabric. Fire Mater., vol. 29, no. 1, 2005, pp. 27-37.


10. Johnston, Michael C., et al.: Self Induced Buoyant Blow Off in Upward Flame Spread on Thin Solid
Fuels. Fire Saf. J., vol. 71, 2015, pp. 279-286.
11. Tseng, Ya-Ting; and T'ien, James S.: Limiting Length, Steady Spread, and Nongrowing Flames in
Concurrent Flow Over Solids. J. Heat Trans., vol. 132, no. 9, 2010, p. 091201


NASA/TM-20210011385 101






#### Appendix A.-Test Matrices for Burning and Suppression Solids-II (BASS-II)


These summary test matrices are grouped by principal investigator with Bhattacharjee in Table A.1, Ferkul in Table A.2, Fernandez-Pello in Table A.3, Miller in Table A.4, Olson in Table A.5, and T'ien in Table A.6.


### A.1 Bhattacharjee Test Matrix


### Details are available at http://flame.sdsu.edu/.


### TABLE A.1.-BHATTACHARJEE TEST MATRIX


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)c</th>
 </tr>
 <tr>
  <td>2/19/2014<br/>GMT 2014<br/>050</td>
  <td>10:09:50 to<br/>10:10:16</td>
  <td>7</td>
  <td>B1</td>
  <td>147</td>
  <td>100-µm<br/>PMMA film,<br/>2 cm wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>62</td>
  <td>5</td>
  <td>50</td>
  <td>---</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>off</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>57</td>
  <td>22.2</td>
  <td>22.2</td>
  <td>20.6</td>
  <td>20.6</td>
  <td>0.44</td>
  <td>0.44</td>
  <td>0</td>
  <td>6</td>
  <td>Ignited very quickly, turned flow off after spread halfway;<br/>flame extinguished very quickly; and sooty with blue leading<br/>edge</td>
 </tr>
 <tr>
  <td>7/7/2014<br/>GMT 188</td>
  <td>---------</td>
  <td>62</td>
  <td>B10</td>
  <td>173m</td>
  <td>1-cm, 0.2-<br/>mm PMMA<br/>film</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>1.7 (52), 1.25,<br/>0.9, 0.6, 0.4, 0.35</td>
  <td>5, 4, 3, 2, 1</td>
  <td>10</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>16</td>
  <td>123</td>
  <td>21.0</td>
  <td>20.8</td>
  <td>20.1</td>
  <td>19.9</td>
  <td>0.33</td>
  <td>0.44</td>
  <td>0</td>
  <td>23</td>
  <td>Multiple velocities for steady spread, extinguished at pot 0.35</td>
 </tr>
 <tr>
  <td>7/7/2014<br/>GMT 188</td>
  <td>---------</td>
  <td>61</td>
  <td>B11</td>
  <td>158m</td>
  <td>2-cm, 0.2-<br/>mm PMMA<br/>film</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>2.5 (59), 1.3, 0.7,<br/>0.5, 0.35</td>
  <td>5, 3, 1, &lt;1</td>
  <td>10</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>131</td>
  <td>21.0</td>
  <td>20.7</td>
  <td>20.1</td>
  <td>19.8</td>
  <td>0.33</td>
  <td>0.47</td>
  <td>0</td>
  <td>46</td>
  <td>Multiple velocities for steady spread, extinguished at pot 0.35</td>
 </tr>
 <tr>
  <td>2/19/2014<br/>GMT 2014<br/>050</td>
  <td>12:52:07 to<br/>12:53:12</td>
  <td>13</td>
  <td>B12</td>
  <td>160</td>
  <td>300-µm film,<br/>2 cm wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>46.5</td>
  <td>2</td>
  <td>50</td>
  <td>---</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>off</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>160</td>
  <td>22.2</td>
  <td>22.1</td>
  <td>20.5</td>
  <td>20.4</td>
  <td>0.51</td>
  <td>0.56</td>
  <td>17</td>
  <td>33</td>
  <td>Mostly blue, soot only on bottom</td>
 </tr>
 <tr>
  <td>7/7/2014<br/>GMT 188</td>
  <td>---------</td>
  <td>63</td>
  <td>B13</td>
  <td>162m</td>
  <td>2-cm, 0.4-<br/>mm thick<br/>film</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>3.5 (68), 1.7,<br/>1.25, 0.9, 0.6, 0.4,<br/>0.35</td>
  <td>10, 5, 4, 3, 2, 1</td>
  <td>10</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>16</td>
  <td>311</td>
  <td>21.0</td>
  <td>20.5</td>
  <td>20.1</td>
  <td>19.6</td>
  <td>0.33</td>
  <td>0.65</td>
  <td>0</td>
  <td>61</td>
  <td>Multiple velocities for steady spread, extinguished at pot 0.35</td>
 </tr>
 <tr>
  <td>7/2/14<br/>GMT 183</td>
  <td>---------</td>
  <td>47</td>
  <td>B14</td>
  <td>174m</td>
  <td>1-cm-wide,<br/>200-µm-<br/>thick PMMA</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>----------------</td>
  <td>5, 3, 2,<br/>extinction</td>
  <td>250</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>----</td>
  <td>15.0</td>
  <td>-----</td>
  <td>14.1</td>
  <td>-----</td>
  <td>0.00</td>
  <td>-----</td>
  <td>0.2</td>
  <td>----</td>
  <td>HCl O, only brief ignition, flame extinguished</td>
 </tr>
 <tr>
  <td>7/7/2014<br/>GMT 188</td>
  <td>---------</td>
  <td>59</td>
  <td>B15</td>
  <td>149m</td>
  <td>2-cm, 0.1-<br/>mm PMMA<br/>film</td>
  <td>Integral 0</td>
  <td>Opposed</td>
  <td>1.4 (50) increase<br/>to 10.0 pot</td>
  <td>10, max</td>
  <td>10</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>12</td>
  <td>122</td>
  <td>21.0</td>
  <td>20.8</td>
  <td>20.1</td>
  <td>19.9</td>
  <td>0.33</td>
  <td>0.43</td>
  <td>0</td>
  <td>22</td>
  <td>Spread at 10 cm/s, did not blowoff</td>
 </tr>
 <tr>
  <td>7/2/14<br/>GMT 183</td>
  <td>---------</td>
  <td>51</td>
  <td>B16</td>
  <td>150m</td>
  <td>2-cm 100-<br/>µm-thick<br/>PMMA</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>----------------</td>
  <td>3, 5 pot, 0.4 pot</td>
  <td>250</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>94</td>
  <td>17.3</td>
  <td>17.2</td>
  <td>16.5</td>
  <td>16.4</td>
  <td>0.47</td>
  <td>0.51</td>
  <td>103</td>
  <td>119</td>
  <td>HCl 1.1 &gt; 1.3; flame quenched after prolonged burn at 0.4<br/>pot, one-sided flame; spread to top side and quenched<br/>immediately; did igniter wire affect top flame?</td>
 </tr>
 <tr>
  <td>7/2/14<br/>GMT 183</td>
  <td>---------</td>
  <td>48</td>
  <td>B17</td>
  <td>175m</td>
  <td>1-cm-wide,<br/>200-µm-<br/>thick PMMA</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>----------------</td>
  <td>5, 3, pot 0.4</td>
  <td>250</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>17</td>
  <td>190</td>
  <td>17.5</td>
  <td>17.4</td>
  <td>16.6</td>
  <td>16.5</td>
  <td>0.2</td>
  <td>0.34</td>
  <td>0</td>
  <td>47</td>
  <td>Burned steadily at higher flows, extinguished just as we<br/>reached a pot of 0.4; vapor jetting more on bottom, possibly<br/>because of sample tilted slightly to flow?</td>
 </tr>
</table>


aGreenwich Mean Time.
bPolymethylmethacrylate (PMMA).
cPotentiometer (pot).
dContinuous high (CH). Continuous low (CL).
eManual (M). Automatic (A).
fExposure value (#EV).
gNumber of frames and exposure increment (#F/1.0).
hContinuous (cont). Seconds (s).


NASA/TM-20210011385 103




#### TABLE A.1.-Concluded.


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)c</th>
 </tr>
 <tr>
  <td>7/2/14<br/>GMT 183</td>
  <td>---------</td>
  <td>49</td>
  <td>B18</td>
  <td>176m</td>
  <td>1-cm-wide,<br/>200-µm-<br/>thick PMMA</td>
  <td>Integral 0</td>
  <td>Opposed</td>
  <td>----------------</td>
  <td>10, blowoff</td>
  <td>250</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>11</td>
  <td>152</td>
  <td>17.4</td>
  <td>17.4</td>
  <td>16.5</td>
  <td>16.5</td>
  <td>0.34</td>
  <td>0.42</td>
  <td>47</td>
  <td>78</td>
  <td>HCl 0.6 &gt; 0.9, flame blew out at a fan pot of 7.0</td>
 </tr>
 <tr>
  <td>7/2/14<br/>GMT 183</td>
  <td>---------</td>
  <td>52</td>
  <td>B19</td>
  <td>151m</td>
  <td>2-cm, 100-<br/>µm-thick<br/>PMMA</td>
  <td>Integral 0</td>
  <td>Opposed</td>
  <td>----------------</td>
  <td>10, blowoff</td>
  <td>250</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>2</td>
  <td>95</td>
  <td>17.3</td>
  <td>17.2</td>
  <td>16.4</td>
  <td>16.3</td>
  <td>0.51</td>
  <td>0.57</td>
  <td>119</td>
  <td>131</td>
  <td>HCl 1.3 &gt; 1.4; flame blew out at a pot of 6.0</td>
 </tr>
 <tr>
  <td>2/19/2014<br/>GMT 2014<br/>050</td>
  <td>10:25:54 to<br/>10:26:34</td>
  <td>8</td>
  <td>B2</td>
  <td>155</td>
  <td>200-µm<br/>PMMA film,<br/>2 cm wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>62</td>
  <td>5</td>
  <td>50</td>
  <td>---</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>off</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>none</td>
  <td>22.2</td>
  <td>1.6</td>
  <td>20.6</td>
  <td>-----</td>
  <td>0.44</td>
  <td>-----</td>
  <td>6</td>
  <td>----</td>
  <td>No stills taken, cable came loose; not quite a straight on edge<br/>view</td>
 </tr>
 <tr>
  <td>7/2/14<br/>GMT 183</td>
  <td>---------</td>
  <td>50</td>
  <td>B20</td>
  <td>152m</td>
  <td>2-cm, 100-<br/>µm-thick<br/>PMMA</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>----------------</td>
  <td>5, 3, pot 0.5</td>
  <td>250</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>111</td>
  <td>17.4</td>
  <td>17.4</td>
  <td>16.5</td>
  <td>16.5</td>
  <td>0.42</td>
  <td>0.47</td>
  <td>78</td>
  <td>103</td>
  <td>HCl 0.9 &gt; 1.1; flame burned entire sample</td>
 </tr>
 <tr>
  <td>8/4/14<br/>GMT 216</td>
  <td>12:48:30</td>
  <td>121</td>
  <td>B21</td>
  <td>174m</td>
  <td>1-cm-wide,<br/>200-µm-<br/>thick PMMA</td>
  <td>46 1</td>
  <td>Opposed</td>
  <td>53 and down</td>
  <td>5 down to<br/>extinction</td>
  <td>250</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>88</td>
  <td>20.8</td>
  <td>20.6</td>
  <td>19.8</td>
  <td>19.6</td>
  <td>0.36</td>
  <td>0.44</td>
  <td>-1</td>
  <td>18</td>
  <td>Ignition at 5 cm/s then fan pot turned down slowly after<br/>flame; spreads halfway; flame goes out at 0.355 pot setting</td>
 </tr>
 <tr>
  <td>8/4/14<br/>GMT 216</td>
  <td>17:56:02</td>
  <td>126</td>
  <td>B22</td>
  <td>176m</td>
  <td>1-cm-wide,<br/>200-µm-<br/>thick PMMA</td>
  <td>39 1</td>
  <td>Opposed</td>
  <td>53, 42, 41, 40.5</td>
  <td>5, 2, 0</td>
  <td>250</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>8</td>
  <td>77</td>
  <td>20.7</td>
  <td>20.5</td>
  <td>19.8</td>
  <td>19.6</td>
  <td>0.41</td>
  <td>0.47</td>
  <td>-1</td>
  <td>10</td>
  <td>Ignition at 5 cm/s then decreased flow in step, fan pot 1.7,<br/>0.5, 0.4, 0.36 (flame out)</td>
 </tr>
 <tr>
  <td>2/19/2014<br/>GMT 2014<br/>050</td>
  <td>12:26:33 to<br/>12:27:01</td>
  <td>11</td>
  <td>B3</td>
  <td>148</td>
  <td>100-µm film,<br/>2 cm wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>47</td>
  <td>2</td>
  <td>50</td>
  <td>---</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>off</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>253</td>
  <td>22.2</td>
  <td>21.8</td>
  <td>20.9</td>
  <td>20.5</td>
  <td>0.43</td>
  <td>0.49</td>
  <td>12</td>
  <td>19</td>
  <td>Probably 20.6 O2 to start; lower flow flames much more blue<br/>overall; still some soot though</td>
 </tr>
 <tr>
  <td>2/19/2014<br/>GMT 2014<br/>050</td>
  <td>11:56:10 to<br/>11:57:06</td>
  <td>9</td>
  <td>B4</td>
  <td>159</td>
  <td>300-µm<br/>PMMA film,<br/>2 cm wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>61</td>
  <td>5</td>
  <td>50</td>
  <td>---</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>off</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>137</td>
  <td>22.2</td>
  <td>22.2</td>
  <td>20.6</td>
  <td>20.6</td>
  <td>0.44</td>
  <td>0.51</td>
  <td>-1</td>
  <td>10</td>
  <td>Bubble layer thickness increases with sample thickness</td>
 </tr>
 <tr>
  <td>2/19/2014<br/>GMT 2014<br/>050</td>
  <td>12:14:24 to<br/>12:15:07</td>
  <td>10</td>
  <td>B5</td>
  <td>156</td>
  <td>200 µm 2<br/>cm wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>59</td>
  <td>5</td>
  <td>50</td>
  <td>---</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>off</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>206</td>
  <td>22.2</td>
  <td>21.9</td>
  <td>20.9</td>
  <td>20.6</td>
  <td>0.43</td>
  <td>0.43</td>
  <td>0</td>
  <td>12</td>
  <td>Repeat of B2 test conditions, to get top view images; question<br/>the 20.9 reading; all others were 20.6 this day</td>
 </tr>
 <tr>
  <td>7/7/2014<br/>GMT 188</td>
  <td>---------</td>
  <td>57</td>
  <td>B6</td>
  <td>153m</td>
  <td>2-cm,<br/>0.1-mm<br/>PMMA film</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>0.9, 1.3, 2.75</td>
  <td>3, 5, approaching<br/>10</td>
  <td>10</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>8</td>
  <td>80</td>
  <td>21.0</td>
  <td>20.9</td>
  <td>20.1</td>
  <td>20.0</td>
  <td>0.33</td>
  <td>0.41</td>
  <td>0</td>
  <td>0.3</td>
  <td>Steady burning at 3 and 5 cm/s, did not reach 10 cm/s before<br/>end of sample, complete burnout, HCl -&gt;0.3</td>
 </tr>
 <tr>
  <td>2/19/2014<br/>GMT 2014<br/>050</td>
  <td>12:42:23 to<br/>12:43:48</td>
  <td>12</td>
  <td>B7</td>
  <td>161</td>
  <td>400-µm film,<br/>2 cm wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>47</td>
  <td>2</td>
  <td>50</td>
  <td>---</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>off</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>84</td>
  <td>22.2</td>
  <td>22.1</td>
  <td>20.6</td>
  <td>20.5</td>
  <td>0.45</td>
  <td>0.51</td>
  <td>1</td>
  <td>17</td>
  <td>Very long bubble layer</td>
 </tr>
 <tr>
  <td>7/7/2014<br/>GMT 188</td>
  <td>---------</td>
  <td>60</td>
  <td>B8</td>
  <td>157m</td>
  <td>2-cm,<br/>0.2-mm<br/>PMMA film</td>
  <td>Integral 0</td>
  <td>Opposed</td>
  <td>1.4, increase to<br/>10.0</td>
  <td>10, maximum</td>
  <td>10</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>12</td>
  <td>226</td>
  <td>21.0</td>
  <td>20.5</td>
  <td>20.1</td>
  <td>19.6</td>
  <td>0.33</td>
  <td>0.58</td>
  <td>0</td>
  <td>131</td>
  <td>Spread at 10 cm/s, did not blowoff</td>
 </tr>
 <tr>
  <td>7/7/2014<br/>GMT 188</td>
  <td>---------</td>
  <td>58</td>
  <td>B9</td>
  <td>154m</td>
  <td>2-cm,<br/>0.1-mm<br/>PMMA film</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>0.6, 0.35</td>
  <td>2, &lt;1</td>
  <td>10</td>
  <td>---</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>12</td>
  <td>45</td>
  <td>21.0</td>
  <td>20.9</td>
  <td>20.1</td>
  <td>20.0</td>
  <td>0.33</td>
  <td>0.35</td>
  <td>0</td>
  <td>10</td>
  <td>Steady burning at 2 cm/s, extinguished at 0.35</td>
 </tr>
</table>


aGreenwich Mean Time.
bPolymethylmethacrylate (PMMA).
cPotentiometer (pot).
dContinuous high (CH). Continuous low (CL).
eManual (M). Automatic (A).
fExposure value (#EV).
gNumber of frames and exposure increment (#F/1.0).
hContinuous (cont). Seconds (s).


NASA/TM-20210011385 104




## A.2 Ferkul Test Matrix


### TABLE A.2.-FERKUL TEST MATRIX


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)</th>
 </tr>
 <tr>
  <td>2/19/2014</td>
  <td>13:59 to</td>
  <td>14</td>
  <td>F1</td>
  <td>227</td>
  <td>Nomex®</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>82</td>
  <td>9.5</td>
  <td>250</td>
  <td></td>
  <td>8</td>
  <td>NA N CL</td>
  <td>M</td>
  <td>NA</td>
  <td>off</td>
  <td>1/10</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>208</td>
  <td>22.2</td>
  <td>22.2</td>
  <td>20.6</td>
  <td>20.6</td>
  <td>0.46</td>
  <td>0.45</td>
  <td>0</td>
  <td>2</td>
  <td>Ignited briefly but did not spread at all and extinguished</td>
 </tr>
 <tr>
  <td>GMT 2014<br/>050</td>
  <td>14:00</td>
  <td></td>
  <td></td>
  <td></td>
  <td>(DuPontTM)<br/>natural<br/>(Nomex III)</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td>while the igniter was still on</td>
 </tr>
 <tr>
  <td>7/28/2014<br/>GMT 209</td>
  <td>--------</td>
  <td>103</td>
  <td>F2</td>
  <td>228m</td>
  <td>Nomex®<br/>natural<br/>(Nomex III)</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>92</td>
  <td>15</td>
  <td>250</td>
  <td></td>
  <td>NA</td>
  <td>NA N CL</td>
  <td>M</td>
  <td>NA</td>
  <td>NA</td>
  <td>1/10</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>8</td>
  <td>72</td>
  <td>21</td>
  <td>21.0</td>
  <td>21</td>
  <td>21.0</td>
  <td>0.37</td>
  <td>0.39</td>
  <td>105</td>
  <td>82</td>
  <td>Tried to ignite, flame would not sustain</td>
 </tr>
 <tr>
  <td>8/1/14 GMT<br/>213</td>
  <td>8:58:25</td>
  <td>115</td>
  <td>F3</td>
  <td>229m</td>
  <td>Nomex®<br/>natural<br/>(Nomex III)</td>
  <td>Integral 1</td>
  <td>Concurrent</td>
  <td>61</td>
  <td>8</td>
  <td>50</td>
  <td></td>
  <td>NA</td>
  <td>NA N CL</td>
  <td>A</td>
  <td>-3</td>
  <td>NA</td>
  <td>------</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>13</td>
  <td>46</td>
  <td>21.7</td>
  <td>0.9</td>
  <td>20.8</td>
  <td>------</td>
  <td>0.36</td>
  <td>------</td>
  <td>2</td>
  <td>---</td>
  <td>Brief ignition flash, no sustained flame; no postburn sensor<br/>readings taken</td>
 </tr>
 <tr>
  <td>6/24/2018</td>
  <td>--------</td>
  <td>36</td>
  <td>F4</td>
  <td>39M</td>
  <td>Japan Wax<br/>candle</td>
  <td>Integral 2</td>
  <td>Stagnation</td>
  <td>See notes</td>
  <td>3 ignition</td>
  <td>250</td>
  <td></td>
  <td>NA</td>
  <td>NA N CH</td>
  <td>A</td>
  <td>-5</td>
  <td>9F 1.0</td>
  <td>------</td>
  <td>F2</td>
  <td>1,600</td>
  <td>7 s</td>
  <td>3</td>
  <td>270</td>
  <td>17.4</td>
  <td>17.4</td>
  <td>16.2</td>
  <td>16.2</td>
  <td>0.38</td>
  <td>0.48</td>
  <td>22</td>
  <td>56</td>
  <td>Long ignition, but blue flame established at 3 cm/s, reduced<br/>flow in increments: potentiometers 0.6, 0.4, 0.35, 0.32, 0.31,<br/>0.305 flame extinguished</td>
 </tr>
</table>


aGreenwich Mean Time.
bContinuous high (CH). Continuous low (CL). Shutter
cManual (M). Automatic (A).
dExposure value (#EV).
eNumber of frames and exposure increment (#F/1.0).
fContinuous (cont). Seconds (s).


NASA/TM-20210011385 105




## A.3 Fernandez-Pello Test Matrix


### TABLE A.3.-FERNANDEZ-PELLO TEST MATRIX


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)b</th>
 </tr>
 <tr>
  <td>6/16/14<br/>GMT 167</td>
  <td>----------</td>
  <td>25</td>
  <td>P1</td>
  <td>185m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-22 2</td>
  <td>Opposed</td>
  <td>------------</td>
  <td>5, 2, slow<br/>decrease to<br/>extinction</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>307</td>
  <td>17.7</td>
  <td>17.5</td>
  <td>16.6</td>
  <td>16.4</td>
  <td>0.27</td>
  <td>0.44</td>
  <td>1</td>
  <td>14</td>
  <td>Broke -20, -21 igniters, -22 worked; nice flame, got down to<br/>extinction at pot 0.315 (finite low flow), very slow increments</td>
 </tr>
 <tr>
  <td>7/3/2014<br/>GMT 184</td>
  <td>----------</td>
  <td>55</td>
  <td>P10</td>
  <td>187m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-35 2</td>
  <td>Opposed</td>
  <td>48, 41</td>
  <td>5, pots 0.4, 0.36,<br/>0.32, 0.31, 0.30<br/>extinguished</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>15</td>
  <td>221</td>
  <td>17</td>
  <td>16.4</td>
  <td>16.1</td>
  <td>15.5</td>
  <td>0.29</td>
  <td>0.72</td>
  <td>2</td>
  <td>44</td>
  <td>HCl 0.3 &gt; 0.9, steady burn at multiple velocities, finite<br/>quench at pot 0.3</td>
 </tr>
 <tr>
  <td>7/29/14<br/>GMT 210</td>
  <td>----------</td>
  <td>104</td>
  <td>P12</td>
  <td>199m</td>
  <td>9.525-mm<br/>black rod</td>
  <td>-36 2</td>
  <td>Opposed</td>
  <td>60, 52, 48, 44.5,<br/>42, 41.5, 41 (2.6,<br/>1.6, 1.2, 0.75, 0.5,<br/>0.4, 0.36, 0.34)</td>
  <td>5, 3, 2, 1, 0.5,<br/>lower</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>3</td>
  <td>273</td>
  <td>17.5</td>
  <td>16.8</td>
  <td>16.4</td>
  <td>15.7</td>
  <td>0.29</td>
  <td>0.95</td>
  <td>2</td>
  <td>57</td>
  <td>Loss of signal before extinguished, oscillating at 0.36, out<br/>immediately at 0.34, multiple steady spread flows</td>
 </tr>
 <tr>
  <td>7/14/14<br/>GMT 195</td>
  <td>14:30:00</td>
  <td>85</td>
  <td>P13a</td>
  <td>203m</td>
  <td>12.7-mm<br/>black rod</td>
  <td>-37 2</td>
  <td>Opposed</td>
  <td>Fan pot 1.1<br/>(5cm/s), 0.4,<br/>0.36, 0.32, 0.3,<br/>0.28, 0.26, 0 ext</td>
  <td>5 down to<br/>extinction</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>14</td>
  <td>255</td>
  <td>20.7</td>
  <td>19.1</td>
  <td>19.8</td>
  <td>18.2</td>
  <td>0.36</td>
  <td>1.63</td>
  <td>38</td>
  <td>450</td>
  <td>Fan pot 1.1 (5 cm/s), 0.4, 0.36, 0.32, 0.3, 0.28, 0.26; flame out<br/>when pot turned to 0; HCL 0.5 &gt; 4.1; flame reached front of<br/>sample and began to wrap around</td>
 </tr>
 <tr>
  <td>7/14/14<br/>GMT 195</td>
  <td>16:04:00</td>
  <td>86</td>
  <td>P13b</td>
  <td>203m</td>
  <td>12.7-mm<br/>black rod</td>
  <td>-37 2</td>
  <td>Opposed</td>
  <td>Fan pot 1.3<br/>(5cm/s), 0.4,<br/>0.36, 0.32 ext</td>
  <td>5 down to<br/>extinction</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>10</td>
  <td>94</td>
  <td>20.6</td>
  <td>20.2</td>
  <td>19.7</td>
  <td>19.3</td>
  <td>0.41</td>
  <td>0.62</td>
  <td>5</td>
  <td>72</td>
  <td>Fan pot 1.3 (5 cm/s), 0.4, 0.36, 0.32; flame out when pot<br/>turned to 0.32</td>
 </tr>
 <tr>
  <td>6/23/2014</td>
  <td>----------</td>
  <td>29</td>
  <td>P14</td>
  <td>189M</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-22 2</td>
  <td>Opposed</td>
  <td>46, 41</td>
  <td>5, low (0.85, 0.4,<br/>0.32)</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>162</td>
  <td>18.4</td>
  <td>18.0</td>
  <td>17.1</td>
  <td>16.7</td>
  <td>0.34</td>
  <td>0.62</td>
  <td>3</td>
  <td>90</td>
  <td>All blue, extinguished at 0.31</td>
 </tr>
 <tr>
  <td>6/23/2014</td>
  <td>----------</td>
  <td>30</td>
  <td>P15</td>
  <td>190M</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-22 2</td>
  <td>Opposed</td>
  <td>46, 41</td>
  <td>5, (0.36)</td>
  <td>250,<br/>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>170</td>
  <td>18.0</td>
  <td>17.5</td>
  <td>16.7</td>
  <td>16.2</td>
  <td>0.62</td>
  <td>1.11</td>
  <td>90</td>
  <td>108</td>
  <td>Nice stable burn with sooty tail but blue leading edge</td>
 </tr>
 <tr>
  <td>7/22/14<br/>GMT 203</td>
  <td>----------</td>
  <td>93</td>
  <td>P16</td>
  <td>191m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-36 2</td>
  <td>Concurrent</td>
  <td>49, 62, 44, 41.5,<br/>41 (pots 1.3, 2.8,<br/>0.7, 0.4, 0.36,<br/>0.32)</td>
  <td>5, 8, 2, low</td>
  <td>250,<br/>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>17</td>
  <td>129</td>
  <td>18.2</td>
  <td>17.4</td>
  <td>17.2</td>
  <td>16.4</td>
  <td>0.30</td>
  <td>0.92</td>
  <td>0</td>
  <td>56</td>
  <td>Extinguished at pot 0.32, one high flow setting</td>
 </tr>
 <tr>
  <td>7/29/14<br/>GMT 210</td>
  <td>----------</td>
  <td>105</td>
  <td>P17</td>
  <td>192m</td>
  <td>6.35-mm rod</td>
  <td>-36 2</td>
  <td>Opposed</td>
  <td>60, 52, 48, 233,<br/>48, 41 (2.6, 1.6,<br/>1.2, 10, 1.2, 0.36,<br/>0.34)</td>
  <td>5, 3, 2, 22, 2,<br/>low</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>186</td>
  <td>16.8</td>
  <td>16.5</td>
  <td>15.7</td>
  <td>15.4</td>
  <td>0.95</td>
  <td>1.34</td>
  <td>57</td>
  <td>68</td>
  <td>A few finite flows, then tried blowoff without success, turned<br/>back down to 2 cm/s, then 0.36, 0.34 pots, oscillated and out<br/>at 0.34; leading edge receded slightly but did not blowoff</td>
 </tr>
 <tr>
  <td>7/30/14<br/>GMT 211</td>
  <td>10:46:00</td>
  <td>107</td>
  <td>P18</td>
  <td>193m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>36 2</td>
  <td>Opposed</td>
  <td>55, 47, etc.<br/>(pot 1,2,1,2, etc.)</td>
  <td>2, 0, 2, 0, etc.</td>
  <td>250</td>
  <td>Saturated</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>280</td>
  <td>20.0</td>
  <td>19.0</td>
  <td>18.8</td>
  <td>17.8</td>
  <td>0.34</td>
  <td>1.20</td>
  <td>1</td>
  <td>26</td>
  <td>Alternated fan pot between 1 and 2 at 1-min intervals to try to<br/>get time constant resolution; finally turned pot down slowly,<br/>extinction at fan pot 0.32</td>
 </tr>
 <tr>
  <td>7/22/14<br/>GMT 203</td>
  <td>----------</td>
  <td>94</td>
  <td>P19</td>
  <td>194m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-36 2</td>
  <td>Concurrent</td>
  <td>49, 62, 44, 41.5,<br/>122, 41 (pots 1.3,<br/>2.8, 0.7, 0.4, 0.36,<br/>10., 0.32)</td>
  <td>5, 8, 2,<br/>maximum, 0</td>
  <td>250,<br/>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>2</td>
  <td>279</td>
  <td>17.5</td>
  <td>16.7</td>
  <td>16.5</td>
  <td>15.7</td>
  <td>0.90</td>
  <td>1.61</td>
  <td>54</td>
  <td>94</td>
  <td>Tried blowoff, did not blowoff at pot 10 2 restrictors, flame<br/>out at 0.32, sample mostly gone</td>
 </tr>
 <tr>
  <td>6/16/2014</td>
  <td>----------</td>
  <td>26</td>
  <td>P2</td>
  <td>188M</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-22 2</td>
  <td>Opposed</td>
  <td>------------</td>
  <td>5, 2.5, 2 (pot 0.9,<br/>0.5, 0.35, 0.33)</td>
  <td>250</td>
  <td>Nearly<br/>saturated</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>303</td>
  <td>17.4</td>
  <td>17.2</td>
  <td>16.4</td>
  <td>16.2</td>
  <td>0.44</td>
  <td>0.66</td>
  <td>14</td>
  <td>26</td>
  <td>Nice stable burn at low velocity, mostly blue with some inner<br/>soot at higher flow, stable flame at pot 0.33, did not get<br/>extinction on stills, but was just fan off, not slow ramp</td>
 </tr>
 <tr>
  <td>7/30/14<br/>GMT 211</td>
  <td>15:22:22</td>
  <td>109</td>
  <td>P20</td>
  <td>195m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>36 2</td>
  <td>Opposed</td>
  <td>55, 47, etc.<br/>(pot 1, 2, 1, 2,<br/>etc.)</td>
  <td>2, 0, 2, 0, etc.</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>2</td>
  <td>311</td>
  <td>19.0</td>
  <td>18.2</td>
  <td>17.9</td>
  <td>17.1</td>
  <td>0.34</td>
  <td>1.05</td>
  <td>2</td>
  <td>78</td>
  <td>Alternated fan pot between 1 and 2 at 1-min intervals to try to<br/>get time constant resolution; finally turned pot down slowly,<br/>extinction at fan pot 0.335</td>
 </tr>
 <tr>
  <td>6/23/2014<br/>GMT 174</td>
  <td>----------</td>
  <td>31</td>
  <td>P21a</td>
  <td>196M</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-22 2</td>
  <td>Opposed</td>
  <td>46</td>
  <td>5</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>57</td>
  <td>16.3</td>
  <td>16.3</td>
  <td>15</td>
  <td>15.0</td>
  <td>0.96</td>
  <td>1.00</td>
  <td>86</td>
  <td>94</td>
  <td>Flame self-extinguished at 5 cm/s after sample end became<br/>flat, dim flame</td>
 </tr>
 <tr>
  <td>6/23/2014</td>
  <td>----------</td>
  <td>32</td>
  <td>P21b</td>
  <td>196M</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-22 2</td>
  <td>Opposed</td>
  <td>46</td>
  <td>5</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>14</td>
  <td>16.3</td>
  <td>16.3</td>
  <td>15</td>
  <td>15.0</td>
  <td>1.00</td>
  <td>1.03</td>
  <td>94</td>
  <td>98</td>
  <td>Igniter broke after third attempt to ignite flattened end of<br/>sample</td>
 </tr>
</table>


aGreenwich Mean Time.
bPotentiometer (pot). Extinction (ext).
cContinuous high (CH). Continuous low (CL).
dManual (M). Automatic (A).
eExposure value (#EV).
fNumber of frames and exposure increment (#F/1.0).
gContinuous (cont). Seconds (s).


NASA/TM-20210011385 106




#### TABLE A.3.-Concluded.


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)b</th>
 </tr>
 <tr>
  <td>7/8/2014<br/>GMT 189</td>
  <td>----------</td>
  <td>68</td>
  <td>P22a</td>
  <td>200m</td>
  <td>9.525-mm<br/>black rod</td>
  <td>-35 2</td>
  <td>Opposed</td>
  <td>5, 0.36, 0.32<br/>extinction after<br/>some time</td>
  <td>5 down to<br/>extinction</td>
  <td>250 &gt;<br/>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>83</td>
  <td>20.8</td>
  <td>0.6</td>
  <td>20.2</td>
  <td>----</td>
  <td>0.32</td>
  <td>----</td>
  <td>4</td>
  <td>----</td>
  <td>Extinguished at higher flow, possibly rod not preheated<br/>enough by a bit, CO readings elevated, slow response</td>
 </tr>
 <tr>
  <td>7/8/2014<br/>GMT 189</td>
  <td>----------</td>
  <td>69</td>
  <td>P22b</td>
  <td>200m</td>
  <td>9.525-mm<br/>black rod</td>
  <td>-35 2</td>
  <td>Opposed</td>
  <td>5, 0.36, 0.34,<br/>0.33, 0.32, 0.31,<br/>extinction</td>
  <td>5 down to<br/>extinction</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>155</td>
  <td>20.0</td>
  <td>39.1</td>
  <td>----</td>
  <td>19.1</td>
  <td>----</td>
  <td>1.09</td>
  <td>----</td>
  <td>236</td>
  <td>Extinguished at lower flow than P22a by a bit, longer slower<br/>decrease in flow, CO elevated, slow response</td>
 </tr>
 <tr>
  <td>7/30/14<br/>GMT 211</td>
  <td>16:18:33</td>
  <td>110</td>
  <td>P23</td>
  <td>201m</td>
  <td>9.525-mm<br/>black rod</td>
  <td>36 2</td>
  <td>Opposed</td>
  <td>55, 47, etc.<br/>(pot 1, 2, 1, 2,<br/>etc.)</td>
  <td>2, 0, 2, 0, etc.</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>10</td>
  <td>242</td>
  <td>18.2</td>
  <td>17.0</td>
  <td>17.1</td>
  <td>15.9</td>
  <td>1.05</td>
  <td>2.08</td>
  <td>78</td>
  <td>159</td>
  <td>Alternated fan pot between 1 and 2 at 1-min then 2-min<br/>intervals to try to get time constant resolution; finally turned<br/>pot down slowly, extinction at fan pot 0.38</td>
 </tr>
 <tr>
  <td>7/30/14<br/>GMT 211</td>
  <td>11:13:35</td>
  <td>108</td>
  <td>P24</td>
  <td>819L</td>
  <td>9.525-mm<br/>black rod</td>
  <td>36 2</td>
  <td>Opposed</td>
  <td>55, 47, etc.<br/>(pot 1,2,1,2, etc.)</td>
  <td>2, 0, 2, 0, etc.</td>
  <td>250 &gt;<br/>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>308</td>
  <td>19.0</td>
  <td>17.5</td>
  <td>17.8</td>
  <td>16.3</td>
  <td>1.20</td>
  <td>2.24</td>
  <td>26</td>
  <td>260</td>
  <td>Alternated fan pot between 1 and 2 at 1-min intervals to try to<br/>get time constant resolution; finally turned pot down slowly,<br/>extinction at fan pot 0.30</td>
 </tr>
 <tr>
  <td>7/8/2014<br/>GMT 189</td>
  <td>----------</td>
  <td>70</td>
  <td>P25</td>
  <td>217m</td>
  <td>9.525-mm<br/>clear rod</td>
  <td>-36 2</td>
  <td>Opposed</td>
  <td>5, 0.36, 0.34,<br/>0.33, 0.32, 0.31,<br/>extinction</td>
  <td>5 down to<br/>extinction</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>17</td>
  <td>246</td>
  <td>20.9</td>
  <td>20.2</td>
  <td>19.9</td>
  <td>19.2</td>
  <td>0.38</td>
  <td>1.00</td>
  <td>43</td>
  <td>205</td>
  <td>Reburn of 217m in opposed geometry, repeat of P22b,<br/>extinguished at same 0.31 pot, more sparklers from flame,<br/>and less leading edge vapor jetting, or more central jetting;<br/>rod warped downward in video view at end of test,<br/>asymmetrical instabilities noted briefly at pot change to 0.32,<br/>CO elevated, slow response</td>
 </tr>
 <tr>
  <td>6/16/2014</td>
  <td>----------</td>
  <td>27</td>
  <td>P3a</td>
  <td>215M</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-22 2</td>
  <td>Opposed</td>
  <td>------------</td>
  <td>5, 2.5 (1.15, 0.5,<br/>0.35, 0.33. 0.32,<br/>0.315, 0.31, 0.3)</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>8</td>
  <td>304</td>
  <td>17.7</td>
  <td>17.4</td>
  <td>16.6</td>
  <td>16.3</td>
  <td>0.27</td>
  <td>0.51</td>
  <td>33</td>
  <td>----</td>
  <td>Repeat of last test with clear rod; extinguished at 0.3 pot very<br/>small flame, but steady spread</td>
 </tr>
 <tr>
  <td>6/16/2014</td>
  <td>----------</td>
  <td>28</td>
  <td>P3b</td>
  <td>215M</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-22 2</td>
  <td>Opposed</td>
  <td>------------</td>
  <td>5, very low<br/>(0.85, 0.32, 0.31,<br/>0.305, 0.30,<br/>0.295)</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>303</td>
  <td>17.4</td>
  <td>16.8</td>
  <td>16.3</td>
  <td>15.7</td>
  <td>0.51</td>
  <td>failed</td>
  <td>33</td>
  <td>79</td>
  <td>Very low velocity test to get limiting spread rate, pot 0.32<br/>spread, 0.31 spread, etc.; power failed to camera?; fan still<br/>running; camera power cable needed repair and taping to<br/>camera body to make it work</td>
 </tr>
 <tr>
  <td>7/3/2014<br/>GMT 184</td>
  <td>----------</td>
  <td>54</td>
  <td>P4</td>
  <td>197m</td>
  <td>9.525-mm<br/>black rod</td>
  <td>-35 2</td>
  <td>Opposed</td>
  <td>48, 41</td>
  <td>5, pots 0.4, 0.36,<br/>0.32, 0.308, .3,<br/>off</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>297</td>
  <td>18.5</td>
  <td>17.1</td>
  <td>17.6</td>
  <td>16.2</td>
  <td>0.62</td>
  <td>1.8</td>
  <td>64</td>
  <td>493</td>
  <td>HCl 0.9 &gt; 1.8, long slow burn, steady at multiple pots until<br/>turned off flow</td>
 </tr>
 <tr>
  <td>7/14/14<br/>GMT 195</td>
  <td>13:18:00</td>
  <td>83</td>
  <td>P5</td>
  <td>202m</td>
  <td>12.7-mm<br/>black rod</td>
  <td>-37 2</td>
  <td>Opposed</td>
  <td>Fan pot 1.5<br/>(5cm/s), 0.9, 0.4,<br/>0.36, 0.32, 0.308,<br/>0.3, 0.29, 0.28, 0,<br/>extinction</td>
  <td>5 down to<br/>extinction</td>
  <td>250 &gt;<br/>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>8</td>
  <td>313</td>
  <td>19.3</td>
  <td>17.6</td>
  <td>18.4</td>
  <td>16.7</td>
  <td>0.32</td>
  <td>1.67</td>
  <td>0</td>
  <td>525</td>
  <td>Fan pot 1.5 (5 cm/s), 0.9, 0.4, 0.36, 0.32, 0.308, 0.3, 0.29,<br/>0.28 (flame persisted for all) finally turned down flow to 0 to<br/>extinguish; HCL 0 &gt; 4.7; lots of fuel left behind, conical<br/>shape</td>
 </tr>
 <tr>
  <td>7/3/2014<br/>GMT 184</td>
  <td>----------</td>
  <td>53</td>
  <td>P6</td>
  <td>186m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-35 2</td>
  <td>Opposed</td>
  <td>48, 41</td>
  <td>5, pots 0.4, 0.36,<br/>0.32, 0.31, off</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>10</td>
  <td>162</td>
  <td>18.9</td>
  <td>18.5</td>
  <td>18</td>
  <td>17.6</td>
  <td>0.3</td>
  <td>0.62</td>
  <td>0</td>
  <td>64</td>
  <td>HCl 0 &gt; 0.9, steady burning until turned flow off, multiple pot<br/>settings</td>
 </tr>
 <tr>
  <td>7/3/2014<br/>GMT 184</td>
  <td>----------</td>
  <td>56</td>
  <td>P8</td>
  <td>197m</td>
  <td>9.525-mm<br/>black rod</td>
  <td>-35 2</td>
  <td>Opposed</td>
  <td>48, 62, 75</td>
  <td>5, would not stay<br/>lit, 10, 15 ibid</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>14</td>
  <td>66</td>
  <td>16.4</td>
  <td>16.3</td>
  <td>15.5</td>
  <td>15.4</td>
  <td>0.72</td>
  <td>0.81</td>
  <td>44</td>
  <td>69</td>
  <td>HCl 0.9 &gt; 0.9, would not stay lit, tip of sample was flat</td>
 </tr>
 <tr>
  <td>7/14/14<br/>GMT 195</td>
  <td>13:57:00</td>
  <td>84</td>
  <td>P9</td>
  <td>202m</td>
  <td>12.7-mm<br/>black rod</td>
  <td>-37 2</td>
  <td>Opposed</td>
  <td>Fan pot 1.5<br/>(5cm/s), 0.9, 0.4,<br/>0.36, 0.32, 0.3,<br/>0.28 extinction</td>
  <td>5 down to<br/>extinction</td>
  <td>50</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>15</td>
  <td>148</td>
  <td>17.6</td>
  <td>17.1</td>
  <td>16.7</td>
  <td>16.2</td>
  <td>1.67</td>
  <td>2.10</td>
  <td>525</td>
  <td>535</td>
  <td>Fan pot 1.5 (5 cm/s), 0.9, 0.4, 0.36, 0.32, 0.3, 0.28 flame out<br/>at 0.28; HCL 4.7 &gt; 4.5; flame did not leave conical portion<br/>behind, rather fuel was consumed but final sample shape was<br/>very irregular</td>
 </tr>
</table>


aGreenwich Mean Time.
bPotentiometer (pot).
cContinuous high (CH). Continuous low (CL). Shutter
dManual (M). Automatic (A).
eExposure value (#EV).
fNumber of frames and exposure increment (#F/1.0).
gContinuous (cont). Seconds (s).


NASA/TM-20210011385 107




## A.4 Miller Test Matrix


### TABLE A.4.-MILLER TEST MATRIX


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)c</th>
 </tr>
 <tr>
  <td>2/20/14<br/>GMT 2014-<br/>051</td>
  <td>---------</td>
  <td>15</td>
  <td>M1</td>
  <td>222</td>
  <td>1-mm-thick<br/>PMMA,<br/>one-sided, 2<br/>cm</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>58, 54</td>
  <td>10, 8</td>
  <td>50</td>
  <td>-----------</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>Off</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>304</td>
  <td>22.2</td>
  <td>21.9</td>
  <td>20.6</td>
  <td>20.3</td>
  <td>0.45</td>
  <td>0.61</td>
  <td>0</td>
  <td>60</td>
  <td>Prolonged ignition, flame initially on both sides, after igniter<br/>off and flame moved away from end, bottom flame died and<br/>top flame became all blue and small; very slow propagation;<br/>changed flow from 10 to 8 cm/s and flame shrank to a circle;<br/>spread just over 1/3 of sample when we ran out of camera<br/>card, and put flame out by turning off flow</td>
 </tr>
 <tr>
  <td>7/23/14<br/>GMT 204</td>
  <td>17:38</td>
  <td>97</td>
  <td>M10</td>
  <td>180m</td>
  <td>4-mm-thick,<br/>1-cm-wide<br/>PMMA slab</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>75, 105, 94/91,<br/>72/69, 63/61 (4.4,<br/>8.0, 6.6/6.3,<br/>4.0/3.7, 3/0/2.7)</td>
  <td>10, 17, 14, 10, 8</td>
  <td>250,<br/>50,<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>16</td>
  <td>209</td>
  <td>20.1</td>
  <td>18.6</td>
  <td>19</td>
  <td>17.5</td>
  <td>0.36</td>
  <td>1.59</td>
  <td>-1</td>
  <td>536</td>
  <td>Long burn, quick ignition, flame in seconds, kept it on 40 s +<br/>2nd on for another 10 to 15 s when it was shrinking; multiple<br/>flows for steady spreading; flame big at 17, so only left it<br/>there 3 min; other flows longer; flame self-extinguished at 8<br/>cm/s after almost 10 min; Alex saw it going out and locked<br/>shutter for the last few seconds; pictures start after ignition,<br/>about every 8 s</td>
 </tr>
 <tr>
  <td>7/11/14<br/>GMT 192</td>
  <td>---------</td>
  <td>80</td>
  <td>M11</td>
  <td>181m</td>
  <td>1-cm-wide<br/>PMMA 5<br/>mm thick</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>3.9, 6.5, 4.6, 3.3,<br/>2.9, 2.8; 62.5, 93,<br/>77, 66, 63, 62</td>
  <td>10, 20, 15, 12</td>
  <td>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>247</td>
  <td>20.0</td>
  <td>18.5</td>
  <td>19.1</td>
  <td>17.6</td>
  <td>0.58</td>
  <td>1.68</td>
  <td>46</td>
  <td>577</td>
  <td>29-min burn; extinguished at 12 cm/s., HCl 0.5 &gt; 5.0</td>
 </tr>
 <tr>
  <td>7/31/14<br/>GMT 212</td>
  <td>14:35:20</td>
  <td>114</td>
  <td>M12</td>
  <td>165m</td>
  <td>2-mm-thick<br/>PMMA, 2 cm<br/>wide</td>
  <td>Integral 1</td>
  <td>Opposed</td>
  <td>41, 42, 41</td>
  <td>&lt;1</td>
  <td>250 &gt;<br/>50</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>12</td>
  <td>271</td>
  <td>21.7</td>
  <td>20.4</td>
  <td>20.7</td>
  <td>19.4</td>
  <td>0.42</td>
  <td>1.42</td>
  <td>15</td>
  <td>443</td>
  <td>Vigorous ignition led to trying to get flame under control;<br/>finally had about plateaus at pot = 0.35, 0.4, and again 0.35</td>
 </tr>
 <tr>
  <td>7/31/14<br/>GMT 212</td>
  <td>12:18:54</td>
  <td>112</td>
  <td>M13</td>
  <td>169m</td>
  <td>4-mm-thick<br/>PMMA, 2 cm<br/>wide</td>
  <td>Integral 1</td>
  <td>Opposed</td>
  <td>52, 47, 43</td>
  <td>6, 5, 4</td>
  <td>250 &gt;<br/>50</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>11</td>
  <td>258</td>
  <td>20.8</td>
  <td>19.0</td>
  <td>19.8</td>
  <td>18.0</td>
  <td>0.36</td>
  <td>1.75</td>
  <td>0</td>
  <td>487</td>
  <td>Mild ignition at 10 cm/s; decreased flow down holding<br/>constant for 6 min at pot settings of 1.7, 1.0, and 0.55; finally<br/>extinguished by turning pot down to 0.3</td>
 </tr>
 <tr>
  <td>2/20/14<br/>GMT 2014-<br/>051</td>
  <td>---------</td>
  <td>16</td>
  <td>M14</td>
  <td>223</td>
  <td>2-mm-thick<br/>PMMA, one-<br/>sided, 2 cm<br/>wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>Pot 2.4, 1.87 (54)</td>
  <td>10, ~8</td>
  <td>50</td>
  <td>-----------</td>
  <td>?</td>
  <td>NA N</td>
  <td>S A</td>
  <td>-4</td>
  <td>Off</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Man</td>
  <td>8</td>
  <td>259</td>
  <td>22.2</td>
  <td>21.6</td>
  <td>20.6</td>
  <td>20.0</td>
  <td>0.45</td>
  <td>0.98</td>
  <td>0</td>
  <td>198</td>
  <td>Prolonged ignition, followed by flow reduction after flame<br/>moved away from igniter region and spread steadily; flame<br/>self-extinguished at an air reading of 9 cm/s.</td>
 </tr>
 <tr>
  <td>7/7/2014<br/>GMT 188</td>
  <td>---------</td>
  <td>64</td>
  <td>M15</td>
  <td>225m</td>
  <td>2-cm, 4-mm,<br/>one-sided<br/>PMMA slab</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>Ignited 10,<br/>adjusted down<br/>then up to 20,<br/>down in<br/>increments to 15</td>
  <td>10, 8, 7, 8, 10,<br/>20, 18, 16, 15</td>
  <td>10,<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>153</td>
  <td>21.0</td>
  <td>20.0</td>
  <td>20.1</td>
  <td>19.1</td>
  <td>0.37</td>
  <td>1.10</td>
  <td>1</td>
  <td>220</td>
  <td>Ignited and turned flow down to control flame size during end<br/>burning, then turned flow up to 20 cm/s and got steady<br/>spreading there, turned down flow to 15 and got spreading<br/>and slow extinction there.</td>
 </tr>
 <tr>
  <td>7/23/14<br/>GMT 204</td>
  <td>00:25</td>
  <td>99</td>
  <td>M16</td>
  <td>164m</td>
  <td>1-mm-thick<br/>PMMA, 2 cm<br/>wide</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>73, 57, 59, 48,<br/>45, 43, 75 (4.2,<br/>2.2, 2.4, 1.2, 0.8,<br/>0.5, 4.4)</td>
  <td>10, 6, 3, 2, 1, 10</td>
  <td>250,<br/>50,<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>299</td>
  <td>19.2</td>
  <td>18.7</td>
  <td>18.1</td>
  <td>17.6</td>
  <td>0.95</td>
  <td>1.75</td>
  <td>118</td>
  <td>421</td>
  <td>Burned at decreasing flow down to 1 cm/s or so, still fine, at<br/>end of sample, turned up flow to 10 cm/s and flame got really<br/>long; turned it down but Alex reported some soot on the door<br/>and some on the heat sink; dry wipe would not wipe off; try<br/>Monday with some other-water?</td>
 </tr>
 <tr>
  <td>7/15/14<br/>GMT 196</td>
  <td>15:12:00</td>
  <td>88</td>
  <td>M17</td>
  <td>166m</td>
  <td>2-cm-wide<br/>PMMA, 2<br/>mm thick</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>Fan pot 3.7, 1.7,<br/>1.5, 1.3, 0.8, 0.6,<br/>0.5, 0.3<br/>extinction</td>
  <td>10, 5, 3, 0,<br/>extinction</td>
  <td>250 &gt;<br/>50 &gt;<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>11</td>
  <td>309</td>
  <td>18.8</td>
  <td>17.1</td>
  <td>17.8</td>
  <td>16.1</td>
  <td>0.35</td>
  <td>1.70</td>
  <td>4</td>
  <td>485</td>
  <td>30-min burn targeted constant flows of 10, 5, and 3; finally<br/>turned fan pot to 0 to extinguish. HCl 0.3 &gt; 3.7</td>
 </tr>
 <tr>
  <td>7/15/14<br/>GMT 196</td>
  <td>12:40:00</td>
  <td>87</td>
  <td>M18</td>
  <td>168m</td>
  <td>2-cm-wide<br/>PMMA, 3<br/>mm thick</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>Fan pot 3.5, 5<br/>(brief), 3,5, 2.2</td>
  <td>10, 15 (brief), 10,<br/>8</td>
  <td>50 &gt;<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>178</td>
  <td>17.9</td>
  <td>16.8</td>
  <td>16.9</td>
  <td>15.8</td>
  <td>0.32</td>
  <td>1.31</td>
  <td>0</td>
  <td>335</td>
  <td>26-min burn; flow briefly at 15 cm/s but flame was too strong<br/>so turned down; HCl 0 &gt; 3.1, extinguished 8 cm/s</td>
 </tr>
</table>


aGreenwich Mean Time.
bPolymethylmethacrylate (PMMA).
cPotentiometer (pot).
dContinuous high (CH). Continuous low (CL). Shutter
eManual (M). Automatic (A).
fExposure value (#EV).
gNumber of frames and exposure increment (#F/1.0).
hContinuous (cont). Seconds (s).


NASA/TM-20210011385 108




#### TABLE A.4.-Concluded.


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)c</th>
 </tr>
 <tr>
  <td>7/23/14<br/>GMT 204</td>
  <td>23:37</td>
  <td>98</td>
  <td>M19</td>
  <td>170m</td>
  <td>4-mm-thick,<br/>2-cm, two-<br/>sided PMMA<br/>slab</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>75, 105, 94, 75,<br/>77, 79, 59, 61,<br/>57, 55, 53 (4.4,<br/>8.0, 6.6, 4.4, 4.6,<br/>4.8, 2.5, 2.7, 2.2,<br/>2.0, 1.8)</td>
  <td>10, 17, 14, 10, 7,<br/>5</td>
  <td>250,<br/>50,<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>8</td>
  <td>201</td>
  <td>19.0</td>
  <td>17.4</td>
  <td>17.9</td>
  <td>16.3</td>
  <td>0.35</td>
  <td>1.60</td>
  <td>3</td>
  <td>357</td>
  <td>Burned with decreasing flows until it went out on its own at 5<br/>cm/s</td>
 </tr>
 <tr>
  <td>2/20/14<br/>GMT 2014-<br/>051</td>
  <td>---------</td>
  <td>17</td>
  <td>M2</td>
  <td>224</td>
  <td>3-mm-thick<br/>PMMA one-<br/>sided, 2 cm<br/>wide</td>
  <td>Integral 0</td>
  <td>Opposed</td>
  <td></td>
  <td>20, 15, 13</td>
  <td>50</td>
  <td>-----------</td>
  <td>?</td>
  <td>NA N</td>
  <td>S A</td>
  <td>-4</td>
  <td>Off</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Man</td>
  <td>9</td>
  <td>262</td>
  <td>22.2</td>
  <td>21.2</td>
  <td>20.6</td>
  <td>19.6</td>
  <td>0.46</td>
  <td>1.33</td>
  <td>12</td>
  <td>325</td>
  <td>Ignite at 20 cm/s, turn down to 15 cm/s after spread away<br/>from igniter; seemed steady, so turned down to 13 cm/s;<br/>flame got very dim, so increased flow to 14 cm/s, but it self-<br/>extinguished</td>
 </tr>
 <tr>
  <td>8/1/14 GMT<br/>213</td>
  <td>11:10:50</td>
  <td>116</td>
  <td>M20</td>
  <td>172m</td>
  <td>5-mm-thick<br/>PMMA, 2 cm<br/>wide</td>
  <td>Integral 1</td>
  <td>Opposed</td>
  <td>67, 58</td>
  <td>10, 8</td>
  <td>50</td>
  <td>0.4 &gt; 1.2<br/>&gt; 0.8</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>168</td>
  <td>18.0</td>
  <td>17.4</td>
  <td>17.1</td>
  <td>16.5</td>
  <td>0.30</td>
  <td>0.75</td>
  <td>0</td>
  <td>157</td>
  <td>Flame took some time to establish, initially only on bottom of<br/>fuel; ignition at 10 cm/s (left 8 min) then flow down to 8 cm/s<br/>(flame out after 3 more minutes)</td>
 </tr>
 <tr>
  <td>7/11/14<br/>GMT 192</td>
  <td>---------</td>
  <td>82</td>
  <td>M3</td>
  <td>226m</td>
  <td>2-cm-wide,<br/>5-mm-thick,<br/>one-sided<br/>PMMA</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>3.0, 3.1, 3.2, 6.4,<br/>5.5, 5.4</td>
  <td>10, 20, 18</td>
  <td>250 &gt;<br/>50 &gt;<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>16</td>
  <td>-----</td>
  <td>20.8</td>
  <td>19.7</td>
  <td>19.9</td>
  <td>18.8</td>
  <td>0.33</td>
  <td>1.18</td>
  <td>11</td>
  <td>300</td>
  <td>Extinguished at 18 cm/s; HCl 0.6 &gt; 2.6</td>
 </tr>
 <tr>
  <td>7/31/14<br/>GMT 212</td>
  <td>13:59:12</td>
  <td>113</td>
  <td>M4</td>
  <td>171m</td>
  <td>5-mm-thick<br/>PMMA, 2 cm<br/>wide</td>
  <td>Integral 1</td>
  <td>Opposed</td>
  <td>52, 47, 43</td>
  <td>5, 4, 3</td>
  <td>250 &gt;<br/>50</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>16</td>
  <td>262</td>
  <td>21.8</td>
  <td>19.8</td>
  <td>20.7</td>
  <td>18.7</td>
  <td>0.42</td>
  <td>2.15</td>
  <td>2</td>
  <td>561</td>
  <td>Mild ignition at 10 cm/s; decreased flow down holding<br/>constant for 6 min at pot settings of 1.7, 1.0, and 0.55; finally<br/>extinguished by turning pot down to 0.3</td>
 </tr>
 <tr>
  <td>2/20/14<br/>GMT 2014-<br/>051</td>
  <td>---------</td>
  <td>18</td>
  <td>M5</td>
  <td>167</td>
  <td>3-mm-thick<br/>PMMA,<br/>two-sided,<br/>2 cm thick</td>
  <td>Integral 0</td>
  <td>Opposed</td>
  <td></td>
  <td>20, 13, 10, 8, 5</td>
  <td>50</td>
  <td>-----------</td>
  <td>?</td>
  <td>NA N</td>
  <td>S A</td>
  <td>-4</td>
  <td>Off</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Man</td>
  <td>10,<br/>14</td>
  <td>300+<br/>+102</td>
  <td>22.2</td>
  <td>19.0</td>
  <td>20.6</td>
  <td>17.4</td>
  <td>0.44</td>
  <td>3.22</td>
  <td>9</td>
  <td>&gt;500</td>
  <td>Rick ignited while we were loss of signal and out of contact<br/>with ISS, unfortunately; ignition was ~3 min per his verbal<br/>call down when we came back; flame already burning ~1/3 of<br/>sample, both sides, long and sooty; more vapor jetting on<br/>bottom due to molten ball attached there, visible when lights<br/>on to change camera card; turned down to 10 cm/s, then<br/>further down in increments to 5 cm/s; extinguished at 5 cm/s<br/>after prolonged flashing; during soot cleaning, Rick noticed<br/>damage to front door corner by the switches; He sent pictures<br/>down for us to evaluate for damage; CO reading posttest was<br/>came back 500</td>
 </tr>
 <tr>
  <td>7/31/14<br/>GMT 212</td>
  <td>11:12:57</td>
  <td>111</td>
  <td>M6</td>
  <td>163m</td>
  <td>1-mm-thick<br/>PMMA, 2 cm<br/>wide</td>
  <td>Integral 1</td>
  <td>Opposed</td>
  <td>68, 52, 47, 43,<br/>42, 41</td>
  <td>10, 5, 3, 0</td>
  <td>250</td>
  <td>Saturated<br/>at start</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>17</td>
  <td>269</td>
  <td>21.8</td>
  <td>20.7</td>
  <td>20.8</td>
  <td>19.7</td>
  <td>0.38</td>
  <td>1.27</td>
  <td>1</td>
  <td>345</td>
  <td>Aggressive ignition led to large flame initially; once flame<br/>settled down, we kept flow low and had two flow plateaus<br/>(pot 0.4 and 0.36); when flame reached end of sample it<br/>started backing up and spreading along the edges.</td>
 </tr>
 <tr>
  <td>7/11/14<br/>GMT 192</td>
  <td>---------</td>
  <td>81</td>
  <td>M7</td>
  <td>177m</td>
  <td>1-cm-wide<br/>PMMA, 1<br/>mm thick</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>2.6, 1.3, 0.8, 0.7,<br/>0.6, 0.5; 60, 49,<br/>45, 44, 43, 42</td>
  <td>10, 6, 5, 4.5, 4, 3</td>
  <td>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>12</td>
  <td>-----</td>
  <td>18.9</td>
  <td>18.4</td>
  <td>18</td>
  <td>17.5</td>
  <td>1.42</td>
  <td>1.84</td>
  <td>398</td>
  <td>612</td>
  <td>18 min burn; burned entire sample; HCl 2.2 &gt; 3.9</td>
 </tr>
 <tr>
  <td>7/11/14<br/>GMT 192</td>
  <td>---------</td>
  <td>79</td>
  <td>M8</td>
  <td>178m</td>
  <td>1-cm-wide<br/>PMMA, 2<br/>mm thick</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>3.3, 1.6, 1.0,<br/>decrease</td>
  <td>10, 5 &gt; 7, 5<br/>decrease</td>
  <td>50 &gt;<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>292</td>
  <td>19.1</td>
  <td>18.2</td>
  <td>18.2</td>
  <td>17.3</td>
  <td>0.44</td>
  <td>1.28</td>
  <td>52</td>
  <td>467</td>
  <td>25-min burn; turned down flow to extinguish, went out at pot<br/>0.4; HCl 0.4 &gt; 4.6</td>
 </tr>
 <tr>
  <td>7/11/14<br/>GMT 192</td>
  <td>---------</td>
  <td>78</td>
  <td>M9</td>
  <td>179m</td>
  <td>1-cm-wide<br/>PMMA, 3<br/>mm thick</td>
  <td>Integral 2</td>
  <td>Opposed</td>
  <td>3.3, 4.8; 66, 79</td>
  <td>10, 14</td>
  <td>50,<br/>250</td>
  <td>-----------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>2</td>
  <td>156</td>
  <td>18.0</td>
  <td>17.6</td>
  <td>17.1</td>
  <td>16.7</td>
  <td>0.26</td>
  <td>0.54</td>
  <td>0</td>
  <td>191</td>
  <td>Ignited at 10 cm/s, photographs every 5 s or so, turned up<br/>flow when flame looked weak; died after 15 min at 14 cm/s;<br/>17-min burn; HCl 0 &gt; 1.7</td>
 </tr>
</table>


aGreenwich Mean Time.
bPolymethylmethacrylate (PMMA).
cPotentiometer (pot).
dContinuous high (CH). Continuous low (CL).
eManual (M). Automatic (A).
fExposure value (#EV).
gNumber of frames and exposure increment (#F/1.0).
hContinuous (cont). Seconds (s).


NASA/TM-20210011385 109




## A.5 Olson Test Matrix


### TABLE A.5.-OLSON TEST MATRIX


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)c</th>
 </tr>
 <tr>
  <td>2/18/2014<br/>GMT 2014-<br/>049</td>
  <td>16:20-</td>
  <td>5</td>
  <td>O1</td>
  <td>207</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>0020-23 2</td>
  <td>?</td>
  <td>89, 62, 50, 41</td>
  <td>20, 10, 5, 2, 1</td>
  <td>50</td>
  <td>----</td>
  <td>8</td>
  <td>NA N</td>
  <td>CH A</td>
  <td>-5</td>
  <td>9F 1.0</td>
  <td>---</td>
  <td>F4</td>
  <td>1,600</td>
  <td>7s</td>
  <td>3</td>
  <td>62</td>
  <td>22.2</td>
  <td>21.7</td>
  <td>20.6</td>
  <td>20.1</td>
  <td>0.44</td>
  <td>0.85</td>
  <td>-1</td>
  <td>51</td>
  <td>Bracket test with decreasing flows; very sooty long flame at<br/>high flows; rod very thinned out and was wobbling due to<br/>vapor jetting later in test; Rick broke it off holder during<br/>readjustments</td>
 </tr>
 <tr>
  <td>7/22/14<br/>GMT 203</td>
  <td>13:26</td>
  <td>95</td>
  <td>O10</td>
  <td>210m</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-31 2</td>
  <td>Concurrent</td>
  <td>49, 44, 41, 122<br/>(1.3, 0.7, 0.4,<br/>0.36, 0.32, 10)</td>
  <td>5, 2, 0,<br/>maximum</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>172</td>
  <td>16.7</td>
  <td>16.1</td>
  <td>15.7</td>
  <td>15.1</td>
  <td>1.61</td>
  <td>2.10</td>
  <td>94</td>
  <td>287</td>
  <td>Leading edge (LE) blew out at fan 81, 25 s for rest of flame<br/>to blowoff at maximum flow</td>
 </tr>
 <tr>
  <td>7/8/2014<br/>GMT 189</td>
  <td>--------</td>
  <td>65</td>
  <td>O11</td>
  <td>184m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>-32 2</td>
  <td>Stagnation</td>
  <td>Ignition, 5, 0.36,<br/>0.32, 0.31, 0.305,<br/>blowoff 6.0</td>
  <td>5, down then<br/>blowoff</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>11</td>
  <td>271</td>
  <td>15.4</td>
  <td>14.8</td>
  <td>14.5</td>
  <td>13.9</td>
  <td>0.27</td>
  <td>0.72</td>
  <td>2</td>
  <td>290</td>
  <td>Repeat of clear rod O8b test, to compare black versus clear<br/>for stagnation flame, blowoff at pot of 6.0, fan slightly<br/>higher than O8b, HCl 2.8</td>
 </tr>
 <tr>
  <td>7/8/2014<br/>GMT 189</td>
  <td>--------</td>
  <td>67</td>
  <td>O12</td>
  <td>217m</td>
  <td>9.525-mm<br/>clear rod</td>
  <td>-32 2</td>
  <td>Stagnation</td>
  <td>pots 1.4, 3, 0.9,<br/>0.7</td>
  <td>No ignition at<br/>any flow</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>52</td>
  <td>13.6</td>
  <td>13.5</td>
  <td>12.7</td>
  <td>12.6</td>
  <td>1.72</td>
  <td>1.71</td>
  <td>+OR</td>
  <td>+OR</td>
  <td>No sustained flame at any flow, flame with igniter but died<br/>immediately upon igniter removal, HCL 12.3</td>
 </tr>
 <tr>
  <td>7/21/14<br/>GMT 202</td>
  <td>17:22</td>
  <td>91</td>
  <td>O13a</td>
  <td>221m</td>
  <td>12.7-mm<br/>clear PMMA<br/>rod</td>
  <td>-29 2</td>
  <td>Concurrent</td>
  <td>1.3, 0.7, 0.45,<br/>0.36, 0.32, 0.31</td>
  <td>49, 44, 42, 41,<br/>41, 40.5 (5, 2,<br/>0)</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>199</td>
  <td>15.9</td>
  <td>14.6</td>
  <td>14.9</td>
  <td>13.6</td>
  <td>0.91</td>
  <td>1.85</td>
  <td>389</td>
  <td>950</td>
  <td>Ignited and burned at 5 pot settings, flame self-extinguished<br/>after 3+ min at pot 0.31</td>
 </tr>
 <tr>
  <td>7/21/14<br/>GMT 202</td>
  <td>17:57</td>
  <td>92</td>
  <td>O13b</td>
  <td>221m</td>
  <td>12.7-mm<br/>clear PMMA<br/>rod</td>
  <td>-29 2</td>
  <td>Concurrent</td>
  <td>1.3, 0.9</td>
  <td>7, 4? (49, ?)</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>17</td>
  <td>6</td>
  <td>14.6</td>
  <td>14.4</td>
  <td>13.6</td>
  <td>13.4</td>
  <td>1.85</td>
  <td>2.09</td>
  <td>950</td>
  <td>Over</td>
  <td>Only stayed lit at 0.9 for less than a minute</td>
 </tr>
 <tr>
  <td>8/1/14 GMT<br/>213</td>
  <td>16:18:00</td>
  <td>117</td>
  <td>O14</td>
  <td>183m</td>
  <td>6.35-mm<br/>black rod</td>
  <td>39 1</td>
  <td>Concurrent</td>
  <td>52 and down</td>
  <td>5 down to<br/>extinction</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>8</td>
  <td>279</td>
  <td>16.3</td>
  <td>15.3</td>
  <td>15.3</td>
  <td>14.3</td>
  <td>0.29</td>
  <td>0.86</td>
  <td>4</td>
  <td>352</td>
  <td>Ignition at 5 cm/s then slow pot decreases to quenching pot<br/>0.28</td>
 </tr>
 <tr>
  <td>7/28/2014<br/>GMT 209</td>
  <td>11:36 msg</td>
  <td>100</td>
  <td>O15a</td>
  <td>218m</td>
  <td>9.525-mm<br/>clear rod</td>
  <td>-31 2</td>
  <td>Stagnation</td>
  <td>57.5, 47, 42, 41<br/>(2.3, 1.0, 0.5,<br/>0.35, 0.32)</td>
  <td>5,0</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>15</td>
  <td>124</td>
  <td>17.1</td>
  <td>16.7</td>
  <td>16</td>
  <td>15.6</td>
  <td>0.27</td>
  <td>0.62</td>
  <td>0</td>
  <td>176</td>
  <td>Decrease flow to extinction at 0.32 pot, from 0.35 pot. 1.5<br/>min at 5 cm/s; 2.5 min pot 1.0; 3.5 min at 0.5; 3.5 min 0.35;<br/>slow turn down to 0.32, flame out fairly quickly</td>
 </tr>
 <tr>
  <td>7/28/2014<br/>GMT 209</td>
  <td>11:59:30<br/>msg</td>
  <td>101</td>
  <td>O15b</td>
  <td>218m</td>
  <td>9.525-mm<br/>clear rod</td>
  <td>-31 2</td>
  <td>Stagnation</td>
  <td>57.5, 42, 41, 40<br/>(2.3, 0.5, 0.35,<br/>0.34, 0.33, 0.32,<br/>0.31, 0.30, 0.29,<br/>0.28, 0.27)</td>
  <td>5, 0</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>316</td>
  <td>16.7</td>
  <td>15.6</td>
  <td>15.6</td>
  <td>14.5</td>
  <td>0.62</td>
  <td>1.63</td>
  <td>176</td>
  <td>751</td>
  <td>Reburn of same rod as previous; decreased flow to extinction<br/>at 0.27 pot, much lower than previous; rod heatup effect? 1<br/>min 5 cm/s; 3.5 min pot 0.5; 5 min 0.35; 4 min 0.34; 4 min<br/>0.33; 3 min 0.32; 1 min 0.31; 1 min 0.3; 1 min 0.29; 1.5 min<br/>0.28; 0.27 out</td>
 </tr>
 <tr>
  <td>7/29/14<br/>GMT 210</td>
  <td>--------</td>
  <td>106</td>
  <td>O16</td>
  <td>219m</td>
  <td>9.525-mm<br/>clear rod</td>
  <td>-31 2</td>
  <td>Stagnation</td>
  <td>60 (2.6)</td>
  <td>5</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>7</td>
  <td>10<br/>postburn<br/>only</td>
  <td>14.5</td>
  <td>14.5</td>
  <td>13.4</td>
  <td>13.4</td>
  <td>0.27</td>
  <td>0.32</td>
  <td>2</td>
  <td>33</td>
  <td>Brief flame at end of first ignition, but no joy on sustained<br/>flame</td>
 </tr>
 <tr>
  <td>7/22/14<br/>GMT 203</td>
  <td>--------</td>
  <td>96</td>
  <td>O17</td>
  <td>211m</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-31 2</td>
  <td>Concurrent</td>
  <td>49, 46.5, 44,<br/>42,41,72,<br/>decrease (1.3,<br/>1.0, 0.7, 0.5, 0.4,<br/>4.0, decrease)</td>
  <td>3, 0, 11</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>12</td>
  <td>174</td>
  <td>15.1</td>
  <td>14.3</td>
  <td>14.1</td>
  <td>13.3</td>
  <td>0.31</td>
  <td>0.90</td>
  <td>2</td>
  <td>377</td>
  <td>Stable burns at slightly higher flows, LE blowoff at fan 72<br/>and turned down flow but flame did not recover and<br/>extinguished even after flow was down to 43-44</td>
 </tr>
 <tr>
  <td>7/28/2014<br/>GMT 209</td>
  <td>11:05</td>
  <td>102</td>
  <td>O18</td>
  <td>212m</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-31 2</td>
  <td>Stagnation</td>
  <td>57, 51, 47, 72,<br/>51, 72, 51, 47<br/>(2.3, 1.5, 1.0,<br/>4.0, 1.5, 4.0, 1.5,<br/>1.0)</td>
  <td>5, 2, 0, 11, 2,<br/>11, 2, 0</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>176</td>
  <td>15.2</td>
  <td>14.5</td>
  <td>14.1</td>
  <td>13.4</td>
  <td>1.45</td>
  <td>1.94</td>
  <td>523</td>
  <td>816</td>
  <td>Got rod hot, blue flame, turned flow up to pot 4.0, stag<br/>region blew out, Alex turned down quickly to 1.5 and got it<br/>to restabilize; we repeated it but it would not restabilize<br/>second time and flame extinguished after multiple<br/>oscillations at pot 1.0, after 1.5 would not restabilize</td>
 </tr>
 <tr>
  <td>8/1/14 GMT<br/>213</td>
  <td>16:49:00</td>
  <td>118</td>
  <td>O19</td>
  <td>213m</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>39 1</td>
  <td>Concurrent</td>
  <td>52 and down</td>
  <td>5 down to<br/>extinction</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>15</td>
  <td>266</td>
  <td>15.3</td>
  <td>14.6</td>
  <td>14.3</td>
  <td>13.6</td>
  <td>0.86</td>
  <td>1.51</td>
  <td>352</td>
  <td>686</td>
  <td>Ignition at 5 cm/s then slow pot decreases to quenching pot<br/>0.288</td>
 </tr>
 <tr>
  <td>2/18/14<br/>GMT2014-<br/>049</td>
  <td>--------</td>
  <td>6</td>
  <td>O2</td>
  <td>204</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>0020-23 2</td>
  <td>?</td>
  <td>0.54 pot and 0.45<br/>pot</td>
  <td>0</td>
  <td>50</td>
  <td>----</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>Off</td>
  <td>---</td>
  <td>F4</td>
  <td>1,600</td>
  <td>Cont</td>
  <td>3</td>
  <td>287</td>
  <td>22.2</td>
  <td>21.9</td>
  <td>20.6</td>
  <td>20.3</td>
  <td>0.44</td>
  <td>0.59</td>
  <td>-1</td>
  <td>23</td>
  <td>Ignited at 2 cm/s, and got dim flame that got sooty with lots<br/>of vapor jetting, reduced flow to 1.5 pot and got less vapor<br/>jetting test; still sooty at these low flows</td>
 </tr>
</table>


NASA/TM-20210011385 110




#### TABLE A.5.-Concluded.


<table>
 <tr>
  <th></th>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td>Test observations and anomalies (ignited, spread,<br/>extinguished, burn time, color, etc.)c</td>
 </tr>
 <tr>
  <th>6/13/2014<br/>GMT 164</th>
  <td>--------</td>
  <td>23</td>
  <td>O3a</td>
  <td>205M</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-23 2</td>
  <td>Concurrent</td>
  <td>------------</td>
  <td>5, 3</td>
  <td>1,000</td>
  <td>----</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>85</td>
  <td>18.0</td>
  <td>18.0</td>
  <td>15.9</td>
  <td>15.9</td>
  <td>0.25</td>
  <td>0.28</td>
  <td>16</td>
  <td>22</td>
  <td>Flame extinguished as soon as he turned flow down,<br/>probably overshot, flame sooty at 5 cm/s</td>
 </tr>
 <tr>
  <th></th>
  <td>--------</td>
  <td>24</td>
  <td>O3b</td>
  <td>205M</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-23 2</td>
  <td>Concurrent</td>
  <td>------------</td>
  <td>5, 3, 2, 1, low</td>
  <td>1,000<br/>and 250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>306</td>
  <td>18.0</td>
  <td>17.7</td>
  <td>15.9</td>
  <td>15.6</td>
  <td>0.28</td>
  <td>0.53</td>
  <td>22</td>
  <td>116</td>
  <td>Flame sooty even at lower flows, didn't get blue until air<br/>reading was zero</td>
 </tr>
 <tr>
  <th>7/8/2014<br/>GMT 189</th>
  <td>--------</td>
  <td>66</td>
  <td>O4</td>
  <td>216m</td>
  <td>9.525-mm<br/>clear rod</td>
  <td>-32 2</td>
  <td>Stagnation</td>
  <td>5, 0.7, 0.5, 0.4,<br/>0.36 extinction</td>
  <td>5 down to<br/>extinction</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CH A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>13</td>
  <td>249</td>
  <td>14.8</td>
  <td>13.6</td>
  <td>13.9</td>
  <td>12.7</td>
  <td>0.72</td>
  <td>1.72</td>
  <td>290</td>
  <td>+OR</td>
  <td>Larger rod, decreased flow, extinguished at 0.36, HCl 9.7</td>
 </tr>
 <tr>
  <th>7/21/14<br/>GMT 202</th>
  <td>15:59</td>
  <td>89</td>
  <td>O5a</td>
  <td>220m</td>
  <td>12.7-mm<br/>clear pmma<br/>rod</td>
  <td>-41, -42, - 2<br/>30</td>
  <td>Concurrent</td>
  <td>1.3, 2.7, 1.3, 0.7,<br/>0.45, 4.0</td>
  <td>5, 10, 5, 2, 0<br/>(49, 62, 49, 44,<br/>42)</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>13</td>
  <td>164</td>
  <td>15.1</td>
  <td>14.2</td>
  <td>14.1</td>
  <td>13.2</td>
  <td>0.25</td>
  <td>1.05</td>
  <td>-2</td>
  <td>496</td>
  <td>Hard to ignite, broke two igniters, burned for 9 min then<br/>blew out with pot of 4.0, tried to stay lit but blew off after<br/>multiple oscillations.</td>
 </tr>
 <tr>
  <th>7/21/14<br/>GMT 202</th>
  <td>17:02</td>
  <td>90</td>
  <td>O5b</td>
  <td>220m</td>
  <td>12.7-mm<br/>clear pmma<br/>rod</td>
  <td>-30 2</td>
  <td>Concurrent</td>
  <td>1.3</td>
  <td>49, 5 cm/s</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>2</td>
  <td>14.2</td>
  <td>14.1</td>
  <td>13.2</td>
  <td>13.1</td>
  <td>1.05</td>
  <td>1.14</td>
  <td>496</td>
  <td>590</td>
  <td>Would not sustain a flame without igniter on, broke igniter<br/>again</td>
 </tr>
 <tr>
  <th>6/26/2014</th>
  <td>--------</td>
  <td>37</td>
  <td>O6</td>
  <td>206M</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-24 2</td>
  <td>Stagnation</td>
  <td>5, 0.36, 0.32,<br/>0.31, 0.305, out<br/>0.275</td>
  <td>See fan</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>2</td>
  <td>241</td>
  <td>16.7</td>
  <td>16.0</td>
  <td>15.8</td>
  <td>15.1</td>
  <td>0.32</td>
  <td>0.74</td>
  <td>1</td>
  <td>232</td>
  <td>-----------------------------------------</td>
 </tr>
 <tr>
  <th>6/26/2014</th>
  <td>--------</td>
  <td>38</td>
  <td>O7</td>
  <td>214m</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-24 2</td>
  <td>Stagnation</td>
  <td>5, 0.36, 0.32,<br/>0.305, blowoff<br/>fan max 10</td>
  <td>------------</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>14</td>
  <td>254</td>
  <td>16.0</td>
  <td>15.5</td>
  <td>15.1</td>
  <td>14.6</td>
  <td>0.74</td>
  <td>1.27</td>
  <td>232</td>
  <td>512</td>
  <td>Blowoff fan 97, HCl post 4.9</td>
 </tr>
 <tr>
  <th>6/26/2014</th>
  <td>--------</td>
  <td>39</td>
  <td>O8a</td>
  <td>208m</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-24 2</td>
  <td>Stagnation</td>
  <td>5, 0.36, 0.32,<br/>0.31,<br/>extinguished</td>
  <td>------------</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>15</td>
  <td>133</td>
  <td>15.7</td>
  <td>15.3</td>
  <td>14.8</td>
  <td>14.4</td>
  <td>1.23</td>
  <td>1.44</td>
  <td>436</td>
  <td>536</td>
  <td>Quench at pot 0.31, HCL 4.8 to 5.9</td>
 </tr>
 <tr>
  <th>6/26/2014</th>
  <td>--------</td>
  <td>40</td>
  <td>O8b</td>
  <td>208m</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-24 2</td>
  <td>Stagnation</td>
  <td>5, 0.36, 0.32,<br/>0.31 blowoff fan<br/>pot 6.0</td>
  <td>------------</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>17</td>
  <td>152</td>
  <td>15.5</td>
  <td>15.2</td>
  <td>14.4</td>
  <td>14.1</td>
  <td>1.44</td>
  <td>1.74</td>
  <td>536</td>
  <td>660</td>
  <td>Blowoff fan 78, HCl prepost 5.9 to 7.9</td>
 </tr>
 <tr>
  <th>6/26/2014</th>
  <td>--------</td>
  <td>41</td>
  <td>O9</td>
  <td>209m</td>
  <td>6.35-mm<br/>clear rod</td>
  <td>-24 2</td>
  <td>Stagnation</td>
  <td>5, 0.36, 0.32<br/>blowoff pot 4.0</td>
  <td>------------</td>
  <td>250</td>
  <td>----</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>NA</td>
  <td>---</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>13</td>
  <td>154</td>
  <td>15.0</td>
  <td>14.8</td>
  <td>14.1</td>
  <td>13.9</td>
  <td>1.74</td>
  <td>1.96</td>
  <td>660</td>
  <td>794</td>
  <td>Blowoff fan 68, HCl 7.5 to 9.3</td>
 </tr>
</table>


aGreenwich Mean Time.
bPolymethylmethacrylate (PMMA).
cPotentiometer (pot). Maximum (max).
dContinuous high (CH). Continuous low (CL). Shutter
eManual (M). Automatic (A).
fExposure value (#EV).
gNumber of frames and exposure increment (#F/1.0).
hContinuous (cont). Seconds (s).


NASA/TM-20210011385 111




## A.6 T'ien Test Matrix


### TABLE A.6.-T'IEN TEST MATRIX


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread, extinguished, burn time, color, etc.)c</th>
 </tr>
 <tr>
  <td>2/14/2014 GMT 2014-45</td>
  <td>12:45:40 to 12:47:10</td>
  <td>1</td>
  <td>T1</td>
  <td>128</td>
  <td>SIBAL 2 cm</td>
  <td>Integrated 2</td>
  <td>1</td>
  <td>80</td>
  <td>10</td>
  <td>50</td>
  <td>0.97 maximum</td>
  <td>10</td>
  <td>0 N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>100 s</td>
  <td>2</td>
  <td>85</td>
  <td>18.5</td>
  <td>18.5</td>
  <td>17.3</td>
  <td>17.3</td>
  <td>0.35</td>
  <td>0.41</td>
  <td>0</td>
  <td>40</td>
  <td>Compound Specific Analyzer-Combustion Products (CSA- CP) unit 1024; Carbon Dioxide Monitor (CDM) unit 1018; Prefill O2 reading = 20.9 percent; GN2 fill was from video display time 10:53 to 12:31 at maximum GN2 flow rate (pot = 10); Video display time is currently 1 day plus 6 min 10 s ahead of actual GMT; flow velocity held constant</td>
 </tr>
 <tr>
  <td>6/24/2018</td>
  <td>----------</td>
  <td>34</td>
  <td>T10</td>
  <td>134M</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>Pot 1.1</td>
  <td>5</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>43</td>
  <td>16.4</td>
  <td>16.5</td>
  <td>15.2</td>
  <td>15.3</td>
  <td>0.31</td>
  <td>0.33</td>
  <td>9</td>
  <td>14</td>
  <td>Brief ignition but flame extinguished before spreading beyond igniter</td>
 </tr>
 <tr>
  <td>6/27/2014</td>
  <td>----------</td>
  <td>42</td>
  <td>T11</td>
  <td>135m</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>48</td>
  <td>5</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>12</td>
  <td>109</td>
  <td>17.1</td>
  <td>17.0</td>
  <td>16.2</td>
  <td>16.1</td>
  <td>0.35</td>
  <td>0.39</td>
  <td>1</td>
  <td>45</td>
  <td>Burned completely, steady, HCl 0.3 to 0.9</td>
 </tr>
 <tr>
  <td>6/27/14 GMT 178</td>
  <td>----------</td>
  <td>44</td>
  <td>T12</td>
  <td>136m</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>Pot 1.1</td>
  <td>5</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1000</td>
  <td>Cont</td>
  <td>16</td>
  <td>39</td>
  <td>16.8</td>
  <td>16.9</td>
  <td>15.9</td>
  <td>16.0</td>
  <td>0.7</td>
  <td>0.7</td>
  <td>113</td>
  <td>117</td>
  <td>Extinguished quickly</td>
 </tr>
 <tr>
  <td>4/10/2014 GMT 100</td>
  <td>----------</td>
  <td>21</td>
  <td>T13</td>
  <td>137</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td></td>
  <td>5,1</td>
  <td>50</td>
  <td>---------</td>
  <td>8</td>
  <td>NA n</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>14</td>
  <td>55</td>
  <td>17.5</td>
  <td>17.6</td>
  <td>15.9</td>
  <td>16.0</td>
  <td>0.19</td>
  <td>0.20</td>
  <td>2</td>
  <td>12</td>
  <td>HCL 0.2 end, 0.1 start, no HCN, flame extinguished quickly after flow change.</td>
 </tr>
 <tr>
  <td>6/27/14 GMT 178</td>
  <td>----------</td>
  <td>45</td>
  <td>T14</td>
  <td>140m</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td></td>
  <td>5, 3</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>16</td>
  <td>119</td>
  <td>16.9</td>
  <td>16.9</td>
  <td>16</td>
  <td>16.0</td>
  <td>0.7</td>
  <td>0.72</td>
  <td>117</td>
  <td>152</td>
  <td>Extinguished as we reduced flow below 3 cm/s</td>
 </tr>
 <tr>
  <td>2/14/2014 GMT 2014-45</td>
  <td>15:48:35 to 15:49:12</td>
  <td>4</td>
  <td>T15</td>
  <td>138</td>
  <td>SIBAL 2 cm</td>
  <td>Integrated 0</td>
  <td>1</td>
  <td>80, 122</td>
  <td>9, 29</td>
  <td>50</td>
  <td>1.68 maximum</td>
  <td>10</td>
  <td>0 N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>100 s</td>
  <td>5</td>
  <td>46</td>
  <td>18.7</td>
  <td>18.7</td>
  <td>17.5</td>
  <td>17.5</td>
  <td>0.45</td>
  <td>0.51</td>
  <td>72</td>
  <td>102</td>
  <td>Initial air reading is 15, but Rick did not wait long enough for the anemometer to stabilize; actual airspeed is about 9 cm/s; no flow restrictors installed, but flow only maxed out to 29 cm/s; no blowoff attained</td>
 </tr>
 <tr>
  <td>4/10/2014 GMT 100</td>
  <td>----------</td>
  <td>22</td>
  <td>T16</td>
  <td>139</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td></td>
  <td>5, 3</td>
  <td>50</td>
  <td>---------</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>14</td>
  <td>100</td>
  <td>17.6</td>
  <td>17.5</td>
  <td>16.0</td>
  <td>15.9</td>
  <td>0.21</td>
  <td>0.21</td>
  <td>17</td>
  <td>41</td>
  <td>Initial HCl 0.2 final 0.5, no HCN, flame spread whole sample at 3 cm/s</td>
 </tr>
 <tr>
  <td>6/27/14 GMT 178</td>
  <td>----------</td>
  <td>46</td>
  <td>T17</td>
  <td>142m</td>
  <td>2 cm SIBAL</td>
  <td>Integral 0</td>
  <td>Concurrent</td>
  <td></td>
  <td>6, 53</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>83</td>
  <td>16.9</td>
  <td>16.9</td>
  <td>16</td>
  <td>16.0</td>
  <td>0.72</td>
  <td>0.75</td>
  <td>152</td>
  <td>190</td>
  <td>Tried to blowoff, but did not</td>
 </tr>
 <tr>
  <td>6/24/2018</td>
  <td>----------</td>
  <td>35</td>
  <td>T18</td>
  <td>141M</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td></td>
  <td>5, 2</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>49</td>
  <td>17.4</td>
  <td>17.4</td>
  <td>16.2</td>
  <td>16.2</td>
  <td>0.36</td>
  <td>0.38</td>
  <td>2</td>
  <td>22</td>
  <td>Brief ignition but flame extinguished as it spread away from igniter, further than previous runs today</td>
 </tr>
 <tr>
  <td>7/9/14 GMT 190</td>
  <td>----------</td>
  <td>71</td>
  <td>T19</td>
  <td>143m</td>
  <td>1 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>68.5, pot 3.6</td>
  <td>11</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>73</td>
  <td>17.2</td>
  <td>17.2</td>
  <td>16.3</td>
  <td>16.3</td>
  <td>0.29</td>
  <td>0.31</td>
  <td>1</td>
  <td>20</td>
  <td>Steady burn, HCL 0.3 &gt; 0.6</td>
 </tr>
 <tr>
  <td>2/14/2014 GMT 2014-45</td>
  <td>13:08:58 to 13:10:35</td>
  <td>2</td>
  <td>T2</td>
  <td>129</td>
  <td>SIBAL 2 cm</td>
  <td>Integrated 2</td>
  <td>1</td>
  <td>80, 59, 55</td>
  <td>9, 5, 4</td>
  <td>50</td>
  <td>0.64 maximum</td>
  <td>10</td>
  <td>0 N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>100 s</td>
  <td>2</td>
  <td>100</td>
  <td>18.5</td>
  <td>18.5</td>
  <td>17.3</td>
  <td>17.3</td>
  <td>0.41</td>
  <td>0.45</td>
  <td>40</td>
  <td>78</td>
  <td>Flow velocity changed to 9 to 5 fairly early then very late in the burn changed to 4</td>
 </tr>
 <tr>
  <td>7/9/14 GMT 190</td>
  <td>----------</td>
  <td>72</td>
  <td>T20</td>
  <td>144m</td>
  <td>1 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>3.6, 0.9</td>
  <td>11, 3</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>117</td>
  <td>17.2</td>
  <td>17.2</td>
  <td>16.3</td>
  <td>16.3</td>
  <td>0.31</td>
  <td>0.31</td>
  <td>20</td>
  <td>34</td>
  <td>Quick extinction when we turned air down to 3 cm/s, HCl 0.8 end</td>
 </tr>
 <tr>
  <td>7/9/14 GMT 190</td>
  <td>----------</td>
  <td>73</td>
  <td>T21</td>
  <td>145m</td>
  <td>1 cm SIBAL</td>
  <td>Integral 0</td>
  <td>Concurrent</td>
  <td>1.6 pot, 52</td>
  <td>11, maximum (47)</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>151</td>
  <td>17.2</td>
  <td>17.2</td>
  <td>16.3</td>
  <td>16.3</td>
  <td>0.31</td>
  <td>0.32</td>
  <td>34</td>
  <td>45</td>
  <td>Successful blowoff! HCl still 0.8 end</td>
 </tr>
 <tr>
  <td>7/9/14 GMT 190</td>
  <td>----------</td>
  <td>76</td>
  <td>T22</td>
  <td>146m</td>
  <td>1 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>3.4, 1.7</td>
  <td>10, 5</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>38</td>
  <td>17.1</td>
  <td>17.0</td>
  <td>16.2</td>
  <td>16.1</td>
  <td>0.59</td>
  <td>0.62</td>
  <td>140</td>
  <td>162</td>
  <td>Ignited at 11, turned down to 5 and extinguished, HCl 2.0</td>
 </tr>
 <tr>
  <td>7/9/14 GMT 190</td>
  <td>----------</td>
  <td>74</td>
  <td>T23</td>
  <td>133m</td>
  <td>2 cm SI, moved igniter</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>3.3, 66</td>
  <td>10</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>9</td>
  <td>203</td>
  <td>17.2</td>
  <td>17.3</td>
  <td>16.3</td>
  <td>16.4</td>
  <td>0.32</td>
  <td>0.32</td>
  <td>45</td>
  <td>49</td>
  <td>Did not ignite with moved igniter, HCl 0.8</td>
 </tr>
 <tr>
  <td>7/9/14 GMT 190</td>
  <td>----------</td>
  <td>77</td>
  <td>T24</td>
  <td>133m</td>
  <td>1 cm SIBAL, top side ign</td>
  <td>-29 2</td>
  <td>Concurrent</td>
  <td>3.3, 66</td>
  <td>10</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>4</td>
  <td>130</td>
  <td>18.2</td>
  <td>18.2</td>
  <td>17.7</td>
  <td>17.7</td>
  <td>0.51</td>
  <td>0.53</td>
  <td>85</td>
  <td>107</td>
  <td>Ignited top of sample with retractable igniter and got steady spread of a one-sided flame</td>
 </tr>
</table>


aGreenwich Mean Time.
bSIBAL is Solid Inflammability Boundary at Low Speeds.
cPotentiometer (pot).
dContinuous high (CH). Continuous low (CL). Shutter
eManual (M). Automatic (A).
fExposure value (#EV).
gNumber of frames and exposure increment (#F/1.0).
hContinuous (cont). Seconds (s).


NASA/TM-20210011385 112




#### TABLE A.6.-Concluded.


<table>
 <tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
  <th>Test observations and anomalies (ignited, spread, extinguished, burn time, color, etc.)c</th>
 </tr>
 <tr>
  <td>8/4/14 GMT 216</td>
  <td>12:13:20</td>
  <td>119</td>
  <td>T25</td>
  <td>138m</td>
  <td>SIBAL 2 cm</td>
  <td>39 1</td>
  <td>Concurrent</td>
  <td>53, 45</td>
  <td>5, 2.5</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>14</td>
  <td>75</td>
  <td>20.8</td>
  <td>20.7</td>
  <td>19.8</td>
  <td>19.7</td>
  <td>0.36</td>
  <td>0.39</td>
  <td>-1</td>
  <td>17</td>
  <td>Ignition at 5 cm/s then decrease to 2.5 cm/s and hold constant</td>
 </tr>
 <tr>
  <td>8/4/14 GMT 216</td>
  <td>12:28:44</td>
  <td>120</td>
  <td>T26</td>
  <td>137m</td>
  <td>SIBAL 2 cm</td>
  <td>39 1</td>
  <td>Concurrent</td>
  <td>53, 45</td>
  <td>5, 2.5</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>14</td>
  <td>87</td>
  <td>20.8</td>
  <td>20.7</td>
  <td>19.8</td>
  <td>19.7</td>
  <td>0.36</td>
  <td>0.43</td>
  <td>-1</td>
  <td>24</td>
  <td>Ignition at 5 cm/s then decrease to 2.5 cm/s and hold constant</td>
 </tr>
 <tr>
  <td>8/4/14 GMT 216</td>
  <td>17:08:10</td>
  <td>122</td>
  <td>T27</td>
  <td>146m</td>
  <td>1 cm SIBAL</td>
  <td>39 1</td>
  <td>Concurrent</td>
  <td>53, 45</td>
  <td>5, 2</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>58</td>
  <td>20.7</td>
  <td>20.6</td>
  <td>19.8</td>
  <td>19.7</td>
  <td>0.41</td>
  <td>0.42</td>
  <td>-1</td>
  <td>9</td>
  <td>Ignition at 5 cm/s, then quickly to 2 cm/s (fan pot 0.7); fuel is burned out</td>
 </tr>
 <tr>
  <td>8/4/14 GMT 216</td>
  <td>17:21:03</td>
  <td>123</td>
  <td>T28a</td>
  <td>144m</td>
  <td>1 cm SIBAL</td>
  <td>39 1</td>
  <td>Concurrent</td>
  <td>53</td>
  <td>5</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>19</td>
  <td>20.7</td>
  <td>0.9</td>
  <td>19.8</td>
  <td>------</td>
  <td>0.41</td>
  <td>------</td>
  <td>-1</td>
  <td>----</td>
  <td>Tried to get one-sided ignition, but flame only briefly flashed then went out</td>
 </tr>
 <tr>
  <td>8/4/14 GMT216</td>
  <td>17:29:49</td>
  <td>124</td>
  <td>T28b</td>
  <td>144m</td>
  <td>1 cm SIBAL</td>
  <td>39 1</td>
  <td>Concurrent</td>
  <td>53</td>
  <td>5</td>
  <td>250</td>
  <td>--------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>27</td>
  <td>20.7</td>
  <td>40.4</td>
  <td>------</td>
  <td>19.7</td>
  <td>------</td>
  <td>0.42</td>
  <td>----</td>
  <td>2</td>
  <td>Tried to get one-sided ignition, but again flame only briefly flashed then went out</td>
 </tr>
 <tr>
  <td>8/4/14 GMT 216</td>
  <td>17:39:30</td>
  <td>125</td>
  <td>T29</td>
  <td>145m</td>
  <td>1 cm SIBAL</td>
  <td>39 1</td>
  <td>Concurrent</td>
  <td>53, 43</td>
  <td>5, 2(?)</td>
  <td>250</td>
  <td>--------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>5</td>
  <td>60</td>
  <td>20.7</td>
  <td>20.5</td>
  <td>19.8</td>
  <td>19.6</td>
  <td>0.41</td>
  <td>0.44</td>
  <td>-1</td>
  <td>10</td>
  <td>Alex commented that he thought the angle of the igniter should be reversed to get one-sided ignition, so he tried that; one-sided flame initially but quickly became two-sided; after ignition, fan pot changed to 0.6 and flame went out after a few seconds</td>
 </tr>
 <tr>
  <td>6/27/14 GMT 178</td>
  <td>----------</td>
  <td>43</td>
  <td>T3</td>
  <td>182m</td>
  <td>4 cm spherical section</td>
  <td>-24 broke, 2 -25</td>
  <td>Stagnation</td>
  <td>63</td>
  <td>10</td>
  <td>250</td>
  <td>--------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-4</td>
  <td>1/4</td>
  <td>F4</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>3, 8</td>
  <td>166</td>
  <td>17.2</td>
  <td>16.8</td>
  <td>16.3</td>
  <td>15.9</td>
  <td>0.42</td>
  <td>0.7</td>
  <td>45</td>
  <td>113</td>
  <td>Multiple ignition attempts on card 3, brief flames go out</td>
 </tr>
 <tr>
  <td>2/14/2014 GMT 2014- 45</td>
  <td>15:20:15 to 15:21:15</td>
  <td>3</td>
  <td>T4</td>
  <td>130</td>
  <td>SIBAL 2 cm</td>
  <td>Integrated 2</td>
  <td>1</td>
  <td>80, 46</td>
  <td>9,1</td>
  <td>50</td>
  <td>0.19 maximum</td>
  <td>10</td>
  <td>0 N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>100 s</td>
  <td>5</td>
  <td>97</td>
  <td>18.7</td>
  <td>18.7</td>
  <td>17.5</td>
  <td>17.5</td>
  <td>0.44</td>
  <td>0.45</td>
  <td>59</td>
  <td>72</td>
  <td>O2 reading creeped up slightly after a long pause in operations; flow velocity changed immediately after ignition down to 1 (fan pot 0.9); extinguished after turning into flamelet</td>
 </tr>
 <tr>
  <td>4/10/2014 GMT 100</td>
  <td>14:27 to 14:29</td>
  <td>19</td>
  <td>T5</td>
  <td>131</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>2.72, 0.50, 0.42</td>
  <td>10, 2, 1</td>
  <td>50</td>
  <td>--------</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>11</td>
  <td>100</td>
  <td>18.8</td>
  <td>18.9</td>
  <td>16.7</td>
  <td>16.8</td>
  <td>0.20</td>
  <td>0.25</td>
  <td>2</td>
  <td>41</td>
  <td>HCN 0 HCL 0.6; ignited at 10, turned down to 2, then 1, sample very small and dim, but seemed to burn full sample length as a flamelet</td>
 </tr>
 <tr>
  <td>4/10/2014 GMT 100</td>
  <td>14:51 to 15:53</td>
  <td>20</td>
  <td>T6</td>
  <td>132</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td></td>
  <td>5, 2, 1, &lt;1</td>
  <td>50</td>
  <td>----------</td>
  <td>8</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>1/8</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>11</td>
  <td>117</td>
  <td>18.8</td>
  <td>18.8</td>
  <td>16.7</td>
  <td>16.7</td>
  <td>0.24</td>
  <td>0.28</td>
  <td>39</td>
  <td>77</td>
  <td>HCL 0.9 at the end, still did not extinguish</td>
 </tr>
 <tr>
  <td>7/9/14 GMT 190</td>
  <td>----------</td>
  <td>75</td>
  <td>T7</td>
  <td>182m</td>
  <td>4 cm spherical section</td>
  <td>-33, -34 2</td>
  <td>Stagnation</td>
  <td>3.4, 67</td>
  <td>10, 5, 3, 1, decrease</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL A</td>
  <td>-3</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>3</td>
  <td>299</td>
  <td>17.3</td>
  <td>17.1</td>
  <td>16.4</td>
  <td>16.2</td>
  <td>0.32</td>
  <td>0.59</td>
  <td>49</td>
  <td>140</td>
  <td>Broke one igniter quickly, took a while to ignite, turned pot down in series ignition at 3.4, 1.6, 1.0, 0.4, 0.36, 0.34, 0.32, 0.31, 0.30, 0.29, 0.285, 0.28 extinction finally, HCl 1.8</td>
 </tr>
 <tr>
  <td>6/24/2018</td>
  <td>----------</td>
  <td>33</td>
  <td>T9</td>
  <td>133M</td>
  <td>2 cm SIBAL</td>
  <td>Integral 2</td>
  <td>Concurrent</td>
  <td>Pot 2.5</td>
  <td>10</td>
  <td>250</td>
  <td>---------</td>
  <td>NA</td>
  <td>NA N</td>
  <td>CL M</td>
  <td>NA</td>
  <td>----</td>
  <td>F2</td>
  <td>1,000</td>
  <td>Cont</td>
  <td>6</td>
  <td>48</td>
  <td>16.4</td>
  <td>16.4</td>
  <td>15.2</td>
  <td>15.2</td>
  <td>0.30</td>
  <td>0.31</td>
  <td>0</td>
  <td>9</td>
  <td>Brief ignition but flame extinguished before spreading beyond igniter</td>
 </tr>
</table>


aGreenwich Mean Time.
bSIBAL is Solid Inflammability Boundary at Low Speeds.
cPotentiometer (pot).
dContinuous high (CH). Continuous low (CL). Shutter
eManual (M). Automatic (A).
fExposure value (#EV).
gNumber of frames and exposure increment (#F/1.0).
hContinuous (cont). Seconds (s).


NASA/TM-20210011385 113






##### Appendix B.-Microgravity Science Glovebox Work Volume Nitrogen Dilution Continuously Stirred Tank Reactor Model and On-Orbit Verification Testing of Model


### B.1 Symbols


Cin concentration of O2 entering work volume, = 0 (pure N2)
Co initial concentration of O2 in the work volume
Cout concentration of O2 exiting the work volume, = c(t), a continuously stirred tank reactor (CSTR)
property
c(t) concentration of O2 in the work volume as a function of time
r flow rate of gaseous N2, 0.0005 m3/min maximum, adjustable
T temperature
V volume of Microgravity Science Glovebox (MSG) working volume, 0.25 m3


### B.2 Information


The continuously stirred tank reactor (CSTR) model is based on a mole balance on O2


as follows:


1. The control volume is the working volume, with an input of N2 and a leak rate of well-mixed gas.

2. Boundary and conditions: a. Concentration of O2 coming into the work volume Cin = 0 (pure N2) b. Cout = c(t) (CSTR property) c. Initial concentration of O2 in the work volume C(0) = Co


The rate of change of the O2 concentration c(t) with time t within the work volume V equation is
given by the flow of gaseous N2 (r) multiplied by the difference between the inlet (Cin) and outlet O2
concentrations (Cout)


V =r( Cin - Cout ) - = =rCout -rc( )t (B.1)


dc
dt


3. Integrating and applying initial conditions:


-r 
c( t) = Co exp t 
V 


(B.2)


Astronaut Chris Cassidy conducted a calibration test on the morning of GMT (Greenwich Mean
Time) 2013-095 in the Microgravity Science Glovebox (MSG) using a Compound Specific Analyzer-
Combustion Products (CSA-CP) sensor taking O2 readings of the MSG working volume at intervals
during the dilution. During dilution, the Burning and Suppression of Solids (BASS) duct fan was turned
to maximum, and the working volume air circulation was deactivated. To validate the model, we used the
following values in the model based upon the test conditions:


• MSG working volume (Ref. 1) = 0.255 m3
• BASS-II hardware = ~0.005 m3
• Net volume V = ~0.25 m3


NASA/TM-20210011385 115




- N2 flow rate in = 493 cm3/min or 0.000493 m3/min

- Initial O2 concentration c(0) = Co

- CSA-CP sensor C(0) = 20.9 percent O2 • International Space Station Major Constituents Analyzer (MCA) = 21.48 available from NASA Johnson Space Center)


percent O2 (data


Figure B.1 shows the calibration data compared to the model predictions for both the CSA-CP
readings and corrected for the offset from the MCA. The model agrees very well with CSA-CP readings
directly and corrected for the offset to provide a calibrated O2 level with time. The curvature is minimal
due to the slow rate of N2 flow into the large volume.
This model was used for subsequent BASS-II operations to determine the N2 flow rate and flow time
to achieve the desired test O2 concentration based upon the initial O2 concentration and operational crew
time constraints. It worked very well, and postdilution CSA-CP readings agreed extremely well with the
model predictions over a range of dilution rates, as shown in Figure B.2. The CSA-CP readings were then
corrected for the offset from the MCA readings for that day to provide a calibrated O2 reading for each
test.


Figure B.1.-Model verification of continuously stirred tank reactor (CSTR)
modeling the Microgravity Science Glovebox (MSG) dilution using Compound
Specific Analyzer-Combustion Products (CSA-CP) sensor O2 readings. Sensor
data taken at intervals during dilution show how measurements agree with model
curve (Eq. (B.2)). Data symbols are sized to ±0.1 percent O2, resolution of
sensor. Raw CSA-CP data and corrected data for Major Constituents Analyzer
(MCA) offset are shown with model predictions using initial reading as starting
value.


NASA/TM-20210011385 116




Figure B.2.-Dilution model compared to fast, slow, and average dilution rates
during Burning and Suppression of Solids-II (BASS-II) operations. Data from
three BASS-II tests and continuously stirred tank reactor (CSTR) model
(Eq. (B.2)) results show range of dilution times and O2 levels obtained. Control
of both flow rate and dilution time allowed us to work around crew schedules
while still obtaining desired working volume O2 concentration for test.
Compound Specific Analyzer-Combustion Products (CSA-CP).


### B.3 References


1 Spivey, Reggie A., et al.: An Overview of the Microgravity Science Glovebox (MSG) Facility, and
the Gravity-Dependent Phenomena Research Performed in the MSG on the International Space
Station (ISS). AIAA 2008-812, 2008.


NASA/TM-20210011385 117






#### Appendix C.-List of Preflight, In-Flight, and Postflight Anomalies


1. An anomaly occurred on 2014 Greenwich Mean Time (GMT) 51, where the lower right corner of the Lexan door overheated and bubbled due to a flow leak at that spot during a very long burn. The damage affected the door interlock switches, as was found during inspection on GMT 58. A repair plan to recover switch functionality and seal the door leaks was implemented successfully on GMT 86 and 91, as shown in Figure C.1, and operations have continued since then without further door damage.

2. After the end of operations on GMT 167, the experiment video dropped out and was intermittent. Inspection on GMT 168 indicated it was the connector on the back of the camera, and a repair to the cable was successfully implemented on GMT 170, as shown in Figure C.2, that restored the experiment video. A backup plan to utilize a different camera was not required. For future operations, a new camera cable will be launched.

3. During operations on GMT 205, during a high-flow blowoff attempt with a flat polymethylmethacrylate sample, some flame briefly vapor-jetted out from the open sides of the sample holder toward the window before the flame was extinguished. The crew noted a soot spot that did not come off with a dry wipe. On the next operations day, GMT 209, prior to the start of operations, the crew used a wet wipe to remove the residue, and operations continued nominally without further incident.


Figure C.1.-Repaired duct door seal and interlocks, showing bubbled lower right corner.


NASA/TM-20210011385 119




Figure C.2.-Video cable repair and strain relief.


NASA/TM-20210011385 120




#### Appendix D.-Heat Release Rate and Hardware Temperature Rise Estimates for Burning and Suppression of Solids-II Thick Polymethylmethacrylate Slab Samples


### D.1 Symbols


Q  steady total heat release
 Qair kJ/min of energy carried out of the Burning and Suppression of Solids (BASS) flow duct


ρ density of air; 1.2 kg/m3


cp heat capacity of air 1 kJ/kg K
H duct height; 7.5 cm = 0.075 m
m mass
r0 initial regression rate
rmax peak regression rate
t time
U flow velocity; 30 cm/s = 0.3 m/s = 18 m/min
W duct width; 7.5 cm = 0.075 m
∆T change in temperature


### D.2 Introduction


The principal investigator Sandra L. Olson wrote this report on January 10, 2014.


### D.3 Purpose of the Analysis


Burning and Suppression of Solids-II (BASS-II) samples are larger than previously flown samples,
and there is a concern that the hardware will become overheated and be damaged by the burning of these
large samples. This analysis is to estimate the temperature rise of the BASS experiment assembly for a
worst-case flame for this large thick sample. It should be noted that we have no plans to run a test like this.
Assumptions:


- The worst-case sample is the 0.5-cm-thick, 8.5-cm-long, and 2-cm-wide polymethylmethacrylate (PMMA) slab sample.

- The worst-case flame is a concurrent flame, which is expected to be larger than an opposed flame. Note that these samples are actually expected to be used only for opposed flow, but we do not want to restrict ourselves so assume the larger flame for these calculations.

- The worst-case flame is a two-sided burn, assumed to burn symmetrically. • The sample will burn stoichiometrically. • The flame will grow to reach a steady-state size. • The ambient flow condition will be air at 30 cm/s, three times the highest flow in the test matrix for these samples, again, so that we are not restricted by the current test plan. • The maximum burn time is the time it takes to burn the largest sample completely. • The air leaving the flow duct is in equilibrium temperature with the exhaust hardware.


NASA/TM-20210011385 121




Figure D.1.-Predicted flame temperature profile for flame in forced flow velocity U of


60-cm/s flow, from Reference 1. Polymethylmethacrylate (PMMA).


### D.4 Background


The basis for the burning rate estimates presented here are based on both a computational study
looking at the burning rate distribution for boundary layer flow combustion of a PMMA plate in forced
flow, shown in Figure D.1, (Ref. 1), and BASS test results from a 1-cm PMMA sphere burning in a
stagnation flow (which captures the burning of the exposed base of the sample). A thick PMMA slab will
take time to ignite and grow to a steady-state size, and the sample burning rate distribution is an important
quantity to determine how much heat is being generated by the flame.


### D.5 Analysis


As can be seen in Figure D.2, the base of the flame (at x = 0) has the highest burning rate and there is
an exponential decay in the regression rate away from that peak burning rate. Using peak regression rate
(rmax) for the four flow profiles given, we can extrapolate down to the 30-cm/s flow of interest.
The exposed base of the flame (the upstream most point) will be the strongest part of the flame, and
the burning rate is expected to be a maximum there. Based on data in the Section D.7 from a 1-cm-sphere
BASS test, we estimate the regression rate to be 3.05 mm/min, which is in keeping with the estimates
from Figure D.2, as shown in Figure D.3. The downstream regression rates will decay exponentially from
there, as shown in Figure D.2.


NASA/TM-20210011385 122




Figure D.2.-Peak regression rates from Figure D.2 curve fit with expected
root trend as flow is reduced (Ref. 2). Fit is used to calculate extrapolated
At 30 cm/s, peak regression rate is estimated to be 3.13 mm/min.


square
points.


Figure D.3.-Power law growth pattern used to predict flame size as function of


time.


The sample is 8.5 cm long, so at 3.05 mm/min, it will take ~28 min for the flame base to regress the
entire length of the sample. Note that this is way beyond the still camera card limit of 7 min.
The flame will take some time to grow the steady-state size. To estimate the growth rate, we use an
expected power law growth rate (Ref. 3) and estimate the flame will grow to a steady-state size in
approximately 2.5 min, as shown in Figure D.3.
This growth rate is quite reasonable, since a previous BASS test showed that a PMMA slab sample
took over 3 min to grow to steady size, as shown in the Section D.7. Using the experimental growth
history and peak regression rates, we can estimate the regression rate profiles as a function of time.
These regression profiles (which occur on both sides of the sample) can then be used to determine
how much fuel is being consumed each minute. We do this by adding up the regression at each x location
(basically, the area under the curves) and also multiplying that value by the width of the sample (2 cm).
Note that these profiles are derived from steady slab burning where a significant fraction of the heat
release is returned to the fuel for preheating or reradiated to the environment.


NASA/TM-20210011385 123




Figure D.4.-Estimated regression rate profiles at different times for 30-cm/s flame. Also shown, total
burning rate with time during transient.


The total cubic mm of fuel per minute can then be converted to a heat release rate by assuming
stoichiometric burning on both sides of the fuel, and an O2 consumption calorimetry-based heat release
rate of 13.1 kJ/g of O2.


C5H8O2 + 6 O2 → 5 CO2 + 4 H2O


m m3 2 sides gram fuel gmol fuel stoichiometric gmol O


× × × 2


minimum side sample m m3 gram fuel stoichiometric gmol fuel


gram O 2 13.1 kJ 1,000 J J 
×××Q= 
gmo O gram O l2 2 kJ comb min 


Values used:


- 1.19 g/cc fuel density (1.19 mg/mm3)

- 100 g/gmol fuel • 32 g/gmol O2 • 6 gmol O2/1 gmol fuel


The steady total heat release rate Q  is 72 W based on these regression rates and properties. Ignition
energy is estimated by using 4-A current through a 1-Ω igniter or 16 W. This heat is carried through the
flow duct and out into the Microgravity Science Glovebox (MSG). The experiment housing will absorb
some of this heat.
The rate at which the combustion energy is carried out of the hardware by the air can be calculated:


-  kJ

-  = ρc


min °C pUHW


 ⋅



Qair 





∆T 


where  Qair is the kJ/min of energy carried out of the BASS flow duct, ΔT is the temperature change, the
density of air ρ is 1.2 kg/m3, the heat capacity of air cp is 1 kJ/kg K, the forced flow velocity U is 30 cm/s,
0.3 m/s, or 18 m/min, and the duct height H and width W is 7.5 cm or 0.075 m.


NASA/TM-20210011385 124





The air carries air ∆ QT = 121.5 J/min Δ°C. The heat exchanger components the hot exhaust gas


passes through can be found in Table D.1. These are connected to the main housing of the experiment
assembly, which is about 1,580 g of aluminum, and more remotely, the total mass of the Experiment
Assembly is 6.94 kg.
To determine the hardware temperature with time (t), we simply sum the mass (m) times the heat
capacity (cp) of each hardware component times a temperature change:


 ρ +∑ ∆ =
Qt  ( cpUHW p )air mc Texhaust 


where Q  is the total heat release rate in watts and Texhaust is the temperature of the exhaust gas after
passing through each component and solve for ΔT. This is shown in Figure D.5 for just the exhaust
hardware, the main housing, and the total experiment assembly.


TABLE D.1.-HEAT EXCHANGER COMPONENTS


<table>
 <tr>
  <th>Hardware</th>
  <th>Mass,<br/>g</th>
  <th>Material</th>
  <th>Heat capacity,<br/>kJ/kg°C</th>
  <th>Melting temperature,<br/>°C</th>
 </tr>
 <tr>
  <td>Heat sink</td>
  <td>250</td>
  <td>Copper</td>
  <td>0.4</td>
  <td>1,085</td>
 </tr>
 <tr>
  <td>Soot housing</td>
  <td>58</td>
  <td>Aluminum</td>
  <td>0.9</td>
  <td>660</td>
 </tr>
 <tr>
  <td>Soot cover</td>
  <td>32</td>
  <td>Aluminum</td>
  <td>0.9</td>
  <td>660</td>
 </tr>
 <tr>
  <td>Screens</td>
  <td>50</td>
  <td>Bronze</td>
  <td>0.4</td>
  <td>950</td>
 </tr>
</table>


Figure D.5.-Estimated heat release rate and associated temperature
rise with time for various total mass quantities.


NASA/TM-20210011385 125




The maximum burn time is assumed to be the 2.5-min growth phase plus the 28-min sample
regression phase, for a total of 30.5 min, as plotted in Figure D.5. The maximum temperatures reported in
the following information are for this maximum burn time.
The heat release in the early phase is dominated by the ignition energy. Once the combustion heat
release approaches steady state, the igniter is turned off and the flame is sustained.
The maximum temperature will occur in the exhaust hardware. This metal (primarily copper)
hardware is built to take the hot combustion gases and cool via conduction to the other hardware. The
maximum temperature if all of the combustion energy is only deposited in this heat sink under these
worst-case assumptions, is 434 °C, which is below the melting point of the lowest melting material
(aluminum at 660 °C) so this absolute worst-case maximum temperature will not cause damage to the
hardware. This maximum temperature will not be realized in actuality because the heat will quickly
dissipate to the main housing, which reaches a maximum temperature of 110 °C if all of the heat is
distributed only there. The experiment assembly dissipates the heat further, and the maximum
temperature of the entire experiment assembly is 62 °C.
During the 10-min cooldown for these thick samples, both the flow through the BASS duct and the
MSG air circulation fans help dissipate the heat. The MSG air cooling loop has a 125-W capacity, which
would dissipate the energy in 18 min, assuming no dissipation via conduction to the MSG hardware.
Based on this worst-case analysis, it is not expected that the hardware will suffer any damage from
the worst-case, largest flames that could be achieved with the BASS-II samples.


### D.6 References


1. Ananth, Ramagopal; Ndubizu, Chuka C.; and Tatem, P.A.: Burning Rate Distributions for Boundary Layer Flow Combustion of a PMMA Plate in Forced Flow. Combust. Flame, vol. 135, nos. 1-2, 2003, pp. 35-55.

2. Olson, S., et al.: Sounding Rocket Microgravity Experiments Elucidating Diffusive and Radiative Transport Effects on Flame Spread Over Thermally Thick Solids. Combust. Sci. Technol., vol. 176, 2004, pp. 557-584.

3. Olson, Sandra, et al.: Pressure Response in Enclosures During and After Large-Scale Flame Spread: Testing and Modeling. AIAA 2013-3412, 2013. 4. Olson, S.: Convective Heat Transfer Scaling of Ignition Delay and Burning Rate With Heat Flux and Stretch Rate in the Equivalent Low Stretch Apparatus. Fire Saf. Sci., vol. 10, 2011, pp. 959-970.


NASA/TM-20210011385 126




## D.7 Appendix-Polymethylmethacrylate Growth to Steady Size


In Figure D.6, a one-sided PMMA slab was burned at a slow flow. The 1-cm-wide sample took


7.5 min for the total test time, with the ignition taking over 1 min. Flame reached steady size in about


3 min and was only 15 mm long. The spread rate was 0.037 mm/s (0.0037 cm/s or 2.2 mm/min).
The BASS 1-cm sphere had an initial mass of 617.5 mg. Sample 19 (1-cm PMMA sphere) was
completely consumed in four tests (various high- and low-flow speeds) with the burn durations in
Table D.2.
The total burn time was 5 min and 25 s (325 s). The average burning rate was 617.5/325 = 1.9 mg/s.
Assume this occurs over the surface of the sphere where A = 4πr2 = 3.14 × 0.52 × 4 = 3.14 cm2. So,


1.9 mg/s ÷ 1.19 mg/mm3 ÷ 314 mm2 = 0.005 mm/s × 60 s/min = 0.3 mm/min. Note this is 0.0005 cm/s,


which is equivalent to a stretch rate of 10 s-1, a reasonable 0g level for burning rates for PMMA from
(Ref. 4) as seen in Figure D.7.


Figure D.6.-Burning and Suppression of Solids (BASS) one-sided polymethylmethacrylate
(PMMA) slab burn at slower flow, 1-cm-wide sample.


NASA/TM-20210011385 127




TABLE D.2.-BURN DURATIONS


<table>
 <tr>
  <th>Test</th>
  <th>Start</th>
  <th>End</th>
  <th>Total</th>
 </tr>
 <tr>
  <td>18</td>
  <td>14:45:25</td>
  <td>14:47:05</td>
  <td>00:01:40</td>
 </tr>
 <tr>
  <td>19</td>
  <td>10:37:40</td>
  <td>10:38:30</td>
  <td>00:00:50</td>
 </tr>
 <tr>
  <td>20</td>
  <td>10:55:25</td>
  <td>10:56:40</td>
  <td>00:01:15</td>
 </tr>
 <tr>
  <td>21</td>
  <td>11:17:35</td>
  <td>11:19:05</td>
  <td>00:01:40</td>
 </tr>
</table>


Figure D.7.-Polymethylmethacrylate (PMMA) stagnation point burning
rate data from Reference 4.


NASA/TM-20210011385 128




### Appendix E.-Burning and Suppression Solids (BASS) and BASS-II Papers and Presentations


The following is a list of Burning and Suppression of Solids (BASS) and BASS-II papers and
presentations, going from newest to oldest through summer 2020.


1. Thomsen, Maria, et al.: Buoyancy Effect on Downward Flame Spread Over PMMA Cylinders. Fire Technol., vol. 56, 2020, pp. 247-269.

2. Endo, Makoto, et al.: Flame Growth Around a Spherical Solid Fuel in Low Speed Forced Flow in Microgravity. Fire Technol., vol. 56, 2020, pp. 5-32.

3. Carmignani, L.; and Bhattacharjee, S.: Burn Angle and Its Implications on Flame Spread Rate, Mass Burning Rate, and Fuel Temperature for Downward Flame Spread Over Thin PMMA. Combust. Sci. Technol., vol. 192, no. 8, 2020, pp. 1617-1632.

4. Thomsen, Maria, et al.: Downward Burning of PMMA Cylinders: The Effect of Pressure and Oxygen. Proc. Comb. Inst., vol. 38, no. 3, 2020, pp. 4837-4844.

5. Carmignani, L.; Dong, K.; and Bhattacharjee, S.: Radiation From Flames in a Microgravity Environment: Experimental and Numerical Investigations. Fire Technol., vol. 56, 2020, pp. 33-47.

6. Hossain, Sarzina, et al.: Opposed Flow Flame Spread Over Thermally Thick Solid Fuels: Buoyant Flow Suppression, Stretch Rate Theory, and the Regressive Burning Regime. Combust. Flame, vol. 219, 2020, pp. 57-69.

7. Carmignani, Luca: Opposed-Flow Flame Spread Over Solid Fuels in Different Burning Regimes. Ph.D. Dissertation, Univ. of California San Diego, 2019.

8. Winter, Kelsey Gloria: Experimental Measurements of PMMA Combustion in Simulated Microgravity Along the Normoxic Curve. M.S. Thesis, San Diego State Univ., 2019.

9. Olson, Sandra L., et al.: Flammability Limits From BASS-II Testing in Microgravity Compared to Normal Gravity Limits. ICES-2019-101, 2019.

10. Thomsen, Maria, et al.: Opposed Flow Burning of PMMA Cylinders in Normoxic Atmospheres. Fire Saf. J., vol. 110, no. 102903, 2019.

11. Marcum, Jeremy W.; Ferkul, Paul V.; and Olson, Sandra L.: PMMA Rod Stagnation Region Flame Blowoff Limits at Various Radii, Oxygen Concentrations, and Mixed Stretch Rates. Proc. Comb. Inst., vol. 37, no. 3, 2019, pp. 4001-4008.

12. Olson, Sandra L.; Ferkul, Paul V.; and Marcum, Jeremy W.: High-Speed Video Analysis of Flame Oscillations Along a PMMA Rod After Stagnation Region Blowoff. Proc. Comb. Inst., vol. 37, no. 2, 2019, pp. 1555-1562.

13. Huang, Xinyan, et al.: Transition From Opposed Flame Spread to Fuel Regression and Blow Off: Effect of Flow, Atmosphere, and Microgravity. Proc. Comb. Inst., vol. 37, no. 3, 2019, pp. 4117- 4126. 14. Hernández, N., et al.: Piloted Ignition Delay Times on Optically Thin PMMA Cylinders. Proc. Comb. Inst., vol. 37, no. 3, 2019, pp. 3993-4000.


15. Carmignani, Luca, et al.: Boundary Layer Effect on Opposed-Flow Flame Spread and Flame Length
Over Thin Polymethyl-Methacrylate in Microgravity. Combust. Sci. Technol., vol. 190, no. 3, 2018,
pp. 535-549.
16. Lage, Nicholas Alexander: Two Dimensional Heat Transfer in Non-Thermally Thin Poly(Methyl
Methacrylate) During Combustion in a Narrow Channel Apparatus. M.S. Thesis, San Diego State
Univ., 2018.


NASA/TM-20210011385 129




1. Chan, Ryan Lesley: Effect of Oxygen Concentration on Flame Spread Over Thin Fuels in Different Regimes: A Numerical Investigation. M.S. Thesis, San Diego State Univ., 2018.

2. Link, Shmuel, et al.: The Effect of Gravity on Flame Spread Over PMMA Cylinders. Sci. Rep., vol. 8, no. 120, 2018. 19. Carmignani, L.; Sato, S.; and Bhattacharjee, S.: Flame Spread Over Acrylic Cylinders in Microgravity: Effect of Surface Radiation on Flame Spread and Extinction. ICES-2018-311, 2018.


20. Johnston, Michael C.: Growth and Extinction Limits: Ground Based Testing of Solid Fuel
Combustion in Low Stretch Conditions in Support of Space Flight Experiments. Ph.D. Dissertation,
Case Western Reserve Univ., 2018.
21. Johnston, Michael C.; and T'ien, James S.: Gravimetric Measurement of Solid and Liquid Fuel
Burning Rate Near and at the Low Oxygen Extinction Limit. Fire Saf. J., vol. 91, 2017, pp. 140-146.


1. Marcum, Jeremy; Olson, Sandra; and Ferkul, Paul: Mixed Convection Blowoff Limits as a Function of Oxygen Concentration and Upward Forced Stretch Rate for Burning PMMA Rods of Various Sizes. ICES-2017-370, 2017. 23. Olson, Sandra; and Ferkul, Paul V.: Microgravity Flammability Boundary for PMMA Rods in Axial Stagnation Flow: Experimental Results and Energy Balance Analyses. Combust. Flame, vol. 180, 2017, pp. 217-229. 24. Bhattacharjee, Subrata, et al.: Measurement of Instantaneous Flame Spread Rate Over Solid Fuels Using Image Analysis, Fire Saf. J., vol. 91, 2017, pp. 123-129. 25. Bhattacharjee, Subrata, et al.: Radiative, Thermal, and Kinetic Regimes of Opposed-Flow Flame Spread: A Comparison Between Experiment and Theory, Proc. Comb. Inst., vol. 36, no. 2, 2017, pp. 2963-2969. 26. Zhao, Xiaoyang, et al.: Concurrent Flame Growth, Spread, and Quenching Over Composite Fabric Samples in Low Speed Purely Forced Flow in Microgravity. Proc. Comb. Inst., vol. 36, no. 2, 2017, pp. 2971-2978. 27. Link, Shmuel, et al.: The Effect of Gravity on Flame Spread Over PMMA Cylinders in Opposed Flow With Variable Oxygen Concentration. ICES-2016-79, 2016.


28. Shah, Tirthesh Jayesh: Flame Spread Over Thick Polymethylmethacrylate Samples in a Simulated
and Actual Microgravity Environment. M.S. Thesis, San Diego State Univ., 2016.


29. Pham, Thao; and Miller, Fletcher: A Narrow Channel Apparatus to Study Radiative Heat Loss of
Solid Fuel in Microgravity Combustion. Poster presented at the 32nd Annual Meeting of the
American Society for Gravitational and Space Research (ASGSR), Cleveland, OH, 2016.
30. Endo, Makoto: Numerical Modeling of Flame Spread Over Spherical Solid Fuel Under Low Speed
Flow in Microgravity: Model Development and Comparison to Space Flight Experiments. Ph.D.
Dissertation, Case Western Reserve Univ., 2016.
31. Marcum, Jeremy; Olson, Sandra; and Ferkul, Paul: BASS-II Microgravity Forced Flow Rod Blowoff
Limits Compared to Normal Gravity Mixed Convective Blowoff Limits. Presented at the 32nd
Annual Meeting of the American Society for Gravitational and Space Research (ASGSR), Cleveland,
OH, 2016.
32. Endo, Makoto, et al.: Experimental Data Analysis and Numerical Modeling of Flame Spread on a
PMMA Sphere in Microgravity. Presented at the 32nd Annual Meeting of the American Society for
Gravitational and Space Research (ASGSR), Cleveland, OH, 2016.
33. Carmignani, Luca; and Bhattacharjee, Subrata: Flame Spread Over PMMA Samples and Blow-Off
Extinction for Different Angles. Presented at the 32nd Annual Meeting of the American Society for
Gravitational and Space Research (ASGSR), Cleveland, OH, 2016.


NASA/TM-20210011385 130




1. Miller, Fletcher, et al.: Experimental Measurements and Numerical Modeling of Solid Fuel Combustion in a Narrow Channel Apparatus to Simulate Microgravity. Presented at the 32nd Annual Meeting of the American Society for Gravitational and Space Research (ASGSR), Cleveland, OH, 2016.

2. Miller, Fletcher: Developing the Narrow Channel Apparatus for Material Flammability Tests in Normal Gravity: A Comparison to Data Obtained on ISS. Presented at the ISS R&D Conference, San Diego, CA, 2016.

3. Bhattacharjee, Subrata; Simsek, Aslihan; and Carmignani, Luca: Boundary Layer Effect on Opposed- Flow Flame Spread in the Microgravity Regime. ICES-2016-387, 2016.

4. Link, Scmuel, et al.: The Effect of Gravity on Flame Spread Over PMMA Cylinders in Opposed Flow With Variable Oxygen Concentration. ICES-2016-79, 2016.

5. Marcum, Jeremy W.; Olson, Sandra L.; and Ferkul, Paul V.: Correlation of Normal Gravity Mixed Convection Blowoff Limits With Microgravity Forced Flow Blowoff Limits. Presented at the 2016 Spring Technical Meeting Central States Section of the Combustion Institute, Knoxville, TN, 2016.

6. Chu, Yanyan; and Wichman, Indrek S.: Laminar Opposed Flow Flame Spread Over Degrading Combustible Materials. Presented at the 2016 Spring Technical Meeting Central States Section of the Combustion Institute, Knoxville, TN, 2016.

7. Wichman, Indrek S., et al.: Fire in Microgravity. Am. Sci., vol. 104, no. 1, 2016, pp. 44-51.

8. Bhattacharjee, S., et al.: The Critical Flow Velocity for Radiative Extinction in Opposed-Flow Flame Spread in a Microgravity Environment: A Comparison of Experimental, Computational, and Theoretical Results. Combust. Flame, vol. 163, 2016, pp. 472-477.

9. Bhattacharjee, S., et al.: Opposed-Flow Flame Spread: A Comparison of Microgravity and Normal Gravity Experiments to Establish the Thermal Regime. Fire Saf. J., vol. 79, 2016, pp. 111-118.

10. Olson, S.L.: Concurrent Flow Blowoff Boundary Extrapolation to Zero Stretch: A Proposed New Materials Flammability Test Method. Presented at the FLARE International Workshop, Sapporo Japan, 2016.

11. Shah, Tirthesh J.; Olson, Sandra L.; and Miller Fletcher J.: Modeling and Analysis of Intermediate Thickness PMMA Sheets in Microgravity Opposed Flow. Presented at the 31st ASGSR Annual Meeting, Alexandria, VA, 2015.

12. Olson, Sandra L.; Ferkul, Paul V.: Critical Damkohler Number Flammability Boundary Analysis for PMMA Cylinders Burning in Axial Forced Concurrent Flow. Presented at the 31st ASGSR Annual Meeting, Alexandria, VA, 2015.

13. Link, Shmuel, et al.: Downward Flame Spread Over PMMA Cylinders in Opposed Flow Under 1g and μg Conditions. Presented at the 31st ASGSR Annual Meeting, Alexandria, VA, 2015.

14. Bhattacharjee, Subrata: Opposed-Flow Flame Spread: A Comparison of Microgravity and Normal Gravity Experiments Establishing the Thermal Regime. Presented at the 31st ASGSR Annual Meeting, Alexandria, VA, 2015.

15. Bhattacharjee, Subrata, et al.: Opposed-Flow Flame Spread: A Comparison of Microgravity and Normal Gravity Experiments Establishing the Thermal Regime. Presented at the 31st ASGSR Annual Meeting, Alexandria, VA, 2015.

16. Shah, Tirthesh J., et al.: Modeling and Analysis of Intermediate Thickness PMMA Sheets Burning in Microgravity Opposed Flow. Presented at the Western States Section of the Combustion Institute- Fall 2015 Meeting, paper 134HC-0056, 2015.

17. Bhattacharjee, Subrata, et al.: Temperature and CO2 Fields of a Downward Spreading Flame Over Thin Cellulose: A Comparison of Experimental and Computational Results. Proc. Combust. Inst., vol. 35, no. 3, 2015, pp. 2665-2672.


NASA/TM-20210011385 131




1. Bhattacharjee, Subrata, et al.: Experimental Validation of a Correlation Capturing the Boundary Layer Effect on Spread Rate in the Kinetic Regime of Opposed-Flow Flame Spread. Proc. Combust. Inst., vol. 35, no. 3, 2015, pp. 2631-2638.

2. Olson, Sandra L., et al.: Results From On-Board CSA-CP and CDM Sensor Readings During the Burning and Suppression of Solids-II (BASS-II) Experiment in the Microgravity Science Glovebox (MSG). ICES-2015-196, 2015. 53. Bhattacharjee, S., et al.: The Critical Flow Velocity for Radiative Extinction in Opposed-Flow Flame Spread in a Microgravity Environment: A Comparison of Experimental, Computational, and Theoretical Results. Presented at the 9th Mediterranean Combustion Symposium, Rhodes, Greece, 2015. 54. Olson, Sandra L.; and Ferkul, Paul V.: Microgravity Flammability of PMMA Rods in Concurrent Flow. Presented at the 9th U.S. National Combustion Meeting, Cincinnati, OH, 2015. 55. Zhao, Xiaoyang, et al.: Concurrent Flame Growth, Spread and Extinction Over Composite Fabric Samples in Low Speed Purely Forced Flow in Microgravity. Presented at the 9th U.S. National Combustion Meeting, Cincinnati, OH, 2015. 56. Bornand, Garrett; Shah, Tirthesh; and Miller, Fletcher: Experiments and Modeling of Flame Spread in a Narrow Channel Apparatus and on the International Space Station. Presented at the 9th Southern California Symposium on Flow Physics, San Diego, CA, 2015. 57. Hamdan, Ghaleb; and Miller, Fletcher: Computational Modeling of a Laminar Flow in a 2D Planar Couette Channel at Low Reynolds Numbers. Presented at the 9th Southern California Symposium on Flow Physics, San Diego, CA, 2015. 58. Olson, Sandra: Development of an ISS Experiment to Study Spacecraft Materials Flammability Evaluation Test Methods. Presented at the 30th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR), Pasadena, CA, 2014. 59. Shah, Tirthesh, et al.: Model and Experiments of Burning Intermediate Thickness PMMA Sheets in Microgravity Opposed Flow. Presented at the 30th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR), Pasadena, CA, 2014. 60. Bornand, Garrett, et al.: Using a Narrow Channel Apparatus to Study Thermally-Intermediate Fuel Combustion in a Simulated 0g Environment. Poster presented at the 30th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR), Pasadena, CA, 2014. 61. Endo, M., et al.: Experiment and Modeling of Flame Spread on PMMA Sphere in Low-Speed Forced Flow in Microgravity. Presented at the 30th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR), Pasadena, CA, 2014. 62. Link, S., et al.: Gravitational Effects on Flame Spread Rates for Clear and Black PMMA Cylinders in Opposed Flows. Presented at the 30th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR), Pasadena, CA, 2014. 63. Bornand, Garrett; Sullivan, Greg; and Miller, Fletcher: Polymethylmethacrylate Combustion in a Simulated Microgravity Environment. Poster presented at the 35th International Symposium on Combustion, San Francisco, CA, 2014. 64. Bornand, Garrett; and Miller, Fletcher: Computational Modeling of Polymethylmethacrylate Combustion in a Narrow Channel Apparatus. Poster presented at the 35th International Symposium on Combustion, San Francisco, CA, 2014. 65. Bornand, Garrett R.; Sullivan, Greg J.; and Miller, Fletcher J.: Flame Spread Over Thermally Thick Polymethylmethacrylate in a Narrow Channel Apparatus. Paper 087EF-0034, Western States Section of the Combustion Institute Spring Meeting, Pasadena, CA, 2014.


NASA/TM-20210011385 132




1. Olson, S.L., et al.: Burning and Suppression of Solids-II Fire Safety Investigation for the Microgravity Science Glovebox. Presented at the 29th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR) and the 5th International Symposium on Physical Sciences in Space (ISPS), Orlando, FL, 2013.

2. Takahashi, Fumiaki, et al.: Burning Characteristics of Paraffin and Japan Wax Candle Flames in a Low-Speed Oxidizing Stream in Microgravity. Presented at the 29th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR) and the 5th International Symposium on Physical Sciences in Space (ISPS), Orlando, FL, 2013.

3. Ferkul, Paul V., et al.: Thickness and Fuel Preheating Effects on Material Flammability in Microgravity From the BASS Experiment. Presented at the 29th Annual Meeting of the American Society for Gravitational and Space Research (ASGSR) and the 5th International Symposium on Physical Sciences in Space (ISPS), Orlando, FL, 2013.

4. Bhattacharjee, Subrata, et al.: A Novel Apparatus for Flame Spread Study. Proc. Combust. Inst., vol. 34, no. 2, 2013, pp. 2513-2521.

5. Ferkul, P.V., et al.: Flammability Aspects of Fabric in Opposed and Concurrent Air Flow in Microgravity. Presented at the 8th U.S. National Combustion Meeting, Park City, UT, 2013.

6. Bornand, G.R., et al.: Opposed-Flow Flame Spread in a Narrow Channel Apparatus Over Thin PMMA Sheets. Presented at the 8th U.S. National Combustion Meeting, paper 070FR-0418, 2013.

7. Endo, M., et al.: A Numerical Simulation of Flame Growth and Decay Over a Spherical Solid in Microgravity. Presented at the 2012 Central States Section Spring Technical Meeting of the Combustion Institute, Dayton, OH, 2012.


NASA/TM-20210011385 133








