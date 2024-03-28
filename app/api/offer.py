from typing import List, Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from app.api import deps
from app import crud

from app.schemas.offer import Offer, OfferCreate

router = APIRouter()

@router.get("/", response_model=List[Offer])
def get_offers(
    db: Session = Depends(deps.get_db)
) -> List[Offer]:
    return crud.offer.get_multi(db)

@router.post("/", response_model=Offer)
def create_offer(
    offer: OfferCreate,
    db: Session = Depends(deps.get_db)
) -> Offer:
    return crud.offer.create(db, obj_in=offer)

