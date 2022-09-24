from fastapi import FastAPI

from src.v1.infrastructure.webserver.root.root import app as v1

app = FastAPI()

app.mount("/api/v1", v1)
