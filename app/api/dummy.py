from typing import List, Optional

from fastapi import APIRouter


from app.models.calendar import Calendar
from app.models.extrainfo import ExtraInfo
from app.models.image import Image
from app.models.menuitem import MenuItem
from app.models.offer import Offer 
from app.models.reservation import Reservation
from app.models.review import Review

#dont remove this before you completed all other endpoints, ensure every model is imported somewhere at least once
router = APIRouter()
