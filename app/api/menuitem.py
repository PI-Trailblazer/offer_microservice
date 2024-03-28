from typing import List, Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from app.api import deps
from app import crud

from app.schemas.menuitem import MenuItem, MenuItemCreate

router = APIRouter()

@router.get("/{offer_id}", response_model=List[MenuItem])
def get_menuitem(
    offer_id: int,
    db: Session = Depends(deps.get_db)
) -> List[MenuItem]:
    return crud.menuitem.get_by_offer_id(db, offer_id)

@router.post("/", response_model=MenuItem)
def create_menuitem(
    menuitem: MenuItemCreate,
    db: Session = Depends(deps.get_db)
) -> MenuItem:
    return crud.menuitem.create(db, obj_in=menuitem)