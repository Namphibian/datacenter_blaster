from enum import Enum
from typing import List

from pydantic import IPvAnyNetwork

from .base.record_base import RecordBase
from .ipaddress import IpAddressBase


class NetworkType(str, Enum):
    ipv4 = "IPV4"
    ipv6 = "IPV6"


class Cidr(RecordBase):
    cidr: IPvAnyNetwork
    network_type: NetworkType
    adresses: List[IpAddressBase]


class CidrSummary(RecordBase):
    cidr: IPvAnyNetwork
    network_type: NetworkType
    number_of_free_ips: int
