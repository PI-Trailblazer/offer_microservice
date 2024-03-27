from fastapi import APIRouter

from . import offer

router = APIRouter()

router.include_router(offer.router, prefix="/offer", tags=["offer"])
