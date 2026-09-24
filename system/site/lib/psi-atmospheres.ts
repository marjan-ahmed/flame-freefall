// Named mission-atmosphere presets — TypeScript twin of
// system/chatkit-server/psi_atmospheres.py. Every number is copied from a
// stable governed document and cited by its stable id; keep both in sync.

export const ATM_PER_KPA = 1 / 101.325;

export type Atmosphere = {
  id: string;
  label: string;
  o2_pct: number;
  pressure_atm: number;
  pressure_source_value: string;
  doc: string;
  doc_title: string;
  quote: string;
};

export const ATMOSPHERES: Record<string, Atmosphere> = {
  iss: {
    id: "iss",
    label: "ISS / ambient (NASA-STD-6001B)",
    o2_pct: 20.9,
    pressure_atm: Math.round(101.4 * ATM_PER_KPA * 10000) / 10000,
    pressure_source_value: "101.4 kPa (14.7 psia)",
    doc: "knowledge/foundations/nasa-std-6001b",
    doc_title: "NASA-STD-6001B",
    quote: "ambient conditions are defined as 20.9% O₂, 101.4 kPa (14.7 psia), 23±5°C",
  },
  gateway: {
    id: "gateway",
    label: "Lunar Gateway (proposed)",
    o2_pct: 26.5,
    pressure_atm: Math.round(73.5 * ATM_PER_KPA * 10000) / 10000,
    pressure_source_value: "73.5 kPa",
    doc: "knowledge/foundations/decadal-survey/liao-micro-partial-gravity-fires",
    doc_title: "Challenges and Research Needs for Micro- and Partial-Gravity Fires",
    quote: "the Lunar Gateway is expected to have an oxygen concentration of 26.5% and a pressure of 73.5 kPa",
  },
  lunar: {
    id: "lunar",
    label: "Lunar surface habitat (proposed)",
    o2_pct: 34.0,
    pressure_atm: Math.round(56.5 * ATM_PER_KPA * 10000) / 10000,
    pressure_source_value: "56.5 kPa",
    doc: "knowledge/foundations/decadal-survey/liao-micro-partial-gravity-fires",
    doc_title: "Challenges and Research Needs for Micro- and Partial-Gravity Fires",
    quote: "the Lunar modules are expected to have an oxygen concentration of 34% and a pressure of 56.5 kPa",
  },
};

export function queryFor(atmId: string): { o2_pct: number; pressure_atm: number } {
  const a = ATMOSPHERES[atmId];
  return { o2_pct: a.o2_pct, pressure_atm: a.pressure_atm };
}
