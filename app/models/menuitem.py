from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base
from app.core.config import settings


class MenuItem(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    offerid: Mapped[int] = mapped_column(
        ForeignKey(f"{settings.SCHEMA_NAME}.offer.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    image: Mapped[str] = mapped_column(String(2048), nullable=False)
    description: Mapped[str] = mapped_column(String(264))
    vegetarian: Mapped[bool] = mapped_column(Boolean, default=False)
