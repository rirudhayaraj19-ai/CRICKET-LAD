from app.models.schemas import WorkflowResponse
from app.services.rag import RAGService
from app.services.vector_store import VectorStore


class WorkflowRouter:
    """Routes automation objectives to the smallest reliable workflow."""

    def __init__(self, store: VectorStore, rag: RAGService) -> None:
        self.store = store
        self.rag = rag

    def run(self, objective: str, payload: dict[str, str]) -> WorkflowResponse:
        text = objective.lower()
        if "ingest" in text or "index" in text:
            doc_id, chunks = self.store.add_document(
                payload.get("title", "Untitled"), payload.get("content", ""), payload.get("source", "workflow")
            )
            return WorkflowResponse(route="ingestion", steps=["clean", "chunk", "embed", "persist"], result={"document_id": doc_id, "chunks": chunks})
        answer = self.rag.answer(payload.get("query", objective), top_k=4)
        return WorkflowResponse(route="rag_answer", steps=["retrieve", "generate", "verify"], result=answer.model_dump())
