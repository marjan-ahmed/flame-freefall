"""Comparison-card tool: the model's alternative to prose when a question
spans 2+ investigations.

Both research reports in the repo root (chatgpt-generated-reseach-report.txt,
claude-generated-research-report.md) converge on the same root problem this
corpus exists to address: researchers don't struggle to find BASS-II or
SAFFIRE data, they struggle to compare across investigations, because each
one reports flame spread rate, O2%, pressure, gravity and geometry in its
own narrative document with no shared schema — Liao's own NASA grant is
literally a person hand-building that comparison table. This renders it
instead, on demand.

Widget classes here (Card, Row, Col, Title, Text, Caption, Badge) are
flagged deprecated in openai-chatkit in favor of authoring a .widget file at
https://widgets.chatkit.studio/ and loading it via WidgetTemplate — the
newer, visually-designed path. Direct class usage still works (deprecated,
not removed) and needs no external tool, so it's what's used here; redoing
this visually in ChatKit Studio is a reasonable later upgrade, not a
correctness issue.
"""

from agents import RunContextWrapper, function_tool
from chatkit.agents import AgentContext
from chatkit.widgets import Badge, Caption, Card, Col, Row, Title

from pydantic import BaseModel, Field, field_validator


class InvestigationFact(BaseModel):
    name: str = Field(description="Investigation name, e.g. 'BASS-II' or 'SAFFIRE-I'")
    geometry_class: str = Field(description="e.g. 'solid-fuel', 'droplet-combustion', 'gaseous-flames'")
    flame_spread_rate: str = Field(default="—", description="With units, e.g. '0.45 mm/s'")
    oxygen_pct: str = Field(default="—", description="e.g. '21%'")
    pressure: str = Field(default="—", description="e.g. '101 kPa'")
    gravity: str = Field(default="—", description="e.g. 'microgravity', 'Lunar (1/6 g)'")
    citation: str = Field(default="—", description="Short source reference, e.g. document slug or heading")

    # Pydantic's `default="—"` only applies when the model OMITS a field —
    # smaller models (the HF fallback tier especially) pass explicit empty
    # strings instead, which Pydantic accepts as a valid value, so the
    # widget rendered fully blank in practice (confirmed live 2026-09-22).
    # Coerce blank/whitespace-only input to the same placeholder here.
    @field_validator(
        "geometry_class", "flame_spread_rate", "oxygen_pct", "pressure", "gravity", "citation",
        mode="before",
    )
    @classmethod
    def _blank_to_dash(cls, value: str) -> str:
        if value is None or not str(value).strip():
            return "—"
        return value


@function_tool(
    description_override=(
        "Render a structured side-by-side comparison card instead of prose. Use this "
        "whenever the user asks to compare 2 or more investigations (flame spread rate, "
        "oxygen %, pressure, gravity, geometry). Gather the facts via search/read FIRST, "
        "then call this with what you found — never invent a value; use '—' for anything "
        "the record doesn't state."
    )
)
async def show_comparison(
    ctx: RunContextWrapper[AgentContext],
    investigations: list[InvestigationFact],
) -> str:
    for inv in investigations:
        print(f"[show_comparison] {inv.model_dump()}")
    columns = [
        Col(
            gap=1,
            flex=1,
            minWidth=160,
            children=[
                Title(value=inv.name, size="sm"),
                Badge(label=inv.geometry_class, color="secondary", size="sm"),
                Caption(value=f"Spread rate: {inv.flame_spread_rate}"),
                Caption(value=f"O₂: {inv.oxygen_pct}"),
                Caption(value=f"Pressure: {inv.pressure}"),
                Caption(value=f"Gravity: {inv.gravity}"),
                Caption(value=inv.citation, color="tertiary"),
            ],
        )
        for inv in investigations
    ]

    widget = Card(
        children=[
            Title(value="Investigation comparison"),
            Row(gap=3, wrap="wrap", children=columns),
        ]
    )
    await ctx.context.stream_widget(widget)
    return "Comparison card rendered — do not repeat these facts in prose, just add a one-line takeaway."
