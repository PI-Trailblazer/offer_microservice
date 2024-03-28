from typing import List, Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from app.api import deps
from app import crud

from app.schemas.image import Image, ImageCreate

router = APIRouter()

@router.get("/{offer_id}", response_model=List[Image])
def get_image(
    offer_id: int,
    db: Session = Depends(deps.get_db)
) -> List[Image]:
    return crud.image.get_by_offer_id(db, offer_id)

@router.post("/", response_model=Image)
def create_image(
    image: ImageCreate,
    db: Session = Depends(deps.get_db)
) -> Image:
    return crud.image.create(db, obj_in=image)