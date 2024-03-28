from typing import List, Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from app.api import deps
from app import crud

from app.schemas.reservation import Reservation, ReservationCreate

router = APIRouter()

@router.get("/{offer_id}", response_model=List[Reservation])
def get_reservation(
    offer_id: int,
    db: Session = Depends(deps.get_db)
) -> List[Reservation]:
    return crud.reservation.get_by_offer_id(db, offer_id)

@router.post("/", response_model=Reservation)
def create_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(deps.get_db)
) -> Reservation:
    return crud.reservation.create(db, obj_in=reservation)
