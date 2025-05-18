# app/schemas.py
from pydantic import BaseModel

class NotificationRequest(BaseModel):
    user_id: int
    message: str
    type: str  # "email", "sms", or "in-app"

class NotificationResponse(BaseModel):
    status: str
    user_id: int

class UserNotificationsResponse(BaseModel):
    user_id: int
    notifications: list
