from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base
from app.core.config import settings


class Review(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    userid: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    offerid: Mapped[int] = mapped_column(
        ForeignKey(f"{settings.SCHEMA_NAME}.offer.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    comment: Mapped[str] = mapped_column(String(264), nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)
