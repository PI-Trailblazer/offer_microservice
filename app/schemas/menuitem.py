from typing import Optional, List

from pydantic import BaseModel

class MenuItem(BaseModel):
    image: str
    description: str
    vegetarian: bool

class MenuItemCreate(MenuItem):
    offerid: int

class MenuItemUpdate(MenuItem):
    image: Optional[str]
    description: Optional[str]
    vegetarian: Optional[bool]

class MenuItemInDB(MenuItem):
    id: int
    offerid: int