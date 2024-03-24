from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.offer import Offer
from app.schemas.offer import OfferCreate, OfferUpdate


class CRUDUser(CRUDBase[Offer, OfferCreate, OfferUpdate]): ...


user = CRUDUser(Offer)