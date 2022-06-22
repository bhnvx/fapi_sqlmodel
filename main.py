import uvicorn

from starlette.config import Config
from api.app import create_app
from api.settings import settings


api = create_app(settings)


if __name__ == "__main__":
    conf = Config(".env")
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=int(conf("SERVER_PORT")),
        reload=bool(int(conf("SERVER_DEBUG"))),
    )

