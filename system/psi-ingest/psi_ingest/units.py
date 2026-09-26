"""Cell parsers shared by every adapter.

PSI tables put units inside cells ("20 cm/s"), write ranges ("21.5 - 21.7",
"10 to 2.2"), lists ("21; 26.5; 40", "10, 6, 5, and 3"), approximations
("~ 21.5") and placeholders ("RAMP", "n/a", "#VALUE!"). A parser here turns
one cell into a Measure that ALWAYS keeps the cell's raw text, and flags what
it had to interpret. A cell it can't read with confidence comes back with
value None and an `unparsed` / `suspect_value` flag — never a guess.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

NUM = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
UNIT = r"[A-Za-z%°µ][A-Za-z/%°µ²0-9]*"

_MISSING = {
    "", "n/a", "na", "none", "-", "—", "–", "#value!", "�", "?", "null", "nan",
}
_RAMP = re.compile(r"\bramp(ed)?\b", re.I)
_SINGLE = re.compile(rf"^\s*({NUM})\s*({UNIT})?\s*$")
_RANGE = re.compile(rf"^\s*({NUM})\s*({UNIT})?\s*(?:-|–|to)\s*({NUM})\s*({UNIT})?\s*$", re.I)
# "037 mm": an integer with a leading zero is almost certainly a lost decimal
# point (0.37?) — but that is a guess, so it is refused rather than read.
_LEADING_ZERO_INT = re.compile(r"^0\d+$")


@dataclass
class Measure:
    raw: str
    value: float | None = None
    min: float | None = None
    max: float | None = None
    unit: str | None = None
    flags: list[str] = field(default_factory=list)
    values: list[float] | None = None

    def __post_init__(self) -> None:
        if self.value is not None:
            if self.min is None:
                self.min = self.value
            if self.max is None:
                self.max = self.value

    def flag(self, *names: str) -> "Measure":
        for n in names:
            if n not in self.flags:
                self.flags.append(n)
        return self

    @property
    def usable(self) -> bool:
        return self.value is not None or self.min is not None

    def scaled(self, factor: float, unit: str, flag: str | None = "converted") -> "Measure":
        """Unit conversion; the raw text is kept, so the conversion is auditable."""
        f = lambda x: None if x is None else round(x * factor, 6)  # noqa: E731
        m = Measure(
            raw=self.raw,
            value=f(self.value),
            min=f(self.min),
            max=f(self.max),
            unit=unit,
            flags=list(self.flags),
            values=None if self.values is None else [f(v) for v in self.values],
        )
        if flag:
            m.flag(flag)
        return m

    def to_json(self) -> dict:
        out: dict = {"raw": self.raw}
        for k in ("value", "min", "max", "unit"):
            v = getattr(self, k)
            if v is not None:
                out[k] = v
        if self.values is not None:
            out["values"] = self.values
        if self.flags:
            out["flags"] = self.flags
        return out


def is_missing(raw: object) -> bool:
    return raw is None or str(raw).strip().lower() in _MISSING


def _num(s: str) -> float | None:
    s = s.strip()
    if _LEADING_ZERO_INT.match(s.lstrip("+-")):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def parse_measure(raw: object, unit: str | None = None) -> Measure | None:
    """One cell → Measure, or None when the cell is empty/placeholder.

    `unit` is the unit the COLUMN header declares; a unit written in the cell
    wins over it (and both are kept: the cell's text is `raw`).
    """
    if is_missing(raw):
        return None
    text = str(raw).strip()
    if _RAMP.search(text):
        return Measure(raw=text, unit=unit, flags=["ramped"])

    s = text
    flags: list[str] = []
    if "~" in s:
        flags.append("approx")
        s = s.replace("~", " ").strip()
    # "3,150" is a thousands separator, not a two-value list.
    if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?(?:\s*" + UNIT + r")?", s):
        s = s.replace(",", "")

    m = _SINGLE.match(s)
    if m:
        v = _num(m.group(1))
        if v is None:
            return Measure(raw=text, unit=unit, flags=["suspect_value"])
        return Measure(raw=text, value=v, min=v, max=v, unit=m.group(2) or unit, flags=flags)

    m = _RANGE.match(s)
    if m:
        a, b = _num(m.group(1)), _num(m.group(3))
        if a is None or b is None:
            return Measure(raw=text, unit=unit, flags=["suspect_value"])
        lo, hi = min(a, b), max(a, b)
        return Measure(
            raw=text,
            value=round((lo + hi) / 2, 6),
            min=lo,
            max=hi,
            unit=m.group(4) or m.group(2) or unit,
            flags=flags + ["range"],
            values=[a, b],
        )

    parts = [p for p in re.split(r"\s*(?:;|,|\band\b|\bor\b|&)\s*", s) if p.strip()]
    if len(parts) > 1:
        vals: list[float] = []
        cell_unit = None
        for p in parts:
            pm = _SINGLE.match(p)
            if not pm:
                return Measure(raw=text, unit=unit, flags=["unparsed"])
            v = _num(pm.group(1))
            if v is None:
                return Measure(raw=text, unit=unit, flags=["suspect_value"])
            vals.append(v)
            cell_unit = cell_unit or pm.group(2)
        return Measure(
            raw=text,
            value=None,
            min=min(vals),
            max=max(vals),
            unit=cell_unit or unit,
            flags=flags + ["multi"],
            values=vals,
        )

    return Measure(raw=text, unit=unit, flags=["unparsed"])


def fraction_to_pct(m: Measure | None) -> Measure | None:
    """Mole fraction (0–1) → percent. A value already > 1 is refused, not rescaled."""
    if m is None or not m.usable:
        return m
    if (m.max or 0) > 1.0:
        return Measure(raw=m.raw, flags=m.flags + ["suspect_value"], unit="%")
    return m.scaled(100.0, "%", "mole_fraction_to_pct")


def pct(m: Measure | None) -> Measure | None:
    """A column that is already in percent: normalize the unit, refuse > 100."""
    if m is None:
        return None
    if m.usable and (m.max or 0) > 100.0:
        return Measure(raw=m.raw, flags=m.flags + ["suspect_value"], unit="%")
    m.unit = "%"
    return m


LENGTH_TO_MM = {"mm": 1.0, "cm": 10.0, "m": 1000.0, "µm": 0.001, "micron": 0.001, "in": 25.4, '"': 25.4}
PRESSURE_TO_ATM = {"atm": 1.0, "mmhg": 1 / 760.0, "bar": 1 / 1.01325, "kpa": 1 / 101.325}


def to_mm(m: Measure | None, default_unit: str | None = None) -> Measure | None:
    if m is None or not m.usable:
        return m
    u = (m.unit or default_unit or "").lower()
    if u not in LENGTH_TO_MM:
        # Numbers refused (null plus flag, never a guess); the unit stays the
        # one actually read, never relabelled as mm.
        return Measure(raw=m.raw, unit=m.unit or default_unit, flags=m.flags + ["unknown_unit"])
    if u == "mm":
        m.unit = "mm"
        return m
    return m.scaled(LENGTH_TO_MM[u], "mm")


def to_atm(m: Measure | None, from_unit: str) -> Measure | None:
    if m is None or not m.usable:
        return m
    # An absolute pressure of zero is vacuum, where nothing burns: FLEX-114
    # prints "0" mmHg in both the PSI table and the report, yet burned 18.9 s.
    # Refused as a value (raw kept), never "corrected".
    if (m.max or 0) <= 0:
        return Measure(raw=m.raw, unit="atm", flags=m.flags + ["suspect_value", "zero_absolute_pressure"])
    u = (m.unit or from_unit).lower()
    factor = PRESSURE_TO_ATM.get(u)
    if factor is None:
        return Measure(raw=m.raw, unit=m.unit or from_unit, flags=m.flags + ["unknown_unit"])
    if factor == 1.0:
        m.unit = "atm"
        return m
    return m.scaled(factor, "atm", f"converted_from_{u}")


def text(raw: object) -> str | None:
    """A categorical cell: stripped, collapsed whitespace, None when a placeholder."""
    if is_missing(raw):
        return None
    return re.sub(r"\s+", " ", str(raw)).strip()
