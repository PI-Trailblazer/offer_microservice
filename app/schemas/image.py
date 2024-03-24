from typing import Optional, List

from pydantic import BaseModel

class Image(BaseModel):
    image: str

class ImageCreate(Image):
    offerid: int

class ImageUpdate(Image):
    image: Optional[str]

class ImageInDB(Image):
    id: int
    offerid: int