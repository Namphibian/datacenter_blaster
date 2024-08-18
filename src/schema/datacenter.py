from typing import Optional, List

from pydantic import BaseModel

from schema.base.record_base import RecordBase, AuditMetaData
from schema.cidr import CidrSummary


class DataCenterStatus(RecordBase):
    code: str
    description: Optional[str]


class DataCenterInfo(RecordBase):
    name: str
    code: str
    description: str
    datacenter_status: DataCenterStatus
    networks: Optional[List[CidrSummary]]
    audit_data: AuditMetaData


class DataCenterStatusRecord(BaseModel):
    code: str
    description: Optional[str] = None


class DataCenterRecord(BaseModel):
    name: str
    code: str
    description: str
    datacenter_status: Optional[DataCenterStatusRecord] = None
