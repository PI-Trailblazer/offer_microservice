from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Offer(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    userid: Mapped[str] = mapped_column(String(264), nullable=False)
    name: Mapped[str] = mapped_column(String(264), nullable=False)
    description: Mapped[str] = mapped_column(String(264), nullable=False)
    street: Mapped[str] = mapped_column(String(264))
    city: Mapped[str] = mapped_column(String(264))
    postal_code: Mapped[str] = mapped_column(String(264))
    price: Mapped[float] = mapped_column(Float, nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)
    discount: Mapped[float] = mapped_column(Float, default=0.0)
    tags: Mapped[List[str]] = mapped_column(String(264))
    max_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    modules: Mapped[List[str]] = mapped_column(String(264))
