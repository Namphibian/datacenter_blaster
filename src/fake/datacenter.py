import uuid
from datetime import datetime

from exceptions.http import Missing, Duplicate
from schema.base.record_base import AuditMetaData
from schema.cidr import CidrSummary

from schema.datacenter import DataCenterInfo, DataCenterStatus, DataCenterRecord

from system.decorators import log

fakes = [
    DataCenterInfo(
        name="Iceland",
        ipv6_networks=[

            CidrSummary(
                total_addresses=1024,
                cidr="2001:db8::/92",
                free_addresses=13,

            )],
        ipv4_networks=[
            CidrSummary(

                cidr="13.0.0.0/16",
                total_addresses=256,
                free_addresses=35,
            ),
            CidrSummary(

                cidr="14.0.0.0/16",
                total_addresses=256,
                free_addresses=73,
            )],
        audit_data=AuditMetaData(
            created_on=datetime.utcnow(),
            created_by="Demo User",
            updated_on=datetime.utcnow(),
            updated_by="Demo User",
        ),
        code="ICE",
        description="Iceland main center",
        datacenter_status=DataCenterStatus(
            code="Active",
            description="used",
        ),
    ),
    DataCenterInfo(
        audit_data=AuditMetaData(
            created_on=datetime.utcnow(),
            created_by="Demo User",
            updated_on=datetime.utcnow(),
            updated_by="Demo User",
        ),
        ipv6_networks=[],
        ipv4_networks=[
            CidrSummary(
                cidr="10.0.0.0/16",
                free_addresses=13,
                total_addresses=256,
            ),
            CidrSummary(
                cidr="12.0.0.0/16",
                free_addresses=13,
                total_addresses=256,
            ),
        ],
        name="Amsterdam",
        code="AM1",
        description="Amsterdam main center",
        datacenter_status=DataCenterStatus(
            code="Active",
            description="used",
        ),
    ),
    DataCenterInfo(
        name="Sacramento",
        ipv6_networks=[
            CidrSummary(
                cidr="2001:db8::/92",
                total_addresses=512,
                free_addresses=13,
            )],
        ipv4_networks=[
            CidrSummary(
                cidr="13.0.0.0/16",
                total_addresses=256,
                free_addresses=35,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                total_addresses=256,
                free_addresses=73,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                total_addresses=256,
                free_addresses=73,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                total_addresses=256,
                free_addresses=73,
            ),
            CidrSummary(

                cidr="17.0.0.0/16",
                total_addresses=256,
                free_addresses=73,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                total_addresses=256,
                free_addresses=73,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                total_addresses=256,
                free_addresses=73,
            ),
        ],
        audit_data=AuditMetaData(
            created_on=datetime.utcnow(),
            created_by="Demo User",
            updated_on=datetime.utcnow(),
            updated_by="Demo User",
        ),
        code="SAC",
        description="Sacramento main center",
        datacenter_status=DataCenterStatus(
            code="Active",
            description="used",
        ),
    ),
    DataCenterInfo(
        name="Alpharetta",
        ipv6_networks=[
            CidrSummary(
                cidr="2001:db8::/92",
                total_addresses=2048,
                free_addresses=13,
            )],
        ipv4_networks=[
            CidrSummary(
                cidr="13.0.0.0/16",
                free_addresses=35,
                total_addresses=256,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                free_addresses=73,
                total_addresses=256,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                free_addresses=73,
                total_addresses=256,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                free_addresses=73,
                total_addresses=256,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                free_addresses=73,
                total_addresses=256,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                free_addresses=73,
                total_addresses=256,
            ),
            CidrSummary(
                cidr="17.0.0.0/16",
                free_addresses=73,
                total_addresses=256,
            )
        ],
        audit_data=AuditMetaData(
            created_on=datetime.utcnow(),
            created_by="Demo User",
            updated_on=datetime.utcnow(),
            updated_by="Demo User",
        ),
        code="ALP",
        description="Alpharetta main center",
        datacenter_status=DataCenterStatus(
            code="Active",
            description="used",
        ),
    ),
]


def find(code: str) -> DataCenterInfo | None:
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


@log
def get_all() -> list[DataCenterInfo]:
    """Return all creatures"""
    return fakes


@log
def get_one(code: str) -> DataCenterInfo:
    """Return one creature"""
    check_missing(code)
    return find(code)


# The following are non-functional for now,
# so they just act like they work, without modifying
# the actual fakes list:
def create(datacenter: DataCenterRecord) -> DataCenterInfo:
    """Add a creature"""
    check_duplicate(datacenter.code)
    return datacenter


def modify(code: str, datacenter: DataCenterRecord) -> DataCenterInfo:
    """Partially modify a creature"""
    check_missing(datacenter.code)
    return datacenter


def delete(name: str) -> None:
    """Delete a creature"""
    check_missing(name)
    return None
