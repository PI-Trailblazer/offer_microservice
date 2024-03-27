from typing import Optional
from typing import List

from sqlalchemy import String, Integer, Boolean, Float, ARRAY, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Offer(Base):
    id: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    userid: Mapped[str] = mapped_column(String(128), nullable=False)
    name: Mapped[str] = mapped_column(String(264), nullable=False)
    description: Mapped[str] = mapped_column(String(1028), nullable=False)
    street: Mapped[str] = mapped_column(String(264), nullable=False)
    city: Mapped[str] = mapped_column(String(264), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(264), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    max_review_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    n_reviews: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    discount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    tags: Mapped[List[str]] = mapped_column(ARRAY(Text), default=[], nullable=False)
    max_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    modules: Mapped[List[int]] = mapped_column(
        ARRAY(Integer), default=[], nullable=False
    )
