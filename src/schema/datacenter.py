from typing import Optional, List

from pydantic import BaseModel

from schema.base.record_base import RecordBase, AuditMetaData
from schema.cidr import CidrSummary


class DataCenterStatus(BaseModel):
    code: str
    description: Optional[str]


class DataCenterInfo(BaseModel):
    name: str
    code: str
    description: str
    datacenter_status: DataCenterStatus
    ipv4_networks: Optional[List[CidrSummary]]
    ipv6_networks: Optional[List[CidrSummary]]
    audit_data: AuditMetaData


class DataCenterStatusRecord(BaseModel):
    code: str
    description: Optional[str] = None


class DataCenterRecord(BaseModel):
    name: str
    code: str
    description: str
    datacenter_status: Optional[DataCenterStatusRecord] = None
