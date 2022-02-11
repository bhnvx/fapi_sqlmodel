from starlette.config import Config
from typing import AsyncGenerator

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio.engine import create_async_engine

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

conf = Config(".env")
database = dict(
    drivername=str(conf("POSTGRES_CONNECTION")),
    username=str(conf("POSTGRES_USERNAME")),
    password=str(conf("POSTGRES_PASSWORD")),
    host=str(conf("POSTGRES_HOST")),
    port=int(conf("POSTGRES_PORT")),
    database=str(conf("POSTGRES_DATABASE"))
)
url = URL.create(**database)
engine = create_async_engine(url, echo=bool(int(conf("SERVER_DEBUG"))))


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session


async def create_model_table() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
