

# Smoke Aerosol Measurement Experiment (SAME)


## by


David L. Urban1, Gary A. Ruff2 and William Sheredy3,
NASA Glenn Research Center, Cleveland, Ohio 44135
Thomas Cleary4 and Jiann Yang5
National Institute of Standards and Technology, Gaithersburg, Maryland 20899
George Mulholland6
The University of Maryland, College Park, Maryland 20742
and
Zeng-Guang Yuan7
National Center for Space Exploration Research, Cleveland, Ohio 44135


## Final


Report


## November 1, 2000 - April 14, 2009


March 15, 2010


## -----------------------------------------


1 Branch Chief, Combustion and Reacting Systems Branch, 21000 Brookpark Road, MS 77-5,
2 Advanced Capabilities Project Office, 21000 Brookpark Road, MS 77-7,
3 ISS Projects Office, 21000 Brookpark Road, MS 77-5.
4 Engineered Fire Safety Group, 100 Bureau Drive, Stop 8664.
5 Fire Measurements Group Leader, 100 Bureau Drive, Stop 8662.
6 Visiting Professor of Mechanical Engineering, Glenn L. Martin Hall.
7 Staff Scientist, 21000 Brookpark Road, MS 110-3.




ii




### Smoke Aerosol Measurement Experiment (SAME)


## Abstract


Leaks, fires, and spills are some of the most significant hazards that must be accounted for in the
design of the environmental control and life-support system on spacecraft. While prevention is
certainly the first line of defense against a fire, early detection of a overheat event or an actual
fire allows the crew to respond before the hazard gets out of control. The limited options
available for response to a spacecraft fire increase the importance of detecting the fire in an
earlier stage of its development than is typical for terrestrial applications. This report describes
the outcomes of the Smoke Aerosol Measurements Experiment (SAME), an experiment
conducted in the Microgravity Science Glovebox (MSG) on the International Space Station (ISS)
to characterize the size distribution of smoke particulate produced in low-gravity from a variety
of overheated spacecraft materials The absence of gravity can impact not only the formation of
the smoke particulate but also the aging and coagulation processes that occur as the particulate
are transported from their source to a detector.


Based on the results of an earlier flight project carried out in the Glovebox of the Space Shuttle,
(Comparative Soot Diagnostics (CSD)), the soot particles generated and observed in low gravity
environment tend to be larger in size than those in earth conditions. However, the preliminary
results of CSD project were not conclusive because of a minor variation of the temperature of hot
wire which heated the test sample to generate smoke, and also because the CSD apparatus could
not measure the liquid drops existing in the smoke produced by several of the samples.
Furthermore, the CSD project was not designed to provide on-orbit measurement of the particle
size distribution. The Smoke Aerosol Measurement Experiment was designed to obtain this data
that could then be used to design the next-generation smoke detectors for space exploration
missions. Unfortunately, because of the relatively small volume of the MSG, it cannot
accommodate the instruments normally used in a ground-based laboratory to measure the size
distribution of smoke particulate. Therefore, a new procedure was developed, the moment
method, from which the characteristics of the particle size distribution can be inferred using a
minimum number of portable instrument.


The SAME experiments were conducted during Expedition 15 on the ISS. Four materials,
typical of those found in spacecraft, were tested including cellulose (lamp wick), Kapton,
silicone rubber, and Teflon. A fifth material, dibutyl-phthalate (DBP) retained in a cotton wick
was used as a reference. In order to simulate the detection of a pre-fire overheated-material event,
samples were heated to temperatures below the ignition point. The smoke generation conditions
were controlled to provide repeatable sample surface temperatures and air flow conditions. The
transport time from the smoke source to the detector was simulated by holding the smoke in an
aging chamber for times ranging from 10 seconds to 1800 seconds. Smoke particle samples
were collected on Transmission Electron Microscope (TEM) grids for post-flight analysis. The
smoke properties were measured using particulate aerosol diagnostics that measure different
moments of the size distribution. These statistics were combined to determine the geometric
mean particle sizes and geometric standard deviation, which is sufficient to describe the entire
smoke distribution if a lognormal distribution is assumed. For comparison, smoke detectors from


iii




the ISS and the space shuttle were also included in the SAME apparatus. The experimental
results show that, for the materials tested, a substantial portion of the smoke particles are below
500 nm in diameter. The smoke transport model demonstrated that mixing dominates the smoke
transport and that consequently detection time lags are longer than in normal gravity. The
knowledge gained from SAME can be used to establish design requirements for smoke detectors
used in future spacecraft.


iv




### Acknowledgments


The authors wish to gratefully acknowledge the contributions and support of the SAME experiment
team and the crews of ISS increments 10, 13, and 15. The SAME project was funded through the
Advanced Capabilities Division of the Exploration Systems Mission Directorate and specifically by the
ISS Research and the Fire Prevention Detection and Suppression Projects of the Exploration Technology
Development Program.


Certain commercial entities, equipment, or materials may be identified in this document in order to
describe an experimental procedure or concept adequately. Such identification is neither intended to
imply recommendation or endorsement by the National Aeronautics and Space Administration or the
National Institute of Standards and Technology, nor intended to imply that the entities, materials, or
equipment are necessarily the best available for the purpose.


v




vi




Table of Contents


Abstract..........................................................................................iii
Acknowledgments...............................................................................v
Table of Contents..............................................................................vii
List of Tables...................................................................................viii
List of Figures..................................................................................viii
Nomenclature....................................................................................ix
Acronyms.........................................................................................ix


1. Introduction.................................................................................1

2. Smoke Background........................................................................1

3. SAME Experiment.........................................................................4 A. The Moment Method....................................................................4 A.1. Principle of the Moment Method.................................................4 A.2. Implementation of the Moment Method in SAME Experiment.............8 A.3. Uncertainty Analysis...............................................................8 B. Instrumentation...........................................................................9 C. Instrument Calibration.................................................................12

4. Flight Tests................................................................................14

5. Test Results and Discussion.............................................................15

6. Closing Remarks..........................................................................19


References........................................................................................20
Publication List..................................................................................21


Appendix A. Log of SAME Flight Tests..................................................A-1


Appendix B. (2009 ICES Paper)............................................................B-1


Appendix C. (2009 AIAA Paper)..........................................................C-1


Appendix D. (2008 ICES Paper)...........................................................D-1


Appendix E. (2008 AIAA Paper)..........................................................E-1


vii




List of Tables


Table 1. Results of SAME flight tests


List of figures


Figure 1. Brunswick Defense smoke detector used in the NASA orbiter fleet.


Figure 2. Allied Signal/Honeywell light-scattering smoke detector used in the ISS.


Figure 3. Diameters for a log-normal distribution with Dg = 1.0 m and g = 1.6.


Figure 4. Schematic of the SAME hardware.


Figure 5. Photograph of a sample carousel.


Figure 6. Thermal Precipitator Module.


Figure 7. P-trak Calibration results with Mono disperse DOP droplets.


Figure 8. Ion Chamber Calibration results with Mono disperse DOP droplets.


Figure 9. DustTrak results with Mono disperse DOP droplets.


Figure 10. SAME Experiment installed in the ISS MSG Facility.


Figure 11. Instrument traces for a typical silicone rubber run.


Figure 12. Instrument traces for a typical Teflon run.


Figure 13. Instrument traces for a typical smoke aging run for silicone rubber.


Figure 14. TEM images for Lamp wick (test point 32) and Teflon (test point 26).


viii




Nomenclature


<table>
 <tr>
  <th>d</th>
  <th>--</th>
  <th>Count mean diameter or arithmetic mean diameter</th>
 </tr>
 <tr>
  <td>d</td>
  <td>--</td>
  <td>Diameter of average mass</td>
 </tr>
 <tr>
  <td></td>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <td>D</td>
  <td>--</td>
  <td>Diameter of particles</td>
 </tr>
 <tr>
  <td>Dg</td>
  <td>--</td>
  <td>Geometry mean diameter</td>
 </tr>
 <tr>
  <td>Dp</td>
  <td>--</td>
  <td>A type of characteristic diameter depending on the value of p</td>
 </tr>
 <tr>
  <td>fN(D)</td>
  <td>--</td>
  <td>Frequency of particle count distribution function (zeroth moment distribution function)</td>
 </tr>
 <tr>
  <td>fi(D)</td>
  <td>--</td>
  <td>Frequency of the i-th moment distribution function</td>
 </tr>
 <tr>
  <td>Fi(D)</td>
  <td>--</td>
  <td>Cumulative i-th moment distribution function</td>
 </tr>
 <tr>
  <td>L</td>
  <td>--</td>
  <td>Letter for length dimension</td>
 </tr>
 <tr>
  <td>Mi</td>
  <td>--</td>
  <td>The i-th moment</td>
 </tr>
 <tr>
  <td>N(D)</td>
  <td>--</td>
  <td>Number of particles per unit volume with diameters equal or less than D</td>
 </tr>
 <tr>
  <td>Nt</td>
  <td>--</td>
  <td>Total number of particles per unit volume</td>
 </tr>
 <tr>
  <td>u(x)</td>
  <td>--</td>
  <td>Absolute uncertainty of variable x, with the same unit as variable x</td>
 </tr>
 <tr>
  <td>ur(x)</td>
  <td>--</td>
  <td>Relative uncertainty of variable x, dimensionless. ur(x) = u(x)/x</td>
 </tr>
 <tr>
  <td>g</td>
  <td>--</td>
  <td>Geometric standard deviation of a lognormal distribution</td>
 </tr>
</table>


Acronyms


CMD: Count Mean Diameter


CSD: Comparative Soot Diagnostics Experiment
DACU: Data Acquisition and Control Unit
DAFT: Dust Aerosol measurement Feasibility Test, a precursor project of SAME
GMD: Geometric Mean Diameter
GSD: Geometric Standard Deviation
ISS: International Space Station
MSG: Microgravity Science Glovebox
SAME: Smoke Aerosol Measurement Experiment
STS: Space Transportation System
TEM: Transmission Electron Microscope


ix




x




### 1. Introduction


Appropriate design of fire detection systems requires knowledge of both the expected signature of the
events to be detected and the background levels of the measured parameters. Terrestrial fire detection
systems have been developed based on extensive study of terrestrial fires.1, 2 Unfortunately, there is no
corresponding data set for spacecraft fires and consequently current spacecraft fire detectors were
developed based upon experience on normal gravity fire behavior and properties. This approach was
necessary given the absence of data concerning microgravity smoke particulate. However planned
spacecraft and their planned missions outside of low earth-orbit will require increased reliability of fire
detection systems in addition to robust false alarm resistance. Extended lunar-surface missions will
require systems that are not influenced by lunar dust and other nuisance dust sources.


The absence of buoyant flow increases the residence time in microgravity fires causing substantial
changes in flame structure. Given the large changes in fire behavior seen in reduced gravity, it is
reasonable to expect that the signatures and detection requirements of these fires will change. There are
a number of factors that can be expected to affect the particle size distribution of the smoke from
spacecraft fires. The absence of buoyant flow in low-gravity increases the residence time in
microgravity fires and increases the transit time from the reaction zone to the detector.3 The materials
used in spacecraft are different from those typically used in terrestrial applications where smoke
properties were previously evaluated. More importantly, the limited options available to respond to a
spacecraft fire increase the importance of detecting the fire in an earlier stage of its development than is
typical for terrestrial applications. All of these effects can be expected to change the smoke particle size
distribution. The objective of this work was to make sufficient measurements of smoke from spacecraft
fires to enable improved design of future detectors.


## 2. Smoke Background


Smoke is a general term that encompasses aerosol materials produced by a number of processes. In
particular for non-flaming combustion, the aerosol includes recondensed original material or pyrolysis
products that can be either liquid or solid. For flaming combustion, the aerosol includes soot particulate,
condensed water vapor, and ash particles. Soot particles dominate the smoke particulate in established
flaming fires while unburned pyrolysis products and recondensed polymer fragments are produced by
smoldering and pyrolysis in the early stage of fire growth. Given the constrained space on any
spacecraft, the target for the fire detection system is necessarily the early phase and not established
flaming fires; consequently, the primary target for detection is the pyrolysis products and not the soot.


The background regarding fire detection in US spacecraft is summarized in this paper but is discussed in
more detail in papers by Friedman and Urban4, 5 In the Mercury, Gemini and Apollo missions, the crew
quarters were limited and mission durations were short, consequently it was considered reasonable that
the astronauts would rapidly detect any fire. The Skylab module, however, included approximately 30
UV-sensing fire detectors.4 These devices were limited to line-of-sight and were reported to have
difficulties with false alarms.


Details of the ISS and STS detector requirements are described by Steisslinger et al.6 A brief overview
of the requirements is given below.


1




Space Shuttle Detectors:
At the time the Space Shuttle Orbiter (Space Transportation System (STS)) was developed, smoke
detection for terrestrial applications was becoming commonplace.1 In particular, ionization detectors
were readily available but photoelectric
(scattering or obscuration detectors) were
generally unavailable due to the difficulty of
producing stable light sources. There were
no data available concerning the smoke or
dust particle size distribution in low-gravity
and the database for normal-gravity smoke
characteristics was a fraction of what is
available today. Consequently, the STS
smoke detector (Fig. 1) employed a variant
of the accepted ground-based approach
(ionization detectors). The Orbiter has nine
particle-ionization smoke detectors in
avionics cooling air return lines in the mid-
deck and flight deck and the SpaceLab had
six additional particle-ionization smoke
detectors in the avionics lines.7 While the Figure 1. Brunswick Defense™ smoke detector used in the
design rationale is not completely known, NASA orbiter fleet. The inlet is on the right and the gas is
expelled out the small plate on the top.
Celesco™ (later Brunswick Defense™)
based their design on data that suggested
incipient fires could be discriminated by looking for particulate in the 0.4 μm to 0.7 μm range.8 The use
of a pump provided the opportunity to use a particle separator that rejected particulate larger than 1μm.
This air pump increased the power requirements and reduced the operational life of the detector. The
STS detector as built was designed to alarm at a particle loading of 2 mg/m3 for 5 seconds (based on 1
micron particles) or a 0.022 mg/m3/s rise in concentration for 20 seconds9.


ISS Detectors:
The International Space Station (ISS) smoke detector design took advantage of the availability of stable
laser-diode light sources, mirroring a trend in terrestrial detectors toward light scattering devices. This
provided the opportunity to produce a detector that required substantially less power, (1.5 Watts versus 9
Watts for the orbiter detector)6 and, with no moving parts, was quieter with a much longer operational
life. The choice was supported by data indicating that early smoldering fires produce larger particulate
than established flaming fires.1 The ISS detectors (Fig. 2) are laser-diode, forward-scattering, smoke or
particulate detectors. The sensitivity extends down to 0.3 μm but is greatest for particles larger than 1
μm. The current requirements for the ISS call for two detectors in the open area of the module, and
detectors in racks that have cooling air-flow.10


The design developed for the ISS by Allied Signal™ (Fig. 2) consists of a 2-pass laser diode to sense
forward scattered light (30 degrees). There is also a light transmission sensor to monitor the beam
intensity. The system is designed to alarm based on the magnitude of the scattered light signal
referenced to the beam intensity. The system is less sensitive to particles smaller than the wavelength of
the laser (near IR) than it is to larger particles. The minimum reported sensitivity is 0.3 μm.6 The ISS
detector was designed to alarm at 1% obscuration per foot using an Underwriters Laboratory (UL)


2




smoke box and white light extinction. This
was implemented using a transfer standard
detector and a 0.5 m polystyrene-bead
aerosol system that was used to set the
amplifiers on each unit. The transfer
standard was calibrated in the smoke box
and then used to set the levels with the
aerosol system.


As a result of these design decisions, the ISS
and the Orbiter detectors have particle
sensitivities that do not overlap. In both
cases the designs were based upon the best
available data at the time. However, due to
the complete absence of low-g data
concerning the nature of particulate and
radiant emission from incipient and fully
developed low-g fires, different conclusions
were drawn concerning the optimal design
for spacecraft fire detection.


Figure 2. Allied Signal/Honeywell light-scattering smoke
detector used in the ISS. The near IR laser beam emerges from
the enclosure into the top assembly (A) and is reflected by two
mirrors (one visible at top right (B)) and is then reflected back to
the sensors in the enclosure (C). One sensor detects the forward
scattered light and is referenced by another sensor that looks
directly at the incident beam.


As described by Friedman4 there have been
six overheat and failed component failures in
the NASA Orbiter fleet in addition to several
similar incidents that have occurred on the
ISS. None of these events spread into a real fire but as mission durations increase, the likelihood of
failures increases. The experience on Mir in 1997 has shown that failure of oxygen generation systems
can have significant consequences. As a result, improved understanding of spacecraft fire detection is
critically needed.11


Previous work on smoke particles from low-gravity sources by Urban et al.5 indicated that the
particulate produced by low-gravity flames (soot or unburned fuel particles) tends to have larger size
particles than in normal gravity. Results from the CSD (Comparative Soot Diagnostics) Experiment5
which studied smoke properties in low-gravity from several spacecraft materials suggested that liquid
smoke particles could achieve sizes larger than 1 µm while solid particulate remained in the sub-
micrometer range. However, the CSD experiment did not produce sufficient data concerning the size of
the liquid smoke particles to guide detector design. The combined impact of these limited results and
physical expectations is that, based on the increased smoke residence time in low gravity, direct
knowledge of low-g combustion particulate is needed for the confident design of smoke detectors for
spacecraft rather than extrapolation from 1-g data


Any effort to detect fires must be able to discriminate against the ambient background and nuisance
signals. In the case of smoke detection, the background dust aerosol conditions must be considered. The
only spacecraft background aerosol particulate measurements to date were made on the Orbiter on STS-
32 in 199012 and on the ISS.5


3




The STS measurements included the results from two cascade impactors and a light scattering device.
The two impactors reported a bimodal particle size distribution with ~ 40% of the particles in each of the


2.5 μm to 10 μm and >100 μm ranges. The other two ranges <2.5 μm and 10 μm to 100 μm were very
lightly populated. Each impactor sampled approximately 15 m3 of air over approximately 30 hours.


These results showed substantially higher concentrations than typical indoor measurements (over a
factor of 5 for the two most populated size ranges). These data were supported by the light scattering
instrument which made 17 measurements in 12 locations, all of these reported mass concentrations
ranging from 50 μg/m3 to 70 μg/m3. The ISS results of Urban et al.5 were obtained from a feasibility
experiment to validate the operation of an aerosol particle counter in low-gravity (DAFT). The
measurements were made in the US Lab on Increment 10 and the particle count levels were at the noise
level for the instrument (less than 5 particles/cm3). The low particle levels in the < 2.5 μm bin for the
STS and the low overall numbers for the ISS suggest a zone of opportunity for spacecraft fire detection
since typical normal gravity fires produce substantial particulate in this size range5,2 However more
complete particle size statistics are needed.


## 3. SAME Experiment


To address the limited data from the CSD experiment concerning the likely size of spacecraft smoke
particulate, the Smoke Aerosol Measurement Experiment (SAME) was developed. The SAME
experiment sought to avoid the problems experienced by the CSD experiment by obtaining the
particulate size statistics on-orbit with a reduced dependence upon sample return to Earth. This is a
challenging endeavor because existing aerosol instrumentation is typically too large to be compatible
with spacecraft experiment constraints. Thus, to obtain particulate size statistics with existing aerosol
instrumentation would require the return of numerous samples to Earth. As will be described below, an
alternative approach was employed that used three discrete instruments to measure separate moments of
the size distribution. When combined, these moments provide useful aggregate statistics of the size
distribution if a lognormal distribution is assumed. The measurements were made using smoke
generated by overheated spacecraft materials in much the same manner as the CSD experiment however
the sample temperature, flow field, and particle aging time were more rigorously controlled.


A. The Moment Method


The approach used by the SAME experiment is termed the 'moment method' for convenience.13 This
approach consists of measuring three moments of the size distribution (the zeroth, first and third moment)
on orbit, using several small, light-weight instruments. By applying the properties of the lognormal
distribution to the measured moments, the total number concentration, Nt, the geometric mean diameter,
Dg, and the geometric standard deviation, g, of the aerosol can be estimated. Once these three
parameters are known, the size distribution of the measured aerosol is uniquely defined, assuming that
the distribution is lognormal. In what follows, we will explain how the moment method works.


A.1. Principle of the moment method


The number (or count) distribution of an aerosol describes the number of particles that fall into a certain
size range in a unit volume of aerosol. The number distribution is sometimes also called size distribution.
Mathematically, a distribution function can be expressed in four different, but related, forms. First, a
distribution function can be expressed as a frequency (or density) distribution function or a cumulative
distribution function. Then, each of the two can be expressed in terms of its normalized form or non-


4




normalized form. The normalized forms of any distribution function are much like the probability
functions in statistics. To avoid future confusion, we will define these distribution functions first.


The particle number distribution function of an aerosol, fN(D), is defined as follows:


(1) fN (D)  ,


dN
dD


where dN is the number of particles per unit volume having diameters between D and D + dD. Here, the
subscript N in fN(D) denotes particle numbers. The function fN(D) is a non-normalized frequency
distribution function with a dimension of [L-4]. The corresponding cumulative distribution function,
F(D), is defined as a definite integral of fN(D) as follows:


F D f ( )d


(1-a) ( ) 
0 D N


As the upper limit D of the integral in Eq. (1-a) approaches infinity, F(D) approaches the total number of
particles in a unit volume, denoted by Nt. Thus, F(D) is a non-normalized cumulative distribution
function, with a dimension of [L-3]. When fN(D) or F(D) is normalized by Nt, one gets its normalized
counterpart. Note that Nt has a dimension of [L-3], thus the normalized cumulative distribution function
is always dimensionless whereas the normalized frequency distribution function has a dimension of [L-1].
In this report, unless otherwise stated, we will use non-normalized distribution functions, either in their
frequency forms or in their cumulative forms.


Based on fN(D), distribution functions of various properties of a given aerosol can be defined. For
instance, the distribution functions of particle diameter, fD(D), surface area, fA(D), and particle volume,
fV(D) (or mass distribution function, fm(D) if the particle material density is constant) are defined in the
following manner.


(2)


(2a)


(2b)


(2c)


f D  f
( )
D





1 ( D)


D


2


f ( D) 


( D) 


3


 DfN ( D)


dN
D2 fN
dD
dN 
D3 
dD 6


 dN
D3 
6 dD 6


dN
dD


f ( D)  f ( D) D2


( D)


A



6 3

f
6


f ( D) 
V


D3 fN ( D)


-  D3 fN ( D)

-  6


f ( D) 
m


It can be seen that to address various aerosol property distributions, it is convenient to define a moment
distribution function fi(D) as follows.


(2d)


fi ( D)  Di fN ( D) i  0, 1, 2, ...


When i = 0, f0(D) and the number (or count) distribution function, fN(D) are identical. Because equation
(2d) is similar to the calculation of moment in mechanics, fi(D) is conventionally called the i-th moment


5




distribution function of the aerosol. Note that each fi(D) is a frequency distribution function. The
corresponding cumulative distribution function, Fi(D), is as follows.


(2e)


-  0D

- i f


F ( D)
i


N


( )d i  0, 1, 2, ....


When the upper limit of the above integral approaches infinity, the integral of (2e) returns a single value,
which is called the i-th moment of the distribution function fN(D), denoted by Mi. That is


(2f)  ( )  ( ) , i  0, 1, 2, ...
M F 0 i
i i fN  d
The dimensions of fi(D) are [Li-4] and those of Fi(D) and Mi are [Li-3]. Note that for the sake of
generalization, we do not set a limit on the number of moments now, although the highest moment used
in SAME is the third moment.


If fN(D) is an arbitrary function, all its moments are independent of each other making it impossible to
reconstruct fN(D) from a finite number of its moments. However, if fN(D) is a function that can be
uniquely defined by a finite number of parameters, only that same number of its moments are
independent and they can be arbitrarily selected. From any set of independent moments, one can solve
for the parameters that define the distribution function, fN(D). Thus, this type of distribution function,
fN(D), can always be constructed if the independent moments are known. This is the underlying idea of
the moment method.


The lognormal distribution function below is widely accepted for describing the size distribution of
aerosols14, 15.


(3) 


f D
N
( )


 D D 2
ln ln
g


##  


- 

-  ,

- 


N
t
2D ln










2 ln 2


exp


g


g


where Nt is the total number of particles in a unit volume, or total number concentration of the aerosol,
and parameters Dg and g are the geometric mean diameter and geometric standard deviation,
respectively, defined by





1


(4) ln D   ln fn dD
g Nt 0


and


-  1 

1.  ln ln ln     D D g N 1 g  t 0


2
 
f D dD
N



0.5


The lognormal distribution is related to the well known normal (or Gaussian) distribution function in
that lnD is used as the independent variable in the Gaussian distribution, including dN/d(lnD) that
defines fN(D), because the particle diameter D can never take negative values.


6




The SAME project assumes a lognormal distribution function for the aerosol size distribution. Since a
lognormal distribution function is uniquely defined by three parameters, Nt, Dg and g, only three
moments are needed to reconstruct the distribution function. In SAME, these three moments are chosen
to be the zeroth moment, the first moment and the third moment. Based on Eq. (2f), the zeroth moment,
M0 is simply equal to Nt, whereas the first moment, M1, can be thought of as the "diameter concentration"
or integrated diameter per unit volume. The third moment, M3, is proportional, but not equal, to the total
volume or mass of the particles per unit volume of the aerosol. From these three moments, two
characteristic diameters are defined. They are a) the count (arithmetic) mean diameter, which is equal to
M1/M0 and denoted by D0.5 or d and b) the diameter of average mass16, which is equal to (M3/M0)1/3 and
d . The subscripts of 0.5 and 1.5 used for these two diameters follow an existing
denoted by D1.5 or m
naming convention.


There is a unique feature of the lognormal distribution, which is described by the Hatch-Choate
conversion equations17. The diameters for various moment distributions are related to the geometric
mean diameter, Dg, and the geometric standard deviation, g, via the following equation.14, 15


1. p g  g 


D  D exp p ln2


In equation (6), p is a parameter defining the meaning of diameter Dp. For instance, when p = 0.5, Dp is
the count mean diameter, whereas when p = 1.5, Dp is the diameter of average mass. This feature of the
lognormal distribution greatly simplifies the application of the moment method in finding the aerosol
size distribution. Figure 3 shows a typical lognormal distribution along with various characteristic
diameters, where Dg=1.0m and g= 1.6. Differing from Eq. (3), the y-axis in Fig. 3 is normalized by
Nt, i.e., fN(D)/Nt. In this distribution, the corresponding values of the count mean diameter, D0.5, and the
diameter of average mass, D1.5, can be computed from equation (6). They are 1.117 m and 1.393 m,
respectively.


Figure 3: Diameters for a log-normal distribution with Dg=1.0 m and g= 1.6.


7




1. D  0.5 g


D3
D


and


1.5


In the case of the SAME experiment, our objective is to obtain Dg, g, and Nt based on measured
moments, M0, M1 and M3 with D0.5 and D1.5 being intermediate parameters. For this purpose, equation (6)
is rearranged to provide the following explicit expressions for Dg and g.


  exp ln D  ln D  exp ln D D


(8) g  1.5 0.5    1.5 / 0.5 


Thus, once the three moments, M0, M1 and M3, are obtained, we can compute D0.5 and D1.5. Using
equations (7) and (8), we can get the corresponding values for Dg and g. When Dg, g and Nt (i.e., M0)
are known, a lognormal distribution function, fN(D) can be uniquely defined for the measured aerosol.
Validation of this approach is discussed in Cleary, Weinert and Mulholland.13 This moment method
provides a strong basis for the design of the SAME experiment.


A.2. Implementation of the moment method in SAME experiment


In the SAME experiment, the zeroth moment, M0, was measured using a condensation nuclei counter
called the P-TrakTM (TSI Inc.). The first moment, M1, was approximately proportional to the output
signal of an ionization detector, which was a modified ionization chamber taken from a commercially-
available smoke detector. The third moment, M3, was inferred from the light scattered by the smoke
aerosol when illuminated by a red laser. For particles in the size range of 0.2 μm to 2.0 μm, , the light
scattering signal at 90 degrees from a red laser is approximately proportional to the third moment. The
instrument used to obtain the third moment is called a DustTrakTM (TSI Inc.). Calibration measurements
were made for the DustTrak to account for the departure of the scattering signal from the 3rd moment.
More detailed information of instruments and their operations can be found in the Instruments section
below. The instruments used in SAME were compact enough to be installed in the ISS MSG.


Extensive calibrations of these instruments were performed at NIST to ensure that correct values of each
moment were obtained from the instrument output signals. The results of these calibrations showed that
the instrument signals correlate well with corresponding moments except for the third moment. The
third moment was found to be a function of the DustTrak output and the particle diameters. This led to
an iterative procedure to find the best-fit results of Dg and g.


A.3. Uncertainty Analysis


Inevitably there are uncertainties in the measured moments. It is interesting to know the contribution of
the uncertainty of each moment to the uncertainties of Dg and g. To do so, we need to express Dg and
g in terms of the three moments. By substituting D0.5 and D1.5 by M0, M1 and M3 in equations (7) and
(8), we have


(9)
and


D M 4/3 M1.5M 1/6
g 0 1 3


8




-  M2 / 3M 1/ 3  

-  0 3  

-  M  

-  1  

- 

- 

- 

- 

1.   exp ln g


The law of propagation of uncertainty18 for the case of independent variables (i.e., there is no
covariance) states


n  f 


u2 y 


(11) c ( )  
x
i 1  i 


u2 x
i ,


2


where u(xi) is the uncertainty of independent variable xi, n is the number of independent variables, and
uc(y) is the combined uncertainty of dependent variable y = f(xi). Uncertainties can be expressed in terms
of an absolute value of the variable or, in a relative sense, the ratio of the uncertainty to the value of the
variable. Since relative uncertainties are easier to use, we will discuss relative uncertainties in the
following text. A subscript r will be added to the letter u to indicate relative uncertainties. Then Eq.(11)
can be rewritten as


n x f 


i
rc ( )   r
y x
i 1  i 


u2 x
i 


2


u2 y 


(11a)


In our case, y is either Dg or g and xi (i = 1, 2, 3) are M0, M1 and M3, respectively. Substituting Eqs. (9)
and (10) into Eq. (11a), we obtain the relative combined uncertainties of Dg and g as follows.


2 16 2 2 1
u D  u M  2 25u M  u2 M
 0 . 1  r 3 
rc g 9 r r 36


(12)


and
1


u2   u2 M  2 25 u2 M 0 25 u2 M


(13) 2  0  . r 1 . r 3 
rc g 9 ln r

g
Equations (12) and (13) show the relative uncertainties of Dg and g as functions relative uncertainties of
M0, M1 and M3. It is interesting that both equations (12) and (13) show the uncertainty of M3 contributes


the least to the combined uncertainties of Dg and g, whereas that of M1 contributes the most.


B. Instrumentation


The moment measurements were made using an assembly of three separate instruments. Two are
industrial hygiene instruments manufactured by TSI and one is a modified residential smoke detector.


The zeroth-moment instrument is a condensation nuclei counter, the P-Trak™ (TSI Inc.). This device
operates by passing the aerosol-laden air stream through a region saturated with isopropanol vapor and
then into a cooler region where the vapor condenses onto the particles increasing their diameter such that
they can be readily counted by a light scattering device. This instrument is very robust and operates
over a range of 0 to 105 particles/cm3 and 20 nm to 1 μm diameter. Some dilution is required since the
smoke concentration in SAME ranges from about 0.5 × 106 to 5 × 106 particles/cm3. There was also a
concern that the isopropanol condensate would not return to the wick in low-gravity.5 To mitigate this


9




issue, the condensing section of the device was modified with very small grooves to improve
conductance of the condensate back to the wick. These changes were tested in a separate space
experiment with good results indicating the modified device could be used successfully in low gravity.5


The first-moment instrument is the ionization chamber taken from a residential smoke detector. This
device uses an alpha-particle emitter to generate ions in a region within a DC electric field. Normally,
the ions drift toward an electrode inside the ionization chamber producing a current. When particulate
are present, the ions attach themselves to the particles thereby charging the particles. Because the
charged particles have a much smaller mobility than ions alone, the current is reduced. The required
particle concentrations are on the order of 105 particles/cm3, thus no sample dilution was required.


The third-moment instrument is a light scattering device, the DustTrak™ (TSI Inc.). The device uses a
90 degree light scattering signal to quantify the aerosol mass density. For terrestrial dust particulate, this
signal correlates well with the mass concentration, however additional compensation was needed to
account for the range of particle sizes observed in the SAME experiment. The device operating range is
from 0.001 mg/m3 to 100 mg /m3. These devices are equipped with an aerodynamic impactor at the inlet
which captures particles larger than the selected size. The SAME experiment included 2 DustTraks™,
one with a 1 μm impactor and the other with a 10 μm impactor. The difference in the signal from the
two devices provided a measure of the fraction of the particulate that was larger than 1 μm. In some
cases dilution was required owing to the high smoke concentration levels.


A schematic of the assembled hardware appears in Fig. 4. The system was installed in the Microgravity
Science Glovebox, an ISS facility that provides many resources including: containment, power, data,
video and uplink commanding. Smoke was generated by resistively heating small samples of spacecraft
materials. Sample heating was achieved by heating a steel wire that was wrapped around an
approximately 3 mm diameter cylinder of the sample material. The steel wire was resistively heated and


Figure 4. Schematic of the SAME hardware.


10




the wire resistance was monitored to control its
temperature. This technique was found to
produce repeatable weight loss from sample to
sample in laboratory tests. Groups of six pre-
weighed samples were installed in carousels (Fig.


5) that the crew installed in the SAME hardware.


For each test, a new sample was moved into place
by rotating one of the six sample chambers in the
carousel into the flow duct and the sample
heating and the flow were synchronized to
provide a steady air stream over the sample
during the heating interval. The system was
designed to provide air flow rates ranging from 2
to 8 cm/s.


To emulate a variety of fire scenarios, tests were
conducted at different sample temperatures, air
flow rates, and smoke aging durations. The Figure 5. Photograph of a sample carousel. Carousel
sample heating time is approximately 60 seconds. contains an assortment of Teflon, Kapton, lamp wick, and
During this interval, controlled flow was induced silicone rubber. The samples were supported and heated
by the same stainless steel wire coil.
by a moving piston in the aging chamber which
drew the smoke into the chamber. The smoke was held in the chamber for a pre-determined time,
allowing the particles to coagulate. After a specified aging time, the smoke was then pushed by the
piston into the diagnostics duct where the moment instruments made their measurements. Also installed
in the diagnostics duct were space shuttle and ISS smoke detectors. Their output signals were used to
compare with the results of the moment method.
As the aging chamber was filled and as the aerosol was pushed out to the moment instruments, a small
aerosol stream was drawn off to the thermal precipitator, (Fig. 6). Inside the precipitator, the aerosol
passes between a Transmission Electron Microscope (TEM) grid and a heated wire. Thermophoretic


## Heated Wire


## Air Flow


## TEM Grid


11


Figure 6. Thermal Precipitator Module. Left image is a photograph of a partially disassembled Thermal Precipitator
Module with the inlet manifold exposed on the left, the hot wire leads in the red Vespel block in the middle and the
outlet valves on the right. The drawing on the right displays the position of the hot wire above the TEM grid with
the air flow passing over both. The heated wire drives aerosol particles onto the grid via thermophoresis.




forces moved particles to the grid surface where they adhered. After the mission the grids were removed
from the assembly and examined in a TEM to obtain an independent determination of the particle size
and morphology.


C. Instrument Calibration


Calibration of these instruments was essential to properly interpret the flight data and was performed on
the ground before the flight. Calibration was accomplished using two different aerosol generators; one
generates mono-disperse particle using dioctyl phthalate (DOP) according to the approach by
Mulholland and Liu19 and the other uses polystyrene spheres. The monodisperse droplet generator
functioned by producing a spray of DOP diluted with isopropanol which is then evaporated and
recondensed producing monodisperse droplets. The droplet size is controlled by the DOP dilution level.
The generator will operate stably for tens of minutes. The aerosol from the generator was sampled
simultaneously by the SAME instrument under test and a reference instrument. For the number count,
the reference instrument was a TSI 3022 particle counter, for the mass concentration of the aerosol, a
Tapered Element Oscillating Microbalance and for the first moment a TSI Electrical Aerosol Detector
was used. The results for the P-Trak are shown in Fig. 7. As the number concentration increases, the
effect of the particle diameter becomes more evident. Separate correlations were developed for each
particle size and the closest correlation was used to analyze the flight data based on the initial estimates
of the average particle size.


600000


500000


400000


300000


200000


100000


100 nm
600 nm
1200 nm


0


0 50000 100000 150000 200000 250000 300000 350000
Ptrak output (number count/cc)


Figure 7. P-trak Calibration results with monodisperse DOP droplets.


The
first moment device, the ion chamber, showed very little effect of particle size, as seen in Fig 8.
Consequently a single correlation was used for all particle sizes. The third moment device (TSI-
DustTrak®) is theoretically predicted to show non-monotonic behavior as particle size is increased.


12




<table>
 <tr>
  <th>500</th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>350</th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td>100 nm<br/>150 nm<br/>300 nm</td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td>600 nm<br/>750 nm</td>
 </tr>
 <tr>
  <th>150</th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>Figure 8. Ion</th>
  <td>5 5 5 . 6<br/>Ionization Chamber output (volts)<br/>Calibration results with monodisperse DOP droplets.</td>
  <td></td>
 </tr>
</table>


While a satisfactory prediction of the DustTrak® response was obtained using liquid droplets of dioctyl
phthalate, (Fig. 9) the uncertainty associated with the Mie scattering calculations due to the particle
refractive index estimate, the potential of agglomerated particles, and deviation from assumed log-


180


160


140


120


100


80


60


40


20


0


0


50


100


150
DustTrak output (mg/m3)


Figure 9. DustTrak results with monodisperse DOP droplets.


200


250


100 nm
150 nm
300 nm
600 nm
750 nm
1200 nm


300


13




normal size distribution must be assessed further for the smoke samples here. In the results reported
here, the DustTrak® response was directly calibrated, for each smoke source, against mass
concentration measurements using a tapered element oscillating microbalance. This approach is valid as
long as the size distribution of the sample does not change significantly. Using estimated material
densities, the diameter of average mass was computed for each sample. Equation 8 was used to compute
the geometric standard deviation from the arithmetic mean diameter and the diameter of average mass,
and Equation 7 was used to compute the GMD.


## 4. Flight Tests


The SAME hardware installed in the ISS MSG is shown in Fig 10. The SAME tests were performed on
board ISS in September and early October of 2007. Overall 30 sample materials were tested. These
were comprised of six samples each of 5 materials: Teflon™, Kapton™, silicone rubber, cellulose, and
dibutyl-phthalate deposited on a porous wick. These samples were tested at different airflow rates,
pyrolysis temperatures, and smoke aging durations.


Figure 10. SAME Experiment installed in the ISS MSG Facility.


Realizing that crew time was the most precious ISS resource, SAME was designed to be operated both
autonomously and from the ground to the greatest extent possible. The SAME hardware was organized
into a number of smaller modular units to facilitate stowage for launch, provide for easy change out,
increase the reliability and reduce risk. The downside of this strategy was that the assembly of the
experiment involved many connections and required approximately 5 hours of crew time. Once installed,
however, SAME was easily and effectively operated from the Tele Science Center (TSC) at the Glenn
Research Center (GRC), and this capability enabled the ground team to achieve roughly a 50% greater
number of test points (and data) than was originally planned.


The on orbit operations were scheduled around the availability of the crew for installing the next Sample
Carousel and Thermal Precipitator (and removing and stowing the used ones). Typically, the crew would
install the next units during the morning, and operations would be scheduled for later that day. SAME
would be nominally scheduled by the ISS staff for two test points on each of the following days.


14




Because the allowed operations windows were sufficiently large, the ground team was frequently able to
perform four test points in the allowed time.


The staffing level of the ground team varied between two and five members from the engineering team
with additional support from up to three members of the Science team. Most of the time, there would be
one person operating the linked computer that controlled the experiment, one providing verbal
communication to the ISS cadre and doing data reduction and a third recording video and performing
other miscellaneous functions.


Uplink parameter sheets were generated by the Science team and most times, emailed to the engineering
team the day before operations, although when additional unplanned test points were performed during a
session, the Science team provided a hard copy of the parameters during the interim between test points.
These sheets were printed and checked, and in most cases, signed. The parameters were entered into the
ground computer by a team member and then the entry was checked both by means of a checksum and
by the other member on consol before uplinking them to the DACU.


The test points were scheduled by the ground team to coincide with Ku and S band coverage so that
video of the heating and the measurement data could be obtained Near Real Time (NRT) and recorded
on the ground. Because the data reduction software was already in place, processing of the data could be
done immediately after the test point had been completed, and in all cases, before the next test point was
performed. Periodically during the overall operations, downloads from the DACU were commanded as a
backup to the NRT data to insure that the most complete compilation was available.


Detailed chronological record of the SAME flight tests can be found in Appendix A.


## 5. Test Results and Discussions


The analog signals from various instruments were digitized at 1 Hz by an 8 bit A/D converter. Figure 11
contains the signal traces from a typical run for silicone rubber. The difference in the signals for the two
DustTrak's indicates that a substantial portion of the aerosol mass is in particles that are larger than 1
μm.


For comparison, Fig. 12 contains similar data for a Teflon run where little difference is evident between
the two DustTrak instruments, indicating that the bulk of the aerosol mass is in particles below 1 μm.
Figure 13 shows that the effect of is a substantial decrease in the number concentration (Ptrak) while the
mass concentrations (DustTraks) remain relatively steady. This behavior is consistent with particle
coagulation with limited wall loss. It is also interesting to compare the response of the ISS and STS
detectors for silicone rubber and Teflon. In figure 11, both the ISS detector and the STS detectors show
strong signals. (Note that the presence of smoke yields a positive deflection of the ISS signal and a
negative deflection on the STS signal). This is reasonable because the silicone rubber smoke has a larger
diameter of average mass in Table 1. In figure 12, the STS detector provided a strong signal, whereas
the signal from the ISS detector was more erratic, because the Teflon smoke is comprised primarily of
particles having diameters less than 1 m, as mentioned above. This shows that the smoke detectors
used in STS and ISS have different response to particle size range.


Results from the moment instruments for baseline runs (no aging) and 720 second aging runs are
summarized in Table 1.


15




7


6


5


4


3


2


1


## Silicone Run 24 GMT 267


ISSDetectorScatterMeasurement(Volts)


STSDetectorMeasurement(Volts)


IonDetectorBMeasurement(Volts) 80
PTrakMeasurement(PtPerCC)/1000 (right)
DustTrakAMeasurement(MgPerM3) (right) 70
DustTrakBMeasurement(MgPerM3) (right)


60


50


40


30


20


10


0


75


125


175


225


275


325


0
375


Figure 11. Instrument traces for a typical silicone rubber run. Base levels are at the beginning and end of the trace. The
actual sampling interval is between 125 and 160 seconds. The differences in the rise times of each instrument are due to the
smoke transit time to the instrument. The large difference between DustTrak A and DustTrak B is indicative of the
substantial portion of the particle distribution that is larger than 1μm (the cutoff for the impactor on DustTrak A).


7


6


5


4


## Teflon Test 25 GMT 268


ISSDetectorScatterMeasurement(Volts)
STSDetectorMeasurement(Volts)
IonDetectorBMeasurement(Volts)
PTrakMeasurement(PtPerCC/1000) (right)
DustTrakAMeasurement(MgPerM3) (right)
DustTrakBMeasurement(MgPerM3) (right)


80


70


60


50


40


3


2


1


30


20


10


0


0
73975


74025


74075


74125
Time (Seconds)


74175


74225


-10


74275


Figure 12. Instrument traces for a typical Teflon run. Base levels are at the beginning and end of the trace. The
actual sampling interval is between 74025 and 74060 seconds. The small difference between DustTrak A and
DustTrak B is indicative that the most of the particle distribution is smaller than 1μm (the cutoff for the impactor on
DustTrak A).


16




ISSDetectorScatterMeasurement(Volts)
IonDetectorBMeasurement(Volts)
PTrakMeasurement(PtPerCC)/1000 (right scale)
DustTrakAMeasurement(MgPerM3) (right scale)
DustTrakBMeasurement(MgPerM3) (right scale)


## GMT 267 Silicone Run 23


8


130


7


110


6


90


5


70


4


50


3


30


2


10


1


0
5100


-10


6500


6300


6100


5700


5900


5500


5300


## Time (sec)


Figure 13. Instrument traces for a typical smoke aging run for silicone rubber. Base levels are at the beginning and
end of the trace. The first sampling interval is between 5200 and 5250 seconds and the post aging sampling interval
is between 6000 and 6050 seconds. Consistent with particle coagulation with limited wall loss, the overall number
count (Ptrak) decreases substantially while the mass concentrations (DustTraks) remain relatively steady.


Table 1. Results of SAME flight tests
Geom.Mean Diam. Arithmetic Mean Diam.


<table>
 <tr>
  <th></th>
  <th>(nm)</th>
  <th>(nm)</th>
  <th>(nm)</th>
  <th>σg</th>
 </tr>
 <tr>
  <td>Kapton</td>
  <td>80</td>
  <td>105</td>
  <td>179</td>
  <td>2.08</td>
 </tr>
 <tr>
  <td>Kapton aged</td>
  <td>155</td>
  <td>186</td>
  <td>267</td>
  <td>1.82</td>
 </tr>
 <tr>
  <td>Lamp wick</td>
  <td>186</td>
  <td>227</td>
  <td>341</td>
  <td>1.89</td>
 </tr>
 <tr>
  <td>Lamp wick aged</td>
  <td>258</td>
  <td>308</td>
  <td>438</td>
  <td>1.81</td>
 </tr>
 <tr>
  <td>Silicone</td>
  <td>189</td>
  <td>257</td>
  <td>472</td>
  <td>2.18</td>
 </tr>
 <tr>
  <td>Silicone aged</td>
  <td>352</td>
  <td>422</td>
  <td>606</td>
  <td>1.83</td>
 </tr>
 <tr>
  <td>Teflon</td>
  <td>170</td>
  <td>205</td>
  <td>297</td>
  <td>1.84</td>
 </tr>
 <tr>
  <td>Teflon aged</td>
  <td>228</td>
  <td>273</td>
  <td>392</td>
  <td>1.82</td>
 </tr>
</table>


## Diam. of Average Mass


The Teflon and Kapton particles are very small with Teflon showing limited increase in the size from
the diameter of average mass compared to the arithmetic mean diameter. The lamp wick results exhibit
substantially larger diameter of average mass. As reported previously,12 the DustTrak results for lamp
wick and silicone demonstrated substantial portions of the particle distribution possessed particle
diameters larger than 1 m. The small diameters for the Kapton and Teflon will make detection of this
smoke challenging for light scattering devices, on the other hand the large sizes seen with the lamp wick
and silicone would generate very large signals on a light scattering system, suggesting that detection of
these particles against the background environment will require a detection system capable of measuring
more than one moment of the particle size distribution. The aging results show substantial increase in
the average particle sizes with them rising to over 1 m for the aged silicone diameter of average mass.
Since the aging can be considered to be representative of smoke emerging from a closed volume (e.g. an


17




avionics enclosure), fire sensors must consider large particles in addition to the smaller particles seen
with Kapton.


In general, since the mass increases with the cube of the diameter, the larger particles do not affect the
count mean diameter (CMD) as much as they affect the light scattering signal which scales with the
particle mass. Consequently, although the CMD for silicone rubber is 189 nm, almost half the particle
mass is larger than 1 m, as evidenced by the ratio of the DustTrak instruments. The lamp wick shows
similar behavior.


On the other hand, the Kapton and Teflon show substantially narrower particle size distributions with
little mass in particles larger than 1m. These low populations of larger particles are consistent with the
less effective detection by light scattering devices which was seen for some of the Teflon tests and with
the signals obtained from the STS and ISS detectors. All of the tests conducted in this series of
experiments show strong signals on the Space Shuttle detector (ionization) despite the larger particle
size distributions seen for the lamp wick (cellulose) and silicone rubber. The CSD experiment5 reported
poor detection by the Space Shuttle detector for non-flaming overheat of cellulose and silicone rubber
(indicating larger particle sizes). The reduced signal on the Space Shuttle detector for CSD suggests that
under some reasonable pre-fire conditions the smoke size distribution can extend to diameters beyond
those seen in the SAME experiment.


The TEM grids recovered from the thermal precipitators were unfortunately contaminated with
extraneous particles whose origin was believed to be somewhere in the assembly of the thermal
precipitators. Despite the contamination, the lamp wick and Teflon samples produced distinct particles
consistent with ground based experience. Typical particles are shown in Fig. 14.


Figure 14: Test point 32 lamp wick


Test point 26, Teflon


18




Several conference papers were prepared during the analysis of the data obtained from SAME and are
included in the appendices. These provide additional details on several intermediate steps in the data
analysis process that led to the final results described in this report.


## 6. Closing Remarks


The SAME project successfully implemented the moment method described in this report, under the
volume constraints of the ISS MSG, to determine the size distribution of the smokes generated from 5
tested materials in well controlled conditions of heating temperature, heating time and air flow rate. In
combination with the knowledge gained from previous CSD experiment, it becomes obvious that the
detection of smoke across the size range seen in SAME and CSD, while still discriminating against dust
(which tends to be large), will probably require a detection system that can discriminate the particle size
distribution to at least a limited degree. Two possible effective means of achieving this size
discrimination are to employ a detector that measures more than one moment of the size distribution or
to use a detector that can classify the particles into size ranges.


19




### References


1. Bukowski, R.W. and G.W. Mulholland, "Smoke Detector Design and Smoke Properties," NBS Technical Note 973, 1978.

2. Bukowski, R. W, R. D. Peacock, J. D. Averill, T. G. Cleary, N. P. Bryner, W. D. Walton, P. A. Reneke, and E. D. Kuligowski, "Performance of Home Smoke Alarms, Analysis of the Response of Several Available Technologies in Residential Fire Settings," NIST Technical Note 1455, December 2003. 3. Brooker, J. E., Urban, D.L., Ruff, G.A., "ISS Destiny Laboratory Smoke Detection Model", 07ICES-113, 2007 International Conference on Environmental Systems, Chicago, Ill. July 2007. 4. Friedman, R., "Fire Safety Practices and Needs in Human-Crew Spacecraft," Journal of Applied Fire Science, Vol. 2, 1992, pp. 243-259. 5. Urban, D.L., Griffin D., Ruff, G.A., Cleary, T., Yang, J., Mulholland, G., Yuan, Z.G., "Detection of Smoke from Microgravity Fires", 2005 International Conference on Environmental Systems, Rome Italy, Paper # 2005-01-2930 July 2005, SAE Transactions, pp 375-384. 6. Steisslinger, H. R., D. M. Hoy, J. A. McLin and E. C. Thomas., "Comparison Testing of the Space Shuttle Orbiter and Space Station Freedom Smoke Detectors," SAE Paper 932291, 1993. 7. Martin, C.E. and R.C. DaLee, "Spacecraft Fire Detection and Suppression (FDS) Systems: An Overview and Recommendations for Future Flights," SAE Technical Paper 932166, 23rd International Conference on Environmental Systems, Colorado Springs, CO, July 12-15, 1993. 8. National Research Council, Fire Detection for Life Safety, National Academy of Sciences, Washington D.C., 1975. 9. Steisslinger, H.R., Hoy, D.M., McLin, J.A, and Thomas, E.C., "Comparison Testing of the Space Shuttle Orbiter and Space Station Freedom Smoke Detectors." SAE Technical Paper 932291, July 12-15, 1993. 10. McKinnie, J., "Fire Response Aboard the International Space Station," SAE Technical Paper 972334, 27th International Conference on Environmental Systems, Lake Tahoe, NV, July 14-17, 1997. 11. Ruff, G.A., D.L. Urban, and M.K. King, "A Research Plan for Fire Prevention Detection and Suppression," AIAA-2005-0341, 43rd Aerospace Sciences Meeting and Exhibit, Reno, NV, January 9-12, 2005. 12. Liu, B. Y. H., K. L. Rubow, P. H. McMurry, T. J. Kotz and D. Russo, "Airborne Particulate Matter and Spacecraft Internal Environments," SAE Technical Paper 911476, 21st International Conference on Environmental Systems, San Francisco, CA , July 15-18, 1991 13. Cleary, T.G., D W. Weinert, and G.W. Mulholland, "Moment Method for Obtaining Particle Size Measures of Test Smokes", Natl. Inst. Stand. Technol., NISTIR 7050, 2003. 14. Raabe, O.G., J. Aerosol Sci., Vol. 2, 1971, p. 289. 15. Reist, P.C., Introduction to Aerosol Science, Macmillan Pub. Co., NY, NY, 1984. 16. Hinds, W.C., "Aerosol Technology," Wiley-Interscience, John Wiley & Sons, Inc. 2nd ed. 1999, p.83. 17. Hinds, William C., "Aerosol Technology," Wiley-Interscience, John Wiley & Sons, Inc. 2nd ed. 1999, pp. 97-100.


18. Taylor, B.N. and Kuyatt, C.E., "Guidelines for Evaluating and Expressing the Uncertainty of NIST
Measurement Results", NIST Technical Note 1297, 1994 Edition.
19. Mulholland, G.W. and Liu, B.Y.H., 1980. Response of Smoke Detectors to Monodisperse Aerosols,
J. Research of the National Bureau of Standards, 85:223-238.


20




Publication and Presentation List


1. Smoke Particle Sizes in Low-Gravity and Implications for the Design of Spacecraft Smoke
Detectors, David Urban, Gary A. Ruff, George Mulholland, Thomas Cleary, Jiann Yang, Zeng-
Guang Yuan, Victoria Bryg, 2009 International Conference on Environmental Systems,
Savannah, GA, July 2009, 2009-01-2468.
2. Properties of Smoke from overheated Spacecraft Materials in Low-Gravity, David L. Urban ,
Gary A. Ruff, Thomas Cleary, Jiann Yang, George Mulholland, Zeng-Guang Yuan, William
Sheredy, 47th Aerospace Sciences Meeting, Orlando, Fl. Paper AIAA-2009-956 (Jan, 2009).
3. Measurement of Smoke Particle Size under Low-Gravity Conditions, David L. Urban, Gary
Ruff, George Mulholland, Thomas Cleary, Jiann Yang, Zengguang Yuan, 2008 SAE ICES,
08ICES-2089
4. Spacecraft Fire Detection: Smoke Properties and Transport in Low-Gravity, David L. Urban ,
Gary A. Ruff, John E. Brooker , Thomas Cleary, Jiann Yang, George Mulholland, and Zeng-
Guang Yuan 46th Aerospace Sciences Meeting, Reno, NV Paper AIAA-2008-0806 (Jan 7-10,
2008).
5. Detection of Smoke from Microgravity Fires, George W. Mulholland, David Urban, Gary Ruff,
Bill Sheredy, Greg Funk, Jiann Yang, Thomas Cleary, Presentation at TSI Inc., August 20,
2007.
6. Particle and Smoke Detection on ISS for Next Generation Smoke Detectors David Urban, Gary
Ruff, William Sheredy, Greg Funk, International Space Development Conference 2007 Dallas,
TX May 25, 2007
7. Moment Method for Estimating Micro-gravity Smoke Particle Size Parameters, Thomas Cleary,
Claudia Rexfort, George Mulholland, David Urban, Jiann Yang, and Zeng-Guang Yuan, AAAR
meeting Sept 10, 2006 St Paul Minn.
8. Detection of Smoke from Microgravity Fires, David L. Urban, DeVon Griffin, Gary A. Ruff,
Thomas G. Cleary, Jiann Yang, George W. Mulholland, and Zeng-Guang Yuan
2005 International Conference on Environmental Systems, Rome Italy, Paper # 2005-01-2930
July 2005, SAE Transactions, pp 375-384.
9. Cleary, T.G., D W. Weinert, and G.W. Mulholland, "Moment Method for Obtaining Particle
Size Measures of Test Smokes", Natl. Inst. Stand. Technol., NISTIR 7050, 2003.
10. David L. Urban, George W. Mulholland, Jiann Yang, Thomas G. Cleary, and Zeng-Guang Yuan,
"Smoke": Characterization Of Smoke Particulate For Spacecraft Fire Detection, Seventh
International Microgravity Combustion Workshop, Cleveland, NASA CP-2003-212376, pp 269-
272, (June 2003)
11. David L. Urban, George W. Mulholland, Jiann Yang, Thomas G. Cleary, and Zeng-Guang Yuan,
"Smoke": Characterization of Smoke Particulate for Spacecraft Fire Detection, Sixth
International Microgravity Combustion Workshop, Cleveland, NASA CP-2001-210826, pp. 401-
404 (2001)


21




22




Appendix A


Log of SAME flight tests


<table>
 <tr>
  <th>Test<br/>Number</th>
  <th>GMT</th>
  <th>Sample<br/>Type</th>
  <th>Reheat/Initial</th>
  <th>Carousel</th>
  <th>Number<br/>(Position)</th>
  <th>Record Time</th>
  <th>Comments</th>
 </tr>
 <tr>
  <td>1</td>
  <td>252</td>
  <td>Silicone</td>
  <td>Initial</td>
  <td>1</td>
  <td>1</td>
  <td>11:50 - 13:20</td>
  <td></td>
 </tr>
 <tr>
  <td>2</td>
  <td>254</td>
  <td>DBP</td>
  <td>Initial</td>
  <td>1</td>
  <td>5</td>
  <td>5:50 - 7:01</td>
  <td></td>
 </tr>
 <tr>
  <td>3</td>
  <td>254</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>1</td>
  <td>5</td>
  <td>4:48 - 6:10</td>
  <td></td>
 </tr>
 <tr>
  <td>4</td>
  <td>255</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>1</td>
  <td>5</td>
  <td>37:42 - 38:51</td>
  <td></td>
 </tr>
 <tr>
  <td>5</td>
  <td>255</td>
  <td>Silicone</td>
  <td>Initial</td>
  <td>1</td>
  <td>6</td>
  <td>39:99 - 41:15</td>
  <td></td>
 </tr>
 <tr>
  <td>6</td>
  <td>256</td>
  <td>Teflon</td>
  <td>Initial</td>
  <td>1</td>
  <td>2</td>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <td>7</td>
  <td>256</td>
  <td></td>
  <td>Initial</td>
  <td>1</td>
  <td>3</td>
  <td>18:54 - 20.25</td>
  <td></td>
 </tr>
 <tr>
  <td>8</td>
  <td>257</td>
  <td>Kapton</td>
  <td>Initial</td>
  <td>1</td>
  <td>4</td>
  <td>1:13 - 1:46</td>
  <td>run abort because of high Rt/Ro, finished<br/>manually</td>
 </tr>
 <tr>
  <td>9</td>
  <td>257</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>1</td>
  <td>5</td>
  <td>1:13 - 2:50</td>
  <td></td>
 </tr>
 <tr>
  <td></td>
  <td>257</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td>3:40 -3:50</td>
  <td>engage carousel</td>
 </tr>
 <tr>
  <td>10</td>
  <td>257</td>
  <td>Teflon</td>
  <td>Reheat</td>
  <td>1</td>
  <td>2</td>
  <td>6:35 - 8:17</td>
  <td></td>
 </tr>
 <tr>
  <td></td>
  <td>257</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td>8:30 - 8:39</td>
  <td>carousel</td>
 </tr>
 <tr>
  <td>11</td>
  <td>262</td>
  <td>DBP</td>
  <td>Initial</td>
  <td>2</td>
  <td>4</td>
  <td>1:39 - 3:07</td>
  <td></td>
 </tr>
 <tr>
  <td>12</td>
  <td>262</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>2</td>
  <td>4</td>
  <td>5:37 - 7:05</td>
  <td></td>
 </tr>
 <tr>
  <td>13</td>
  <td>262</td>
  <td>Teflon</td>
  <td>Initial</td>
  <td>2</td>
  <td>1</td>
  <td>9:36 - 10:59</td>
  <td></td>
 </tr>
 <tr>
  <td>14</td>
  <td>263</td>
  <td></td>
  <td>Initial</td>
  <td>2</td>
  <td>3</td>
  <td>33:05 - 34:18</td>
  <td></td>
 </tr>
 <tr>
  <td>15</td>
  <td>263</td>
  <td>DBP</td>
  <td>Initial</td>
  <td>2</td>
  <td>5</td>
  <td>38:29 - 40:03</td>
  <td></td>
 </tr>
 <tr>
  <td>16</td>
  <td>263</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>2</td>
  <td>4</td>
  <td>35:42 - 36:48</td>
  <td></td>
 </tr>
 <tr>
  <td>17</td>
  <td>264</td>
  <td>Lampwick</td>
  <td>Initial</td>
  <td>2</td>
  <td>2</td>
  <td>14:05 - 15: 50</td>
  <td></td>
 </tr>
 <tr>
  <td></td>
  <td>264</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td>16:31 - 17:30</td>
  <td>rotate carousel</td>
 </tr>
 <tr>
  <td>18</td>
  <td>264</td>
  <td>DBP</td>
  <td>Initial</td>
  <td>2</td>
  <td>6</td>
  <td>&lt;6.:39</td>
  <td></td>
 </tr>
 <tr>
  <td>19</td>
  <td>264</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>2</td>
  <td>6</td>
  <td>6:39 - 8:00</td>
  <td></td>
 </tr>
 <tr>
  <td>20</td>
  <td>264</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>2</td>
  <td>6</td>
  <td>8:00 - 11:00</td>
  <td></td>
 </tr>
 <tr>
  <td>21</td>
  <td>264</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>2</td>
  <td>6</td>
  <td>19:32 - 21:10</td>
  <td></td>
 </tr>
 <tr>
  <td>22</td>
  <td>264</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>2</td>
  <td>6</td>
  <td>22:30 - 24:16</td>
  <td></td>
 </tr>
 <tr>
  <td>23</td>
  <td>267</td>
  <td>Silicone</td>
  <td>Initial</td>
  <td>3</td>
  <td>1</td>
  <td>12:28 - 13:48</td>
  <td></td>
 </tr>
 <tr>
  <td>24</td>
  <td>267</td>
  <td>Silicone</td>
  <td>Initial</td>
  <td>3</td>
  <td>2</td>
  <td>17:40 - 19:10</td>
  <td></td>
 </tr>
 <tr>
  <td>25</td>
  <td>268</td>
  <td>Teflon</td>
  <td>Initial</td>
  <td>3</td>
  <td>4</td>
  <td>17:58 - 19:12</td>
  <td></td>
 </tr>
 <tr>
  <td>26</td>
  <td>268</td>
  <td>Teflon</td>
  <td>Initial</td>
  <td>3</td>
  <td>5</td>
  <td>20:33 - 21:58</td>
  <td></td>
 </tr>
 <tr>
  <td>27</td>
  <td>269</td>
  <td>Silicone</td>
  <td>Initial</td>
  <td>3</td>
  <td>3</td>
  <td>1:48 - 3:09</td>
  <td></td>
 </tr>
 <tr>
  <td>28</td>
  <td>269</td>
  <td>Teflon</td>
  <td>Initial</td>
  <td>3</td>
  <td>6</td>
  <td>4:35 - 5:36</td>
  <td></td>
 </tr>
 <tr>
  <td>29</td>
  <td>271</td>
  <td>Kapton</td>
  <td>Initial</td>
  <td>4</td>
  <td>4</td>
  <td>1:22 - 2:23</td>
  <td></td>
 </tr>
 <tr>
  <td>30</td>
  <td>272</td>
  <td></td>
  <td>Initial</td>
  <td>4</td>
  <td>5</td>
  <td>1:00 - 2.30</td>
  <td></td>
 </tr>
 <tr>
  <td>31</td>
  <td>272</td>
  <td></td>
  <td>Initial</td>
  <td>4</td>
  <td>1</td>
  <td>2:50 - 4:20</td>
  <td></td>
 </tr>
 <tr>
  <td>32</td>
  <td>272</td>
  <td></td>
  <td>Initial</td>
  <td>4</td>
  <td>2</td>
  <td>8:35 - 9:57</td>
  <td></td>
 </tr>
 <tr>
  <td>33</td>
  <td>273</td>
  <td></td>
  <td>Initial</td>
  <td>4</td>
  <td>6</td>
  <td>9:58 - 10:59</td>
  <td>missed first of 2 cm/s</td>
 </tr>
 <tr>
  <td>34</td>
  <td>273</td>
  <td></td>
  <td>Initial</td>
  <td>4</td>
  <td>3</td>
  <td>14:38 - 15:48</td>
  <td>2 cm/s</td>
 </tr>
 <tr>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td>16: 18 - 16:27</td>
  <td>carousel</td>
 </tr>
 <tr>
  <td>35</td>
  <td>276</td>
  <td>Silicone</td>
  <td>Initial</td>
  <td>5</td>
  <td>1</td>
  <td>10:10 - 11:05</td>
  <td></td>
 </tr>
 <tr>
  <td>36</td>
  <td>276</td>
  <td>DBP</td>
  <td>Initial</td>
  <td>5</td>
  <td>6</td>
  <td>12:08 - 13:32</td>
  <td></td>
 </tr>
 <tr>
  <td>37</td>
  <td>276</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>5</td>
  <td>6</td>
  <td>14:46 - 15:45</td>
  <td>8 cm/s</td>
 </tr>
 <tr>
  <td>38</td>
  <td>276</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>5</td>
  <td>6</td>
  <td>18:46 - 20:18</td>
  <td></td>
 </tr>
 <tr>
  <td>39</td>
  <td>276</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>5</td>
  <td>6</td>
  <td>20:25 -21:55</td>
  <td></td>
 </tr>
 <tr>
  <td>40</td>
  <td>276</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>5</td>
  <td>6</td>
  <td>22:58 - 23:58</td>
  <td></td>
 </tr>
 <tr>
  <td>41</td>
  <td>277</td>
  <td>Teflon</td>
  <td>Initial</td>
  <td>5</td>
  <td>2</td>
  <td>3:57 - 5:15</td>
  <td></td>
 </tr>
 <tr>
  <td>42</td>
  <td>277</td>
  <td>DBP</td>
  <td>Initial</td>
  <td>5</td>
  <td>5</td>
  <td>00:53 - 2.21</td>
  <td></td>
 </tr>
 <tr>
  <td>43</td>
  <td>277</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>5</td>
  <td>5</td>
  <td>6:19 - 7:55</td>
  <td></td>
 </tr>
 <tr>
  <td>44</td>
  <td>277</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>5</td>
  <td>5</td>
  <td>8:05 - 9:42</td>
  <td>30 minute 75 second</td>
 </tr>
 <tr>
  <td>45</td>
  <td>278</td>
  <td>DBP</td>
  <td>Reheat</td>
  <td>5</td>
  <td>5</td>
  <td>10:58 - 12:17</td>
  <td></td>
 </tr>
 <tr>
  <td>46</td>
  <td>278</td>
  <td>Lampwick</td>
  <td>Initial</td>
  <td>5</td>
  <td>3</td>
  <td>13:34 - 14:29</td>
  <td></td>
 </tr>
 <tr>
  <td>47</td>
  <td>278</td>
  <td>Kapton</td>
  <td>Intiial</td>
  <td>5</td>
  <td>4</td>
  <td>15: 59 - 17:06</td>
  <td></td>
 </tr>
</table>


1. -1




1. -2




Appendix B


2009-01-2468


Smoke Particle Sizes in Low-Gravity and Implications for Spacecraft Smoke
Detector Design


Copyright © 2009 SAE International


## David L. Urban, Gary A. Ruff


NASA Glenn Research Center


## George W. Mulholland


University of Maryland


## Thomas G. Cleary, Jiann C. Yang


National Institute of Standards and Technology


## Zengguang Yuan, Victoria Bryg


National Center for Space Exploration Research


## ABSTRACT


This paper presents results from a smoke detection
experiment entitled Smoke Aerosol Measurement
Experiment (SAME) which was conducted in the
Microgravity Science Glovebox on the International
Space Station (ISS) during Expedition 15. Five different
materials representative of those found in spacecraft
were pyrolyzed at temperatures below the ignition point
with conditions controlled to provide repeatable sample
surface temperatures and air flow conditions. The
sample materials were Teflon®, Kapton®, cellulose,
silicone rubber and dibutylphthalate. The transport time
from the smoke source to the detector was simulated by
holding the smoke in an aging chamber for times
ranging from 10 to1800 seconds. Smoke particle
samples were collected on Transmission Electron
Microscope (TEM) grids for post-flight analysis. The
smoke particle size distributions were measured using
three particulate aerosol diagnostics that measure
different moments of the size distribution and smoke
detectors from the ISS and the space shuttle. These
diagnostics were used to estimate the particle number
concentration (zeroth moment), the diameter
concentration (first moment) and the mass concentration
(third moment). These values were combined to


<table>
 <tr>
  <th>The Engineering Meetings Board<br/>session organizer. This process</th>
  <td>has approved this paper for publication. It has successfully completed SAE's peer review process under the supervision of the<br/>a minimum of three (3) reviews by industry experts.</td>
 </tr>
 <tr>
  <th>mechanical, photocopying,<br/>ISSN 0148-7191</th>
  <td>or otherwise, without the prior written permission of SAE.</td>
 </tr>
 <tr>
  <th>Positions and opinions advanced</th>
  <td>in this paper are those of the author(s) and not necessarily those of SAE. The author is solely responsible for the content of</td>
 </tr>
 <tr>
  <th>the paper.</th>
  <td></td>
 </tr>
 <tr>
  <th>SAE Customer Service: Tel:</th>
  <td>877-606-7323 USA and</td>
 </tr>
 <tr>
  <th>Tel:</th>
  <td>724-776-4970</td>
 </tr>
 <tr>
  <th>Fax:</th>
  <td>724-776-0790</td>
 </tr>
 <tr>
  <th>Email:</th>
  <td>CustomerService@sae.org</td>
 </tr>
 <tr>
  <th></th>
  <td></td>
 </tr>
 <tr>
  <th>Printed in USA</th>
  <td></td>
 </tr>
</table>


estimate the diameter of average mass, the count mean
diameter, the geometric mean diameter and the
geometric standard deviation. Even though the analysis
of these data is ongoing, information from the various
instruments and the calculated mean particle sizes has
important implications for the design of spacecraft
smoke detectors. These implications are reviewed in this
paper relative to the operating principles of existing
smoke detection technology. These results can be used
to establish design requirements for smoke detectors for
future spacecraft.


## INTRODUCTION


Design of fire detector systems requires understanding
of the background conditions and the expected range of
events to be detected. Detectors for terrestrial fires
were developed using the results of extensive study of
terrestrial fires.1,2 Unfortunately, there is no
corresponding data set for spacecraft fires and
consequently current spacecraft fire detectors were
developed based upon experience from terrestrial
systems. Given the large changes in fire behavior seen
in reduced gravity, it is reasonable to expect that the
smoke characteristics and detection requirements of
these fires will change. The absence of buoyant flow in




low-gravity increases the residence time in microgravity
fires and increases the transit time from the reaction
zone to the detector.3 The materials used in spacecraft
are different from typical terrestrial applications where
smoke properties were previously evaluated. Very
significantly, the limited options available to respond to a
spacecraft fire increase the importance of detecting the
fire in an earlier stage of its development than is typical
for terrestrial applications. All of these effects can be
expected to change the detection requirements: both the
smoke concentration sensitivity, and the expected
smoke particle size distribution. The objective of this
work was to make sufficient measurements of smoke
from spacecraft fires to enable improved design of future
detectors.


## SMOKE BACKGROUND


Smoke is a general term that encompasses aerosol
materials produced by a number of processes. In
particular it can include unburned, recondensed, original
polymer or pyrolysis products that can be liquid, solid,
carbonaceous soot, condensed water vapor, or ash
particles. Soot particles dominate the smoke particulate
in established flaming fires while unburned pyrolysis
products and recondensed polymer fragments are
produced by smoldering and pyrolysis in the early stage
of fire growth. Given the constrained space on any
spacecraft, the target for the fire detection system is
necessarily the early phase and not established flaming
fires; consequently, the primary target for detection is
the pyrolysis products and not the soot.


Prior spacecraft systems are summarized in more detail
in papers by Friedman and Urban.4,5 In the Mercury,
Gemini and Apollo missions, the crew quarters were
limited and mission durations were short. Consequently
it was considered reasonable that the astronauts would
rapidly detect any fire. The Skylab module, however,
included approximately 30 UV-sensing fire detectors.4
These devices were limited to line-of-sight and were
reported to have difficulties with false alarms. The
Space Shuttle (Space Transportation System (STS))
detectors were based upon ionization fire detector
technology, the most advanced technology available at
the time and used an inertial separator designed to
eliminate particles larger than 1-2 micrometers. The
International Space Station (ISS) smoke detectors use
near-IR forward scattering, rendering them most
sensitive to particles larger than a micrometer, outside of
the range of sensitivity of the shuttle detector.


More details of the ISS and STS detector requirements
are presented by Steisslinger et al. 6
however the basic
details are summarized below. The STS detector, as
built, was designed to alarm at 2 mg/m3 (based on 1
micrometer particles) or 0.022 mg/m3/s rise in
concentration for 20 seconds. The ISS detector was
designed to alarm at obscuration of 1% per foot using an
Underwriters Laboratory (UL) smoke box and a white


light extinction meter. This was implemented using a
transfer standard detector and a 0.5 micrometer
polystyrene latex-bead aerosol system that was used to
set the amplifiers on each unit. The transfer standard
was calibrated in the smoke box and then used to set
the levels with the aerosol system.


As described by Friedman4 there have been six
overheat and failed component failures in the NASA
Orbiter fleet in addition to several similar incidents that
have occurred on the ISS. None of these events spread
into a real fire but as mission durations increase, the
likelihood of failures increases. The experience on Mir in
1997 has shown that failure of oxygen generation
systems can have significant consequences. As a result,
improved understanding of spacecraft fire detection is
critically needed.7


Previous work on smoke particles from low-gravity
sources by Urban et al.5 found that the particulate
produced by low-gravity flames (soot or unburned fuel
particles) tends to have larger size particles than in
normal gravity. Results from the CSD (Comparative
Soot Diagnostics) Experiment5 which studied smoke
properties in low-gravity from several spacecraft
materials suggested that liquid smoke particles could
achieve sizes larger than 1 µm while solid particulate
remained in the sub-micrometer range. However, the
CSD experiment did not produce sufficient data
concerning the size of the liquid smoke particles to guide
detector design. The combined impact of these limited
results and theoretical predictions is that, as opposed to
extrapolation from 1-g data, direct knowledge of low-g
combustion particulate is needed for more confident
design of smoke detectors for spacecraft.


## SAME EXPERIMENT CONCEPT


To address the limited data from the CSD experiment
concerning the likely size of spacecraft smoke
particulate, another experiment, the Smoke Aerosol
Measurement Experiment (SAME), was developed. The
SAME experiment sought to avoid the problems
experienced by the CSD experiment by obtaining the
particulate size statistics on-orbit with a reduced
dependence upon sample return to Earth. This is a
challenging endeavor because existing aerosol
instrumentation is typically large, incompatible with
spacecraft experiment constraints, and may require
substantial sample return to Earth. As will be described
below, an alternative approach was employed that used
three discrete instruments to estimate separate
moments of the size distribution. When combined, these
moments provide useful aggregate statistics of the size
distribution. The measurements were made using
smoke generated by overheated spacecraft materials in
much the same manner as the CSD experiment,
however, the sample temperature, flow field, and particle
aging time were more rigorously controlled.


1. -2




### MOMENT METHOD


The approach used by the SAME experiment is termed
the 'moment method' for convenience.8 As will be
described below, the approach consists of measuring
three moments of the size distribution (zeroth, first and
third) and using the properties of the log-normal
distribution to estimate the geometric mean diameter
(GMD) and the geometric standard deviation (GSD).


The average particle size and the width of the size
distribution will be estimated from various moments of
the size distribution. The number distribution, fN(D), is
defined as


## fN (D) = (1)


## dN dD


where dN is the number of particles per cm3 with
diameter between D and D + dD. The moments of
interest consist of the number concentration, M0, the first
moment M1, and the volume or mass concentration
moment, M3 and are defined as


Mi = ∫Di fN (D )dD i = 0,1,3 (2)
When i=0, the zeroth moment of the distribution, M0,
equation (2) is simply the number of particles per unit
volume. In the SAME experiment, this was measured
using a condensation nuclei counter. The first moment,
i=1, can also be thought of as the "diameter
concentration" or integrated diameter per unit volume
and is approximately proportional to the ionization
detector moment (signal). For particles in the Mie
scattering regime, particles sizes from 0.3λ to about 3λ
(~0.2 μm to 2.0 μm for a red laser), the light scattering
signal is approximately proportional to the third moment,
i=3. From these moments, and a measurement of M0
using a condensation particle counter, two mean
diameters can be computed: the count (arithmetic) mean
diameter D0.5 or d , which is equal to M1/M0 and the
diameter of average mass D1.5 or d , which is equal to
m
(3/(4πρ)M3/M0)1/3. The basis for the subscript naming
convention for D0.5 and D1.5 will be discussed later). The
log-normal size distribution is widely used for describing
the size distribution of aerosols including non-flaming
smoke because, for most aerosols, the bulk of the
number concentration is associated with smaller
particles.9, 10
The number distribution fN(D) for the


lognormal distribution is expressed as follows:


⎛ D D 2
ln ln ⎞


t - g ⎟
N = N
f (D) exp
2π 1/2D lnσ 2ln2σ ⎟ (3)
( )


## ( )


g ⎠


⎜


⎜-


⎝


g


where Nt is the total number concentration of the aerosol
(=M0), and Dg and σg are the geometric mean diameter
and geometric standard deviation defined by


## ∞ ∞ ln Dg = ∫ ln DfN ( D)dD / fN dD ∫ (4) 0 0


1 / 2


⎤ ∞
f N( D) dD⎥
⎦


(ln ln )2 ( D) dD/ ∫


⎡∞
⎢∫ D- Dg fN


⎣
(5)


lnσ =
g


0 0


For the log-normal distribution, one finds that the various
diameter definitions given above are related to the GMD,
Dg, via the equation:9,10


D = D exp( p ln 2σ
g g )
p


(6)


For the count mean diameter, D0.5, and the diameter of
average mass, D1.5, the corresponding values of p are
0.5 and 1.5. Fig. 1 shows a typical log-normal
distribution for a Dg=1.0 μm and σg= 1.6. For this
distribution, the corresponding values of D0.5 and D1.5
are1.17 μm and 1.39 μm, respectively. Using equation
(6), one can relate σg to the ratio of D1.5 and D0.5 via the
equation:


## (


g exp ln(D


)1 / 2


1. / (7)


D
0.5 )


## σ =


Figure 1: Diameters for a log-normal distribution
with Dg=1.0 and σg= 1.6.


By combining these three moments it is possible to
compute three mean diameters of the size distribution
and the geometric standard deviation. Validation of this
approach is discussed in Cleary, Weinert and
Mulholland.8 These statistics provide a strong basis for
design of spacecraft smoke detectors.


1. -3




### INSTRUMENTS


More details of the experiment hardware and its
calibration are presented elsewhere,11,12 however a brief
summary follows. The moment measurements were
made using an assembly of three separate instruments.
Two are industrial hygiene instruments manufactured by
TSI and one is a modified residential smoke detector.


The zeroth-moment instrument is a condensation nuclei
counter P-Trak® (TSI Inc.). This device operates by
passing the aerosol-laden particle stream through a
region saturated with isopropanol vapor and then into a
cooler region where the vapor condenses onto the
particles increasing their diameter such that they can be
readily counted by a light scattering detector. This
instrument is very robust and operates over a range of 0
to 105 particles/cm3 and 20 nm to 4 to 5 μm diameter.
Some dilution is required, since the allowable smoke
concentration ranges from about 0.5 × 106 to 5 × 106
particles / cm3.


The first-moment instrument is an ionization chamber
from a residential smoke detector. This device uses an
alpha-particle emitter (Am241) to generate ions in a
region within a DC electric field. The drift of the ions in
the electric field results in a current. The presence of
particulate reduces the current as a result of the
attachment of the ions to the particulate. The mobility of
the charged aerosol is too small for it to be collected on
the ionization chamber electrode. The required particle
concentrations are on the order of 105 particles/cm3, and
no sample dilution was required.


The third-moment instrument is a light scattering device
DustTrak® (TSI Inc.). The device measures the
intensity of light scattered by the smoke aerosol at a
scattering angle of about 90 degrees light scattering
signal to quantify the aerosol mass. This light scattering
signal is approximately proportional to the mass
concentration; however, to compensate for the non-
linearity of the relationship between mass and the
scattering signal density, additional analysis based on
Mie Scattering theory or calibration with the specific
aerosol material is required. The device's operating
range is from 0.001 mg/m3 to 100 mg/m3. These
devices are equipped with an aerodynamic impactor at
the inlet which captures particles larger than the
selected size. The SAME experiment included 2
DustTraks® one with a 1 μm impactor and one with a 10
μm impactor. The difference in the signal from these
two devices provided a measure of the fraction of the
particulate that was larger than 1 μm. In some cases
dilution was required owing to the high smoke
concentration levels.


A schematic of the assembled hardware appears in Fig.


1. The system was installed in the Microgravity Science


B-4


Glovebox, an ISS facility that provides many resources
including: containment, power, data, video and uplink
commanding. Smoke was generated by overheating a
small sample of material in the smoke generation duct
for approximately 60 seconds. During this interval,
controlled flow was induced by a moving piston in the
aging chamber which drew the smoke into the chamber.
The smoke was held in the aging chamber for a
predetermined time, allowing the particles to coagulate.
After a specified aging time, the smoke was then pushed
by the piston into the diagnostics duct where the
moment instruments made their measurements. Also
installed in the diagnostics duct were space shuttle and
ISS smoke detectors. As the smoke was monitored by
the moment instruments, a sample of the smoke
particles was deposited on a Transmission Electron
Microscope (TEM) grid via a thermal precipitator which
uses thermophoresis to deposit the particles on the
grids.


Figure 2. Schematic of the SAME hardware.


The zeroth and first moment devices showed good
linearity over the conditions of interest however, the third
moment device (TSI- DustTrak®) is theoretically
predicted to show non-monotonic behavior as particle
size is increased. While a satisfactory prediction of the
DustTrak® response was obtained using liquid droplets
of dioctyl phthalate, the uncertainty associated with the
Mie scattering calculations due to the particle refractive
index estimate, the potential of agglomerated particles,
and deviation from assumed log-normal size distribution
must be assessed further for the smoke samples here.
In the results reported here, the DustTrak® response
was directly calibrated, for each smoke source, against
mass concentration measurements using a tapered
element oscillating microbalance. This approach is valid
as long as the size distribution of the sample does not
change significantly. Using estimated material densities,
the diameter of average mass was computed for each
sample. Equation 7 was used to compute the geometric
standard deviation from the arithmetic mean diameter
and the diameter of average mass, and Equation 6 was
used to compute the GMD.




#### EXPERIMENTAL RESULTS


Overall, 30 sample materials were tested. These were
comprised of six samples each of 5 materials: Teflon®,
Kapton®, silicone rubber, cellulose (lamp wick), and
dibutyl-phthalate deposited on a porous wick. Geometric
Mean (GMD), Arithmetic Mean, and Average Mass
diameters and the Geometric Standard Deviation (GSD)
results from the moment instruments for baseline runs
(no aging) and 720 second aging are presented in Table


1.


The Teflon® and Kapton® particles were very small with
Teflon® showing limited increase in the size from the
diameter of average mass compared to the arithmetic
mean diameter. The lamp wick results exhibited
substantially larger diameter of average mass. As
reported previously,11 the DustTrak results for lamp wick
and silicone rubber demonstrated that substantial
portions of the particle distribution possessed
aerodynamic diameters larger than 1 micrometer. The
small diameters for the Kapton® and Teflon® will make
detection of this smoke challenging for light scattering
devices; on the other hand, the large sizes seen with the
lamp wick and silicone rubber would generate very large
signals on a light scattering system, suggesting that
detection of these particles against the background
environment will require a detection system capable of
measuring more than one moment of the particle size
distribution. The aging results showed substantial
increase in the average particle sizes with the diameter
of average mass rising to over 500 nm for the aged
silicone rubber. Since the aging process can be
considered to be representative of smoke emerging from
a closed volume (e.g. an avionics enclosure), fire
sensors must consider large particles in addition to the
smaller particles seen with Kapton®.


<table>
 <tr>
  <th></th>
  <th>Geom.<br/>Mean<br/>Diam.<br/>(nm)</th>
  <th>Arithmetic<br/>Mean<br/>Diam.<br/>(nm)</th>
  <th>Diam. of<br/>Average<br/>Mass<br/>(nm)</th>
  <th></th>
 </tr>
 <tr>
  <td>Kapton<br/>Kapton</td>
  <td>80<br/>155</td>
  <td>105<br/>186</td>
  <td>179<br/>267</td>
  <td>2.08<br/>1.82</td>
 </tr>
 <tr>
  <td>Lamp wick<br/>Lamp wick</td>
  <td>186<br/>258</td>
  <td>227<br/>308</td>
  <td>341<br/>438</td>
  <td>1.89<br/>1.81</td>
 </tr>
 <tr>
  <td>Silicone<br/>Silicone</td>
  <td>189<br/>352</td>
  <td>257<br/>422</td>
  <td>472<br/>606</td>
  <td>2.18<br/>1.83</td>
 </tr>
</table>


Teflon 170 205 297 1.84
Teflon
aged 228 273 392 1.82


## DETECTOR DESIGN REQUIREMENT IMPLICATIONS


To develop requirements from these results, it is
instructive to consider some basic overarching criteria:


B-5


1. The requirement must not effectively define the
technology
2. The requirement must be verifiable in a laboratory.


1. If the requirement describes or implies a test that cannot be done on every unit, it must be possible to define a subtest that can be conducted to qualify production units.

2. The requirement should represent the best understanding of spacecraft smoke conditions.


One possible method to meet these criteria is to develop
a requirement that states an aerosol condition at alarm.
To provide some perspective on the impact of the choice
of such requirements, Figs. 3 and 4 present the outcome
of a hypothetical single point requirement if it were
implemented with different detector technologies. Each
of these technologies respond to different particle
characteristics such as the first or third moment of the
distribution or the scattering signal. These figures were
developed assuming the alarm level was set at 2 mg/m3
for a log-normal particle size distribution with a 500 nm
geometric mean diameter (GMD) and a geometric
standard deviation (GSD) of 1.3. The values for the
moment devices were calculated using Eq. 6 and the
values for the scattering device were calculated using
the Mie scattering model of Gockel.13 In practice, a fire
could produce a smoke particle size distribution with a
GMD different than 500 nm yet each of these detectors
would have an alarm point determined by their response
at the alarm-requirement aerosol. For each type of
detector, the alarm number concentration (Fig. 3) or
alarm mass concentration (Fig. 4) were calculated as a
function of the particle diameter. This is the
concentration needed to achieve the same signal level
as the alarm-requirement aerosol (2 mg/m3 mass
concentration, 500 nm GMD, and 1.3 GSD). As is
evident in the graphs, depending upon the selected
instrument, strong deviations are seen in number
concentration and mass concentration at either the small
or large ends of the particle distribution. For example,
as particle diameter is increased, progressively smaller
number concentrations are needed to reach alarm for


1000.00


1. 


10.00


1. 


0


1. 


0.01


500


## Particle Counter device


First moment device
Third moment device
Scattering device


1000


1500


## Count Median Diameter (nm)


Figure 3: Normalized Number concentration at
alarm for 4 smoke detector technologies assuming
the alarm level was set at 2 mg/m3 for 500 nm GMD
and a geometric standard deviation of 1.3.




<table>
 <tr>
  <th>1000.00</th>
  <th>Counter device<br/>moment device</th>
 </tr>
 <tr>
  <td></td>
  <td>moment device<br/>device</td>
 </tr>
 <tr>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <td></td>
  <td>500 1000</td>
 </tr>
 <tr>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <td></td>
  <td>Count Median Diameter</td>
 </tr>
</table>


1500


Figure 4: Normalized mass concentration at alarm for
4 smoke detector technologies assuming the alarm
level was set at 2 mg/m3 for 500 nm GMD and a
geometric standard deviation of 1.3.


the scattering detector. This could indicate increased
sensitively to nuisance sources such as dust. On the
other hand, the number concentrations for alarm also
rise quite high at smaller sizes for the same detector.
Similar dependencies are seen with all detectors
suggesting that a detector that measures a single
moment of the size distribution may suffer from
conditions where it is either too sensitive or not sensitive
enough. Consequently a specification for a single
particle size (or no size specification) would be risky. If
the requirement is limited to a single particle size, the
result can easily be a detector that is insensitive to the
other sizes. This is essentially the case for the current
ISS and STS detectors which are tuned to different size
ranges and have very different sensitivities to particle
size.5 An alternative is to develop alarm requirements
that include criteria at particle sizes spanning the
expected range of fire particulate (e.g. 200 to 1200 nm).
A detector that involves two moment measurements
may be able to capitalize on the size information that is
generated by the ratio between the two moment values.
As can be seen in Figs. 3 and 4, the systematic variation
between the alarm signals of different instruments could
be used to discern size information This is similar to the
approach suggested by Litton et al. who demonstrated
that by combining two simple particle sensors that
measure different moments, an inexpensive assessment
of the particle size could be achieved.14 With a detector
that provides a combination of a concentration or
moment measurement and an indication of the size, it
would be possible to satisfy detection requirements that
include concentrations at more than one particle size
and the two signals might also help reduce false alarms


## ACKNOWLEDGMENTS


The support of the SAME experiment team and the
crews of ISS Increments 10, 13, and 15 are gratefully
acknowledged. The SAME project was conducted
through the ISS Exploration Research Project of the
Exploration Technology Development Program. The
support of this program is also acknowledged.


B-6


Certain commercial entities, equipment, or materials
may be identified in this document in order to describe
an experimental procedure or concept adequately. Such
identification is not intended to imply recommendation or
endorsement by the National Aeronautics and Space
Administration or the National Institute of Standards and
Technology, nor is it intended to imply that the entities,
materials, or equipment are necessarily the best
available for the purpose.


## REFERENCES


1. Bukowski, R.W. and G.W. Mulholland, "Smoke Detector Design and Smoke Properties," NBS Technical Note 973, 1978.

2. Bukowski, R. W, R. D. Peacock, J. D. Averill, T. G. Cleary, N. P. Bryner, W. D. Walton, P. A. Reneke, and E. D. Kuligowski, "Performance of Home Smoke Alarms, Analysis of the Response of Several Available Technologies in Residential Fire Settings," NIST Technical Note 1455, December 2003.

3. Brooker, J. E., Urban, D.L., Ruff, G.A., "ISS Destiny Laboratory Smoke Detection Model", 07ICES-113, 2007 International Conference on Environmental Systems, Chicago, Ill. July 2007.

4. Friedman, R., "Fire Safety Practices and Needs in Human-Crew Spacecraft," Journal of Applied Fire Science, Vol. 2, 1992, pp. 243-259.

5. Urban, D.L., Griffin D., Ruff, G.A., Cleary, T., Yang, J., Mulholland, G., Yuan, Z.G., "Detection of Smoke from Microgravity Fires", 2005 International Conference on Environmental Systems, Rome Italy, Paper # 2005-01-2930 July 2005, SAE Transactions, pp 375-384.

6. Steisslinger, H. R., D. M. Hoy, J. A. McLin and E. C. Thomas., "Comparison Testing of the Space Shuttle Orbiter and Space Station Freedom Smoke Detectors," SAE Paper 932291, 1993.

7. Ruff, G.A., D.L. Urban, and M.K. King, "A Research Plan for Fire Prevention Detection and Suppression," AIAA-2005-0341, 43rd Aerospace Sciences Meeting and Exhibit, Reno, NV, January 9-12, 2005. 8. Cleary, T.G., D W. Weinert, and G.W. Mulholland, "Moment Method for Obtaining Particle Size Measures of Test Smokes", Natl. Inst. Stand. Technol., NISTIR 7050, 2003. 9. Raabe, O.G., J. Aerosol Sci., Vol. 2, 1971, p. 289. 10. Reist, P.C., Introduction to Aerosol Science, Macmillan Pub. Co., NY, NY, 1984. 11. Urban, D.L. Ruff, G.A., Mulholland, G.W., Cleary, T.G., Yang, J.C., Yuan, Z.G., "Measurement of Smoke Particle Size under Low-Gravity Conditions," 2008 International Conference on Environmental Systems, Chicago, IL, Paper 2008- 01-2089.




1. Urban, D.L. Ruff, G.A., Cleary, T.G., Yang, J.C., Mulholland, G.W., Yuan, Z.G., Sheredy, W., "Properties of Smoke from overheated Spacecraft Materials in Low-Gravity", 47th Aerospace Sciences Meeting, Orlando, Fl Paper AIAA-2009- 956, 2009. 13. Gockel, F., "Fire Sensor Modelling and Simulation," 12th Int. Conference on Automatic Fire Detection, AUBE 2001, 26-28 March 2001, Maryland, USA 14. Litton, C.D., Smith, K.R., Edwards, R., and Allen, T., "Combined Optical and Ionization Measurement Techniques for Inexpensive Characterization of Micrometer and Submicrometer Aerosols," Aerosol Science and Technology, Vole 38, 1054-1062, 2004.


## ACRONYNMS


CSD: Comparative Soot Diagnostics


DAFT: Dust Aerosol measurement Feasibility Test


GMD: Geometric Mean Diameter


GSD: Geometric Standard Deviation


ISS: International Space Station


MSG: Microgravity Science Glovebox


SAME: Smoke Aerosol Measurement Experiment


STS: Space Transportation System


TEM: Transmission Electron Microscope


UL: Underwriters Laboratory


1. -7




1. -8




### Appendix C


#### Properties of Smoke from Overheated Materials in Low- Gravity


David L. Urban1, Gary A. Ruff2 and William Sheredy3,
NASA Glenn Research Center, Cleveland, Ohio 44135


Thomas Cleary4 and Jiann Yang5
National Institute of Standards and Technology, Gaithersburg, Maryland 20899


George Mulholland6
The University of Maryland, College Park, Maryland 20742


and


Zeng-guang Yuan7
National Center for Space Exploration Research, Cleveland, Ohio 44135


Smoke particle size measurements were obtained under low-gravity conditions by
overheating several materials typical of those found in spacecraft. The measurements
included integral measurements of the smoke particles and physical sample of the particles
for Transmission Electron Microscope analysis. The integral moments were combined to
obtain geometric mean particle sizes and geometric standard deviations. These results are
presented with the details of the instrument calibrations. The experimental results show
that, for the materials tested, a substantial portion of the smoke particles are below 500 nm
in diameter.


## I. Introduction


Appropriate design of fire detection systems requires knowledge of both the expected signature of the events to
be detected and the background levels of the measured parameters. Terrestrial fire detection systems have been
developed based on extensive study of terrestrial fires.1, 2 Unfortunately there is no corresponding data set for
spacecraft fires and consequently the fire detectors in current spacecraft were developed based upon terrestrial
designs. There are a number of factors that can be expected to affect the particle size distribution of the smoke from
spacecraft fires. The absence of buoyant flow in low-gravity increases the residence time in microgravity fires and
increases the transit time from the reaction zone to the detector.3 Microgravity fires have been found to have
radically different structure from their 1-g counterparts. The limited options available to respond to a spacecraft fire
increase the importance of early detection. Finally the materials used in spacecraft are different from typical
terrestrial applications where smoke properties were previously evaluated. All of these effects can be expected to
change the smoke particle size distribution. The objective of this work was to make sufficient measurements of
smoke from spacecraft fires to enable improved design of future detectors.


Smoke Background


1 Branch Chief, Combustion and Reacting Systems Branch, 21000 Brookpark Road, MS 77-5, Senior Member.
2 Advanced Capabilities Project Office, 21000 Brookpark Road, MS 77-7, Associate Fellow.
3 ISS Projects Office, 21000 Brookpark Road, MS 77-5.
4 Engineered Fire Safety Group, 100 Bureau Drive, Stop 8664.
5 Fire Measurements Group Leader, 100 Bureau Drive, Stop 8662.
6 Visiting Professor of Mechanical Engineering, Glenn L. Martin Hall.
7 Staff Scientist, 21000 Brookpark Road, MS 77-5.


1
American Institute of Aeronautics and Astronautics


1. -1




Smoke is a general term that encompasses aerosol materials produced by a number of processes. In particular it
can include unburned, recondensed, original polymer or pyrolysis products that can be either liquid or solid,
hydrocarbon soot, condensed water vapor, and ash particles. Soot particles dominate the smoke particulate in
established flaming fires while unburned pyrolysis products and recondensed polymer fragments are produced by
smoldering and pyrolysis in the early stage of fire growth. Given the constrained space on any spacecraft, the target
for the fire detection system is necessarily the early phase and not established flaming fires; consequently, the
primary target for detection is the pyrolysis products and not the soot.
Prior spacecraft systems are summarized in more detail in papers by Friedman and Urban.4, 5 In the Mercury,
Gemini and Apollo missions, the crew quarters were limited and mission durations were short, consequently it was
considered reasonable that the astronauts would rapidly detect any fire. The Skylab module, however, included
approximately 30 UV-sensing fire detector.4 These devices were limited to line-of-sight and were reported to have
difficulties with false alarms. The Space Shuttle Detectors were based upon ionization fire detector technology, the
most advanced technology available at the time and used an inertial separator designed to eliminate particles larger
than 1-2 micrometers. The International Space Station (ISS) smoke detectors use near-IR forward scattering,
rendering them most sensitive to particles larger than a micrometer, outside of the range of sensitivity of the shuttle
detector. As described by Friedman4 there have been six overheat and failed component failures in the NASA
Orbiter fleet in addition to several similar incidents that have occurred on the ISS. None of these events spread into a
real fire but as mission durations increase, the likelihood of failures increases. The experience on Mir in 1997 has
shown that failure of oxygen generation systems can have significant consequences. As a result, improved
understanding of spacecraft fire detection is critically needed.6
Previous work on smoke particles from low-gravity sources by Urban et al.5 found that the particulate produced
by low-gravity flames (soot or unburned fuel particles) tends to have larger size particles than in normal gravity.
Results from the CSD (Comparative Soot Diagnostics) Experiment5 which studied smoke properties in low-gravity
from several spacecraft materials suggested that liquid smoke particles could achieve sizes larger than 1 µm while
solid particulate remained in the sub-micrometer range. However, the CSD experiment did not produce sufficient
data concerning the size of the liquid smoke particles to guide detector design. The combined impact of these limited
results and theoretical predictions is that, as opposed to extrapolation from 1-g data, direct knowledge of low-g
combustion particulate is needed for more confident design of smoke detectors for spacecraft.


## II. SAME Experiment


To address the limited data from the CSD experiment concerning the likely size of spacecraft smoke particulate,
another experiment the Smoke Aerosol Measurement Experiment (SAME) was developed. The SAME experiment
sought to avoid the problems experienced by the CSD experiment by obtaining the particulate size statistics on-orbit
with a reduced dependence upon sample return to Earth. This is a challenging endeavor because existing aerosol
instrumentation is typically large, incompatible with spacecraft experiment constraints, and may require substantial
sample return to Earth. As will be described below, an alternative approach was employed that used three discrete
instruments to measure separate moments of the size distribution. When combined, these moments provide useful
aggregate statistics of the size distribution. The measurements were made using smoke generated by overheated
spacecraft materials in much the same manner as the CSD experiment however the sample temperature, flow field,
and particle aging time were more rigorously controlled.


## A. Moment Method


The approach used by the SAME experiment is termed the 'moment method' for convenience.7 As will be
described below, the approach consists of measuring three moments of the size distribution (zeroth, first and third)
and using the properties of the log-normal distribution to estimate the geometric mean diameter and the standard
deviation.
The average particle size and an estimate of the width of the size distribution will be estimated from various
moments of the size distribution. The number distribution, fN(D), is defined as


## fN (D)  (1)


## dN dD


where dN is the number of particles per cm3 with diameter between D and D + dD. The moments of interest consist
of the number concentration, M0, the first moment M1, and the volume or mass concentration moment, M3 and are
defined as


2
American Institute of Aeronautics and Astronautics


1. -2




### Mi  Di fN (D )dD i  0,1,3 (2)


When i=0, the zeroth moment of the distribution, M0, equation (2) is simply the number of particles per unit
volume. In the SAME experiment, this was measured using a condensation nuclei counter. The first moment, i=1,
can also be thought of as the "diameter concentration" or integrated diameter per unit volume and is approximately
proportional to the ionization detector moment (signal). For particles in the Mie scattering regime, particles sizes
from 0.3 to about 3 (~0.2 μm to 2.0 μm for a red laser), the light scattering signal is approximately proportional to
the third moment, i=3. From these moments, and a measurement of M0 using a condensation particle counter, two
mean diameters can be computed: the count (arithmetic) mean diameter D0.5 or d , which is equal to M1/M0 and the
d , which is equal to (M
diameter of average mass D1.5 or m 3/M0)1/3. The basis for the subscript naming convention
for D0.5 and D1.5 will be discussed later). The log-normal size distribution is widely used for describing the size
distribution of aerosols including non-flaming smoke because for most aerosols; the bulk of the number
concentration is associated with smaller particles.8, 9 The number distribution fN(D) for the lognormal distribution is
expressed as follows:


 D D  
 g 
2
ln ln
2ln2 
g 


t
N
2 1/2D ln
( )


- 

- 


exp






N
f (D)


(3)


## 


g


where Nt is the total number concentration of the aerosol (=M0), and Dg and g are the geometric mean diameter and
geometric standard deviation defined by


##  / NdD (4)


##   ln Dg   ln Df N( D)dD f


0 0


1/ 2


 
fN ( D) dD 
 0




ln g   (ln D ln Dg )2 fN ( D)dD /


0


(5)


For the log-normal distribution, one finds that the various diameter definitions given above are related to the
geometric mean number diameter, Dg, via the equation:8 9


p ) (6)


## D  D


p 
g exp( ln2 g


For the count mean diameter, D0.5, and the diameter of average mass, D1.5, the corresponding values of p are 0.5
and 1.5. Fig. 1 shows a typical log-normal distribution for a Dg=1.0 and g= 1.6. For this distribution, the
corresponding values of D0.5 and D1.5 are1.17 m and 1.39 m, respectively. Using equation (6), one can relate g to
the ratio of D1.5 and D0.5 via the equation:


1.5 / D0.5) (7)


## 


g exp ln(D


1 / 2


##  


3
American Institute of Aeronautics and Astronautics


1. -3




By combining these three moments it is possible
to compute three mean diameters of the size
distribution and the geometric standard deviation.
Validation of this approach is discussed in Cleary,
Weinert and Mulholland.7 These statistics provide a
strong basis for design of spacecraft smoke
detectors.


## B. Instruments


These measurements were made using an
assembly of three separate instruments. Two are
industrial hygiene instruments manufactured by TSI
and one is a modified residential smoke detector.
The zeroth-moment instrument is a condensation Figure 1: Diameters for a log-normal distribution with
nuclei counter P-Trak™ (TSI Inc.). This device Dg=1.0 and g= 1.6.
operates by passing the aerosol-laden particle stream
through a region saturated with isopropanol vapor
and then into a cooler region where the vapor
condenses onto the particles increasing their diameter such that they can be readily counted by a light scattering
device. This instrument is very robust and operates over a range of 0 to 105 particles/cm3 and 20 nm to 1 μm
diameter. Some dilution is required, since the smoke concentration ranges from about 0.5 × 106 to 5 × 106 particles /
cm3 There was also a concern that the isopropanol condensate would not return to the wick in low-gravity.5 To
mitigate this issue, the condensing section of the device was modified with very small grooves to improve
conductance of the condensate back to the wick. These changes were tested in a separate space experiment with
good results indicating the modified device could be used successfully in low gravity.5
The first-moment instrument is the ionization chamber from a residential smoke detector. This device uses an
alpha-particle emitter to generate ions in a region within a DC electric field. The drift of the ions in the electric field
results in a current. The presence of particulate reduces the current as a result of the attachment of the ions to the
particulate. The mobility of the charged aerosol is too small for it to be collected on the ionization chamber
electrode. The required particle concentrations are on the order of 105 particles/cm3 and no sample dilution was
required.
The third-moment instrument is a light scattering device DustTrak™ (TSI Inc.). The device uses a 90 degree
light scattering signal to quantify the aerosol mass density. For terrestrial dust particulate this signal correlates well
with the mass concentration, however additional compensation will be needed to account for the range of particle
sizes that will be seen in the SAME experiment. The device's operating range is from 0.001 mg/m3 to 100 mg /m3.
These devices are equipped with an aerodynamic impactor at the inlet which captures particles larger than the
selected size. The SAME experiment included 2 DustTraks™ one with a 1 μm impactor and one with a 10 μm
impactor. The difference in the signal from these two devices provided a measure of the fraction of the particulate
that was larger than 1 μm. In some cases dilution was required owing to the high smoke concentration levels.
A schematic of the assembled hardware
appears in Fig. 2. The system was installed
in the Microgravity Science Glovebox, an
ISS facility that provides many resources
including: containment, power, data, video
and uplink commanding. Smoke was
generated by overheating a small sample of
material in the smoke generation duct for
approximately 60 seconds. During this
interval, controlled flow was induced by a
moving piston in the aging chamber which
drew the smoke into the chamber. The
smoke was held in the chamber for a
predetermined time, allowing the particles
to coagulate. After a specified aging time, Figure 2. Schematic of the SAME hardware.
the smoke was then pushed by the piston
into the diagnostics duct where the moment instruments made their measurements. Also installed in the diagnostics


4
American Institute of Aeronautics and Astronautics


1. -4




duct were space shuttle and ISS smoke 600000
detectors. As the smoke was monitored
by the moment instruments, a sample of 500000
the smoke particles was deposited on
Transmission Electron Microscope (TEM) 400000
grid via a thermal precipitator which uses
thermophoresis to deposit the particles on 100 nm
the grids. 300000 600 nm
1200 nm
Calibration of these instruments was
essential to properly interpret the flight 200000
data and was performed on the ground
before the flight. Calibration was 100000
accomplished using two different aerosol
generators one using mono-disperse 0
0 50000 100000 150000 200000 250000 300000 350000
particle generation using dioctyl phthalate Ptrak output (number count/cc)
(DOP) according to the approach by Figure 3: Ptrak Calibration results with Mono disperse DOP
Mulholland and Liu10 and the other using droplets.
polystyrene spheres. The monodisperse
droplet generator functioned by producing a spray of DOP diluted with isopropanol which is then evaporated and
recondensed producing monodisperse droplets. The droplet size is controlled by the DOP dilution level. The
generator will operate stably for tens of
minutes. The aerosol from the generator 500
was sampled simultaneously by the 450
SAME instrument under test and a 400
reference standard. For the number
count, the reference instrument was a 350
TSI 3022 particle counter, for the Mass 300
Concentration, a Tapered Element
Oscillating Microbalance and for the 250
Separate correlations were developed for
each particle size and the closest 0
4.5 5 5.5 6 6.5 7
correlation was used to analyze the flight Ionization Chamber output (volts)
data based on the initial estimates of the Figure 4: Ion Chamber Calibration results with Mono disperse DOP
average particle size. droplets.
100 150 nm
600 nm
1200 nm
the DustTrak shown in Fig. 5 was


<table>
 <tr>
  <th></th>
 </tr>
 <tr>
  <th>100 nm<br/>150 nm<br/>300 nm</th>
 </tr>
 <tr>
  <th>600 nm<br/>750 nm<br/>1200 nm</th>
 </tr>
 <tr>
  <th></th>
 </tr>
</table>


<table>
 <tr>
  <th>first moment a TSI Electrical Aerosol</th>
  <td>200</td>
 </tr>
 <tr>
  <th>Detector was used. The results for the P-</th>
  <td>150</td>
 </tr>
 <tr>
  <th>Trak are shown in Fig. 3. As the number</th>
  <td></td>
 </tr>
 <tr>
  <th>concentration increased, the effect of the</th>
  <td>100</td>
 </tr>
 <tr>
  <th>particle diameter became more evident.</th>
  <td>50</td>
 </tr>
</table>


<table>
 <tr>
  <th>The first moment device, the ion</th>
  <td>180</td>
  <td></td>
 </tr>
 <tr>
  <th>chamber showed little effect of particle</th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>size as seen in Fig 4. Consequently a</th>
  <td>160</td>
  <td></td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>single correlation was used for all</th>
  <td>140</td>
  <td></td>
 </tr>
 <tr>
  <th>particle sizes.</th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>The third moment device (TSI-Dust</th>
  <td>120</td>
  <td></td>
 </tr>
 <tr>
  <th>Trak) is theoretically predicted to show</th>
  <td></td>
  <td>100 nm</td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>non-monotonic behavior as particle size</th>
  <td></td>
  <td>300 nm</td>
 </tr>
 <tr>
  <th></th>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <th>is increased. The calibration results for</th>
  <td>80</td>
  <td>750 nm</td>
 </tr>
</table>


60
obtained using monodisperse DOP
particles and indicates a strong 40
dependence on particle size. This
dependence becomes even more 20
complicated when the particle size 0
distribution is polydisperse. 0 50 100 150 200 250 300
DustTrak output (mg/m3)


Figure 5: Dust Trak results with Mono disperse DOP droplets.
5
American Institute of Aeronautics and Astronautics


1. -5




To address this calibration while minimizing the assumptions required about the particle size distribution, a
model of the operation of the DustTrak instrument was developed using Mie scattering theory. Using the zeroth and
first moment data along with the refractive index of the particulate, the third moment was predicted by assuming a
log-normal distribution and making initial guesses for the geometric mean diameter and the geometric standard
deviation. The output of the DustTrak was then predicted by the scattering model and the model proceeded in an
iterative manner until the predicted DustTrak output matched the actual output. The geometric mean diameter and
geometric standard deviation were those that produced convergence of the predicted and measured DustTrak output.
In some cases, convergence was not obtained and for these cases, the geometric mean diameter can not be
determined. This non-convergence is currently under investigation but may be due to the presence of a bimodal
particle size distribution.


## C. Experimental Results


Overall 30 sample materials were
tested. These were comprised of six
samples each of 5 materials: Teflon™,
Kapton™, silicone rubber, cellulose
(lamp wick), and dibutyl-phthalate
deposited on a porous wick. The TEM
girds recovered from the thermal
precipitators were unfortunately
contaminated with extraneous particles
whose origin is currently under
investigation. Despite the contamination,
the lamp wick and Teflon samples
produced distinct particles consistent
with ground based experience. Typical
particles are shown in Fig. 6 Geometric
Mean, Arithmetic Mean, and Average
Mass diameter results from the moment instruments for baseline


<table>
 <tr>
  <th>Geometric Mean</th>
  <th>Arithmetic Mean</th>
  <th></th>
 </tr>
 <tr>
  <td>Diameter</td>
  <td>Diameter</td>
  <td>Diameter of Average</td>
 </tr>
 <tr>
  <td>(micro meters)</td>
  <td>(micro meters)</td>
  <td>Mass (micro meters)</td>
 </tr>
 <tr>
  <td>Kapton 0.080</td>
  <td>0.105</td>
  <td>0.172</td>
 </tr>
 <tr>
  <td>Lamp wick 0.186</td>
  <td>0.227</td>
  <td>0.420</td>
 </tr>
 <tr>
  <td>Silicone 0.189</td>
  <td>N/A</td>
  <td>N/A</td>
 </tr>
 <tr>
  <td>Teflon 0.159</td>
  <td>0.205</td>
  <td>0.219</td>
 </tr>
</table>


Figure 6: Test point 32 Lamp wick


Test point 26, Teflon


runs are presented in Table 1.


Table 1:Diameter results from baseline runs. The Silicone results did not converge for these conditions


Overall, the Teflon and Kapton particles were very small with limited increase in the size from the diameter of
average mass compared to the arithmetic mean diameter. The Lamp wick results exhibited substantially larger
diameter of average mass. As reported previously,11 the Dust Trak results for Lamp wick and Silicone demonstrated
substantial portions of the particle distribution possessed aerodynamic diameters larger than 1 micrometer. The
small diameters for the Kapton and Teflon will make detection of this smoke challenging for light scattering
devices, on the other hand the large sizes seen with the Lamp wick and Silicone would generate very large signals
on a light scattering system, suggesting that detection of these particles against the background environment will
require a detection system capable of measuring more than one moment of the particle size distribution.


## III. Acknowledgments


The support of the SAME experiment team and the crews of ISS increments 10, 13, and 15 are gratefully
acknowledged. The SAME project was conducted through the ISS Exploration Research Project of the Exploration
Technology Development Program. The support of this program is also acknowledged.


6
American Institute of Aeronautics and Astronautics


1. -6




Certain commercial entities, equipment, or materials may be identified in this document in order to describe an
experimental procedure or concept adequately. Such identification is not intended to imply recommendation or
endorsement by the National Aeronautics and Space Administration or the National Institute of Standards and
Technology, nor is it intended to imply that the entities, materials, or equipment are necessarily the best available for
the purpose.


## IV. References


1Bukowski, R.W. and G.W. Mulholland, "Smoke Detector Design and Smoke Properties," NBS Technical Note 973, 1978.
2Bukowski, R. W, R. D. Peacock, J. D. Averill, T. G. Cleary, N. P. Bryner, W. D. Walton, P. A. Reneke, and E. D.
Kuligowski, "Performance of Home Smoke Alarms, Analysis of the Response of Several Available Technologies in Residential
Fire Settings," NIST Technical Note 1455, December 2003.
3Brooker, J. E., Urban, D.L., Ruff, G.A., "ISS Destiny Laboratory Smoke Detection Model", 07ICES-113, 2007
International Conference on Environmental Systems, Chicago, Ill. July 2007.
4Friedman, R., "Fire Safety Practices and Needs in Human-Crew Spacecraft," Journal of Applied Fire Science, Vol. 2, 1992,
pp. 243-259.
5Urban, D.L., Griffin D., Ruff, G.A., Cleary, T., Yang, J., Mulholland, G., Yuan, Z.G., "Detection of Smoke from
Microgravity Fires", 2005 International Conference on Environmental Systems, Rome Italy, Paper # 2005-01-2930 July 2005,
SAE Transactions, pp 375-384.
6Ruff, G.A., D.L. Urban, and M.K. King, "A Research Plan for Fire Prevention Detection and Suppression," AIAA-2005-
0341, 43rd Aerospace Sciences Meeting and Exhibit, Reno, NV, January 9-12, 2005.
7Cleary, T.G., D W. Weinert, and G.W. Mulholland, "Moment Method for Obtaining Particle Size Measures of Test
Smokes", Natl. Inst. Stand. Technol., NISTIR 7050, 2003.
8Raabe, O.G., J. Aerosol Sci., Vol. 2, 1971, p. 289.
9Reist, P.C., Introduction to Aerosol Science, Macmillan Pub. Co., NY, NY, 1984.
10Mulholland, G.W. and Liu, B.Y.H., 1980. Response of Smoke Detectors to Monodisperse Aerosols, J. Research of the
National Bureau of Standards, 85:223-238.
11Urban, D.L. Ruff, G.A., Mulholland, G.W., Cleary, T.G., Yang, J.C., Yuan, Z.G., "Measurement of Smoke Particle Size
under Low-Gravity Conditions," 2008 International Conference on Environmental Systems, Chicago, IL, Paper 2008-01-2089.


7
American Institute of Aeronautics and Astronautics


1. -7




1. -8




Appendix D


2008-01-2089


## Measurement of Smoke Particle Size under Low-Gravity Conditions


Copyright © 2008 SAE International


## David L. Urban, Gary A. Ruff


NASA Glenn Research Center


## George W. Mulholland


University of Maryland


## Thomas G. Cleary, Jiann C. Yang


National Institute of Standards and Technology


## Zengguang Yuan


National Center for Space Exploration Research


## ABSTRACT


Smoke detection experiments were conducted in the
Microgravity Science Glovebox (MSG) on the
International Space Station (ISS) during Expedition 15 in
an experiment entitled Smoke Aerosol Measurement
Experiment (SAME). The preliminary results from these
experiments are presented. In order to simulate
detection of a prefire overheated-material event,
samples of five different materials were heated to
temperatures below the ignition point. The smoke
generation conditions were controlled to provide
repeatable sample surface temperatures and air flow
conditions. The smoke properties were measured using
particulate aerosol diagnostics that measure different
moments of the size distribution. These statistics were
combined to determine the count mean diameter which
can be used to describe the overall smoke distribution.


## INTRODUCTION


Current spacecraft fire detection systems have all been
designed based on normal gravity fire behavior and
properties. This approach was necessary given the
absence of data concerning microgravity smoke
particulate. However planned spacecraft and associated
missions outside of low earth-orbit will require increased
reliability of fire detection systems in addition to robust
false alarm resistance. Extended lunar-surface missions
will require systems that are not influenced by lunar dust
and other nuisance dust sources. The absence of
buoyant flow increases the residence time in
microgravity fires causing substantial changes in flame


D-1


structure and consequently can change the properties of
the produced smoke. In particular, the increased
residence time in the high temperature zone where the
smoke is formed, can increase the opportunity for
growth in the size of the smoke particulate.
Furthermore, the increased transit time to the detector
seen in low-gravity smoke detection scenarios [1]
provides additional time for growth in particle size
through aging or low temperature agglomeration of
smoke particles. The objective of this work is to make
sufficient measurements of smoke from spacecraft fires
to enable improved design of future detectors.


SMOKE BACKGROUND


The background in fire detection in US spacecraft is
discussed by Urban et al. [2] however some details will
be summarized here. Smoke is a general term that
encompasses aerosol materials produced by a number
of processes. In particular it can include unburned,
recondensed, original polymer or pyrolysis products that
can be either liquid or solid, hydrocarbon soot,
condensed water vapor, and ash particles. Ash and
soot particles dominate the smoke particulate in
established 1-g flaming fires while unburned pyrolysis
products and recondensed polymer fragments are
produced by smoldering and pyrolysis in the early stage
of fire growth. Given the constrained space on any
spacecraft, the target for the fire detection system is
necessarily the early phase and not established flaming
fires; consequently, the primary target for detection is
the pyrolysis products and not the soot and ash.




Urban et al. [2] reported that particulate produced by
low-gravity flames (soot or unburned fuel particles) tends
to have larger size particles than in normal gravity.
Results from the CSD (Comparative Soot Diagnostics)
Experiment


[2] which studied smoke properties in low-


gravity from several spacecraft materials suggested that
liquid smoke particles could achieve sizes larger than 1
µm while solid particulate remained in the sub-
micrometer range. The combined impact of these
limited results and theoretical predictions is that direct
knowledge of low-g combustion particulate rather than
extrapolation from 1-g data is needed for more confident
design of smoke detectors for spacecraft.


## SM SD


Figure 1: Current Spacecraft smoke detectors.
Clockwise from top left: ionization smoke detector used in the
NASA Orbiter fleet; light scattering detector used in the US
lab on the ISS; ionization detector used in the Russian ISS
Service Module; and ionization detector used in the Russian
ISS FGB Module.


In the Mercury, Gemini and Apollo missions, the crew
quarters were limited and mission durations were short,
consequently it was considered reasonable that the
astronauts would rapidly detect any fire. The Skylab
module, however, included approximately 30 UV-
sensing fire detectors [3]. The US Space Shuttle and the
Russian segments of the ISS all use ionization smoke
detectors while the US, JEM and Columbus labs of the
ISS use light scattering detectors. The systems currently
in use are shown in Figure 1.


Light scattering devices are most sensitive to particulate
whose size is of the same order as the wavelength of
the light used by the detector, typically particle diameters
greater than 0.3 μm. Ionization devices are more
sensitive to smaller particles. As reviewed by Urban et
al. [2] this difference in size sensitivity is significant for
some types of fires, consequently ionization and
scattering detectors have different performance for
normal-gravity fires. Proper implementation of smoke
detection requires understanding of the smoke particle
size distribution. Low-gravity smoke particle size data
were not available when the existing systems were
designed, consequently the designers used 1-g smoke
detector designs. These design decisions led to
detectors on the ISS and the Space Shuttle Orbiter that,
in general, have non-overlapping particle size
sensitivities.


As described by Friedman [4] there have been six
overheated electrical component events in the NASA
Orbiter fleet. None of these events spread into a real fire
but as mission durations increase, the likelihood of
failures increases. The experience on Mir in 1997 has
shown that failure of oxygen generation systems can
have significant consequences. As a result, improved
understanding of spacecraft fire detection is critically
needed. [5]


Any effort to detect fires must be able to discriminate
against the ambient background and nuisance signals.
In the case of smoke detection, the background dust
aerosol conditions must be considered. The only
spacecraft background aerosol particulate
measurements to date were made on the Orbiter on
STS-32 in 1990 [6] and on the ISS. [2] The STS
measurements reported a bimodal particle size
distribution with ~ 40% of the particles in each of the 2.5
to 10 μm and >100 μm ranges. The other two ranges
<2.5 μm and 10 to 100 μm were very lightly populated.
These results showed substantially higher
concentrations than typical indoor measurements (over
a factor of 5 for the two most populated size ranges).
The ISS results of Urban et al.


[2] were a secondary


result of an experiment to validate the operation of an
aerosol particle counter in low-gravity. The
measurements were made in the US Lab on Increment
10 and the particle count levels were at the noise level
for the instrument (less than 5 particles/cc). The low
particle levels in the < 2.5 μm bin for the STS and the
low overall numbers for the ISS suggest a zone of
opportunity for spacecraft fire detection since typical
normal gravity fires produce substantial particulate in
this size range[2,7]. However more complete particle
size statistics are needed.


## SAME EXPERIMENT CONCEPT


To date the only data on low-gravity smoke particulate
were collected by the CSD experiment[2]. The CSD data
set was not particularly large as the size statistics were
obtained from TEM data, critical details were not
obtained for the liquid droplet aerosols and the smoke
flow conditions were not well characterized. To rectify
these concerns, another experiment, the Smoke Aerosol
Measurement Experiment (SAME) was developed. The
SAME experiment sought to avoid the problems
experienced by the CSD experiment by obtaining the
particulate size statistics on-orbit with a reduced
dependence upon sample return to Earth. This is a
challenging endeavor because existing aerosol
instrumentation is typically large, incompatible with
spacecraft experiment constraints, and may require
substantial sample return to Earth. As will be described
below, an alternative approach was employed that used
three discrete instruments to measure separate
moments of the size distribution. When combined, these


1. -2




moments provide useful aggregate statistics of the size
distribution. The measurements were made using
smoke generated by overheated spacecraft materials in
much the same manner as the CSD experiment
however the sample temperature, flow field, and particle
aging time were more rigorously controlled.


## MOMENT METHOD


The approach used by the SAME experiment is termed
the 'moment method' for convenience[8]. As will be
described below, the approach consists of measuring
three moments of the size distribution (zeroth, first and
third) and using the properties of the log-normal
distribution to estimate the geometric mean diameter
and the standard deviation.


The average particle size and an estimate of the width of
the size distribution will be estimated from various
moments of the size distribution. Consider a number
distribution, fN(D), that is defined as


f (D) = (1)
N


## dN dD


where dN is the number of particles per cm3 with
diameter between D and D + dD. The moments of
interest consist of the number concentration, M0, the first
moment M1, and the volume or mass concentration
moment, M3 As defined in Eq. 2.


## Mi = ∫Di fN (D )dD i = 0,1,3 (2)


The first moment which can also be thought of as the
"diameter concentration" or integrated diameter-per-unit-
volume is approximately proportional to the signal from
an ionization smoke particulate detector. For particles in
the Mie scattering regime, particles sizes from 0.3 λ to
about 3 λ (~0.2 to 2.0 μm for a red laser) the light
scattering signal is approximately proportional to the
third moment. From these moments, and a
measurement of M0 from a condensation nuclei counter,
two mean diameters can be computed: the count
(arithmetic) mean diameter D0.5 or d , which is equal to
M1/M0 and the diameter of average mass D1.5 or d ,
m
which is equal to (M3/M0)1/3. The log-normal size
distribution is widely used for describing the size
distribution of aerosols including non-flaming smoke.
For smokes, as in most aerosols, the bulk of the number
concentration is associated with smaller particles.[9, 10]
The form of this distribution function is the same as the
normal distribution except that the diameter is replaced
with the ln D so that one has


⎛ D D 2


ln ln ⎞


⎜ ( - g ⎟ (3) )


exp -


- ⎜ ⎟ 2 ln 2σ

- ⎝ g ⎠


f D = t
N
( ) (2π )1/2D lnσ


N


g


where Nt is the total number concentration of the aerosol
(=M0), and Dg and σg are the geometric mean number
diameter and geometric standard deviation defined by


## ∞ ∞ ln Dg = ∫ ln DfN ( D)dD / f NdD


∫ (4)


0 0


1 / 2


⎤ ∞
fN ( D) dD⎥
⎦ 0


(ln ln ) 2 ( D)dD / ∫ (5)


⎡∞
⎢∫ D- Dg fN
⎣
0


lnσ =
g


For the log-normal distribution, one finds that the various
diameter definitions are related to the geometric mean
number diameter, Dg, via the equation: [9, 10]


D = D exp( p ln 2σ
p g g )


(6)


For the count mean diameter, D0.5, and the diameter of
average mass, D1.5, the corresponding values of p are
0.5 and 1.5. As an example, for a log-normal distribution
with Dg=1.0 μm and σg=2.0, the corresponding values of
D0.5 and D1.5 are 1.27 μm and 2.06 μm, respectively.
Using equation (6), one can relate σg to the ratio of D1.5
and D0.5 via the equation:


## (


g exp ln(D


1. / 0.5 ) (7)

- ) 1/ 2


## σ =


## D


In summary, by combining these three measured
moments of the size distribution, M0, M1, and M3, it is
possible to compute three mean diameters of the size
distribution, D0.5, D1.5, and Dg, and the geometric
standard deviation, σg. Validation of this approach is
discussed in Cleary, Weinert and Mulholland. [8] These
statistics provide a strong basis for design of spacecraft
smoke detectors.


## SAME EXPERIMENT DESIGN


The experiment was developed as a Microgravity
Science Glovebox (MSG) payload under the ISS
research program. A schematic of the experiment
hardware appears in Fig. 2 and an assembled
photograph in Fig. 3. Smoke was generated by
overheating a small sample of material in the smoke
generation duct for approximately 60 seconds. During
this interval, controlled flow over the sample was


1. -3 Figure 2. Schematic of the SAME hardware.




Figure 4. Photograph of a sample carousel.
Carousel contains an assortment of Teflon, Kapton, lamp
wick, and silicone rubber. The samples were supported
and heated by the same stainless steel wire coil.


Figure 3: Engineering model of the SAME hardware
installed in a MSG simulator. The sample carousel is on
the left side, the large vertical cylinder is the aging chamber
and the moment instruments are on the right side. (Clockwise
from top left): Dynamic Diluter for the zeroth moment
instrument, Commercial Diagnostics Unit A (first and third
moments), Commercial Diagnostics Unit B, Zeroth Moment
instrument. The ISS and STS smoke detectors are visible to
the left of the aging chamber.


## INSTRUMENTS


The moment measurements were made using an
assembly of three separate instruments. Two are
industrial hygiene instruments manufactured by TSI Inc.
and one is a modified residential smoke detector. The
zeroth-moment instrument is a condensation nuclei
counter P-Trak™ (TSI Inc.). This device operates by
passing the aerosol-laden particle stream through a
volume saturated with isopropanol vapor and then into a
cooler region where the vapor condenses onto the
particles raising them all to a size where they are readily
counted by a light scattering device. This instrument is
very robust and operates over a range of 0 to 105
particles/cm3 and 20 nm to 5 μm diameter. Some
dilution is required since the smoke concentration
ranges from about 0.5 × 106 to 5 × 106. There was also a
concern that the isopropanol condensate would not
return to the wick in low-gravity. [2] To mitigate this
issue, the condensing section of the device was
modified with very small grooves to improve
conductance of the condensate back to the wick. These
changes were tested in a separate space experiment
with good results indicating the modified device could be
used successfully in low gravity [2]. The device was
repackaged into an enclosure (Fig. 3) and the internal air
pump was replaced with a choked-flow orifice that
vented into the MSG vacuum resource.


induced by a moving piston in the aging chamber which
drew the smoke into the chamber. The smoke was held
in the chamber for a predetermined time, allowing the
particles to coagulate. The smoke was then pushed by
the piston into the diagnostics duct where the moment
instruments made their measurements. Also installed in
the diagnostics duct were Space Shuttle and ISS smoke
detectors. As the smoke was monitored by the moment
instruments, a sample of the smoke particles was
deposited on Transmission Electron Microscope (TEM)
grid via a thermal precipitator which uses
thermophoresis to deposit the particles on the grids.


Smoke was generated by resistively heating small
samples of spacecraft materials. Sample heating was
achieved by heating a steel wire that was wrapped
around an approximately 3mm diameter cylinder of the
sample material. The steel wire was resistively heated
and the wire resistance was monitored to control its
temperature. This technique was found to produce
repeatable weight loss from sample to sample. Groups
of six preweighed samples were installed in carousels
(Fig. 4) that the crew installed in the SAME hardware.
For each test, a new sample was moved into place and
the sample heating and the flow were synchronized to
provide a steady air stream over the sample during the
heating interval. The system was designed to provide
air flow rates ranging from 2 to 8 cm/s. To emulate a
variety of fire scenarios, tests were conducted at
different sample temperatures, air flow rates, and smoke
aging durations. Five material were tested, Teflon™,
Kapton™, silicone rubber, lamp wick (cellulose) and a
reference material (dibutyl phthalate).


The first and third moment instruments were packaged
together in a single enclosure and two of these
combined enclosures were used simultaneously during
SAME operations. The first-moment instrument is the
ionization chamber from a residential smoke detector
which uses an alpha-particle emitter to generate ions in
a region inside a DC electric field. The sensor measures
the voltage of a reference electrode inside this field. The
presence of particulate changes the charge distribution
(and thereby the reference electrode voltage) as a result
of the attachment of the ions to the particulate. The


1. -4




required particle concentrations are on the order of 105
particles / cm3 and no sample dilution was required. The
sensor was enclosed in a chamber through which the
smoke was drawn at a controlled velocity by the MSG
vacuum resource.


The third-moment instrument is a light scattering device
DustTrak™ (TSI Inc.). The device uses a 90 degree
light scattering signal to quantify the aerosol mass
density. For terrestrial dust particulate this signal
correlates well with the mass concentration, however
additional compensation will be needed to account for
the range of particle sizes that will be seen in the SAME
experiment. The device operating range is from 0.001 to
100 mg /m3. These devices are equipped with an
aerodynamic impactor at the inlet which captures
particles larger than the selected size. The SAME
experiment included 2 DustTraks™ in separate
enclosures. This made it possible to use one with a 1
μm impactor and one with a 10 µm impactor. The
difference in the signal from these two devices provides
a measure of the fraction of the particulate that was
larger than 1 µm. In some cases dilution was required
owing to the high smoke concentration levels.


As the aging chamber is filled and as the aerosol is
pushed out to the moment instruments, a small aerosol
stream is drawn off to the thermal precipitator, (Fig. 5).
Inside the precipitator, the aerosol passes between a
Transmission Electron Microscope (TEM) grid and a
heated wire. Thermophoretic forces move particles to
the grid surface where they adhere. After the mission
the grids are removed from the assembly and examined
in a TEM to obtain an independent determination of the
particle size and morphology.


The smoke in the diagnostics duct is also sampled by an
ISS smoke detector and a Space Shuttle smoke detector
at the same time the moment instruments are making
their measurements. These instruments are visible in
Figure 3.


## EXPERIMENTAL RESULTS


## Air Flow


## Heated Wire


## TEM Grid


Figure 5: Thermal Precipitator Module. Top image is a
photograph of a partially disassembled Thermal Precipitator
Module with the inlet manifold exposed on the left, the hot wire
leads in the red Vespel block in the middle and the outlet
valves on the right. The drawing below displays the position of
the hot wire above the TEM grid with the air flow passing over
both. The heated wire drives aerosol particles onto the grid via
thermophoresis.


DustTrak instruments, indicating that the bulk of the
aerosol mass is in particles below 1 μm. The effect of
aging is shown in Fig. 9 where, consistent with particle
coagulation with limited wall loss, the overall number
count (Ptrak) decreases substantially while the mass
concentrations (DustTraks) remain relatively steady.


The system was installed in the Microgravity Science
Glovebox, an ISS facility that provides many resources
including: containment, power, data, video and uplink
commanding. The hardware is shown installed in the
MSG in Fig 6. Overall 30 sample materials were tested.
These were comprised of six samples each of 5
materials: Teflon™, Kapton™, silicone rubber, cellulose,
and dibutyl-phthalate deposited on a porous wick. These
samples were tested at different airflow rates, pyrolysis
temperatures, and smoke aging durations. The analog
signals from the diagnostics were digitized at 1 Hz.
Figure 7 contains the signal traces from a typical run for
silicone rubber. The difference in the signals for the two
DustTrak's indicates that a substantial portion of the
aerosol mass is in particles that are larger than 1 μm.
For comparison, Fig. 8 contains similar data for a Teflon
run where little difference is evident between the two


Figure 6: SAME Experiment installed in the MSG
Facility.


1. -5




ISSDetectorScatterMeasurement(Volts)
IonDetectorBMeasurement(Volts)
PTrakMeasurement(PtPerCC)/1000 (right scale)
DustTrakAMeasurement(MgPerM3) (right scale)
DustTrakBMeasurement(MgPerM3) (right scale)


## Silicone Run 24 GMT 267


ISSDetectorScatterMeasurement(Volts)


## GMT 267 Silicone Run 23


STSDetectorMeasurement(Volts)


7


130


IonDetectorBMeasurement(Volts) 80
PTrakMeasurement(PtPerCC)/1000 (right)
DustTrakAMeasurement(MgPerM3) (right) 70
DustTrakBMeasurement(MgPerM3) (right)


8


7


110


6


6


60


90


5


5


50


70


4


4


40


50


3


3


30


30


2


2


20


10


1


1


10


-10


0
5100


6100


5900


5700


5500


5300


6300


6500


0
375


0


75


125


175


## Time (sec)


225


275


325


Figure 7: Instrument traces for a typical silicone
rubber run. Base levels are at the beginning and end of
the trace. The actual sampling interval is between 125 and
160 seconds. The differences in the rise times of each
instrument are due to the smoke transit time to the
instrument. The large difference between DustTrak A and
DustTrak B is indicative of the substantial portion of the
particle distribution that is larger than 1μm (the cutoff for the
impactor on DustTrak A).


Figure 9: Instrument traces for a typical smoke
aging run for silicone rubber. Base levels are at the
beginning and end of the trace. The first sampling interval is
between 5200 and 5250 seconds and the post aging
sampling interval is between 6000 and 6050 seconds.
Consistent with particle coagulation with limited wall loss, the
overall number count (Ptrak) decreases substantially while
the mass concentrations (DustTraks) remain relatively
steady.


## Teflon Test 25 GMT 268


7


80


70


6


60


5


50


4


40


30


3


20


2


10


1


0


0
73975


-10


74275


74025


74075


74125
Time (Seconds)


74175


74225


Figure 8: Instrument traces for a typical Teflon run.
Base levels are at the beginning and end of the trace. The
actual sampling interval is between 74025 and 74060
seconds. The small difference between DustTrak A and
DustTrak B is indicative that the most of the particle
distribution is smaller than 1μm (the cutoff for the impactor
on Dust Trak A).


ISSDetectorScatterMeasurement(Volts)
STSDetectorMeasurement(Volts)
IonDetectorBMeasurement(Volts)
PTrakMeasurement(PtPerCC/1000) (right)
DustTrakAMeasurement(MgPerM3) (right)
DustTrakBMeasurement(MgPerM3) (right)


It is also interesting to compare the response of the ISS
and STS detectors for silicone rubber and Teflon. In
figure 7, both the ISS detector and the STS detectors
show strong signals. (Note that the presence of smoke
yields a positive deflection of the ISS signal and a
negative deflection on the STS signal.) This is
reasonable given the broader size distribution for
silicone smoke containing significant numbers of both
large and small particles. For the Teflon smoke
comprised primarily of particles having diameters less
than 1 micron as shown in figure 9, the STS detector
provided a strong signal. Conversely, the signal from the
ISS detector was more erratic. This will be re-visited
after considering the preliminary data from the moment
instruments.


1. -6


At this time the samples and TEM grids have been
received back from the ISS; TEM and mass loss
analyses have been initiated but not completed.
Validation of the instrument calibration is underway and
ground-based comparison (1-g) runs are being
conducted. The zeroth and first moment instruments
have a limited dependence on particle diameter so they
may be directly calibrated. The third moment instrument
(the DustTrak™) has a significant dependence on both
the particle diameter and refractive index. An algorithm
has been implemented to use the results of a Mie
scattering calculation with the measured results to
iteratively converge on the value of the third moment that
best fits the DustTrak™ signal and the other two
moment measurements. This third moment value will be
used to compute the geometric mean diameters and
standard deviations.


Average values of the count mean diameter for all of the
unaged results for each material are tabulated in Table 1
along with the ratio of the signal from the two DustTraks.
Recall that the impactor used in DustTrak A removed
particles greater than approximately 1 micron; the
impactor for DustTrak B removed particles greater than
about 10 microns (although few particles greater than 10
microns should be present in these conditions). Although
the count mean diameters are all in the 100 to 200 nm
range, interpreting particle sizes by only one statistic can
be deceptive due to the nature of the particle size
distribution. In general, since the mass increases with
the cube of the diameter, the larger particles do not
affect the count mean diameter (CMD) as much as they
affect the light scattering signal which scales with the
particle mass. Consequently, although the CMD for
silicone rubber is 227 nm, almost half the particle mass
is larger than 1000 nm, as evidenced by the ratio of the
DustTrak instruments. The lamp wick showed similar
behavior.




<table>
 <tr>
  <th>Material</th>
  <th>Count Mean<br/>Diameter (nm)</th>
  <th>Ratio of<br/>B/DustTrak A</th>
 </tr>
 <tr>
  <td>Silicone Rubber</td>
  <td>227</td>
  <td>1.92</td>
 </tr>
 <tr>
  <td>Teflon™</td>
  <td>158</td>
  <td>1.22</td>
 </tr>
 <tr>
  <td>Lamp wick</td>
  <td>172</td>
  <td>1.79</td>
 </tr>
 <tr>
  <td>Kapton™</td>
  <td>128</td>
  <td>1.26</td>
 </tr>
</table>


Table 1: Average Count Mean Diameters and
ratios of the Dust Trak instruments. Dust Trak A had
a 1 μm cutoff impactor while the cutoff for DustTrak B was
10 μm.


On the other hand, the Kapton and Teflon showed
substantially narrower particle size distributions with little
mass in particles larger than 1000 nm. These low
populations of larger particles are consistent with the
less effective detection by light scattering devices which
was seen for some of the Teflon tests and with the
signals obtained from the STS and ISS detectors. All of
the tests conducted in this series of experiments showed
strong signals on the Space Shuttle detector (ionization)
despite the larger particle size distributions seen for the
lamp wick(cellulose) and silicone rubber. The CSD
experiment [2] reported poor detection by the Space
Shuttle detector for nonflaming overheat of cellulose and
silicone rubber (indicating larger particle sizes). The
reduced signal on the Space Shuttle detector for CSD
suggests that under some reasonable pre-fire conditions
the smoke size distribution can extend to diameters
beyond those seen in the SAME experiment. The
detection of smoke across the size range seen in SAME
and CSD, while still discriminating against dust (which
tends to be large) will probably require a detection
system that can discriminate the particle size distribution
to at least a limited degree. Two effective means of
achieving this size discrimination are to employ a
detector that measures more than one moment of the
size distribution or to use a detector that can classify the
particles into size ranges.


## CONCLUSIONS


The SAME experiment operated successfully on the ISS
during Increment 15. The preliminary results from the
experiments indicate that substantial differences in the
size distributions of the smoke particles are evident for
the four materials that were tested. For the conditions of
the SAME experiment, all samples produced significant
numbers of sub-micron particulate that are better
detected using an ionization smoke detector.
Considering the results from both the SAME and CSD
experiments, the only two fire detection experiments
conducted in low-gravity, broader smoke particulate size
distributions can be produced from credible pre-fire
overheat events, depending on the conditions. These
results suggest that detection methods that can measure
more than one moment of the size distribution may show


D-7


more successful detection and alarm rejection than
single moment detectors.


## ACKNOWLEDGMENTS


The support of the SAME experiment team and the
crews of ISS increments 10, 13, and 15 are gratefully
acknowledged. The SAME project was conducted
through the ISS Exploration Research Project of the
Exploration Technology Development Program. The
support of this program is also acknowledged.


Certain commercial entities, equipment, or materials
may be identified in this document in order to describe
an experimental procedure or concept adequately. Such
identification is not intended to imply recommendation or
endorsement by the National Aeronautics and Space
Administration or the National Institute of Standards and
Technology, nor is it intended to imply that the entities,
materials, or equipment are necessarily the best
available for the purpose.


## REFERENCES


1. Brooker, J. E., Urban, D.L., Ruff, G.A., "ISS Destiny Laboratory Smoke Detection Model", 07ICES-113, 2007 International Conference on Environmental Systems, Chicago, Ill. July 2007.

2. Urban, D.L., Griffin D., Ruff, G.A., Cleary, T., Yang, J., Mulholland, G., Yuan, Z.G., "Detection of Smoke from Microgravity Fires", 2005 International Conference on Environmental Systems, Rome Italy, Paper # 2005-01-2930 July 2005, SAE Transactions, pp 375-384. 3. Friedman, R., "Fire Safety Practices and Needs in Human-Crew Spacecraft," Journal of Applied Fire Science, Vol. 2, 1992, pp. 243-259. 4. Friedman, R., "Risks and Issues in Fire Safety on the Space Station," NASA TM 106430, 1994. 5. Ruff, G.A., D.L. Urban, and M.K. King, "A Research Plan for Fire Prevention Detection and Suppression," AIAA-2005-0341, 43rd Aerospace Sciences Meeting and Exhibit, Reno, NV, January 9- 12, 2005. 6. Liu, B. Y. H., K. L. Rubow, P. H. McMurry, T. J. Kotz and D. Russo, "Airborne Particulate Matter and Spacecraft Internal Environments," SAE Technical Paper 911476, 21st International Conference on Environmental Systems, San Francisco, CA , July 15-18, 1991. 7. Bukowski, R. W, R. D. Peacock, J. D. Averill, T. G. Cleary, N. P. Bryner, W. D. Walton, P. A. Reneke, and E. D. Kuligowski, "Performance of Home Smoke Alarms, Analysis of the Response of Several Available Technologies in Residential Fire Settings," NIST Technical Note 1455, December 2003. 8. Cleary, T.G., D W. Weinert, and G.W. Mulholland, "Moment Method for Obtaining Particle Size Measures of Test Smokes", Natl. Inst. Stand. Technol., NISTIR 7050, 2003.




1. Raabe, O.G., J. Aerosol Sci., Vol. 2, 1971, p. 289. 10. Reist, P.C., Introduction to Aerosol Science, Macmillan Pub. Co., NY, NY, 1984.


## ACRONYNMS


CMD: Count Mean Diameter


CSD: Comparative Soot Diagnostics


DAFT: Dust Aerosol measurement Feasibility Test


ISS: International Space Station


MSG: Microgravity Science Glovebox


SAME: Smoke Aerosol Measurement Experiment


STS: Space Transportation System


TEM: Transmission Electron Microscope


1. -8




### Appendix E


#### Spacecraft Fire Detection: Smoke Properties and Transport in Low-Gravity


David L. Urban1, Gary A. Ruff2 and John E. Brooker3,
NASA Glenn Research Center, Cleveland, Ohio 44135


Thomas Cleary4 and Jiann Yang5
National Institute of Standards and Technology, Gaithersburg, Maryland 20899


George Mulholland6
The University of Maryland, College Park, Maryland 20742


and


Zeng-guang Yuan7
National Center for Space Exploration Research, Cleveland, Ohio 44135


Results from a recent smoke particle size measurement experiment conducted on the
International Space Station (ISS) are presented along with the results from a model of the
transport of smoke in the ISS. The experimental results show that, for the materials tested,
a substantial portion of the smoke particles are below 500 nm in diameter. The smoke
transport model demonstrated that mixing dominates the smoke transport and that
consequently detection times are longer than in normal gravity.


## I. Introduction


he absence of buoyant flow increases the residence time in microgravity fires causing substantial changes in
Tflame structure and consequently changes the properties of the produced smoke. In particular, the increased
residence time in the high temperature zone where the smoke is formed, can increase the opportunity for growth in
the size of the smoke particulate. However, no measurements of the properties of smoke from microgravity fires
had been made at the time when the detectors were designed for both the space shuttle and the ISS. This absence of
data caused the designers to base the design on 1-g information and the current state of the art. As a result, the two
detectors were designed using different detection technologies which have very different particle size sensitivities.
The objective of this work was to make sufficient measurements of smoke from spacecraft fires to enable improved
design of future detectors.


## A. Smoke Background


Smoke is a general term that encompasses aerosol materials produced by a number of processes. In particular it
can include unburned, recondensed, original polymer or pyrolysis products that can be either liquid or solid,
hydrocarbon soot, condensed water vapor, and ash particles. Ash and soot particles dominate the smoke particulate
in established flaming fires while unburned pyrolysis products and recondensed polymer fragments are produced by
smoldering and pyrolysis in the early stage of fire growth. Given the constrained space on any spacecraft, the target


1 Branch Chief, Combustion and Reacting Systems Branch, 21000 Brookpark Road, MS 77-5, Senior Member.
2 Advanced Capabilities Project Office, 21000 Brookpark Road, MS 77-7, Associate Fellow.
3 Aerospace Engineer, Combustion and Reacting Systems Branch, 21000 Brookpark Road, MS 77-5.
4 Integrated Performance Assessment Group Leader, 100 Bureau Drive, Stop 8664.
5 Fire Metrology Group Leader, 100 Bureau Drive, Stop 8662.
6 Visiting Professor of Mechanical Engineering, Glenn L. Martin Hall.
7 Staff Scientist, 21000 Brookpark Road, MS 77-5.


1
American Institute of Aeronautics and Astronautics


1. -1




for the fire detection system is necessarily the early phase and not established flaming fires; consequently, the
primary target for detection is the pyrolysis products and not the soot and ash.


## B. Prior Spacecraft Systems


In the Mercury, Gemini and Apollo missions, the crew quarters were limited and mission durations were short,
consequently it was considered reasonable that the astronauts would rapidly detect any fire. The Skylab module,
however, included approximately 30 UV-sensing fire detectors.1 These devices were limited to line-of-sight and
were reported to have difficulties with false alarms.


## C. Space Shuttle Detectors


At the time the Space Shuttle Orbiter (Space Transportation System (STS)) was developed, smoke detection for
terrestrial applications was becoming commonplace.2 In particular, ionization detectors were becoming readily
available but photoelectric (scattering or obscuration detectors) were generally unavailable due to the difficulty of
producing stable light sources. There was no data available concerning the smoke or dust particle size distribution
in low-gravity and the database of normal-
gravity smoke characteristics was a fraction of
what is available today. Consequently, the
STS smoke detector (Fig. 1) employed a
variant of the accepted ground based approach
(ionization detectors). The Orbiter has nine
particle-ionization smoke detectors in avionics
cooling air return lines in the mid-deck and
flight deck and SpaceLab had six additional
particle-ionization smoke detectors in the
avionics lines.3 While the design rationale is
not completely known, Celesco™ (later
Brunswick Defense™) based their design on
data that suggested incipient fires could be
discriminated by looking for particulate in the
0.4 to 0.7 μm range.4 Use of a pump provided
the opportunity to employ a particle separator
allowing rejection of particulate larger than
1μm. This air pump increased the power
requirements and reduced the operational life Figure 1. Brunswick Defense™ smoke detector used in the
for the detectors. NASA Orbiter fleet. The inlet is on the right and the gas is
expelled out the small plate on the top.


D. ISS Detectors
The International Space Station (ISS) smoke detector design took advantage of the availability of stable laser-


diode light sources, mirroring a trend in terrestrial detectors toward light scattering devices. This provided the
opportunity to produce a detector that required substantially less power, (1.5 Watts versus 9 Watts for the Orbiter
detector)5 and, with no moving parts, was quieter with a much longer operational life. The choice was supported by
data indicating that early smoldering fires produce larger particulate than established flaming fires.2 The designated
detectors (Fig. 2) for the ISS are laser-diode, forward-scattering, smoke or particulate detectors. Their sensitivity is
greatest for particles larger than 1 μm with sensitivity extending down to 0.6 μm. The current requirements for the
ISS call for two detectors in the open area of the US Lab module, and detectors in racks that have cooling air-flow.6
The design developed for the ISS by Allied Signal™ (Fig. 2) consists of a 2-pass laser diode to sense forward
scattered light (30 degrees). There is also a zero degree obscuration system that is used as a measure of the beam
strength. The system is designed to alarm based on the magnitude of the scattered light signal referenced to the
beam intensity. The system is less sensitive to particles smaller than the wavelength of the laser (near IR) than it is
to larger particles. The minimum reported sensitivity is 0.3 μm.5 On the other hand, for a fixed mass concentration
of smoke aerosol; the STS ionization smoke detector is more sensitive to smaller particle sizes.


2
American Institute of Aeronautics and Astronautics


1. -2




As a result of these design decisions, the
ISS and the Orbiter detectors are sensitive to
particles in different size ranges. In both
cases the designs were based upon the best
available data however, due to the complete
absence of low-g data concerning the nature
of particulate and radiant emission from
incipient and fully developed low-g fires,
different conclusions were drawn
concerning the optimal design for spacecraft
fire detection.
As described by Friedman7 there have
been six overheat and failed component
failures in the NASA Orbiter fleet. None of
these events spread into a real fire but as
mission durations increase, the likelihood of
failures increases. The experience on Mir in
1997 has shown that failure of oxygen
generation systems can have significant
consequences. As a result, improved
understanding of spacecraft fire detection is
critically needed.8 Figure 2. Allied Signal/Honeywell light-scattering smoke


detector used in the ISS. The near IR laser beam emerges


E. Background in Low Gravity Smoke from the enclosure into the top assembly (A) and is reflected
The salient result on smoke particle size by two mirrors (one visible at top right (B)) and is then


determination in low-gravity reported by reflected back to the sensors in the enclosure (C). One sensor
Urban et al.9 is that particulate produced by detects the forward scattered light and is referenced by
low-gravity flames (soot or unburned fuel another sensor that looks directly at the incident beam.
particles) tends to have larger size particles
than in normal gravity. Results from the
CSD (Comparative Soot Diagnostics) Experiment9 which studied smoke properties in low-gravity from several
spacecraft materials suggested that liquid smoke particles could achieve sizes larger than 1 µm while solid
particulate remained in the sub-micrometer range. The combined impact of these limited results and theoretical
predictions is that, as opposed to extrapolation from 1-g data, direct knowledge of low-g combustion particulate is
needed for more confident design of smoke detectors for spacecraft.


## F. Spacecraft Atmosphere Dust Background


Any effort to detect fires must be able to discriminate against the ambient background and nuisance signals. In
the case of smoke detection, the background dust aerosol conditions must be considered. The only spacecraft
background aerosol particulate measurements to date were made on the Orbiter on STS 32 in 199010 and on the ISS.9
The STS measurements included the results from two cascade impactors and a light scattering device. The two
impactors reported a bimodal particle size distribution with ~ 40% of the particles in each of the 2.5 to10 μm and
>100 μm ranges. The other two ranges < 2.5 μm and 10 to 100 μm were very lightly populated. Each impactor
sampled approximately 15 m3 of air over approximately 30 hours. These results showed substantially higher
concentrations than typical indoor measurements (over a factor of 5 for the two most populated size ranges). These
data were supported by the light scattering instrument which made 17 measurements in 12 locations, all of these
reported mass concentrations ranging from 50 to 70 μg/m3. The ISS results of Urban et al.9 were a secondary result
of an experiment to validate the operation of an aerosol particle counter in low-gravity. The measurements were
made in the US Lab on Increment 10 and the particle count levels were at the noise level for the instrument (less
than 5 particles/cc). The low particle levels in the < 2.5 μm bin for the STS and the low overall numbers for the ISS
suggest a zone of opportunity for spacecraft fire detection since typical normal gravity fires produce substantial
particulate in this size range.2,11 However more complete particle size statistics are needed.


3
American Institute of Aeronautics and Astronautics


1. -3




### II. SAME Experiment


Although the CSD experiment produced useful information concerning the likely size of spacecraft smoke
particulate, the data set was not particularly large as the size statistics were obtained from TEM data and critical
details were not obtained for the liquid droplet aerosols. To rectify this concern, another experiment (Smoke
Aerosol Measurement Experiment: SAME) was developed. The SAME experiment sought to avoid the problems
experienced by the CSD experiment by obtaining the particulate size statistics on-orbit with a reduced dependence
upon sample return to Earth. This is a challenging endeavor because existing aerosol instrumentation is typically
large, incompatible with spacecraft experiment constraints, and may require substantial sample return to Earth. As
will be described below, an alternative approach was employed that used three discrete instruments to measure
separate moments of the size distribution. When combined, these moments provide useful aggregate statistics of the
size distribution. The measurements were made using smoke generated by overheated spacecraft materials in much
the same manner as the CSD experiment however the sample temperature, flow field, and particle aging time were
more rigorously controlled.


## A. Moment Method


The approach used by the SAME experiment is termed the 'moment method' for convenience.12 As will be
described below, the approach consists of measuring three moments of the size distribution (zeroth, first and third)
and using the properties of the log-normal distribution to estimate the geometric mean diameter and the standard
deviation.
The average particle size and an estimate of the width of the size distribution will be estimated from various
moments of the size distribution. The number distribution, fN(D), is defined as


## fN (D)  (1)


## dN dD


where dN is the number of particles per cm3 with diameter between D and D + dD. The moments of interest consist
of the number concentration, M0, the first moment M1, and the volume or mass concentration moment, M3.


## Mi  Di fN (D )dD i  0,1,3 (2)


The first moment which can also be thought of as the "diameter concentration" or integrated diameter per unit
volume is approximately proportional to the ionization detector moment (signal). For particles in the Mie scattering
regime, particles sizes from 0.3 to about 3 (~0.2 to 2.0 μm for a red laser) the light scattering signal is
approximately proportional to the third moment. From these moments, and a measurement of M0 using a
condensation nucleus counter, two mean diameters can be computed: the count (arithmetic) mean diameter D0.5
d , which is equal to (M
or d , which is equal to M1/M0 and the diameter of average mass D1.5 or m 3/M0)1/3. The log-
normal size distribution is widely used for describing the size distribution of aerosols including non-flaming smoke.
As in most aerosols; the bulk of the number concentration is associated with smaller particles.13, 14 The form of the
distribution is the same as the normal distribution except that the diameter is replaced with the ln D so that one has


 D D  
 g 
2
ln ln
2ln2 
g 


t
N
2 1/2D ln
( )


- 

- 


exp






N
f (D)


(3)


## 


g


where Nt is the total number concentration of the aerosol (=M0), and Dg and g are the geometric mean number
diameter and geometric standard deviation defined by


##  / NdD (4)


##   ln Dg   ln Df N( D)dD f


0 0


4
American Institute of Aeronautics and Astronautics


1. -4




1/ 2


 
fN ( D) dD 
 0




g   (ln D ln Dg )2 fN ( D)dD /


0


ln


(5)


For the log-normal distribution, one finds that the various diameter definitions are related to the geometric mean
number diameter, Dg, via the equation:13, 14


p ) (6)


## D  D


p 
g exp( ln2 g


For the count mean diameter, D0.5, and the diameter of average mass, D1.5, the corresponding values of p are 0.5
and 1.5. As an example, for a log-normal distribution with Dg=1.0 m and g=2.0, the corresponding values of D0.5
and D1.5 are1.27 m and 2.06 m, respectively. Using equation (6), one can relate g to the ratio of D1.5 and D0.5 via
the equation:


1.5 / D0.5) (7)


## 


g exp ln(D


1 / 2


##  


By combining these three moments it is possible to compute three mean diameters of the size distribution and the
geometric standard deviation. Validation of this approach is discussed in Cleary, Weinert and Mulholland.3 These
statistics provide a strong basis for design of spacecraft smoke detectors.


## B. Instruments


These measurements were made using an assembly of three separate instruments. Two are industrial hygiene
instruments manufactured by TSI and one is a modified residential smoke detector.
The zeroth-moment instrument is a condensation nuclei counter P-Trak™ (TSI Inc.). This device operates by
passing the aerosol-laden particle stream through a region where it is saturated with isopropanol vapor and then into
a cooler region where the vapor condenses onto the particles raising them all to a size where they are readily counted
by a light scattering device. This instrument is very robust and operates over a range of 0 to 105 particles/cm3 and
20 nm to 1 μm diameter. Some dilution is required since the smoke concentration ranges from about 0.5 × 106 to 5


× 106. There was also a concern that the isopropanol condensate would not return to the wick in low-gravity.9 To


mitigate this issue, the condensing section of the device was modified with very small grooves to improve
conductance of the condensate back to the wick. These changes were tested in a separate space experiment with
good results indicating the modified device could be used successfully in low gravity.9
The first-moment instrument is the ionization chamber from a residential smoke detector which uses an alpha-
particle emitter to generate ions in a region inside a DC electric field which causes the ions to drift producing
current. The presence of particulate reduces the current as a result of the attachment of the ions to the particulate.
The mobility of the charged aerosol is too small for it to be collected on the ionization chamber electrode. The
required particle concentrations are on the order of 105 particles / cm3 and no sample dilution was required.
The third-moment instrument is a light scattering device DustTrak™ (TSI Inc.). The device uses a 90 degree
light scattering signal to quantify the aerosol mass density. For terrestrial dust particulate this signal correlates well
with the mass concentration, however additional compensation will be needed to account for the range of particle
sizes that will be seen in the SAME experiment. The device operating range is from 0.001 to 100 mg /m3. These
devices are equipped with an aerodynamic impactor at the inlet which captures particles larger than the selected size.
The SAME experiment included 2 DustTraks™ one with a 1 μm impactor and one with a 10 μm impactor. The
difference in the signal from these two devices provided a measure of the fraction of the particulate that was larger
than 1 μm. In some cases dilution was required owing to the high smoke concentration levels.


A schematic of the assembled hardware appears in Fig. 3. Smoke was generated by overheating a small sample
of material in the smoke generation duct for approximately 60 seconds. During this interval, controlled flow was
induced by a moving piston in the aging chamber which drew the smoke into the chamber. The smoke was held in
the chamber for a predetermined time, allowing the particles to coagulate. The smoke was then pushed by the piston
into the diagnostics duct where the moment instruments made their measurements. Also installed in the diagnostics
duct were space shuttle and ISS smoke detectors. As the smoke was monitored by the moment instruments, a


5
American Institute of Aeronautics and Astronautics


1. -5




sample of the smoke particles was
deposited on Transmission Electron
Microscope (TEM) grid via a thermal
precipitator which uses thermophoresis to
deposit the particles on the grids.


## C. Experimental Results


The system was installed in the
Microgravity Science Glovebox, an ISS
facility that provides many resources
including: containment, power, data, video
and uplink commanding. The assembled
hardware is shown in Fig 4. Overall 30
sample materials were tested. These were Figure 3. Schematic of the SAME hardware.
comprised of six samples each of 5
materials: Teflon™, Kapton™, silicone rubber, cellulose, and dibutyl-phthalate deposited on a porous wick. These
samples were tested at different airflow rates, pyrolysis temperatures, and smoke aging durations. The analog
signals from the diagnostics were digitized at 1
Hz. At this time the used samples and TEM
grids have just been received back from the ISS
so mass-balances and TEM analysis have not
been initiated. The zeroth and first moment
instruments have a limited dependence of
particle diameter so they may be directly
calibrated. The third moment instrument (the
DustTrak™) has a significant dependence on
the particle diameter and the refractive index.
An algorithm has been implemented to use the
results of a Mie Scattering calculation with the
measured results to iteratively converge on the
value of the third moment that best fits the
DustTrak™ signal and the other two moment
measurements. This work is currently
underway so only results from the zeroth and Figure 4. SAME Experiment installed in the MSG Facility
first moment instruments will be presented
here. As discussed above, the ratio of the first to the zeroth moment is the count mean diameter (D0.5). Values of
D0.5 were calculated directly from the calibrated signals from the P-Trak and the Ion sensor and are shown in Table 1
for the baseline runs of the 4 solid materials with the
percentage increase over the sizes from a comparable test in Count
normal gravity. Count
Mean Diameter
Material Mean


III. Smoke Transport Model Diameter (nm) (% larger than
1-g)


To assist in the interpretation of the SAME results and to Silicone
263 53
provide a further understanding of the implementation of Rubber
smoke detectors in spacecraft applications, a numerical model
of the smoke transport and detection in the Destiny Laboratory
Teflon™ 223
(US Lab) of the ISS was developed. The details of the model
are discussed by Brooker et al.15 This study was conducted
using FDS (Fire Dynamics Simulator) a fire modeling Lamp wick 248 65
program developed by McGrattan et al.16,17 at NIST. FDS
(version 4.0.7 Linux) is a computational fluid dynamics (CFD)
model that numerically solves a form of the Navier-Stokes Kapton™ 114 58
equations for low speed, thermally driven flow with an
emphasis on smoke and heat transport from fires.16 A detailed Table 1: Count Mean Diameters for Baseline
description of the theoretical equations, underlying Runs with comparison to 1-g tests.


6
American Institute of Aeronautics and Astronautics


1. -6




assumptions, and numerical solution can be found in the technical reference guide.17 For this application, large eddy
simulation (LES) was utilized in which the large scale eddies are computed directly and the sub-grid scale
dissipative processes are modeled. Since the ISS is in low earth orbit, the gravitational acceleration was set to zero.
As a result, the vorticity generated by buoyancy is no longer present in the momentum equation; therefore, the
baroclinic torque was included to account for other sources of vorticity. A mixture fraction combustion model (a
conserved quantity representing the fraction of material at a given point that originated in the fuel stream) was
utilized for this analysis. All solid surfaces were designated as inert with a thermal boundary condition of 293 K.
The number of grid cells
spanning each coordinate
direction was determined such
that the cell dimension was
approximately 5 cm in length for
a total of 259,200 cells. The
model layout is shown in Fig 5.
The smoke generation was
modeled using a source
positioned at the center of each
Figure 5. Computational Model Domain showing six overhead supply
rack location or ISPR diffusers, six deck return registers, and one aft-port IMV diffuser for air
(International Standard Payload ventilation. Induced flow patterns are indicated with dashed lines. Two
Rack). The source was modeled area smoke detectors are located in front of LAP1 return register
as a propane burner with an area (LAP1RR) and LAS5 return register (LAS5RR). Also shown are
of 0.023 m2 and heat flux of 57.6 internal obstructions representing on-orbit equipment and a smoke
kW/m2 at three soot yield levels, source at LAP3. ISPR sections are numbered one through six (fwd to
producing smoke particulate aft) and labeled: port (P), starboard (S), nadir (N), or zenith (Z).
outputs of 1.46, 2.95, and 8.47
mg/s. The alarm point for the ISS
detector is on the order of 0.5 mg/m3. The computational model was run at each smoke generation rate and rack
location. The flow conditions in the lab were established to duplicate the operation of the ventilation system on
orbit. The return and diffuser vanes are
oriented to create an overall toroidal
flow field that rotates counterclockwise
(looking forward). Axial flow is
induced near the floor on the port side
by the Inter Module Ventilation (IMV)
register on the aft bulkhead. For smoke
generation locations at sections 5 and 6,
the simulations were also run with and
without the internal obstructions shown
in Fig. 5. These internal obstructions Figure 6: Representation of the smoke distribution 177 seconds
were positioned to simulate typical after the smoke source was activated at location 4 on the floor.
installed hardware in the US Lab The smoke generation rate was 8.5 mg/s.
Module. The smoke source was
activated 30 seconds after the simulation was initiated and the simulations were run for an additional 300 seconds.
Figure 6 presents a reconstruction of the smoke distribution for an 8.5 mg/s generation rate case after 177 seconds.
It is notable that other than the high concentration zone near the source, the smoke is fairly well mixed throughout
the region without obstructions. The region with obstructions has lower smoke levels than the rest of the module.
This scenario is substantially different from that seen in normal gravity where the smoke concentrates near the
ceiling and mixing is generally not as complete as seen in Fig. 6.
Figures 7, 8 and 9 show the alarm time response for sources at Section LA1 (Fig. 7), LA3 (Fig. 8) and LA6
(Fig.9). Evident in the figures is the variation in detection times with soot yield and source location. Although for
LA3, for the zenith smoke source, the detectors alarmed at the same time, overall one detector typically alarmed
significantly sooner than the other, particularly at low smoke yield levels. For LA1and LA3, the port detector was
the first to alarm in most cases while by LA6 the starboard detector was the first to alarm. This behavior is
consistent with the relative proximity of the detectors to the smoke sources. In Fig. 9, the impact of the obstructions
is evident. For sources on the floor, the obstruction had no effect. This is consistent with expectation since the


7
American Institute of Aeronautics and Astronautics


1. -7




floors are unobstructed and the flow is across the floor toward the detector. For cases on the starboard or zenith, the
obstructions had a strong impact due to the longer transit time of the smoke to the detector.


Figure 7 (left) and 8 (right): Smoke detector alarm time response to a variable strength smoke source.
Data is from a circumferential profile at section LA1 (Fig. 7) and LA3 (Fig. 8). Note that a DNA (did not
alarm) condition occurred for LA1 for the 0.05 soot yield on the N1 wall for LAS5RR and for LA3 0.05
soot yield on the S3 wall for LAP1RR.


## IV. Conclusion


Smoke particulate produced in low-gravity was found
to be typically 50% large in count mean diameter than
similar conditions in normal gravity. The resultant sizes
were all below 300 nm suggesting that discriminating
smoke from spacecraft dust possibly could be achieved by
detecting in the sub-micrometer range. Numerical
modeling of smoke transport in the US Lab Module of the
ISS predicted that actual detection times can be quite long
and strongly dependent on location and the presence of
obstructions.


Figure 9. Smoke detector alarm time response
variable strength smoke source. Data is
circumferential profile at section LA6.
DNA (did not alarm) condition
0.05 soot yield on the S6, Z6,
LAP1RR, and S6 and Z6 walls
lines and symbols: with
dashed lines and open
8
Aeronautics and Astronautics


E-8


to a
from a
Note that a
occurred for the
and N6 walls for
for LAS5RR. Solid
internal obstructions,
symbols: no obstructions.


American Institute of




### V. Acknowledgments


The support of the SAME experiment team and the crews of ISS increments 10, 13, and 15 are gratefully
acknowledged. The SAME project was conducted through the ISS Exploration Research Project of the Exploration
Technology Development Program. The support of this program is also acknowledged.
Certain commercial entities, equipment, or materials may be identified in this document in order to describe an
experimental procedure or concept adequately. Such identification is not intended to imply recommendation or
endorsement by the National Aeronautics and Space Administration or the National Institute of Standards and
Technology, nor is it intended to imply that the entities, materials, or equipment are necessarily the best available for
the purpose.


## VI. References


1Friedman, R., "Fire Safety Practices and Needs in Human-Crew Spacecraft," Journal of Applied Fire Science, Vol. 2, 1992,
pp. 243-259.
2Bukowski, R.W. and G.W. Mulholland, "Smoke Detector Design and Smoke Properties," NBS Technical Note 973, 1978.
3Martin, C.E. and R.C. DaLee, "Spacecraft Fire Detection and Suppression (FDS) Systems: An Overview and
Recommendations for Future Flights," SAE Technical Paper 932166, 23rd International Conference on Environmental Systems,
Colorado Springs, CO, July 12-15, 1993.
4National Research Council, Fire Detection for Life Safety, National Academy of Sciences, Washington D.C., 1975.
5Steisslinger, H. R., D. M. Hoy, J. A. McLin and E. C. Thomas, SAE Paper 932291, 19th International Conference on
Environmental System, 1993.
6McKinnie, J., "Fire Response Aboard the International Space Station," SAE Technical Paper 972334, 27th International
Conference on Environmental Systems, Lake Tahoe, NV, July 14-17, 1997.
7Friedman, R., "Risks and Issues in Fire Safety on the Space Station," NASA TM 106430, 1994.
8Ruff, G.A., D.L. Urban, and M.K. King, "A Research Plan for Fire Prevention Detection and Suppression," AIAA-2005-
0341, 43rd Aerospace Sciences Meeting and Exhibit, Reno, NV, January 9-12, 2005.
9Urban, D.L., Griffin D., Ruff, G.A., Cleary, T., Yang, J., Mulholland, G., Yuan, Z.G., "Detection of Smoke from
Microgravity Fires", 2005 International Conference on Environmental Systems, Rome Italy, Paper # 2005-01-2930 July 2005,
SAE Transactions, pp 375-384.
10Liu, B. Y. H., K. L. Rubow, P. H. McMurry, T. J. Kotz and D. Russo, "Airborne Particulate Matter and Spacecraft Internal
Environments," SAE Technical Paper 911476, 21st International Conference on Environmental Systems, San Francisco, CA ,
July 15-18, 1991.
11Bukowski, R. W, R. D. Peacock, J. D. Averill, T. G. Cleary, N. P. Bryner, W. D. Walton, P. A. Reneke, and E. D.
Kuligowski, "Performance of Home Smoke Alarms, Analysis of the Response of Several Available Technologies in Residential
Fire Settings," NIST Technical Note 1455, December 2003.
12Cleary, T.G., D W. Weinert, and G.W. Mulholland, "Moment Method for Obtaining Particle Size Measures of Test
Smokes", Natl. Inst. Stand. Technol., NISTIR 7050, 2003.
13Raabe, O.G., J. Aerosol Sci., Vol. 2, 1971, p. 289.
14Reist, P.C., Introduction to Aerosol Science, Macmillan Pub. Co., NY, NY, 1984.
15Brooker, J. E., Urban, D.L., Ruff, G.A., "ISS Destiny Laboratory Smoke Detection Model", 07ICES-113, 2007
International Conference on Environmental Systems, Chicago, Ill. July 2007.
16K.B. McGrattan and G.P. Forney. "Fire Dynamics Simulator (Version 4) User Guide". NIST Special Publication 1019,
National Institute of Standards and Technology, Gaithersburg, Maryland, March 2006.
17K.B. McGrattan (editor). "Fire Dynamics Simulator (Version 4) Technical Reference Guide". NIST Special Publication
1018, National Institute of Standards and Technology, Gaithersburg, Maryland, March 2006.


9
American Institute of Aeronautics and Astronautics


1. -9




1. -10


