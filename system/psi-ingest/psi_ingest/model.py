"""The unified run record every adapter emits.

One Run = one test as its source lists it (granularity "test"), or — where a
source only publishes a daily summary or a planned envelope — one day
("day") or one matrix row ("envelope"). The granularity is carried so a
count of runs is never inflated by treating a summary row as a test.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .units import Measure


def cat(value: str | None, raw: object = None, basis: str | None = None) -> dict | None:
    """A categorical condition: the normalized value, the cell it came from,
    and — when the value was inferred rather than read — the sourced basis."""
    if value is None:
        return None
    out = {"value": value}
    if raw is not None and str(raw).strip() and str(raw).strip() != value:
        out["raw"] = str(raw).strip()
    if basis:
        out["basis"] = basis
    return out


@dataclass
class Outcome:
    quantity: str
    measure: Measure | None = None
    text: str | None = None
    source: int = 0
    at: dict | None = None  # the condition this value was measured at, e.g. {"flow_cm_s": 10}
    note: str | None = None
    confirmed_by: list[int] = field(default_factory=list)  # other sources stating the same value
    metadata: dict = field(default_factory=dict)  # outcome-specific, independently source-indexed methods/instruments

    def to_json(self) -> dict:
        out: dict = {"quantity": self.quantity, "source": self.source}
        if self.confirmed_by:
            out["confirmed_by"] = self.confirmed_by
        if self.measure is not None:
            out["measure"] = self.measure.to_json()
        if self.text is not None:
            out["text"] = self.text
        if self.at:
            out["at"] = self.at
        if self.note:
            out["note"] = self.note
        if self.metadata:
            out["metadata"] = self.metadata
        return out


@dataclass
class Run:
    investigation: str
    label: str
    granularity: str = "test"
    date: str | None = None
    sources: list[dict] = field(default_factory=list)
    conditions: dict = field(default_factory=dict)
    outcomes: list[Outcome] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    raw: list[dict] = field(default_factory=list)  # parallel to `sources`
    conflicts: list[dict] = field(default_factory=list)
    id: str = ""
    observation_relationship: dict | None = None

    def set(self, key: str, value) -> None:
        if value is not None:
            self.conditions[key] = value

    def outcome(self, quantity: str, measure: Measure | None = None, text: str | None = None, **kw) -> None:
        if measure is None and not text:
            return
        self.outcomes.append(Outcome(quantity, measure=measure, text=text, **kw))

    def to_json(self) -> dict:
        conditions = {
            k: (v.to_json() if isinstance(v, Measure) else v)
            for k, v in sorted(self.conditions.items())
        }
        out = {
            "id": self.id,
            "investigation": self.investigation,
            "label": self.label,
            "granularity": self.granularity,
            "date": self.date,
            "sources": self.sources,
            "conditions": conditions,
            "outcomes": [o.to_json() for o in self.outcomes],
        }
        if self.conflicts:
            out["conflicts"] = self.conflicts
        if self.notes:
            out["notes"] = self.notes
        if self.observation_relationship is not None:
            out["observation_relationship"] = self.observation_relationship
        out["raw"] = self.raw
        return out


def psi_source(psi_id: str, file: str, row: int) -> dict:
    """`row` is the 1-based line number in the file, header = line 1, so a
    reader can open the CSV and land on the exact line."""
    return {"kind": "psi", "dataset": psi_id, "file": file, "row": row}
