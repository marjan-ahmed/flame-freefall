"""OpenAI-compatible embeddings endpoint backed by a local Sentence Transformers model."""

from __future__ import annotations

import os
import secrets
from functools import lru_cache
from typing import Any

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

MODEL_ID = os.environ.get("SENTENCE_TRANSFORMER_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
OUTPUT_DIM = int(os.environ.get("SENTENCE_TRANSFORMER_OUTPUT_DIM", "1536"))


class EmbeddingRequest(BaseModel):
    model: str
    input: str | list[str]
    dimensions: int | None = None


@lru_cache(maxsize=1)
def load_model() -> Any:
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise RuntimeError("Install the 'model' extra to run Sentence Transformers inference") from exc

    return SentenceTransformer(MODEL_ID)


app = FastAPI(title="Local Sentence Transformers embeddings")


@app.get("/health")
def health() -> dict[str, str | int]:
    model = load_model()
    return {
        "status": "ok",
        "model": MODEL_ID,
        "model_dimensions": int(model.get_sentence_embedding_dimension()),
        "dimensions": OUTPUT_DIM,
    }


@app.post("/v1/embeddings")
def create_embeddings(
    request: EmbeddingRequest, authorization: str | None = Header(default=None)
) -> dict[str, object]:
    token = os.environ.get("SENTENCE_TRANSFORMERS_API_TOKEN")
    if token and not secrets.compare_digest(authorization or "", f"Bearer {token}"):
        raise HTTPException(status_code=401, detail="Invalid bearer token")
    if request.model != MODEL_ID:
        raise HTTPException(status_code=400, detail=f"Configured model is {MODEL_ID!r}")

    texts = [request.input] if isinstance(request.input, str) else request.input
    if not texts or any(not text.strip() for text in texts):
        raise HTTPException(status_code=400, detail="input must contain non-empty text")

    model = load_model()
    model_dimensions = int(model.get_sentence_embedding_dimension())
    if OUTPUT_DIM < model_dimensions:
        raise HTTPException(status_code=500, detail="Configured output dimension is smaller than the model dimension")
    if request.dimensions is not None and request.dimensions != OUTPUT_DIM:
        raise HTTPException(status_code=400, detail=f"Configured output dimension is {OUTPUT_DIM}")

    vectors = model.encode(texts, convert_to_numpy=True, normalize_embeddings=True, show_progress_bar=False)
    return {
        "object": "list",
        "model": MODEL_ID,
        "data": [
            {
                "object": "embedding",
                "index": index,
                "embedding": vector.tolist() + [0.0] * (OUTPUT_DIM - model_dimensions),
            }
            for index, vector in enumerate(vectors)
        ],
    }
