# Local Sentence Transformers for KSOR

This service implements the OpenAI embeddings HTTP response shape used by the
KSOR Sentence Transformers provider. It runs inference locally and does not
require a Gemini or OpenAI API key.

Install and start it from this directory:

```powershell
uv sync --extra model
$env:SENTENCE_TRANSFORMER_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
uv run uvicorn server:app --host 127.0.0.1 --port 8001
```

The first health check downloads the model if it is not cached:

```powershell
Invoke-RestMethod http://127.0.0.1:8001/health
```

Set the KSOR embedding URL for `npm run refresh` and the serving process to
`http://127.0.0.1:8001/v1`. Both processes must reach the same model service.
For a deployed KSOR door, localhost means the door's own container, so deploy
this service alongside it or provide a private/reachable service URL. Do not
point a public service at an unauthenticated embedding endpoint. Set
`SENTENCE_TRANSFORMERS_API_TOKEN` on both processes to require a bearer token.

The model in `instance.md` must match `SENTENCE_TRANSFORMER_MODEL`, and its
`dim` must match `SENTENCE_TRANSFORMER_OUTPUT_DIM` (1536 by default). The
selected MiniLM model emits normalized 384-dimensional vectors; the service
appends zeros to 1536. Zero-padding normalized vectors preserves cosine
similarity while matching the existing `vector(1536)` database schema. Changing
the model or output dimension means re-ingesting the corpus and recalibrating
the retrieval floor.

Run the API contract tests without installing model weights:

```powershell
uv sync --group dev
uv run pytest
```
