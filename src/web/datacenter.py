from fastapi import APIRouter
from fake import datacenter as service
from schema.datacenter import DataCenterInfo, DataCenterRecord
from system.decorators import log
from system.jinja import jinja

router = APIRouter(prefix="/datacenter")


@router.get(
    "/",
    description="Operation retrieves a list of data centers with data indicating networks and associated free ip "
    "addresses.",
    # response_model=List[DataCenterInfo],
    tags=["Datacenter"],
    summary="List all the datacenters summary",
)
@jinja.hx("/partials/datacenter_list.html")
@log
def get_all_datacenters() -> list[DataCenterInfo]:
    return service.get_all()


@router.get(
    "/{code}",
    tags=["Datacenter"],
)
@jinja.hx("/partials/datacenter_view.html")
def get_one(code) -> DataCenterInfo | None:
    return service.get_one(code)


# all the remaining endpoints do nothing yet:
@router.post(
    "/",
    tags=["Datacenter"],
)
def create(datacenter: DataCenterRecord) -> DataCenterInfo:
    return service.create(datacenter)


@router.patch(
    "/",
    tags=["Datacenter"],
)
def modify(datacenter: DataCenterRecord) -> DataCenterInfo:
    return service.modify(datacenter)


@router.put(
    "/",
    tags=["Datacenter"],
)
def replace(datacenter: DataCenterInfo) -> DataCenterInfo:
    return service.replace(datacenter)


@router.delete(
    "/{code}",
    tags=["Datacenter"],
)
def delete(code: str):
    return None
