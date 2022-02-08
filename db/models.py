from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid as _uuid


class User(SQLModel, table=True):
    uuid: Optional[_uuid.UUID] = Field(
        default_factory=_uuid.uuid4(),
        primary_key=True,
        index=True,
        nullable=False,
    )
    username: str = Field(..., min_length=4, nullable=False)
    password: str = Field(..., min_length=8, nullable=False)
    created_on: datetime = Field(default_factory=datetime.today)
