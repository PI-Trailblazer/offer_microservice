from typing import Optional, List

from pydantic import BaseModel

class Review(BaseModel):
    comment: str
    score: float

class ReviewCreate(Review):
    userid: int
    offerid: int

class ReviewUpdate(Review):
    comment: Optional[str]
    score: Optional[float]

class ReviewInDB(Review):
    id: int
    userid: int
    offerid: int

