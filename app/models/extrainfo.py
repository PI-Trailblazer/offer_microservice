from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base
from app.core.config import settings


class ExtraInfo(Base):
    offerid: Mapped[int] = mapped_column(
        ForeignKey(f"{settings.SCHEMA_NAME}.offer.id", ondelete="CASCADE"),
        index=True,
        primary_key=True,
    )
    nbeds: Mapped[int] = mapped_column(Integer)
    ntoilets: Mapped[int] = mapped_column(Integer)
