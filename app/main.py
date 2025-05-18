# app/main.py
from fastapi import FastAPI, HTTPException
from app.schemas import NotificationRequest, NotificationResponse, UserNotificationsResponse
from app.database import add_notification, get_notifications_for_user
from app.services import send_notification

app = FastAPI(title="Notification Service")

@app.post("/notifications", response_model=NotificationResponse)
def send_notification_endpoint(notification: NotificationRequest):
    # Save notification
    notif = add_notification(notification.user_id, notification.message, notification.type)

    # Send notification
    status = send_notification(notification.user_id, notification.message, notification.type)
    if status == "Unknown notification type":
        raise HTTPException(status_code=400, detail="Invalid notification type")

    return {"status": status, "user_id": notification.user_id}

@app.get("/users/{user_id}/notifications", response_model=UserNotificationsResponse)
def get_user_notifications(user_id: int):
    user_notifications = get_notifications_for_user(user_id)
    return {"user_id": user_id, "notifications": user_notifications}
