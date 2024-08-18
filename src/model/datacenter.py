from typing import Optional

from sqlalchemy import BINARY, DateTime, Index, String, text
from sqlalchemy.orm import Mapped, mapped_column
import datetime

from system.db_connect import Base


class Datacenter(Base):
    __tablename__ = "datacenter"
    __table_args__ = (
        Index("uix_datacenter_name", "datacenter_name", unique=True),
        Index("uix_datacenter_code", "code", unique=True),
    )

    datacenter_id: Mapped[bytes] = mapped_column(BINARY(16), primary_key=True)
    datacenter_name: Mapped[str] = mapped_column(String(64))
    code: Mapped[str] = mapped_column(String(8))
    created_on: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_by: Mapped[str] = mapped_column(
        String(128), server_default=text("'system'")
    )
    description: Mapped[Optional[str]] = mapped_column(String(256))
    updated_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    updated_by: Mapped[Optional[str]] = mapped_column(String(128))
