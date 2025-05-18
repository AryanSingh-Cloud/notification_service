# app/services.py

def send_email(user_id: int, message: str):
    print(f"Sending Email to user {user_id}: {message}")
    return "Email sent"

def send_sms(user_id: int, message: str):
    print(f"Sending SMS to user {user_id}: {message}")
    return "SMS sent"

def send_in_app(user_id: int, message: str):
    print(f"Sending In-App notification to user {user_id}: {message}")
    return "In-app notification sent"

def send_notification(user_id: int, message: str, type_: str):
    if type_ == "email":
        return send_email(user_id, message)
    elif type_ == "sms":
        return send_sms(user_id, message)
    elif type_ == "in-app":
        return send_in_app(user_id, message)
    else:
        return "Unknown notification type"
