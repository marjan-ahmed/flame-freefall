import type { Category, Condition, Measure, Outcome } from "@/lib/psi-types";

export const QUANTITY_LABEL: Record<string, string> = {
  spread_rate: "Flame spread rate",
  spread_rate_1g: "Spread rate (1-g comparison)",
  burning_rate_k: "Burning-rate constant k",
  burning_rate_k_hot: "Burning-rate constant k (hot flame)",
  burning_rate_k_cool: "Burning-rate constant k (cool flame)",
  extinction_diameter: "Extinction diameter",
  extinction_diameter_hot: "Extinction diameter (hot flame)",
  extinction_diameter_cool: "Extinction diameter (cool flame)",
  burn_time: "Burn time",
  burn_time_hot_flame: "Hot-flame burn time",
  test_end: "Test end",
  end_mode: "End mode",
  ignited: "Ignited",
  hot_ignition: "Hot ignition",
  cool_flame: "Cool flame",
  spread_extent: "Spread extent",
  burn_extent_1g: "Burn extent (1-g comparison)",
  flames_ignited: "Flames ignited (per day)",
  weight_loss_rate: "Weight-loss rate",
  peak_heat_release: "Peak heat release",
  total_heat_release_imaging: "Total heat release (imaging)",
  avg_heat_release_o2: "Avg heat release (O₂ consumption)",
  total_heat_release_o2: "Total heat release (O₂ consumption)",
  max_temp_sfu_outlet: "Max temp at flow-unit outlet",
  max_temp_ffd_nearest: "Max temperature at far-field device / nearest location",
  co2_partial_pressure_increase: "CO₂ partial-pressure increase",
  smoke_threshold_crossing_time: "Reported smoke-threshold crossing time",
  co2_increase_ppm: "CO₂ increase",
  co_increase_ppm: "CO increase",
  final_co2_pct: "Final CO₂",
  final_co_ppm: "Final CO",
  peak_burner_temp_c: "Peak burner temperature",
  flame_color: "Flame color",
  reignitions: "Re-ignitions",
  comment: "Comment",
  dusttrak_a_mass_concentration: "DustTrak A mass concentration (source processed)",
  dusttrak_b_mass_concentration: "DustTrak B mass concentration (source processed)",
  aerosol_arithmetic_mean_diameter: "Arithmetic mean aerosol diameter (source processed)",
  aerosol_diameter_of_average_mass: "Diameter of average mass (source processed)",
  iss_detector_scatter_volts: "ISS smoke-detector scattering signal (source processed)",
  sts_detector_volts: "STS smoke-detector signal (source processed)",
};

export const CONDITION_LABEL: Record<string, string> = {
  o2_pct: "O₂",
  flow_cm_s: "Flow velocity",
  pressure_atm: "Pressure",
  thickness_mm: "Thickness",
  width_cm: "Width",
  width_nominal_cm: "Width (nominal, from description)",
  length_cm: "Length",
  diameter_mm: "Diameter",
  droplet_d0_mm: "Droplet initial diameter",
  fuel: "Fuel / material (as written)",
  fuel_family: "Fuel family",
  fuel_form: "Sample form",
  flow_direction: "Flow direction",
  diluent: "Diluent",
  gravity: "Gravity",
  flame_type: "Flame type",
  n2_pct: "N₂",
  co2_pct: "CO₂",
  he_pct: "He",
  fuel_fraction_pct: "Fuel fraction",
  ambient_fuel_pct: "Ambient fuel fraction",
  oxidizer_stream_o2_pct: "Oxidizer-stream O₂ (inverse flame)",
  fuel_flow_mg_s: "Fuel flow",
  oxidizer_flow_mg_s: "Oxidizer flow",
  ignition_power_w: "Igniter power",
  ignition_time_s: "Igniter on-time",
  flow_setting_air: "Air display (panel reading)",
  flow_setting_fan: "Fan display (panel reading)",
  flow_restrictor: "Flow restrictor",
  sides_burning: "Sides burning",
  pi: "Principal investigator",
  adiabatic_flame_temp_k: "Adiabatic flame temperature (computed)",
  stoich_mixture_fraction: "Stoichiometric mixture fraction",
  apparatus: "Apparatus",
  confinement: "Confinement",
  instrument: "Instrument",
  measurement_method: "Measurement method",
  duct_width_cm: "Duct width (documented apparatus)",
  duct_height_cm: "Duct height (documented apparatus)",
  duct_length_cm: "Duct length (documented apparatus)",
};

export const FLAG_LABEL: Record<string, string> = {
  approx: "approximate (~)",
  range: "range",
  multi: "several values",
  converted: "unit converted",
  drifted_during_test: "drifted during test",
  varied_during_test: "varied during test",
  sources_disagree: "sources disagree",
  final_reading_suspect: "final reading implausible — not used",
  mole_fraction_to_pct: "from mole fraction",
  unit_from_report: "unit per report",
  reading_may_be_inaccurate: "reading may be inaccurate (per report)",
  suspect_value: "unreadable value",
  unparsed: "not machine-readable",
  ramped: "ramped",
  computed: "computed, not measured",
  nominal: "nominal",
  negative_reading: "negative reading",
  initial: "initial value",
  source_processed: "source-processed value",
  workbook_cached: "saved workbook result, not recalculated",
  documented_apparatus: "documented campaign apparatus; not a test-specific measurement",
};

export function fmt(x: number | undefined | null, digits = 3): string {
  if (x === undefined || x === null || Number.isNaN(x)) return "—";
  if (x === 0) return "0";
  const a = Math.abs(x);
  if (a >= 1000) return x.toLocaleString("en-US", { maximumFractionDigits: 0 });
  return Number(x.toPrecision(digits)).toString();
}

export function isCat(c: Condition | undefined): c is Category {
  return !!c && typeof (c as Category).value === "string";
}

export function measureText(m: Measure): string {
  const unit = m.unit ? ` ${m.unit}` : "";
  if (m.detection_limit) return `${m.detection_limit.operator}${fmt(m.detection_limit.value)}${unit} (reported bound)`;
  if (m.uncertainty && m.value !== undefined && m.uncertainty.plus !== undefined)
    return `${fmt(m.value)} ± ${fmt(m.uncertainty.plus)}${unit} (reported uncertainty)`;
  if (m.values?.length && m.value === undefined) return m.values.map((v) => fmt(v)).join(", ") + unit;
  if (m.value !== undefined && m.min !== undefined && m.max !== undefined && m.min !== m.max)
    return `${fmt(m.min)}–${fmt(m.max)}${unit}`;
  if (m.value !== undefined) return `${fmt(m.value)}${unit}`;
  if (m.min !== undefined && m.max !== undefined) return `${fmt(m.min)}–${fmt(m.max)}${unit}`;
  return m.raw;
}

export function conditionText(c: Condition): string {
  return isCat(c) ? c.value : measureText(c as Measure);
}

export function outcomeText(o: Outcome): string {
  // A measure with no number but a text (a FLEX 0 that means "no visible
  // extinction", not 0 mm) shows the text; run-detail adds the raw cell.
  const numeric = o.measure && (o.measure.min !== undefined || o.measure.values?.length);
  const v = o.measure && (numeric || !o.text) ? measureText(o.measure) : (o.text ?? "—");
  const conditions = Object.entries(o.at ?? {}).map(([key, value]) => key === "flow_cm_s"
    ? `${fmt(value)} cm/s` : key === "selected_mass_concentration_mg_m3"
      ? `${fmt(value)} mg/m³ selected smoke threshold` : `${key}=${fmt(value)}`);
  const at = conditions.length ? ` at ${conditions.join(", ")}` : "";
  const withheld = o.measure?.flags?.includes("source_definition_unresolved")
    ? " (reported value; excluded from analysis pending source clarification)" : "";
  return `${v}${at}${withheld}`;
}

export const GEOMETRY_LABEL: Record<string, string> = {
  "solid-fuel": "Solid fuel",
  "droplet-combustion": "Droplet combustion",
  "gaseous-flames": "Gaseous flames",
  "smoke-aerosol": "Smoke / aerosol",
};
