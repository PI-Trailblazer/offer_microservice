from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column, ForeignKey

from app.db.base_class import Base
from app.core.config import settings

class Review(Base):
    id: Mapped[int] = mapped_column("id", Integer,  primary_key=True)
    userid: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    offerid: Mapped[int] = mapped_column(
        ForeignKey(f"{settings.SCHEMA_NAME}.offer.id", ondelete="CASCADE"),
        index=True,
    )
    comment: Mapped[str] = mapped_column(String(264), nullable=False)
    score: Mapped[float] = mapped_column(Float)
