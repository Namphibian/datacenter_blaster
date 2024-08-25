from enum import Enum
from typing import List

from pydantic import IPvAnyNetwork, BaseModel

from .base.record_base import RecordBase
from .ipaddress import IpAddressBase


class NetworkType(str, Enum):
    ipv4 = "IPV4"
    ipv6 = "IPV6"


class Cidr(RecordBase):
    cidr: IPvAnyNetwork
    network_type: NetworkType
    addresses: List[IpAddressBase]


1


class CidrSummary(BaseModel):
    cidr: IPvAnyNetwork
    total_addresses: int
    free_addresses: int
