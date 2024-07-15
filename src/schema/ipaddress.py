from pydantic import IPvAnyAddress

from .base.record_base import RecordBase, StatusBase


class IpAddressBase(RecordBase):
    address: IPvAnyAddress
    status: StatusBase
