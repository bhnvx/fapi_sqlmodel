from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid as _uuid


class User(SQLModel, table=True):
    __tablename__ = 'user'

    uuid: Optional[str] = Field(..., max_length=32, nullable=False, default=lambda: str(_uuid.uuid4()))
    username: str = Field(..., min_length=4, nullable=False)
    password: str = Field(..., min_length=8, nullable=False)
    created_on: datetime = Field(default_factory=datetime.today)
