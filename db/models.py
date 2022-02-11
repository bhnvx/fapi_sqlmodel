from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid as _uuid


class User(SQLModel, table=True):
    __tablename__ = 'user'

    uuid: Optional[_uuid.UUID] = Field(
        ..., primary_key=True, index=True
    )
    username: str = Field(..., min_length=4, nullable=False)
    password: str = Field(..., min_length=8, nullable=False)
    created_on: datetime = Field(default_factory=datetime.today)
