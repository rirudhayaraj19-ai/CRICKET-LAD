from app.services.vector_store import VectorStore

store = VectorStore("data/vector_store/store.json")
store.add_document(
    "Hackathon Platform Overview",
    "CRICKET LAD collects information, cleans it, chunks documents, builds a searchable vector index, retrieves evidence, verifies generated answers, and routes automation workflows for knowledge tasks.",
    "demo",
)
print("Seeded demo document")
