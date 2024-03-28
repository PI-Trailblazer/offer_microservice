from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.calendar import Calendar
from app.schemas.calendar import CalendarCreate, CalendarUpdate


class CRUDCalendar(CRUDBase[Calendar, CalendarCreate, CalendarUpdate]):
    def get_by_offer_id(self, db: Session, offer_id: int):
        return db.query(self.model).filter(self.model.offerid == offer_id).all()

calendar = CRUDCalendar(Calendar)