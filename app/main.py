from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes import router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.services.connectors import ConnectorRegistry
from app.services.lab import AutonomousLab
from app.services.rag import RAGService
from app.services.vector_store import VectorStore
from app.services.workflows import WorkflowRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    configure_logging(settings.log_level)
    store = VectorStore(settings.vector_store_path)
    rag = RAGService(store)
    app.state.vector_store = store
    app.state.rag = rag
    connectors = ConnectorRegistry()
    app.state.workflow_router = WorkflowRouter(store, rag)
    app.state.autonomous_lab = AutonomousLab(connectors, store, rag)
    yield


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        description="Intelligent automation API with ingestion, vector search, RAG answers, verification, and workflow routing.",
        version="0.1.0",
        lifespan=lifespan,
    )
    app.include_router(router, prefix="/api")
    app.mount("/static", StaticFiles(directory="app/web/static"), name="static")

    @app.get("/", include_in_schema=False)
    def index() -> FileResponse:
        return FileResponse("app/web/static/index.html")

    return app


app = create_app()
