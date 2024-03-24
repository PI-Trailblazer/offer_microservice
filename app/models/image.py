from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base
from app.core.config import settings

class Image(Base):
    id: Mapped[int] = mapped_column("id", Integer,  primary_key=True)
    offerid: Mapped[int] = mapped_column(
        ForeignKey(f"{settings.SCHEMA_NAME}.offer.id", ondelete="CASCADE"),
        index=True,
    )
    image: Mapped[str] = mapped_column(String(2048), nullable=False)