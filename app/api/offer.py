from typing import List, Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from app.api import deps

router = APIRouter()
