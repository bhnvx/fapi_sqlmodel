from fastapi import FastAPI, Depends, HTTPException, Path
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


@app.get('/get_user/{user_id}', response_model=User)
async def get_user(user_id: None, *, session: AsyncSession = Depends(get_session)):
    instance = await session.get(User, user_id)
    if not instance:
        raise HTTPException(status_code=404, detail=f"This User is not exist.")
    return instance


@app.patch('/update_user/{user_id}', response_model=User)
async def update_user(data: User, user_id: None, *, session: AsyncSession = Depends(get_session)):
    instance = await session.get(User, user_id)
    if not instance:
        raise HTTPException(status_code=404, detail=f"This User is not exist.")
    update_data = data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(instance, key, value)

    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


@app.delete('/delete_user/{user_id}', response_model=User)
async def delete_user(user_id: None, *, session: AsyncSession = Depends(get_session)):
    instance = await session.get(User, user_id)
    if not instance:
        raise HTTPException(status_code=404, detail=f"This User is not exist.")

    await session.delete(instance)
    await session.commit()

    return user_id


if __name__ == "__main__":
    conf = Config(".env")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(conf("SERVER_PORT")),
        reload=bool(int(conf("SERVER_DEBUG"))),
    )

