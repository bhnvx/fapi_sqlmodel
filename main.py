import uvicorn
from starlette.config import Config


if __name__ == "__main__":
    conf = Config(".env")
    uvicorn.run(
        "api.app:api",
        host="0.0.0.0",
        port=int(conf("SERVER_PORT")),
        reload=bool(int(conf("SERVER_DEBUG"))),
    )

