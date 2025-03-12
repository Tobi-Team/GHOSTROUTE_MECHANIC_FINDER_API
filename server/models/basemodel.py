import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, UUID, DateTime

from ..config import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(
        UUID(as_uuid=False),
        index=True,
        primary_key=True,
        default=uuid.uuid4()
    )
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.now(tz=timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True),
        onupdate=datetime.now(tz=timezone.utc)
    )
