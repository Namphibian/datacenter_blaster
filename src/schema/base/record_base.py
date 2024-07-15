from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID5


class RecordBase(BaseModel):
    id: UUID5


class AuditMetaData(BaseModel):
    created_on: datetime
    created_by: str
    updated_on: Optional[datetime]
    updated_by: Optional[str]


class StatusBase(BaseModel):
    status: str
    description: Optional[str]
