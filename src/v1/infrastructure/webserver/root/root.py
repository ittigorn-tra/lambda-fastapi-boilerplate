from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import ENVIRONMENT, logger
from src.v1.infrastructure.webserver.api.status_routes import router as status_router

logger.info(f"ENVIRONMENT={ENVIRONMENT}")
root_path = "/"

app = FastAPI(
    title="Lambda FastAPI Boilerplate",
    description="A boilerpalte for FastAPI on AWS Lambda.",
    version="0.1.0",
    root_path=root_path,
)

origins = [
    "http://localhost:8000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(status_router, prefix="/status")
