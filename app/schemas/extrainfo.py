from typing import Optional, List

from pydantic import BaseModel

class ExtraInfo(BaseModel):
    nbeds: int
    ntoilets: int

class ExtraInfoCreate(ExtraInfo):
    offerid: int

class ExtraInfoUpdate(ExtraInfo):
    nbeds: Optional[int]
    ntoilets: Optional[int]

class ExtraInfoInDB(ExtraInfo):
    id: int
    offerid: int