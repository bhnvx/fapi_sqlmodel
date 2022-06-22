from fastapi import FastAPI

from api.settings import settings as api_setting
from api.dbCreate import create_model_table
from api.apps import api as api


def create_app(api_setting):
    app = FastAPI(
        docs_url="/docs",
        redoc_url="/redocs",
        title="Fast API (Dev Server)",
        description="Dev server",
        version="1.0",
        openapi_url="/openapi.json"
    )

    app.on_event("startup")(create_model_table)

    app.include_router(api)

    return app