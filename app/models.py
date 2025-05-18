# app/models.py
from typing import List
from pydantic import BaseModel

class Notification(BaseModel):
    id: int
    user_id: int
    message: str
    type: str  # "email", "sms", or "in-app"
