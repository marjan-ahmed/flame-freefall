"""Conservative, deterministic binding of an evidence lookup to this user turn.

This is deliberately a bounded parser, not another model. Ambiguous numbers,
ranges and unsupported units refuse the lookup instead of silently narrowing it.
Recorded query defaults (retrieval tolerances) are unchanged. Named atmospheres
come only from the existing cited presets and are exposed beside the query.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import math
import re

import psi_atmospheres
import psi_query


@dataclass
class RequestIntent:
    query: dict = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    atmosphere: str | None = None
    investigations: list[str] = field(default_factory=list)


NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)"
OXYGEN = r"(?:oxygen|o2|o₂)"
QUERY_KEYS = ("o2_pct", "flow_cm_s", "pressure_atm", "fuel_family", "geometry_class", "flow_direction", "investigation")


def parse_request(text: str) -> RequestIntent:
    result = RequestIntent()
    consumed: list[tuple[int, int]] = []
    normalized = text.lower().replace("−", "-")

    def add(key, value, span=None):
        if key == "investigation" and value not in result.investigations:
            result.investigations.append(value)
        if key in result.query and result.query[key] != value:
            result.errors.append(f"More than one {key} was requested; use the Explorer to specify separate searches.")
        else:
            result.query[key] = value
        if span:
            consumed.append(span)

    def numbers(pattern, key, convert=lambda n, _m: n):
        for match in re.finditer(pattern, normalized, re.I):
            value = convert(float(match.group("n")), match)
            if not math.isfinite(value):
                result.errors.append("A requested condition is not finite.")
            else:
                add(key, value, match.span())

    if re.search(r"\b(?:nan|infinity|inf)\b|±|\+/-|\b(?:between|below|above|less than|greater than|at least|at most)\b", normalized):
        result.errors.append("Ranges, inequalities and custom tolerances need the Explorer; no point query was inferred.")
    if re.search(r"\d\s*(?:[-–—]|\bto\b)\s*\d", normalized):
        result.errors.append("A range cannot be interpreted as one target condition; use the Explorer.")
    if re.search(r"\b(?:exclude|excluding|except|not|without)\s+(?:at\s+)?(?:\d|opposed|concurrent|coflow|pressure|oxygen|o2|pmma|methanol|heptane|solid|droplet|saffire|bass)", normalized):
        result.errors.append("Negated filters need explicit Explorer controls; no positive filter was inferred.")
    if re.search(rf"\b(?:spread|regression|burning)\s+rate\s*(?:is|of|=|:)?\s*(?:at\s+)?{NUMBER}\s*(?:mm|cm|m)\s*/", normalized):
        result.errors.append("An outcome rate is not a flow condition; use the measurement controls to inspect outcomes.")

    numbers(rf"(?P<n>{NUMBER})\s*(?:%|percent)\s*(?:of\s+)?{OXYGEN}\b", "o2_pct")
    numbers(rf"\b{OXYGEN}(?:\s+(?:concentration|level|fraction))?\s*(?:is|of|at|=|:)?\s*(?P<n>{NUMBER})\s*(?:%|percent)", "o2_pct")
    numbers(rf"(?P<n>{NUMBER})\s*(?P<u>kpa|atm|atmospheres?|psia|psi)\b", "pressure_atm",
            lambda n, m: n * (psi_atmospheres.ATM_PER_KPA if m.group("u") == "kpa" else psi_atmospheres.ATM_PER_PSIA if m.group("u") in ("psi", "psia") else 1))
    numbers(rf"(?P<n>{NUMBER})\s*(?P<u>cm|mm|m)\s*(?:/\s*s(?:ec(?:ond)?s?)?|s\s*[-−]\s*1)\b", "flow_cm_s",
            lambda n, m: n * {"cm": 1, "mm": .1, "m": 100}[m.group("u")])

    geometries = {
        "solid-fuel": r"\b(?:solid[- ]fuel|solid samples?|solid materials?|solids)\b",
        "droplet-combustion": r"\b(?:droplet[- ]combustion|droplets?)\b",
        "gaseous-flames": r"\b(?:gaseous[- ]flames?|gas flames?)\b",
        "smoke-aerosol": r"\b(?:smoke[- ]aerosol|smoke particles?|aerosols?)\b",
    }
    for key, pattern in geometries.items():
        for m in re.finditer(pattern, normalized):
            add("geometry_class", key, m.span())
    for direction in ("opposed", "concurrent", "coflow", "stagnation"):
        if re.search(rf"\b{direction}\b", normalized):
            add("flow_direction", direction)

    runs, investigations = psi_query.load()
    # Longest first: a blend or a named variant must not turn into its pure fuel.
    fuels = {r["conditions"]["fuel_family"]["value"] for r in runs if r["conditions"].get("fuel_family", {}).get("value")}
    matches: list[tuple[int, int]] = []
    aliases = {"sibal": "SIBAL", **{f: f for f in fuels}}
    for label, canonical in sorted(aliases.items(), key=lambda x: -len(x[0])):
        pattern = rf"(?<![\w/-]){re.escape(label)}(?P<family>\*)?(?![\w/-])"
        for m in re.finditer(pattern, text, re.I):
            if any(m.start() < end and m.end() > start for start, end in matches):
                continue
            matches.append(m.span())
            add("fuel_family", canonical + ("*" if m.group("family") else ""), m.span())

    names = {k: k for k in investigations}
    names.update({i["name"]: k for k, i in investigations.items()})
    names.update({"SAFFIRE": "SAFFIRE", "ACME": "ACME", "BASS 2": "bass-ii", "BASS II": "bass-ii", "FLEX 2": "flex-2"})
    matched_names: list[tuple[int, int]] = []
    for label, canonical in sorted(names.items(), key=lambda x: -len(x[0])):
        pattern = re.escape(label).replace(r"\-", r"[- _]?").replace(r"\ ", r"[- _]?")
        for m in re.finditer(rf"(?<![\w-]){pattern}(?![\w-])", text, re.I):
            if any(m.start() < end and m.end() > start for start, end in matched_names):
                continue
            matched_names.append(m.span())
            add("investigation", canonical, m.span())

    missions = []
    # Merely mentioning the ISS as the experiment platform is not a request
    # for ambient ISS pressure. Presets require a stated environment context.
    def environment(name):
        return bool(re.search(rf"\b(?:near|for|at)\s+(?:the\s+)?(?:proposed\s+)?(?:{name})\b|\b(?:{name})(?:\s+(?:surface|habitat|cabin|mission|ambient))*\s+(?:atmosphere|conditions|environment)\b|\b(?:atmosphere|conditions|environment)\s+(?:(?:of|for|near|at|on)\s+)?(?:the\s+)?(?:{name})\b", normalized))
    if environment("(?:lunar\\s+)?gateway"):
        missions.append("gateway")
    elif environment("lunar|moon|artemis"):
        missions.append("lunar")
    if environment("iss|international space station"):
        missions.append("iss")
    if len(missions) > 1:
        result.errors.append("Multiple mission atmospheres were named; choose one atmosphere or explicit conditions.")
    elif missions:
        result.atmosphere = missions[0]
        for key, value in psi_atmospheres.query_for(missions[0]).items():
            result.query.setdefault(key, value)  # Explicit numeric targets override a cited preset.
    if re.search(r"\b(?:mars|martian|spacesuit|rover)\b", normalized) and not any(k in result.query for k in ("o2_pct", "pressure_atm")):
        result.errors.append("This context has no cited numerical atmosphere preset; state explicit conditions or use unconstrained Explorer browsing.")
    if re.search(rf"\b{OXYGEN}\b", normalized) and "o2_pct" not in result.query and re.search(rf"\b(?:at|near)\s+\S+\s+{OXYGEN}\b|{OXYGEN}\s*(?:is|at|of|=|:)\s*\S+", normalized):
        result.errors.append("An oxygen condition was mentioned but its percentage could not be interpreted; state it with % or percent.")
    material_phrase = re.search(r"\b(?:find|show|list|search for)\s+([\w*/ ()-]+?)\s+(?:tests|runs|records)\b", normalized)
    if material_phrase and not any(k in result.query for k in ("fuel_family", "geometry_class", "investigation")):
        words = set(material_phrase.group(1).split())
        if words - {"all", "the", "relevant", "matching", "combustion", "microgravity", "available", "indexed", "individual"}:
            result.errors.append("The requested material or investigation was not recognized; no broader condition-only lookup was inferred.")

    consumed.extend(m.span() for m in re.finditer(r"\bo2\b", normalized))
    for m in re.finditer(NUMBER, normalized):
        if not any(start <= m.start() and end >= m.end() for start, end in consumed):
            result.errors.append("A number or its units could not be assigned to a supported condition. Use oxygen %, pressure atm/kPa/psi, or flow cm/s, mm/s or m/s.")
            break
    for key in ("o2_pct", "pressure_atm", "flow_cm_s"):
        if key in result.query:
            n = result.query[key]
            if (key == "o2_pct" and not 0 <= n <= 100) or (key == "pressure_atm" and n <= 0) or (key == "flow_cm_s" and n < 0):
                result.errors.append(f"Requested {key} is outside its physical range.")
    if not result.query:
        result.errors.append("No supported explicit condition, fuel, investigation or named atmosphere was recognized. Restate the request or use the Explorer.")
    return result


def bind_query(text: str, proposed: dict) -> tuple[RequestIntent, list[str]]:
    intent = parse_request(text)
    corrections = [key for key in QUERY_KEYS if proposed.get(key) != intent.query.get(key)]
    # An unrecognized model fuel could reflect a real, unsupported user material.
    # Do not discard that material and accidentally execute a broader query.
    if proposed.get("fuel_family") and "fuel_family" not in intent.query:
        intent.errors.append("The requested material could not be bound to an explicit recognized fuel identity; no broader query was run.")
    return intent, corrections
