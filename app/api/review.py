from typing import List, Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from app.api import deps
from app import crud

from app.schemas.review import Review, ReviewCreate

router = APIRouter()

@router.get("/{offer_id}", response_model=List[Review])
def get_review(
    offer_id: int,
    db: Session = Depends(deps.get_db)
) -> List[Review]:
    return crud.review.get_by_offer_id(db, offer_id)

@router.post("/", response_model=Review)
def create_review(
    review: ReviewCreate,
    db: Session = Depends(deps.get_db)
) -> Review:
    return crud.review.create(db, obj_in=review)