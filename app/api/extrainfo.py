from typing import List, Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from app.api import deps
from app import crud

from app.schemas.extrainfo import ExtraInfo, ExtraInfoCreate

router = APIRouter()

@router.get("/{offer_id}", response_model=List[ExtraInfo])
def get_extrainfo(
    offer_id: int,
    db: Session = Depends(deps.get_db)
) -> List[ExtraInfo]:
    return crud.extrainfo.get_by_offer_id(db, offer_id)

@router.post("/", response_model=ExtraInfo)
def create_extrainfo(
    extrainfo: ExtraInfoCreate,
    db: Session = Depends(deps.get_db)
) -> ExtraInfo:
    return crud.extrainfo.create(db, obj_in=extrainfo)