import uuid
from datetime import datetime

from ..exceptions.http import Missing, Duplicate
from ..schema.base.record_base import AuditMetaData
from ..schema.cidr import CidrSummary

from ..schema.datacenter import DataCenter, DataCenterStatus

fakes = [
    DataCenter(
        name="Iceland",
        id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="ICE"),
        networks=[
            CidrSummary(
                id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="2001:db8::/92"),
                cidr="2001:db8::/92",
                network_type="ipv6",
                number_of_free_ips=13,
            ),
            CidrSummary(
                id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="13.0.0.0/16"),
                cidr="13.0.0.0/16",
                network_type="ipv4",
                number_of_free_ips=35,
            ),
            CidrSummary(
                id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="14.0.0.0/16"),
                cidr="14.0.0.0/16",
                network_type="ipv4",
                number_of_free_ips=73,
            ),
        ],
        audit_data=AuditMetaData(
            created_on=datetime.utcnow(),
            created_by="Demo User",
            updated_on=datetime.utcnow(),
            updated_by="Demo User",
        ),
        code="ICE",
        description="Iceland main center",
        datacenter_status=DataCenterStatus(
            id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="Active"),
            code="Active",
            description="used",
        ),
    ),
    DataCenter(
        id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="AM1"),
        audit_data=AuditMetaData(
            created_on=datetime.utcnow(),
            created_by="Demo User",
            updated_on=datetime.utcnow(),
            updated_by="Demo User",
        ),
        networks=[
            CidrSummary(
                id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="10.0.0.0/16"),
                cidr="10.0.0.0/16",
                network_type="ipv4",
                number_of_free_ips=13,
            ),
            CidrSummary(
                id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="12.0.0.0/16"),
                cidr="12.0.0.0/16",
                network_type="ipv4",
                number_of_free_ips=13,
            ),
        ],
        name="Amsterdam",
        code="AM1",
        description="Amsterdam main center",
        datacenter_status=DataCenterStatus(
            id=uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="Active"),
            code="Active",
            description="used",
        ),
    ),
]


def find(code: str) -> DataCenter | None:
    for c in fakes:
        if c.code == code:
            return c
    return None


def check_missing(code: str):
    if not find(code):
        raise Missing(msg=f"Missing datacenter: {code}")


def check_duplicate(code: str):
    if find(code):
        raise Duplicate(msg=f"Duplicate datacenter {code}")


def get_all() -> list[DataCenter]:
    """Return all creatures"""
    return fakes


def get_one(code: str) -> DataCenter:
    """Return one creature"""
    check_missing(code)
    return find(code)


# The following are non-functional for now,
# so they just act like they work, without modifying
# the actual fakes list:
def create(datacenter: DataCenter) -> DataCenter:
    """Add a creature"""
    check_duplicate(datacenter.code)
    return datacenter


def modify(code: str, datacenter: DataCenter) -> DataCenter:
    """Partially modify a creature"""
    check_missing(datacenter.code)
    return datacenter


def delete(name: str) -> None:
    """Delete a creature"""
    check_missing(name)
    return None
