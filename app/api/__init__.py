from fastapi import APIRouter

from . import offer
from . import calendar
from . import extrainfo
from . import review
from . import reservation

router = APIRouter()

router.include_router(offer.router, prefix="/offer", tags=["offer"])
router.include_router(calendar.router, prefix="/calendar", tags=["calendar"])
router.include_router(extrainfo.router, prefix="/extrainfo", tags=["extrainfo"])
router.include_router(review.router, prefix="/review", tags=["review"])
router.include_router(reservation.router, prefix="/reservation", tags=["reservation"])
