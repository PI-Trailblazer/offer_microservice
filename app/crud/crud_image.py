from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.image import Image
from app.schemas.image import ImageCreate, ImageUpdate


class CRUDImage(CRUDBase[Image, ImageCreate, ImageUpdate]):
    def get_by_offer_id(self, db: Session, offer_id: int):
        return db.query(self.model).filter(self.model.offerid == offer_id).all()

image = CRUDImage(Image)