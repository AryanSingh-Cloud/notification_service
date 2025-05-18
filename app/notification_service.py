from app.schemas import NotificationRequest

def send_notification(notification: NotificationRequest):
    """
    Simulate sending notification based on type.
    In real apps, replace with actual email/SMS sending code.
    """
    if notification.type == "email":
        # Here, you'd integrate an email API
        return {"status": "Email sent", "user_id": notification.user_id}
    elif notification.type == "sms":
        # Here, you'd integrate an SMS API
        return {"status": "SMS sent", "user_id": notification.user_id}
    elif notification.type == "in-app":
        # Store in-app notification to DB or cache (dummy here)
        return {"status": "In-app notification sent", "user_id": notification.user_id}
    else:
        return {"status": "Unknown notification type"}
