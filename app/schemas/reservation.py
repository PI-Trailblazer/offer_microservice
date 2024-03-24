from typing import Optional, List

from pydantic import BaseModel

class Reservation(BaseModel):
    init_date: str
    end_date: str

class ReservationCreate(Reservation):
    userid: int
    offerid: int

class ReservationUpdate(Reservation):
    init_date: Optional[str]
    end_date: Optional[str]

class ReservationInDB(Reservation):
    id: int
    userid: int
    offerid: int
