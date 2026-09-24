---
type: Summary
---

The 20 PSI experimental tables are the closest thing to a per-test record,
but each flight team made its own: different columns and units, some with one
row per test, some one row per day. Read what a table does **not** record
before using it.

- **Per test:** BASS (122 rows), BASS-II (129), FLEX (274), CFI (87), CFI-G
  (179 normal flames, and 1015 inverse-flame rows of which 154 are non-blank),
  Flame Design (207 + 120), SAME-R (109).
- **Per day:** the ACME BRE, CLD, E-FIELD and s-Flame tables, and SLICE.
- **Per fuel, planned:** FLEX-2 (8 rows of condition ranges, not tests).
- **Key gaps:** BASS-II gives flow only as Fan display / Air display
  readings with no unit; SPICE has no smoke-point lengths; CFI has no
  farnesane tests.
- **Quirks found:** units written inside cells, headers that lost
  characters, blank and repeated rows, spreadsheet fill artifacts such as
  "40% CH5".
