FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/opt/huggingface \
    SENTENCE_TRANSFORMER_MODEL=sentence-transformers/all-MiniLM-L6-v2 \
    SENTENCE_TRANSFORMER_OUTPUT_DIM=1536 \
    SENTENCE_TRANSFORMERS_REQUIRE_TOKEN=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --extra model --no-dev --no-install-project

ENV PATH="/app/.venv/bin:$PATH"

COPY server.py ./
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"

EXPOSE 8001
CMD ["sh", "-c", "uvicorn server:app --host 0.0.0.0 --port ${PORT:-8001}"]