

NASA/TP-2015-216046


# Detailed Results From the Flame Extinguishment Experiment (FLEX) March 2009 to December 2011


Daniel L. Dietrich
Glenn Research Center, Cleveland, Ohio


Paul V. Ferkul, Victoria M. Bryg, and M. Vedha Nayagam
National Center for Space Exploration Research, Glenn Research Center, Cleveland, Ohio


Michael C. Hicks
Glenn Research Center, Cleveland, Ohio


Forman A. Williams
University of California, San Diego, La Jolla, California


Frederick L. Dryer
Princeton University, Princeton, New Jersey


Benjamin D. Shaw
University of California, Davis, Davis, California


Mun Y. Choi
University of Connecticut, Storrs, Connecticut


C. Thomas Avedisian


Cornell University, Ithaca, New York


November 2015




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




NASA/TP-2015-216046


# Detailed Results From the Flame Extinguishment Experiment (FLEX) March 2009 to December 2011


Daniel L. Dietrich
Glenn Research Center, Cleveland, Ohio


Paul V. Ferkul, Victoria M. Bryg, and M. Vedha Nayagam
National Center for Space Exploration Research, Glenn Research Center, Cleveland, Ohio


Michael C. Hicks
Glenn Research Center, Cleveland, Ohio


Forman A. Williams
University of California, San Diego, La Jolla, California


Frederick L. Dryer
Princeton University, Princeton, New Jersey


Benjamin D. Shaw
University of California, Davis, Davis, California


Mun Y. Choi
University of Connecticut, Storrs, Connecticut


C. Thomas Avedisian


Cornell University, Ithaca, New York


National Aeronautics and
Space Administration


Glenn Research Center
Cleveland, Ohio 44135


November 2015




Trade names and trademarks are used in this report for identification
only. Their usage does not constitute an official endorsement,
either expressed or implied, by the National Aeronautics and
Space Administration.


Level of Review: This material has been technically reviewed by expert reviewer(s).


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




## Contents


Executive Summary ................................................................................................................................................... 1


1. Introduction ....................................................................................................................................................... 2

2. Experiment Setup .............................................................................................................................................. 2 2.1 Experimental Hardware ........................................................................................................................... 2 2.2 Experiment Diagnostics ........................................................................................................................... 4 2.3 Experimental Procedures ......................................................................................................................... 4 2.4 Experiment Data Downlink and Format .................................................................................................. 7

3. Data Analysis .................................................................................................................................................... 7 3.1 HiBMS Image Analysis ........................................................................................................................... 7 3.1.1 Procedure ...................................................................................................................................... 7 3.1.2 Error Analysis ............................................................................................................................... 8 3.2 LLUV Image Analysis ............................................................................................................................. 8 3.2.1 Procedure ..................................................................................................................................... 8 3.2.2 Error Analysis ............................................................................................................................... 8 3.3 Multi-User Droplet Combustion Apparatus Color Camera Analysis ...................................................... 9 3.3.1 Procedure ...................................................................................................................................... 9 3.3.2 Error Analysis ............................................................................................................................... 9

4. Experimental Results ........................................................................................................................................ 9 4.1 Test Matrix-March 2009 through December 2011 ................................................................................ 9 4.2 Analyzed Data ....................................................................................................................................... 16

5. Observations and Discussion .......................................................................................................................... 16 5.1 General Observations ............................................................................................................................. 16 5.2 Fuel Needle Contamination ................................................................................................................... 16

6. Conclusions ..................................................................................................................................................... 17


Appendix A.-Detailed Experimental Results ....................................................................................................... 19


1. Summary Data ..................................................................................................................................... 19


A.2 Experiment Results ................................................................................................................................ 20


Appendix B.-Droplet and Flame Sizes ................................................................................................................ 29
References .............................................................................................................................................................. 305


NASA/TP-2015-216046 iii






### Detailed Results From the Flame Extinguishment Experiment (FLEX) March 2009 to December 2011


Daniel L. Dietrich
National Aeronautics and Space Administration
Glenn Research Center
Cleveland, Ohio 44135


Paul V. Ferkul, Victoria M. Bryg, and M. Vedha Nayagam
National Center for Space Exploration Research
Glenn Research Center
Cleveland, Ohio 44135


Michael C. Hicks
National Aeronautics and Space Administration
Glenn Research Center
Cleveland, Ohio 44135


Forman A. Williams
University of California, San Diego
La Jolla, California 92093


Frederick L. Dryer
Princeton University
Princeton, New Jersey 08544


Benjamin D. Shaw
University of California, Davis
Davis, California 95616


Mun Y. Choi
University of Connecticut
Storrs, Connecticut 06269


C. Thomas Avedisian
Cornell University


Ithaca, New York 14853


#### Executive Summary


The Flame Extinguishment Experiment (FLEX) program
is a continuing set of experiments on droplet combustion,
performed employing the Multi-User Droplet Combustion
Apparatus (MDCA), inside the chamber of the Combustion
Integrated Rack (CIR), which is located in the Destiny module
of the International Space Station (ISS). This report describes
the experimental hardware, the diagnostic equipment, the
experimental procedures, and the methods of data analysis for
FLEX. It also presents the results of the first 284 tests
performed. The intent is not to interpret the experimental results
but rather to make them available to the entire scientific
community for possible future interpretations.
The apparatus for the FLEX experiments was transported to
the ISS and installed late in 2009. It includes canisters for fuel


storage, two opposed-needle syringes for injecting fuel to form
a droplet, two opposed hot-wire igniters for initiating combus-
tion, and a long, fine fiber that can be used to tether the droplet
and move it at a programmable low velocity through the gas in
the chamber. The combustion history is recorded photograph-
ically, with a visible-light color camera that views the entire
field, a backlit camera that highlights the droplet to determine
its diameter accurately as a function of time during burning, and
a camera with a filter centered at 310 nm, intended to record
emissions from excited hydroxyl radicals produced in the flame
(Low Light Level Ultra-Violet, LLUV), thereby providing a
measure of the flame diameter. Although the ISS crew must
change the fuel canisters and the gas bottles needed to establish
the atmosphere in the combustion chamber, each droplet-
burning experiment is run remotely from the Telescience
Support Center at the NASA Glenn Research Center in


NASA/TP-2015-216046 1




Cleveland, Ohio. During periodically scheduled experiment
intervals, about 4 to 10 droplets are burned in this remote
operation, with use made mainly of the color camera to guide
the procedure, which involves a number of manual steps.
In addressing the experimental procedures and data analysis,
this report details the methods, data downlink, and format, and
it provides error estimates. The results include histories of
droplet diameters obtained from the backlit camera and
histories of flame diameters obtained from both the hydroxyl-
filter camera and the color camera. Both flame diameter
measurements are of the outer edge of the flame, and the
diameters in the color-camera images are the smaller of the two,
approximately three-fourths of the LLUV results. Average
burning-rate constants for each burn also are reported, as are
extinction diameters, for the cases where the flame extinguished
at a finite droplet size. Both radiative and diffusive extinctions
occurred during the testing.
The fuels studied in these experiments were methanol and


n-heptane. The droplets had initial diameters between 2 and


5 mm, and they were burned in oxidizing atmospheres at ambient
temperature and various pressures between 0.70 and 3.05 atm,
over ranges of dilution of oxygen with nitrogen, with carbon
dioxide, and with mixtures thereof. Most of the tests were
conducted at pressures between 0.7 and 1 atm, and many of the
tests were in air. A principle objective was to determine the
limiting oxygen index (LOI), the oxygen percentage below which
combustion would not occur. This objective reflected the FLEX
focus on investigating fire safety in spacecraft. Observed LOI
values for these fuels appear to be slightly lower than initially
expected. Besides documenting both radiative extinction at
higher dilutions and diffusive extinctions at lower dilutions for
both fuels, the results exhibited disruptive extinctions and
provided information pertinent to soot production for heptane.
The continuing experiments are providing additional data for
these two fuels, as well as droplet-combustion data for other
fuels, and NASA intends to catalog these data in similar reports.


#### 1.0 Introduction


The spherically symmetrical combustion of a liquid fuel
droplet in a quiescent ambient gaseous oxidizing atmosphere
is a classical problem in combustion research, having been
addressed first more than 50 years ago by Godsave (1952),
Hall and Diederichsen (1953), and Spalding (1952, 1953).
Numerous reviews of the subject are now available in the
literature, among them those of Wise and Agoston (1958),
Williams (1973), Faeth (1977), Law (1982), Sirignano (1983),
and Choi and Dryer (2001). An advantage of spherical sym-
metry is that only one spatial dimension enters the description
of the combustion process, so that one-dimensional (spherically
symmetrical) time-dependent conservation equations apply.
This greatly facilitates both computational and theoretical


descriptions of the problem, thereby enhancing understanding
of experimental results, which becomes much more difficult,
uncertain, and inaccurate in multidimensional situations.
Natural convection, however, destroys the spherical symmetry
of combustion in normal gravity, as was quite evident in the
earliest experiments of Hall and Diederichsen (1953) and
Goldsmith (1956). Kumagai and Isoda (1956) were the first to
realize that microgravity experiments afforded the opportunity
to achieve spherical symmetry-a fact that NASA has taken
advantage of in fundamental combustion investigations for a
number of years (Williams, 1981; Dietrich et al., 1996;
Nayagam et al., 1998).
The Flame Extinguishment Experiment (FLEX) is a droplet
combustion experiment performed on the International Space
Station (ISS). FLEX is the first experiment in the multipurpose
facility developed at the NASA Glenn Research Center-the
Combustion Integrated Rack (CIR). The CIR provides the
combustion chamber, most of the diagnostics, the gas-
mixing system, and the primary interface between the ISS and
the ground controllers at Glenn. The Multi-User Droplet
Combustion Apparatus (MDCA) is the hardware that deploys
and ignites the liquid fuel droplets and provides some of the
diagnostics. The MDCA is located in the CIR combustion
chamber, but it communicates through the CIR to ground
controllers at Glenn.
The purpose of this report is to detail and permanently
archive the results of a subset of the FLEX experiments, namely
those occurring between March 2009 and the end of December
2011. It is not intended to interpret the data from those experi-
ments or to draw any scientific conclusions; that will occur
through future NASA reports and peer-reviewed journal articles
that reference this report. The next section provides a brief
description of the experimental hardware and test procedures.
This is followed by a section that provides details of the data
analysis. The last two sections provide details of the
experimental results.


#### 2.0 Experiment Setup


The FLEX experiments are conducted on the ISS in the
combustion chamber of the CIR facility-a multipurpose
facility dedicated to combustion experiments. The CIR, a large
rack-level experiment in the Destiny module, was developed at
Glenn. The FLEX experiments were the first experiments to be
conducted in the CIR.


#### 2.1 Experimental Hardware


The CIR facility (Fig. 1), described in detail elsewhere (Banu,
2008), consists of a 90-liter combustion chamber that can
operate at pressures of approximately 0 to 9 atm. Although the
chamber can operate at a working pressure of 9 atm, the
maximum pressure for a given experiment is frequently much


NASA/TP-2015-216046 2




Figure 2.-Multi-User Droplet Combustion Apparatus
(MDCA) with hardware installed in the Combustion
Integrated Rack (CIR).


Figure 1.-Astronaut Mike Fincke to the left of the
Combustion Integrated Rack (CIR) facility shortly after
it was installed in the Destiny module of the
International Space Station (ISS).


less than that depending on a rigorous (and very conservative)
safety analysis. For the FLEX experiments, this analysis
reduced the maximum working pressures to approximately
3 atm. The interior of the CIR chamber contains the
mechanical, fluid, and electrical interfaces necessary to mount
experiment-specific hardware inside the chamber.
The CIR facility can accurately control the ambient environ-
ment inside the chamber. This capability is provided by the Fuel
and Oxidizer Mixing Apparatus (FOMA). The FOMA consists
of gas bottles, a connection for ISS nitrogen connected through
a series of valves, pressure transducers, and mass flow
controllers to the combustion chamber. The contents of the
chamber can be evacuated via a vacuum pump connected to the
ISS overboard vent.
The hardware for the FLEX experiments, the MDCA, is
pictured in Figure 2 and shown schematically in Figure 3. The
MDCA facility, which is described in detail elsewhere (Robbins
and Shinn, 2010), is based on the design of the space shuttle
Droplet Combustion Experiment (DCE, Nayagam et al., 1998).


Figure 3.-Multi-User Droplet Combustion Apparatus
(MDCA) looking down from the top, with hardware
installed in the Combustion Integrated Rack (CIR).


The MDCA can deploy both free and fiber-supported droplets
in a quiescent microgravity environment.
Stainless-steel tubes with 250-µm outside diameters and
specially treated ends are used for the deployment. Each needle
is connected via flexible Teflon (DuPont) tubing to a fuel
reservoir, or cartridge, which consists of a gas-tight syringe
connected to a remotely actuated, gas-tight solenoid valve. The
crew can easily replace the two reservoirs mounted in the
MDCA during nominal operations. For the experiments
reported herein, each reservoir contained one of the experiment
fuels-heptane or methanol. The amount of fuel put in the
syringe was a function of the detailed safety analysis, approxi-
mately 2.5 ml for methanol and 1.25 ml for heptane.


NASA/TP-2015-216046 3




During each FLEX test, the syringe assembly dispensed the
fluid between the horizontally opposed needles. The needles
then slowly stretched to a distance slightly smaller than the
distance where the fluid would pull off one of the needles. Just
before ignition, the needles rapidly retracted, ideally leaving a
motionless droplet floating in the middle of the CIR combustion
chamber.
Once the needles retracted, the control computer energized
two hot-wire igniters located 180° to each other and in the same
plane as the deployment needles. After a preset time, the control
computer deenergized the igniters and activated the linear
motors to retract them away from the droplet.
The MDCA also performed tests with fiber-supported drop-
lets, either for cases where the drift velocity of the droplets
exceeded values acceptable to the science team or for tests
where the science team wished to examine the effect of a
subbuoyant convective flow on the combustion process. For
fiber-supported tests, the procedure was exactly the same,
except that the droplets were deployed on a small 80-µm
support fiber. For tests with translation, after ignition, the
control computer translated the fiber (in the direction parallel to
the orientation of the fiber) at a prescribed speed and for a
prescribed time duration.


#### 2.2 Experiment Diagnostics


The primary diagnostics for the FLEX experiment were
provided by the CIR facility and are described in detail
elsewhere (Banu, 2008). They included a backlit view of the
droplet and an orthogonal view of the flame. The illumination
for the backlit view was a laser diode source and a collimating
optical system. They provided monochromatic illumination
with a center wavelength between 650 to 660 nm. The laser
diode operated below the lasing threshold current and thus acted
as a noncoherent illumination source. The image system for the
backlit view was the High-Bit-Depth Multispectral (HiBMs)
imaging package. The HiBMs package had a telemetric imag-
ing optical system and a high-resolution 12-bit output digital
camera.
Almost all of the tests reported herein1 used the full 1024 by
1024 array with a fixed field of view (FOV) of approximately
30 mm on a side. The images used the full 12-bit output and a
framing rate of approximately 30 frames per second (fps). The
HiBMs package, when used in conjunction with the illumi-
nation package, can measure the droplet size as a function of
time and the soot volume fraction for soot-producing flames


(i.e., heptane for the tests described in this report).
The CIR also provided a LLUV package to image the


chemiluminescence from hydroxyl (OH•) emissions from the


1The exception is the first few "engineering" test points that used ISS
cabin air as the ambient. The primary purpose of these tests was an
engineering evaluation of the integrated hardware. These tests used a
camera configuration that was slightly different.


burning droplet. The LLUV package was a 1024 by 1024
monochrome frame-transfer charged-coupled device (CCD)
array with 12-bit digital imaging capability. The CCD array was
directly coupled to an 18-mm Gen II-UV microchannel plate
intensifier to provide maximum response at short wavelengths.
The intensifier included intensifier and gating control that
allowed varied exposure times depending on the expected
brightness of the flames. The LLUV also had a spectral notch
filter integrated to image the chemiluminescence at 310 nm (the
filter had a 10-nm full width at half maximum (FWHM)
bandwidth). Ground control of the LLUV enabled pretest setting
of the gain, pixel binning, and gate to optimally image the flames
surrounding the droplets. All of the tests reported herein used the
2 by 2 binned (512 by 512) array with a fixed FOV of approxi-
mately 50 mm on a side. The framing rate for the majority of the
tests was 30 fps, with a smaller number at 15 fps as an attempt to
improve flame contrast for very dim flames. The intensifier gain
did vary somewhat over the tests in this report.
The MDCA provided two diagnostics: a color camera and
radiometers. The color camera provided a visual overview of
the FLEX experiments. This camera view was augmented with
illumination from a white-light-emitting diode (LED) located
on the MDCA inside the CIR chamber. This camera had a zoom
lens that provided a closeup view of the needles and droplet
during droplet formation. The white LED was turned on at this
time to allow the operator to see the droplet formation process.
Immediately prior to droplet deployment and ignition, the
camera zoomed out and the white LED turned off to provide an
overview of the combustion process. The FOV of this camera
was approximately 110 by 90 mm. This view, which provided
flame size, shape, and color information, was downlinked to the
ground during nominal test point operations.
The MDCA provided two radiometers: a broadband radiom-
eter to detect the total radiative output of the flame and a
radiometer with a filter to examine the emission from the water
vapor. For the tests reported herein, these radiometers were not
sensitive enough to provide reliable quantitative information
about flame radiometric output, so the data are not reported. A
replacement radiometer package will be available for future
FLEX tests.


#### 2.3 Experimental Procedures


During nominal operations, there was very little crew
involvement in the FLEX experiments. The FLEX experiments
required crew time to replace gas bottles, fuel reservoirs, and
fiber assemblies during nominal operations. Crew time also was
required during malfunction operations to diagnose hardware
and replace damaged components. Finally, immediately prior to


NASA/TP-2015-216046 4




test-point operations, the crew removed the alignment guides to
the Passive Rack Isolation System (PaRIS). PaRIS isolated the
CIR from the lower level, higher frequency vibrations or g-jitter
of the ISS to provide a cleaner gravitational environment for
the FLEX experiments. The CIR rack had accelerometer heads
to monitor the gravitational (g) and vibrational environment
during testing. For all of the experiments in this report, the


g-environment was low enough that buoyant flow could be


considered to be negligible; however, g-jitter was evident when
the droplet began to move in a particular direction and potentially
out of the camera FOV (particularly with the HiBMs).
Once the fuel reservoirs and gas bottles were in place and the
alignment guides removed, the test operations began. Personnel
at the Telescience Support Center (TSC) at Glenn controlled all
functions of the FLEX experiments. Test-point operations typi-
cally required three operators, two controlling the functions of
the CIR, and one dedicated to the MDCA. In addition, for most
tests a representative of the science team was present to help
make any necessary real-time decisions regarding the testing.
The sequence for test-point operations follows:


(1) Activate the CIR. The CIR operators activated the rack


and performed all housekeeping necessary for test-point
operations.


(2) Operate the FOMA. The CIR operators operated the


FOMA to fill the CIR chamber to the appropriate ambient
pressure and gas composition. During these operations, the CIR
and ground computers recorded in detail the pressure history
during the fill and evacuation procedures so that the actual
chamber composition could be computed a posteriori.


(3) Activate the MDCA. Once the ambient environment


was set, the MDCA was activated. The MDCA console operator
at the TSC then performed all necessary housekeeping on the
MDCA to prepare for test-point operations. All commands to
and from the MDCA passed through the CIR computers.


(4) Open the fuel valve and purge line. Typically, all the


fuel in the fuel lines between the reservoir and needle tip had
evaporated. The MDCA operator then slowly dispensed fuel
(advances the linear stepper motor attached to the fuel syringe
containing the fuel) until fuel visually appeared from the fuel
needle.


(5) Perform the test-point operation.
(a) Dispense the fuel droplet. The MDCA operator


slowly dispensed fuel to form a droplet of the appropriate
size. In theory, the operator could just advance the stepper
motor the theoretical amount to dispense the fuel volume for
a given droplet size. In practice, however, the MDCA
operator used the stepper motor counts as a guide and
estimated the appropriate droplet size (with consultation from


the science team). The needles were together at this point,
and the dispensed fuel bridged the small gap between the
needles.


(b) Stretch the fuel droplet. The MDCA operator


slowly moved the needles apart to a distance slightly smaller
than that where the fuel would spontaneously pull off. This
distance was a function of the fuel type and fuel volume and
was performed manually according to the judgment of the
MDCA operator.


(c) Burn the droplet. The MDCA computer could per-


form steps (1) to (5)(b) in a preprogrammed manner. Early
testing, however, showed that manual operation was more
efficient. Consequently, for these tests, once the droplet had
the appropriate stretch, the MDCA operator zoomed out the
color camera, turned off the illumination from the LED (the
backlight for the HiBMs, however, remained on), and turned
over control to the MDCA onboard computer. The MDCA
computer then performed the following steps in a rapid
progression:


(i) Start data recording. The CIR HiBMs and


LLUV and the MDCA color camera began recording
images.


(ii) Deploy the droplet. The needles were rapidly


and simultaneously retracted.


(iii) Ignite the droplet. The small hot-wire igniters


located nearly orthogonal to the deployment needles and
close to the droplet (a ground-controllable distance) were
turned on for a preset time and power level (a ground-
controllable voltage).


(iv) Retract the igniter. The igniters were turned


off and rapidly retracted a relatively large distance from
the droplet.


(v) Stop data recording. The CIR and MDCA


cameras stopped recording data after a preset time
(typically on the order of 40 s).


(6) Conduct posttest operations. The CIR and MDCA


operators then performed a number of housekeeping operations
to prepare for the next test-point operations (if necessary). If
another test was to be performed in the same ambient
environment, the circulation fan located in the chamber was
turned on for a brief period of time (approximately 1 min) to
mix the gases uniformly inside the chamber.


Figure 4 shows sequence (1) to (6) as recorded by the HiBMs,
LLUV, and MDCA color cameras. Figure 4(a) (HiBMs and
MDCA color cameras only) shows the droplet stretched
between the fuel needles just before the automated sequence
was run. Figure 4(b) (HiBMs only) shows the droplet
immediately after the deployment needles had retracted. The


NASA/TP-2015-216046 5




Figure 4.-Test sequence as recorded by the High-Bit-Depth Multispectral (HiBMs) (left), Low Light Level Ultra-Violet
(LLUV) (center), and Multi-User Droplet Combustion Apparatus (MDCA) color (right) cameras. The chamber
illumination for the MDCA color camera turns off when the needles retract. The sequence shows (from top to bottom)
the droplet stretched between the needles, droplet deployment, ignition, and an image during the burn. This test is a
heptane droplet burning in a cabin air (0.21/0.79 O2/N2 mole fraction), 1.0-atm ambient environment. Each row of
images is from the same instant of time. Missing images for the LLUV and MDCA color cameras are dark-field
images.


NASA/TP-2015-216046 6




droplet in this image is misshaped by the needle retraction but
assumes the expected spherical shape within approximately 1 s.
Figure 4(c) shows the views from all three cameras during
ignition.
Given the large size of the CIR chamber and the need to
minimize resource utilization, the chamber atmosphere was
frequently reused. The ambient atmosphere in this report was
that computed from the downlink from the pressure and tem-
perature data during the FOMA operations and corrected for the
fuel vaporized, oxygen consumed, and carbon dioxide and
water vapor produced during test-point operations.


#### 2.4 Experiment Data Downlink and Format


The CIR diagnostics systems can store the camera data for
several on-orbit tests. The exact number depends on the length
of recording, the recording format (binned versus unbinned on
the cameras), and other factors. Typically after one or two test-
point days, there is a dedicated time to transfer the data between
CIR computers and then downlink the image data from the ISS
to ground computers at the NASA Johnson Space Center. From
Johnson, the data are eventually transferred to the servers at the
TSC at Glenn. This process typically takes approximately 24 hr
for three to six test points. The data from the CIR cameras is
compressed, and once at the TSC, the CIR staff decompresses
and transfers the raw data to the science team.
The data transferred to the FLEX science team for analysis
consist of a number of text files that contain the following
information:


(1) HiBMs camera settings
(2) LLUV camera settings
(3) MDCA color camera settings (two files)
(4) CIR chamber and pressure data
(5) Radiometer data
(6) CIR facility settings
(7) MDCA settings
(8) Test comments for any anomalies encountered (e.g.,
missing data) during the acquisition, transfer, and
downlink process


In addition, there are text files for each camera that include
the image number, the image name, and the time of acquisition
for each camera image. Each frame from the HiBMs and LLUV
cameras is stored as a 12-bit tagged-image file format (TIFF)
image, and each frame from the color camera is stored as a
bitmap (BMP) image.
This represents a large amount of data, much of it
unnecessary for scientific analysis of the FLEX data. For this
report, the FLEX science team extracted a small subset of the
total downlinked data-only that which was important for
scientific analysis.


3.0 Data Analysis
The three camera views are the primary data for the FLEX


experiments. The backlit HiBMs view of the droplet provides
the droplet size and droplet dynamics as a function of time. This
camera operated at full resolution (1024 by 1024 pixels) and
30 fps for all but the first few tests documented in this report.
The images provided to the FLEX team are 12-bit grayscale
images scaled to 16-bit images. The droplet appears as a dark
object on a light background. The images from this view also
allow the determination of the soot volume fraction surrounding
the droplet for tests that produce soot. Those data are not
detailed in this report, but will be available elsewhere (e.g., Suh
et al., 2011).
The LLUV view provides the flame chemiluminescence from
OH• as a function of time. The viewing window for the LLUV
camera became dirty or smudged early in the FLEX testing. For
the majority of tests in this report, this contamination showed
up as asymmetries in the LLUV view. This coupled with the
very dim flames added to the uncertainty in the flame meas-
urements. The flame sizes documented in this report are the
dimensions of the flame directly from the TIFF images. No
effort was made to perform the deconvolution to determine the
peak radial location of OH• chemiluminescence (e.g., Marchese
et al., 1996) because of the asymmetrical noisy images that
resulted from the smudged window.
The color camera provided a direct view of the combustion
process. This view provided the size and dynamics of the visual
flame as a function of time. The following subsections provide
detailed descriptions of the analysis of each view.


#### 3.1 HiBMS Image Analysis 3.1.1 Procedure


The images were analyzed in a semiautomatic manner by
using the commercially available image-processing packages,
Image J (National Institutes of Health, 2011) or Igor Pro
(http://www.wavemetrics.com). Analysis of the HiBMs images
proceeded as follows:


(1) Determine which frames to analyze. The droplets were


typically deployed with some residual velocity. In addition,


g-jitter caused the droplet to drift. In a significant number of


tests, the droplet drifted out of the HiBMs FOV (and sometimes
back into the FOV) before recording stops. This stage involved
identifying the frames where the droplet was within the FOV.


1. Crop the image to limit the region to analyze.

2. Despeckle the image to reduce noise.

3. Adjust the contrast and set the segmentation value.


This is the value that set the threshold between the background
and the object (droplet). It varied from test to test because the


NASA/TP-2015-216046 7




background intensity varied between tests. The value was set
manually to optimally distinguish between the droplet and
background for the entire test. Detailed analysis of a single test
showed that within reasonable limits the threshold value had
little impact on the droplet size and, thus, was not a major
source of error.


(5) Fill holes and manually remove stray objects. If there


was a bright spot in the middle of the droplet, this step made
that region the same average intensity as the surrounding
droplet. This step also involved manually removing stray
objects that might interfere with the droplet size measurement.


(6) Measure the area, center of mass, and perimeter of


the flame in the image. The measurement was converted to a
flame size using the appropriate scale factor (32.5 pixels/mm)
for most of the tests herein.


(7) Perform steps 2 through 6 for each image identified


in step 1.


3.1.2 Error Analysis
The error or uncertainty in the measurement of droplet
diameter comes from a few sources. The first is the spatial
resolution of the camera. The FOV for the HiBMs is 30.25 mm2.
For all but the first few tests, the HiBMs operated at full frame
(not binned), or 1024 by 1024 pixels. Therefore, the minimum
spatial resolution was ±29.5 µm.
There was additional uncertainty in estimating the appro-
priate segmentation value, especially since the background gray
level in the HiBMs view was not spatially uniform. The FLEX
science team performed extensive ground testing in the func-
tionally identical (to the CIR HiBMs on the ISS) Ground
Interface Unit (GIU) HiBMs system with precision spheres of
known size. This testing provided the guidelines for setting the
appropriate threshold (segmentation) value to determine the
edge of the droplet.
Also, it was obvious that there was noise in the image that
could contribute to the uncertainty in droplet size. The uncer-
tainty as a result of these last two sources was greatly reduced
by measuring the projected area (as opposed to a single spatial
dimension) of the droplet. As a result, we estimated the
uncertainty in the droplet size to be ±50 µm.


#### 3.2 LLUV Image Analysis 3.2.1 Procedure


The flame size is much more difficult to measure than the
droplet size. The flames are quite dim, and as a result, there is a
significant amount of noise in the LLUV images. The damage
to the window in the CIR chamber for the LLUV camera made
the noise worse for the tests in this report. There was also
ambiguity in the flame definition, the peak in flame tem-
perature, the peak in OH• emission, or the outer edge of OH•


emission. The damage to the CIR window, coupled with
the very dim images, precluded the deconvolution of the LLUV
images (e.g., Marchese et al., 1996) to get the radial distribu-
tion of the OH• chemiluminescence. The flame dimension
detailed in this report represents the outer edge of the OH•
chemiluminescence.
The image sequences were analyzed in a semiautomatic
manner using the commercially available image-processing
packages, Image J (National Institutes of Health, 2011) or Igor
Pro (http://www.wavemetrics.com). Analysis of the LLUV
images proceeded as follows.


(1) Determine which frames to analyze.
(2) Perform a gaussian blur to reduce the noise in the


image.


(3) Remove outliers. This process removed any pixel values


that were near saturation. These values were not from the flame
but were a result of the intensifier on the LLUV camera.


(4) Adjust the contrast, and set the threshold value. This


was the value that set the threshold between the background and
the object (flame). The value was manually set to optimally
distinguish between the flame and the background for an
individual image. For some tests a constant threshold value could
be used for the entire test. For others the threshold value was a
function of the flame luminosity with brighter flames using a
higher threshold value. The segmentation (threshold) value was
typically relatively low (compared with the maximum in an
image) and, therefore, represented a very dim part of the flame or
the very outer edge of the flame. The value is likely somewhat
larger than a flame diameter based on the dimension of maximum
temperature or OH• chemiluminescence.


(5) Fill holes, and manually remove stray objects. There


was a darker region inside the flame, and this "hole" was
included in the area measurement of the flame.


(6) Measure the area, center of mass, and perimeter of


the droplet in the image. The measurement was converted to
a droplet size using the appropriate scale factor (8.86 pixels/mm
for most of the tests herein).


(7) Perform steps 2 through 6 for each image identified


in step 1.


3.2.2 Error Analysis
The error or uncertainty in the measurement of flame
diameter is more difficult to determine than the droplet size
measurement. The FOV for the LLUV is 57.8 mm2. For all of


the tests in this report, the LLUV operated with 2 by 2 binning
or a resolution of 512 by 512 pixels. Therefore, the minimum
spatial resolution was ±113 µm.
There is additional uncertainty in estimating the appropriate
segmentation value. The value represents the outer edge of the


NASA/TP-2015-216046 8




flame and likely overestimates a measure based on the maxi-
mum radial intensity. Also, it is obvious that there is noise in
the image that can contribute to the uncertainty in flame size.
The uncertainty as a result of these last two sources was greatly
reduced by measuring the projected area (as opposed to a single
spatial dimension) of the flame. As a result, we estimated the
uncertainty in the flame size to be ±200 µm.


#### 3.3 Multi-User Droplet Combustion Apparatus Color Camera Analysis


3.3.1 Procedure
The procedure to measure the flame size from the MDCA


color camera was almost identical to that used on the LLUV
images. The flames were also quite dim, and as a result, there is
a significant amount of noise in the color camera images. There
also is ambiguity as to the definition of the flame. The flame
dimension detailed in this report represents the outer edge of the
visible flame.
The image sequences were analyzed in a semiautomatic
manner using the commercially available image-processing
packages, Image J (National Institutes of Health, 2011) or Igor
Pro (http://www.wavemetrics.com). The analysis used on the
MDCA color camera images follows.


1. Determine which frames to analyze.

2. Crop the image so that it contains only the flame.

3. Remove outliers. This process removed any pixel


values that were near saturation. These values were not from
the flame but were a result of the intensifier on the LLUV
camera.


(4) Adjust the contrast and set the segmentation value.


This is the value that sets the threshold between the background
and the object (flame). It was constant throughout the test but
varied from test to test. The value was set manually to optimally
distinguish between the flame and background for the entire
test. The segmentation (threshold) value was typically
relatively low and therefore represented a very dim part of the
flame or the very outer edge of the flame. The value was likely
somewhat larger than a flame diameter based on the dimension
of the maximum temperature or OH• chemiluminescence.


(5) Fill holes and manually remove stray objects. There


was a darker region inside the flame, and this "hole" was
included in the area measurement of the flame.


(6) Measure the area, center of mass, and perimeter of


the droplet in the image. The measurement was converted to
a droplet size using the appropriate scale factor (6.87 pixels/mm
for most of the tests herein).


(7) Perform steps 2 through 6 for each image identified


in step 1.


3.3.2 Error Analysis
The error or uncertainty in the measurement of the flame
diameter is more difficult to determine than the droplet size
measurement. The FOV for the LLUV is 93.2 mm wide, and
the video camera has standard National Television System
Committee (NTSC) resolution, or 640 by 480 pixels. Therefore,
the minimum spatial resolution is ±146 µm.
There is additional uncertainty in estimating the appropriate


segmentation value. The value represents the outer edge of the
flame and likely overestimates a measure based on maximum
radial intensity. Also, it is obvious that there is noise in the
image that can contribute to the uncertainty in flame size. The
uncertainty as a result of these last two sources was greatly
reduced by measuring the projected area (as opposed to a single
spatial dimension) of the flame. As a result, we estimated the
uncertainty in the flame size to be ±250 µm.


#### 4.0 Experimental Results 4.1 Test Matrix-March 2009 through December 2011


This report documents the results of the FLEX experiments
from March 2009 through December 2011. The tests were
conducted in numerical order, so there was a small amount of
accumulated carbon dioxide, water vapor, and fuel vapor.
Table I outlines the first tests, which were performed in cabin
air on the ISS. The ambient gas composition on the ISS is
nominally that of air (0.21 oxygen mole fraction, 0.005 carbon
dioxide mole fraction, balance nitrogen) at 1.0-atm pressure.
Once filled, the atmosphere was not changed for any of these
tests. These tests were not part of the nominal FLEX test
matrix, but were performed to determine the proper operation
of the CIR and MDCA integrated systems. The tests do,
however, provide scientifically relevant data, so the results are
reported in this document.
Table II provides details for the next series of tests, which were
in high-pressure, carbon-dioxide-enriched ambient environ-
ments. These tests were next in sequence in order to optimize the
use of limited on-orbit gas resources. During these tests,
however, the engineering and science teams noticed that the fuel
system did not respond well to cycling from high to low
pressures. As a result, after only a few tests were conducted in
these ambient environments, the teams decided to change the
order of the tests in the test matrix.
After the test matrix was reordered, the FLEX experiments
focused on low-pressure (≤1-atm), nitrogen-diluted, ambient
environments. Table III provides details for the initial tests,
which focused on ambient conditions with higher oxygen mole


NASA/TP-2015-216046 9




TABLE I.-FLEX TEST MATRIX FOR TESTS CONDUCTED IN CABIN AIR
[Droplet not supported by a fiber; tests conducted in ambient air-0.21 oxygen mole fraction,
0.005 carbon dioxide mole fraction, 0.79 nitrogen mole fraction (balance) at 1.0-atm pressure.]


<table>
 <tr>
  <th>Test</th>
  <th>Date</th>
  <th>Fuel</th>
  <th>Initial droplet diameter,<br/>D0,<br/>mm</th>
  <th>Pressure,<br/>P,<br/>atm</th>
 </tr>
 <tr>
  <td>001</td>
  <td>Mar. 5, 2009</td>
  <td>Methanol</td>
  <td>1.80</td>
  <td>1.00</td>
 </tr>
 <tr>
  <td>002</td>
  <td>Mar. 5, 2009</td>
  <td>Methanol</td>
  <td>2.00</td>
  <td>1.00</td>
 </tr>
 <tr>
  <td>003</td>
  <td>Mar. 5, 2009</td>
  <td>Methanol</td>
  <td>1.71</td>
  <td>1.01</td>
 </tr>
 <tr>
  <td>004</td>
  <td>Mar. 31, 2009</td>
  <td>Methanol</td>
  <td>2.19</td>
  <td>1.00</td>
 </tr>
 <tr>
  <td>005</td>
  <td>Mar. 31, 2009</td>
  <td>Methanol</td>
  <td>1.95</td>
  <td>1.00</td>
 </tr>
 <tr>
  <td>006</td>
  <td>Mar. 31, 2009</td>
  <td>Methanol</td>
  <td>2.90</td>
  <td>1.00</td>
 </tr>
 <tr>
  <td>007</td>
  <td>Apr. 10, 2009</td>
  <td>Heptane</td>
  <td>1.91</td>
  <td>1.00</td>
 </tr>
 <tr>
  <td>008</td>
  <td>Apr. 10, 2009</td>
  <td>Heptane</td>
  <td>2.89</td>
  <td>1.00</td>
 </tr>
 <tr>
  <td>009</td>
  <td>Apr. 10, 2009</td>
  <td>Heptane</td>
  <td>3.00</td>
  <td>1.00</td>
 </tr>
</table>


TABLE II.-FLEX TEST MATRIX FOR TESTS CONDUCTED IN HIGH-PRESSURE,
CARBON-DIOXIDE-ENRICHED AMBIENT ENVIRONMENTS
[Droplet not supported by a fiber; 0.21 oxygen mole fraction, 0.700 carbon
dioxide mole fraction, 0.090 nitrogen mole fraction.]


<table>
 <tr>
  <th>Test</th>
  <th>Date</th>
  <th>Fuel</th>
  <th>Initial droplet diameter,<br/>D0,<br/>mm</th>
  <th>Pressure,<br/>P,<br/>atm</th>
 </tr>
 <tr>
  <td>010</td>
  <td>May 22, 2009</td>
  <td>Methanol</td>
  <td>3.88</td>
  <td>3.05</td>
 </tr>
 <tr>
  <td>011</td>
  <td>May 22, 2009</td>
  <td>Methanol</td>
  <td>3.02</td>
  <td>3.05</td>
 </tr>
 <tr>
  <td>012</td>
  <td>May 22, 2009</td>
  <td>Heptane</td>
  <td>3.09</td>
  <td>3.05</td>
 </tr>
 <tr>
  <td>013</td>
  <td>June 25, 2009</td>
  <td>Methanol</td>
  <td>2.72</td>
  <td>2.73</td>
 </tr>
 <tr>
  <td>014</td>
  <td>June 29, 2009</td>
  <td>Methanol</td>
  <td>3.71</td>
  <td>2.70</td>
 </tr>
 <tr>
  <td>015</td>
  <td>June 29, 2009</td>
  <td>Methanol</td>
  <td>4.43</td>
  <td>2.72</td>
 </tr>
 <tr>
  <td>016</td>
  <td>June 29, 2009</td>
  <td>Methanol</td>
  <td>1.80</td>
  <td>2.73</td>
 </tr>
 <tr>
  <td>017</td>
  <td>July 1, 2009</td>
  <td>Methanol</td>
  <td>2.81</td>
  <td>2.03</td>
 </tr>
 <tr>
  <td>018</td>
  <td>July 1, 2009</td>
  <td>Heptane</td>
  <td>2.92</td>
  <td>2.04</td>
 </tr>
</table>


NASA/TP-2015-216046 10




TABLE III.-FLEX TEST MATRIX FOR THE TESTS CONDUCTED IN NITROGEN-DILUTED AMBIENT
ENVIRONMENTS, INCLUDING TESTS IN ENVIRONMENTS WITH HIGHER OXYGEN MOLE FRACTIONS


<table>
 <tr>
  <th>Test</th>
  <th>Date</th>
  <th>Fuel</th>
  <th>Initial droplet diameter,<br/>D0,<br/>mm</th>
  <th>Fiber</th>
  <th>Pressure,<br/>P,<br/>atm</th>
  <th>Mole fraction<br/>of oxygen</th>
  <th>Mole fraction<br/>of nitrogen</th>
 </tr>
 <tr>
  <td>019</td>
  <td>Aug. 26, 2009</td>
  <td>Heptane</td>
  <td>3.43</td>
  <td>No</td>
  <td>0.71</td>
  <td>0.400</td>
  <td>0.600</td>
 </tr>
 <tr>
  <td>020</td>
  <td>Oct. 24, 2009</td>
  <td>Methanol</td>
  <td>3.46</td>
  <td>No</td>
  <td>.71</td>
  <td>.400</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>021</td>
  <td>Oct. 24, 2009</td>
  <td>Methanol</td>
  <td>3.49</td>
  <td>No</td>
  <td>.71</td>
  <td>.400</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>022</td>
  <td>Oct. 24, 2009</td>
  <td>Methanol</td>
  <td>3.55</td>
  <td>No</td>
  <td>.71</td>
  <td>.400</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>023</td>
  <td>Oct. 24, 2009</td>
  <td>Heptane</td>
  <td>3.18</td>
  <td>No</td>
  <td>.71</td>
  <td>.400</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>024</td>
  <td>Oct. 24, 2009</td>
  <td>Heptane</td>
  <td>4.0</td>
  <td>No</td>
  <td>.71</td>
  <td>.400</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>025</td>
  <td>Nov. 9, 2009</td>
  <td>Methanol</td>
  <td>2.65</td>
  <td>No</td>
  <td>.71</td>
  <td>.300</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>026</td>
  <td>Nov. 9, 2009</td>
  <td>Methanol</td>
  <td>3.70</td>
  <td>No</td>
  <td>.71</td>
  <td>.300</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>027</td>
  <td>Nov. 9, 2009</td>
  <td>Heptane</td>
  <td>4.00</td>
  <td>No</td>
  <td>.71</td>
  <td>.300</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>028</td>
  <td>Nov. 9, 2009</td>
  <td>Heptane</td>
  <td>3.46</td>
  <td>No</td>
  <td>.71</td>
  <td>.300</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>029</td>
  <td>Nov. 13, 2009</td>
  <td>Methanol</td>
  <td>2.65</td>
  <td>No</td>
  <td>1.01</td>
  <td>.300</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>030</td>
  <td>Nov. 13, 2009</td>
  <td>Methanol</td>
  <td>3.32</td>
  <td>No</td>
  <td>1.01</td>
  <td>.300</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>031</td>
  <td>Nov. 13, 2009</td>
  <td>Heptane</td>
  <td>3.51</td>
  <td>No</td>
  <td>1.01</td>
  <td>.300</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>032</td>
  <td>Nov. 13, 2009</td>
  <td>Heptane</td>
  <td>3.08</td>
  <td>No</td>
  <td>1.01</td>
  <td>.300</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>037</td>
  <td>Jan. 7, 2010</td>
  <td>Methanol</td>
  <td>3.41</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.337</td>
  <td>.662</td>
 </tr>
 <tr>
  <td>038</td>
  <td>Jan. 7, 2010</td>
  <td>Methanol</td>
  <td>3.51</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.337</td>
  <td>.661</td>
 </tr>
 <tr>
  <td>039</td>
  <td>Jan. 7, 2010</td>
  <td>Heptane</td>
  <td>2.91</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.336</td>
  <td>.661</td>
 </tr>
 <tr>
  <td>040</td>
  <td>Jan. 8, 2010</td>
  <td>Methanol</td>
  <td>3.77</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.297</td>
  <td>.699</td>
 </tr>
 <tr>
  <td>041</td>
  <td>Jan. 8, 2010</td>
  <td>Methanol</td>
  <td>3.33</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.297</td>
  <td>.699</td>
 </tr>
 <tr>
  <td>042</td>
  <td>Jan. 8, 2010</td>
  <td>Heptane</td>
  <td>3.02</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.298</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>043</td>
  <td>Jan. 8, 2010</td>
  <td>Heptane</td>
  <td>3.02</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.298</td>
  <td>.700</td>
 </tr>
 <tr>
  <td>044</td>
  <td>Jan. 11, 2010</td>
  <td>Methanol</td>
  <td>3.52</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.298</td>
  <td>.697</td>
 </tr>
 <tr>
  <td>045</td>
  <td>Jan. 11, 2010</td>
  <td>Methanol</td>
  <td>2.46</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.298</td>
  <td>.697</td>
 </tr>
 <tr>
  <td>052</td>
  <td>Jan. 11, 2010</td>
  <td>Heptane</td>
  <td>3.64</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.297</td>
  <td>.697</td>
 </tr>
</table>


fractions. As testing progressed, however, the science team
noticed a propensity for the droplets to burn disruptively and
not exhibit flame extinction (at a finite-sized droplet diameter).
The latter half of the test matrix focused on lower oxygen mole
fraction ambient environments where both diffusive and
radiative extinction occurred; these results are detailed in
Table IV for methanol and in Table V for heptane. The tests in
the lower oxygen mole fraction ambient environments started
at the maximum ambient oxygen mole fraction, 0.21 (at 1-atm
pressure). Testing proceeded as the ambient gas in the chamber


was gradually diluted with increasing amounts of nitrogen until
the limit where quasi-steady burning was not observed. This
limit represented the limiting oxygen index (LOI), identi-
fication of which was one of the primary objectives of the
FLEX experiments. Typically in a given ambient environment,
tests were conducted with both fuels (on different test days)
over a small range of droplet sizes (typically 3 to 4 mm). In
many cases, tests with fiber-supported droplets and a brief
translation of the fiber were conducted in addition to the
quiescent, free-floating droplet tests.


NASA/TP-2015-216046 11




TABLE IV.-FLEX TEST MATRIX FOR METHANOL TESTS CONDUCTED IN NITROGEN-DILUTED
AMBIENT ENVIRONMENTS, INCLUDING TESTS IN ENVIRONMENTS WITH
LOWER OXYGEN MOLE FRACTIONS (BELOW 0.21)


<table>
 <tr>
  <th>Test</th>
  <th>Date</th>
  <th>Initial droplet diameter,<br/>D0,<br/>mm</th>
  <th>Fiber</th>
  <th>Pressure,<br/>P,<br/>atm</th>
  <th>Mole fraction of<br/>oxygen</th>
  <th>Mole fraction of<br/>nitrogen</th>
 </tr>
 <tr>
  <td>033</td>
  <td>Nov. 27, 2009</td>
  <td>2.72</td>
  <td>No</td>
  <td>1.01</td>
  <td>0.210</td>
  <td>0.790</td>
 </tr>
 <tr>
  <td>034</td>
  <td>Nov. 27, 2009</td>
  <td>3.95</td>
  <td>No</td>
  <td>1.01</td>
  <td>.210</td>
  <td>.790</td>
 </tr>
 <tr>
  <td>036</td>
  <td>Dec. 15, 2009</td>
  <td>2.45</td>
  <td>No</td>
  <td>0.71</td>
  <td>.210</td>
  <td>.790</td>
 </tr>
 <tr>
  <td>046</td>
  <td>Jan. 12, 2010</td>
  <td>2.88</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.209</td>
  <td>.786</td>
 </tr>
 <tr>
  <td>048</td>
  <td>Jan. 12, 2010</td>
  <td>3.68</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.209</td>
  <td>.786</td>
 </tr>
 <tr>
  <td>054</td>
  <td>Jan. 12, 2010</td>
  <td>3.61</td>
  <td>No</td>
  <td>0.71</td>
  <td>.197</td>
  <td>.796</td>
 </tr>
 <tr>
  <td>055</td>
  <td>Jan. 29, 2010</td>
  <td>3.52</td>
  <td>Yes</td>
  <td>0.71</td>
  <td>.197</td>
  <td>.795</td>
 </tr>
 <tr>
  <td>058</td>
  <td>Feb. 4, 2010</td>
  <td>3.73</td>
  <td>No</td>
  <td>1.02</td>
  <td>.176</td>
  <td>.816</td>
 </tr>
 <tr>
  <td>059</td>
  <td>Feb. 4, 2010</td>
  <td>3.08</td>
  <td>No</td>
  <td>1.01</td>
  <td>.176</td>
  <td>.816</td>
 </tr>
 <tr>
  <td>060</td>
  <td>Feb. 4, 2010</td>
  <td>3.57</td>
  <td>Yes</td>
  <td>1.02</td>
  <td>.176</td>
  <td>.816</td>
 </tr>
 <tr>
  <td>061</td>
  <td>Feb. 4, 2010</td>
  <td>3.77</td>
  <td>Yes</td>
  <td>1.02</td>
  <td>.176</td>
  <td>.815</td>
 </tr>
 <tr>
  <td>065</td>
  <td>Mar. 19, 2010</td>
  <td>3.44</td>
  <td>No</td>
  <td>1.01</td>
  <td>.146</td>
  <td>.846</td>
 </tr>
 <tr>
  <td>066</td>
  <td>Mar. 19, 2010</td>
  <td>2.63</td>
  <td>No</td>
  <td>1.01</td>
  <td>.146</td>
  <td>.845</td>
 </tr>
 <tr>
  <td>067</td>
  <td>Mar. 19, 2010</td>
  <td>4.01</td>
  <td>No</td>
  <td>1.01</td>
  <td>.146</td>
  <td>.845</td>
 </tr>
 <tr>
  <td>068</td>
  <td>Mar. 19, 2010</td>
  <td>2.45</td>
  <td>No</td>
  <td>1.01</td>
  <td>.146</td>
  <td>.845</td>
 </tr>
 <tr>
  <td>071</td>
  <td>Mar. 19, 2010</td>
  <td>2.26</td>
  <td>No</td>
  <td>1.01</td>
  <td>.146</td>
  <td>.845</td>
 </tr>
 <tr>
  <td>075</td>
  <td>Mar. 29, 2010</td>
  <td>2.56</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.135</td>
  <td>.854</td>
 </tr>
 <tr>
  <td>076</td>
  <td>Mar. 29, 2010</td>
  <td>3.29</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.135</td>
  <td>.854</td>
 </tr>
 <tr>
  <td>077</td>
  <td>Mar. 29, 2010</td>
  <td>3.41</td>
  <td>No</td>
  <td>1.01</td>
  <td>.135</td>
  <td>.854</td>
 </tr>
 <tr>
  <td>078</td>
  <td>Mar. 29, 2010</td>
  <td>2.69</td>
  <td>No</td>
  <td>1.01</td>
  <td>.135</td>
  <td>.854</td>
 </tr>
 <tr>
  <td>082</td>
  <td>Apr. 19, 2010</td>
  <td>2.93</td>
  <td>No</td>
  <td>1.01</td>
  <td>.126</td>
  <td>.870</td>
 </tr>
 <tr>
  <td>083</td>
  <td>Apr. 19, 2010</td>
  <td>3.60</td>
  <td>No</td>
  <td>1.02</td>
  <td>.125</td>
  <td>.869</td>
 </tr>
 <tr>
  <td>084</td>
  <td>Apr. 19, 2010</td>
  <td>2.43</td>
  <td>No</td>
  <td>1.01</td>
  <td>.126</td>
  <td>.869</td>
 </tr>
 <tr>
  <td>085</td>
  <td>Apr. 19, 2010</td>
  <td>2.49</td>
  <td>No</td>
  <td>1.01</td>
  <td>.126</td>
  <td>.869</td>
 </tr>
 <tr>
  <td>086</td>
  <td>Apr. 19, 2010</td>
  <td>3.10</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.126</td>
  <td>.869</td>
 </tr>
 <tr>
  <td>087</td>
  <td>Apr. 19, 2010</td>
  <td>2.66</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.126</td>
  <td>.869</td>
 </tr>
</table>


NASA/TP-2015-216046


12




TABLE V.-FLEX TEST MATRIX FOR
AMBIENT ENVIRONMENTS,
LOWER


<table>
 <tr>
  <th>Test</th>
  <th>Date</th>
  <th>Initial droplet diameter,<br/>D0,<br/>mm</th>
  <th>Fiber</th>
  <th>Pressure,<br/>P,<br/>atm</th>
  <th>Mole fraction of<br/>oxygen</th>
  <th>Mole fraction of<br/>nitrogen</th>
 </tr>
 <tr>
  <td>035</td>
  <td>Nov. 27, 2009</td>
  <td>3.91</td>
  <td>No</td>
  <td>1.01</td>
  <td>0.210</td>
  <td>0.790</td>
 </tr>
 <tr>
  <td>047</td>
  <td>Jan. 12, 2010</td>
  <td>3.42</td>
  <td>No</td>
  <td>1.01</td>
  <td>.209</td>
  <td>.786</td>
 </tr>
 <tr>
  <td>049</td>
  <td>Jan. 19, 2010</td>
  <td>3.58</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.208</td>
  <td>.786</td>
 </tr>
 <tr>
  <td>050</td>
  <td>Jan. 19, 2010</td>
  <td>3.69</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.208</td>
  <td>.786</td>
 </tr>
 <tr>
  <td>051</td>
  <td>Jan. 19, 2010</td>
  <td>2.45</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.208</td>
  <td>.786</td>
 </tr>
 <tr>
  <td>053</td>
  <td>Jan. 12, 2010</td>
  <td>3.4</td>
  <td>No</td>
  <td>1.01</td>
  <td>.209</td>
  <td>.786</td>
 </tr>
 <tr>
  <td>056</td>
  <td>Jan. 29, 2010</td>
  <td>3.64</td>
  <td>No</td>
  <td>.72</td>
  <td>.196</td>
  <td>.795</td>
 </tr>
 <tr>
  <td>057</td>
  <td>Jan. 29, 2010</td>
  <td>3.17</td>
  <td>Yes</td>
  <td>.72</td>
  <td>.196</td>
  <td>.794</td>
 </tr>
 <tr>
  <td>062</td>
  <td>Mar. 11, 2010</td>
  <td>3.48</td>
  <td>No</td>
  <td>1.00</td>
  <td>.175</td>
  <td>.815</td>
 </tr>
 <tr>
  <td>063</td>
  <td>Mar. 11, 2010</td>
  <td>2.28</td>
  <td>No</td>
  <td>1.01</td>
  <td>.175</td>
  <td>.815</td>
 </tr>
 <tr>
  <td>064</td>
  <td>Mar. 11, 2010</td>
  <td>2.74</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.175</td>
  <td>.815</td>
 </tr>
 <tr>
  <td>069</td>
  <td>Mar. 19, 2010</td>
  <td>1.29</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.145</td>
  <td>.845</td>
 </tr>
 <tr>
  <td>070</td>
  <td>Mar. 23, 2010</td>
  <td>1.30</td>
  <td>No</td>
  <td>1.01</td>
  <td>.145</td>
  <td>.845</td>
 </tr>
 <tr>
  <td>073</td>
  <td>Mar. 23, 2010</td>
  <td>4.72</td>
  <td>No</td>
  <td>1.00</td>
  <td>.145</td>
  <td>.845</td>
 </tr>
 <tr>
  <td>074</td>
  <td>Mar. 23, 2010</td>
  <td>1.53</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.145</td>
  <td>.845</td>
 </tr>
 <tr>
  <td>079</td>
  <td>Mar. 30, 2010</td>
  <td>3.06</td>
  <td>No</td>
  <td>1.01</td>
  <td>.134</td>
  <td>.853</td>
 </tr>
 <tr>
  <td>080</td>
  <td>Mar. 30, 2010</td>
  <td>4.00</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.134</td>
  <td>.853</td>
 </tr>
 <tr>
  <td>081</td>
  <td>Mar. 30, 2010</td>
  <td>2.40</td>
  <td>Yes</td>
  <td>1.01</td>
  <td>.134</td>
  <td>.853</td>
 </tr>
</table>


HEPTANE TESTS CONDUCTED IN NITROGEN-DILUTED
INCLUDING TESTS IN ENVIRONMENTS WITH
OXYGEN MOLE FRACTIONS (BELOW 0.21)


Following the completion of the nitrogen-diluted ambient test
matrix, testing proceeded with carbon-dioxide-diluted ambient
environments. These tests also began at the highest oxygen
mole fraction ambient environment; then increasing amounts of
CO2 were added while the ambient pressure was maintained
constant. Testing concluded when quasi-steady burning was not
observed, again the determination of the LOI. This also
represented the minimum carbon dioxide mole fraction required
to extinguish or prevent the spread of a flame. The tests were
conducted in a 1.0-atm, 0.21 oxygen mole fraction (initially)
ambient environment and a 0.70-atm, 0.30 oxygen mole


fraction (initially) ambient environment. These two ambient
environments represent the nominal environment on the ISS
and the extravehicular activity (EVA) pre-breathe environment
on the ISS and the maximum proposed oxygen mole fraction on
future exploration vehicles. Table VI (for methanol) and
Table VII (for heptane) detail the test matrices in the nominally
0.7-atm ambient environment. These tests start at a relatively
high carbon dioxide mole fraction (0.15) to minimize the
testing in higher oxygen mole fraction ambient environments.
Table VIII details the test matrix in the 1.0-atm ambient
environment.


NASA/TP-2015-216046 13




<table>
 <tr>
  <th>Test</th>
  <th>Date</th>
  <th>Initial droplet diameter,<br/>D0,<br/>mm</th>
  <th>Fiber</th>
  <th>Pressure,<br/>P,<br/>atm</th>
  <th>Mole fraction of<br/>oxygen</th>
  <th>Mole fraction of<br/>carbon dioxide</th>
  <th>Mole fraction of<br/>nitrogen</th>
 </tr>
 <tr>
  <td>088</td>
  <td>May 5, 2010</td>
  <td>3.08</td>
  <td>No</td>
  <td>0.71</td>
  <td>0.250</td>
  <td>0.150</td>
  <td>0.600</td>
 </tr>
 <tr>
  <td>089</td>
  <td>May 5, 2010</td>
  <td>3.79</td>
  <td>No</td>
  <td>.71</td>
  <td>.250</td>
  <td>.150</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>090</td>
  <td>May 6, 2010</td>
  <td>3.65</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.250</td>
  <td>.150</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>091</td>
  <td>May 5, 2010</td>
  <td>3.59</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.250</td>
  <td>.150</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>097</td>
  <td>June 16, 2010</td>
  <td>4.29</td>
  <td>No</td>
  <td>.70</td>
  <td>.240</td>
  <td>.200</td>
  <td>.560</td>
 </tr>
 <tr>
  <td>098</td>
  <td>June 21, 2010</td>
  <td>3.67</td>
  <td>No</td>
  <td>.71</td>
  <td>.230</td>
  <td>.250</td>
  <td>.520</td>
 </tr>
 <tr>
  <td>099</td>
  <td>June 21, 2010</td>
  <td>4.34</td>
  <td>No</td>
  <td>.70</td>
  <td>.230</td>
  <td>.250</td>
  <td>.520</td>
 </tr>
 <tr>
  <td>104</td>
  <td>June 16, 2010</td>
  <td>3.66</td>
  <td>No</td>
  <td>.70</td>
  <td>.240</td>
  <td>.200</td>
  <td>.560</td>
 </tr>
 <tr>
  <td>105</td>
  <td>June 16, 2010</td>
  <td>4.35</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.240</td>
  <td>.200</td>
  <td>.560</td>
 </tr>
 <tr>
  <td>106</td>
  <td>June 21, 2010</td>
  <td>3.16</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.230</td>
  <td>.250</td>
  <td>.520</td>
 </tr>
 <tr>
  <td>107</td>
  <td>June 16, 2010</td>
  <td>3.25</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.240</td>
  <td>.200</td>
  <td>.560</td>
 </tr>
 <tr>
  <td>108</td>
  <td>June 21, 2010</td>
  <td>3.82</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.230</td>
  <td>.250</td>
  <td>.520</td>
 </tr>
 <tr>
  <td>109</td>
  <td>Aug. 31, 2010</td>
  <td>3.62</td>
  <td>No</td>
  <td>.71</td>
  <td>.211</td>
  <td>.299</td>
  <td>.490</td>
 </tr>
 <tr>
  <td>110</td>
  <td>Aug. 31, 2010</td>
  <td>2.88</td>
  <td>No</td>
  <td>.71</td>
  <td>.211</td>
  <td>.299</td>
  <td>.490</td>
 </tr>
 <tr>
  <td>111</td>
  <td>Aug. 31, 2010</td>
  <td>3.38</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.211</td>
  <td>.299</td>
  <td>.490</td>
 </tr>
 <tr>
  <td>112</td>
  <td>Sept. 1, 2010</td>
  <td>4.02</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.211</td>
  <td>.299</td>
  <td>.490</td>
 </tr>
 <tr>
  <td>113</td>
  <td>Sept. 1, 2010</td>
  <td>4.26</td>
  <td>No</td>
  <td>.70</td>
  <td>.200</td>
  <td>.350</td>
  <td>.450</td>
 </tr>
 <tr>
  <td>114</td>
  <td>Sept. 1, 2010</td>
  <td>3.28</td>
  <td>No</td>
  <td>.70</td>
  <td>.200</td>
  <td>.350</td>
  <td>.450</td>
 </tr>
 <tr>
  <td>115</td>
  <td>Sept. 1, 2010</td>
  <td>4.03</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.200</td>
  <td>.350</td>
  <td>.450</td>
 </tr>
 <tr>
  <td>116</td>
  <td>Sept. 1, 2010</td>
  <td>3.15</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.200</td>
  <td>.350</td>
  <td>.450</td>
 </tr>
 <tr>
  <td>121</td>
  <td>Sept. 8, 2010</td>
  <td>4.33</td>
  <td>No</td>
  <td>.69</td>
  <td>.180</td>
  <td>.400</td>
  <td>.420</td>
 </tr>
 <tr>
  <td>122</td>
  <td>Sept. 8, 2010</td>
  <td>3.57</td>
  <td>No</td>
  <td>.70</td>
  <td>.180</td>
  <td>.400</td>
  <td>.420</td>
 </tr>
 <tr>
  <td>123</td>
  <td>Sept. 8, 2010</td>
  <td>4.13</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.180</td>
  <td>.400</td>
  <td>.420</td>
 </tr>
 <tr>
  <td>124</td>
  <td>Sept. 8, 2010</td>
  <td>3.57</td>
  <td>Yes</td>
  <td>.70</td>
  <td>.180</td>
  <td>.400</td>
  <td>.420</td>
 </tr>
 <tr>
  <td>125</td>
  <td>Sept. 13, 2010</td>
  <td>3.70</td>
  <td>No</td>
  <td>.71</td>
  <td>.170</td>
  <td>.450</td>
  <td>.380</td>
 </tr>
 <tr>
  <td>126</td>
  <td>Sept. 13, 2010</td>
  <td>2.89</td>
  <td>No</td>
  <td>.71</td>
  <td>.170</td>
  <td>.450</td>
  <td>.380</td>
 </tr>
 <tr>
  <td>127</td>
  <td>Sept. 13, 2010</td>
  <td>3.20</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.170</td>
  <td>.450</td>
  <td>.380</td>
 </tr>
 <tr>
  <td>128</td>
  <td>Sept. 13, 2010</td>
  <td>2.93</td>
  <td>Yes</td>
  <td>.71</td>
  <td>.170</td>
  <td>.450</td>
  <td>.380</td>
 </tr>
 <tr>
  <td>140</td>
  <td>Nov. 4, 2010</td>
  <td>4.05</td>
  <td>No</td>
  <td>.70</td>
  <td>.146</td>
  <td>.500</td>
  <td>.354</td>
 </tr>
 <tr>
  <td>141</td>
  <td>Nov. 4, 2010</td>
  <td>2.94</td>
  <td>No</td>
  <td>.70</td>
  <td>.146</td>
  <td>.500</td>
  <td>.354</td>
 </tr>
 <tr>
  <td>142</td>
  <td>Nov. 4, 2010</td>
  <td>1.88</td>
  <td>No</td>
  <td>.70</td>
  <td>.146</td>
  <td>.500</td>
  <td>.354</td>
 </tr>
 <tr>
  <td>143</td>
  <td>Nov. 4, 2010</td>
  <td>2.33</td>
  <td>No</td>
  <td>.70</td>
  <td>.146</td>
  <td>.500</td>
  <td>.354</td>
 </tr>
 <tr>
  <td>147</td>
  <td>Sept. 13, 2010</td>
  <td>3.13</td>
  <td>No</td>
  <td>.71</td>
  <td>.170</td>
  <td>.450</td>
  <td>.380</td>
 </tr>
</table>


METHANOL TESTS CONDUCTED IN 0.70-atm
CARBON-DIOXIDE-DILUTED AMBIENT ENVIRONMENTS


TABLE VI.-FLEX TEST MATRIX FOR


NASA/TP-2015-216046


14




<table>
 <tr>
  <th>Test</th>
  <th>Date</th>
  <th>Initial</th>
  <th>diameter,</th>
  <th>Fiber</th>
  <th>P,<br/>atm</th>
  <th>fraction of<br/>oxygen</th>
  <th>fraction of<br/>carbon dioxide</th>
  <th>Mole fraction of<br/>nitrogen</th>
 </tr>
 <tr>
  <td>092</td>
  <td>June 14, 2010</td>
  <td></td>
  <td></td>
  <td>No</td>
  <td>0.71</td>
  <td>0.250</td>
  <td>0.150</td>
  <td>0.600</td>
 </tr>
 <tr>
  <td>093</td>
  <td>June 15, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.71</td>
  <td>.250</td>
  <td>.150</td>
  <td>.600</td>
 </tr>
 <tr>
  <td>094</td>
  <td>June 15, 2010</td>
  <td></td>
  <td></td>
  <td>No</td>
  <td>.70</td>
  <td>.240</td>
  <td>.200</td>
  <td>.560</td>
 </tr>
 <tr>
  <td>095</td>
  <td>June 15, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.70</td>
  <td>.240</td>
  <td>.200</td>
  <td>.560</td>
 </tr>
 <tr>
  <td>096</td>
  <td>June 15, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.70</td>
  <td>.240</td>
  <td>.200</td>
  <td>.560</td>
 </tr>
 <tr>
  <td>100</td>
  <td>June 29, 2010</td>
  <td></td>
  <td></td>
  <td>No</td>
  <td>.71</td>
  <td>.230</td>
  <td>.250</td>
  <td>.520</td>
 </tr>
 <tr>
  <td>101</td>
  <td>June 29, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.71</td>
  <td>.230</td>
  <td>.250</td>
  <td>.520</td>
 </tr>
 <tr>
  <td>102</td>
  <td>June 29, 2010</td>
  <td></td>
  <td></td>
  <td>No</td>
  <td>.70</td>
  <td>.210</td>
  <td>.300</td>
  <td>.490</td>
 </tr>
 <tr>
  <td>103</td>
  <td>June 29, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.70</td>
  <td>.210</td>
  <td>.300</td>
  <td>.490</td>
 </tr>
 <tr>
  <td>117</td>
  <td>Sept. 6, 2010</td>
  <td></td>
  <td></td>
  <td>No</td>
  <td>.70</td>
  <td>.200</td>
  <td>.350</td>
  <td>.450</td>
 </tr>
 <tr>
  <td>118</td>
  <td>Sept. 6, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.70</td>
  <td>.200</td>
  <td>.350</td>
  <td>.450</td>
 </tr>
 <tr>
  <td>119</td>
  <td>Sept. 7, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.70</td>
  <td>.180</td>
  <td>.400</td>
  <td>.420</td>
 </tr>
 <tr>
  <td>120</td>
  <td>Sept. 7, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.70</td>
  <td>.180</td>
  <td>.400</td>
  <td>.420</td>
 </tr>
 <tr>
  <td>129</td>
  <td>Sept. 17, 2010</td>
  <td></td>
  <td></td>
  <td>No</td>
  <td>.71</td>
  <td>.170</td>
  <td>.450</td>
  <td>.380</td>
 </tr>
 <tr>
  <td>130</td>
  <td>Sept. 17, 2010</td>
  <td></td>
  <td></td>
  <td>Yes</td>
  <td>.71</td>
  <td>.170</td>
  <td>.450</td>
  <td>.380</td>
 </tr>
 <tr>
  <td></td>
  <td></td>
  <td></td>
  <td>TEST</td>
  <td>MATRIX<br/>not</td>
  <td>TESTS<br/>by a</td>
  <td>IN</td>
  <td></td>
  <td></td>
 </tr>
 <tr>
  <td>Test</td>
  <td>Date</td>
  <td>Fuel</td>
  <td>Initial</td>
  <td>diameter,</td>
  <td>Pressure,<br/>P,<br/>atm</td>
  <td>Mole fraction of<br/>oxygen</td>
  <td>Mole fraction of<br/>carbon dioxide</td>
  <td>Mole fraction of<br/>nitrogen</td>
 </tr>
 <tr>
  <td>148</td>
  <td>Nov. 18, 2010</td>
  <td>Heptane</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>0.200</td>
  <td>0.050</td>
  <td>0.750</td>
 </tr>
 <tr>
  <td>149</td>
  <td>Nov. 18, 2010</td>
  <td>Heptane</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.200</td>
  <td>.050</td>
  <td>.750</td>
 </tr>
 <tr>
  <td>150</td>
  <td>Nov. 18, 2010</td>
  <td>Heptane</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.200</td>
  <td>.050</td>
  <td>.750</td>
 </tr>
 <tr>
  <td>151</td>
  <td>Dec. 8, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.00</td>
  <td>.180</td>
  <td>.150</td>
  <td>.670</td>
 </tr>
 <tr>
  <td>152</td>
  <td>Dec. 8, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.180</td>
  <td>.150</td>
  <td>.670</td>
 </tr>
 <tr>
  <td>153</td>
  <td>Dec. 8, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.180</td>
  <td>.150</td>
  <td>.670</td>
 </tr>
 <tr>
  <td>154</td>
  <td>Dec. 9, 2010</td>
  <td>Heptane</td>
  <td></td>
  <td></td>
  <td>1.00</td>
  <td>.180</td>
  <td>.150</td>
  <td>.670</td>
 </tr>
 <tr>
  <td>155</td>
  <td>Dec. 9, 2010</td>
  <td>Heptane</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.180</td>
  <td>.150</td>
  <td>.670</td>
 </tr>
 <tr>
  <td>156</td>
  <td>Dec. 9, 2010</td>
  <td>Heptane</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.180</td>
  <td>.150</td>
  <td>.670</td>
 </tr>
 <tr>
  <td>157</td>
  <td>Dec. 9, 2010</td>
  <td>Heptane</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.180</td>
  <td>.150</td>
  <td>.670</td>
 </tr>
 <tr>
  <td>158</td>
  <td>Dec. 14, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.00</td>
  <td>.160</td>
  <td>.250</td>
  <td>.590</td>
 </tr>
 <tr>
  <td>159</td>
  <td>Dec. 14, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.160</td>
  <td>.250</td>
  <td>.590</td>
 </tr>
 <tr>
  <td>160</td>
  <td>Dec. 14, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.160</td>
  <td>.250</td>
  <td>.590</td>
 </tr>
 <tr>
  <td>161</td>
  <td>Dec. 14, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.160</td>
  <td>.250</td>
  <td>.590</td>
 </tr>
 <tr>
  <td>162</td>
  <td>Dec. 28, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.00</td>
  <td>.153</td>
  <td>.298</td>
  <td>.549</td>
 </tr>
 <tr>
  <td>163</td>
  <td>Dec. 28, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.153</td>
  <td>.298</td>
  <td>.549</td>
 </tr>
 <tr>
  <td>164</td>
  <td>Dec. 28, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.153</td>
  <td>.298</td>
  <td>.549</td>
 </tr>
 <tr>
  <td>165</td>
  <td>Dec. 28, 2010</td>
  <td>Methanol</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.153</td>
  <td>.298</td>
  <td>.549</td>
 </tr>
 <tr>
  <td>166</td>
  <td>Dec. 9, 2010</td>
  <td>Heptane</td>
  <td></td>
  <td></td>
  <td>1.01</td>
  <td>.180</td>
  <td>.150</td>
  <td>.670</td>
 </tr>
</table>


TABLE VII.-FLEX TEST MATRIX FOR HEPTANE TESTS CONDUCTED IN
0.70-atm CARBON-DIOXIDE-DILUTED AMBIENT ENVIRONMENTS
droplet
Pressure, Mole
Mole
D0,
mm


NASA/TP-2015-216046 15




##### 4.2 Analyzed Data The great majority of the tests were of free-floating droplets


(no support tether). For these tests, the droplets were rarely
The digital image data from the FLEX experiments yielded a completely motionless; they had some residual velocity from
wealth of information regarding the combustion of liquid fuel deployment and ignition and then drifted more as a result of the
droplets in quiescent and subbuoyant flow (achieved by residual acceleration of the spacecraft (g-jitter). As a result of
translating the fiber) microgravity environments. The data this, the droplets did drift out of the FOV of one (typically the
archived in this report include the following: HiBMs) or more of the CIR cameras. For tests where the droplet
drifted out of the FOV of the camera, the data end abruptly (e.g.,


1. Droplet size as a function of time the droplet regression during the FLEX-011 test). This does not

2. LLUV flame size as a function of time correspond to the end of the test, just to the end of the data from

3. Color camera flame size as a function of time that particular view (note that the flame histories continue during the FLEX-011 test). For a minority of tests, the droplet The video records also provide qualitative information of the drifted out of the HiBMs FOV as a result of the deployment,


combustion process including, but not limited to, ignition, and/or g-jitter. However, it then actually drifted back
into the FOV. In this case, there is a gap in the history of that


1. Droplet shape as a function of time view (e.g., the droplet history for the FLEX-013 test). The

2. Qualitative sooting propensity as a function of time sharp decline in the droplet size on either side of that gap (3) Flame shape and flame dynamics as a function of time corresponds to the time when the droplet (usually) or flame


(4) Disruptive burning (rarely) was partially in and partially out of the FOV.


(5) Droplet/fiber interactions For some tests, some of the CIR cameras failed to record data
(6) Postcombustion vaporization and vapor cloud formation for a portion of the test, and for other tests, none of the test was
recorded. These show up in the plots in Appendix A as either
In an effort to document and archive the results from the missing traces or gaps in the data (e.g., the FLEX-024 test, for


FLEX experiments, all data for (1) to (6) are archived in this which the HiBMs failed to record any data).
report. Appendix A gives the detailed results of the The detailed data plots in Appendix B show two different
experiments. The data are also available electronically as text measurements of flame diameter, one from the LLUV camera
files and compressed video recordings of the HiBMs and color and the other from the color camera. For almost all of the tests,
camera views. the diameter measured by the LLUV is larger than that
measured by the color camera. The flame diameters from the


1. Observations and Discussion color camera are typically about three-fourths of those from the LLUV camera. This discrepancy is not unusual and is a result


5.1 General Observations of the LLUV being sensitive to the OH• chemiluminescence,
which typically peaks outside of the visible flame. For heptane
The primary objective for this report was to detail and archive tests, where there is significant soot luminosity (which is not
the results from the FLEX experiments from March 2009 to visible in the LLUV, but dominates the color camera), the
December 2010. Appendix B presents the detailed results for discrepancy is even larger because the peak of the soot
the droplet size (droplet diameter squared) and flame sizes luminosity is typically inside the blue flame envelope.
(from both the LLUV and color camera views) as functions of
time. These results, along with the raw experiment data, are 5.2 Fuel Needle Contamination
available from the NASA Physical Science Informatics data
repository (psi.nasa.gov, registration required). During the assembly of the MDCA hardware, a conformal
In each test, there is a clear ambiguity in the droplet size coating was applied to the fuel-dispensing needles. The product
during ignition (after deployment and before the igniters was applied in two layers, a primer (Dow Corning 1204) and a
withdraw). This was the result of the broadband glow from the conformal coat (Dow Corning 3140 RTV (MIL-A-46146)
igniters changing the discrimination between the droplet and coating). Subsequent testing showed that the coating can both
the background. This was especially present from the FLEX- dissolve and "flake" off in both methanol and heptane. When
001 test to the FLEX-009 test. For these tests, the shutter speed this occurred, the deployed fuel droplet was clearly not pure but
(integration time of the array) was 1/30 s (inverse of the framing contained an unknown amount of the conformal coating. Once
rate). After the FLEX-009 test, the shutter speed decreased to a this problem was discovered, the mitigation was to prepare and
much smaller value (1/1000 s) with a corresponding increase in fly new uncoated needles. All tests subsequent to these (to be
the illumination level. This minimized the image distortion reported in the future) will not have contamination. From
caused by the igniters and the broadband flame radiation (from extensive testing, careful analysis of the experimental data,
soot for heptane), resulting in more accurate droplet size data. comparison with space-based data from uncontaminated


NASA/TP-2015-216046 16




needles, numerical modeling efforts, and ground-based testing,
we can make the following assertions about the experimental
data reported herein:


(1) Burning-rate constants were average, and the droplet


history was minimally influenced by the contaminant. The
contaminant was likely present in trace amounts and was a very
low volatility compound. Because methanol and heptane are
relatively high volatility fuels, the droplet regression history
was dominated by the fuel not by the contaminant.


(2) The flame size and flame history were similarly


minimally influenced by the contaminant.


(3) In the few tests where unusual features were observed


in the flame view, such as minor disruptions and visual
"sparklers," these features were probably influenced, and
possibly caused, by the presence of the contaminant.


(4) Disruptive extinction of methanol is probably due to the


presence of the contaminant.


(5) Disruptive extinction of heptane may be due to the


presence of the contaminant. Subsequent tests with clean
needles and fuel, however, also exhibited disruptive extinction
at small droplet sizes, so no conclusion can be drawn regarding
disruptive burning for heptane in the tests reported herein.


(6) The diffusive extinction droplet diameters (smaller


diameters) for methanol (where there is no disruption) were
minimally influenced by the presence of the contaminant.


(7) Radiative extinction droplet diameters (larger diameters)


were not influenced by the presence of the contaminant.


(8) Distorted droplets (e.g., the HiBMs video from the


FLEX-088 test) for methanol droplet burning (approximately
four tests) are probably the result of the contaminant.


#### 6.0 Conclusions


Histories of droplet and flame diameters, as well as burning-
rate constants and extinction diameters, were obtained in Flame
Extinguishment Experiment (FLEX) program experiments
performed on the International Space Station for methanol and


n-heptane droplets with initial diameters between 2 and 5 mm.


Burning was done in oxidizing atmospheres at ambient
temperature and at various pressures between 0.70 and


3.05 atm, over ranges of dilution of oxygen with nitrogen,


oxygen with carbon dioxide, and mixtures thereof. The
experimental methods and data analysis procedures are reported
here, and the results are presented and catalogued. More than
100 useful combustion histories were obtained. These extensive
experimental results are not interpreted here; the intent is
merely to make the data readily available for future scientific
interpretation.


Glenn Research Center
National Aeronautics and Space Administration
Cleveland, Ohio, November 21, 2015


NASA/TP-2015-216046 17






##### Appendix A.-Detailed Experimental Results


This appendix provides a detailed listing of all the results of the test. For cases where the droplet left the HiBMs field of
the Flame Extinguishment Experiment (FLEX) tests from view (FOV) before extinction, we did estimate (extrapolate
March 2009 through December 2010. In addition to the data the burning history) to determine the extinction droplet
printed in this section, electronic data files are available with diameter if there was sufficient burning history and the length
the detailed results on the digital video disc (DVD) addendum. of time to extrapolate was not that long. If the droplet was
not in the HiBMS FOV for enough time, the extinction


A.1 Summary Data droplet diameter is not listed.
Notes-specific observations for a particular test, as explained
The following list explains the column headings in Table IX: in the notes at the bottom of the table
Fiber-Yes or No depending on whether a support fiber was in
FLEX test-number used by the FLEX science team place for the tests
FLEX identifier-used by the Combustion Integrated Rack P-absolute ambient pressure
(CIR) engineering team O2-ambient oxygen mole fraction from detailed records of the
Test date-date the test was performed chamber fill, recirculation, filter, and combustion history
Test time-time the test was performed (Greenwich Mean CO2-ambient carbon dioxide mole fraction from detailed
Time, GMT) records of the chamber fill, recirculation, filter, and
Fuel-fuel used for the test: methanol (CH3OH) or heptane combustion history
(C7H16) N2-ambient nitrogen mole fraction from detailed records of the


Actual D0-initial droplet diameter or droplet diameter at chamber fill, recirculation, filter, and combustion history
time zero where time zero is the time when the igniters are H2O-ambient water vapor mole fraction from detailed records
turned ON of the chamber fill, recirculation, filter, and combustion
Burning rate-average burning rate constant from a linear fit history
of the droplet diameter squared versus time from shortly after Heptane-ambient heptane (C7H16) vapor mole fraction from
ignition to extinction detailed records of the chamber fill, recirculation, filter, and
Visible flame extinction diameter-droplet diameter at the combustion history
time the visible flame extinguished, where "-" indicates Methanol-ambient methanol (CH3OH) vapor mole fraction
flame extinction did not occur either because the droplet from detailed records of the chamber fill, recirculation, filter,
burned to completion or because a droplet disruption ended and combustion history


NASA/TP-2015-216046 19




###### A.2 Experiment Results


#### Table IX summarizes the data.


<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>time, Burn s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>FLEX-001</td>
  <td>20CAL08</td>
  <td>3/5/09</td>
  <td>17:22:03</td>
  <td>Methanol</td>
  <td>757.7</td>
  <td>0.21</td>
  <td>0.79</td>
  <td>0</td>
  <td>0</td>
  <td>1.69</td>
  <td>0.89</td>
  <td>0.52</td>
  <td>4.3</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-002</td>
  <td>20CAL10</td>
  <td>3/5/09</td>
  <td>19:20:06</td>
  <td>Methanol</td>
  <td>762</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>1.86</td>
  <td>.94</td>
  <td>.6</td>
  <td>5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-003</td>
  <td>20CAL12</td>
  <td>3/5/09</td>
  <td>21:17:46</td>
  <td>Methanol</td>
  <td>764.2</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>1.61</td>
  <td>.92</td>
  <td>.58</td>
  <td>3.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-004</td>
  <td>30CAL02</td>
  <td>3/31/09</td>
  <td>17:16:18</td>
  <td>Methanol</td>
  <td>760</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>2.06</td>
  <td>-</td>
  <td>.6</td>
  <td>7.64</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-005</td>
  <td>30CAL03</td>
  <td>3/31/09</td>
  <td>19:00:48</td>
  <td>Methanol</td>
  <td>760</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>1.92</td>
  <td>.81</td>
  <td>.48</td>
  <td>6.34</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-006</td>
  <td>40CAL01</td>
  <td>3/31/09</td>
  <td>20:05:49</td>
  <td>Methanol</td>
  <td>760</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>2.54</td>
  <td>1.53</td>
  <td>.51</td>
  <td>9.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-007</td>
  <td>20CAL13</td>
  <td>4/10/09</td>
  <td>13:26:11</td>
  <td>Heptane</td>
  <td>761.3</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>1.87</td>
  <td>-</td>
  <td>.67</td>
  <td>5.3</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-008</td>
  <td>30CAL06</td>
  <td>4/10/09</td>
  <td>18:07:15</td>
  <td>Heptane</td>
  <td>762.4</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>2.95</td>
  <td>-</td>
  <td>.79</td>
  <td>14.8</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-009</td>
  <td>30CAL07</td>
  <td>4/10/09</td>
  <td>-</td>
  <td>Heptane</td>
  <td>760</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-010</td>
  <td>256F002</td>
  <td>5/22/09</td>
  <td>14:53:27</td>
  <td>Methanol</td>
  <td>2319.7</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>3.86</td>
  <td>-</td>
  <td>.37</td>
  <td>13.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-011</td>
  <td>256R001</td>
  <td>5/22/09</td>
  <td>15:33:47</td>
  <td>Methanol</td>
  <td>2318.8</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>3.03</td>
  <td>-</td>
  <td>.4</td>
  <td>16.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-012</td>
  <td>264F003</td>
  <td>5/22/09</td>
  <td>19:23:35</td>
  <td>Heptane</td>
  <td>2319.9</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>2.74</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-013</td>
  <td>256R002</td>
  <td>6/25/09</td>
  <td>15:33:05</td>
  <td>Methanol</td>
  <td>2074.2</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>2.59</td>
  <td>-</td>
  <td>.49</td>
  <td>10.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-014</td>
  <td>256F007</td>
  <td>6/29/09</td>
  <td>12:26:06</td>
  <td>Methanol</td>
  <td>2055.6</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>3.7</td>
  <td>-</td>
  <td>-</td>
  <td>11.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-015</td>
  <td>256F008</td>
  <td>6/29/09</td>
  <td>13:56:06</td>
  <td>Methanol</td>
  <td>2066.6</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>4.42</td>
  <td>-</td>
  <td>-</td>
  <td>23.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-016</td>
  <td>256F009</td>
  <td>6/29/09</td>
  <td>15:34:58</td>
  <td>Methanol</td>
  <td>2072.1</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>1.66</td>
  <td>1</td>
  <td>.53</td>
  <td>3.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-017</td>
  <td>240R003</td>
  <td>7/1/09</td>
  <td>12:28:41</td>
  <td>Methanol</td>
  <td>1545.7</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>2.67</td>
  <td>-</td>
  <td>-</td>
  <td>2.4</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-018</td>
  <td>248F001</td>
  <td>7/1/09</td>
  <td>16:28:56</td>
  <td>Heptane</td>
  <td>1553.8</td>
  <td>.21</td>
  <td>.09</td>
  <td>.7</td>
  <td>0</td>
  <td>2.74</td>
  <td>1.77</td>
  <td>.61</td>
  <td>8.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-019</td>
  <td>196F001</td>
  <td>8/26/09</td>
  <td>19:07:28</td>
  <td>Heptane</td>
  <td>539.1</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>0</td>
  <td>3.39</td>
  <td>-</td>
  <td>.9</td>
  <td>4.2</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-020</td>
  <td>192F001</td>
  <td>10/24/09</td>
  <td>14:09:04</td>
  <td>Methanol</td>
  <td>539.5</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>0</td>
  <td>3.4</td>
  <td>1.56</td>
  <td>.53</td>
  <td>17.4</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-021</td>
  <td>192F002</td>
  <td>10/24/09</td>
  <td>15:15:24</td>
  <td>Methanol</td>
  <td>540.6</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>0</td>
  <td>3.49</td>
  <td>.95</td>
  <td>.66</td>
  <td>17.8</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-022</td>
  <td>192F003</td>
  <td>10/24/09</td>
  <td>15:39:48</td>
  <td>Methanol</td>
  <td>540.5</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>0</td>
  <td>3.5</td>
  <td>-</td>
  <td>.65</td>
  <td>18.2</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-023</td>
  <td>196F002</td>
  <td>10/24/09</td>
  <td>18:29:53</td>
  <td>Heptane</td>
  <td>541.8</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>0</td>
  <td>3.01</td>
  <td>-</td>
  <td>.73</td>
  <td>13.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-024</td>
  <td>196F003</td>
  <td>10/24/09</td>
  <td>19:44:04</td>
  <td>Heptane</td>
  <td>542.8</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-025</td>
  <td>191R001</td>
  <td>11/9/09</td>
  <td>11:42:23</td>
  <td>Methanol</td>
  <td>537.3</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>0</td>
  <td>2.6</td>
  <td>.59</td>
  <td>.65</td>
  <td>10.3</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-026</td>
  <td>191F001</td>
  <td>11/9/09</td>
  <td>11:59:59</td>
  <td>Methanol</td>
  <td>538.4</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>0</td>
  <td>3.63</td>
  <td>.4</td>
  <td>.62</td>
  <td>22.2</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-027</td>
  <td>195F001</td>
  <td>11/9/09</td>
  <td>14:04:11</td>
  <td>Heptane</td>
  <td>540.7</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>0</td>
  <td>3.87</td>
  <td>-</td>
  <td>.64</td>
  <td>23.8</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-028</td>
  <td>195F002</td>
  <td>11/9/09</td>
  <td>14:56:05</td>
  <td>Heptane</td>
  <td>539.7</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>0</td>
  <td>3.36</td>
  <td>-</td>
  <td>.64</td>
  <td>17.3</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-029</td>
  <td>178R001</td>
  <td>11/13/09</td>
  <td>13:11:23</td>
  <td>Methanol</td>
  <td>766.9</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>0</td>
  <td>2.57</td>
  <td>-</td>
  <td>.74</td>
  <td>10.4</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-030</td>
  <td>178F001</td>
  <td>11/13/09</td>
  <td>14:03:46</td>
  <td>Methanol</td>
  <td>769.2</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>0</td>
  <td>3.26</td>
  <td>1.32</td>
  <td>.59</td>
  <td>15.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-031</td>
  <td>182F001</td>
  <td>11/13/09</td>
  <td>18:33:39</td>
  <td>Heptane</td>
  <td>770.5</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>0</td>
  <td>3.39</td>
  <td>-</td>
  <td>.85</td>
  <td>18.4</td>
  <td>Disruption</td>
 </tr>
</table>


TABLE IX.-RESULTS BY TEST NUMBER AND FLEX IDENTIFIER
Initial ambient
composition,
fraction


NASA/TP-2015-216046


20




<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>Burn time, s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>Test</td>
  <td>Identifier</td>
  <td>Date</td>
  <td>Greenwich mean time</td>
  <td>Heptane</td>
  <td>771</td>
  <td>O 2</td>
  <td>N2</td>
  <td>CO2</td>
  <td>mm</td>
  <td>diameter, mm</td>
  <td>.68</td>
  <td>14</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-032</td>
  <td>182F002</td>
  <td>11/13/09</td>
  <td>19:04:33</td>
  <td>Heptane</td>
  <td>771</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>3.07</td>
  <td>-</td>
  <td>.68</td>
  <td>14</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-033</td>
  <td>177R002</td>
  <td>11/27/09</td>
  <td>10:02:15</td>
  <td>Methanol</td>
  <td>764.5</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>2.62</td>
  <td>1.25</td>
  <td>.48</td>
  <td>11.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-034</td>
  <td>177F001</td>
  <td>11/27/09</td>
  <td>11:15:38</td>
  <td>Methanol</td>
  <td>767.7</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>3.89</td>
  <td>2</td>
  <td>.44</td>
  <td>27.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-035</td>
  <td>181F001</td>
  <td>11/27/09</td>
  <td>13:01:24</td>
  <td>Heptane</td>
  <td>768.1</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>3.85</td>
  <td>3.34</td>
  <td>.43</td>
  <td>8.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-036</td>
  <td>190R002</td>
  <td>12/15/09</td>
  <td>10:39:35</td>
  <td>Methanol</td>
  <td>539</td>
  <td>.2</td>
  <td>.8</td>
  <td>0</td>
  <td>2.4</td>
  <td>1.67</td>
  <td>.45</td>
  <td>7.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-037</td>
  <td>220R001</td>
  <td>1/7/10</td>
  <td>19:08:46</td>
  <td>Methanol</td>
  <td>534.3</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>3.31</td>
  <td>-</td>
  <td>.72</td>
  <td>10.7</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-038</td>
  <td>220R002</td>
  <td>1/7/10</td>
  <td>19:20:38</td>
  <td>Methanol</td>
  <td>534.4</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>3.59</td>
  <td>-</td>
  <td>.71</td>
  <td>15.3</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-039</td>
  <td>224F001</td>
  <td>1/7/10</td>
  <td>21:51:19</td>
  <td>Heptane</td>
  <td>534.9</td>
  <td>.34</td>
  <td>.66</td>
  <td>0</td>
  <td>2.91</td>
  <td>0</td>
  <td>.8</td>
  <td>9.9</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-040</td>
  <td>219R001</td>
  <td>1/8/10</td>
  <td>5:02:52</td>
  <td>Methanol</td>
  <td>535.1</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>3.77</td>
  <td>-</td>
  <td>.62</td>
  <td>19.2</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-041</td>
  <td>219F001</td>
  <td>1/8/10</td>
  <td>4:41:55</td>
  <td>Methanol</td>
  <td>534.3</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>3.35</td>
  <td>-</td>
  <td>.65</td>
  <td>14.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-042</td>
  <td>223F001</td>
  <td>1/8/10</td>
  <td>1:02:04</td>
  <td>Heptane</td>
  <td>535</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>2.92</td>
  <td>-</td>
  <td>.58</td>
  <td>11.3</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-043</td>
  <td>223F002</td>
  <td>1/8/10</td>
  <td>3:16:16</td>
  <td>Heptane</td>
  <td>534.9</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>2.97</td>
  <td>0</td>
  <td>.78</td>
  <td>11.4</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-044</td>
  <td>206F001</td>
  <td>1/11/10</td>
  <td>10:33:22</td>
  <td>Methanol</td>
  <td>766.8</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>3.49</td>
  <td>-</td>
  <td>.63</td>
  <td>16.6</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-045</td>
  <td>206R001</td>
  <td>1/11/10</td>
  <td>10:54:25</td>
  <td>Methanol</td>
  <td>768.3</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>2.42</td>
  <td>1.01</td>
  <td>.73</td>
  <td>6.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-046</td>
  <td>205R001</td>
  <td>1/12/10</td>
  <td>13:14:25</td>
  <td>Methanol</td>
  <td>769.5</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>2.78</td>
  <td>1.08</td>
  <td>.54</td>
  <td>13.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-047</td>
  <td>209F001</td>
  <td>1/12/10</td>
  <td>15:48:17</td>
  <td>Heptane</td>
  <td>770.1</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>3.36</td>
  <td>-</td>
  <td>.5</td>
  <td>17.1</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-048</td>
  <td>205F001</td>
  <td>1/12/10</td>
  <td>12:14:55</td>
  <td>Methanol</td>
  <td>768.7</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>3.66</td>
  <td>-</td>
  <td>.27</td>
  <td>23.5</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-049</td>
  <td>209F003</td>
  <td>1/19/10</td>
  <td>9:09:16</td>
  <td>Heptane</td>
  <td>764.9</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>3.46</td>
  <td>2.78</td>
  <td>.59</td>
  <td>8.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-050</td>
  <td>209F004</td>
  <td>1/19/10</td>
  <td>14:08:17</td>
  <td>Heptane</td>
  <td>770.1</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>3.57</td>
  <td>2.98</td>
  <td>.52</td>
  <td>8.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-051</td>
  <td>209F005</td>
  <td>1/19/10</td>
  <td>16:38:35</td>
  <td>Heptane</td>
  <td>771.4</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>2.41</td>
  <td>0</td>
  <td>.65</td>
  <td>8.2</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-052</td>
  <td>210F002</td>
  <td>1/11/10</td>
  <td>13:46:44</td>
  <td>Heptane</td>
  <td>771.1</td>
  <td>.3</td>
  <td>.7</td>
  <td>0</td>
  <td>3.53</td>
  <td>0</td>
  <td>.7</td>
  <td>18.3</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-053</td>
  <td>209F002</td>
  <td>1/12/10</td>
  <td>16:29:37</td>
  <td>Heptane</td>
  <td>770.2</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>18.5</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-054</td>
  <td>190F003</td>
  <td>1/29/10</td>
  <td>11:27:01</td>
  <td>Methanol</td>
  <td>541.4</td>
  <td>.2</td>
  <td>.8</td>
  <td>0</td>
  <td>3.56</td>
  <td>-</td>
  <td>.41</td>
  <td>29</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-055</td>
  <td>218F001</td>
  <td>1/29/10</td>
  <td>16:06:50</td>
  <td>Methanol</td>
  <td>542.6</td>
  <td>.2</td>
  <td>.8</td>
  <td>0</td>
  <td>3.37</td>
  <td>2.39</td>
  <td>.46</td>
  <td>20.5</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-056</td>
  <td>194F001</td>
  <td>1/29/10</td>
  <td>19:13:22</td>
  <td>Heptane</td>
  <td>544.1</td>
  <td>.2</td>
  <td>.79</td>
  <td>0</td>
  <td>3.56</td>
  <td>3.04</td>
  <td>.44</td>
  <td>7.9</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-057</td>
  <td>303F001</td>
  <td>1/29/10</td>
  <td>19:50:16</td>
  <td>Heptane</td>
  <td>544.4</td>
  <td>.2</td>
  <td>.79</td>
  <td>0</td>
  <td>3.1</td>
  <td>2.49</td>
  <td>.54</td>
  <td>6.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-058</td>
  <td>176F001</td>
  <td>2/4/10</td>
  <td>2:32:01</td>
  <td>Methanol</td>
  <td>773.3</td>
  <td>.18</td>
  <td>.82</td>
  <td>0</td>
  <td>3.69</td>
  <td>-</td>
  <td>.42</td>
  <td>29.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-059</td>
  <td>176R001</td>
  <td>2/4/10</td>
  <td>0:26:28</td>
  <td>Methanol</td>
  <td>769.2</td>
  <td>.18</td>
  <td>.82</td>
  <td>0</td>
  <td>2.93</td>
  <td>1.39</td>
  <td>.43</td>
  <td>17.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-060</td>
  <td>204F001</td>
  <td>2/4/10</td>
  <td>3:26:05</td>
  <td>Methanol</td>
  <td>773.7</td>
  <td>.18</td>
  <td>.82</td>
  <td>0</td>
  <td>3.43</td>
  <td>-</td>
  <td>.45</td>
  <td>23.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-061</td>
  <td>204R001</td>
  <td>2/4/10</td>
  <td>3:52:39</td>
  <td>Methanol</td>
  <td>774.1</td>
  <td>.18</td>
  <td>.82</td>
  <td>0</td>
  <td>3.68</td>
  <td>2</td>
  <td>.41</td>
  <td>25.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-062</td>
  <td>301F001</td>
  <td>3/11/10</td>
  <td>21:37:48</td>
  <td>Heptane</td>
  <td>761.8</td>
  <td>.18</td>
  <td>.82</td>
  <td>0</td>
  <td>3.43</td>
  <td>3.17</td>
  <td>.39</td>
  <td>4.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-063</td>
  <td>301F002</td>
  <td>3/11/10</td>
  <td>23:07:51</td>
  <td>Heptane</td>
  <td>767.6</td>
  <td>.18</td>
  <td>.81</td>
  <td>0</td>
  <td>2.15</td>
  <td>0</td>
  <td>.51</td>
  <td>9.6</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-064</td>
  <td>302F001</td>
  <td>3/11/10</td>
  <td>22:12:39</td>
  <td>Heptane</td>
  <td>764.6</td>
  <td>.18</td>
  <td>.81</td>
  <td>0</td>
  <td>2.69</td>
  <td>2.07</td>
  <td>.6</td>
  <td>5.5</td>
  <td>Extinction</td>
 </tr>
</table>


NASA/TP-2015-216046


21




<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>time, Burn s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>FLEX-066</td>
  <td>189F001</td>
  <td>3/19/10</td>
  <td>9:26:45</td>
  <td>Methanol</td>
  <td>766.8</td>
  <td>.15</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>2.52</td>
  <td>1.32</td>
  <td>.38</td>
  <td>12.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-067</td>
  <td>189F002</td>
  <td>3/19/10</td>
  <td>10:17:06</td>
  <td>Methanol</td>
  <td>767.7</td>
  <td>.15</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>3.97</td>
  <td>3.3</td>
  <td>.36</td>
  <td>14.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-068</td>
  <td>189R003</td>
  <td>3/19/10</td>
  <td>12:04:45</td>
  <td>Methanol</td>
  <td>768.8</td>
  <td>.15</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>2.38</td>
  <td>1.29</td>
  <td>.39</td>
  <td>10.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-069</td>
  <td>193R002</td>
  <td>3/23/10</td>
  <td>10:23:00</td>
  <td>Heptane</td>
  <td>767.1</td>
  <td>.14</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>1.1</td>
  <td>0</td>
  <td>.94</td>
  <td>1.3</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-070</td>
  <td>193F001</td>
  <td>3/23/10</td>
  <td>7:25:43</td>
  <td>Heptane</td>
  <td>761</td>
  <td>.15</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>4.67</td>
  <td>4.6</td>
  <td>.41</td>
  <td>1.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-071</td>
  <td>189R002</td>
  <td>3/19/10</td>
  <td>11:19:22</td>
  <td>Methanol</td>
  <td>768.3</td>
  <td>.15</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>2.25</td>
  <td>-</td>
  <td>.4</td>
  <td>8.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-072</td>
  <td>193R001</td>
  <td>3/23/10</td>
  <td>9:06:37</td>
  <td>Heptane</td>
  <td>765.2</td>
  <td>.15</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>1.13</td>
  <td>-</td>
  <td>.52</td>
  <td>2.5</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-073</td>
  <td>193F001</td>
  <td>3/23/10</td>
  <td>7:25:43</td>
  <td>Heptane</td>
  <td>761</td>
  <td>.15</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>4.64</td>
  <td>4.58</td>
  <td>.56</td>
  <td>1.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-074</td>
  <td>221F001</td>
  <td>3/23/10</td>
  <td>9:44:36</td>
  <td>Heptane</td>
  <td>765.9</td>
  <td>.15</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>1.33</td>
  <td>-</td>
  <td>.77</td>
  <td>2.3</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-075</td>
  <td>203R002</td>
  <td>3/29/10</td>
  <td>21:06:40</td>
  <td>Methanol</td>
  <td>770.8</td>
  <td>.13</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>2.54</td>
  <td>1.78</td>
  <td>.37</td>
  <td>9.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-076</td>
  <td>203F001</td>
  <td>3/29/10</td>
  <td>19:24:36</td>
  <td>Methanol</td>
  <td>769.5</td>
  <td>.13</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>3.21</td>
  <td>2.78</td>
  <td>.37</td>
  <td>8.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-077</td>
  <td>175R001</td>
  <td>3/29/10</td>
  <td>18:39:20</td>
  <td>Methanol</td>
  <td>768.4</td>
  <td>.14</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>3.33</td>
  <td>2.91</td>
  <td>.34</td>
  <td>8.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-078</td>
  <td>175F001</td>
  <td>3/29/10</td>
  <td>17:49:23</td>
  <td>Methanol</td>
  <td>766</td>
  <td>.14</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>2.66</td>
  <td>1.66</td>
  <td>.35</td>
  <td>12.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-079</td>
  <td>179F001</td>
  <td>3/30/10</td>
  <td>0:40:16</td>
  <td>Heptane</td>
  <td>768.1</td>
  <td>.13</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>2.92</td>
  <td>2.86</td>
  <td>.25</td>
  <td>1.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-080</td>
  <td>207F001</td>
  <td>3/30/10</td>
  <td>2:29:19</td>
  <td>Heptane</td>
  <td>770</td>
  <td>.13</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-081</td>
  <td>207F002</td>
  <td>3/30/10</td>
  <td>3:59:28</td>
  <td>Heptane</td>
  <td>770.2</td>
  <td>.13</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>1.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-082</td>
  <td>304F001</td>
  <td>4/19/10</td>
  <td>17:19:17</td>
  <td>Methanol</td>
  <td>764.6</td>
  <td>.13</td>
  <td>.87</td>
  <td>0</td>
  <td>0</td>
  <td>2.84</td>
  <td>2.39</td>
  <td>.35</td>
  <td>7.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-083</td>
  <td>304F002</td>
  <td>4/19/10</td>
  <td>21:18:05</td>
  <td>Methanol</td>
  <td>772</td>
  <td>.12</td>
  <td>.87</td>
  <td>0</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>5.45</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-084</td>
  <td>304R001</td>
  <td>4/19/10</td>
  <td>17:51:24</td>
  <td>Methanol</td>
  <td>767.2</td>
  <td>.12</td>
  <td>.87</td>
  <td>0</td>
  <td>0</td>
  <td>2.35</td>
  <td>1.42</td>
  <td>.35</td>
  <td>10.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-085</td>
  <td>304R002</td>
  <td>4/19/10</td>
  <td>20:12:58</td>
  <td>Methanol</td>
  <td>771.2</td>
  <td>.12</td>
  <td>.87</td>
  <td>0</td>
  <td>0</td>
  <td>2.4</td>
  <td>1.77</td>
  <td>.35</td>
  <td>9.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-086</td>
  <td>305F002</td>
  <td>4/19/10</td>
  <td>19:16:37</td>
  <td>Methanol</td>
  <td>770</td>
  <td>.12</td>
  <td>.87</td>
  <td>0</td>
  <td>0</td>
  <td>3.07</td>
  <td>2.56</td>
  <td>.35</td>
  <td>9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-087</td>
  <td>305F003</td>
  <td>4/19/10</td>
  <td>20:38:54</td>
  <td>Methanol</td>
  <td>771.2</td>
  <td>.12</td>
  <td>.87</td>
  <td>0</td>
  <td>0</td>
  <td>2.64</td>
  <td>1.92</td>
  <td>.38</td>
  <td>9.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-088</td>
  <td>053R001</td>
  <td>5/5/10</td>
  <td>22:37:54</td>
  <td>Methanol</td>
  <td>537.5</td>
  <td>.25</td>
  <td>.6</td>
  <td>.15</td>
  <td>0</td>
  <td>3.01</td>
  <td>-</td>
  <td>.53</td>
  <td>14.8</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-089</td>
  <td>053F001</td>
  <td>5/5/10</td>
  <td>22:19:33</td>
  <td>Methanol</td>
  <td>537.4</td>
  <td>.25</td>
  <td>.6</td>
  <td>.15</td>
  <td>0</td>
  <td>3.7</td>
  <td>-</td>
  <td>.51</td>
  <td>24</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-090</td>
  <td>141R001</td>
  <td>5/6/10</td>
  <td>0:07:51</td>
  <td>Methanol</td>
  <td>539.2</td>
  <td>.25</td>
  <td>.6</td>
  <td>.15</td>
  <td>0</td>
  <td>3.62</td>
  <td>-</td>
  <td>.53</td>
  <td>20.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-091</td>
  <td>141F001</td>
  <td>5/5/10</td>
  <td>23:10:01</td>
  <td>Methanol</td>
  <td>538.3</td>
  <td>.25</td>
  <td>.6</td>
  <td>.15</td>
  <td>0</td>
  <td>3.51</td>
  <td>-</td>
  <td>.51</td>
  <td>18</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-092</td>
  <td>061F002</td>
  <td>6/14/10</td>
  <td>22:54:56</td>
  <td>Heptane</td>
  <td>536.3</td>
  <td>.25</td>
  <td>.6</td>
  <td>.15</td>
  <td>0</td>
  <td>3.41</td>
  <td>-</td>
  <td>.55</td>
  <td>21.7</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-093</td>
  <td>149F001</td>
  <td>6/15/10</td>
  <td>0:32:31</td>
  <td>Heptane</td>
  <td>537.3</td>
  <td>.25</td>
  <td>.6</td>
  <td>.15</td>
  <td>0</td>
  <td>2.48</td>
  <td>0</td>
  <td>.71</td>
  <td>8.3</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-094</td>
  <td>C08H101</td>
  <td>6/15/10</td>
  <td>2:10:43</td>
  <td>Heptane</td>
  <td>533.6</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.53</td>
  <td>2.76</td>
  <td>.51</td>
  <td>10.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-095</td>
  <td>C08H201</td>
  <td>6/15/10</td>
  <td>3:22:41</td>
  <td>Heptane</td>
  <td>534.4</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.6</td>
  <td>3.04</td>
  <td>.58</td>
  <td>8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-096</td>
  <td>C08H301</td>
  <td>6/15/10</td>
  <td>4:37:39</td>
  <td>Heptane</td>
  <td>534.4</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>5.2</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-097</td>
  <td>C08M101</td>
  <td>6/16/10</td>
  <td>22:43:35</td>
  <td>Methanol</td>
  <td>534.2</td>
  <td>.23</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>4.25</td>
  <td>2.6</td>
  <td>.45</td>
  <td>26.5</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-098</td>
  <td>C09M201</td>
  <td>6/21/10</td>
  <td>14:21:26</td>
  <td>Methanol</td>
  <td>537.1</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>3.64</td>
  <td>1.74</td>
  <td>.47</td>
  <td>22.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-099</td>
  <td>C09M101</td>
  <td>6/21/10</td>
  <td>12:57:34</td>
  <td>Methanol</td>
  <td>535</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>4.28</td>
  <td>2.32</td>
  <td>.42</td>
  <td>33</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-100</td>
  <td>C09H101</td>
  <td>6/29/10</td>
  <td>8:30:46</td>
  <td>Heptane</td>
  <td>536.7</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>4.14</td>
  <td>3.98</td>
  <td>.34</td>
  <td>6.1</td>
  <td>Extinction</td>
 </tr>
</table>


NASA/TP-2015-216046


22




<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>Burn time, s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>FLEX-101</td>
  <td>C09H201</td>
  <td>6/29/10</td>
  <td>9:38:10</td>
  <td>Heptane</td>
  <td>538.7</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>3.88</td>
  <td>3.45</td>
  <td>.5</td>
  <td>6.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-102</td>
  <td>C10H101</td>
  <td>6/29/10</td>
  <td>11:21:09</td>
  <td>Heptane</td>
  <td>534.2</td>
  <td>.21</td>
  <td>.49</td>
  <td>.3</td>
  <td>0</td>
  <td>3.57</td>
  <td>3.43</td>
  <td>.33</td>
  <td>4.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-103</td>
  <td>C10H201</td>
  <td>6/29/10</td>
  <td>11:56:02</td>
  <td>Heptane</td>
  <td>534.3</td>
  <td>.21</td>
  <td>.49</td>
  <td>.3</td>
  <td>0</td>
  <td>4</td>
  <td>3.88</td>
  <td>.35</td>
  <td>3.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-104</td>
  <td>C08M201</td>
  <td>6/16/10</td>
  <td>23:04:00</td>
  <td>Methanol</td>
  <td>534.1</td>
  <td>.23</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.6</td>
  <td>1.58</td>
  <td>.49</td>
  <td>23.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-105</td>
  <td>C08M301</td>
  <td>6/16/10</td>
  <td>23:29:19</td>
  <td>Methanol</td>
  <td>534.6</td>
  <td>.23</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>4.17</td>
  <td>2</td>
  <td>.47</td>
  <td>30.7</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-106</td>
  <td>C09M401</td>
  <td>6/21/10</td>
  <td>15:52:51</td>
  <td>Methanol</td>
  <td>538.3</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>3.08</td>
  <td>1.75</td>
  <td>.51</td>
  <td>14.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-107</td>
  <td>C08M401</td>
  <td>6/16/10</td>
  <td>23:51:26</td>
  <td>Methanol</td>
  <td>535</td>
  <td>.23</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.18</td>
  <td>-</td>
  <td>.52</td>
  <td>15.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-108</td>
  <td>C09M301</td>
  <td>6/21/10</td>
  <td>15:35:57</td>
  <td>Methanol</td>
  <td>538.3</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>3.75</td>
  <td>-</td>
  <td>.47</td>
  <td>24.3</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-109</td>
  <td>C10M102</td>
  <td>8/31/10</td>
  <td>5:38:01</td>
  <td>Methanol</td>
  <td>536.5</td>
  <td>.21</td>
  <td>.49</td>
  <td>.3</td>
  <td>0</td>
  <td>3.56</td>
  <td>1.92</td>
  <td>.42</td>
  <td>-</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-110</td>
  <td>C10M201</td>
  <td>8/31/10</td>
  <td>7:16:40</td>
  <td>Methanol</td>
  <td>537</td>
  <td>.21</td>
  <td>.49</td>
  <td>.3</td>
  <td>0</td>
  <td>2.83</td>
  <td>1.57</td>
  <td>.45</td>
  <td>13</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-111</td>
  <td>C10M303</td>
  <td>8/31/10</td>
  <td>8:58:24</td>
  <td>Methanol</td>
  <td>536.9</td>
  <td>.21</td>
  <td>.49</td>
  <td>.3</td>
  <td>0</td>
  <td>3.37</td>
  <td>2.1</td>
  <td>.45</td>
  <td>16.4</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-112</td>
  <td>C10M401</td>
  <td>9/1/10</td>
  <td>15:27:44</td>
  <td>Methanol</td>
  <td>530.7</td>
  <td>.21</td>
  <td>.49</td>
  <td>.3</td>
  <td>0</td>
  <td>3.99</td>
  <td>2.35</td>
  <td>.43</td>
  <td>25.2</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-113</td>
  <td>C11M101</td>
  <td>9/1/10</td>
  <td>19:17:58</td>
  <td>Methanol</td>
  <td>534.6</td>
  <td>.2</td>
  <td>.45</td>
  <td>.35</td>
  <td>0</td>
  <td>4.2</td>
  <td>2.85</td>
  <td>.49</td>
  <td>18.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-114</td>
  <td>C11M201</td>
  <td>9/6/10</td>
  <td>19:14:22</td>
  <td>Methanol</td>
  <td>0</td>
  <td>.2</td>
  <td>.45</td>
  <td>.35</td>
  <td>0</td>
  <td>3.23</td>
  <td>1.68</td>
  <td>.42</td>
  <td>18.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-115</td>
  <td>C11M301</td>
  <td>9/1/10</td>
  <td>20:40:16</td>
  <td>Methanol</td>
  <td>535.8</td>
  <td>.2</td>
  <td>.45</td>
  <td>.35</td>
  <td>0</td>
  <td>3.97</td>
  <td>2.61</td>
  <td>.41</td>
  <td>22.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-116</td>
  <td>C11M401</td>
  <td>9/1/10</td>
  <td>20:57:41</td>
  <td>Methanol</td>
  <td>536.3</td>
  <td>.2</td>
  <td>.45</td>
  <td>.35</td>
  <td>0</td>
  <td>3.16</td>
  <td>1.57</td>
  <td>.46</td>
  <td>16.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-117</td>
  <td>C11H101</td>
  <td>9/6/10</td>
  <td>18:14:53</td>
  <td>Heptane</td>
  <td>531.1</td>
  <td>.2</td>
  <td>.45</td>
  <td>.35</td>
  <td>0</td>
  <td>3.84</td>
  <td>3.77</td>
  <td>.25</td>
  <td>2.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-118</td>
  <td>C11H201</td>
  <td>9/6/10</td>
  <td>19:14:22</td>
  <td>Heptane</td>
  <td>532.8</td>
  <td>.2</td>
  <td>.44</td>
  <td>.35</td>
  <td>0</td>
  <td>3.03</td>
  <td>2.93</td>
  <td>.38</td>
  <td>2.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-119</td>
  <td>C12H103</td>
  <td>9/7/10</td>
  <td>1:50:01</td>
  <td>Heptane</td>
  <td>532.6</td>
  <td>.18</td>
  <td>.42</td>
  <td>.4</td>
  <td>0</td>
  <td>2.6</td>
  <td>2.48</td>
  <td>.37</td>
  <td>1.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-120</td>
  <td>C12H201</td>
  <td>9/7/10</td>
  <td>1:08:26</td>
  <td>Heptane</td>
  <td>532.5</td>
  <td>.18</td>
  <td>.42</td>
  <td>.4</td>
  <td>0</td>
  <td>2.45</td>
  <td>2.39</td>
  <td>.38</td>
  <td>1.43</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-121</td>
  <td>C12M101</td>
  <td>9/8/10</td>
  <td>19:21:31</td>
  <td>Methanol</td>
  <td>526.3</td>
  <td>.18</td>
  <td>.42</td>
  <td>.4</td>
  <td>0</td>
  <td>4.25</td>
  <td>3.92</td>
  <td>.34</td>
  <td>8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-122</td>
  <td>C12M201</td>
  <td>9/8/10</td>
  <td>21:44:37</td>
  <td>Methanol</td>
  <td>531.2</td>
  <td>.18</td>
  <td>.42</td>
  <td>.4</td>
  <td>0</td>
  <td>3.46</td>
  <td>2.58</td>
  <td>.41</td>
  <td>13.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-123</td>
  <td>C12M301</td>
  <td>9/8/10</td>
  <td>22:16:51</td>
  <td>Methanol</td>
  <td>532</td>
  <td>.18</td>
  <td>.42</td>
  <td>.4</td>
  <td>0</td>
  <td>4.13</td>
  <td>3.79</td>
  <td>.35</td>
  <td>8.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-124</td>
  <td>C12M401</td>
  <td>9/8/10</td>
  <td>22:45:54</td>
  <td>Methanol</td>
  <td>532.4</td>
  <td>.18</td>
  <td>.42</td>
  <td>.4</td>
  <td>0</td>
  <td>2.87</td>
  <td>2.74</td>
  <td>.3</td>
  <td>2.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-125</td>
  <td>C13M103</td>
  <td>9/13/10</td>
  <td>21:07:02</td>
  <td>Methanol</td>
  <td>537.2</td>
  <td>.17</td>
  <td>.38</td>
  <td>.45</td>
  <td>0</td>
  <td>3.63</td>
  <td>3.37</td>
  <td>.35</td>
  <td>5.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-126</td>
  <td>C13M201</td>
  <td>9/13/10</td>
  <td>18:11:39</td>
  <td>Methanol</td>
  <td>536.1</td>
  <td>.17</td>
  <td>.38</td>
  <td>.45</td>
  <td>0</td>
  <td>2.8</td>
  <td>1.84</td>
  <td>.4</td>
  <td>11.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-127</td>
  <td>C13M301</td>
  <td>9/13/10</td>
  <td>19:22:49</td>
  <td>Methanol</td>
  <td>536.7</td>
  <td>.17</td>
  <td>.38</td>
  <td>.45</td>
  <td>0</td>
  <td>3.22</td>
  <td>2.53</td>
  <td>.38</td>
  <td>11</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-128</td>
  <td>C13M401</td>
  <td>9/13/10</td>
  <td>19:49:24</td>
  <td>Methanol</td>
  <td>537.3</td>
  <td>.17</td>
  <td>.38</td>
  <td>.45</td>
  <td>0</td>
  <td>2.91</td>
  <td>-</td>
  <td>.39</td>
  <td>11.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-129</td>
  <td>C13H102</td>
  <td>9/17/10</td>
  <td>1:32:49</td>
  <td>Heptane</td>
  <td>536.2</td>
  <td>.17</td>
  <td>.38</td>
  <td>.45</td>
  <td>0</td>
  <td>3.33</td>
  <td>3.34</td>
  <td>.33</td>
  <td>.55</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-130</td>
  <td>C13H201</td>
  <td>9/17/10</td>
  <td>3:55:59</td>
  <td>Heptane</td>
  <td>537.2</td>
  <td>.17</td>
  <td>.38</td>
  <td>.45</td>
  <td>0</td>
  <td>2.91</td>
  <td>2.89</td>
  <td>.05</td>
  <td>.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-131</td>
  <td>C21H101</td>
  <td>10/6/10</td>
  <td>11:28:52</td>
  <td>Heptane</td>
  <td>763.9</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>1.72</td>
  <td>.52</td>
  <td>.61</td>
  <td>4.9</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-132</td>
  <td>C21H201</td>
  <td>10/6/10</td>
  <td>12:59:06</td>
  <td>Heptane</td>
  <td>765.2</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>2.63</td>
  <td>.53</td>
  <td>.6</td>
  <td>12.4</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-133</td>
  <td>C21H301</td>
  <td>10/6/10</td>
  <td>13:59:59</td>
  <td>Heptane</td>
  <td>766.7</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.25</td>
  <td>.55</td>
  <td>.56</td>
  <td>19</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-134</td>
  <td>C21H401</td>
  <td>10/6/10</td>
  <td>14:57:06</td>
  <td>Heptane</td>
  <td>767.2</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.66</td>
  <td>2.88</td>
  <td>.56</td>
  <td>9.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-135</td>
  <td>C21H501</td>
  <td>10/6/10</td>
  <td>16:22:15</td>
  <td>Heptane</td>
  <td>768.2</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>2.78</td>
  <td>0</td>
  <td>.59</td>
  <td>10.8</td>
  <td>Completion</td>
 </tr>
</table>


NASA/TP-2015-216046


23




<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>Burn time, s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>FLEX-136</td>
  <td>C21H302</td>
  <td>10/6/10</td>
  <td>17:30:58</td>
  <td>Heptane</td>
  <td>768.1</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.08</td>
  <td>-</td>
  <td>.51</td>
  <td>17</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-137</td>
  <td>C21H303</td>
  <td>10/6/10</td>
  <td>17:53:35</td>
  <td>Heptane</td>
  <td>768.2</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.13</td>
  <td>-</td>
  <td>.55</td>
  <td>17.5</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-138</td>
  <td>C21H304</td>
  <td>10/6/10</td>
  <td>18:08:43</td>
  <td>Heptane</td>
  <td>768.6</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-139</td>
  <td>C21H305</td>
  <td>10/6/10</td>
  <td>19:09:45</td>
  <td>Heptane</td>
  <td>768</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>1.75</td>
  <td>-</td>
  <td>.63</td>
  <td>5.4</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-140</td>
  <td>C14M101</td>
  <td>11/4/10</td>
  <td>16:52:39</td>
  <td>Methanol</td>
  <td>533.5</td>
  <td>.15</td>
  <td>.35</td>
  <td>.5</td>
  <td>0</td>
  <td>3.98</td>
  <td>3.95</td>
  <td>.2</td>
  <td>1.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-141</td>
  <td>C14M201</td>
  <td>11/4/10</td>
  <td>18:07:51</td>
  <td>Methanol</td>
  <td>534.1</td>
  <td>.15</td>
  <td>.35</td>
  <td>.5</td>
  <td>0</td>
  <td>2.86</td>
  <td>2.73</td>
  <td>.3</td>
  <td>2.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-142</td>
  <td>C14M301</td>
  <td>11/4/10</td>
  <td>19:11:39</td>
  <td>Methanol</td>
  <td>534.5</td>
  <td>.15</td>
  <td>.35</td>
  <td>.5</td>
  <td>0</td>
  <td>1.86</td>
  <td>1.48</td>
  <td>.39</td>
  <td>3.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-143</td>
  <td>C14M302</td>
  <td>11/4/10</td>
  <td>20:19:22</td>
  <td>Methanol</td>
  <td>534.7</td>
  <td>.15</td>
  <td>.35</td>
  <td>.5</td>
  <td>0</td>
  <td>2.25</td>
  <td>2.06</td>
  <td>.36</td>
  <td>2.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-144</td>
  <td>C01M101</td>
  <td>11/16/10</td>
  <td>9:42:08</td>
  <td>Methanol</td>
  <td>761.9</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>3.53</td>
  <td>1.53</td>
  <td>.45</td>
  <td>23.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-145</td>
  <td>C01M201</td>
  <td>11/16/10</td>
  <td>10:21:24</td>
  <td>Methanol</td>
  <td>763.5</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>3.33</td>
  <td>1.61</td>
  <td>.45</td>
  <td>20</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-146</td>
  <td>C01M301</td>
  <td>11/16/10</td>
  <td>10:54:23</td>
  <td>Methanol</td>
  <td>765.5</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>4.35</td>
  <td>1.95</td>
  <td>.41</td>
  <td>39.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-147</td>
  <td>C13M102</td>
  <td>9/13/10</td>
  <td>17:35:49</td>
  <td>Methanol</td>
  <td>535.7</td>
  <td>.17</td>
  <td>.38</td>
  <td>.45</td>
  <td>0</td>
  <td>3.02</td>
  <td>2.49</td>
  <td>.4</td>
  <td>7.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-148</td>
  <td>C01H101</td>
  <td>11/18/10</td>
  <td>8:39:27</td>
  <td>Heptane</td>
  <td>764.4</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>2.58</td>
  <td>1.15</td>
  <td>.54</td>
  <td>11.8</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-149</td>
  <td>C01H201</td>
  <td>11/18/10</td>
  <td>9:25:38</td>
  <td>Heptane</td>
  <td>766.2</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>2.21</td>
  <td>.82</td>
  <td>.53</td>
  <td>8.9</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-150</td>
  <td>C01H302</td>
  <td>11/18/10</td>
  <td>10:17:02</td>
  <td>Heptane</td>
  <td>767.6</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>3.18</td>
  <td>2.54</td>
  <td>.46</td>
  <td>8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-151</td>
  <td>C03M101</td>
  <td>12/8/10</td>
  <td>18:31:22</td>
  <td>Methanol</td>
  <td>762.5</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>3.86</td>
  <td>-</td>
  <td>.36</td>
  <td>31.3</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-152</td>
  <td>C03M201</td>
  <td>12/8/10</td>
  <td>20:10:32</td>
  <td>Methanol</td>
  <td>765</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>3.33</td>
  <td>1.23</td>
  <td>.43</td>
  <td>23.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-153</td>
  <td>C03M301</td>
  <td>12/8/10</td>
  <td>21:08:17</td>
  <td>Methanol</td>
  <td>765.6</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>2.78</td>
  <td>1.19</td>
  <td>.42</td>
  <td>15.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-154</td>
  <td>C03H101</td>
  <td>12/9/10</td>
  <td>16:02:14</td>
  <td>Heptane</td>
  <td>762.3</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>3.7</td>
  <td>3.6</td>
  <td>.34</td>
  <td>2.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-155</td>
  <td>C03H201</td>
  <td>12/9/10</td>
  <td>17:49:08</td>
  <td>Heptane</td>
  <td>764.9</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>2.73</td>
  <td>2.52</td>
  <td>.39</td>
  <td>2.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-157</td>
  <td>C03H401</td>
  <td>12/9/10</td>
  <td>19:12:27</td>
  <td>Heptane</td>
  <td>765.7</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>1.34</td>
  <td>.45</td>
  <td>.48</td>
  <td>3.2</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-158</td>
  <td>C05M101</td>
  <td>12/14/10</td>
  <td>13:41:00</td>
  <td>Methanol</td>
  <td>762.1</td>
  <td>.16</td>
  <td>.59</td>
  <td>.25</td>
  <td>0</td>
  <td>4.24</td>
  <td>3.96</td>
  <td>.3</td>
  <td>7.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-159</td>
  <td>C05M201</td>
  <td>12/14/10</td>
  <td>14:30:46</td>
  <td>Methanol</td>
  <td>764.4</td>
  <td>.16</td>
  <td>.59</td>
  <td>.25</td>
  <td>0</td>
  <td>3.7</td>
  <td>3.22</td>
  <td>.37</td>
  <td>10.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-160</td>
  <td>C05M301</td>
  <td>12/14/10</td>
  <td>15:17:59</td>
  <td>Methanol</td>
  <td>765.5</td>
  <td>.16</td>
  <td>.59</td>
  <td>.25</td>
  <td>0</td>
  <td>2.71</td>
  <td>1.34</td>
  <td>.38</td>
  <td>14.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-161</td>
  <td>C05M401</td>
  <td>12/14/10</td>
  <td>17:51:58</td>
  <td>Methanol</td>
  <td>767.6</td>
  <td>.16</td>
  <td>.59</td>
  <td>.25</td>
  <td>0</td>
  <td>2.77</td>
  <td>1.52</td>
  <td>.38</td>
  <td>14.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-162</td>
  <td>C06M101</td>
  <td>12/28/10</td>
  <td>11:41:39</td>
  <td>Methanol</td>
  <td>763.3</td>
  <td>.15</td>
  <td>.54</td>
  <td>.32</td>
  <td>0</td>
  <td>3.72</td>
  <td>3.5</td>
  <td>.28</td>
  <td>6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-163</td>
  <td>C06M201</td>
  <td>12/28/10</td>
  <td>12:05:23</td>
  <td>Methanol</td>
  <td>764.4</td>
  <td>.15</td>
  <td>.53</td>
  <td>.32</td>
  <td>0</td>
  <td>3.05</td>
  <td>2.54</td>
  <td>.37</td>
  <td>8.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-164</td>
  <td>C06M301</td>
  <td>12/28/10</td>
  <td>13:00:43</td>
  <td>Methanol</td>
  <td>765.9</td>
  <td>.15</td>
  <td>.53</td>
  <td>.32</td>
  <td>0</td>
  <td>2.59</td>
  <td>1.63</td>
  <td>.37</td>
  <td>11.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-165</td>
  <td>C06M401</td>
  <td>12/28/10</td>
  <td>13:36:43</td>
  <td>Methanol</td>
  <td>766.1</td>
  <td>.15</td>
  <td>.53</td>
  <td>.32</td>
  <td>0</td>
  <td>2.59</td>
  <td>1.79</td>
  <td>.42</td>
  <td>8.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-166</td>
  <td>C03H302</td>
  <td>12/9/10</td>
  <td>18:51:34</td>
  <td>Heptane</td>
  <td>765.4</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>1.96</td>
  <td>1.39</td>
  <td>.54</td>
  <td>3.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-167</td>
  <td>C07M101</td>
  <td>1/12/11</td>
  <td>21:56:45</td>
  <td>Methanol</td>
  <td>760.8</td>
  <td>.14</td>
  <td>.5</td>
  <td>.36</td>
  <td>0</td>
  <td>3.22</td>
  <td>3.08</td>
  <td>.28</td>
  <td>3.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-168</td>
  <td>C07M201</td>
  <td>1/12/11</td>
  <td>22:11:40</td>
  <td>Methanol</td>
  <td>761.6</td>
  <td>.14</td>
  <td>.5</td>
  <td>.36</td>
  <td>0</td>
  <td>2.32</td>
  <td>1.84</td>
  <td>.37</td>
  <td>5.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-169</td>
  <td>C15M101</td>
  <td>1/18/11</td>
  <td>12:54:25</td>
  <td>Methanol</td>
  <td>763.4</td>
  <td>.21</td>
  <td>.64</td>
  <td>.15</td>
  <td>0</td>
  <td>3.03</td>
  <td>1.57</td>
  <td>.48</td>
  <td>15.6</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-170</td>
  <td>C15M201</td>
  <td>1/18/11</td>
  <td>14:19:29</td>
  <td>Methanol</td>
  <td>766.1</td>
  <td>.21</td>
  <td>.64</td>
  <td>.15</td>
  <td>0</td>
  <td>3.05</td>
  <td>1.28</td>
  <td>.51</td>
  <td>16.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-171</td>
  <td>C15M301</td>
  <td>1/18/11</td>
  <td>15:58:46</td>
  <td>Methanol</td>
  <td>766.7</td>
  <td>.21</td>
  <td>.64</td>
  <td>.15</td>
  <td>0</td>
  <td>3.53</td>
  <td>1.59</td>
  <td>.46</td>
  <td>23.6</td>
  <td>Extinction</td>
 </tr>
</table>


NASA/TP-2015-216046


24




<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>Burn time, s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>FLEX-172</td>
  <td>C03H501</td>
  <td>2/21/11</td>
  <td>17:56:40</td>
  <td>Heptane</td>
  <td>759.9</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>3.74</td>
  <td>3.68</td>
  <td>.35</td>
  <td>2.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-173</td>
  <td>C03H601</td>
  <td>2/21/11</td>
  <td>19:07:48</td>
  <td>Heptane</td>
  <td>762</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>2.4</td>
  <td>1.96</td>
  <td>.46</td>
  <td>4.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-174</td>
  <td>C03H701</td>
  <td>2/21/11</td>
  <td>19:17:37</td>
  <td>Heptane</td>
  <td>762.1</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>1.35</td>
  <td>.47</td>
  <td>.5</td>
  <td>3.6</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-175</td>
  <td>C08H502</td>
  <td>2/21/11</td>
  <td>22:15:54</td>
  <td>Heptane</td>
  <td>531.7</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>2.5</td>
  <td>.21</td>
  <td>.56</td>
  <td>11.2</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-176</td>
  <td>C08H601</td>
  <td>2/21/11</td>
  <td>22:43:37</td>
  <td>Heptane</td>
  <td>532.1</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>2.88</td>
  <td>-</td>
  <td>.55</td>
  <td>15.6</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-177</td>
  <td>C08M501</td>
  <td>4/18/11</td>
  <td>20:27:36</td>
  <td>Methanol</td>
  <td>536.9</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>4.53</td>
  <td>-</td>
  <td>.46</td>
  <td>38.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-178</td>
  <td>C08M601</td>
  <td>4/18/11</td>
  <td>20:52:24</td>
  <td>Methanol</td>
  <td>537</td>
  <td>.24</td>
  <td>.56</td>
  <td>.2</td>
  <td>0</td>
  <td>3.02</td>
  <td>1.35</td>
  <td>.52</td>
  <td>14.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-179</td>
  <td>C09H501</td>
  <td>4/20/11</td>
  <td>17:56:25</td>
  <td>Heptane</td>
  <td>533.6</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>3.32</td>
  <td>2.61</td>
  <td>.5</td>
  <td>8.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-180</td>
  <td>C09H601</td>
  <td>4/20/11</td>
  <td>18:22:58</td>
  <td>Heptane</td>
  <td>534.4</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>2.07</td>
  <td>.48</td>
  <td>.57</td>
  <td>7.5</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-181</td>
  <td>C02H101</td>
  <td>4/20/11</td>
  <td>20:00:24</td>
  <td>Heptane</td>
  <td>758.4</td>
  <td>.19</td>
  <td>.71</td>
  <td>.1</td>
  <td>0</td>
  <td>3.4</td>
  <td>3.13</td>
  <td>.41</td>
  <td>4.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-182</td>
  <td>C02H201</td>
  <td>4/20/11</td>
  <td>21:14:08</td>
  <td>Heptane</td>
  <td>759.1</td>
  <td>.19</td>
  <td>.71</td>
  <td>.1</td>
  <td>0</td>
  <td>2.48</td>
  <td>1.68</td>
  <td>.49</td>
  <td>7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-183</td>
  <td>C02H202</td>
  <td>4/20/11</td>
  <td>21:26:02</td>
  <td>Heptane</td>
  <td>759</td>
  <td>.19</td>
  <td>.71</td>
  <td>.1</td>
  <td>0</td>
  <td>1.64</td>
  <td>.49</td>
  <td>.54</td>
  <td>5.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-184</td>
  <td>C09M501</td>
  <td>8/8/11</td>
  <td>13:14:11</td>
  <td>Methanol</td>
  <td>534.4</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>3.72</td>
  <td>-</td>
  <td>.53</td>
  <td>26.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-185</td>
  <td>C09M502</td>
  <td>8/8/11</td>
  <td>13:30:14</td>
  <td>Methanol</td>
  <td>535.1</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>3.42</td>
  <td>-</td>
  <td>.51</td>
  <td>15.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-186</td>
  <td>C09M601</td>
  <td>8/8/11</td>
  <td>13:42:04</td>
  <td>Methanol</td>
  <td>535.2</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>2.8</td>
  <td>1.33</td>
  <td>.51</td>
  <td>12.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-187</td>
  <td>C09M701</td>
  <td>8/8/11</td>
  <td>14:52:15</td>
  <td>Methanol</td>
  <td>536.2</td>
  <td>.23</td>
  <td>.52</td>
  <td>.25</td>
  <td>0</td>
  <td>2.47</td>
  <td>1.21</td>
  <td>.52</td>
  <td>9.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-188</td>
  <td>C02M101</td>
  <td>8/8/11</td>
  <td>16:16:48</td>
  <td>Methanol</td>
  <td>758</td>
  <td>.19</td>
  <td>.71</td>
  <td>.1</td>
  <td>0</td>
  <td>3.38</td>
  <td>1.29</td>
  <td>.47</td>
  <td>21.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-189</td>
  <td>C02M201</td>
  <td>8/8/11</td>
  <td>17:49:19</td>
  <td>Methanol</td>
  <td>758.1</td>
  <td>.19</td>
  <td>.71</td>
  <td>.1</td>
  <td>0</td>
  <td>2.47</td>
  <td>1.08</td>
  <td>.46</td>
  <td>11</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-190</td>
  <td>C03M501</td>
  <td>8/9/11</td>
  <td>10:53:21</td>
  <td>Methanol</td>
  <td>761.2</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>3.77</td>
  <td>1.78</td>
  <td>.42</td>
  <td>30.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-191</td>
  <td>C03M601</td>
  <td>8/9/11</td>
  <td>12:28:41</td>
  <td>Methanol</td>
  <td>764.6</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>2.74</td>
  <td>.95</td>
  <td>.5</td>
  <td>14</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-192</td>
  <td>C03M701</td>
  <td>8/9/11</td>
  <td>12:46:53</td>
  <td>Methanol</td>
  <td>765.3</td>
  <td>.18</td>
  <td>.67</td>
  <td>.15</td>
  <td>0</td>
  <td>1.76</td>
  <td>.81</td>
  <td>.46</td>
  <td>5.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-193</td>
  <td>C04M101</td>
  <td>8/9/11</td>
  <td>17:07:27</td>
  <td>Methanol</td>
  <td>759.5</td>
  <td>.17</td>
  <td>.63</td>
  <td>.2</td>
  <td>0</td>
  <td>3.46</td>
  <td>-</td>
  <td>.39</td>
  <td>21.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-194</td>
  <td>C04M201</td>
  <td>8/9/11</td>
  <td>18:26:45</td>
  <td>Methanol</td>
  <td>759.1</td>
  <td>.17</td>
  <td>.63</td>
  <td>.2</td>
  <td>0</td>
  <td>2.77</td>
  <td>1.27</td>
  <td>.4</td>
  <td>15.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-195</td>
  <td>C04H101</td>
  <td>8/17/11</td>
  <td>22:31:20</td>
  <td>Heptane</td>
  <td>752</td>
  <td>.17</td>
  <td>.63</td>
  <td>.2</td>
  <td>0</td>
  <td>3.76</td>
  <td>3.71</td>
  <td>.29</td>
  <td>1.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-196</td>
  <td>C04H201</td>
  <td>8/17/11</td>
  <td>22:53:58</td>
  <td>Heptane</td>
  <td>752.5</td>
  <td>.17</td>
  <td>.63</td>
  <td>.2</td>
  <td>0</td>
  <td>2.9</td>
  <td>2.79</td>
  <td>.36</td>
  <td>1.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-197</td>
  <td>C01H501</td>
  <td>8/18/11</td>
  <td>0:24:31</td>
  <td>Heptane</td>
  <td>758.4</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>3.06</td>
  <td>2.28</td>
  <td>.52</td>
  <td>8.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-198</td>
  <td>C01H601</td>
  <td>8/18/11</td>
  <td>1:38:10</td>
  <td>Heptane</td>
  <td>759.8</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>3.04</td>
  <td>2.33</td>
  <td>.49</td>
  <td>8.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-199</td>
  <td>C01H701</td>
  <td>8/18/11</td>
  <td>1:55:56</td>
  <td>Heptane</td>
  <td>760.1</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>2.12</td>
  <td>.13</td>
  <td>.53</td>
  <td>8.7</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-200</td>
  <td>C01M501</td>
  <td>8/24/11</td>
  <td>15:07:47</td>
  <td>Methanol</td>
  <td>754</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>3.37</td>
  <td>.98</td>
  <td>.49</td>
  <td>21</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-201</td>
  <td>C01M602</td>
  <td>8/24/11</td>
  <td>15:56:17</td>
  <td>Methanol</td>
  <td>756.1</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>2.57</td>
  <td>1.13</td>
  <td>.47</td>
  <td>11.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-202</td>
  <td>C01M603</td>
  <td>8/24/11</td>
  <td>16:18:58</td>
  <td>Methanol</td>
  <td>756.9</td>
  <td>.2</td>
  <td>.75</td>
  <td>.05</td>
  <td>0</td>
  <td>2.4</td>
  <td>1.05</td>
  <td>.48</td>
  <td>10.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-203</td>
  <td>N01M101</td>
  <td>8/24/11</td>
  <td>21:05:01</td>
  <td>Methanol</td>
  <td>760.2</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>3.3</td>
  <td>1.42</td>
  <td>.47</td>
  <td>19.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-204</td>
  <td>N01M201</td>
  <td>8/24/11</td>
  <td>21:58:36</td>
  <td>Methanol</td>
  <td>761.6</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>2.75</td>
  <td>1.11</td>
  <td>.52</td>
  <td>12.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-206</td>
  <td>N01H101</td>
  <td>8/29/11</td>
  <td>19:04:50</td>
  <td>Heptane</td>
  <td>756.5</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>3.56</td>
  <td>-</td>
  <td>.43</td>
  <td>23.9</td>
  <td>Disruption</td>
 </tr>
</table>


NASA/TP-2015-216046


25




<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>Burn time, s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>FLEX-207</td>
  <td>N01H102</td>
  <td>8/29/11</td>
  <td>19:21:49</td>
  <td>Heptane</td>
  <td>757.3</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>3.58</td>
  <td>-</td>
  <td>.42</td>
  <td>24</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-208</td>
  <td>N01H201</td>
  <td>8/29/11</td>
  <td>20:28:30</td>
  <td>Heptane</td>
  <td>760.2</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>2.96</td>
  <td>.47</td>
  <td>.5</td>
  <td>17.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-209</td>
  <td>N01H202</td>
  <td>8/29/11</td>
  <td>21:54:40</td>
  <td>Heptane</td>
  <td>762.7</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>2.72</td>
  <td>1.13</td>
  <td>.54</td>
  <td>11.5</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-210</td>
  <td>N01H301</td>
  <td>8/29/11</td>
  <td>22:19:47</td>
  <td>Heptane</td>
  <td>762.9</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>2.92</td>
  <td>-</td>
  <td>.69</td>
  <td>12.8</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-211</td>
  <td>N02H101</td>
  <td>8/29/11</td>
  <td>23:36:18</td>
  <td>Heptane</td>
  <td>759.8</td>
  <td>.16</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>3.34</td>
  <td>3.18</td>
  <td>.34</td>
  <td>3.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-212</td>
  <td>N02H201</td>
  <td>8/29/11</td>
  <td>23:51:11</td>
  <td>Heptane</td>
  <td>759.8</td>
  <td>.16</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-214</td>
  <td>N02H203</td>
  <td>8/30/11</td>
  <td>0:58:06</td>
  <td>Heptane</td>
  <td>759.9</td>
  <td>.16</td>
  <td>.84</td>
  <td>0</td>
  <td>0</td>
  <td>2.52</td>
  <td>2.13</td>
  <td>.42</td>
  <td>4.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-215</td>
  <td>N03H101</td>
  <td>9/1/11</td>
  <td>19:44:42</td>
  <td>Heptane</td>
  <td>764</td>
  <td>.15</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>2.55</td>
  <td>2.31</td>
  <td>.37</td>
  <td>3.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-216</td>
  <td>N03H201</td>
  <td>9/1/11</td>
  <td>21:02:30</td>
  <td>Heptane</td>
  <td>766.2</td>
  <td>.15</td>
  <td>.85</td>
  <td>0</td>
  <td>0</td>
  <td>1.77</td>
  <td>.33</td>
  <td>.47</td>
  <td>6.7</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-217</td>
  <td>N04H101</td>
  <td>9/1/11</td>
  <td>22:54:16</td>
  <td>Heptane</td>
  <td>759.8</td>
  <td>.14</td>
  <td>.86</td>
  <td>0</td>
  <td>0</td>
  <td>4.16</td>
  <td>4.15</td>
  <td>.24</td>
  <td>1.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-218</td>
  <td>N04H201</td>
  <td>9/1/11</td>
  <td>23:17:17</td>
  <td>Heptane</td>
  <td>759.9</td>
  <td>.14</td>
  <td>.86</td>
  <td>0</td>
  <td>0</td>
  <td>1.83</td>
  <td>-</td>
  <td>.39</td>
  <td>3.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-219</td>
  <td>N04M101</td>
  <td>9/8/11</td>
  <td>17:00:27</td>
  <td>Methanol</td>
  <td>757.6</td>
  <td>.14</td>
  <td>.86</td>
  <td>0</td>
  <td>0</td>
  <td>3.5</td>
  <td>-</td>
  <td>.3</td>
  <td>26</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-220</td>
  <td>N04M201</td>
  <td>9/8/11</td>
  <td>17:21:15</td>
  <td>Methanol</td>
  <td>758.3</td>
  <td>.14</td>
  <td>.86</td>
  <td>0</td>
  <td>0</td>
  <td>2.67</td>
  <td>1.27</td>
  <td>.38</td>
  <td>15.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-221</td>
  <td>N05M101</td>
  <td>9/8/11</td>
  <td>19:00:48</td>
  <td>Methanol</td>
  <td>759.4</td>
  <td>.13</td>
  <td>.87</td>
  <td>0</td>
  <td>0</td>
  <td>3.46</td>
  <td>2.96</td>
  <td>.36</td>
  <td>9.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-222</td>
  <td>N05M201</td>
  <td>9/8/11</td>
  <td>20:24:20</td>
  <td>Methanol</td>
  <td>760.6</td>
  <td>.13</td>
  <td>.87</td>
  <td>0</td>
  <td>0</td>
  <td>2.75</td>
  <td>1.46</td>
  <td>.35</td>
  <td>16.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-223</td>
  <td>N06M101</td>
  <td>9/9/11</td>
  <td>13:09:53</td>
  <td>Methanol</td>
  <td>761.6</td>
  <td>.12</td>
  <td>.88</td>
  <td>0</td>
  <td>0</td>
  <td>2.6</td>
  <td>2.09</td>
  <td>.36</td>
  <td>6.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-224</td>
  <td>N06M201</td>
  <td>9/9/11</td>
  <td>13:28:43</td>
  <td>Methanol</td>
  <td>761.9</td>
  <td>.12</td>
  <td>.88</td>
  <td>0</td>
  <td>0</td>
  <td>1.94</td>
  <td>1.05</td>
  <td>.35</td>
  <td>7.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-225</td>
  <td>N06M202</td>
  <td>9/9/11</td>
  <td>14:26:07</td>
  <td>Methanol</td>
  <td>763.7</td>
  <td>.12</td>
  <td>.88</td>
  <td>0</td>
  <td>0</td>
  <td>1.84</td>
  <td>1.04</td>
  <td>.38</td>
  <td>6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-226</td>
  <td>H01M102</td>
  <td>9/9/11</td>
  <td>17:41:47</td>
  <td>Methanol</td>
  <td>759.2</td>
  <td>.2</td>
  <td>.75</td>
  <td>0</td>
  <td>.05</td>
  <td>2.91</td>
  <td>1.12</td>
  <td>.51</td>
  <td>14.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-227</td>
  <td>H01M104</td>
  <td>9/9/11</td>
  <td>18:27:14</td>
  <td>Methanol</td>
  <td>759.6</td>
  <td>.2</td>
  <td>.75</td>
  <td>0</td>
  <td>.05</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>~6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-229</td>
  <td>H01H102</td>
  <td>9/13/11</td>
  <td>11:55:40</td>
  <td>Heptane</td>
  <td>755.3</td>
  <td>.2</td>
  <td>.75</td>
  <td>0</td>
  <td>.05</td>
  <td>2.25</td>
  <td>-</td>
  <td>.57</td>
  <td>~9</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-230</td>
  <td>H01H103</td>
  <td>9/13/11</td>
  <td>12:22:18</td>
  <td>Heptane</td>
  <td>756.5</td>
  <td>.2</td>
  <td>.75</td>
  <td>0</td>
  <td>.05</td>
  <td>2.3</td>
  <td>-</td>
  <td>.58</td>
  <td>9.8</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-231</td>
  <td>H02M101</td>
  <td>9/21/11</td>
  <td>22:28:54</td>
  <td>Methanol</td>
  <td>753.4</td>
  <td>.19</td>
  <td>.71</td>
  <td>0</td>
  <td>.1</td>
  <td>2.78</td>
  <td>-</td>
  <td>.57</td>
  <td>12.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-232</td>
  <td>H03M101</td>
  <td>9/22/11</td>
  <td>0:02:52</td>
  <td>Methanol</td>
  <td>759.2</td>
  <td>.18</td>
  <td>.67</td>
  <td>0</td>
  <td>.15</td>
  <td>2.79</td>
  <td>1.3</td>
  <td>.51</td>
  <td>12.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-233</td>
  <td>H03M201</td>
  <td>9/22/11</td>
  <td>0:44:55</td>
  <td>Methanol</td>
  <td>760.3</td>
  <td>.18</td>
  <td>.67</td>
  <td>0</td>
  <td>.15</td>
  <td>2.95</td>
  <td>1.67</td>
  <td>.53</td>
  <td>11.7</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-234</td>
  <td>N01H401</td>
  <td>9/23/11</td>
  <td>23:18:09</td>
  <td>Heptane</td>
  <td>767.4</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>3.32</td>
  <td>1.37</td>
  <td>.52</td>
  <td>17.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-235</td>
  <td>N01H502</td>
  <td>9/24/11</td>
  <td>0:06:41</td>
  <td>Heptane</td>
  <td>768.1</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>2.39</td>
  <td>-</td>
  <td>.57</td>
  <td>10.6</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-236</td>
  <td>N01H601</td>
  <td>9/24/11</td>
  <td>1:06:33</td>
  <td>Heptane</td>
  <td>769.2</td>
  <td>.21</td>
  <td>.79</td>
  <td>0</td>
  <td>0</td>
  <td>3.65</td>
  <td>2.85</td>
  <td>.57</td>
  <td>9.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-237</td>
  <td>H02H101</td>
  <td>9/24/11</td>
  <td>2:44:09</td>
  <td>Heptane</td>
  <td>758.8</td>
  <td>.19</td>
  <td>.71</td>
  <td>0</td>
  <td>.1</td>
  <td>2.59</td>
  <td>-</td>
  <td>.54</td>
  <td>12</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-238</td>
  <td>H03H101</td>
  <td>9/27/11</td>
  <td>12:08:14</td>
  <td>Heptane</td>
  <td>763.7</td>
  <td>.18</td>
  <td>.67</td>
  <td>0</td>
  <td>.15</td>
  <td>3.52</td>
  <td>3.28</td>
  <td>.41</td>
  <td>4.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-239</td>
  <td>H03H201</td>
  <td>9/27/11</td>
  <td>13:00:54</td>
  <td>Heptane</td>
  <td>765.9</td>
  <td>.18</td>
  <td>.67</td>
  <td>0</td>
  <td>.15</td>
  <td>2.3</td>
  <td>-</td>
  <td>.49</td>
  <td>9.1</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-240</td>
  <td>H03H202</td>
  <td>9/27/11</td>
  <td>13:25:07</td>
  <td>Heptane</td>
  <td>766.5</td>
  <td>.18</td>
  <td>.67</td>
  <td>0</td>
  <td>.15</td>
  <td>2.27</td>
  <td>-</td>
  <td>.51</td>
  <td>8.6</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-241</td>
  <td>H04H101</td>
  <td>9/27/11</td>
  <td>15:00:33</td>
  <td>Heptane</td>
  <td>759.3</td>
  <td>.17</td>
  <td>.63</td>
  <td>0</td>
  <td>.2</td>
  <td>2.85</td>
  <td>2.6</td>
  <td>.46</td>
  <td>3.2</td>
  <td>Extinction</td>
 </tr>
</table>


NASA/TP-2015-216046


26




<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>Burn time, s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>FLEX-242</td>
  <td>H04H201</td>
  <td>9/27/11</td>
  <td>15:12:24</td>
  <td>Heptane</td>
  <td>759.3</td>
  <td>.17</td>
  <td>.63</td>
  <td>0</td>
  <td>.2</td>
  <td>2.12</td>
  <td>1.39</td>
  <td>.59</td>
  <td>4.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-243</td>
  <td>H04H302</td>
  <td>9/27/11</td>
  <td>16:18:19</td>
  <td>Heptane</td>
  <td>759.6</td>
  <td>.17</td>
  <td>.63</td>
  <td>0</td>
  <td>.2</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>1.7</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-244</td>
  <td>H04H303</td>
  <td>9/27/11</td>
  <td>16:40:04</td>
  <td>Heptane</td>
  <td>759.8</td>
  <td>.17</td>
  <td>.63</td>
  <td>0</td>
  <td>.2</td>
  <td>1.61</td>
  <td>-</td>
  <td>.91</td>
  <td>2.7</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-245</td>
  <td>H04M101</td>
  <td>10/1/11</td>
  <td>0:34:58</td>
  <td>Methanol</td>
  <td>754.2</td>
  <td>.17</td>
  <td>.63</td>
  <td>0</td>
  <td>.2</td>
  <td>2.99</td>
  <td>-</td>
  <td>.49</td>
  <td>9.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-246</td>
  <td>H04M202</td>
  <td>10/1/11</td>
  <td>1:21:41</td>
  <td>Methanol</td>
  <td>757</td>
  <td>.17</td>
  <td>.63</td>
  <td>0</td>
  <td>.2</td>
  <td>2.9</td>
  <td>1.42</td>
  <td>.51</td>
  <td>13.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-247</td>
  <td>H05M102</td>
  <td>10/1/11</td>
  <td>2:58:40</td>
  <td>Methanol</td>
  <td>759.9</td>
  <td>.16</td>
  <td>.59</td>
  <td>0</td>
  <td>.25</td>
  <td>3.4</td>
  <td>2.79</td>
  <td>.51</td>
  <td>7.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-248</td>
  <td>H05M202</td>
  <td>10/1/11</td>
  <td>4:26:52</td>
  <td>Methanol</td>
  <td>761</td>
  <td>.16</td>
  <td>.59</td>
  <td>0</td>
  <td>.25</td>
  <td>-</td>
  <td>-</td>
  <td>-</td>
  <td>5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-249</td>
  <td>H05H103</td>
  <td>10/5/11</td>
  <td>14:58:32</td>
  <td>Heptane</td>
  <td>757.9</td>
  <td>.16</td>
  <td>.59</td>
  <td>0</td>
  <td>.25</td>
  <td>1.49</td>
  <td>.69</td>
  <td>.6</td>
  <td>2.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-250</td>
  <td>H06M102</td>
  <td>10/7/11</td>
  <td>12:12:14</td>
  <td>Methanol</td>
  <td>755.6</td>
  <td>.15</td>
  <td>.55</td>
  <td>0</td>
  <td>.3</td>
  <td>3.67</td>
  <td>3.47</td>
  <td>.43</td>
  <td>3.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-251</td>
  <td>H06M201</td>
  <td>10/7/11</td>
  <td>13:00:56</td>
  <td>Methanol</td>
  <td>756.7</td>
  <td>.15</td>
  <td>.55</td>
  <td>0</td>
  <td>.3</td>
  <td>2.52</td>
  <td>2.06</td>
  <td>.56</td>
  <td>4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-252</td>
  <td>H07M101</td>
  <td>10/7/11</td>
  <td>14:25:42</td>
  <td>Methanol</td>
  <td>759.2</td>
  <td>.14</td>
  <td>.51</td>
  <td>0</td>
  <td>.35</td>
  <td>2.44</td>
  <td>2.26</td>
  <td>.56</td>
  <td>1.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-253</td>
  <td>H07M202</td>
  <td>10/7/11</td>
  <td>15:06:17</td>
  <td>Methanol</td>
  <td>759.8</td>
  <td>.14</td>
  <td>.51</td>
  <td>0</td>
  <td>.35</td>
  <td>1.88</td>
  <td>1.73</td>
  <td>.58</td>
  <td>1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-254</td>
  <td>H08M101</td>
  <td>10/11/11</td>
  <td>12:11:56</td>
  <td>Methanol</td>
  <td>763.5</td>
  <td>.13</td>
  <td>.47</td>
  <td>0</td>
  <td>.4</td>
  <td>3.56</td>
  <td>3.54</td>
  <td>.51</td>
  <td>.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-255</td>
  <td>H10H101</td>
  <td>10/12/11</td>
  <td>20:16:43</td>
  <td>Heptane</td>
  <td>534</td>
  <td>.24</td>
  <td>.56</td>
  <td>0</td>
  <td>.2</td>
  <td>3.78</td>
  <td>2.52</td>
  <td>.72</td>
  <td>12.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-256</td>
  <td>H11H101</td>
  <td>10/12/11</td>
  <td>21:58:55</td>
  <td>Heptane</td>
  <td>532.2</td>
  <td>.23</td>
  <td>.52</td>
  <td>0</td>
  <td>.25</td>
  <td>2.8</td>
  <td>.12</td>
  <td>.71</td>
  <td>11.4</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-257</td>
  <td>H10M101</td>
  <td>11/18/11</td>
  <td>14:48:10</td>
  <td>Methanol</td>
  <td>534.3</td>
  <td>.24</td>
  <td>.56</td>
  <td>0</td>
  <td>.2</td>
  <td>2.82</td>
  <td>1.03</td>
  <td>.62</td>
  <td>11.2</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-258</td>
  <td>H10M102</td>
  <td>11/18/11</td>
  <td>15:19:28</td>
  <td>Methanol</td>
  <td>534.6</td>
  <td>.24</td>
  <td>.56</td>
  <td>0</td>
  <td>.2</td>
  <td>2.79</td>
  <td>1.53</td>
  <td>.7</td>
  <td>8.1</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-259</td>
  <td>H11M101</td>
  <td>11/18/11</td>
  <td>16:59:20</td>
  <td>Methanol</td>
  <td>531.7</td>
  <td>.23</td>
  <td>.52</td>
  <td>0</td>
  <td>.25</td>
  <td>2.45</td>
  <td>.86</td>
  <td>.6</td>
  <td>8.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-260</td>
  <td>H11M102</td>
  <td>11/18/11</td>
  <td>17:51:23</td>
  <td>Methanol</td>
  <td>531.8</td>
  <td>.23</td>
  <td>.52</td>
  <td>0</td>
  <td>.25</td>
  <td>2.61</td>
  <td>-</td>
  <td>.73</td>
  <td>6.3</td>
  <td>Disruption</td>
 </tr>
 <tr>
  <td>FLEX-261</td>
  <td>H12M101</td>
  <td>11/18/11</td>
  <td>18:53:50</td>
  <td>Methanol</td>
  <td>531.9</td>
  <td>.21</td>
  <td>.49</td>
  <td>0</td>
  <td>.3</td>
  <td>3.22</td>
  <td>-</td>
  <td>.56</td>
  <td>10.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-262</td>
  <td>H12M102</td>
  <td>11/18/11</td>
  <td>21:29:35</td>
  <td>Methanol</td>
  <td>531.2</td>
  <td>.21</td>
  <td>.49</td>
  <td>0</td>
  <td>.3</td>
  <td>3.25</td>
  <td>1.78</td>
  <td>.65</td>
  <td>12.1</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-263</td>
  <td>H12M201</td>
  <td>11/18/11</td>
  <td>21:53:16</td>
  <td>Methanol</td>
  <td>531.2</td>
  <td>.21</td>
  <td>.49</td>
  <td>0</td>
  <td>.3</td>
  <td>2.67</td>
  <td>1.42</td>
  <td>.7</td>
  <td>7.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-264</td>
  <td>H12H101</td>
  <td>11/22/11</td>
  <td>13:04:17</td>
  <td>Heptane</td>
  <td>529.6</td>
  <td>.21</td>
  <td>.49</td>
  <td>0</td>
  <td>.3</td>
  <td>3.23</td>
  <td>2.33</td>
  <td>.67</td>
  <td>7.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-265</td>
  <td>H12H201</td>
  <td>11/22/11</td>
  <td>15:49:36</td>
  <td>Heptane</td>
  <td>529</td>
  <td>.21</td>
  <td>.49</td>
  <td>0</td>
  <td>.3</td>
  <td>2.86</td>
  <td>.71</td>
  <td>.7</td>
  <td>11</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-266</td>
  <td>H13H101</td>
  <td>11/22/11</td>
  <td>20:40:42</td>
  <td>Heptane</td>
  <td>532.5</td>
  <td>.2</td>
  <td>.45</td>
  <td>0</td>
  <td>.35</td>
  <td>3.69</td>
  <td>3.32</td>
  <td>.61</td>
  <td>4.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-267</td>
  <td>H13H201</td>
  <td>11/22/11</td>
  <td>20:58:21</td>
  <td>Heptane</td>
  <td>532</td>
  <td>.2</td>
  <td>.45</td>
  <td>0</td>
  <td>.35</td>
  <td>3.08</td>
  <td>1.69</td>
  <td>.67</td>
  <td>5.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-268</td>
  <td>H13M102</td>
  <td>11/28/11</td>
  <td>13:13:31</td>
  <td>Methanol</td>
  <td>527.6</td>
  <td>.2</td>
  <td>.45</td>
  <td>0</td>
  <td>.35</td>
  <td>3.87</td>
  <td>2.24</td>
  <td>.6</td>
  <td>17.4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-269</td>
  <td>H13M201</td>
  <td>11/28/11</td>
  <td>13:24:55</td>
  <td>Methanol</td>
  <td>527.9</td>
  <td>.2</td>
  <td>.45</td>
  <td>0</td>
  <td>.35</td>
  <td>2.95</td>
  <td>1.5</td>
  <td>.63</td>
  <td>10.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-270</td>
  <td>H14M101</td>
  <td>11/28/11</td>
  <td>15:07:28</td>
  <td>Methanol</td>
  <td>532.4</td>
  <td>.18</td>
  <td>.42</td>
  <td>0</td>
  <td>.4</td>
  <td>3.5</td>
  <td>2.67</td>
  <td>.59</td>
  <td>7.8</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-271</td>
  <td>H14M201</td>
  <td>11/28/11</td>
  <td>15:35:38</td>
  <td>Methanol</td>
  <td>532.9</td>
  <td>.18</td>
  <td>.42</td>
  <td>0</td>
  <td>.4</td>
  <td>2.7</td>
  <td>1.92</td>
  <td>.63</td>
  <td>5.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-272</td>
  <td>H14M202</td>
  <td>11/28/11</td>
  <td>15:54:09</td>
  <td>Methanol</td>
  <td>533.2</td>
  <td>.18</td>
  <td>.42</td>
  <td>0</td>
  <td>.4</td>
  <td>1.84</td>
  <td>1.3</td>
  <td>.62</td>
  <td>2.3</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-273</td>
  <td>H14H101</td>
  <td>11/30/11</td>
  <td>8:39:18</td>
  <td>Heptane</td>
  <td>528</td>
  <td>.18</td>
  <td>.42</td>
  <td>0</td>
  <td>.4</td>
  <td>2.27</td>
  <td>1.64</td>
  <td>.71</td>
  <td>3.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-274</td>
  <td>H14H201</td>
  <td>11/30/11</td>
  <td>9:49:07</td>
  <td>Heptane</td>
  <td>530.3</td>
  <td>.18</td>
  <td>.42</td>
  <td>0</td>
  <td>.4</td>
  <td>1.86</td>
  <td>.84</td>
  <td>.77</td>
  <td>3.5</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-275</td>
  <td>H15H101</td>
  <td>11/30/11</td>
  <td>11:30:51</td>
  <td>Heptane</td>
  <td>532.2</td>
  <td>.17</td>
  <td>.38</td>
  <td>0</td>
  <td>.45</td>
  <td>2.22</td>
  <td>1.86</td>
  <td>.76</td>
  <td>1.9</td>
  <td>Extinction</td>
 </tr>
</table>


NASA/TP-2015-216046


27




<table>
 <tr>
  <th>Test FLEX</th>
  <th>Identifier FLEX</th>
  <th>Date Test</th>
  <th>Greenwich mean time Test</th>
  <th>Fuel</th>
  <th>pressure, Ambient mmHg</th>
  <th>O 2 Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>N2 CO2 He Initial mole composition, fraction ambient</th>
  <th>mm diameter, Droplet initial</th>
  <th>diameter, mm extinction Visible flame</th>
  <th>Burning mm2/s rate,</th>
  <th>time, Burn s</th>
  <th>Test end</th>
 </tr>
 <tr>
  <td>FLEX-276</td>
  <td>H15H201</td>
  <td>11/30/11</td>
  <td>12:09:00</td>
  <td>Heptane</td>
  <td>532.5</td>
  <td>.17</td>
  <td>.38</td>
  <td>0</td>
  <td>.45</td>
  <td>1.61</td>
  <td>.91</td>
  <td>1.06</td>
  <td>1.4</td>
  <td>Completion</td>
 </tr>
 <tr>
  <td>FLEX-277</td>
  <td>H15M102</td>
  <td>12/5/11</td>
  <td>22:54:10</td>
  <td>Methanol</td>
  <td>530.4</td>
  <td>.17</td>
  <td>.38</td>
  <td>0</td>
  <td>.45</td>
  <td>2.79</td>
  <td>2.3</td>
  <td>.63</td>
  <td>4</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-278</td>
  <td>H15M201</td>
  <td>12/5/11</td>
  <td>23:39:04</td>
  <td>Methanol</td>
  <td>531.5</td>
  <td>.17</td>
  <td>.38</td>
  <td>0</td>
  <td>.45</td>
  <td>2.68</td>
  <td>2.31</td>
  <td>.66</td>
  <td>2.9</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-279</td>
  <td>H19H101</td>
  <td>12/8/11</td>
  <td>22:29:44</td>
  <td>Heptane</td>
  <td>764.7</td>
  <td>.21</td>
  <td>.64</td>
  <td>0</td>
  <td>.15</td>
  <td>3.54</td>
  <td>2.91</td>
  <td>.55</td>
  <td>7.6</td>
  <td>Extinction</td>
 </tr>
 <tr>
  <td>FLEX-280</td>
  <td>H19H201</td>
  <td>12/8/11</td>
  <td>23:41:45</td>
  <td>Heptane</td>
  <td>766.2</td>
  <td>.21</td>
  <td>.64</td>
  <td>0</td>
  <td>.15</td>
  <td>2.82</td>
  <td>.73</td>
  <td>.65</td>
  <td>11.7</td>
  <td>Extinction</td>
 </tr>
</table>


NASA/TP-2015-216046 28




##### Appendix B.-Droplet and Flame Sizes


Figures 5 to 280 show the results of each experiment. These camera) as functions of time. Time zero in the plots corresponds
figures show the droplet diameter squared and the flame to when the igniter was energized. This time came from data
diameter (for both the Low Light Level Ultra-Violet (LLUV) files downlinked from the CIR after a test. The data for each
and Multi-User Droplet Combustion Apparatus (MDCA) color test are also available in a text file associated with this report.


Figure 5.-Test FLEX-001. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. This was the first FLEX test. The droplet remained in the fields of view (FOVs) of
all the cameras for the entire test. Because the Low Light Level Ultra-Violet (LLUV) camera settings were
not optimal, the LLUV data are not reliable. The droplet probably disrupted at the end of the test
coincident with flame extinction. The igniters were too bright and overexposed the High-Bit-Depth
Multispectral (HiBMs) images during ignition, so the droplet diameter could not be measured accurately.


NASA/TP-2015-216046 29




Figure 6.-Test FLEX-002. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras for the entire
test and extinguished diffusively. Because this was a calibration run, the Low Light Level Ultra-Violet
(LLUV) setting was not optimal. Consequently, the LLUV flame data are not reliable, especially near the
end of the test. The droplet did not disrupt, but clearly something happened to the flame near the end of
the test.


NASA/TP-2015-216046 30




Figure 7.-Test FLEX-003. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras for the entire
test. Because this was a calibration run, the Low Light Level Ultra-Violet (LLUV) setting was not optimal
as indicated by the flame being very difficult to see and measure (especially near the end of the test).


NASA/TP-2015-216046 31




Figure 8.-Test FLEX-004. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) after deployment and ignition, leaving the HiBMs FOV one-third of the way through the burn.
There was some evidence of flame disruption before the flame extinguished, but it was difficult to judge
from the color camera images. This was a calibration test point. The igniter overwhelmed the HiBMs and
made measuring the droplet impossible until the igniters moved out of the FOV. The Low Light Level
Ultra-Violet (LLUV) setting was not optimal, and the flame nearly disappeared from the LLUV halfway
through the burn, coincident with when the color camera showed a noticeable change in the flame
behavior.


NASA/TP-2015-216046 32




Figure 9.-Test FLEX-005. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras. Because this
was a calibration run, the Low Light Level Ultra-Violet (LLUV) settings were not optimal. Consequently,
halfway through the burn the flame became undetectable in the LLUV. There was no evidence of
disruptive burning near extinction. The flame, however, seemed to shrink quickly after ignition-maybe
because of a small bubble burst.


NASA/TP-2015-216046 33




Figure 10.-Test FLEX-006. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet was misshapen on the needles before it stretched and deployed.
Ignition imparted a significant drift velocity on the droplet to the east. This could be due to a small air
bubble that distorted the droplet and then popped when the igniters turned on. The droplet drifted out of
the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) and then drifted back in the FOV. The flame
extinguished without disruption. This was a calibration test. Because the Low Light Level Ultra-Violet
(LLUV) settings were not optimized for these tests, late in the flame lifetime the flame was not discernable
in the LLUV.


NASA/TP-2015-216046 34




Figure 11.-Test FLEX-007. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet deployed and ignited with little residual velocity and remained within
the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire test. The droplet burned with a
very luminous flame that obscured the droplet in the HiBMs for a large portion of the test. The droplet
burned to a small droplet size and then disrupted. The last part of the droplet history was obscured by
the luminous flame.


NASA/TP-2015-216046 35




Figure 12.-Test FLEX-008. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet drifted southeast out of the High-Bit-Depth Multispectral (HiBMs) field
of view (FOV) a few seconds after the igniter was withdrawn. Significant sooting was apparent in the
HiBMs. The droplet also drifted out of the color camera FOV. It remained in the Low Light Level Ultra-
Violet (LLUV) FOV for the entire burn. There is a lot of noise in the droplet diameter data because of the
soot, but the LLUV showed that the droplet disrupted at the end of the burn.


NASA/TP-2015-216046 36




Figure 13.-Test FLEX-009. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The deployment was very poor, and the droplet drifted out of the
fields of view (FOVs) of all the cameras very shortly after deployment and ignition. No Image
Processing and Storage Unit (IPSU) data were downlinked for this test. The color camera
analysis was from the downlinked video.


NASA/TP-2015-216046 37




Figure 14.-Test FLEX-010. Free-floating methanol droplet burning in a 0.21/0.09/0.70 O2/N2/CO2,


3.0-atm ambient environment. The droplet drifted southeast after deployment, hit the igniter, changed


direction, and quickly moved west out of the fields of view (FOVs) of the High-Bit-Depth Multispectral
(HiBMs), Low Light Level Ultra-Violet (LLUV), and color camera. The HiBMs produced a saturated image
that influenced the droplet size measurement. In addition, the HiBMs backlight was too strong, and the
droplet size measurement was a function of which "quad-slice" the droplet was in the HiBMs image.
Because the droplet was in the HiBMs FOV for only a short time, no burning rate constant or extinction
droplet diameter is reported.


NASA/TP-2015-216046 38




Figure 15.-Test FLEX-011. Free-floating methanol droplet burning in a 0.21/0.09/0.70 O2/N2/CO2, 3.0-atm
ambient environment. The droplet drifted southeast in the High-Bit-Depth Multispectral (HiBMs) field of
view (FOV) after deployment, hit the lower igniter, and then drifted very quickly to the east and out of the
HiBMs FOV. The HiBMs and illumination settings were not correct, so the igniters obscured the droplet.
Also the background was near saturation, so the droplet size is a function of the "quadrant slice" of the
HiBMs image that it was in. The droplet drifted out of the Low Light Level Ultra-Violet (LLUV) FOV, but it
remained in the color camera FOV most of the time.


NASA/TP-2015-216046 39




Figure 16.-Test FLEX-012. Free-floating heptane droplet burning in a 0.21/0.09/0.70 O2/N2/CO2, 3.0-atm
ambient environment. The deployment was very poor. The droplet drifted toward the upper igniter in the
High-Bit-Depth Multispectral (HiBMs) field of view (FOV) after deployment, hooked around the igniter, and
got hit by the igniter when the igniter was withdrawn. That propelled the droplet rapidly out of the HiBMs
FOV. The droplet left the FOVs of all the cameras before burning to a presumed extinction. The flame was
very luminous and yellow, with significant sooting present in the HiBMs.


NASA/TP-2015-216046 40




Figure 17.-Test FLEX-013. Free-floating methanol droplet burning in a 0.21/0.09/0.70 O2/N2/CO2,


3.0-atm ambient environment. The droplet drifted west in the High-Bit-Depth Multispectral (HiBMs)


field of view (FOV), hit the igniter, drifted southeast after the igniter was withdrawn, and left the FOV.
It reappeared for a short time before disappearing again. The glow from the igniter influenced the
droplet size measurement early, the HiBMs and illumination package settings were not good enough
for reliable droplet size measurements. Because the droplet was not in the HiBMs FOV for enough
of the test, no extinction droplet diameter is reported. The color camera Image Processing and
Storage Unit (IPSU) did not record any images after deployment.


NASA/TP-2015-216046 41




Figure 18.-Test FLEX-014. Free-floating methanol droplet burning in a 0.21/0.09/0.70 O2/N2/CO2,


3.0-atm ambient environment. The droplet drifted significantly to the northwest in the High-Bit-


Depth Multispectral (HiBMs) after deployment and ignition (ignition did not change the motion
visually). Then the droplet quickly drifted out of the field of view (FOV) of the HiBMs. The color
camera Image Processing and Storage Unit (IPSU) did not record any images for this test. The
droplet also drifted north out of the Low Light Level Ultra-Violet (LLUV) FOV before the flame
extinguished. Because the droplet was within the HiBMs FOV for only a limited time, no burning
rate or extinction droplet diameter is reported.


NASA/TP-2015-216046 42




Figure 19.-Test FLEX-015. Free-floating methanol droplet burning in a 0.21/0.09/0.70 O2/N2/CO2,


3.0-atm ambient environment. After ignition, the droplet quickly drifted north and out of the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV). Because the droplet was in the HiBMs FOV for only
a short time, no burning rate constant is reported. The droplet did not drift out of the FOV of the Low
Light Level Ultra-Violet (LLUV), but the Image Processing and Storage Unit (IPSU) data for the
LLUV ended before the flame extinguished. The droplet drifted northeast and out of the color
camera FOV before the flame extinguished. In the color camera view, the flame was visibly brighter
in the direction of the translation, an indication that the convective motion was impacting the flame
behavior significantly.


NASA/TP-2015-216046 43




Figure 20.-Test FLEX-016. Free-floating methanol droplet burning in a 0.21/0.09/0.70 O2/N2/CO2,


3.0-atm ambient environment. The droplet drifted and hit the igniter before the igniter was


withdrawn. Then the droplet drifted slowly west in the High-Bit-Depth Multispectral (HiBMs) field of
view (FOV), but it remained in the FOVs of all the cameras for the entire test. There was significant
translation in the HiBMs FOV during the test.


NASA/TP-2015-216046 44




Figure 21.-Test FLEX-017. Free-floating methanol droplet burning in a 0.21/0.09/0.70 O2/N2/CO2, 3.0-atm
ambient environment. The droplet drifted east in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) after deployment, hit the igniter, and then drifted north. The droplet immediately began to grow,
disrupted, and finally shattered, causing the flame to extinguish. This behavior was probably due to a gas
bubble being trapped in the droplet after deployment.


NASA/TP-2015-216046 45




Figure 22.-Test FLEX-018. Free-floating heptane droplet burning in a 0.21/0.09/0.70 O2/N2/CO2, 2.0-atm
ambient environment. There was a luminous yellow flame immediately after ignition, with the High-Bit-
Depth Multispectral (HiBMs) view showing significant soot formation. Then the luminous flame
disappeared, and a dim blue flame surrounded the droplet. The flame oscillated and then appeared to
extinguish in both the Low Light Level Ultra-Violet (LLUV) and color camera fields of view (FOVs).
However, the droplet continued to vaporize vigorously, and the radiometer did not settle to its baseline
value. There was "hazing" around the droplet in the HiBMs FOV during combustion, almost like there
was significant internal liquid motion. The droplet disrupted after it drifted out of the HiBMs FOV. There
probably was cool flame burning after the visible flame extinguished.


NASA/TP-2015-216046 46




Figure 23.-Test FLEX-019. Free-floating heptane droplet burning in a 0.34/0.66 O2/N2, 0.70-atm ambient
environment. The droplet was almost motionless after deployment, but after the igniters began to heat, a
large impulse moved the droplet southwest and quickly out of High-Bit-Depth Multispectral (HiBMs) field
of view (FOV). The droplet was nearly out of the FOV when the igniters began to move away from the
droplet. There was significant sooting with large aggregates, so the data from this test are not reliable.


NASA/TP-2015-216046 47




Figure 24.-Test FLEX-020. Free-floating methanol droplet burning in a 0.34/0.66 O2/N2, 0.70-atm
ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) after deployment and ignition. It was in the HiBMs FOV for only a short time, and it drifted quickly
out of the color camera FOV. It remained in the Low Light Level Ultra-Violet (LLUV) FOV for the entire
burn and seemed to burn to either a very small extinction droplet size or completion.


NASA/TP-2015-216046 48




Figure 25.-Test FLEX-021. Free-floating methanol droplet burning in a 0.34/0.66 O2/N2, 0.70-atm
ambient environment. This was the first successful test after switching from the high-CO2, high-
pressure ambient environments, where we had significant deployment problems. The droplet had a
high burning rate and remained in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the
entire test. Before the flame extinguished, the droplet distorted. Eventually, the droplet shattered
coincident with flame extinction.


NASA/TP-2015-216046 49




Figure 26.-Test FLEX-022. Free-floating methanol droplet burning in a 0.34/0.66 O2/N2, 0.7-atm
ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) for the entire test and drifted slowly south-southeast during the test. The droplet began to
change shape, and it became almost oblong with a pointed end (shown in the video) before
disrupting. The disruption was coincident with flame extinction.


NASA/TP-2015-216046 50




Figure 27.-Test FLEX-023. Free-floating heptane droplet burning in a 0.37/0.66 O2/N2, 0.70-atm
ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs) field of
view (FOV) after deployment and ignition. It drifted partially out of the FOV, but then it drifted back
in. Throughout the test, there was significant sooting with large agglomerates.


NASA/TP-2015-216046 51




Figure 28.-Test FLEX-024. Free-floating heptane droplet burning in a 0.34/0.66 O2/N2, 0.70-atm
ambient environment. The High-Bit-Depth Multispectral (HiBMs) Image Processing and Storage
Unit (IPSU) did not record any images for this test. There appeared to be a needle fire. The color
camera and Low Light Level Ultra-Violet (LLUV) IPSUs stopped recording before the test was
complete. In addition, the LLUV images were recorded at 8-bit depth (instead of 12-bit depth),
which resulted in more uncertainty in the LLUV flame size measurements.


NASA/TP-2015-216046 52




Figure 29.-Test FLEX-025. Free-floating methanol droplet burning in a 0.30/0.70 O2/N2, 0.7-atm
ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs) field of
view (FOV) after deployment and ignition, leaving the FOV halfway through the burn before burning to
near completion.


NASA/TP-2015-216046 53




Figure 30.-Test FLEX-026. Free-floating methanol droplet burning in a 0.30/0.80 O2/N2, 0.70-atm
ambient environment. The droplet drifted northwest out of the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) about halfway through the burn. The droplet appeared to burn to completion or a
very small size before it disrupted, causing the flame to extinguish.


NASA/TP-2015-216046 54




Figure 31.-Test FLEX-027. Free-floating heptane droplet burning in a 0.30/0.70 O2/N2, 0.7-atm
ambient environment. The droplet drifted west in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) after deployment and ignition, and it drifted out of the FOV two-thirds of the way through the
test. Initially luminous yellow, the flame dimmed to blue relatively quickly about one-third of the way
through the burn. There was significant sooting with large soot agglomerates present throughout the
burn. The droplet disrupted coincident with flame extinction.


NASA/TP-2015-216046 55




Figure 32.-Test FLEX-028. Free-floating heptane droplet burning in a 0.30/0.70 O2/N2, 0.7-atm ambient
environment. The droplet drifted north in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV)
after deployment and ignition and out of the FOV approximately two-thirds of the way through the burn.
A bright, luminous flame persisted throughout the droplet lifetime. There was significant sooting with
large soot agglomerates present throughout the burn. The droplet disrupted coincident with flame
extinction.


NASA/TP-2015-216046 56




Figure 33.-Test FLEX-029. Free-floating methanol droplet burning in a 0.360/0.80 O2/N2, 1.0-atm
ambient environment. The droplet drifted south out of the High-Bit-Depth Multispectral (HiBMs) field
of view (FOV) about one-third of the way through the test. The droplet also drifted out of the color
camera FOV before the flame extinguished. The droplet remained in the Low Light Level Ultra-Violet
(LLUV) FOV for the entire test and the droplet did not appear to disrupt when the flame extinguished.
From the extrapolated droplet history and the duration of the burn, the droplet burned to completion or
to a very small droplet size.


NASA/TP-2015-216046 57




Figure 34.-Test FLEX-030. Free-floating methanol droplet burning in a 0.30/0.70 O2/N2, 1.0-atm
ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras for the
entire test. The droplet drifted south, east, and then north in the High-Bit-Depth Multispectral (HiBMs)
FOV. Coincident with flame extinction, the droplet became almost football shaped. The oblong-
shaped droplet with a pointed end remained stationary for several seconds until the recording ended.
The actual extinction diameter is reported, but it may be influenced by the shape change.


NASA/TP-2015-216046 58




Figure 35.-Test FLEX-031. Free-floating heptane droplet burning in a 0.30/0.70 O2/N2, 1.0-atm ambient
environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV)
and left the FOV shortly after the igniter was withdrawn. There was significant sooting, and a large soot
shell surrounded the droplet. The droplet drifted out of the color camera FOV, but it remained in the Low
Light Level Ultra-Violet (LLUV) FOV. The droplet burned to disruption at a small size.


NASA/TP-2015-216046 59




Figure 36.-Test FLEX-032. Free-floating heptane droplet burning in a 0.30/0.70 O2/N2, 1.0-atm
ambient environment. There was significant sooting with large agglomerates throughout the test. A
very luminous flame persisted throughout the droplet lifetime until disruptive extinction. The droplet
drifted northwest out of the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) one-third of the
way through the test. It remained in the Low Light Level Ultra-Violet (LLUV) and color camera FOVs
for the entire test. The significant sooting made accurate measurement of the droplet size difficult.


NASA/TP-2015-216046 60




Figure 37.-Test FLEX-033. Free-floating methanol droplet burning in a 0.21/0.79 O2/N2, 1.0-atm
ambient environment. The droplet drifted slightly north and then east in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV). It eventually left the HiBMs FOV, but that was well after the flame
extinguished. The color camera Image Processing and Storage Unit (IPSU) did not record any images
after deployment.


NASA/TP-2015-216046 61




Figure 38.-Test FLEX-034. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2,


1.0-atm) ambient environment. The droplet was almost motionless after deployment and ignition. It


slowly drifted north in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV), then began to move
north much quicker and out of the HiBMs FOV about halfway through the test. The color camera Image
Processing and Storage Unit (IPSU) did not record any images for this test. It is not clear from the Low
Light Level Ultra-Violet (LLUV) whether the droplet disrupted coincident with flame extinction. Because
the droplet was out of the HiBMs FOV for a long time near visible flame extinction, no extinction droplet
diameter is reported.


NASA/TP-2015-216046 62




Figure 39.-Test FLEX-035. Free-floating heptane droplet in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) for the entire test including a long time after the visible flame extinguished. The flame oscillated
before the visible flame extinguished, and this was apparent in both the Low Light Level Ultra-Violet
(LLUV) and color camera. After the flame extinguished, the droplet vaporized very vigorously with
droplet-diameter-squared versus time behavior that was nearly perfectly linear. The vaporization rate
was only slightly lower than the burning rate constant before the flame extinguished. The droplet
vaporization rate then plateaued coincident with the formation of a very large vapor cloud. This behavior
is indicative of cool flame burning and extinction.


NASA/TP-2015-216046 63




Figure 40.-Test FLEX-036. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2),
0.70-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) for the entire burn and for several seconds after the flame extinguished. The
droplet did not distort or disrupt.


NASA/TP-2015-216046 64




Figure 41.-Test FLEX-037. Fiber-supported methanol droplet translating approximately 3 mm/s and
burning in a 0.34/0.66 O2/N2, 0.7-atm ambient environment. The droplet remained within the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV) for the entire test. After ignition and the start of
translation, there was significant transverse motion. There was a lot of scatter in the droplet history
because of the motion of the droplet on the fiber. The color camera showed a bright flame with a lot
of sparklers throughout the burn. The transverse droplet motion became more severe toward the end
of the test, with the droplet deforming. The flame extinguished when a complete disruption tore the
droplet off the fiber.


NASA/TP-2015-216046 65




Figure 42.-Test FLEX-038. Fiber-supported methanol droplet translating and burning in a 0.34/0.66
O2/N2, 0.7-atm ambient environment. The burn was very smooth, with little motion of the droplet
relative to the fiber for most of the test. About 80 percent of the way through the burn, the droplet
began to vibrate transversely on the fiber. The vibrations grew in magnitude until the droplet disrupted
and disintegrated, extinguishing the flame and leaving no fuel droplet on the fiber. The Low Light Level
Ultra-Violet (LLUV) Image Processing and Storage Unit (IPSU) stopped recording for about one-half of
the test (in the middle).


NASA/TP-2015-216046 66




Figure 43.-Test FLEX-039. Fiber-supported heptane droplet translating 3 mm/s and burning in a
0.34/0.66 O2/N2, 0.70-atm ambient environment. There were significant transverse and axial
oscillations on the fiber during the entire burn, but the droplet remained within the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) for the entire test. There also was significant sooting with
large aggregates throughout the test. The sooting was so severe that the threshold intensity for droplet
discrimination had to be reduced to get reasonable droplet size measurements. The flame was bright
yellow and very luminous throughout the entire test. A disruption dislocated the droplet from fiber
coincident with flame extinction.


NASA/TP-2015-216046 67




Figure 44.-Test FLEX-040. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.30/0.70 O2/N2, 0.7-atm ambient environment. The droplet had some transverse oscillations after
ignition, but they diminished relatively quickly. During and after translation, the droplet oscillated
axially. It moved east into and partially out of the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV). Then the droplet stopped moving both transversely and axially and burned smoothly-
eventually shrinking until it was fully in the HiBMs FOV. Near the end of the test, the droplet again
began to oscillate on the fiber and disrupted, dislodging from the fiber and causing the flame to
extinguish.


NASA/TP-2015-216046 68




Figure 45.-Test FLEX-041. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.30/0.70 O2/N2, 0.7-atm ambient environment. The droplet had significant axial oscillations during and
after the start and stop of fiber translation. The droplet drifted in and partially out of the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV). At the end of the test, the droplet swelled, disrupted, and
became dislodged from the fiber coincident with flame extinction. The dislodged droplet did burn as it
drifted away. The color camera Image Processing and Storage Unit (IPSU) did not record any images
after deployment.


NASA/TP-2015-216046 69




Figure 46.-Test FLEX-042. Fiber-supported heptane droplet burning in a 0.30/0.70 O2/N2, 0.70-atm
ambient environment. The droplet was sooted relatively heavily immediately after ignition. Shortly after
ignition, the droplet began to distort severely, periodically expelling small droplets of fuel that continued to
burn. A large disruption completely dislodged the droplet from the fiber. Afterward, the droplet drifted north
in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV), then south (after another disruption). It
then burned relatively cleanly to disruption at a small size. The burning rate constant was that during the
relatively clean period after the droplet was dislodged from the fiber. The color camera Image Processing
and Storage Unit (IPSU) did not record any images after deployment.


NASA/TP-2015-216046 70




Figure 47.-Test FLEX-043. Fiber-supported heptane droplet translating 3 mm/s and burning in a
0.30/0.70 O2/N2, 0.7-atm ambient environment. There was significant sooting, but the droplet
remained in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire test until it
disrupted and dislodged from the fiber. There was significant oscillatory axial motion on the fiber
during the entire test.


NASA/TP-2015-216046 71




Figure 48.-Test FLEX-044. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.30/0.70 O2/N2, 1.0-atm ambient environment. Transverse motion that began after deployment
persisted throughout the test. In addition, there was significant oscillatory axial motion during the
translation that persisted after the fiber stopped translating. The droplet drifted axially out of the High-
Bit-Depth Multispectral (HiBMs) field of view (FOV) about one-third of the way through the burn.
Significant "sparkling" was evident in the color camera but was not visible in the HiBMs or Low Light
Level Ultra-Violet (LLUV). The droplet disrupted and dislodged from the fiber coincident with flame
extinction.


NASA/TP-2015-216046 72




Figure 49.-Test FLEX-045. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.30/0.70 O2/N2, 1.0-atm ambient environment. The droplet remained in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) for the entire test. There was some axial and transverse
droplet motion from deployment until the end of the test, and there was some droplet swelling or
shape change before disruption. The color camera Image Processing and Storage Unit (IPSU) did not
record any images after deployment, so the extinction droplet diameter is that when the droplet
disrupted and became dislodged from the fiber coincident with flame extinction.


NASA/TP-2015-216046 73




Figure 50.-Test FLEX-046. Fiber-supported methanol droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) field of


view (FOV) for the entire test. There was significant oscillatory axial motion during the most of the test,
but at the very end, the droplet became stationary and there was some deformation, growth, and shape
change. A small disruption occurred coincident with flame extinction.


NASA/TP-2015-216046 74




Figure 51.-Test FLEX-047. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet drifted east out of the High-Bit-Depth Multispectral (HiBMs)


field of view (FOV) about halfway through the test. The droplet oscillated for several seconds before
the droplet left the FOVs of all the cameras. It left the Low Light Level Ultra-Violet (LLUV) FOV last,
oscillating as it translated south out of the FOV. The radiometer showed that the flame persisted even
after the droplet left the FOV. Extrapolating the burning history to when the radiometer indicated
extinction (with large error bars) showed that the droplet burned nearly to extinction. There was no
evidence of disruptive burning in any of the camera views. The color camera did not capture the flame
history correctly because it did not zoom out.


NASA/TP-2015-216046 75




Figure 52.-Test FLEX-048. Fiber-supported methanol droplet translating 3 mm/s and burning in a
cabin air (0.21/0.79 O2/N2), 1.0-atm ambient environment. The droplet drifted east after the start of
translation and out of the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) about one-fifth of
the way through the test. The flame remained within the FOVs of the Low Light Level Ultra-Violet
(LLUV) and color camera for the entire test. There was disruptive burning at the end of the test.


NASA/TP-2015-216046 76




Figure 53.-Test FLEX-049. Fiber-supported heptane droplet translating 3 mm/s and burning in a cabin
air (0.21/0.79 O2/N2), 1-atm ambient environment. The High-Bit-Depth Multispectral (HiBMs) Image
Processing and Storage Unit (IPSU) stopped recording for a few seconds, which resulted in a gap in
the droplet history. The droplet oscillated on the fiber throughout the test, with the amplitude and
frequency changing. There also was some unusual gas-phase recirculation evident from soot particle
motion. The droplet vaporized vigorously after the visible flame extinguished, and a large vapor cloud
formed near the end of the recording period. This is evidence of cool flame burning and extinction
following visible flame extinction.


NASA/TP-2015-216046 77




Figure 54.-Test FLEX-050. Fiber-supported heptane droplet translating 3 mm/s and burning in a cabin
air (0.21/0.79 O2/N2), 1-atm ambient environment. There were moderate transverse oscillations on
the fiber throughout the test, and unique circulation patterns in the gas phase were evident from the
soot motion. The droplet continued to vaporize linearly after the visible flame extinguished, and a
large vapor cloud formed nearly coincident with a plateau in the droplet history. This is evidence of
cool flame burning and extinction following visible flame extinction.


NASA/TP-2015-216046 78




Figure 55.-Test FLEX-051. Fiber-supported heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) field


of view (FOV) for the entire test, and it burned to completion. The flame was very luminous flame
initially, but it disappeared abruptly halfway through the burn. The droplet had significant transverse
oscillations on the fiber, but it never dislodged.


NASA/TP-2015-216046 79




Figure 56.-Test FLEX-052. Fiber-supported heptane droplet translating 3 mm/s and burning in a
0.30/0.70 O2/N2, 1.0-atm ambient environment. The droplet oscillated significantly on the fiber
throughout the burn. There also was significant sooting, with large agglomerates stuck to the fiber
(which created scatter in the droplet history). The droplet drifted partially out of the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) for a short time before moving back in. Late in the test,
significant oscillations, shape changes, and ejection of material from the droplet ended with a
disruption.


NASA/TP-2015-216046 80




Figure 57.-Test FLEX-053. Fiber-supported heptane droplet burning in a cabin air (0.21/0.79
O2/N2), 1.0-atm ambient environment. There were no High-Bit-Depth Multispectral (HiBMs) data
for this test. There was poor alignment between the needle and the droplet, and the droplet did not
deploy on the fiber. It drifted north in the color camera field of view (FOV) after deployment and
ignition and out of the FOV before the end of the test. However, the droplet remained in the Low
Light Level Ultra-Violet (LLUV) FOV for the entire test. The discrepancy in the flame size between
the LLUV and color camera was due to the flame being much brighter at the leading edge than at
the trailing edge, which resulted in some of the flame being cropped from the color camera images
during analysis.


NASA/TP-2015-216046 81




Figure 58.-Test FLEX-054. Free-floating methanol droplet burning in a 0.20/0.80 O2/N2, 0.7-atm
ambient environment. The droplet had almost no residual motion after ignition. About halfway through
the test, the droplet began to move abruptly north-northeast and then quickly changed direction to the
northeast. The droplet left the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) after the
second change in direction. The color camera views indicate that there may have been some small
gas bubbles in the droplet. There also was some distortion in the droplet history right before the droplet
changed direction. This could have been due to the expanding gas bubbles distorting the droplet, then
bursting and imparting a momentum to the droplet. The burning rate constant and flame standoff data
are for the portion of the test before the disruption and change in direction. Because the droplet was in
the HiBMs FOV for only a limited time and because there were disruptions in the droplet during the
burn, no extinction droplet diameter is reported.


NASA/TP-2015-216046 82




Figure 59.-Test FLEX-055. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.20/0.80 O2/N2, 0.7-atm ambient environment. The droplet remained in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) for the entire test. After the start of translation, the droplet
oscillated rapidly between the spots where the flame impinged on the fiber. The periodic noise in the
droplet history was caused by the oscillation, which stopped approximately halfway through the test.
The droplet then grew and had a small disruption (coincident with flame extinction) that left a small
residual droplet on the fiber.


NASA/TP-2015-216046 83




Figure 60.-Test FLEX-056. Free-floating heptane droplet burning in a 0.20/0.80 O2/N2, 0.70-atm
ambient environment. The droplet drifted east after ignition and left the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) shortly after the visible flame extinguished. The droplet reentered the
HiBMs FOV from the east a few seconds prior to the stop of video recording. A vapor cloud formed in
the color camera view approximately 20 s after the visible flame extinguished. It is not clear whether
cool flame burning and extinction occurred for this test.


NASA/TP-2015-216046 84




Figure 61.-Test FLEX-057. Fiber-supported heptane droplet translating 3 mm/s and burning in a
0.20/0.80 O2/N2, 0.70-atm ambient environment. There were moderate transverse and axial
oscillations on the fiber after deployment, during the entire visible flame, and after the visible flame
extinguished. The flame extinguished after the translation stopped, with the trailing edge of the flame
visibly weaker and extinguishing first. There were unusual, recirculating flow patterns in the High-Bit-
Depth Multispectral (HiBMs) fuel from soot that moved toward the droplet, accelerated
circumferentially in a short arc, and then moved radially toward the flame and back again. A small
vapor cloud formed in the color camera view approximately 20 s after the visible flame extinguished. It
is not clear whether cool flame burning and extinction was present in this test.


NASA/TP-2015-216046 85




Figure 62.-Test FLEX-058. Free-floating methanol droplet burning in a 0.18/0.82 O2/N2, 1.0-atm
ambient environment. The droplet drifted slowly east out of the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV), accelerating slowly before leaving the FOV. The droplet remained in the FOVs of
the Low Light Level Ultra-Violet (LLUV) and color camera for the entire test, and there was no
disruption. Because the droplet was not in the HiBMs FOV for the majority of the burning history, no
extinction droplet diameter is reported.


NASA/TP-2015-216046 86




Figure 63.-Test FLEX-059. Free-floating methanol droplet burning in a 0.18/0.82 O2/N2, 1.0-atm
ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) for the entire test, drifting north after deployment, stopping, drifting southwest to the corner of
the FOV, and then drifting north to the middle west of the FOV. The color camera Image Processing
and Storage Unit (IPSU) did not record any images for this test.


NASA/TP-2015-216046 87




Figure 64.-Test FLEX-060. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.18/0.82 O2/N2, 1.0-atm ambient environment. The droplet moved east in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) with translation and continued to move east along the fiber
and out of the FOV after the translation stopped. It also drifted partially out of the Low Light Level
Ultra-Violet (LLUV) FOV. The droplet then oscillated between the regions where the flame impinged on
the fiber for several seconds before becoming quiescent and burning until the flame extinguished,
presumably diffusively. There was no apparent disruption at or near flame extinction.


NASA/TP-2015-216046 88




Figure 65.-Test FLEX-061. Fiber-supported methanol droplet with no translation and burning in a
0.18/0.82 O2/N2, 1.0-atm ambient environment. The droplet remained stationary on the fiber and
within the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire test. The flame was
very dim in both the Low Light Level Ultra-Violet (LLUV) and color camera views.


NASA/TP-2015-216046 89




Figure 66.-Test FLEX-062. Free-floating heptane droplet burning in a 0.18/0.82 O2/N2, 1.0-atm
ambient environment. The droplet was nearly motionless after deployment and ignition and remained
in the fields of view (FOVs) of all the cameras for the entire test. The High-Bit-Depth Multispectral
(HiBMs) Image Processing and Storage Unit (IPSU) stopped recording images for a short time after
the visible flame extinguished. After the visible flame extinguished, there was continued rapid
vaporization and a large vapor cloud formed. This is indicative of cool flame burning and extinction
following visible flame extinction.


NASA/TP-2015-216046 90




Figure 67.-Test FLEX-063. Free-floating heptane droplet burning in a 0.18/0.82 O2/N2, 1.0-atm
ambient environment. The droplet drifted north in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) after deployment and ignition and out of the FOV two-thirds of the way through the test. There
was a small disruption near the end of the test. Extrapolating the droplet history using the average
burning rate constant resulted in a very small extinction droplet size, indicating that the droplet burned
essentially to completion.


NASA/TP-2015-216046 91




Figure 68.-Test FLEX-064. Fiber-supported heptane droplet translating 3 mm/s (for approximately
4 s) and burning in a 0.18/0.82 O2/N2, 1.0-atm ambient environment. The droplet had moderate
transverse oscillations and remained within the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) for the entire test. The flame grew and became dim blue. During translation, the leading edge
of the flame was bright and the fiber glowed brightly. The trailing edge of the flame was much dimmer
and the fiber did not glow. After the translation stopped, the flame extinguished and the droplet
vaporized significantly. A small disruption very late in the droplet lifetime left a small residual droplet
on the fiber. The behavior after the visible flame extinguished is indicative of cool flame burning and
extinction.


NASA/TP-2015-216046 92




Figure 69.-Test FLEX-065. Free-floating methanol droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. The droplet drifted south-southeast and out of the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) before the end of the test. The color camera Image Processing and
Storage Unit (IPSU) did not record any images for this test. The Low Light Level Ultra-Violet (LLUV)
showed a very long burn with a flame that appeared to get a little bit brighter for a short period of
time. Because the droplet was out of the HiBMs FOV for most of the droplet lifetime, no extinction
droplet diameter is reported.


NASA/TP-2015-216046 93




Figure 70.-Test FLEX-066. Free-floating methanol droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. The droplet drifted southeast and out of the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV), but then it drifted back into the FOV for a few seconds before the flame
extinguished. During ignition, the droplet changed shape when some material was apparently
ejected. The droplet shape oscillated immediately after this. The color camera Image Processing
and Storage Unit (IPSU) did not record any images for this test.


NASA/TP-2015-216046 94




Figure 71.-Test FLEX-067. Free-floating methanol droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. The flame oscillated significantly before the flame extinguished. After the
flame extinguished, the droplet drifted slowly east and then southeast and out of the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV).


NASA/TP-2015-216046 95




Figure 72.-Test FLEX-068. Free-floating methanol droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. The droplet drifted slowly to the north, turned south, then drifted slowly before
accelerating out of the field of view (FOV) right after the visible flame extinguished.


NASA/TP-2015-216046 96




Figure 73.-Test FLEX-069. Fiber-supported heptane droplet with no translation burning in a 0.15/0.85
O2/N2, 1.0-atm ambient environment. There was significant droplet motion during the entire very short
burn, and there appeared to be some visible distortions where the droplet edge intersected the fiber.
This small droplet had significant motion on the fiber, which had a marked influence on the burning
characteristics.


NASA/TP-2015-216046 97




Figure 74.-Test FLEX-070. Free-floating heptane droplet burning in a 0.15/0.85 O2/N2, 1.0-atm ambient
environment. Extra fuel was dispensed after the automated sequence started. After deployment, the
droplet drifted northwest in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV), hit the upper
igniter, and quickly drifted southeast and out of the HiBMs FOV. The post deployment/ignition velocity
was quite high, approximately 8 mm/s. The color camera Image Processing and Storage Unit (IPSU)
did not record any images after deployment. It is not known whether there was cool flame burning and
extinction for this test.


NASA/TP-2015-216046 98




Figure 75.-Test FLEX-071. Free-floating methanol droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. The droplet had a high drift velocity to the north after deployment. It hit the
igniter and then continued to move to the north-northwest after ignition at approximately 7 to 8 mm/s.
It left the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) relatively quickly and well before
the flame extinguished. Because the droplet was out of the HiBMs FOV for most of the burn, no
extinction droplet diameter is reported. The color camera Image Processing and Storage Unit (IPSU)
did not record any images after deployment.


NASA/TP-2015-216046 99




Figure 76.-Test FLEX-072. Free-floating heptane droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. This was a very small droplet, smaller than would be typically recommended
to burn in the apparatus. The droplet drifted north-northwest in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after deployment and ignition with a significant (7 to 8 mm/s) velocity,
and it left the FOV before the test was complete. The droplet burned with a dim blue flame to
completion without disruption. After ignition, there was only a little luminous region. This may have
been due to a small bubble burst during ignition (indicated by the droplet history).


NASA/TP-2015-216046 100




Figure 77.-Test FLEX-073. Free-floating heptane droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. There was an error in the automated test sequence, and the Multi-User Droplet
Combustion Apparatus (MDCA) dispensed fuel before deployment. The result was a very large
droplet, much larger than intended. The droplet drifted northwest in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after deployment, then it hit the igniter and began to drift southeast and
quickly out of the FOV. The droplet lifetime was very short with the flame extinguishing only a few
seconds after the igniter was withdrawn. The color camera Image Processing and Storage Unit
(IPSU) did not record any images after deployment, and there is not enough evidence to know
whether this test exhibited cool flame burning and extinction after the visible flame extinguished.


NASA/TP-2015-216046 101




Figure 78.-Test FLEX-074. Fiber-supported heptane droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. The droplet oscillated significantly on the fiber after deployment and throughout
the burn. The oscillations caused the droplet to become misshapen and caused large errors and
scatter in the droplet size measurements. This was a very short burn and, although there was not a
large disruption, the oscillations compromised the test data.


NASA/TP-2015-216046 102




Figure 79.-Test FLEX-075. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.13/0.85 O2/N2, 1.0-atm ambient environment. After deployment, there was some transverse, but
no axial, motion along the fiber. The transverse motion persisted throughout the test, but it stopped
after the flame extinguished. There was no axial motion relative to the fiber; that is, the droplet
started and stopped with the start and stop of the fiber. There also was no disruption during this test.


NASA/TP-2015-216046 103




Figure 80.-Test FLEX-076. Fiber-supported methanol droplet burning in a 0.14/0.86 O2/N2, 1.0-atm
ambient environment. The droplet oscillated axially on the fiber throughout the flame lifetime, only
becoming quiescent after the visible flame extinguished.


NASA/TP-2015-216046 104




Figure 81.-Test FLEX-077. Free-floating methanol droplet burning in a 0.14/0.85 O2/N2, 1.0-atm
ambient environment. There was very little droplet motion after deployment and ignition (it only moved a
few millimeters during the entire test).


NASA/TP-2015-216046 105




Figure 82.-Test FLEX-078. Free-floating methanol droplet burning in a 0.14/0.85 O2/N2, 1.0-atm ambient
environment. There was very little droplet motion after ignition. Halfway through the burn, the droplet
began to drift east at approximately 3 mm/s. It drifted out of the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) just before the flame extinguished. The extinction droplet diameter was extrapolated
from the droplet history and the measured average burning rate constant just prior to when the droplet
left the HiBMs FOV.


NASA/TP-2015-216046 106




Figure 83.-Test FLEX-079. Free-floating heptane droplet burning in a 0.13/0.85 O2/N2, 1.0-atm
ambient environment. This very short burn was entirely transient. The ambient environment was
probably below the quasi-steady flammability limit. A small vapor cloud formed shortly after the
visible flame extinguished, which may be indicative of cool flame burning and extinction following
hot flame extinction.


NASA/TP-2015-216046 107




Figure 84.-Test FLEX-080. Fiber-supported heptane droplet translating 3 mm/s and burning in a
0.13/0.87 O2/N2, 1.0-atm ambient environment. The High-Bit-Depth Multispectral (HiBMs) Image
Processing and Storage Unit (IPSU) did not record any images for this test. This test had a very
short flame lifetime, with the flame extinguishing before the droplet began to translate. A small
vapor cloud formed sometime after the visible flame extinguished. It is not clear whether there was
cool flame burning and extinction following visible flame extinction.


NASA/TP-2015-216046 108




Figure 85.-Test FLEX-081. Fiber-supported heptane droplet burning in a 0.13/0.87 O2/N2, 1.0-atm
ambient environment. The High-Bit-Depth Multispectral (HiBMs) and color camera Image
Processing and Storage Units (IPSUs) did not record any images after deployment. This was a
very short burn with almost no burning after the igniter was withdrawn.


NASA/TP-2015-216046 109




Figure 86.-Test FLEX-082. Free-floating methanol droplet burning in a 0.13/0.87 O2/N2, 1.0-atm
ambient environment. The deployment and ignition were very good, with almost no residual
motion. The droplet did drift south in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV)
and then drifted out of the FOV, but not until well after the flame extinguished. This was a very dim
flame.


NASA/TP-2015-216046 110




Figure 87.-Test FLEX-083. Free-floating methanol droplet burning in a 0.12/0.88 O2/N2, 1.0-atm
ambient environment. The High-Bit-Depth Multispectral (HiBMs) Image Processing and Storage
Unit (IPSU) did not record any images for this test. The droplet did not drift after deployment and
ignition and remained in the fields of view (FOVs) of both the Low Light Level Ultra-Violet (LLUV)
and color camera. The flame was very dim and almost undetectable by the LLUV (especially later
in the flame lifetime). As a result, the LLUV flame size measurements are not accurate.


NASA/TP-2015-216046 111




Figure 88.-Test FLEX-084. Free-floating methanol droplet burning in a 0.13/0.87 O2/N2, 1.0-atm
ambient environment. The droplet drifted north after deployment and ignition (deployment-induced
motion) and out of the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) halfway through the
test. The flame remained within the Low Light Level Ultra-Violet (LLUV) and color camera FOVs
during the entire test. The droplet burned for a long time in this ambient environment. The extinction
droplet diameter was based on extrapolating the droplet history using the measured burning rate
constant while the droplet was within the HiBMs FOV. The flame was very dim, and the LLUV flame
data are not as reliable as for the other tests because of the intensifier noise.


NASA/TP-2015-216046 112




Figure 89.-Test FLEX-085. Free-floating methanol droplet burning in a 0.13/0.87 O2/N2, 1.0-atm
ambient environment. The droplet drifted northwest in the High-Bit-Depth Multispectral (HiBMs) field
of view (FOV) and then drifted out of the FOV about halfway through the test. The flame remained
within the Low Light Level Ultra-Violet (LLUV) and color camera FOVs for the entire test. The
extinction droplet diameter is based on extrapolating the droplet history using the known burning rate
constant from the droplet history until just before the droplet left the HiBMs FOV.


NASA/TP-2015-216046 113




Figure 90.-Test FLEX-086. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.13/0.87 O2/N2, 1.0-atm ambient environment. The droplet oscillated transversely on the fiber
throughout the test. It continued to move (relative to the fiber) even after the fiber stopped translating.
It drifted out of the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) and to the edge of the
Low Light Level Ultra-Violet (LLUV) FOV. Only about half of the test was captured by the HiBMs. The
color camera Image Processing and Storage Unit (IPSU) did not record any images after deployment.
The extinction droplet diameter was based on extrapolating the droplet history using the measured
burning rate constant while the droplet was within the HiBMs FOV (and extinction from the LLUV).


NASA/TP-2015-216046 114




Figure 91.-Test FLEX-087. Fiber-supported methanol droplet with no translation and burning in a
0.13/0.87 O2/N2, 1.0-atm ambient environment. Throughout the burn, there were significant axial
oscillations along the fiber axis. The oscillations were significant and persistent. The droplet
remained within the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire test,
and it burned for a relatively long time in this low-O2 ambient environment. Because the flame was
very dim, the Low Light Level Ultra-Violet (LLUV) flame size measurements are not reliable.


NASA/TP-2015-216046 115




Figure 92.-Test FLEX-088. Free-floating methanol droplet burning in a 0.25/0.60/0.15 O2/N2/CO2,
0.70-atm ambient environment. The droplet deployed and ignited with almost no residual motion.
It remained within the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire test.
The droplet burned cleanly with a brighter-than-usual blue flame during the entire test. Near the
end of the test, the droplet deformed (becoming football shaped). Then the droplet disrupted
coincident with flame extinction. The droplet shattered at the end of the test, indicating that it was
probably compromised by contamination from the conformal coating on the needle.


NASA/TP-2015-216046 116




Figure 93.-Test FLEX-089. Free-floating methanol droplet burning in a 0.25/0.60/0.15 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted slowly to the east in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV), then drifted out of the FOV before the test ended. As the
droplet was leaving the HiBMs FOV, the liquid began to oscillate slightly. The motion was visible in
the color camera view. The flame extinguished abruptly-probably because of disruption.


NASA/TP-2015-216046 117




Figure 94.-Test FLEX-090. Fiber-supported methanol droplet with no translation in a 0.25/0.60/0.15
O2/N2/CO2, 0.70-atm ambient environment. There were significant axial and transverse oscillations
on the fiber after ignition. While the droplet was oscillating on the fiber, "sparklers" were evident on
the color camera view. Then the oscillations diminished and the droplet burned cleanly (on the color
camera view as well). A few seconds before the flame extinguished, there was a disruption (without
dislocation), followed by a complete disruption, dislocation, and flame extinction.


NASA/TP-2015-216046 118




Figure 95.-Test FLEX-091. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.25/0.60/0.15 O2/N2/CO2, 0.70-atm ambient environment. There were moderate axial oscillations on
the fiber (lower frequency than for some of the tests with severe oscillations) while the droplet was
translating. The oscillations stopped and the droplet burned nicely until the end of the test, when
there was a disruption coincident with flame extinction. The increase in droplet size at the end of the
test was probably the result of bubble nucleation and growth.


NASA/TP-2015-216046 119




Figure 96.-Test FLEX-092. Free-floating heptane droplet burning in a 0.14/0.86 O2/N2, 0.7-atm
ambient environment. The droplet drifted north and out of the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) before the burn was complete (about 60 percent of the burn was
captured with the HiBMs). The burn looked very clean. The droplet burned for a very long time to
a small size, with a disruption that was coincident with flame extinction.


NASA/TP-2015-216046 120




Figure 97.-Test FLEX-093. Fiber-supported heptane droplet translating 3 mm/s and burning in a
0.24/0.56/0.20 O2/N2/CO2, 0.70-atm ambient environment. There was a lot of transverse and axial
oscillatory motion during the entire droplet burn. The droplet did not leave the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) during the test, but the burning rate was high, probably
because of the significant and high-frequency oscillations.


NASA/TP-2015-216046 121




Figure 98.-Test FLEX-094. Free-floating heptane droplet burning in a 0.27/0.56/0.20 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north after deployment and ignition and out of the
High-Bit-Depth Multispectral (HiBMs) field of view (FOV) shortly after the visible flame extinguished.
Sometime after the visible flame extinguished, a large vapor cloud formed. This is indicative of cool
flame burning and extinction following visible flame extinction.


NASA/TP-2015-216046 122




Figure 99.-Test FLEX-095. Fiber-supported heptane droplet translating 3 mm/s (for approximately
4 s) and burning in a 0.24/0.56/0.20 O2/N2/CO2, 0.70-atm ambient environment. The droplet had
very little axial or transverse oscillation on the fiber, and it remained within the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) for the entire test. Shortly after the fiber translation
stopped, the visible flame extinguished, but the droplet continued to vaporize at a relatively high
rate. Then there was some axial oscillation on the fiber, followed by a significant reduction in the
vaporization rate. The marked decrease in vaporization was coincident with the formation of a
large vapor cloud, with a toroidal vapor cloud in the immediate vicinity of the droplet. This is
indicative of cool flame burning and extinction following visible flame extinction.


NASA/TP-2015-216046 123




Figure 100.-Test FLEX-096. Fiber-supported heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,


1.0-atm ambient environment. The High-Bit-Depth Multispectral (HiBMs) Image Processing and
Storage Unit (IPSU) did not record any images for this test. There were significant oscillations on the
fiber, so severe that the droplet dislodged from the fiber and drifted south and out of the color camera
and Low Light Level Ultra-Violet (LLUV) fields of view (FOVs).


NASA/TP-2015-216046 124




Figure 101.-Test FLEX-097. Free-floating methanol droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north with a relatively high velocity in the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV) after deployment and ignition, and it drifted out of the
FOV shortly after ignition. The droplet appeared to drift close enough to the needle to start a needle
fire (also visible on the Low Light Level Ultra-Violet, LLUV). This changed the droplet direction from
north to east in the color camera FOV, and it pushed the droplet north in the LLUV FOV. While the
needle was still burning, the droplet quickly left the color camera FOV, but it remained in the LLUV
FOV, drifting south after deployment and ignition until it left the LLUV FOV before extinction or
disruption.


NASA/TP-2015-216046 125




Figure 102.-Test FLEX-098. Free-floating methanol droplet burning in a 0.23/0.52/0.25 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after deployment and ignition, to the edge of the FOV, then east and
out of HiBMs FOV before the end of the test. The flame "swirled" a little before extinction in both
Low Light Level Ultra-Violet (LLUV) and color camera. The droplet was not in the HiBMs FOV long
enough to obtain an accurate estimate of the extinction droplet diameter.


NASA/TP-2015-216046 126




Figure 103.-Test FLEX-099. Free-floating methanol droplet burning in a 0.23/0.52/0.25 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north and out of the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after deployment and ignition. It appeared to drift close to the needle
(no fire) in the color camera view and was pushed away slightly. It remained in both the Low Light
Level Ultra-Violet (LLUV) and color camera FOVs until the flame extinguished. The droplet was not
in the HiBMs FOV long enough to obtain a good estimate of the extinction droplet diameter.


NASA/TP-2015-216046 127




Figure 104.-Test FLEX-100. Free-floating heptane droplet burning in a 0.23/0.52/0.25 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north after deployment and ignition, and out of
High-Bit-Depth Multispectral (HiBMs) field of view (FOV) just after the visible flame extinguished
radiatively at a relatively large droplet size. A vapor cloud, which is indicative of cool flame burning
and extinction, formed approximately 15 s after the visible flame extinguished.


NASA/TP-2015-216046 128




Figure 105.-Test FLEX-101. Fiber-supported heptane droplet translating 3 mm/s (for approximately
4 s) and burning in a 0.23/0.52/0.25 O2/N2/CO2, 0.70-atm ambient environment. There was a little
axial and transverse oscillation after deployment and ignition and during translation of the fiber, but
for most of the burn and postburn, the droplet was relatively quiescent. The droplet remained in the
High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire recording of the HiBMs Image
Processing and Storage Unit (IPSU). The flame extinguished radiatively, preferentially along the
fiber axis. The droplet continued to vaporize at a high rate after the visible flame extinguished. The
vaporization then slowed considerably, and a visible vapor cloud formed, which is indicative of cool
flame burning and extinction following visible flame extinction.


NASA/TP-2015-216046 129




Figure 106.-Test FLEX-102. Free-floating heptane droplet burning in a 0.21/0.49/0.30 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after deployment and ignition and out of the HiBMs FOV shortly after
the visible flame extinguished. The color camera Image Processing and Storage Unit (IPSU) failed
to record any images after the droplet deployed. The flame extinguished radiatively, and a vapor
cloud was visible on the downlink video sometime after the visible flame extinguished. This is
indicative of cool flame burning and extinction following visible flame extinction.


NASA/TP-2015-216046 130




Figure 107.-Test FLEX-103. Fiber-supported heptane droplet translating 3 mm/s and burning in a
0.21/0.49/0.30, 0.70-atm ambient environment. A short time after translation stopped, the droplet
moved axially on the fiber and partially out of the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV). By the end of the HiBMs Image Processing and Storage Unit (IPSU) recording, it had moved
completely back into the HiBMs FOV. A small droplet or debris on the fiber ignited and burned briefly,
but it burned out before the flame extinguished radiatively before translation stopped. For a while, the
droplet continued to vaporize at a relatively high rate. Then the vaporization rate slowed coincident
with the formation of a visible vapor cloud that formed a toroidal ring around the droplet. The
background intensity in the HiBMs decreased significantly as the vapor cloud formed. The post-
visible-flame-extinction behavior is indicative of cool flame burning and extinction.


NASA/TP-2015-216046 131




Figure 108.-Test FLEX-104. Free-floating methanol droplet burning in a 0.21/0.49/0.30 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north after deployment and ignition and out of the
High-Bit-Depth Multispectral (HiBMs) field of view (FOV) about one-third of the way through the test.
The color camera Image Processing and Storage Unit (IPSU) did not record any images after
deployment. The flame extinguished diffusively without disruption. Because the droplet was in the
HiBMs FOV for only a short fraction of the burn time, no extinction droplet diameter is reported.


NASA/TP-2015-216046 132




Figure 109.-Test FLEX-105. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.24/0.56/0.20 O2/N2/CO2, 0.70-atm ambient environment. There was significant axial oscillatory
motion on the fiber after deployment and ignition that persisted after fiber translation stopped about
halfway through the burn. The droplet then burned without axial or transverse motion until it disrupted
and dislocated from the fiber coincident with flame extinction.


NASA/TP-2015-216046 133




Figure 110.-Test FLEX-106. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.23/0.52/0.25 O2/N2/CO2, 0.70-atm ambient environment. The droplet moved west along the fiber a
short distance after deployment and ignition but before translation and then moved east with the fiber
during translation. The droplet remained within the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) for the entire test. There was very little motion of the droplet relative to the fiber during the test.
However, a small disruption coincident with flame extinction left a slightly smaller droplet on the fiber.
The extinction droplet diameter is the droplet diameter just prior to the disruption.


NASA/TP-2015-216046 134




Figure 111.-Test FLEX-107. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.24/0.56/0.20 O2/N2/CO2, 0.70-atm ambient environment. There was not much axial oscillatory
motion associated with fiber motion, but there were some transverse oscillations. There was no
shape change prior to disruption, which was right around the time of extinction.


NASA/TP-2015-216046 135




Figure 112.-Test FLEX-108. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.23/0.52/0.25 O2/N2/CO2, 0.70-atm ambient environment. There was significant oscillatory motion
of the droplet on the fiber during the burn both before and after the translation. The droplet swelled
and eventually disrupted before the flame extinguished, leaving a small residual droplet on the
fiber.


NASA/TP-2015-216046 136




Figure 113.-Test FLEX-109. Free-floating methanol droplet burning in a 0.21/0.49/0.30 O2/N2/CO2,
0.70-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
and color camera fields of view (FOVs) for the entire Image Processing and Storage Unit (IPSU)
recording time (even after the visible flame extinguished). The Low Light Level Ultra-Violet (LLUV)
IPSU did not record any images for this test. The droplet deformed (became aspherical) right
around the time of extinction and remained misshapen after the flame extinguished. The fuel may
have been contaminated during this test.


NASA/TP-2015-216046 137




Figure 114.-Test FLEX-110. Free-floating methanol droplet burning in a 0.21/0.49/0.30 O2/N2/CO2,
0.70-atm ambient environment. The droplet remained in the fields of view (FOVs) of all cameras,
and the flame extinguished radiatively. Because the flame was very dim and there was a smudge on
the Combustion Integrated Rack (CIR) Low Light Level Ultra-Violet (LLUV) viewing window, the
LLUV data have a lot of noise.


NASA/TP-2015-216046 138




Figure 115.-Test FLEX-111. Fiber-supported methanol droplet burning in a 0.21/0.49/0.30 O2/N2/CO2,
0.70-atm ambient environment with fiber translation after ignition. This was an almost ideal fiber-
supported test, with almost no oscillation of the droplet. The fiber started and stopped moving with
almost no relative motion imparted to the droplet.


NASA/TP-2015-216046 139




Figure 116.-Test FLEX-112. Fiber-supported methanol droplet burning in a 0.21/0.49/0.30 O2/N2/CO2,
0.70-atm ambient environment. There was no fiber translation during this test. The droplet initially
moved west in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) before stopping and then
slowly moving back to the center of the image. A little disruption (maybe a small gas bubble popping)
occurred near flame extinction coincident with a small satellite droplet being ejected from the droplet.


NASA/TP-2015-216046 140




Figure 117.-Test FLEX-113. Free-floating methanol droplet burning in a 0.20/0.45/0.35 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted northwest after deployment in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV), hit the igniter, and then drifted southeast after ignition and
out of the FOV approximately 8 s after the igniter was withdrawn. The droplet burned with a very
weak relatively steady flame for a long period of time before oscillating before extinction. The
extinction droplet diameter is based on an extrapolation of the droplet history to the time of extinction.
The measured burning rate constant from just before the droplet left the HiBMs FOV was used in the
extrapolation.


NASA/TP-2015-216046 141




Figure 118.-Test FLEX-114. Free-floating methanol droplet burning in a 0.20/0.45/0.35 O2/N2/CO2,
0.70-atm ambient environment. After ignition, the droplet drifted northeast and out of the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV). The droplet remained out of the FOV until just
before the flame extinguished, when it drifted back into the FOV from the northeast corner.


NASA/TP-2015-216046 142




Figure 119.-Test FLEX-115. Fiber-supported methanol droplet translating 3 mm/s and burning in a
0.20/0.45/0.35 O2/N2/CO2, 0.70-atm ambient environment. A small residue on the fiber to the west of
the droplet ignited a few seconds after the droplet ignited. During translation, this residue burned
with a very bright luminous flame for 1 to 2 s. The droplet drifted partially out of the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) after the translation stopped, then it shrank back so that it
was completely in the FOV. There appeared to be some oscillations near extinction. The droplet
burned without any transverse or axial oscillations along the fiber, and it did not disrupt or deform.


NASA/TP-2015-216046 143




Figure 120.-Test FLEX-116. Fiber-supported methanol droplet (translated for approximately 3 s
immediately after ignition) burning in a 0.20/0.45/0.35 O2/N2/CO2, 0.70-atm ambient environment.
This was a very clean test with very little motion of the droplet on the fiber.


NASA/TP-2015-216046 144




Figure 121.-Test FLEX-117. Free-floating heptane droplet burning in a 0.20/0.45/0.35 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition and out of the FOV after the visible flame
extinguished. The droplet had a very low burning rate constant. A relatively large vapor cloud formed
well after the visible flame extinguished, which indicates that there was probably cool flame burning
and extinction after visible flame extinction.


NASA/TP-2015-216046 145




Figure 122.-Test FLEX-118. Fiber-supported heptane droplet burning in a 0.20/0.45/0.25 O2/N2/CO2,
0.70-atm ambient environment. The droplet ignited, and shortly after ignition, a small droplet or
debris ignited to the west (color camera) or north (Low Light Level Ultra-Violet, LLUV) of the droplet.
This small droplet or particle burned for only a short time and was not visible in the High-Bit-Depth
Multispectral (HiBMs). The droplet burns for only a short time before the visible flame extinguished
radiatively. Rapid vaporization continued, however, and approximately 5 s after the visible flame
extinguished, a vapor cloud formed. This is an indication of cool flame burning and extinction
following visible flame extinction.


NASA/TP-2015-216046 146




Figure 123.-Test FLEX-119. Fiber-supported heptane droplet burning in a 0.18/0.42/0.40 O2/N2/CO2,
0.70-atm ambient environment. After ignition the flame extinguished quickly, probably radiatively. It is
quite possible that this ambient condition was below the flammability limit for heptane. The droplet
had some unusual oscillations on the fiber during the burn that seemed to disappear for most of the
test (after the flame extinguished). The color camera Image Processing and Storage Unit (IPSU) did
not record any images for this test. There was a brief period of significant vaporization after the visible
flame extinguished; then a small vapor cloud formed. This is indicative of cool flame burning and
extinction following visible flame extinction.


NASA/TP-2015-216046 147




Figure 124.-Test FLEX-120. Fiber-supported heptane droplet with fiber translation burning in a
0.18/0.42/0.40 O2/N2/CO2, 0.70-atm ambient environment. The droplet did not oscillate much on
the fiber during or after the burn. A small vapor cloud formed after the visible flame extinguished. It
is difficult to determine whether there was cool flame burning and extinction from the available
data. The Low Light Level Ultra-Violet (LLUV) Image Processing and Storage Unit (IPSU) did not
record any images during the burn.


NASA/TP-2015-216046 148




Figure 125.-Test FLEX-121. Free-floating methanol droplet burning in a 0.18/0.42/0.40 O2/N2/CO2,
0.70-atm ambient environment. The droplet did not drift at all in any of the camera fields of view
(FOVs) after deployment and ignition. The flame oscillated a few times before extinguishing
radiatively.


NASA/TP-2015-216046 149




Figure 126.-Test FLEX-122. Free-floating methanol droplet burning in a 0.18/0.42/0.40 O2/N2/CO2,
0.7-atm ambient environment. The droplet was almost motionless after deployment and ignition. It
then slowly drifted south and eventually out of the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV), but this was after the flame extinguished. The droplet burned for about 15 s. Even though the
flame appeared to be weak, it persisted for quite a while. This was a nice clean burn with no
distortion or disruption. The flame appeared to oscillate radially (primarily in intensity) a few seconds
before it extinguished.


NASA/TP-2015-216046 150




Figure 127.-Test FLEX-123. Fiber-supported methanol droplet burning in a 0.18/0.42/0.40 O2/N2/CO2,
0.70-atm ambient environment. There was no fiber translation, and the large droplet appeared to
extinguish radiatively. The color camera Image Processing and Storage Unit (IPSU) did not record
any images after deployment. The Low Light Level Ultra-Violet (LLUV) IPSU lost data for about 5 s
during the test. Also, the Low Light Level Ultra-Violet (LLUV) images were very dim, and it was almost
impossible to detect the edges of the flame. In the LLUV view, the flame appeared to be quenched
where the flame and fiber met.


NASA/TP-2015-216046 151




Figure 128.-Test FLEX-124. Free-floating methanol droplet burning in a 0.18/0.42/0.40 O2/N2/CO2,
0.70-atm ambient environment. The droplet remained in the fields of view (FOVs) of all the
cameras for the entire burn. The droplet burned for only a short time, and the flame probably
extinguished radiatively.


NASA/TP-2015-216046 152




Figure 129.-Test FLEX-125. Free-floating methanol droplet burning in a 0.17/0.38/0.45 O2/N2/CO2,
0.70-atm ambient environment. The droplet remained in the fields of view (FOVs) of all cameras
after deployment and ignition. The flame oscillated for one or two cycles before extinguishing
radiatively. This test was very near, if not below, the flammability limit. Because the flame was
barely distinguishable from the background in the Low Light Level Ultra-Violet (LLUV), the color
camera flame size data are a bit more reliable than the LLUV data, which have a lot of noise.


NASA/TP-2015-216046 153




Figure 130.-Test FLEX-126. Free-floating methanol droplet burning in a 0.17/0.38/0.45 O2/N2/CO2,
0.70-atm ambient environment. The droplet remained in the fields of view (FOVs) of all cameras
after deployment and ignition. The droplet burned a relatively long time and appeared to
extinguish diffusively.


NASA/TP-2015-216046 154




Figure 131.-Test FLEX-127. Fiber-supported methanol with no translation burning in a 0.17/0.38/0.45
O2/N2/CO2, 0.70-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) for the entire test. The flame then became very dim blue and was nearly
cylindrical because of flame quenching due to the support fiber. There was little fiber glow (broadband
radiation from the heated fiber) after the droplet stopped translating, and the flame measurements
from the color camera indicated that the flame size oscillated periodically after the droplet stopped
translating. The HiBMs Image Processing and Storage Unit (IPSU) stopped recording for a relatively
large block of time: from just before the igniter withdrew to about halfway through the burn.


NASA/TP-2015-216046 155




Figure 132.-Test FLEX-128. Fiber-supported methanol droplet burning in a 0.17/0.38/0/45 O2/N2/CO2,
0.70-atm ambient environment. Shortly after ignition, the droplet began to move west along the fiber
at ~8 mm/s. It left the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) about one-third of the
way through the test. The flame was brighter at the leading edge during the translation. When the
translation stopped, the flame was quenched by the fiber at both ends, making the flame more
cylindrical than spherical. Because the droplet was in the HiBMs FOV for only a short fraction of the
burn, no extinction droplet diameter is reported.


NASA/TP-2015-216046 156




Figure 133.-Test FLEX-129. Free-floating heptane droplet burning in a 0.17/0.38/0.45 O2/N2/CO2,
0.70-atm ambient environment. The droplet remained in the fields of view (FOVs) of all the
cameras for the very short burn and for a considerable period of time after the visible flame
extinguished. The Low Light Level Ultra-Violet (LLUV) stopped recording images for several
seconds right around ignition. This was a very short burn with no appreciable vaporization or
vapor cloud formation after the visible flame extinguished. There was probably no cool flame or
only a very brief cool flame.


NASA/TP-2015-216046 157




Figure 134.-Test FLEX-130. Fiber-supported heptane droplet translating 3 mm/s and burning in a
0.17/0.38/0.45 O2/N2/CO2, 0.7-atm ambient environment. This was a very short burn, and the
flame extinguished radiatively very soon after translation began. No vapor cloud formed, and the
vaporization rate was quite small after the visible flame extinguished. As a result, there was
probably no, or only very brief, cool flame burning.


NASA/TP-2015-216046 158




Figure 135.-Test FLEX-131. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,


1.0-atm ambient environment. This smaller droplet remained in the fields of view (FOVs) of all the


cameras for the entire test. The droplet extinguished disruptively at a small size.


NASA/TP-2015-216046 159




Figure 136.-Test FLEX-132. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted slowly northeast after ignition, but it remained in


the field of view (FOV) for the entire test. The droplet was initially luminous with a bright yellow
flame that eventually turned blue with a little yellow and then blue until the end of the test. The
droplet burned to a small size before a small disruption when the flame extinguished. The Low
Light Level Ultra-Violet (LLUV) Image Processing and Storage Unit (IPSU) stopped recording for
about 7 s in the middle of the test.


NASA/TP-2015-216046 160




Figure 137.-Test FLEX-133. Free-floating heptane droplet in a 0.24/0.56/0.20 O2/N2/CO2, 1.0-atm
ambient environment. The droplet drifted northwest and out of the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) before the end of the test (about halfway). After ignition, the droplet
flame was luminous, quickly changing to a nearly all blue, dim flame. The flame then began to
oscillate for several seconds before becoming stable and brighter. It burned until a small
disruption coincident with when the flame extinguished. The extinction droplet diameter is the
diameter of the droplet when the flame disrupted; it was estimated from the burning rate constant
while the droplet was in the HiBMs FOV and the time of extinction from either the Low Light Level
Ultra-Violet (LLUV) or color camera.


NASA/TP-2015-216046 161




Figure 138.-Test FLEX-134. Free-floating heptane droplet in a 0.24/0.56/0.20 O2/N2/CO2, 1.0-atm
ambient environment. There were problems with gas bubbles during dispensing, stretching, and
deployment. During this test, a small gas bubble burst during ignition and caused the droplet to
oscillate. The droplet drifted slowly southeast and out of the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) a few seconds after the flame extinguished radiatively. The droplet continued
to vaporize at a relatively high rate after the flame extinguished, although only a few seconds
passed before the droplet left the HiBMs FOV. A vapor cloud formed 10 to 20 s after the visible
flame extinguished. The post-visible-flame-extinction behavior is indicative of cool flame burning
and extinction.


NASA/TP-2015-216046 162




Figure 139.-Test FLEX-135. Fiber-supported heptane droplet with no translation in a 0.24/0.56/0.20
O2/N2/CO2, 1.0-atm ambient environment. A small droplet to the west of the main droplet ignited and
quickly burned off. There was significant transverse and axial motion of the droplet on the fiber
during most of the test. The droplet drifted west on the fiber after deployment; then it stopped and
oscillated (irregularly) axially and transversely during the entire burn. The shape changed briefly
from spherical when there was a discrete change in droplet size that corresponded to something
being ejected from the droplet (visible on the color camera).


NASA/TP-2015-216046 163




Figure 140.-Test FLEX-136. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted northwest in the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV) after deployment, then it hit the igniter and moved northeast and out
of the HiBMs FOV. Because the droplet was in the HiBMs FOV for only a small fraction of the
droplet lifetime, no extinction droplet diameter is reported. It is not clear whether the droplet
burned to completion or the flame extinguished at a finite droplet size. However, given the ambient
conditions and the expected burning behavior, burnout is more likely.


NASA/TP-2015-216046 164




Figure 141.-Test FLEX-137. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted northwest and out of the High-Bit-Depth


Multispectral (HiBMs) field of view (FOV) about halfway through the test. After deployment, there
was a disruption (maybe a bubble burst because these droplets had issues with gas bubbles) that
caused significant droplet deformation and oscillations. There also was a moderate degree of
sooting. The droplet burned to a relatively small size before disruptive extinction. The noise in the
beginning of the droplet history was due to soot influencing the droplet size measurement. The color
camera Image Processing and Storage Unit (IPSU) failed to record any images after deployment.
The Low Light Level Ultra-Violet (LLUV) IPSU stopped recording images for a brief time in the
middle of the burn.


NASA/TP-2015-216046 165




Figure 142.-Test FLEX-138. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,


1.0-atm ambient environment. The High-Bit-Depth Multispectral (HiBMs) Image Processing and


Storage Unit (IPSU) did not record any images for this test. The flame grew in size initially, became
very dim, but then shrank, became brighter, and burned to disruption at a small size.


NASA/TP-2015-216046 166




Figure 143.-Test FLEX-139. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,


1.0-atm ambient environment. The droplet deformed shortly after deployment, presumably because


of a gas bubble that burst. This caused the droplet to drift slowly northeast in the High-Bit-Depth
Multispectral (HiBMs). A large flash coincident with ignition caused the droplet to drift southwest at
approximately 6 mm/s. The droplet drifted with a constant trajectory until it left the HiBMs field of
view (FOV) about halfway through the test. The burning rate was relatively high, and the flame was
distorted by the large drift velocity. The droplet burned to a small size, then disrupted when the flame
extinguished.


NASA/TP-2015-216046 167




Figure 144.-Test FLEX-140. Free-floating methanol droplet burning in a 0.15/0.35/0.50 O2/N2/CO2,
0.70-atm ambient environment. The droplet had a very small drift south after deployment and
ignition, but it remained in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire
recording time. For this very short burn, either the droplet was significantly larger than the radiative
extinction limit or the test was completely outside of the quasi-steady flammability boundary.


NASA/TP-2015-216046 168




Figure 145.-Test FLEX-141. Free-floating methanol droplet burning in a 0.15/0.35/0.50 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted slowly south, but it remained in the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV) for the entire test and well after the flame
extinguished. The droplet abruptly left the HiBMs FOV in the video, probably because the HiBMs
stopped archiving images for a short time. This very short burn either extinguished radiatively or was
completely outside of the quasi-steady flammability boundary.


NASA/TP-2015-216046 169




Figure 146.-Test FLEX-142. Free-floating methanol droplet burning in a 0.15/0.35/0.50 O2/N2/CO2,
0.70-atm ambient environment. The droplet deployed with a relatively high (~6 mm/s) drift velocity to
the northwest. The burn time was relatively short, and the droplet remained in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) for the entire test.


NASA/TP-2015-216046 170




Figure 147.-Test FLEX-143. Free-floating methanol droplet burning in a 0.15/0.35/0.50 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted north after deployment and ignition, and it drifted
out of the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) after the flame extinguished. It
then drifted back into the HiBMs FOV before Image Processing and Storage Unit (IPSU) recording
stopped (thus the gap in the droplet history shown in this figure). This smaller droplet had a very
short burn-probably outside of the quasi-steady flammability boundary or, more likely, right at the
boundary.


NASA/TP-2015-216046 171




Figure 148.-Test FLEX-144. Free-floating methanol droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. The droplet was nearly motionless after deployment and ignition.
Halfway through the burn, the droplet drifted south. It left the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) just before the flame extinguished, but it remained in the FOVs of the Low Light
Level Ultra-Violet (LLUV) and color camera. The burning rate constant measured near the end of the


time when the droplet was in the HiBMs FOV was used to extrapolate the extinction droplet diameter
from the droplet history from when the droplet left the HiBMs FOV until the flame extinguished.


NASA/TP-2015-216046 172




Figure 149.-Test FLEX-145. Free-floating methanol droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras


during the entire burn.


NASA/TP-2015-216046 173




Figure 150.-Test FLEX-146. Free-floating methanol droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. This very large droplet was nearly motionless after deployment and
ignition. The droplet eventually drifted south in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) and left the FOV a short time before the flame extinguished. Because the flame was very dim
and there was contamination on the Combustion Integrated Rack (CIR) LLUV viewing window, the
flame size from the color camera was a bit more reliable than that from the Low Light Level Ultra-
Violet (LLUV). The burning rate constant measured near the end of the time that the droplet was in


the High-Bit-Depth Multispectral (HiBMs) FOV was used to extrapolate the extinction droplet
diameter from the droplet history from when the droplet left the HiBMs FOV until the flame
extinguished.


NASA/TP-2015-216046 174




Figure 151.-Test FLEX-147. Free-floating methanol droplet burning in a 0.17/0.38/0.45 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted southeast at approximately 4 to 5 mm/s
(deployment-induced change of direction at ignition) and out of the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after a few seconds. The droplet remained in the FOVs of the Low Light
Level Ultra-Violet (LLUV) and color camera for the entire test, but it was at the very edge of the
FOVs of both cameras. The flame dimmed increasingly throughout the test. Because the droplet
was in the HiBMs FOV for only a small fraction of the burn, no extinction droplet diameter is
reported.


NASA/TP-2015-216046 175




Figure 152.-Test FLEX-148. Free-floating heptane droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. There was very little residual motion after deployment and ignition.
The droplet remained in the fields of view (FOVs) of all the cameras for the entire test. It burned


cleanly to small size, then it disrupted coincident with when the flame extinguished. The extinction
droplet size is the size when the droplet disrupted. The High-Bit-Depth Multispectral (HiBMs) Image
Processing and Storage Unit (IPSU) stopped recording data sometime before deployment to part
way through the burn. The plotted data used the first measured droplet as time zero even though the
droplet had been burning for some time before that point.


NASA/TP-2015-216046 176




Figure 153-Test FLEX-149. Free-floating heptane droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. The deployment was excellent with almost no residual motion after


deployment and ignition. The droplet drifted a little south in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV), but it remained in the FOVs of all cameras for the entire test. The droplet burned
cleanly down to a small size then disrupted coincident with flame extinction. The extinction droplet
size is the size when the disruption occurred.


NASA/TP-2015-216046 177




Figure 154.-Test FLEX-150. Free-floating heptane droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted northwest in the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV) after deployment and ignition, remained in the FOV for the entire burn,
and left the FOV shortly after the visible flame extinguished. The flame oscillated a few times before
it extinguished radiatively. A vapor cloud formed approximately 20 sec after the visible flame
extinguished, indicating cool flame burning and extinction after visible flame extinction. The color
camera Image Processing and Storage Unit (IPSU) did not record any images after deployment.


NASA/TP-2015-216046 178




Figure 155.-Test FLEX-151. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted northeast and out of the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) about one-fourth of the way through the burn. The droplet
burned for a very long time, but the flame was very dim and difficult to see, with significant noise in
the Low Light Level Ultra-Violet (LLUV) when automated analysis was used and a very low threshold
when manual analysis was used. The droplet oscillated for a few seconds halfway through the burn,
then it burned with a steady flame until it oscillated again right before the flame extinguished.
Because the droplet was in the HiBMs FOV for only a short time, no extinction droplet diameter is
reported.


NASA/TP-2015-216046 179




Figure 156.-Test FLEX-152. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)


field of view (FOV), and it left the FOV about two-thirds of the way through the burn. The burning
rate constant from the droplet history for a short period of time before the droplet left the HiBMs FOV
was used to extrapolate the extinction droplet diameter from the droplet history from when the
droplet left the HiBMs FOV until the flame extinguished.


NASA/TP-2015-216046 180




Figure 157.-Test FLEX-153. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted north after deployment and ignition; then it began


to drift back to the center. It remained in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV)
until four-fifths of the way through the burn when the HiBMs stopped recording data for about 5 s.
The HiBMs did not record data when the flame extinguished. It was a long burn, and the measured
burning rate constant for a short time right before recording stopped was used to extrapolate the
extinction diameter from the droplet history until the visible flame extinguished.


NASA/TP-2015-216046 181




Figure 158.-Test FLEX-154. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet had almost no residual motion after deployment and


ignition. This relatively large droplet remained in the High-Bit-Depth Multispectral (HiBMs) field of
view (FOV) for the entire (short) burn and for the entire recording time of the HiBMs Image
Processing and Storage Unit (IPSU). The droplet extinguished radiatively after a short burn with no
flame oscillations. Late in the recording time, there was significant post-visible-flame-extinction
vaporization and a large vapor cloud formed. The post-visible-flame-extinction behavior is indicative
of cool flame burning and extinction.


NASA/TP-2015-216046 182




Figure 159.-Test FLEX-155. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet had almost no residual motion after deployment and


ignition, and it remained in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire
time that images were recorded. The flame had a very short burn time and probably extinguished
radiatively. The vaporization rate was high after the visible flame extinguished, and there was an
eventual plateau late in the HiBMs Image Processing and Storage Unit (IPSU) recording time
coincident with the formation of a large vapor cloud. The post-visible-flame-extinction behavior is
indicative of cool flame burning and extinction.


NASA/TP-2015-216046 183




Figure 160.-Test FLEX-157. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. This very small droplet had a high northwest drift velocity in the High-


Bit-Depth Multispectral (HiBMs) field of view (FOV). The droplet left the HiBMs FOV about one-third
of the way through the test, and it moved past the northwest igniter before the igniter began to
withdraw. The color camera Image Processing and Storage Unit (IPSU) failed to record any frames
after deployment. Because the droplet was in the HiBMs FOV for only a short fraction of the entire
test, no extinction diameter is reported.


NASA/TP-2015-216046 184




Figure 161.-Test FLEX-158. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. This relatively large droplet was nearly motionless after deployment


and ignition, and it remained in the fields of view (FOVs) of all the cameras. The flame oscillated for
a few cycles (increasing in magnitude with time) until it extinguished radiatively. Because the flame
was dim and there was contamination on the Low Light Level Ultra-Violet (LLUV) viewing window,
the flame was difficult to see with the LLUV.


NASA/TP-2015-216046 185




Figure 162.-Test FLEX-159. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet was nearly motionless after deployment and ignition, and


it remained near the center of the fields of view (FOVs) for the entire test. The flame oscillated for
several cycles before extinguishing radiatively. Because the flame was very dim and there was
contamination on the Combustion Integrated Rack (CIR) LLUV viewing window, the Low Light Level
Ultra-Violet (LLUV) flame diameter data are very noisy.


NASA/TP-2015-216046 186




Figure 163.-Test FLEX-160. Free-floating methanol droplet burning in a 0.19/0.59/0.25 O2/N2/CO2,


1.0-atm ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras


for the entire burn, and the flame extinguished diffusively. Because the Low Light Level Ultra-Violet
(LLUV) images were dim and there was contamination on the Combustion Integrated Rack (CIR)
LLUV viewing window, the flame size data are a bit noisy but seem to be reasonable.


NASA/TP-2015-216046 187




Figure 164.-Test FLEX-161. Free-floating methanol droplet burning in a 0.16/0.59/0.25 O2/N2/CO2,


1.0-atm ambient environment. The droplet was nearly motionless after deployment and ignition, and


it remained in the fields of view (FOVs) of all the cameras for the entire burn, which was a long burn
to diffusive extinction. Because the Low Light Level Ultra-Violet (LLUV) images were dim and there
was contamination on the Combustion Integrated Rack (CIR) LLUV viewing window, and the LLUV
flame size data are very noisy.


NASA/TP-2015-216046 188




Figure 165.-Test FLEX-162. Free-floating methanol droplet burning in a 0.14/0.54/0.32 O2/N2/CO2,


1.0-atm ambient environment. The droplet was nearly motionless after deployment and ignition, and


it remained in the fields of view (FOVs) of all the cameras for the duration of the test. The flame
oscillated for several seconds with increasing magnitude before extinguishing radiatively. Because
the Low Light Level Ultra-Violet (LLUV) images were dim and there was contamination on the
Combustion Integrated Rack (CIR) LLUV viewing window, the LLUV flame data are very noisy.


NASA/TP-2015-216046 189




Figure 166.-Test FLEX-163. Free-floating methanol droplet burning in a 0.14/0.54/0.32 O2/N2/CO2,


1.0-atm ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras


for the entire burn. The flame oscillated for several cycles of increasing magnitude before
extinguishing radiatively. Because the Low Light Level Ultra-Violet (LLUV) images were dim and
there was contamination on the Combustion Integrated Rack (CIR) LLUV viewing window, the LLUV
flame data are very noisy.


NASA/TP-2015-216046 190




Figure 167.-Test FLEX-164. Free-floating methanol droplet burning in a 0.14/0.54/0.32 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted northwest in the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV) after deployment and ignition. It left the FOV just after the visible flame
extinguished. The flame oscillated several cycles with a nearly constant amplitude before
extinguishing radiatively. Because the Low Light Level Ultra-Violet (LLUV) images were dim and
there was contamination of the Combustion Integrated Rack (CIR) LLUV viewing window, the LLUV
flame data are noisy.


NASA/TP-2015-216046 191




Figure 168.-Test FLEX-165. Free-floating methanol droplet burning in a 0.14/0.54/0.32 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)


field of view (FOV) after deployment and ignition, left the FOV shortly after the visible flame
extinguished, and then drifted back into the FOV well after extinction near the end of recording.
Because this was a very dim flame and there was contamination on the Combustion Integrated Rack
(CIR) Low Light Level Ultra-Violet (LLUV) viewing window, the LLUV data are very noisy.


NASA/TP-2015-216046 192




Figure 169.-Test FLEX-166. Free-floating heptane droplet burning in a 0.18/0.670.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted southeast in the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV), remained in the FOV until the visible flame extinguished, and then
drifted out of the FOV. The flame became dimmer as the burn progressed, but it did not oscillate
before it extinguished, and no vapor cloud formed after visible flame extinction.


NASA/TP-2015-216046 193




Figure 170.-Test FLEX-167. Free-floating methanol droplet burning in a 0.14/0.50/0.36 O2/N2/CO2,


1.0-atm ambient environment. The droplet remained in the fields of view (FOVs) of all cameras. This


was a short burn to radiative extinction, and the color camera Image Processing and Storage Unit
(IPSU) did not record any images after deployment.


NASA/TP-2015-216046 194




Figure 171.-Test FLEX-168. Free-floating methanol droplet burning in a 0.136/0.50/0.363
O2/N2/CO2, 1.0-atm ambient environment. The droplet drifted west in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) after deployment, hit the igniter, and then drifted slowly
east after ignition. It left the HiBMs FOV shortly after the visible flame extinguished. The very dim
Low Light Level Ultra-Violet (LLUV) images and the contamination on the Combustion Integrated
Rack (CIR) LLUV viewing window resulted in a lot of noise in the data. The flame oscillated for
nearly half of its lifetime.


NASA/TP-2015-216046 195




Figure 172.-Test FLEX-169. Free-floating methanol droplet burning in a 0.21/0.64/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet was nearly motionless after deployment and ignition. It
drifted slightly around the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) and then
disrupted when the flame extinguished. The extinction droplet diameter is the diameter of the droplet
at disruption and not the true extinction droplet diameter.


NASA/TP-2015-216046 196




Figure 173.-Test FLEX-170. Free-floating methanol droplet burning in a 0.21/0.64/0.16 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)


field of view (FOV) after deployment and ignition. The droplet left the HiBMs FOV three-fourths of
the way through the burn; then it drifted back into the FOV just after the visible flame extinguished.
The extinction droplet diameter is the diameter of the droplet when it fully reappeared in the FOV. It
should be nearly identical to the diameter of the droplet when the visible flame extinguished.


NASA/TP-2015-216046 197




Figure 174.-Test FLEX-171. Free-floating methanol droplet burning in a 0.21/0.64/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted north in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition, and it drifted out of the HiBMs FOV about halfway
through the burn. The droplet then drifted back in shortly after the flame extinguished diffusively. The
extinction droplet diameter was determined from a cubic polynomial fit of the droplet history between
the two times that the droplet was in the HiBMs FOV (subject to the constraint that the slope of the
droplet history of the fit was equal to that of the experiment just before it left and after it returned to
the FOV).


NASA/TP-2015-216046 198




Figure 175.-Test FLEX-172. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. This was the first test after the needle and window were changed out


(cleaner window for the Low Light Level Ultra-Violet (LLUV)). The droplet remained in the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV) for the entire test with very little residual motion. The
LLUV image was very bright with none of the asymmetry observed in the previous tests. The flame
extinguished when the droplet was relatively large, and the droplet continued to vaporize at a
relatively high and nearly constant rate after the visible flame extinguished-indicating cool flame
burning and extinction after visible flame extinction. The color camera Image Processing and
Storage Unit (IPSU) did not record any images after deployment.


NASA/TP-2015-216046 199




Figure 176.-Test FLEX-173. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) for the entire test. The Low Light Level Ultra-Violet (LLUV) provided good
distortion-free, bright images. The flame extinguished radiatively. The visible flame extinction was
followed by rapid vaporization, a plateau when the droplet became quite small, and the formation of
a visible vapor cloud late in the recording history. The post-visible-flame-extinction behavior was
consistent with cool flame burning and extinction.


NASA/TP-2015-216046 200




Figure 177.-Test FLEX-174. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. This was a very small heptane droplet. It drifted south in the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV) after deployment and ignition, but it remained in the
FOV for the entire recording time. The droplet burned with a relatively bright flame to a very small
size, at which point there was a small disruption that was coincident with visible flame extinction.


NASA/TP-2015-216046 201




Figure 178.-Test FLEX-175. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted east, but it remained in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) for the entire test. The droplet burned linearly to a small
size, and it disrupted when the flame extinguished. The droplet size at extinction was an
extrapolation of the average burning rate to the time of extinction.


NASA/TP-2015-216046 202




Figure 179.-Test FLEX-176. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted slowly northeast in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) after deployment and ignition and out of the FOV a little
over halfway through the test. The droplet burned to a small size and then disrupted. An
extrapolation of the droplet history to the time when the flame extinguished showed that the droplet
had almost completely vaporized when it disrupted and ended the test. The color camera Image
Processing and Storage Unit (IPSU) did not record any images after deployment.


NASA/TP-2015-216046 203




Figure 180.-Test FLEX-177. Free-floating methanol droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,
0.7-atm ambient environment. There was almost no drift, and the droplet remained in High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) for the entire test. The HiBMs recording stopped before the
burn was complete, and the droplet drifted out of the Low Light Level Ultra-Violet (LLUV) FOV before
the end of the test. The color camera Image Processing and Storage Unit (IPSU) did not record any
images after deployment.


NASA/TP-2015-216046 204




Figure 181.-Test FLEX-178. Free-floating methanol droplet burning in a 0.24/0.56/0.20 O2/N2/CO2,
0.70-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
and Low Light Level Ultra-Violet (LLUV) fields of view (FOVs) during the entire test. The color
camera Image Processing and Storage Unit (IPSU) did not record any images after deployment, and
the flame extinguished diffusively with no disruption.


NASA/TP-2015-216046 205




Figure 182.-Test FLEX-179. Free-floating heptane droplet burning in a 0.23/0.52/0.25 O2/N2/CO2,
0.7-atm ambient environment. The droplet drifted slowly east in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV), but it remained in the HiBMs FOV for the entire recording time
(including after extinction). There was some rapid postextinction vaporization, but it was not as
pronounced as in other heptane tests. This was followed by a plateau in the droplet history. The
flame extinguished radiatively, and this was probably followed by a cool flame and cool flame
extinction. The color camera Image Processing and Storage Unit (IPSU) failed to record any images
after deployment.


NASA/TP-2015-216046 206




Figure 183.-Test FLEX-180. Free-floating heptane droplet burning in a 0.23/0.52/0.25 O2/N2/CO2,
0.7-atm ambient environment. This smaller droplet remained in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) for the entire test. The droplet disrupted when the droplet was very
small-coincident with visible flame extinction. The droplet size at extinction is the size of the droplet
just before the disruption.


NASA/TP-2015-216046 207




Figure 184.-Test FLEX-181. Free-floating heptane droplet burning in a 0.19/0.71/0.10 O2/N2/CO2,
0.7-atm ambient environment. The droplet remained in High-Bit-Depth Multispectral (HiBMs) field of
view (FOV) for the entire test, including a long period after the visible flame extinguished. The flame
extinguished radiatively when the droplet was relatively large. After the visible flame extinguished,
the droplet vaporized rapidly and almost constantly. Then a vapor cloud formed, and there was a
plateau in the droplet history. The post-visible-flame vaporization and plateau indicate cool flame
burning and extinction, respectively. The color camera Image Processing and Storage Unit (IPSU)
did not record any video after deployment.


NASA/TP-2015-216046 208




Figure 185.-Test FLEX-182. Free-floating heptane droplet burning in a 0.19/0.71/0.10 O2/N2/CO2,
0.7-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) for the entire test, including after the visible flame extinguished. The flame
extinguished radiatively, followed by rapid vaporization and then a plateau late in the test time.
The plateau was coincident with the formation of a vapor cloud. The post-visible-flame-extinction
behavior and the plateau in the droplet history indicate cool flame burning and extinction,
respectively.


NASA/TP-2015-216046 209




Figure 186.-Test FLEX-183. Free-floating heptane droplet burning in a 0.19/0.71/0.10 O2/N2/CO2,
0.7-atm ambient environment. This small droplet remained in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) for the entire test. The droplet burned to a very small size where it
disrupted before the droplet vanished. The extinction droplet diameter is the size of the droplet just
prior to the disruption.


NASA/TP-2015-216046 210




Figure 187.-Test FLEX-184. Free-floating methanol droplet burning in a 0.23/0.52/0.25 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted south and out of the High-Bit-Depth Multispectral
(HiBMs) and color camera fields of view (FOVs) relatively quickly after ignition. It remained in the
Low Light Level Ultra-Violet (LLUV) FOV for the entire test. The droplet burned for a long time before
the flame extinguished diffusively.


NASA/TP-2015-216046 211




Figure 188.-Test FLEX-185. Free-floating methanol droplet burning in a 0.70/0.52/0.25 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted south after deployment, hit the igniter, and then
drifted east slowly. It left fields of view (FOVs) of the High-Bit-Depth Multispectral (HiBMs), Low Light
Level Ultra-Violet (LLUV), and color cameras before the flame extinguished.


NASA/TP-2015-216046 212




Figure 189.-Test FLEX-186. Free-floating methanol droplet burning in a 0.23/0.52/0.25 O2/N2/CO2,
0.70-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition, went to the end of the FOV, drifted west briefly,
and drifted back north; but it never left the FOVs of any of the cameras. The flame extinguished
diffusively.


NASA/TP-2015-216046 213




Figure 190.-Test FLEX-187. Free-floating methanol droplet burning in a 0.23/0.52/0.25 O2/N2/CO2,
0.70-atm ambient environment. The droplet deployed and ignited with almost no residual motion and
remained in the fields of view (FOVs) of all the cameras for the entire test. The flame extinguished
diffusively.


NASA/TP-2015-216046 214




Figure 191.-Test FLEX-188. Free-floating methanol droplet burning in a 0.19/0.71/0.10 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted east and then southeast and out of the High-Bit-


Depth Multispectral (HiBMs) field of view (FOV) about one-third of the way through the test. There
was no disruption at extinction. This was a very long burn, and the flame probably extinguished
diffusively. Because the droplet was in the HiBMs FOV for only a small fraction of the burn, no
extinction droplet diameter is reported.


NASA/TP-2015-216046 215




Figure 192.-Test FLEX-189. Free-floating methanol droplet burning in a 0.19/0.71/0.10 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) and left the FOV immediately after the visible flame extinguished. It remained in
the FOVs of all the cameras for the entire burn, which ended with diffusive extinction.


NASA/TP-2015-216046 216




Figure 193.-Test FLEX-190. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted east after deployment and ignition, and it drifted


out of the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) before the flame extinguished. It
then drifted briefly back in the HiBMs FOV immediately after the flame extinguished. The color
camera Image Processing and Storage Unit (IPSU) did not record any images after deployment. The
droplet drifted partially out of the Low Light Level Ultra-Violet (LLUV) FOV for a portion of the burn
(resulting in more scatter in the flame size measurement). The extinction droplet diameter was
estimated by interpolating the droplet history with a cubic polynomial from the known and measured
droplet size and burning rate in the segments of the droplet history just before the droplet left the
HiBMs FOV and after it reentered the FOV.


NASA/TP-2015-216046 217




Figure 194.-Test FLEX-191. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. The droplet deployed and ignited with very little residual motion, but it


started to drift south in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) a few seconds
after the igniters were withdrawn. The droplet remained in the FOVs of the Low Light Level Ultra-
Violet (LLUV) and color camera for the entire burn. The average burning rate constant was used to
extrapolate the droplet size at extinction from the droplet history from the time that the droplet left the
HiBMs FOV until the flame extinguished as determined by the LLUV and color camera.


NASA/TP-2015-216046 218




Figure 195.-Test FLEX-192. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/CO2,


1.0-atm ambient environment. This smaller droplet drifted to the lower igniter after deployment. The


igniter seemed to stop the drift, and the droplet remained near the center of the field of view (FOV)
for the duration of the entire test. The droplet burned to diffusive extinction.


NASA/TP-2015-216046 219




Figure 196.-Test FLEX-193. Free-floating methanol droplet burning in a 0.17/0.63/0.20 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted east and out of the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV) after deployment and ignition. The droplet also drifted out of the Low
Light Level Ultra-Violet (LLUV) FOV before the flame extinguished. The color camera Image
Processing and Storage Unit (IPSU) did not record any images after deployment. The downlink
video shows that the flame extinguished diffusively without disruption.


NASA/TP-2015-216046 220




Figure 197.-Test FLEX-194. Free-floating methanol droplet burning in a 0.17/0.63/0.20 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition, remained in the FOV, briefly drifted north, and then
drifted east and out of the HiBMs FOV just before the visible flame extinguished diffusively. The
measured burning rate constant from the later part of the burn was used to extrapolate the extinction
droplet diameter from the droplet history until the flame extinguished (from the Low Light Level Ultra-
Violet (LLUV)). The color camera Image Processing and Storage Unit (IPSU) did not record any
images after deployment.


NASA/TP-2015-216046 221




Figure 198.-Test FLEX-195. Free-floating heptane droplet burning in a 0.17/0.63/0.20 O2/N2/CO2,


1.0-atm ambient environment. The droplet had almost no drift in the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV), and it remained in the FOVs of all cameras for the entire recording time.
The flame extinguished radiatively and quickly after ignition. The vaporization rate increased after
the visible flame extinguished and then quickly plateaued well after the visible flame extinguished.
This is indicative of cool flame burning and extinction. The HiBMs view became extremely dark when
a vapor cloud formed.


NASA/TP-2015-216046 222




Figure 199.-Test FLEX-196. Free-floating heptane droplet in a 0.20/0.75/0.05 O2/N2/CO2, 1.0-atm
ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) with very little residual motion for the entire test. The flame extinguished radiatively and
quickly, followed by rapid vaporization and the formation of a large vapor cloud. This indicates that
cool flame burning and extinction were likely after the visible flame extinguished. The HiBMs FOV
view dimmed when the cloud formed, and this probably caused the droplet to be recorded as being
slightly larger at the end of the test (the changing background combined with the fixed segmentation
value caused more pixels to be counted as "droplet").


NASA/TP-2015-216046 223




Figure 200.-Test FLEX-197. Free-floating heptane droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted east out of the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV) just before the flame extinguished radiatively. A large vapor cloud
formed 15 to 20 s after the visible flame extinguished (visible in the color camera), indicating that
cool flame burning and extinction were likely after the visible flame extinguished. The measured
burning rate constant (later in the droplet lifetime) was used to extrapolate the extinction droplet
diameter from the droplet history, and the Low Light Level Ultra-Violet (LLUV) was used to
determine the time of extinction.


NASA/TP-2015-216046 224




Figure 201.-Test FLEX-198. Free-floating heptane droplet in a 0.20/0.75/0.05 O2/N2/CO2, 1.0-atm
ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) and Low
Light Level Ultra-Violet (LLUV) fields of view (FOVs) for the entire recording time. The color camera
Image Processing and Storage Unit (IPSU) did not record any images after deployment. The flame
extinguished radiatively, and there appeared to be rapid vaporization followed by a plateau late in
the recording time after the visible flame extinguished. This is indicative of a cool flame burning and
extinction after visible flame extinction.


NASA/TP-2015-216046 225




Figure 202.-Test FLEX-199. Free-floating heptane droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted north after deployment and ignition and out of
High-Bit-Depth Multispectral (HiBMs) field of view (FOV). The droplet left the HiBMs FOV before the
flame extinguished disruptively when the droplet was very small. The measured burning rate
constant was used to extrapolate the extinction droplet diameter from the droplet history until
disruption occurred.


NASA/TP-2015-216046 226




Figure 203.-Test FLEX-200. Free-floating methanol droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted east and out of the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV). After drifting out of the HiBMs FOV, the droplet drifted back in slightly
then out again for the rest of the test. The flame extinguished diffusively after a long burn. Because
the droplet was in the HiBMs FOV for only a small fraction of the total test, no extinction diameter is
reported. The color camera Image Processing and Storage Unit (IPSU) did not record any images
after deployment.


NASA/TP-2015-216046 227




Figure 204.-Test FLEX-201. Free-floating methanol droplet burning in a 0.20/0.75/0.05 O2/N2/CO2,


1.0-atm ambient environment. The droplet drifted north in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition. It left the HiBMs FOV approximately two-thirds of
the way through the burn, which ended with diffusive extinction. The average burning rate constant
from the last half of the time that the droplet was in the HiBMs FOV was used to extrapolate the
extinction droplet diameter from the droplet history until the time of extinction. The color camera
Image Processing and Storage Unit (IPSU) did not record any images after deployment.


NASA/TP-2015-216046 228




Figure 205.-Test FLEX-202. Free-floating methanol droplet in a 0.20/0.75/0.05 O2/N2/CO2, 1.0-atm
ambient environment. The droplet had very little residual motion after deployment and ignition, drifting
very slowly south in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). The droplet
remained in the FOVs of all the cameras for the entire test.


NASA/TP-2015-216046 229




Figure 206.-Test FLEX-203. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet remained in the fields of view (FOVs) of all cameras, and


the flame extinguished diffusively.


NASA/TP-2015-216046 230




Figure 207.-Test FLEX-204. Free-floating methanol droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet remained in the fields of view (FOVs) of all cameras for the


entire burn, but it drifted south and out of the High-Bit-Depth Multispectral (HiBMs) FOV shortly after
the flame extinguished diffusively. Image Processing and Storage Unit (IPSU) did not record every
frame.


NASA/TP-2015-216046 231




Figure 208.-Test FLEX-206. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet drifted southeast in the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV) after deployment; then it hit the igniter and changed direction to the
northwest with a relatively high speed. It drifted northwest and out of the HiBMs FOV after a very
short time. The droplet also drifted out of the color camera FOV, but it remained in the Low Light
Level Ultra-Violet (LLUV) FOV.


NASA/TP-2015-216046 232




Figure 209.-Test FLEX-207. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet drifted southeast in the High-Bit-Depth Multispectral


(HiBMs) field of view (FOV) after deployment; then it hit the igniter and began to drift north. The drift
velocity was relatively high, and the droplet drifted out of the HiBMs FOV relatively quickly after
ignition. It also drifted out of the Low Light Level Ultra-Violet (LLUV) and color camera FOVs before
the end of the test. The flame oscillated briefly in the middle of the burn and then became steady and
burned to a disruptive extinction. The flame was very dim in the color camera FOV, with the leading
edge of the flame (in the direction of the droplet drift) much brighter than the trailing edge.


NASA/TP-2015-216046 233




Figure 210.-Test FLEX-208. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet drifted southeast after deployment, drifted into the igniter,


and changed direction to the north after the igniter was withdrawn. The droplet drifted north during the
burn and out of the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). The flame grew,
remained stable (no oscillations), and then shrank to a disruptive extinction at a relatively small size.
The droplet remained in the Low Light Level Ultra-Violet (LLUV) FOV for the entire test, but the Multi-
User Droplet Combustion Apparatus (MDCA) color camera did not record images onboard for this
test (the downlinked video is available).


NASA/TP-2015-216046 234




Figure 211.-Test FLEX-209. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet drifted southeast after deployment, did not touch the


igniter, and continued to drift southeast in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) and out of the FOV. The droplet also drifted south and out of the Low Light Level Ultra-Violet
(LLUV) FOV. The color camera Image Processing and Storage Unit (IPSU) did not record color
camera data. It is not clear whether disruption occurred.


NASA/TP-2015-216046 235




Figure 212.-Test FLEX-210. Fiber-supported heptane droplet in a cabin air (0.21/0.79 O2/N2), 1.0-atm
ambient environment. The droplet drifted east some on the fiber after ignition and early in the droplet
lifetime. The soot agglomerates that were near the droplet created a lot of noise in the droplet
measurement for the first half of the burn. The droplet also moved significantly on the fiber late in the
droplet lifetime. There was evidence of some unusual soot dynamics-large soot particles moving
slowly toward the droplet and then being more rapidly pushed away (presumably by the Stefan flow).
The droplet burned to completion.


NASA/TP-2015-216046 236




Figure 213.-Test FLEX-211. Free-floating heptane droplet burning in a 0.16/0.84 O2/N2, 1.0-atm
ambient environment. The droplet was nearly motionless after deployment and ignition and remained
in the fields of view (FOVs) of all the cameras throughout the entire recording time of the Image
Processing and Storage Units (IPSUs). The visible flame grew then extinguished radiatively. This was
followed by rapid vaporization. The vaporization rate of the droplet actually increased after the visible
flame extinguished and then rapidly decreased when a vapor cloud formed. This behavior is indicative
of cool flame burning and extinction.


NASA/TP-2015-216046 237




1. 214.-Test FLEX-212. Free-floating heptane droplet burning in a 0.16/0.84 O2/N2, 1.0-atm


ambient environment. The droplet drifted north in the color camera field of view (FOV). The High-
Bit-Depth Multispectral (HiBMs) Image Processing and Storage Unit (IPSU) did not record any
images for this test, but the droplet remained in the FOVs of the Low Light Level Ultra-Violet
(LLUV) and color camera. The flame burned for a short time to radiative extinction. This was
probably followed by cool flame burning and extinction. The color camera showed that a large
vapor cloud formed sometime after the visible flame extinguished.


NASA/TP-2015-216046 238




Figure 215.-Test FLEX-214. Free-floating heptane droplet burning in a 0.16/0.84 O2/N2, 1.0-atm
ambient environment. The droplet remained in the fields of view (FOVs) of all cameras for the entire
recording time of the Image Processing and Storage Units (IPSUs). The flame grew and extinguished
radiatively shortly after ignition. A period of rapid post visible flame extinction vaporization was followed
by a plateau in the droplet history coincident with the appearance of a vapor cloud. Both indicate cool
flame burning and extinction following visible flame extinction.


NASA/TP-2015-216046 239




Figure 216.-Test FLEX-215. Free-floating heptane droplet burning in a 0.15/0.85 O2/N2, 1.0-atm
ambient environment. The droplet had very little residual motion after deployment and ignition with only
a very small drift north in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). The droplet
remained in the FOVs of all cameras throughout the recording time of the Image Processing and
Storage Units (IPSUs). After ignition, the flame grew but became dimmer, and it extinguished
radiatively shortly after ignition. This was followed by a period of rapid vaporization and a quick plateau
in the droplet history coincident with the formation of a vapor cloud. Both of these are evidence of cool
flame burning and extinction after visible flame extinction.


NASA/TP-2015-216046 240




Figure 217.-Test FLEX-216. Free-floating heptane droplet burning in a 0.15/0.84 O2/N2, 1.0-atm
ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras throughout
the entire burn and during the recording time of the Image Processing and Storage Unit (IPSUs).
Either the droplet burned to completion or the flame extinguished when the droplet was very small.
There was no disruption when the flame extinguished.


NASA/TP-2015-216046 241




Figure 218.-Test FLEX-217. Free-floating heptane droplet burning in a 0.14/0.86 O2/N2, 1.0-atm
ambient environment. The droplet remained in the fields of view (FOVs) of all cameras for the entire
recording time of all the Image Processing and Storage Units (IPSUs). The droplet did drift east to the
edge of the High-Bit-Depth Multispectral (HiBMs) FOV and then south to the corner of the HiBMs FOV,
but it never left the HiBMs FOV. The flame had a very quick radiative extinction. The vaporization rate
did not change after extinction, and a small vapor cloud formed, indicating that there may have been a
cool flame, although the extinction of the cool flame was not pronounced.


NASA/TP-2015-216046 242




Figure 219.-Test FLEX-218. Free-floating heptane droplet burning in a 0.14/0.86 O2/N2, 1.0-atm
ambient environment. This small droplet drifted quickly northwest in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after deployment and ignition. It drifted out of the FOV a short time after
the igniter was withdrawn. The droplet appeared to extinguish radiatively, even at this relatively small
size. Because the droplet was in the HiBMs FOV for only a small fraction of the entire test, no
extinction droplet diameter is reported. The color camera Image Processing and Storage Unit (IPSU)
did not record any images after deployment.


NASA/TP-2015-216046 243




Figure 220.-Test FLEX-219. Free-floating methanol droplet burning in a 0.14/0.86 O2/N2, 1.0-atm
ambient environment. The droplet drifted north and out of High-Bit-Depth Multispectral (HiBMs) field
of view (FOV) about one-fourth of the way through a very long burn that appeared to end in a
diffusive extinction. The droplet drifted east and partially out of the Low Light Level Ultra-Violet
(LLUV) FOV, but it remained in the color camera FOV. This was a very weak flame, barely visible on
both the LLUV and color cameras. Because the droplet was only in the HiBMs FOV for a small
fraction of the flame lifetime, no extinction droplet diameter is reported.


NASA/TP-2015-216046 244




Figure 221.-Test FLEX-220. Free-floating methanol droplet in a 0.14/0.86 O2/N2, 1.0-atm ambient
environment. The droplet drifted north after deployment and ignition and then out of High-Bit-Depth
Multispectral (HiBMs) field of view (FOV). Just after the visible flame extinguished, the droplet drifted
back into the HiBMs FOV. This was a weak flame with a long burn to diffusive extinction. The
extinction droplet diameter was derived from a spline fit between the periods of time when the droplet
was in the HiBMs FOV.


NASA/TP-2015-216046 245




Figure 222.-Test FLEX-221. Free-floating methanol droplet burning in a 0.13/0.87 O2/N2, 1.0-atm
ambient environment. The droplet drifted east; then just after the visible flame extinguished, it drifted
south and out of the southeast corner of the High-Bit-Depth Multispectral (HiBMs) field of view (FOV).
The flame oscillated for several seconds before it extinguished radiatively. The flame oscillations are
very difficult to discern in the Low Light Level Ultra-Violet (LLUV) view because the flame luminosity
barely registered on the LLUV. The color camera Image Processing and Storage Unit (IPSU) did not
record any images for this test.


NASA/TP-2015-216046 246




Figure 223.-Test FLEX-222. Free-floating methanol droplet burning in a 0.13/0.87 O2/N2, 1.0-atm
ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) for most of the test. For a short period near visible flame extinction, the droplet drifted partially
out of the FOV. It drifted back into the HiBMs FOV for the remainder of the HiBMs Image Processing
and Storage Unit (IPSU) recording time. The flame was very dim, barely above the background level,
in both the Low Light Level Ultra-Violet (LLUV) and color cameras. The extinction droplet diameter
was interpolated from the droplet history from when the droplet left the HiBMs FOV to when it
reentered a short time after the visible flame extinguished. The interpolation polynomial is a fourth-
order polynomial with the constraint that the values and burning rate constants at both ends match
the experimental values.


NASA/TP-2015-216046 247




Figure 224.-Test FLEX-223. Free-floating methanol droplet burning in a 0.12/0.88 O2/N2, 1.0-atm
ambient environment. The droplet deployed and ignited with almost no residual motion. The droplet
drifted a little south and then east in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV), but it
remained in the FOVs of the HiBMs, Low Light Level Ultra-Violet (LLUV), and color cameras for the
entire recording time.


NASA/TP-2015-216046 248




Figure 225.-Test FLEX-224. Free-floating methanol droplet burning in a 0.12/0.88 O2/N2, 1.0-atm
ambient environment. The droplet drifted north after deployment and ignition and out of the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV) about three-fourths of the way through the burn. The
flame grew and then shrank in response to the shrinking droplet. The flame was very dim and difficult
to see in the Low Light Level Ultra-Violet (LLUV). The flame probably extinguished diffusively. The
measured burning rate constant while the droplet was in the FOV was used to extrapolate the
extinction droplet diameter from the droplet history to flame extinction.


NASA/TP-2015-216046 249




Figure 226.-Test FLEX-225. Free-floating methanol droplet burning in a 0.12/0.88 O2/N2, 1.0-atm
ambient environment. The droplet was nearly motionless after deployment and ignition. Then it started
to drift slowly east, but it changed direction and quickly drifted west in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV). The droplet left the HiBMs FOV about three-fourths of the way through the
burn. The flame was very dim, but it did appear to grow, reach a maximum, and then decrease in size in
response to the shrinking droplet. The burning rate constant measured from the last part of the droplet
history while the droplet was still in the HiBMs FOV was used to extrapolate the extinction droplet
diameter from the droplet history to when the flame extinguished (as measured by the Low Light Level
Ultra-Violet (LLUV)). The flame probably extinguished diffusively with a significant contribution from
radiative loss. The color camera Image Processing and Storage Unit (IPSU) did not record any images
after deployment.


NASA/TP-2015-216046 250




Figure 227.-Test FLEX-226. Free-floating methanol droplet burning in a 0.20/0.75/0.05 O2/N2/He, 1.0-atm
ambient environment. The droplet was nearly motionless after deployment and ignition, but it began to
drift southeast in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) a few seconds after
ignition. The droplet drifted out of the HiBMs field of view (FOV), but it remained in the FOVs of the Low
Light Level Ultra-Violet (LLUV) and color cameras. The color camera Image Processing and Storage Unit
(IPSU) failed to record any images after deployment. The droplet burned for a relatively long time before
the flame extinguished diffusively. The burning rate constant from a short period just prior to the droplet
leaving the HiBMs FOV was used to extrapolate the extinction droplet diameter from the droplet history
from the time that the droplet left the HiBMs FOV until the flame extinguished.


NASA/TP-2015-216046 251




Figure 228.-Test FLEX-227. Free-floating methanol droplet in a 0.20/0.75.0.05 O2/N2/He, 1.0-atm
ambient environment. The High-Bit-Depth Multispectral (HiBMs) Image Processing and Storage
Unit (IPSU) failed to start, so no droplet data were recorded. The flame was bright and burned for
over 5 s until it (presumably) extinguished diffusively.


NASA/TP-2015-216046 252




Figure 229.-Test FLEX-229. Free-floating heptane droplet burning in a 0.20/0.75.0.05 O2/N2/He, 1.0-
atm ambient environment. The droplet drifted southeast after deployment in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV), hit the igniter, and developed a large drift velocity to the
east. The droplet drifted out of the FOV of the HiBMs and then out of the FOVs of the Low Light Level
Ultra-Violet (LLUV) and color cameras before the flame either extinguished or burned out.


NASA/TP-2015-216046 253




Figure 230.-Test FLEX-230. Free-floating heptane droplet burning in a 0.20/0375/0.05 O2/N2/He, 1.0-atm
ambient environment. The droplet drifted southwest after deployment then hit the igniter and moved
southwest in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). It left the HiBMs FOV about
halfway through the burn. Because of soot, the droplet burned very brightly with a lot of luminosity. The
soot diminished, and the flame burned with a dim blue flame that got brighter near the end of the burn.
The droplet burned to a very small size and disrupted coincident with flame extinction.


NASA/TP-2015-216046 254




Figure 231.-Test FLEX-231. Free-floating methanol droplet burning in a 0.19/0.71/0.10 O2/N2/He,


1.0-atm ambient environment. The droplet had a pronounced drift south in the High-Bit-Depth


Multispectral (HiBMs) field of view (FOV) after deployment; then it struck the igniter and continued
to drift south and out of the HiBMs FOV about one-third of the way through the burn. The droplet
burned for a relatively long time before the flame extinguished diffusively. The color camera Image
Processing and Storage Unit (IPSU) did not record any images after deployment for this test. Also,
because the droplet was in the HiBMs FOV for only a short fraction of the total test, no extinction
droplet diameter is reported for this test.


NASA/TP-2015-216046 255




Figure 232.-Test FLEX-232. Free-floating methanol droplet burning in a 0.18/0.67/0.15 O2/N2/He,


1.0-atm ambient environment. The droplet slowly drifted south after deployment and ignition in the


High-Bit-Depth Multispectral (HiBMs) field of view (FOV), but it never left the FOV. The flame
extinguished diffusively with no disruption.


NASA/TP-2015-216046 256




Figure 233.-Test FLEX-233. Fiber-supported methanol droplet burning in a 0.18/0.67/0.15
O2/N2/He, 1.0-atm ambient environment. After ignition, the droplet moved slowly and smoothly west
on the fiber in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). The droplet drifted to
the edge of the HiBMs FOV, but it remained in the FOV. There was some small oscillatory motion
on the fiber, but the burn was relatively clean until the flame extinguished diffusively.


NASA/TP-2015-216046 257




Figure 234.-Test FLEX-234. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet drifted southeast and out of the High-Bit-Depth


Multispectral (HiBMs) field of view (FOV) about halfway through the burn. The flame began to
oscillate and then drifted south and out of the Low Light Level Ultra-Violet (LLUV) FOV before the
flame extinguished. The color camera Image Processing and Storage Unit (IPSU) did not record
any images during the burn. It is not clear whether the droplet continued to burn in the LLUV FOV
or for how long it burned if it continued to burn. The oscillations were significant, but the flame
appeared to decrease in size. From the radiometer, it appears that the droplet burned with a stable
flame after the flame oscillations stopped.


NASA/TP-2015-216046 258




Figure 235.-Test FLEX-235. Free-floating heptane droplet burning in a cabin air (0.21/0.79 O2/N2),


1.0-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) for most of its lifetime. The droplet burned to a very small size, with a small
disruption coincident with visible flame extinction.


NASA/TP-2015-216046 259




Figure 236.-Test FLEX-236. Fiber-supported heptane droplet burning in a cabin air (0.21/0.79
O2/N2), 1.0-atm ambient environment. The droplet oscillated on the fiber throughout the burn, but it
remained in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). Large soot agglomerates
interfered with the measurement of droplet size for a portion of the burn. The flame extinguished
radiatively after a very long, slow, high-amplitude oscillation. This was followed by rapid
vaporization and the formation of a vapor cloud coincident with the plateau. The droplet moved
during the vaporization, but this did not seem to impact the size measurement significantly. There
was a small disruption near the end of the vaporization and a small jump in droplet size-maybe a
gas bubble that burst. A cool flame and cool flame extinction probably followed the visible flame
extinction.


NASA/TP-2015-216046 260




Figure 237.-Test FLEX-237. Free-floating heptane droplet burning in a 0.19/0.71/0.10 O2/N2/He,


1.0-atm ambient environment. The droplet drifted north in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition and just out of the FOV before the flame
extinguished and disrupted. There may have been a disruption coincident with when the flame
extinguished.


NASA/TP-2015-216046 261




Figure 238.-Test FLEX-238. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/He,


1.0-atm ambient environment. The droplet was almost motionless after deployment and ignition.


This was a large droplet, and it remained in High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) for the entire test. After ignition, the flame grew but became increasingly dimmer, and it
quickly extinguished because of radiative loss. After the visible flame extinguished, the droplet
continued to vaporize at almost the same rate well after the flame extinguished when a plateau
occurred coincident with the formation of a large vapor cloud. Both phenomena indicate cool flame
burning and extinction after visible flame extinction. The color camera Image Processing and
Storage Unit (IPSU) did not record any images after deployment.


NASA/TP-2015-216046 262




Figure 239.-Test FLEX-239. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/He,


1.0-atm ambient environment. The droplet drifted north after deployment and ignition and out of the


High-Bit-Depth Multispectral (HiBMs) field of view (FOV) one-third of the way through the burn. The
flame remained in the FOV of both the Low Light Level Ultra-Violet (LLUV) and color camera for the
duration of the burn. Initially, soot oxidation caused the flame to be bright and very luminous, but
quickly the flame became a dimmer blue. The luminosity increased slightly as the flame
approached extinction. Because the droplet was out of the HiBMs FOV for the majority of the test,
no extinction diameter is reported.


NASA/TP-2015-216046 263




Figure 240-Test FLEX-240. Free-floating heptane droplet burning in a 0.18/0.67/0.15 O2/N2/He,


1.0-atm ambient environment. The droplet drifted north after deployment and ignition and out of the


High-Bit-Depth Multispectral (HiBMs) field of view (FOV) about one-fourth of the way through the
burn. The drift velocity was relatively high, and the flame was brighter on the leading edge in the
direction of the drift. The droplet did remain in the FOVs of the Low Light Level Ultra-Violet (LLUV)
and color camera. Because the droplet was in the HiBMs FOV for only a small fraction of the burn,
no extinction diameter is reported for this test. The color camera Image Processing and Storage
Unit (IPSU) did not record any images after deployment for this test.


NASA/TP-2015-216046 264




Figure 241.-Test FLEX-241. Free-floating heptane droplet burning in a 0.17/0.63/0.20 O2/N2/He,


1.0-atm ambient environment. The droplet had almost no drift after deployment and ignition, and it


remained in the High-Bit-Depth Multispectral (HiBMs), Low Light Level Ultra-Violet (LLUV), and color
camera fields of view (FOVs) with little motion throughout the Image Processing and Storage Unit
(IPSU) recording time. The flame extinguished radiatively, and there was a brief period after the
visible flame extinguished in which the droplet continued to vaporize at a nearly constant rate,
indicating that there was a cool flame after the visible flame extinguished. The color camera IPSU
did not record any images after deployment.


NASA/TP-2015-216046 265




Figure 242.-Test FLEX-242. Free-floating heptane droplet burning in a 0.17/0.63/0.20 O2/N2/He,


1.0-atm ambient environment. The droplet had almost no drift after deployment and ignition, moving


slightly to the southeast in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) but
remaining in the FOV of all the cameras for the entire test. The color camera Image Processing and
Storage Unit (IPSU) failed to record any images after deployment. The flame extinguished after
approximately 5 s, and extinction was probably followed by cool flame burning and extinction.


NASA/TP-2015-216046 266




Figure 243.-Test FLEX-243. Fiber-supported heptane droplet burning in a 0.17/0.63 O2/N2,


1.0-atm ambient environment. Neither the High-Bit-Depth Multispectral (HiBMs) or color


camera Image Processing and Storage Units (IPSUs) recorded any images for this test. The
droplet burned for a short time to disruption.


NASA/TP-2015-216046 267




Figure 244.-Test FLEX-244. Fiber-supported heptane droplet burning in a 0.17/0.63/0.20 O2/N2/He,


1.0-atm ambient environment. This was a smaller droplet. After ignition, there was a lot of motion on


the fiber. It was not really disruptive burning, in which the droplet becomes dislodged from the fiber, but
the motion clearly influenced the burning history. The droplet burned to completion, and the color
camera did not record to the onboard Image Processing and Storage Unit (IPSU) for this test.


NASA/TP-2015-216046 268




Figure 245.-Test FLEX-245. Free-floating methanol droplet in a 0.17/0.63/0.20 O2/N2/He, 1.0-atm
ambient environment. The droplet had a strong north to northeast drift after deployment, nearly hitting
the igniter before it withdrew. The droplet had a relatively high drift velocity after ignition and only
remained in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for one-fourth of the burn.
Because the droplet was in the FOV for only a short time, no extinction diameter is reported. The flame
extinguished diffusively.


NASA/TP-2015-216046 269




Figure 246.-Test FLEX-246. Free-floating methanol droplet burning in a 0.17/0.63/0.20 O2/N2/He,


1.0-atm ambient environment. The droplet had almost no drift after deployment and ignition, but


shortly into the burn it developed a slow drift northeast then east in the color camera field of view
(FOV). The droplet left the High-Bit-Depth Multispectral (HiBMs) FOV near diffusive flame extinction.
The measured burning rate constant while the droplet was in the HiBMs FOV was used to
extrapolate the extinction droplet diameter from the droplet history from the time that the droplet left
the HiBMs FOV until the flame extinguished. The diameter should be reasonably accurate because
the flame extinguished only a short time after it left the HiBMs FOV.


NASA/TP-2015-216046 270




Figure 247.-Test FLEX-247. Free-floating methanol droplet burning in a 0.16/0.59/0.25 O2/N2/He,


1.0-atm ambient environment. The droplet was nearly motionless after deployment and ignition, and


it remained in the fields of view (FOVs) of all the cameras for the entire recording time. It is difficult to
say whether the flame extinguished diffusively or radiatively. It was probably near the flammability
boundary. The color camera Image Processing and Storage Unit (IPSU) failed to record any images
after deployment.


NASA/TP-2015-216046 271




Figure 248.-Test FLEX-248. Free-floating methanol droplet burning in a 0.16/0.59/0.25 O2/N2/He,


1.0-atm ambient environment. The High-Bit-Depth Multispectral (HiBMs) Image Processing and
Storage Unit (IPSU) did not record any images for this test. There was only a very small drift south
in color camera field of view (FOV), but the droplet remained in the FOV for the entire test (as well
as the Low Light Level Ultra-Violet (LLUV) FOV). The droplet burned to extinction.


NASA/TP-2015-216046 272




Figure 249.-Test FLEX-249. Free-floating heptane droplet burning in a 0.16/0.59/0.25 O2/N2/He, 1.0-
atm ambient environment. This smaller droplet was nearly motionless after deployment and ignition,
and it remained in the fields of view (FOVs) of all the cameras. The flame surrounding the droplet
extinguished at a very small size, near the limit of what we can reasonably measure. The flame size
was nearly constant throughout the burn, decreasing only slightly toward the end of the burn after
increasing only slightly in size initially. The flame standoff increased linearly throughout the burn.


NASA/TP-2015-216046 273




Figure 250.-Test FLEX-250. Fiber-supported methanol droplet burning in a 0.15/0.55/0.30 O2/N2/He,


1.0-atm ambient environment. There was a small amount of axial motion on the fiber, but it did not


seem to influence the burning behavior to a large degree. This was a relatively short, transient burn,
and the flame probably extinguished radiatively.


NASA/TP-2015-216046 274




Figure 251.-Test FLEX-251. Free-floating methanol droplet burning in a 0.15/0.55/0.30 O2/N2/He,


1.0-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition. It remained in the FOV for the duration of the burn,
leaving shortly after the visible flame extinguished. This ambient environment was probably near the
flammability boundary, so it is difficult to determine whether the flame extinguished diffusively or
radiatively.


NASA/TP-2015-216046 275




Figure 252.-Test FLEX-252. Free-floating methanol droplet burning in a 0.14/0.51/0.35 O2/N2/He,


1.0-atm ambient environment. After deployment and ignition, the droplet had a slow southeast drift in


the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). It left the HiBMs FOV well after the
visible flame extinguished, but it drifted back into the HiBMs FOV before the end of the recording
period. The droplet burned for a short time before the flame extinguished.


NASA/TP-2015-216046 276




Figure 253.-Test FLEX-253. Free-floating methanol droplet burning in a 0.14/0.51/0.35 O2/N2/He,


1.0-atm ambient environment. The droplet was nearly motionless after deployment and ignition in
the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). It started to drift south as it burned, and
it left the FOV well after the visible flame extinguished. The droplet burned for only a very short time,
and the flame was very dim, almost undetectable in both the Low Light Level Ultra-Violet (LLUV) and
color camera. The droplet was very near or even below the flammability limit.


NASA/TP-2015-216046 277




Figure 254.-Test FLEX-254. Free-floating methanol droplet burning in a 0.13/0.47/0.40 O2/N2/He,


1.0-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)


field of view (FOV) for the entire recording period. It had a very short burn to extinction. This was
probably below the flammability limit.


NASA/TP-2015-216046 278




Figure 255.-Test FLEX-255. Free-floating heptane droplet burning in a 0.24/0.56/0.20 O2/N2/He,
0.70-atm ambient environment. The droplet drifted out of the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) close to extinction, but it remained in the FOV of the Low Light Level Ultra-Violet
(LLUV) and color camera FOVs. A small vapor cloud formed at extinction. There was noise in the
analysis of the droplet image because soot particles that formed during combustion interfered with
the analysis. It is not clear whether the visible extinction was radiative or diffusive or if there was a
cool flame after the visible flame extinguished.


NASA/TP-2015-216046 279




Figure 256.-Test FLEX-256. Free-floating heptane droplet burning in a 0.23/0.52/0.25 O2/N2/He,
0.70-atm ambient environment. The droplet drifted east after deployment and ignition in the High-Bit-
Depth Multispectral (HiBMs) field of view (FOV), leaving the FOV just prior to extinction or burnout.
The droplet burned to a very small size and then appeared to disrupt or rapidly change direction
after the droplet left the HiBMs FOV. The measured burning rate constant was used to extrapolate
the extinction droplet diameter from the droplet history from the time that the droplet left the FOV
until the flame extinguished. The small droplet size at extinction suggests that the droplet burned
almost to completion.


NASA/TP-2015-216046 280




Figure 257.-Test FLEX-257. Free-floating methanol droplet burning in a 0.24/0.56/0.20 O2/N2/He,
0.70-atm ambient environment. The droplet drifted southeast in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after deployment and ignition. It stopped briefly at the corner of the FOV
and then disappeared from the FOV (there one frame, gone the next) at a time coincident with
visible flame extinction. The droplet may have moved to just outside of the FOV after the flame
extinguished. The droplet burned nicely to a diffusive extinction. The extinction droplet diameter is
the droplet diameter in the frame just before the droplet disappeared.


NASA/TP-2015-216046 281




Figure 258.-Test FLEX-258. Fiber-supported methanol droplet burning in a 0.24/0.56/0.20 O2/N2/He,
0.70-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV), but there was a lot of motion on the fiber. Eventually the droplet disrupted and
dislodged from the fiber. Because of the disruption, no extinction droplet diameter is reported.


NASA/TP-2015-216046 282




Figure 259.-Test FLEX-259. Free-floating methanol droplet in a 0.23/0.52/0.25 O2/N2/He, 0.70-atm
ambient environment. The droplet drifted southeast in the High-Bit-Depth Multispectral (HiBMs) field
of view (FOV) after ignition and out of the FOV near diffusive extinction. The burning rate constant
from the last part of the burn while the droplet was in the FOV was used to extrapolate the extinction
droplet diameter from the droplet history from the time that the droplet left the HiBMs FOV until the
visible flame extinguished.


NASA/TP-2015-216046 283




Figure 260.-Test FLEX-260. Fiber-supported methanol droplet burning in a 0.23/0.52/0.25 O2/N2/He,
0.70-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV), and there was very little motion on the fiber until very close to visible flame
extinction when the droplet dislodged from the fiber. Because the flame extinguished when the
droplet disrupted off of the fiber, no extinction droplet diameter is reported.


NASA/TP-2015-216046 284




Figure 261.-Test FLEX-261. Free-floating methanol droplet in a 0.21/0.49/0.30 O2/N2/He, 0.70-atm
ambient environment. The droplet drifted northwest in the High-Bit-Depth Multispectral (HiBMs) field
of view (FOV) after deployment, hit the igniter, and then drifted quickly south after ignition. Because
the droplet left the HiBMs FOV shortly after ignition, only a small portion of the droplet burning
history was captured. The droplet also left the color camera FOV. Because only a short part of the
burning history was captured, no extinction droplet diameter is reported and the burning rate
constant is probably inaccurate.


NASA/TP-2015-216046 285




Figure 262.-Test FLEX-262. Free-floating methanol droplet in a 0.21/0.49/0.30 O2/N2/He, 0.70-atm
ambient environment. The droplet drifted southeast in the High-Bit-Depth Multispectral (HiBMs) field
of view (FOV) after deployment, hit the igniter, and then began to drift slowly northwest after ignition.
The droplet left the HiBMs FOV before extinction, but most of the burning history was captured by
the HiBMs. The droplet burned for a long time before the flame extinguished diffusively. The
measured burning rate constant from just before the droplet left the HiBMs FOV was used to
extrapolate the extinction droplet diameter from the droplet size history from the time that the droplet
left the HiBMs FOV until the visible flame extinguished.


NASA/TP-2015-216046 286




Figure 263.-Test FLEX-263. Fiber-supported methanol droplet burning in a 0.21/0.49/0.30 O2/N2/He,
0.70-atm ambient environment. The droplet drifted slowly east along the fiber in the High-Bit-Depth
Multispectral (HiBMs) field of view (FOV) after deployment and ignition. There was a little disruptive
motion on the fiber during the burning history. The flame extinguished diffusively.


NASA/TP-2015-216046 287




Figure 264.-Test FLEX-264. Free-floating heptane droplet in a 0.21/.0.49/0.30 O2/N2/He, 0.7-atm
ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) for the entire test. The flame grew to a maximum size shortly after ignition, then remained at a
constant size until extinction. It is not clear whether the flame extinguished diffusively or radiatively.
There was no evidence of prolonged cool flame burning after the visible flame extinguished; there
was no rapid vaporization after extinction and no vapor cloud formed in the color camera view.


NASA/TP-2015-216046 288




Figure 265.-Test FLEX-265. Free-floating heptane droplet burning in a 0.21/0.49/0.30 O2/N2/He,
0.70-atm ambient environment. The droplet remained in the fields of view (FOVs) of all the cameras
for the entire test. The flame grew, reached a maximum size, and then decreased in size until it
extinguished diffusively at a very small size. Shortly after extinction, the droplet appeared to disrupt
and disappeared from the High-Bit-Depth Multispectral (HiBMs) FOV.


NASA/TP-2015-216046 289




Figure 266.-Test FLEX-266. Free-floating heptane droplet burning in a 0.20/0.45/0.35 O2/N2/He,
0.70-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) (and the FOVs of all cameras) for the entire test. The flame grew continuously
after ignition, extinguishing radiatively after approximately 5 s. There appears to be no cool flame or
only a very brief one-there was no significant vaporization after extinction and no vapor cloud
formed in the color camera view.


NASA/TP-2015-216046 290




Figure 267.-Test FLEX-267. Free-floating heptane droplet burning in a 0.20/0.45/0.35 O2/N2/He,
0.70-atm ambient environment. The droplet remained in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) (and the FOVs of all the cameras) for the entire test. The flame grew throughout
the test and became dimmer until it extinguished radiatively after approximately 5 s. There appeared
to be no evidence of cool flame formation-there was no rapid vaporization after the visible flame
extinguished and no vapor cloud formed in the color camera view.


NASA/TP-2015-216046 291




Figure 268.-Test FLEX-268. Free-floating methanol droplet burning in a 0.20/0.45/0.35 O2/N2/He,
0.70-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition, but it remained in the FOV for the entire test. The
flame was very dim and barely detectable in the color camera. The very long burn resulted in diffusive
extinction, although the flame standoff grew throughout the test.


NASA/TP-2015-216046 292




Figure 269.-Test FLEX-269. Free-floating methanol droplet burning in a 0.20/0.45/0.35 O2/N2/He,
0.70-atm ambient environment. The droplet was nearly motionless after deployment and ignition, and
it drifted around the High-Bit-Depth Multispectral (HiBMs) field of view (FOV). However, it remained in
the FOV for the entire burn and well after the visible flame extinguished.


NASA/TP-2015-216046 293




Figure 270.-Test FLEX-270. Free-floating methanol droplet burning in a 0.18/0.42/0.40 O2/N2/He,
0.70-atm ambient environment. The droplet drifted south in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition, leaving the FOV when the visible flame
extinguished. This was a large droplet, and it probably extinguished radiatively.


NASA/TP-2015-216046 294




Figure 271.-Test FLEX-271. Free-floating methanol droplet burning in a 0.18/0.42/0.40 O2/N2/He,
0.70-atm ambient environment. The droplet drifted north in the High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment; then it hit the igniter and drifted east and out of the FOV before
extinction. The burning rate constant measured during the later period while the droplet was in the
HiBMs FOV was used to extrapolate the extinction droplet diameter from the droplet history from the
time that the droplet left the HiBMs FOV until the visible flame extinguished.


NASA/TP-2015-216046 295




Figure 272.-Test FLEX-272. Fiber-supported methanol droplet burning in a 0.18/0.42/0.40 O2/N2/He,
0.70-atm ambient environment. There was almost no axial motion of the droplet relative to the fiber,
but the droplet oscillated radially on the fiber, causing minor disruptions in the flame and creating
some scatter in the droplet history.


NASA/TP-2015-216046 296




Figure 273.-Test FLEX-273. Free-floating heptane droplet burning in a 0.18/0.42/0.40 O2/N2/He,
0.70-atm ambient environment. The droplet drifted northeast in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after deployment and ignition, but it remained in the FOVs of all cameras
for the entire test. The droplet burned for several seconds, and the flame grew, reached a maximum
size, and remained nearly constant for the entire test. The luminosity of the flame continuously
decreased as the droplet burned. This was probably near the flammability limit. There was no
evidence of cool flame formation (no rapid vaporization or vapor cloud formation).


NASA/TP-2015-216046 297




Figure 274.-Test FLEX-274. Free-floating heptane droplet burning in a 0.18/0.42/0.40 O2/N2/He,
0.70-atm ambient environment. The droplet drifted northeast after deployment and ignition, but it
remained in the High-Bit-Depth Multispectral (HiBMs) field of view (FOV) for the entire burn and for
several seconds after the flame extinguished (long enough to observe the vaporization history). The
flame grew slightly and reached a maximum size one-third of the way through the burn. It then
decreased in size in response to the shrinking droplet. The flame probably extinguished diffusively,
but it was very close to the flammability limit. There was no evidence of a cool flame; that is, there
was no rapid vaporization after the visible flame extinguished and no vapor cloud formed.


NASA/TP-2015-216046 298




Figure 275.-Test FLEX-275. Free-floating heptane droplet burning in a 0.17/0.38/0.45 O2/N2/He,
0.70-atm ambient environment. The droplet drifted northeast in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV), but it remained in the FOV for the entire test. Well after the flame
extinguished, the droplet drifted partially out of the HiBMs FOV and then back in for the remainder of
the recording time. The flame grew continuously throughout the test, getting dimmer until the flame
extinguished. There was no evidence of a cool flame (continued vaporization or vapor cloud).


NASA/TP-2015-216046 299




Figure 276.-Test FLEX-276. Fiber-supported heptane droplet burning in a 0.17/0.38/0.45 O2/N2/He,
0.70-atm ambient environment. The droplet exhibited significant axial and radial oscillations
throughout the test, and the burning rate and extinction diameter data were strongly influenced by
this motion. The residual droplet on the fiber had a large gas bubble that resulted in the size jump
after the visible flame extinguished.


NASA/TP-2015-216046 300




Figure 277.-Test FLEX-277. Free-floating methanol droplet burning in a 0.17/0.38/0.45 O2/N2/He,
0.70-atm ambient environment. The droplet drifted south in High-Bit-Depth Multispectral (HiBMs)
field of view (FOV) after deployment and ignition. Well after extinction, the droplet drifted out of the
FOV.


NASA/TP-2015-216046 301




Figure 278.-Test FLEX-278. Fiber-supported methanol droplet burning in a 0.17/0.38/0.45 O2/N2/He,
0.70-atm ambient environment. The droplet migrated slowly west in the High-Bit-Depth Multispectral
(HiBMs) field of view (FOV) after ignition, but it remained in the FOV the entire test. There was a small
spot on the fiber that burned off early in the burn, which was a short burn to extinction. This was near
the limiting oxygen index (LOI) in this ambient mixture.


NASA/TP-2015-216046 302




Figure 279.-Test FLEX-279. Free-floating heptane droplet burning in a 0.21/0.64/0.15 O2/N2/He, 1.0-atm
ambient environment. The droplet remained in High-Bit-Depth Multispectral (HiBMs) field of view (FOV)
for the entire test (it briefly drifted out well after the visible flame extinguished). A large vapor cloud
formed at the end of the test, indicating that a cool flame probably followed visible flame extinction.


NASA/TP-2015-216046 303




Figure 280.-Test FLEX-280. Free-floating heptane droplet burning in a 0.21/0.15/0.64 O2/N2/He, 1.0-atm
ambient environment. The droplet drifted east in the High-Bit-Depth Multispectral (HiBMs) field of view
(FOV) after deployment and ignition, and it drifted out of the FOV right before the flame extinguished
diffusively. The measured burning rate constant from the last part of the burn was used to extrapolate
the extinction droplet diameter from the droplet history from the time that the droplet left the FOV until
the visible flame extinguished.


NASA/TP-2015-216046 304




## References


Banu, Bilkis: Fluids and Combustion Facility (FCF)-
Combustion Integrated Rack (CIR). Payload
Accommodations Handbook, NASA CIR‒DOC‒4064,
2008. Available from the NASA Center for AeroSpace
Information.
Choi, M.Y.; and Dryer, F.L.: Microgravity Droplet
Combustion. Microgravity Combustion: Fire in Free Fall,
Howard D. Ross, ed., ch. 4, Academic Press, San Diego,
CA, 2001, pp. 183-297.
Dietrich, D.L., et al.: Droplet Combustion Experiments in
Spacelab. Proceedings of the 1996 26th International
Symposium on Combustion, vol. 1, 1996, pp. 1201-1207.
Faeth, G.M.: Current Status of Droplet and Liquid
Combustion. Prog. Energy Combust. Sci., vol. 3, no. 4,
1977, pp. 191-224.
Godsave, G.A.E.: Studies of the Combustion of Drops in a
Fuel Spray: The Burning of Single Drops of Fuel.
Proceedings of the Fourth Symposium (International) on
Combustion, Combustion Institute, 1952, pp. 818-830.
Goldsmith, M.: Experiments on the Burning of Single Drops
of Fuel. Jet Propulsion, vol. 26, no. 3, 1956, pp. 172-178.
Hall, A.R.; and Diederichsen, J.: An Experimental Study of
the Burning of Single Drops of Fuel in Air at Pressures
up to Twenty Atmospheres. Proceedings of the Fourth
Symposium (International) on Combustion, 1953,
pp. 837-846.
Kumagai, Seiichiro; and Isoda, Hiroshi: Combustion of Fuel
Droplets in a Falling Chamber. Proceedings of the Sixth
Symposium (International) on Combustion, 1956,
pp. 726-731.
Law, C.K.: Recent Advances in Droplet Vaporization and
Combustion. Progress in Energy and Combustion
Science, vol. 8, no. 3, 1982, pp. 171-201.


Marchese, A.J., et al.: Hydroxyl Radical Chemiluminescence
Imaging and the Structure of Microgravity Droplet
Flames. Proceedings of the 1996 26th International
Symposium on Combustion, 1996, pp. 1219-1226.
Nayagam, V., et al.: Microgravity n-Heptane Droplet
Combustion in Oxygen-Helium Mixtures at Atmospheric
Pressure. AIAA J., vol. 36, no. 8, 1998, pp. 1369-1378.
National Institutes of Health: ImageJ, Image Processing and
Analysis in Java. 2011. http://rsbweb.nih.gov/ij/
Accessed Dec. 11, 2012.
Robbins, Jesse; and Shinn, Clarise: Multi-user Droplet
Combustion Apparatus FLEX2. Reflight Safety Data
Package, NASA MDC‒DOC‒1790A, Rev. A, 2010.
Available from the NASA Center for AeroSpace
Information.
Sirignano, William A.: Fuel Droplet Vaporization and Spray
Combustion Theory. Prog. Energy Combust. Sci., vol. 9,
no. 4, 1983, pp. 291-322.
Spalding, D.B.: The Combustion of Liquid Fuels.
Proceedings of the Fourth Symposium (International) on
Combustion, 1952, pp. 847-864.
Spalding, D.B.: Experiments on the Burning and Extinction
of Liquid Fuel Spheres. Fuel, Vol. XXXII, 1953,
pp. 169-185.
Suh, H.K.; Choi, M.Y.; and Ferkul, P.V.: New Observations
of Sooting Behavior of Isolated Droplets of n-Heptane in
Microgravity Conditions. Proceedings of the 7th U.S.
National Combustion Meeting, Atlanta, GA, 2011.
Williams, Alan: Combustion of Droplets of Liquid Fuels: A
Review. Combust. Flame, vol. 21, no. 1, 1973, pp. 1-31.
Williams, Forman A.: Droplet Burning. Combustion
Experiments in a Zero-Gravity Laboratory, Thomas H.
Cochran, ed., vol. 73, ch. 2, 1981, pp. 31-60.
Wise, Henry; and Agoston, George A.: Burning of a Liquid
Droplet. Adv. Chem., ch. 10, vol. 20, 1958, pp. 116-135.


NASA/TP-2015-216046 305








