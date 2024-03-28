from typing import Optional, List

from pydantic import BaseModel
from datetime import date as Date

class Reservation(BaseModel):
    init_date: Date
    end_date: Date

class ReservationCreate(Reservation):
    userid: int
    offerid: int

class ReservationUpdate(Reservation):
    init_date: Optional[Date]
    end_date: Optional[Date]

class ReservationInDB(Reservation):
    id: int
    userid: int
    offerid: int
