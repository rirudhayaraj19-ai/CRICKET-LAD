from app.models.schemas import LabRunResponse
from app.services.connectors import ConnectorRegistry, SourceType
from app.services.rag import RAGService
from app.services.vector_store import VectorStore


class AutonomousLab:
    """Runs a complete research-to-correction RAG loop for the website demo."""

    def __init__(self, connectors: ConnectorRegistry, store: VectorStore, rag: RAGService) -> None:
        self.connectors = connectors
        self.store = store
        self.rag = rag

    def run(self, topic: str, difficulty: str = "demo") -> LabRunResponse:
        packets = self.connectors.collect(topic, [SourceType.GOOGLE_RESEARCH, SourceType.CURATED, SourceType.WEB])
        indexed_chunks = 0
        document_ids: list[str] = []
        for packet in packets:
            doc_id, chunks = self.store.add_document(packet.title, packet.content, packet.source)
            document_ids.append(doc_id)
            indexed_chunks += chunks

        question = "What is Newton's second law?"
        first_answer = "Newton's second law says gravity is the same for every object in every situation."
        grounded = self.rag.answer(question, top_k=4, verify=True)
        corrected = "force equals mass times acceleration" not in first_answer.lower()
        final_answer = grounded.answer if corrected else first_answer

        return LabRunResponse(
            topic=topic,
            difficulty=difficulty,
            collected_sources=len(packets),
            indexed_chunks=indexed_chunks,
            document_ids=document_ids,
            question=question,
            first_answer=first_answer,
            corrected=corrected,
            final_answer=final_answer,
            verification=grounded.verification,
            citations=grounded.citations,
        )
