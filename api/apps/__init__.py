from fastapi import APIRouter

from api.apps.user import view as user


api = APIRouter()

api.include_router(user.router, prefix="/user", tags=["User"])
