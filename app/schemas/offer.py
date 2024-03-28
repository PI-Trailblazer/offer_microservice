from typing import Optional, List

from pydantic import BaseModel

class Offer(BaseModel):
    name: str
    description: str
    street: str
    city: str
    postal_code: str
    price: float
    max_review_score: float
    n_reviews: int
    discount: Optional[float] = 0.0
    tags: Optional[List[str]]
    max_quantity: int
    modules: Optional[List[int]]

class OfferCreate(Offer):
    id: int
    userid: int

class OfferUpdate(Offer):
    name: Optional[str]
    description: Optional[str]
    street: Optional[str]
    city: Optional[str]
    postal_code: Optional[str]
    price: Optional[float]
    max_review_score: Optional[float]
    n_reviews: Optional[int]
    discount: Optional[float]
    tags: Optional[List[str]]
    max_quantity: Optional[int]
    modules: Optional[List[int]]

class OfferInDB(Offer):
    id: int