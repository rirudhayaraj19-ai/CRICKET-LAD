from fastapi.testclient import TestClient

from app.main import create_app


def test_ingest_search_answer_workflow(tmp_path, monkeypatch):
    monkeypatch.setenv("VECTOR_STORE_PATH", str(tmp_path / "store.json"))
    app = create_app()
    with TestClient(app) as client:
        health = client.get("/api/health")
        assert health.status_code == 200
        response = client.post(
            "/api/ingest",
            json={"title": "RAG", "content": "Retrieval augmented generation uses search evidence to ground answers.", "source": "test"},
        )
        assert response.status_code == 200
        assert response.json()["chunks_indexed"] == 1
        search = client.post("/api/search", json={"query": "ground answers"})
        assert search.json()["results"]
        answer = client.post("/api/answer", json={"query": "How does RAG ground answers?"})
        assert answer.json()["confidence"] > 0
        workflow = client.post("/api/workflows/run", json={"objective": "answer question", "payload": {"query": "RAG"}})
        assert workflow.json()["route"] == "rag_answer"
        lab = client.post("/api/lab/run", json={"topic": "gravity and Newton laws"})
        assert lab.status_code == 200
        assert lab.json()["corrected"] is True
