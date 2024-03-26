from fastapi import APIRouter

from . import offer
from . import dummy

router = APIRouter()

router.include_router(offer.router, prefix="/offer", tags=["offer"])
router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])