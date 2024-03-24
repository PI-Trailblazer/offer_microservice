from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column, ForeignKey

from app.db.base_class import Base
from app.core.config import settings

class ExtraInfo(Base):
    id: Mapped[int] = mapped_column("id", Integer,  primary_key=True)
    offerid: Mapped[int] = mapped_column(
        ForeignKey(f"{settings.SCHEMA_NAME}.offer.id", ondelete="CASCADE"),
        index=True,
    )
    nbeds: Mapped[int] = mapped_column(Integer)
    ntoilets: Mapped[int] = mapped_column(Integer)