from typing import List, Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from app.api import deps
from app import crud

from app.schemas.calendar import Calendar, CalendarCreate

router = APIRouter()

@router.get("/{offer_id}", response_model=List[Calendar])
def get_calendar(
    offer_id: int,
    db: Session = Depends(deps.get_db)
) -> List[Calendar]:
    return crud.calendar.get_by_offer_id(db, offer_id)

@router.post("/", response_model=Calendar)
def create_calendar(
    calendar: CalendarCreate,
    db: Session = Depends(deps.get_db)
) -> Calendar:
    return crud.calendar.create(db, obj_in=calendar)
