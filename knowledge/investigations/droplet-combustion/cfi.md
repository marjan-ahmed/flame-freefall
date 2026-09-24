---
type: Document
title: "CFI: Cool Flame Investigation"
description: Droplet cool-flame experiments on n-dodecane, n-dodecane/iso-dodecane mixtures and farnesane in the ISS Combustion Integrated Rack in 2017, from the CFI science final report.
status: draft
ksor:
  audience: [public]
  owner: human:you
order: 26
geometry_class: droplet-combustion
sources:
  - id: cfi-final-report
    title: "Cool Flame Investigation (CFI) — Science Final Report"
    resource: "CFI science final report by Vedha Nayagam (CWRU/LTX) and Daniel L. Dietrich (NASA/LTX); distributed in the NASA Physical Sciences Informatics (PSI) archive as 'CFI Science Final Report.pdf'. The title-page date did not survive text extraction legibly."
  - id: cfi-flex-1393-sheet
    title: "CFI analyzed-data summary sheet, test FLEX-1393"
    resource: "One-page analyzed-data summary plot for CFI test FLEX-1393, dated Mon, Aug 28, 2017; NASA PSI dataset PSI-39, file 'PSI-39_Analyzed Data_FLEX-1393_Summary.pdf'"
---

> [!NOTE]
> Geometry class: **droplet combustion** — single fuel droplets burning in the
> same Multi-used Droplet Combustion Apparatus as [FLEX](flex.md) and
> [FLEX-2](flex-2.md). Comparable with those; not directly with solid-fuel or
> gaseous-flame investigations.

> [!IMPORTANT]
> The report says "All the CFI data is yet to be fully analyzed and
> interpreted" and presents only general observations from preliminary
> analysis. Nothing below is a final result.

CFI was conceived as a follow-up to the FLEX and FLEX-2 droplet experiments,
to explore the quasi-steady **cool flames** those experiments discovered: flames
controlled by low-temperature chemistry, occurring in the negative temperature
coefficient (NTC) region of n-alkane fuels, at temperatures in the range of
700 to 900 K — unlike hot flames above 1200 K — and without a visible flame.
Because cool-flame chemistry depends on fuel structure, pressure and
temperature, CFI tested three fuel combinations at ambient pressures up to 5
atmospheres, with and without helium.[^cfi-final-report]

## Structured facts

Every value below is drawn from the sources cited in this document.

### Experimental conditions

| Field | Value |
| --- | --- |
| Facility | Multi-used Droplet Combustion Apparatus (MDCA) in the Combustion Integrated Rack (CIR), ISS |
| Dates of operation | January 2017 through September 2017 |
| Tests | over two hundred |
| Initial droplet size | around 4 mm |
| Fuels and pressures | pure n-dodecane at 0.5, 0.75, 1, 1.25, 2, 3, and 5 atm; n-dodecane/iso-dodecane 75/25% and 60/40% by mass from 0.5 to 5 atm; farnesane from 0.75 to 3 atm |
| Helium dilution | 29% and 59% with O2 mole fraction at 0.21 |
| Droplet tethering (when needed) | 40 micron silicon-carbide fiber |
| Diagnostics | backlit black-and-white camera (5 cm X 5 cm FOV) for droplet size; UV-sensitive camera imaging OH* for flame size; color camera; narrow-band and wide-band radiometers |

### Where the data is (the report's own mapping of test numbers)

| Fuel | Test numbers |
| --- | --- |
| Pure n-dodecane | FLEX-1206 to FLEX-1284 |
| n-dodecane/iso-dodecane (75%-25% and 60%-40%) | FLEX-1285 to FLEX-1387 |
| Farnesane | FLEX-1388 to FLEX-1431 |

### Example analyzed test (FLEX-1393)

The PSI archive includes a one-page analyzed-data summary for test FLEX-1393
(Farnesane): P = 769.710 mmHg, YO2 = 0.210, YHe = 0.000, Dext = 4.330, with
plots of droplet history, hot-flame and cool-flame diameters against
t / D0 ( s / mm ).[^cfi-flex-1393-sheet]

## Findings (preliminary)

- Cool flames were observed for the pure n-dodecane and n-dodecane/iso-dodecane
  cases; adding the branched iso-dodecane reduces the tendency to form cool
  flames (see Open questions on the report's wording).
- Warm flames — from a change in chemical pathway during n-alkane oxidation —
  were observed; "Addition of helium seems to enhance this balance within the
  NTC region."
- No new anomalies or surprises were observed, but above 2 atm multiple
  reignition cycles occurred, and the vapor region between the droplet surface
  and the flame "became unstable and ill-defined at higher pressures, a
  phenomenon which is not fully understood".[^cfi-final-report]

## Open questions

- **Fuel names in the findings.** The findings section writes "n-dodecanol"
  and "iso-dodecanol" (alcohols) where the rest of the report, and its test
  list, say n-dodecane and iso-dodecane. This entry reads them as the alkanes
  named everywhere else, which is an interpretation; the source's own words
  are kept in the footnote.
- **Coverage of the PSI experimental table.** The report maps test numbers up
  to FLEX-1431; the CFI experimental table in PSI (dataset PSI-39) lists fewer
  tests — see [the PSI experimental tables](../../data-sources/psi-experimental-tables.md).
- The unit of Dext on the FLEX-1393 sheet is not printed next to the value.
- Burning rates, extinction diameters and radiant output are said to be
  measured but are not tabulated in the report body.

[^cfi-final-report]: CFI Science Final Report (Nayagam, Dietrich). §1 Overview: "The CFI experiments are conceived as follow-up experiments to the FLEX and FLEX-2 droplet combustion experiments onboard the ISS to further explore the newly discovered quasi-steady "cool flames." Cool flames are controlled by low temperature chemistry, and occur in the NTC region of n-alkane fuels. FLEX series of experiments showed for the first time that quasi-steady stable flames can be established surrounding a droplet in microgravity under certain conditions, without a visible flame at temperatures in the range of 700 to 900 K, unlike the hot flames where the flame temperature is higher than 1200 K... three different fuel combinations were investigated, namely, pure n-dodecane, n-dodecane/iso- dodecane mixtures and farnesane ( a renewable jet fuel) at ambient pressures up to 5 atmospheres." §2.c: "CFI experiments were conducted onboard the ISS from January 2017 through September 2017." §4.a: "When required a 40 micron silicon-carbide fiber is used... a backlit, black-and-white camera ( 5 cm X 5 cm FOV)... a UV-sensitive camera is used to image the OH* emission... Narrow-band and wide-band radiometers." §4.b On-Orbit Testing: "Over two hundred tests were carried out during the CFI experimental campaign. The initial droplet size was kept around 4 mm... Pure n-dodecane at 0.5, 0.75, 1, 1.25, 2, 3, and 5 atm. N-dodecane/Iso-dodecane mixtures: 75/25% and 60/40% by mass at pressures from 0.5 to 5 atm • Helium dilution by 29% and 59% with O2 mole fraction at 0.21 • Farnesane: from 0.75 to 3 atm." §4.c: "No new anomalies or surprises were observed during the CFI experiments. However, as the ambient pressure is increased above 2 atm, multiple reignition cycles were observed... became unstable and ill- defined at higher pressures, a phenomenon which is not fully understood." §4.d Organization of Data in PSI: "Pure n-dodecane data: FLEX-1206 to FLEX-1284; N-dodecane/Iso-dodecane ( 75%-25% & 60%-40%) mixture data: FLEX-1285 to FLEX-1387); Farnesane data: FLEX-1388 to FLEX-1431." §5.a Findings: "All the CFI data is yet to be fully analyzed and interpreted... Cool flames were observed during n-dodecanol combustion as well as n-dodecanol/iso-dodecanol mixture cases. The addition of iso-dodecanol reduces the tendency to form cool flames in n-dodecanol... Addition of helium seems to enhance this balance within the NTC region."

[^cfi-flex-1393-sheet]: CFI analyzed-data summary sheet, FLEX-1393 (Mon, Aug 28, 2017): "FLEX-1393 / F240B02 / P = 769.710 mmHg / YO2 = 0.210 / YHe = 0.000 / Farnesane / Dext = 4.330"; plots titled Droplet History, Hot-Flame Diameter, Cool Flame Diameter, against "t / D0 ( s / mm )".
