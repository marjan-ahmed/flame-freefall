# Flame Freefall

Traceable NASA combustion evidence for researchers deciding what to investigate next.
Search by atmosphere, fuel and flow; inspect individual records; export the evidence
and the query that selected it. The deterministic Explorer works without an AI service.

[Live application](https://marjan-ahmed.github.io/flame-freefall/) ·
[Explorer](https://marjan-ahmed.github.io/flame-freefall/explore/) ·
[Governed record](https://marjan-ahmed.github.io/flame-freefall/docs/)

**Code Nashai · Muhammad Marjan Ahmed, solo builder**

[**View the seven-slide project demonstration (PDF)**](docs/presentation/flame-freefall-pitch.pdf) ·
[Editable PowerPoint](docs/presentation/flame-freefall-pitch.pptx) ·
[Slide preview](docs/presentation/contact-sheet.png) ·
[Speaker notes and sources](docs/presentation/README.md)

**Competition eligibility is unresolved.** This project existed before the November
2026 hackathon. Technical improvements are not a claim of eligibility. See
[submission gates and disclosure](SUBMISSION.md). Local changes do not update the
live deployment until published.

<p align="center">
  <strong><a href="https://marjan-ahmed.github.io/flame-freefall/">Open the dashboard</a></strong>
  &nbsp;·&nbsp;
  <a href="https://marjan-ahmed.github.io/flame-freefall/docs/">Browse the governed record</a>
  &nbsp;·&nbsp;
  <a href="https://flamefreefall-sor.vercel.app/mcp">MCP door</a>
  &nbsp;·&nbsp;
  <a href="https://marjan-ahmed.github.io/flame-freefall/explore/">Test-data explorer</a>
  &nbsp;·&nbsp;
  <a href="docs/presentation/flame-freefall-pitch.pdf">Seven-slide project demo (PDF)</a>
    &nbsp;·&nbsp;
  <a href="docs/presentation/flame-freefall-pitch.pptx">Editable pitch deck</a>
</p>

Which indexed experiments overlap the proposed Lunar atmosphere, and how sensitive
is that answer to the search method?

1. Open the Lunar evidence table on the home page. Compare the default search,
   tighter pressure window and wider oxygen window.
2. Inspect direct solid-fuel tests, BRE condensed-fuel emulation, and other gaseous
   flame experiments separately. BRE remains gaseous by physical geometry; its
   scientific role is indirect evidence about condensed fuels.
3. Follow a result to the Explorer. Adjust tolerances and inspect the source table,
   raw condition cells, missing metadata and disagreements.
4. Download the evidence JSON. It includes every matching, incomplete and remaining
   record in the selected categorical scope, source references, query settings,
   method version and dataset SHA-256. It is a research starting point, not a
   validated model-training dataset.

The previous pitch's fixed gaseous-versus-solid counts omitted relevant BRE report
examples and mixed tests with daily summaries. The current case study computes
individual-test counts and displays sensitivity explicitly. The three added BRE
report examples are preliminary and are not a complete BRE inventory. PSI daily
summaries retain their missing pressure; it is never inferred from another test.

## Scientific boundaries

- Full matches report every requested axis within a numerical search window.
  Incomplete matches lack at least one requested condition. They do not establish
  coverage at that atmosphere. Neither tier proves physical equivalence.
- The default search uses ±1.5 oxygen percentage points and ±0.1 atm pressure.
  These are retrieval heuristics, not safety margins. The Explorer exposes them
  and preserves changes in the URL and download.
- Individual tests, test points, daily summaries and planned envelopes are distinct
  granularities. The mission views use only individual tests and test points.
- Heatmaps count only scalar paired conditions from individual records. Ranges,
  summaries, unknown axes and disputed axes remain searchable but are not plotted
  as measured pairs. An empty cell is an absence in this plotted subset.
- Rankings are exploratory measurement summaries, not flammability or safety
  rankings. Each eligible measurement remains an individual observation, with no
  pooled material estimates. Complete-condition matches with scalar, unambiguous outcomes
  retain investigation and recorded setup; incomplete conditions, conflicting
  outcomes and no-ignition burn times are excluded. Every contributing ID is retained.
- Ambient conditions in NASA-STD-6001B are a reference definition, not a universal
  material certification atmosphere. See the [NASA standard](https://standards.nasa.gov/standard/nasa/nasa-std-6001).
- Microgravity results do not validate Lunar or Martian gravity predictions.
  Missing data is not proof of safety or proof that no research exists.

See [method and export dictionary](docs/evidence-method.md) and the
[demonstration script](DEMO.md) for reproducible interpretation.

## Research workflow in the current implementation

Start at `/decide/`: record a research question, select the explicit conditions
and a measurement focus, then shortlist investigations. The evidence dossier
preserves classification quotes, source-linked records, unknown conditions,
retrieval sensitivity and next source checks. Its versioned export contains the
shortlist plus the complete evidence appendix. Local changes require publication
before this route or behavior is available on the public site.

The worked SAFFIRE comparison audits two real records, their source-indexed
outlet temperatures and their setup differences. Missing instrument/method fields
continue to block a condition-matched claim. This is a useful source audit, not
a newly established controlled comparison.

Outcome-specific metadata identifies the FLEX burning-rate imaging/fit method
and SAME-R detector channels without applying those methods to unrelated
quantities. SAME-R identifier groups retain separate observations, ambiguous
cross-material identifiers and unknown independence. `npm run evaluate:research`
checks three reproducible source-linked tasks and produces an unreviewed
researcher packet; it does not manufacture expert acceptance.

PSI chat measurements render in deterministic widgets. Current-message condition
binding prevents silent model-added pressure or flow-direction filters; ambiguous
requests are refused rather than guessed. PSI-turn model prose is withheld,
including text generated before a tool call. Narrative document answers retain
their separate source-cited path. Chat history is temporary; exported dossiers
are the reproducible record of a selection. Uploads are not offered in this workflow.

## Current evidence and scientific review

The owner approved the FLEX-2 cool-flame, LUCI and DAFT literature documents on
2026-10-31. There are 23 stable governed documents. The owner approved the
SAFFIRE SIBAL cross-check attribution correction from VI-3 to VI-2 on
2026-11-02. FLEX-2 literature rates remain
attached to planned fuel envelopes, while LUCI rotating-platform observations
and DAFT cabin-aerosol bounds remain separate from individual PSI tests.

The index still contains 1,951 records; 1,035 now carry outcomes. The approved
FLEX-2 supplement contributes 13 rates, and the SAFFIRE VI-3 record now includes
a source-guarded smoke-threshold observation. Temperature, gas and detector
measurements retain their locations, units, raw values and source identities.

[Internal scientific evaluation](research/scientific-evaluation.md) and its
[reproducible script](scripts/evaluate-scientific-evidence.py) examine paired
burns, comparability, missingness, uncertainty and conditional energy consistency.
The ambiguous SAFFIRE heat-release/time bundle is excluded from quantitative
analysis and retained as flagged source evidence. This is an internal source-based review,
not NASA endorsement, independent scientific peer review or predictive validation.

The vector publication manifest is [research/rag-publication.json](research/rag-publication.json).
The ingest receipt records generation 10: 23 documents and 284 chunks,
with 20 newly embedded chunks and no embedding failures. A fresh public MCP
evaluation verified generation 10, retrieved the expected document for all 13
target questions, found all four requested expanded-detail phrases and abstained
on all eight out-of-scope controls. The saved publication report records the
endpoint, time, dataset fingerprint and individual results. These document and
phrase checks do not establish answer correctness or independent scientific
review. A 0.415 retrieval floor was measured using 16 relevant and 12 out-of-scope
calibration probes. These are bounded engineering checks, not universal semantic
reliability. Pushes to `main`
trigger the configured deployment workflows; their outcome must be checked
separately from local validation and vector publication.

Structured PSI measurements are served through deterministic query tools;
governed documents are published through KSOR/pgvector. Both paths must be
refreshed after changes; building the website alone does not ingest vectors.

## Architecture and trust

| Layer | Implementation | Boundary |
| --- | --- | --- |
| Record | Governed CommonMark in `knowledge/` | Source statements, citations, approval metadata |
| Ingest | `system/psi-ingest` | Preserves raw cells, units, source conflicts and granularity |
| Query | Python and TypeScript twins | Deterministic filtering and exploratory ranking, pinned by fixtures |
| Site | Next.js static export | Home dashboard, source record and browser-only Explorer |
| Assistant | FastAPI, ChatKit, openai-agents | Tool-rendered evidence, optional model prose |
| Narrative retrieval | KSOR MCP, embeddings, Postgres | Separately deployed; health is not retrieval validation |

The current assistant has one configured XKIRO-hosted Qwen model. The environment
variable retains the legacy name `GROQ_API_KEY`. No multi-provider fallback is
claimed. Tool and citation guards reduce some failure modes; they do not prove
that every model statement is true. Use the static Explorer for the dependable demo.

Generated counts and source inventories live in
[`psi-data/derived/ingest-report.json`](psi-data/derived/ingest-report.json) and
[`source-inventory.md`](psi-data/derived/source-inventory.md). Rows with report data
are not necessarily independently confirmed measurements. Governance stamps are
recorded attestations; this engineering audit does not certify their human review.

## Validate changes

```sh
npm run check
npm --prefix system/site run test:psi
cd system/psi-ingest
uv run pytest
cd ../chatkit-server
GROQ_API_KEY=dummy uv run pytest
cd ../..
npm run build
```

On PowerShell use `npm.cmd` and `$env:GROQ_API_KEY='dummy'`. After ingest changes,
run `uv run psi-ingest`, regenerate fixtures with
`uv run python tests/gen_query_fixtures.py` in the chat backend, then run all suites.
Generated files must be regenerated, never hand-edited. Expected failures mark
known defects; they are not proof that those behaviors are correct.

## Deployment

| Service | Host | Why |
| --- | --- | --- |
| Site (static export) | GitHub Pages | Free, zero-config for a pure static export. |
| Chat backend (FastAPI) | Vercel | Native `pyproject.toml`/`uv.lock` support; serverless fits a request-scoped LLM call. |
| MCP door and embeddings API | Vercel *(container runtime)* | Separate `door` and `embeddings` containers; `/mcp` and `/v1/*` route to their respective services. |
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
npm run check                                   # governed-record format checks
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

> [!NOTE]
> **Windows dev:** Git Bash rewrites `/flame-freefall` in env vars to a Windows
> path. Prefix builds with `MSYS_NO_PATHCONV=1 MSYS2_ENV_CONV_EXCL='*'`.
> Clone with `git -c core.longpaths=true` (long PDF names in `narrative_reports/`).
> Only one `next dev` per project. After config changes, if the dev server
> wedges with "Jest worker encountered 2 child process exceptions":
> stop it, `rm -rf system/site/.next/dev`, and restart.
>
### Production Embedding Cutover

Do not switch the production MCP door directly from Gemini to Sentence
Transformers on the existing database. Embedding vectors are model-specific.
Use this staged migration:

1. Create a separate Neon database named `flame_freefall_sentence_transformers`
  with pgvector enabled. Keep the existing Gemini database unchanged.
2. Configure Vercel Preview variables for the MCP project: `KSOR_DB_URL` to the
  new database, `SENTENCE_TRANSFORMERS_BASE_URL` to the Preview deployment's
  `/v1` route, `SENTENCE_TRANSFORMERS_API_TOKEN` to a generated random token,
  and `KSOR_SNAPSHOT_KEYS` to a stable key. The embeddings container requires
  that same token; it fails closed if missing.
3. Deploy this branch as a Preview. Confirm its `/v1/health` works with bearer
  auth and its MCP `/health` reports the Sentence Transformers space.
4. Put the new database DSN and Preview embeddings URL in local `.env`, then run
  `npm run provision`, `npm run refresh`, and
  `npm run calibrate -- --queries-file <calibration-queries.json>`. Use the
  same model, dimensions, and token for ingestion and serving. Apply the
  measured retrieval floor to `instance.md` and rebuild.
5. Verify search against Preview, then set Production `KSOR_DB_URL` to the new
  database, `SENTENCE_TRANSFORMERS_BASE_URL` to
  `https://flamefreefall-sor.vercel.app/v1`, and the matching token. Merge the
  branch to `main` only after the new database is fully ingested and calibrated.

Never put a DSN, API token, or snapshot key in Git or paste one into chat. Add
secrets directly to Neon/Vercel and the local ignored `.env` file.

Each layer needs `.env` filled in — copy `.env.example` and see the comments
inline; the chat backend currently uses one XKIRO-hosted Qwen endpoint, with its key
in the legacy GROQ_API_KEY setting. There is no active multi-provider fallback. The full runbook — governance model, writing and approving knowledge,
troubleshooting table — is in [`AGENTS.md`](./AGENTS.md).


## References, rights and AI assistance

[MIT license](LICENSE) covers project-authored code and documentation. It does not
settle redistribution rights for bundled scientific reports and datasets. See the
[references and licensing inventory](REFERENCES.md) for remaining third-party review. AI-assisted code and record
creation are disclosed in [SUBMISSION.md](SUBMISSION.md); approval metadata must
never be manufactured to make a build pass.
