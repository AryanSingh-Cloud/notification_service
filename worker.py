import time
from app.database import notifications_db
from app.notifications import send_email, send_sms, send_in_app

def process_notifications():
    while True:
        for notification in notifications_db:
            if notification.status == "pending":
                print(f"Processing notification for user {notification.user_id}...")
                success = False
                if notification.type == "email":
                    success = send_email(notification)
                elif notification.type == "sms":
                    success = send_sms(notification)
                elif notification.type == "in_app":
                    success = send_in_app(notification)

                if success:
                    notification.status = "sent"
                    print(f"Notification sent successfully to user {notification.user_id}")
                else:
                    notification.status = "failed"
                    print(f"Failed to send notification to user {notification.user_id}, will retry later")

        time.sleep(5)  # wait before checking again

if __name__ == "__main__":
    print("Starting notification worker...")
    process_notifications()
