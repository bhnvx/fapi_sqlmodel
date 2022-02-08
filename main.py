from fastapi import FastAPI, Depends
import uvicorn

from starlette.config import Config

from sqlalchemy.sql import text
from sqlmodel.ext.asyncio.session import AsyncSession

from db.dbUtil import get_session, create_model_table
from db.models import User


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="Fast API (Dev Server)",
    description="Dev server",
    version="1.0",
    openapi_url="/openapi.json"
)
app.on_event("startup")(create_model_table)


@app.get('/session_test')
async def session_test(*, session: AsyncSession = Depends(get_session)):
    data = await session.exec(text("select 1"))
    return data.all()


@app.post('/create_user', response_model=User)
async def create_user(data: User, *, session: AsyncSession = Depends(get_session)):
    instance = User.from_orm(data)
    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


if __name__ == "__main__":
    conf = Config(".env")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(conf("SERVER_PORT")),
        reload=bool(int(conf("SERVER_DEBUG"))),
    )

