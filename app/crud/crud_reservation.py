from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.reservation import Reservation
from app.schemas.reservation import ReservationCreate, ReservationUpdate


class CRUDReservation(CRUDBase[Reservation, ReservationCreate, ReservationUpdate]):
    def get_by_offer_id(self, db: Session, offer_id: int):
        return db.query(self.model).filter(self.model.offerid == offer_id).all()

reservation = CRUDReservation(Reservation)