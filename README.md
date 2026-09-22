<p align="center">
  <img src="system/site/app/icon.png" width="88" alt="Flame in Freefall" />
</p>

<h1 align="center">Flame Freefall</h1>

<p align="center">
  A governed, citation-backed record of NASA's microgravity combustion research —
  and an AI assistant that answers only from it, and says so when it can't.
</p>

<p align="center">
  <a href="https://github.com/marjan-ahmed/flame-freefall/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/marjan-ahmed/flame-freefall/actions/workflows/validate.yml/badge.svg" /></a>
  <a href="https://github.com/marjan-ahmed/flame-freefall/actions/workflows/deploy-pages.yml"><img alt="Deploy" src="https://github.com/marjan-ahmed/flame-freefall/actions/workflows/deploy-pages.yml/badge.svg" /></a>
  <img alt="NASA Space Apps 2026" src="https://img.shields.io/badge/NASA%20Space%20Apps-2026-0B3D91" />
  <img alt="License: none asserted" src="https://img.shields.io/badge/knowledge-governed-1d4ed8" />
</p>

<p align="center">
  <strong><a href="https://marjan-ahmed.github.io/flame-freefall/">Try the assistant →</a></strong>
  &nbsp;·&nbsp;
  <a href="https://marjan-ahmed.github.io/flame-freefall/docs/">Browse the governed record →</a>
</p>

---

## The problem

NASA's microgravity combustion program has run BASS-II, SAFFIRE, FLEX, and ACME as
separate investigations, each reporting flame spread rate, oxygen concentration,
pressure, gravity level, and burn geometry in its own narrative PDF — with no shared
schema between them. Nothing is missing; it just isn't comparable without a person
re-reading four documents and re-typing the numbers into one table by hand. That work
already happens today, inside active NASA-funded research.

This project turns that comparison into a five-second chat message, and keeps every
number traceable back to the sentence it came from.

## What this is

Two things, built as one product:

- **A System of Record.** `knowledge/` holds eight governed markdown documents — every
  numeric claim traces to a verbatim quote from its source PDF, gaps are recorded as
  open questions rather than filled by inference, and nothing publishes without a
  `draft → stable` approval carrying a named approver and a timestamp.
- **A research assistant.** A full-screen chat interface that answers exclusively by
  calling tools against that record over the [Model Context Protocol](https://modelcontextprotocol.io) —
  never from the model's own training data — and renders a structured side-by-side
  card instead of prose the moment a question compares two or more investigations.

> [!NOTE]
> This is not a wrapped LLM with a system prompt telling it to "be accurate." The
> assistant has no access to the corpus text at all until it calls a tool; what it
> can say is bounded by what that tool call returns.

## For NASA researchers

- Ask in plain language — *"What did BASS-II find about flame spread over solid
  fuel?"* — and get an answer with its source cited.
- Ask a comparison question and get a table (spread rate, O₂%, pressure, gravity,
  geometry) instead of four PDFs to cross-reference yourself.
- Every answer traces back to a document you can open and verify — the **"System of
  Record"** link in the chat header goes straight to the governed corpus.

## For evaluators and judges

- **[Try it live](https://marjan-ahmed.github.io/flame-freefall/)** — no setup, no
  login.
- What's actually novel here isn't the chat UI — it's that the assistant is
  *architecturally* incapable of answering from anywhere but the governed record: no
  MCP tool result, no fact. The corpus itself carries a formal governance model
  (audiences, approval authorities, an append-only takedown ledger) that a wiki or a
  shared doc doesn't have.
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
                 │  marjan-ahmed.github.io/            │   ChatKit UI + record pages
                 │  flame-freefall/                    │
                 └────────────────┬─────────────────┘
                                  │ POST /chatkit
                                  ▼
                 ┌──────────────────────────────────┐
                 │  Vercel — chat backend             │   FastAPI · openai-agents SDK
                 │  flame-freefall-site.vercel.app    │   Groq (gpt-oss-120b), HF fallback
                 └────────────────┬─────────────────┘
                                  │ MCP: search · read · show_comparison
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
                 │  knowledge/  — the governed record  │   8 documents, plain markdown
                 └──────────────────────────────────┘
```

Three separately deployed, independently scalable services instead of one bundled
app — deliberately: the static site costs nothing to serve, and each backend
service redeploys and fails independently of the others. See
[Deployment](#deployment) for why it landed on this particular split.

## Features

- **Governed knowledge, not a wiki.** Every document carries `draft`/`stable`
  status, a named approver, and provenance (`generated.by`, `generated.at`).
  Withdrawals go through an append-only ledger a door checks on every request.
- **Cited, tool-grounded retrieval.** The assistant calls `search`/`read` over MCP;
  the chat UI shows each tool call live (name, arguments, status) as it happens —
  nothing is hidden behind a spinner.
- **Cross-investigation comparison, structured.** Ask to compare two or more
  investigations and a purpose-built widget renders the facts side by side; the
  model is instructed to never fake this with a markdown table.
- **Resilient by design.** Multi-provider LLM fallback (Groq → Hugging Face) on
  rate limits, and a temporarily unreachable MCP door degrades the assistant to
  "I can't look that up right now" instead of crashing the chat.
- **File attachments, conversation history, auto-titled threads.**

## The corpus

| Geometry class | Investigations | Documents |
| --- | --- | --- |
| Solid fuel | BASS-II, SAFFIRE (incl. Saffire VI) | `knowledge/investigations/solid-fuel/` |
| Droplet combustion | FLEX | `knowledge/investigations/droplet-combustion/` |
| Gaseous flames | ACME | `knowledge/investigations/gaseous-flames/` |
| Foundations *(no geometry class — narrative context)* | NASA-STD-6001B; Liao, Miller and "Thriving in Space" (decadal-survey research priorities) | `knowledge/foundations/` |

Folder layout encodes comparability: two investigations are only honestly
comparable if they share a geometry class, so that's how the record is organized —
not by publication date or program name.

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
cd system/chatkit-server
uv sync
uv run uvicorn main:app --reload --port 8000    # the chat backend
```

```sh
npm run provision        # once: schema + grant
npm run refresh          # publish the record
npm run serve             # the MCP door, at http://localhost:8080
```

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
