from fastapi.testclient import TestClient

import server


class FakeModel:
    def get_sentence_embedding_dimension(self):
        return 3

    def encode(self, texts, **kwargs):
        assert kwargs["normalize_embeddings"] is True
        return [FakeVector([1.0, 0.0, 0.0]) for _ in texts]


class FakeVector(list):
    def tolist(self):
        return list(self)


def test_embeddings_match_openai_response_shape(monkeypatch):
    monkeypatch.setattr(server, "MODEL_ID", "test-model")
    monkeypatch.setattr(server, "OUTPUT_DIM", 3)
    monkeypatch.setattr(server, "load_model", lambda: FakeModel())

    response = TestClient(server.app).post(
        "/v1/embeddings",
        json={"model": "test-model", "input": ["document", "query"], "dimensions": 3},
    )

    assert response.status_code == 200
    assert response.json()["model"] == "test-model"
    assert [entry["index"] for entry in response.json()["data"]] == [0, 1]
    assert [entry["embedding"] for entry in response.json()["data"]] == [
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ]


def test_model_vectors_are_zero_padded_to_declared_dimension(monkeypatch):
    monkeypatch.setattr(server, "MODEL_ID", "test-model")
    monkeypatch.setattr(server, "OUTPUT_DIM", 1536)
    monkeypatch.setattr(server, "load_model", lambda: FakeModel())

    response = TestClient(server.app).post(
        "/v1/embeddings",
        json={"model": "test-model", "input": "query", "dimensions": 1536},
    )

    assert response.status_code == 200
    vector = response.json()["data"][0]["embedding"]
    assert len(vector) == 1536
    assert vector[:3] == [1.0, 0.0, 0.0]
    assert all(value == 0 for value in vector[3:])


def test_requested_dimension_must_match_service_configuration(monkeypatch):
    monkeypatch.setattr(server, "MODEL_ID", "test-model")
    monkeypatch.setattr(server, "OUTPUT_DIM", 1536)
    monkeypatch.setattr(server, "load_model", lambda: FakeModel())

    response = TestClient(server.app).post(
        "/v1/embeddings",
        json={"model": "test-model", "input": "query", "dimensions": 384},
    )

    assert response.status_code == 400


def test_optional_service_token_is_enforced(monkeypatch):
    monkeypatch.setattr(server, "MODEL_ID", "test-model")
    monkeypatch.setattr(server, "OUTPUT_DIM", 3)
    monkeypatch.setattr(server, "load_model", lambda: FakeModel())
    monkeypatch.setenv("SENTENCE_TRANSFORMERS_API_TOKEN", "local-secret")
    client = TestClient(server.app)
    body = {"model": "test-model", "input": "query", "dimensions": 3}

    assert client.post("/v1/embeddings", json=body).status_code == 401
    response = client.post(
        "/v1/embeddings", json=body, headers={"Authorization": "Bearer local-secret"}
    )
    assert response.status_code == 200
