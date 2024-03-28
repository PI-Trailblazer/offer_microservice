from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.extrainfo import ExtraInfo
from app.schemas.extrainfo import ExtraInfoCreate, ExtraInfoUpdate


class CRUDExtraInfo(CRUDBase[ExtraInfo, ExtraInfoCreate, ExtraInfoUpdate]):
    def get_by_offer_id(self, db: Session, offer_id: int):
        return db.query(self.model).filter(self.model.offerid == offer_id).all()

extrainfo = CRUDExtraInfo(ExtraInfo)