from fastapi import APIRouter, Depends, HTTPException, Request

from app.core.config import Settings, get_settings
from app.models.schemas import AnswerRequest, IngestRequest, IngestResponse, LabRunRequest, SearchRequest, WorkflowRequest
from app.services.lab import AutonomousLab
from app.services.rag import RAGService
from app.services.vector_store import VectorStore
from app.services.workflows import WorkflowRouter

router = APIRouter()


def get_store(request: Request) -> VectorStore:
    return request.app.state.vector_store


def get_rag(request: Request) -> RAGService:
    return request.app.state.rag


def get_router(request: Request) -> WorkflowRouter:
    return request.app.state.workflow_router


def get_lab(request: Request) -> AutonomousLab:
    return request.app.state.autonomous_lab


@router.get("/health")
def health(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    return {"status": "ok", "app": settings.app_name, "environment": settings.app_env}


@router.post("/ingest", response_model=IngestResponse)
def ingest(payload: IngestRequest, store: VectorStore = Depends(get_store)) -> IngestResponse:
    try:
        document_id, chunks = store.add_document(payload.title, payload.content, payload.source)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return IngestResponse(document_id=document_id, chunks_indexed=chunks)


@router.post("/search")
def search(payload: SearchRequest, store: VectorStore = Depends(get_store), settings: Settings = Depends(get_settings)):
    return {"results": store.search(payload.query, payload.top_k or settings.top_k)}


@router.post("/answer")
def answer(payload: AnswerRequest, rag: RAGService = Depends(get_rag), settings: Settings = Depends(get_settings)):
    return rag.answer(payload.query, payload.top_k or settings.top_k, payload.verify)


@router.post("/workflows/run")
def run_workflow(payload: WorkflowRequest, router_: WorkflowRouter = Depends(get_router)):
    return router_.run(payload.objective, payload.payload)


@router.post("/lab/run")
def run_lab(payload: LabRunRequest, lab: AutonomousLab = Depends(get_lab)):
    return lab.run(payload.topic, payload.difficulty)
