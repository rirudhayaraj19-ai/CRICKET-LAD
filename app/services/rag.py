from app.models.schemas import AnswerResponse, SearchResult
from app.services.vector_store import VectorStore


class RAGService:
    """Retrieval-augmented answer service with deterministic local generation."""

    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def answer(self, query: str, top_k: int, verify: bool = True) -> AnswerResponse:
        citations = self.store.search(query, top_k)
        if not citations:
            return AnswerResponse(
                answer="I do not have enough indexed evidence to answer that yet.",
                confidence=0.0,
                citations=[],
                verification=["No relevant source chunks were found."],
            )
        answer = self._compose_answer(query, citations)
        checks = self._verify(answer, citations) if verify else []
        confidence = min(0.98, sum(item.score for item in citations) / max(1, len(citations)) + 0.25)
        return AnswerResponse(answer=answer, confidence=round(confidence, 3), citations=citations, verification=checks)

    def _compose_answer(self, query: str, citations: list[SearchResult]) -> str:
        evidence = " ".join(result.chunk for result in citations[:2])
        return f"Based on the indexed knowledge, {query.strip()} relates to: {evidence}"

    def _verify(self, answer: str, citations: list[SearchResult]) -> list[str]:
        checks = ["Answer is grounded in retrieved chunks." if citations else "No citations available."]
        if len(answer) > 1200:
            checks.append("Answer is long; consider summarizing for demo clarity.")
        else:
            checks.append("Answer length is suitable for a concise response.")
        return checks
