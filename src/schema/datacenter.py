from typing import Optional, List

from .base.record_base import RecordBase, AuditMetaData
from .cidr import Cidr, CidrSummary


class DataCenterStatus(RecordBase):
    code: str
    description: Optional[str]


class DataCenter(RecordBase):
    name: str
    code: str
    description: str
    datacenter_status: DataCenterStatus
    networks: Optional[List[CidrSummary]]
    audit_data: AuditMetaData
