from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import engine, Base
from app.api.endpoints import traffic


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(traffic.router, prefix="/api/v1/traffic", tags=["traffic"])


@app.get("/")
async def root():
    return {
        "message": "Smart City Traffic Routing System API",
        "version": settings.version,
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
