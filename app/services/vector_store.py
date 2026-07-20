import json
from pathlib import Path
from uuid import uuid4

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.models.schemas import DocumentRecord, SearchResult
from app.services.chunking import chunk_text, clean_text


class VectorStore:
    """Small persistent vector index optimized for hackathon demos and local development."""

    def __init__(self, path: str) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.documents: list[DocumentRecord] = []
        self.chunks: list[dict[str, str]] = []
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=6000)
        self.matrix = None
        self._load()
        self._rebuild()

    def add_document(self, title: str, content: str, source: str = "manual") -> tuple[str, int]:
        record = DocumentRecord(id=str(uuid4()), title=title, content=clean_text(content), source=source)
        chunks = chunk_text(record.content)
        if not chunks:
            raise ValueError("Document content produced no searchable chunks.")
        self.documents.append(record)
        for index, chunk in enumerate(chunks):
            self.chunks.append({"document_id": record.id, "chunk_id": str(index), "text": chunk})
        self._rebuild()
        self._persist()
        return record.id, len(chunks)

    def search(self, query: str, top_k: int) -> list[SearchResult]:
        if not self.chunks or self.matrix is None:
            return []
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix).flatten()
        ranked = np.argsort(scores)[::-1][:top_k]
        documents = {doc.id: doc for doc in self.documents}
        results: list[SearchResult] = []
        for idx in ranked:
            score = float(scores[idx])
            if score <= 0:
                continue
            chunk = self.chunks[int(idx)]
            doc = documents[chunk["document_id"]]
            results.append(
                SearchResult(
                    document_id=doc.id,
                    title=doc.title,
                    source=doc.source,
                    chunk=chunk["text"],
                    score=round(score, 4),
                )
            )
        return results

    def _rebuild(self) -> None:
        texts = [chunk["text"] for chunk in self.chunks]
        self.matrix = self.vectorizer.fit_transform(texts) if texts else None

    def _persist(self) -> None:
        payload = {"documents": [doc.model_dump() for doc in self.documents], "chunks": self.chunks}
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _load(self) -> None:
        if not self.path.exists():
            return
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        self.documents = [DocumentRecord(**doc) for doc in payload.get("documents", [])]
        self.chunks = payload.get("chunks", [])
