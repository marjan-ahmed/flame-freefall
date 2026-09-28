<p align="center">
  <img src="system/site/app/icon.png" width="88" alt="Flame in Freefall" />
</p>

<h1 align="center">Flame Freefall</h1>

<p align="center">
  Fire behaves differently without gravity — and the atmospheres proposed for the Moon and
  the Lunar Gateway are more flammable than anything NASA certifies materials against today.
  This turns two decades of NASA's microgravity combustion data into a governed, citation-backed
  record that shows exactly where the evidence reaches, where it doesn't, and what NASA's own
  documents say those gaps mean for crew safety.
</p>

<p align="center">
  <a href="https://github.com/marjan-ahmed/flame-freefall/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/marjan-ahmed/flame-freefall/actions/workflows/validate.yml/badge.svg" /></a>
  <a href="https://github.com/marjan-ahmed/flame-freefall/actions/workflows/deploy-pages.yml"><img alt="Deploy" src="https://github.com/marjan-ahmed/flame-freefall/actions/workflows/deploy-pages.yml/badge.svg" /></a>
  <img alt="NASA Space Apps 2026" src="https://img.shields.io/badge/NASA%20Space%20Apps-2026-0B3D91" />
  <img alt="License: none asserted" src="https://img.shields.io/badge/knowledge-governed-1d4ed8" />
</p>

<p align="center">
  <strong><a href="https://marjan-ahmed.github.io/flame-freefall/">Open the dashboard →</a></strong>
  &nbsp;·&nbsp;
  <a href="https://marjan-ahmed.github.io/flame-freefall/docs/">Browse the governed record →</a>
</p>

---

<!-- Dashboard screenshot: system/site/app/(home)/page.tsx after `npm run build` —
     the coverage heatmaps and mission-readiness cards, above the chat. -->
<p align="center">
  <em>The home page leads with this: where the data reaches (a coverage heatmap per
  geometry class, O₂ × pressure), and whether it reaches the atmospheres proposed for
  the ISS, the Lunar Gateway and a Lunar surface habitat — before anyone types a
  question.</em>
</p>

## Why this matters

Spacecraft materials are certified today (NASA-STD-6001B) at 20.9% O₂ and 1
atmosphere. The atmospheres NASA has proposed for exploration missions run as high
as 34% oxygen at reduced pressure — and NASA's own decadal-survey papers say plainly
that "the new exploration atmospheres of up to 34% oxygen will likely require the
retest of many materials." This project doesn't just store that sentence — it puts a
number next to it: for the Lunar-habitat atmosphere, **solid-fuel combustion data
covers zero tests**, while gaseous-flame data covers dozens, computed live from the
1,948-record test table, not asserted.

Ask it a question and it ranks materials by a measured result within one comparable
class ("which solid fuels spread fastest near a Lunar atmosphere?"), shows exactly
which mission atmospheres the evidence reaches, and cites the PSI table line or NASA
report behind every number — never the model's own words. This generalizes past
combustion, too: the same governed-corpus-plus-computed-coverage pattern applies to
any NASA PSI domain, and the same certification question (does ground-test data
cover the atmosphere a mission will actually use?) applies anywhere materials are
qualified for an oxygen-enriched environment — hyperbaric medicine and submarines
included, not just spacecraft.

## What this is

Three things, built as one product:

- **A unified test-run table.** 20 PSI experimental tables from 19 investigations,
  normalized into 1,948 records (1,400 individual tests, 435 SPICE test points, and
  daily summaries, per-fuel summaries and planned envelopes). The original cell is
  kept beside every normalized value. 433 records are cross-checked against NASA
  report tables. The 8 cases where a PSI table and a report disagree are flagged, with
  both values kept, never silently resolved.
- **A System of Record.** `knowledge/` holds 20 governed markdown documents covering
  every investigation, report, table and workbook. Every number in them is checked
  against its source's text, gaps are recorded as open questions rather than filled by
  inference, and nothing publishes without a `draft → stable` approval carrying a named
  approver and a timestamp.
- **A research assistant and a dashboard.** The home page opens on a coverage
  heatmap and mission-readiness cards — computed, glanceable, no typing needed —
  above a full-screen chat that answers only through tools, never from the model's
  own training data. Test-data questions render **interactive widgets**: an evidence
  list, a gap map, a **ranking** of materials by a measured result, a **mission
  readiness** view, a side-by-side comparison, per-test details and results charts.
  Narrative questions go to the governed record over the
  [Model Context Protocol](https://modelcontextprotocol.io).

> [!NOTE]
> This is not a wrapped LLM with a system prompt telling it to "be accurate." Every
> number on screen — in the dashboard, in a ranking, in a mission-readiness card, in
> an evidence list — comes from the data or a verbatim-checked quote from a governed
> document; the model only writes a short summary of what a tool returned and is told
> never to retype or merge values. An empty result ("no test at these conditions", "no
> data near this atmosphere") is shown as an answer, not papered over. A ranking is
> computed in code (median, min–max, every contributing run id) and never invented by
> the model; a mission-readiness finding is a citation checked verbatim against its
> source document by an automated test, not free text. Citations and abstentions work
> the same way: a source link is built straight from a tool's own JSON and streamed
> independently of the model's prose, and a genuinely failed lookup forces the "I
> can't check that right now" reply in code — so a weaker or unlucky model call can't
> cite a source, a run id, or a ranking that was never actually returned.

## For NASA researchers

- **The dashboard, first.** Coverage heatmaps (O₂ × pressure) per geometry class,
  with the ISS, Lunar Gateway and Lunar-habitat atmospheres marked on them, and
  mission-readiness cards showing which classes are covered near each — all computed
  at build time from the run table, none of it typed in by hand.
- Ask by conditions: *"What do all the experiments say about PMMA burning at 15% O₂
  with a 10 cm/s flow?"* The answer is in tiers:
  - **At conditions**: every test that reports all of your conditions within tolerance.
  - **Partial**: tests that match what they report but are silent on one of your
    conditions (e.g. BASS-II rod tests at ~15% O₂ whose flow isn't recorded in cm/s).
  - **Nearest**: the closest remaining tests, with what each one measured.
- **Rank materials** within one geometry class by a measured result — flame spread
  rate, burning-rate constant, extinction diameter, burn time, peak burner
  temperature — highest or lowest first, at conditions you state or a named mission
  atmosphere (`iss`, `gateway`, `lunar`). Every row keeps its n, median, range and
  every contributing run id; materials never tested at those conditions are listed,
  not silently dropped. Never ranks across geometry classes — a solid and a droplet
  are not comparable in kind.
- **Mission readiness**: for a named atmosphere, how many tests exist near it in each
  geometry class, the nearest tested conditions if none do, and a verbatim quote from
  the governed record on why that gap matters where one exists.
- **Gap map**: a grid of O₂ × flow (or pressure) bands, shaded by how many tests were
  run in each cell. Empty cells are conditions nobody has tested; your target is
  outlined.
- **Compare investigations**: one column per investigation, showing the O₂, flow and
  pressure ranges it covered, whether your target falls inside them, and the range of
  its measured results.
- **Details** on any test: every condition with its original cell, every result, and
  its sources (PSI file and line, or NASA report table and page).
- **Results chart**: e.g. flame spread rate against flow, one line per test that swept
  its flow.
- Narrative questions (*"What does NASA-STD-6001B require?"*) are answered from the
  governed record with citations. The chat header links to the **System of Record** and
  the **Test-data explorer**, a browsable page for the same data.

## For evaluators and judges

- **[Try it live](https://marjan-ahmed.github.io/flame-freefall/)** — no setup, no
  login. The dashboard is the first thing you see.
- What's actually novel isn't the chat UI. It's four things:
  - **The data.** 19 investigations' tables normalized into one queryable record,
    with the raw cell kept beside every value.
  - **Honest answers.** Match, partial and near tiers with explicit coverage gaps, so
    "nobody has tested this" is an answer, and source disagreements are shown, not
    hidden.
  - **Ranking and readiness, computed, not asserted.** A material ranking is a
    median over every contributing run, not a guess; a mission-readiness gap is a
    match/partial count of zero, not a feeling — and the "why it matters" text beside
    it is a citation, checked against its source by a test, never generated.
  - **Architecture over prompting.** The assistant can't state a number the data
    didn't return, because numbers live in the widgets, not in the model's prose.
    The same rule holds for citations, gaps, rankings and abstentions — enforced in
    code against every reply, not left to an instruction the model might ignore.
- The corpus carries a formal governance model (audiences, approval authorities, an
  append-only takedown ledger) that a wiki or a shared doc doesn't have.
- Three independently deployed services, wired together over HTTP and MCP — see
  [Architecture](#architecture) below.

## For developers

Tech stack, local setup, and the full architecture are below. The deep governance
and content-authoring rules this record runs on live in [`AGENTS.md`](./AGENTS.md) —
every coding agent working in this repository reads that file first.

---

## Architecture

```
                          reader / researcher
                                  │
                                  ▼
                 ┌──────────────────────────────────┐
                 │  GitHub Pages — static export      │   Next.js 16 · React 19
                 │  marjan-ahmed.github.io/            │   dashboard, ChatKit UI, record pages,
                 │  flame-freefall/                    │   /explore (same query, in-browser)
                 └────────────────┬─────────────────┘
                                  │ POST /chatkit  (messages + widget button actions)
                                  ▼
                 ┌──────────────────────────────────┐    data/runs.json ◄── system/psi-ingest ◄── psi-data/raw
                 │  Vercel — chat backend             │    (1,948 PSI test   (normalize, join       (20 PSI tables,
                 │  flame-freefall-site.vercel.app    │     records)          report tables,         reports,
                 │  FastAPI · openai-agents SDK       │                       verify extractions)    workbooks)
                 │  gpt-oss → qwen → HF fallback      │
                 │  7 PSI tools → ChatKit widgets     │
                 └────────────────┬─────────────────┘
                                  │ MCP: search · read  (narrative questions)
                                  ▼
                 ┌──────────────────────────────────┐
                 │  Vercel — MCP door (ksor serve)    │   Node.js · @panaversity/ksor
                 │  flamefreefall-sor.vercel.app       │   cited retrieval, abstention gate
                 └────────────────┬─────────────────┘
                                  │ pgvector similarity search
                                  ▼
                 ┌──────────────────────────────────┐
                 │  Neon Postgres + pgvector           │   the ingested, embedded corpus
                 └──────────────────────────────────┘
                                  ▲
                                  │ ksor ingest (offline, from source)
                 ┌──────────────────────────────────┐
                 │  knowledge/  — the governed record  │   20 documents, plain markdown
                 └──────────────────────────────────┘
```

Three separately deployed, independently scalable services instead of one bundled
app — deliberately: the static site costs nothing to serve, and each backend
service redeploys and fails independently of the others. See
[Deployment](#deployment) for why it landed on this particular split.

## Features

- **A computed dashboard, not a mockup.** The home page's coverage heatmaps and
  mission-readiness cards are server-rendered at build time from
  `psi-data/derived/*.json`, using the exact same query algorithm (`query()`,
  TypeScript-twinned and golden-fixture-pinned) the chat and Explorer use — not a
  third, drifting reimplementation.
- **Ranking, computed in code.** `psi_query.rank()` aggregates every match/partial
  run's measured value per material (n, min, median, max, every contributing run id)
  within one geometry class, at conditions you state or a named mission atmosphere.
  A TypeScript twin backs an Explorer ranking view; golden fixtures pin both to
  identical output.
- **Mission readiness, cited.** `psi_query.readiness()` computes match/partial/near
  coverage per geometry class near a named atmosphere (ISS, Lunar Gateway, Lunar
  surface habitat — each preset's O₂ %/pressure copied from a governed document and
  checked verbatim by a test); `psi-data/findings.yaml` pairs a gap with a verbatim
  quote from the governed record on why it matters, also checked verbatim by a test.
- **Governed knowledge, not a wiki.** Every document carries `draft`/`stable`
  status, a named approver, and provenance (`generated.by`, `generated.at`).
  Withdrawals go through an append-only ledger a door checks on every request.
- **Cited, tool-grounded retrieval.** The assistant calls `search`/`read` over MCP;
  the chat UI shows each tool call live (name, arguments, status) as it happens —
  nothing is hidden behind a spinner.
- **One table of every test, queried by conditions.** `system/psi-ingest`
  normalizes 20 NASA PSI experimental tables (19 investigations) into 1,948
  records — 1,400 individual tests, 435 SPICE test points, 100 daily summaries,
  5 per-fuel report summaries, 8 planned envelopes — keeping the original cell
  beside every normalized value.
  Ask for "15 % O₂, 10 cm/s, PMMA" and get the tests run there, the tests that
  report only some of those conditions, the nearest tests, and which
  investigations never covered the target. An empty match is an answer, not a gap
  papered over.
- **Cross-checked against NASA reports.** 433 records carry report data: per-test
  tables the governed documents reproduce (BASS-II Tables 5.1 and 7.1, Saffire
  Table I and IV–VI, FLEX Table IX), plus values extracted straight from the
  converted report PDFs (`uv run psi-extract`: BASS-II Appendix A flow direction
  and observations for all 126 tests, SPICE smoke-point ranges per fuel, SAME-R
  sample temperatures). Every extracted value is checked verbatim against the
  report text before it is used. Where the PSI table and a report disagree
  (8 cases, e.g. Saffire-1 thickness 0.37 cm vs 0.37 mm), both values are kept
  and flagged — never silently resolved.
- **Evidence in widgets, not generated numbers.** Seven tools render ChatKit
  widgets: evidence list, gap map, ranking, mission readiness, side-by-side
  comparison, test details and results chart. Every value carries its PSI file line
  or report table, and the model only writes a short summary around it. Widget
  buttons ("Gap map", "Compare investigations", "Details"…) are answered by the
  server directly, with no model call. The static **Test-data explorer**
  (`/explore`) runs the same query in the browser; a TypeScript twin of the Python
  query and ranking logic is held to the same golden test cases.
- **Resilient by design.** Multi-provider LLM fallback (two Groq-hosted models,
  then Hugging Face) on rate limits, a temporarily unreachable MCP door
  degrades the assistant to "I can't look that up right now" instead of
  crashing the chat, and a single failed search/read call mid-conversation
  forces that same honest abstention in code — the model's own text is
  overridden, never left to answer from training knowledge instead. If every
  provider is exhausted at once, the chat says so plainly instead of showing a
  raw error.
- **File attachments, conversation history, auto-titled threads.**

## The corpus

| Geometry class | Investigations | Documents |
| --- | --- | --- |
| Solid fuel | BASS-II, SAFFIRE (incl. Saffire VI), BASS, BASS-II requirements | `knowledge/investigations/solid-fuel/` |
| Droplet combustion | FLEX, FLEX-2, CFI | `knowledge/investigations/droplet-combustion/` |
| Gaseous flames | ACME, ACME BRE, ACME s-Flame, SPICE | `knowledge/investigations/gaseous-flames/` |
| Smoke / aerosol *(heated, non-burning samples)* | SAME, SAME-R | `knowledge/investigations/smoke-aerosol/` |
| Foundations *(no geometry class, narrative context)* | NASA-STD-6001B; Liao, Miller and "Thriving in Space" (decadal-survey research priorities) | `knowledge/foundations/` |
| Data sources *(no geometry class)* | the PSI archive, all 20 experimental tables, the summary and matrix workbooks | `knowledge/data-sources/` |

Folder layout encodes comparability: two investigations are only honestly
comparable if they share a geometry class, so that's how the record is organized,
not by publication date or program name — and it's the same rule the ranking
feature enforces in code, never ranking across classes.

All 20 documents are approved (`stable`) and published on the site, each with a
summary tab. Together they cite every report, table and workbook in
`psi-data/raw/`, and every number in them has been checked against its source's
text. The 12 approved on 2026-09-24 (BASS, BASS-II requirements, FLEX-2, CFI, ACME
BRE, ACME s-Flame, SPICE, SAME, SAME-R and the three data-sources documents) are not
yet marked as human-verified, the page-by-page quote check the original 8 carry.

The chatbot's narrative search (the MCP door) still holds only the original 8
documents. Running `npm run refresh` ingests the other 12. The test-data tools
don't depend on it: they already cite the new documents for SPICE, SAME, SAME-R,
CFI, FLEX-2, ACME BRE and ACME s-Flame.

The test data itself lives in `psi-data/`, which has its own
[README](psi-data/README.md): `raw/` holds the files exactly as downloaded from PSI,
`derived/` the generated run table, report extractions and inventory, `extracted/`
the report values pulled per test, and `findings.yaml` the governed-doc quotes the
mission-readiness view cites.

## Deployment

| Service | Host | Why |
| --- | --- | --- |
| Site (static export) | GitHub Pages | Free, zero-config for a pure static export. |
| Chat backend (FastAPI) | Vercel | Native `pyproject.toml`/`uv.lock` support; serverless fits a request-scoped LLM call. |
| MCP door (`ksor serve`) | Vercel *(container runtime)* | Fly.io and Render both gate free accounts behind a card; Vercel's `services`/container runtime doesn't, and ksor's own deploy guide names Vercel as a supported target. |
| Corpus store | Neon (Postgres + pgvector) | Managed, scales to zero, free tier includes pgvector. |

Verify any of the three independently, the same way the [ksor deploy
guide](https://github.com/panaversity/ksor) recommends:

```sh
curl https://flame-freefall-site.vercel.app/health     # chat backend
curl https://flamefreefall-sor.vercel.app/health       # MCP door
curl https://flamefreefall-sor.vercel.app/ready        # door ↔ database
```

## Quick start — local development

```sh
npm install
npm run dev              # the record, at http://localhost:3000
```

```sh
cd system/psi-ingest
uv run psi-extract       # converted report text → psi-data/extracted/report-outcomes.csv (verbatim, paged)
uv run psi-ingest        # psi-data/raw + knowledge/ + extracted → psi-data/derived/*.json (and the copilot's copy)
uv run pytest            # ingest invariants: every row accounted for, every value keeps its raw cell
```

```sh
cd system/chatkit-server
uv sync
uv run uvicorn main:app --reload --port 8000    # the chat backend
GROQ_API_KEY=dummy uv run pytest                # query, ranking, readiness + widget tests (no network)
```

For local narrative answers, start the Sentence Transformers service before
refreshing the record, then start the KSOR door before ChatKit. The chatbot's
`HANDBOOK_MCP_URL` defaults to `http://127.0.0.1:8080/mcp`:

```powershell
cd system/sentence-transformers
uv sync --extra model
uv run uvicorn server:app --host 127.0.0.1 --port 8001
```

In another terminal, run `npm run refresh` and `npm run serve` from the repo
root, then start the ChatKit backend above. Local KSOR npm scripts select the
dedicated Sentence Transformers database automatically.

```sh
npm --prefix system/site run test:psi           # the in-browser query/ranking matches the Python one
npm run check                                   # the record's format checker (what CI runs)
```

```sh
npm run provision        # once: schema + grant
npm run refresh          # publish the record; requires Sentence Transformers below
npm run serve             # the MCP door, at http://localhost:8080
```

The governed-record embeddings use a local Sentence Transformers model, not a
Gemini or OpenAI embedding API. Start the embedding service before refreshing
or serving the MCP door. Local npm KSOR commands target the dedicated
`flame_freefall_sentence_transformers` database derived from `KSOR_DB_URL`,
leaving any existing embedding database untouched. Setup details are in
[`system/sentence-transformers/README.md`](system/sentence-transformers/README.md).

Each layer needs `.env` filled in — copy `.env.example` and see the comments
inline; the chat backend additionally reads a Groq (and optionally Hugging Face)
API key. The full runbook — governance model, writing and approving knowledge,
troubleshooting table — is in [`AGENTS.md`](./AGENTS.md).

## Built with

Next.js · React · [OpenAI ChatKit](https://openai.github.io/chatkit-js/) · FastAPI ·
[openai-agents SDK](https://github.com/openai/openai-agents-python) ·
[Model Context Protocol](https://modelcontextprotocol.io) · Groq · Hugging Face ·
[ksor](https://github.com/panaversity/ksor) · Neon (Postgres + pgvector) · Vercel ·
GitHub Pages.

Built for NASA Space Apps Challenge 2026, "Flame in Freefall" track.
