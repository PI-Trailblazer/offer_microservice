from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float, Date
from sqlalchemy.orm import Mapped, mapped_column, ForeignKey

from app.db.base_class import Base
from app.core.config import settings

class Calendar(Base):
    id: Mapped[int] = mapped_column("id", Integer,  primary_key=True)
    offerid: Mapped[int] = mapped_column(
        ForeignKey(f"{settings.SCHEMA_NAME}.offer.id", ondelete="CASCADE"),
        index=True,
    )
    init_date: Mapped[Date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Date] = mapped_column(Date, nullable=False)