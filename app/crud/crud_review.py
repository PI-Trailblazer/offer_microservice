from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewUpdate


class CRUDReview(CRUDBase[Review, ReviewCreate, ReviewUpdate]):
    def get_by_offer_id(self, db: Session, offer_id: int):
        return db.query(self.model).filter(self.model.offerid == offer_id).all()

review = CRUDReview(Review)