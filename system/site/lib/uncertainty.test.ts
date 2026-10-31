import assert from "node:assert/strict";
import { test } from "node:test";
import { measureText, outcomeText } from "../components/explore/format.ts";

test("uncertainty, ranges and censored bounds retain distinct display meanings", () => {
  assert.equal(measureText({ raw: "<.005", unit: "mg/m3", detection_limit: { operator: "<", value: .005, raw: "<.005" } }), "<0.005 mg/m3 (reported bound)");
  assert.equal(measureText({ raw: "10 +/- 2", value: 10, unit: "s", uncertainty: { kind: "reported_plus_minus", plus: 2, minus: 2, raw: "10 +/- 2" } }), "10 ± 2 s (reported uncertainty)");
  assert.equal(measureText({ raw: "1-2", value: 1.5, min: 1, max: 2, unit: "cm/s", interval_kind: "reported_range" }), "1–2 cm/s");
  assert.ok(outcomeText({ quantity: "mass", source: 0, measure: { raw: "<.005", detection_limit: { operator: "<", value: .005, raw: "<.005" } } }).includes("reported bound"));
});

test("outcome-specific smoke thresholds retain their units without a flow assumption", () => {
  assert.equal(outcomeText({ quantity: "smoke_threshold_crossing_time", source: 0,
    measure: { raw: "981", value: 981, min: 981, max: 981, unit: "s" },
    at: { selected_mass_concentration_mg_m3: 1 } }), "981 s at 1 mg/m³ selected smoke threshold");
});

test("unresolved source values are explicitly marked as excluded", () => {
  assert.match(outcomeText({ quantity: "total_heat_release_imaging", source: 0,
    measure: { raw: "580", value: 580, unit: "kJ", flags: ["source_definition_unresolved"] } }), /excluded from analysis/);
});
