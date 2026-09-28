"""Per-turn determinism state, collapsed into one deep module instead of
three ad-hoc attributes (_cited_stable_ids, _tool_failure, _query_run_ids)
bolted onto chatkit's AgentContext from different files -- see AGENTS.md's
"Not everything belongs in the system prompt" rule for why this state exists
at all, and the architecture review (candidate 1) for why it was collapsed.

Plain Python, no chatkit/agents SDK imports: constructible and testable
without a real AgentContext/ThreadMetadata/store."""

from __future__ import annotations

import re
from functools import lru_cache

import psi_query  # ground truth for id shapes and value-sanity checks --
# plain data (no chatkit/agents import), same as every other module here.

# The citation format psi_tools.py's _reply() tells the model to use: a full
# run id in parentheses, e.g. "(PSI-25:M18)". Real ids are NOT all "PSI-<n>:"
# shaped (saffire-iv-vi:IV-1, flex:..., spice:...), can contain spaces, '#',
# and one level of nested parentheses (PSI-68:IsoOctane (pure)), and the live
# model sometimes typesets the hyphen as a Unicode look-alike (U+2010-2015,
# U+2212) rather than ASCII '-'. A regex anchored to "PSI-\d+:[\w.-]+" alone
# missed 1096 of 1948 real ids for exactly these reasons -- a fabrication in
# any of those shapes was never even inspected, let alone flagged.
_NONASCII_HYPHENS = re.compile("[‐‑‒–—―−]")
# One outer parenthetical, allowing exactly one level of nested parens inside
# it (covers every real id's own nesting depth; see test coverage).
_PAREN_RE = re.compile(r"\(((?:[^()]|\([^()]*\))*)\)")
# A candidate id: an investigation-style prefix (PSI-<digits>, or a lowercase
# hyphenated slug like "flex"/"spice"/"saffire-iv-vi") + ':' + anything.
_ID_SHAPE_RE = re.compile(r"(?:PSI-\d+|[a-z][a-z0-9-]*):.+", re.DOTALL)
# A number immediately followed by a unit token -- used to find a stated
# measurement next to a citation, never a bare digit (which could be part of
# the run id's own label, a table/page number, etc.).
_VALUE_UNIT_RE = re.compile(
    r"(-?\d+(?:\.\d+)?)\s*(mm/s|cm/s|m/s|mm|cm|m|°c|ppm|%|w|atm|kpa|psia|k)\b", re.IGNORECASE)


def _split_top_level(s: str, sep: str) -> list[str]:
    """Split on `sep` characters that are not inside a nested (...) group --
    so "PSI-25:M18, PSI-25:M99" splits in two but "PSI-68:IsoOctane (pure)"
    (no top-level separator) does not split on the comma that would exist
    inside a *different* nested group elsewhere."""
    parts, depth, cur = [], 0, []
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts


def _window_before(text: str, idx: int, maxlen: int = 60) -> str:
    """Up to `maxlen` characters before `idx`, cut short at an earlier ')' so
    a value stated next to a DIFFERENT, earlier citation is never picked up
    as belonging to this one."""
    w = text[max(0, idx - maxlen):idx]
    last_close = w.rfind(")")
    return w[last_close + 1:] if last_close != -1 else w


@lru_cache(maxsize=1)
def _run_index() -> dict[str, dict]:
    runs, _ = psi_query.load()
    return {r["id"]: r for r in runs}


def _run_numeric_values(run: dict) -> set[float]:
    """Every number genuinely true of this run -- every condition's and every
    outcome's value/min/max/values -- the full set a correctly-stated number
    should land in. Ground truth read straight from data/runs.json, not from
    whatever happened to be in this turn's tool payload, so this catches a
    wrong value even where the id itself is real and was truly shown."""
    out: set[float] = set()

    def take(m: object) -> None:
        if not isinstance(m, dict):
            return
        for k in ("value", "min", "max"):
            v = m.get(k)
            if isinstance(v, (int, float)):
                out.add(round(float(v), 6))
        for v in m.get("values") or []:
            if isinstance(v, (int, float)):
                out.add(round(float(v), 6))

    for c in run.get("conditions", {}).values():
        take(c)
    for o in run.get("outcomes", []):
        take(o.get("measure"))
    return out


def _matches_any(num: float, truth: set[float]) -> bool:
    return any(abs(num - t) <= max(1e-6, 0.01 * abs(t)) for t in truth)


class TurnGuard:
    """One instance per chat turn. Every read/write goes through a named
    verb -- no call site needs to know a representation (set vs list,
    getattr defaults, the citation regex) to participate correctly."""

    def __init__(self) -> None:
        self._cited_stable_ids: set[str] = set()
        self._tool_failure: str | None = None
        self._valid_run_ids: set[str] = set()

    # -- citation dedup (main.py's _cite_sources) -------------------------
    def should_cite(self, stable_id: str | None) -> bool:
        """True, and records it, the first time this stable_id is seen this
        turn; False on every repeat, so a source is never cited twice."""
        if not stable_id or stable_id in self._cited_stable_ids:
            return False
        self._cited_stable_ids.add(stable_id)
        return True

    # -- tool-failure guard (ToolCallVisibilityHooks.on_tool_end) ---------
    def record_tool_result(self, tool_name: str, data: dict | None) -> str | None:
        """Classifies a search/read tool's own JSON: a genuine retrieval
        failure vs. success vs. an honest "record doesn't cover this"
        abstention (ok=false, reason="abstained" -- correct behavior, not a
        failure). Mirrors the ksor gateway's SEARCH_OUTPUT/READ_OUTPUT
        shapes: search always carries "ok" and (on failure) "reason" in
        {"abstained","unavailable","unpublished"}; read carries no "ok"
        field at all, so a missing provenance.stable_id is read's own
        failure signal.

        Only the FIRST failure in a turn sticks. Returns the failure reason
        if THIS call is the one that just set it (so the caller can log it
        once), else None."""
        if self._tool_failure:
            return None
        failure = self._classify_failure(tool_name, data)
        if failure:
            self._tool_failure = failure
        return failure

    @staticmethod
    def _classify_failure(tool_name: str, data: dict | None) -> str | None:
        if data is None:
            return f"{tool_name}_unparseable_or_empty"
        if tool_name == "search":
            if data.get("ok") is False and data.get("reason") != "abstained":
                return f"search_{data.get('reason', 'failed')}"
            return None
        if tool_name == "read":
            prov = data.get("provenance")
            if not isinstance(prov, dict) or not prov.get("stable_id"):
                return "read_no_provenance"
            return None
        return None

    def should_override_reply(self) -> str | None:
        """The fixed text to force onto the streamed reply if a search/read
        call genuinely failed this turn, else None."""
        return self._tool_failure

    # -- citation validation (psi_tools.query_test_runs + response guard) --
    def record_valid_run_ids(self, ids: set[str]) -> None:
        self._valid_run_ids |= ids

    @property
    def valid_run_ids(self) -> frozenset[str]:
        return frozenset(self._valid_run_ids)

    def check_citations(self, text: str) -> set[str]:
        """Problems with the model's own citations in `text`: a cited run id
        that does NOT appear in any query_test_runs/show_test_details payload
        from this turn (a fabricated id, returned as the bare id), or a
        number stated immediately before a REAL, cited id that matches
        nothing this run actually reports (returned as "id@number" -- the id
        itself was real, but the value next to it was invented). Empty set
        if no PSI tool ran this turn, or nothing was wrong.

        A citation is any parenthetical whose content looks like
        "<prefix>:<label>" (see _ID_SHAPE_RE) -- ids may contain spaces, '#',
        one level of nested parens, several ids in one parenthetical
        separated by commas, and Unicode hyphen look-alikes, all of which a
        plain "PSI-\\d+:[\\w.-]+" shape would miss."""
        if not self._valid_run_ids:
            return set()
        norm = _NONASCII_HYPHENS.sub("-", text)
        problems: set[str] = set()
        for m in _PAREN_RE.finditer(norm):
            for part in _split_top_level(m.group(1), ","):
                cand = part.strip()
                if not _ID_SHAPE_RE.fullmatch(cand):
                    continue
                if cand not in self._valid_run_ids:
                    problems.add(cand)
                    continue
                run = _run_index().get(cand)
                truth = _run_numeric_values(run) if run else set()
                if not truth:
                    continue
                for num_s, _unit in _VALUE_UNIT_RE.findall(_window_before(norm, m.start())):
                    if not _matches_any(float(num_s), truth):
                        problems.add(f"{cand}@{num_s}")
        return problems
