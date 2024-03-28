from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.menuitem import MenuItem
from app.schemas.menuitem import MenuItemCreate, MenuItemUpdate


class CRUDMenuItem(CRUDBase[MenuItem, MenuItemCreate, MenuItemUpdate]):
    def get_by_offer_id(self, db: Session, offer_id: int):
        return db.query(self.model).filter(self.model.offerid == offer_id).all()

menuitem = CRUDMenuItem(MenuItem)