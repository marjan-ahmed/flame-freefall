"""Per-turn determinism state, collapsed into one deep module instead of
three ad-hoc attributes (_cited_stable_ids, _tool_failure, _query_run_ids)
bolted onto chatkit's AgentContext from different files -- see AGENTS.md's
"Not everything belongs in the system prompt" rule for why this state exists
at all, and the architecture review (candidate 1) for why it was collapsed.

Plain Python, no chatkit/agents SDK imports: constructible and testable
without a real AgentContext/ThreadMetadata/store."""

from __future__ import annotations

import re

# The exact citation format psi_tools.py's _reply() tells the model to use:
# "(PSI-25:M18)" -- a full run id in parentheses.
_CITED_RUN_ID_RE = re.compile(r"\(PSI-\d+:[A-Za-z0-9._-]+\)")


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
        """Run ids the model cited in `text` that do NOT appear in any
        query_test_runs payload from this turn -- fabrications. Empty set
        if no query_test_runs ran, or nothing was fabricated."""
        if not self._valid_run_ids:
            return set()
        cited = {m[1:-1] for m in _CITED_RUN_ID_RE.findall(text)}
        return cited - self._valid_run_ids
