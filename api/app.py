from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.settings import get_config
from api.dbCreate import create_model_table
from api.apps import api as api


settings = get_config()

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="Fast API (Dev Server)",
    description="Dev server",
    version="1.0",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.on_event("startup")(create_model_table)

app.include_router(api)
