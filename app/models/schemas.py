from pydantic import BaseModel, Field


class IngestRequest(BaseModel):
    title: str = Field(min_length=1, max_length=160)
    content: str = Field(min_length=1)
    source: str = Field(default="manual", max_length=240)


class DocumentRecord(BaseModel):
    id: str
    title: str
    content: str
    source: str
    metadata: dict[str, str] = Field(default_factory=dict)


class IngestResponse(BaseModel):
    document_id: str
    chunks_indexed: int


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int | None = Field(default=None, ge=1, le=20)


class SearchResult(BaseModel):
    document_id: str
    title: str
    source: str
    chunk: str
    score: float


class AnswerRequest(SearchRequest):
    verify: bool = True


class AnswerResponse(BaseModel):
    answer: str
    confidence: float
    citations: list[SearchResult]
    verification: list[str]


class WorkflowRequest(BaseModel):
    objective: str = Field(min_length=1)
    payload: dict[str, str] = Field(default_factory=dict)


class WorkflowResponse(BaseModel):
    route: str
    steps: list[str]
    result: dict[str, object]


class LabRunRequest(BaseModel):
    topic: str = Field(default="Newton's second law and gravity", min_length=1, max_length=180)
    difficulty: str = Field(default="demo", max_length=80)


class LabRunResponse(BaseModel):
    topic: str
    difficulty: str
    collected_sources: int
    indexed_chunks: int
    document_ids: list[str]
    question: str
    first_answer: str
    corrected: bool
    final_answer: str
    verification: list[str]
    citations: list[SearchResult]
