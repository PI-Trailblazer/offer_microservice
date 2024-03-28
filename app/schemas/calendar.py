from typing import Optional, List

from pydantic import BaseModel
from datetime import date as Date


class Calendar(BaseModel):
    init_date: Date
    end_date: Date

class CalendarCreate(Calendar):
    offerid: int

class CalendarUpdate(Calendar):
    init_date: Optional[Date]
    end_date: Optional[Date]

class CalendarInDB(Calendar):
    id: int
    offerid: int