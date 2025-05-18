# app/database.py
from app.models import Notification

notifications = []
current_id = 1

def add_notification(user_id: int, message: str, type_: str) -> Notification:
    global current_id
    notification = Notification(id=current_id, user_id=user_id, message=message, type=type_)
    notifications.append(notification)
    current_id += 1
    return notification

def get_notifications_for_user(user_id: int):
    return [n for n in notifications if n.user_id == user_id]
