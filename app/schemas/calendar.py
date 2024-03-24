from typing import Optional, List

from pydantic import BaseModel

class Calendar(BaseModel):
    init_date: str
    end_date: str

class CalendarCreate(Calendar):
    offerid: int

class CalendarUpdate(Calendar):
    init_date: Optional[str]
    end_date: Optional[str]

class CalendarInDB(Calendar):
    id: int
    offerid: int