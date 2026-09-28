---
type: Document
title: "PSI experimental tables"
description: The 20 per-test tables from NASA's PSI archive — which investigation each belongs to, what one row is, what it records, and what it does not.
status: stable
generated: { by: "claude-code/opus-5.5", at: 2026-09-24T07:55:18Z }
ksor:
  audience: [public]
  owner: human:you
  approval: { by: human:you, at: 2026-09-24T07:55:18Z }
order: 41
verified:
  - by: "human:muhammad-marjan-ahmed"
    at: 2026-09-24T07:55:18Z
sources:
  - id: psi-experimental-tables
    title: "NASA PSI experimental tables (20 CSV files) and their inventory"
    resource: "The 'Experimental table' CSV files of NASA Physical Sciences Informatics datasets PSI-10, PSI-20, PSI-21, PSI-22, PSI-23, PSI-25, PSI-26, PSI-39, PSI-68, PSI-69, PSI-98, PSI-99, PSI-100, PSI-101, PSI-102, PSI-106, PSI-107 and PSI-159, plus one ACME set-point log, as downloaded for this project (psi-data/raw/csvs) and inventoried in psi-data/derived/source-inventory.md"
---

> [!IMPORTANT]
> An experimental table is the closest thing PSI has to a per-test record, but
> the tables were made independently by each flight team: different columns,
> different units, some one row per test, some one row per day. The "Not in
> this table" column below is the one to read before using a table to answer
> a question.

Every count and column name below is as the files themselves give it.[^psi-experimental-tables]

## Solid fuel

| Dataset | Investigation | Rows | One row is | Records | Not in this table |
| --- | --- | --- | --- | --- | --- |
| PSI-26 | [BASS](../investigations/solid-fuel/bass.md) | 122 | one test ("As Run Test #") | Date, GMT, test and sample numbers, Fuel Sample Material | flow, O₂, results |
| PSI-25 | [BASS-II](../investigations/solid-fuel/bass-ii.md) | 129 | one test ("Test #", e.g. B1, M18, O11) | PI, fuel sample, Flow restrictor, Fan display, Air display, Calibrated initial and final O2 % by vol, CO2 and CO before and after | flow velocity in cm/s (the Fan display and Air display columns give no unit), spread rates |
| PSI-98 | [SAFFIRE](../investigations/solid-fuel/saffire.md) (Saffire-1) | 4 | one sample (S1, S2) or a pre-test flow visualization | material, thickness, length, width, Air Flow (cm/s), Percent O2, ignition power and time, Burn Time (s), Flow Direction | spread rate |
| PSI-99 | [SAFFIRE](../investigations/solid-fuel/saffire.md) (Saffire-2) | 15 | one sample (2-1 to 2-9), a flow visualization, or a table note | as Saffire-1, plus burn and spread length and 1-g comparison values | — |
| PSI-100 | [SAFFIRE](../investigations/solid-fuel/saffire.md) (Saffire-3) | 2 | one sample (S1, S2) | material, thickness, length, width, Air Flow, Direction | O₂, results |

## Droplet combustion

| Dataset | Investigation | Rows | One row is | Records | Not in this table |
| --- | --- | --- | --- | --- | --- |
| PSI-69 | [FLEX](../investigations/droplet-combustion/flex.md) | 274 | one test ("FLEX Test #") | fuel, ambient pressure (mmHg), initial O2, N2, CO2 and He mole fractions, droplet initial diameter, extinction diameter, burning rate, burn time, test end | — |
| PSI-68 | [FLEX-2](../investigations/droplet-combustion/flex-2.md) | 8 | one fuel, with the planned condition ranges | Initial Droplet Diameter (mm), Ambient Gas Mixture, Oxygen Mole Fraction, Ambient Pressure (atm), Ambient Temperature (C), Flow Velocity (cm/s) | individual tests, results |
| PSI-39 | [CFI](../investigations/droplet-combustion/cfi.md) | 87 | one test ("Flex Number") | date, CIR, Pressure, Oxygen, Nitrogen, Helium, Fiber, Fuel | results (droplet sizes and burning rates are in a separate CFI data-summary workbook) |

## Gaseous flames

| Dataset | Investigation | Rows | One row is | Records | Not in this table |
| --- | --- | --- | --- | --- | --- |
| PSI-10 | [ACME](../investigations/gaseous-flames/acme.md) Flame Design | 207 normal + 120 inverse | one test | XO2 or XC2H4 before and after, flows (mg/s), pressures (atm), mean Zst, Tad (K) | results |
| PSI-159 | CFI-G | 179 normal + 1015 inverse (154 non-blank) | one test | XO2 or Xf, approx p (bar), flow rates, TFP, Hot ignition, burn time (sec), self-extinction or flow termination, peak burner temperature | — |
| PSI-20 | [ACME BRE](../investigations/gaseous-flames/acme-bre.md) | 18 | one test day | Burner Size (mm), Fuel Bottle, Oxygen Conc (percent), Flames Ignited | per-flame conditions, pressures |
| PSI-21 | ACME CLD Flame | 32 | one test day | Test Day, Fuel MFC, N2 MFC, Fuel Bottle, Fuel conc. Range, Flames ignited | O₂, per-flame values |
| PSI-22 | ACME E-FIELD Flames | 32 | one test day, or a continuation line for the day above | Mesh Polarity, Fuel Bottle, Fuel Conc, Flames Ignited | O₂, per-flame values |
| PSI-23 | [ACME s-Flame](../investigations/gaseous-flames/acme-s-flame.md) | 18 | one test day | Atmosphere, Fuel Bottle, Flames Ignited | per-flame values |
| PSI-107 | [SPICE](../investigations/gaseous-flames/spice.md) | 469 | one flame at one air-rate setting | GMT date and times, Fuel, Nozzle (mm), Fuel Rate (sccm and mg/s), Air Rate (cm/s) | smoke-point lengths (they are in the SPICE final report) |
| PSI-106 | SLICE | 12 | one test day | Test Date, Fuel Type | everything else |

## Smoke / aerosol

| Dataset | Investigation | Rows | One row is | Records | Not in this table |
| --- | --- | --- | --- | --- | --- |
| PSI-102 | [SAME](../investigations/smoke-aerosol/same.md) | 8 | one sample | Sample Material, Air Flow (cm/s), Weight loss rate (mg/min), Aging Duration (minutes) | values for samples 5–8, which read "same conditions as 1-4" |
| PSI-101 | [SAME-R](../investigations/smoke-aerosol/same-r.md) | 109 | one test ("SAME Test #") | Sample Type, Description, Date, Inlet velocity (cm/s), Rt/R0, durations and aging times | sample temperature (Rt/R0 is a heater setting; see SAME-R), particle sizes |

## Known quirks, as found in the files

- **Units inside cells and missing units.** Saffire-2 and Saffire-3 write
  units in the cells ("20 cm/s", ".33 cm"); the FLEX column "Burning rate; mm"
  names a unit the [FLEX](../investigations/droplet-combustion/flex.md) report
  defines differently.
- **Headers that lost characters.** Saffire-2's "?-g Burn Length" and
  "?-g Spread Length" columns; a "Samle Thickness" typo; FLEX's "O", "N", "CO"
  for O2, N2, CO2.
- **Blank and repeated rows.** CFI-G inverse flames has 1015 rows of which
  154 are non-blank; the CFI table's 87 rows carry repeated "Flex Number" values; the
  SPICE table repeats some rows exactly; the E-FIELD table repeats one test
  day's block.
- **Spreadsheet fill artifacts.** The CLD table's Fuel Bottle column counts up
  "40% CH4, 40% CH5, 40% CH6…" and the s-Flame table's Atmosphere* column "~21% O2
  with N2, N3, N4…" — the pattern a dragged spreadsheet cell leaves; the Test
  Type column ("Methane based test") still names the fuel.
- **Placeholders.** "RAMP", "RAMPED", "LOW O2" (Flame Design), "#VALUE!" and
  "#DIV/0!" (CFI-G), "n/a" and "Note 4" (Saffire-2).
- **CFI coverage.** The CFI table's "Flex Number" values run from 1206 to 1387; the
  [CFI](../investigations/droplet-combustion/cfi.md) report says its farnesane
  tests are FLEX-1388 to FLEX-1431, so farnesane is not in this table.

## Open questions

- CFI-G has no final report among this record's sources, so its columns are
  described here without a report to interpret them.
- One file, "19304A1_mfcSetpoints.csv", is a mass-flow-controller set-point
  log for ACME test point 19304A1 rather than a table of tests; how it relates
  to the s-Flame test day 19304 is not stated in any file.

[^psi-experimental-tables]: NASA PSI experimental tables, as inventoried: PSI-26_Experimental table_BASS.csv, data rows: 122, columns: Date | GMT | As Run Test # | Test # | Sample # | Fuel Sample Material. PSI-25_Experimental table_BASS-II.csv, data rows: 129, columns include PI | Test # | ... | Flow restrictor | Fan display | Air display | ... | Calibrated initial O2 % by vol. PSI-98_Experimental table_SAFFIRE-1.csv, data rows: 4. PSI-99_Experimental table_SAFFIRE-2.csv, data rows: 15, columns include Samle Thickness | ?-g Burn Length | ?-g Spread Length. PSI-100_Experimental table_SAFFIRE-3.csv, data rows: 2. PSI-69_Experimental table_FLEX.csv, data rows: 274, columns include Burning rate; mm. PSI-68_Experimental table_Flex2.csv, data rows: 8. PSI-39_Experimental table_CFI.csv, data rows: 87, columns: Flex Number | Test Date | Local Time | CIR | Pressure | Oxygen | Nitrogen | Helium | Fiber | Fuel. PSI-10 Flame Design: Normal Flame data rows: 207; Inverse Flame data rows: 120. PSI-159 CFI-G: Normal Flames data rows: 179; Inverse Flames data rows: 1015; non-blank data rows: 154. PSI-20 ACME BRE: 18. PSI-21 CLD Flame: 32. PSI-22 ACME E-FIELD Flames: 32. PSI-23 ACME s-Flame: 18. PSI-107 Spice: 469. PSI-106 Slice: 12. PSI-102 SAME: 8. PSI-101 SAME-R: 109. Cell contents quoted above ("same conditions as 1-4", "40% CH5", "~21% O2 with N3", "RAMPED", "LOW O2", "#VALUE!", "#DIV/0!", "Note 4", "Methane based test") are as they appear in those files.
