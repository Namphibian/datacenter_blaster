import logging
from typing import List

from fastapi import APIRouter

from ..fake import datacenter as service
from ..schema.datacenter import DataCenter

_LOGGER = logging.getLogger(__name__)
router = APIRouter(prefix="/datacenter")


@router.get(
    "/",
    description="Operation retrieves a list of data centers with data indicating networks and associated free ip "
    "addresses.",
    response_model=List[DataCenter],
    tags=["Datacenter"],
    summary="List all the datacenters summary",
)
def get_all_datacenters() -> list[DataCenter]:
    return service.get_all()


@router.get(
    "/{code}",
    tags=["Datacenter"],
)
def get_one(code) -> DataCenter | None:
    return service.get_one(code)


# all the remaining endpoints do nothing yet:
@router.post(
    "/",
    tags=["Datacenter"],
)
def create(datacenter: DataCenter) -> DataCenter:
    return service.create(datacenter)


@router.patch(
    "/",
    tags=["Datacenter"],
)
def modify(datacenter: DataCenter) -> DataCenter:
    return service.modify(datacenter)


@router.put(
    "/",
    tags=["Datacenter"],
)
def replace(datacenter: DataCenter) -> DataCenter:
    return service.replace(datacenter)


@router.delete(
    "/{code}",
    tags=["Datacenter"],
)
def delete(code: str):
    return None
