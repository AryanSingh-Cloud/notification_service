# 📬 Notification Service

A simple backend system to send and retrieve notifications for users via Email, SMS, and In-App notifications.

---

## 🛠️ Objective

Build a notification system with APIs to:
- Send notifications
- Retrieve notifications per user

Supports:
- Email notifications
- SMS notifications
- In-app notifications

---

## 🔧 Features

✅ Send notifications via POST `/notifications`  
✅ Retrieve notifications via GET `/users/{id}/notifications`  
✅ Supports types: Email, SMS, In-App  
✅ Background worker simulates sending  
✅ Status tracking: `pending`, `sent`, `failed`  
✅ In-memory storage (for demo)  
🚀 Easy to extend with real databases or message queues

---

## 📁 Project Structure
notification_service/
│
├── app/
│ ├── init.py
│ ├── main.py # API endpoints
│ ├── models.py # Notification model
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # In-memory DB (list)
│ ├── notifications.py # Email/SMS/In-App logic
│
├── worker.py # Background worker
├── requirements.txt # Required Python packages
├── README.md # Project documentation




---

## 🚀 Getting Started

### 📌 Prerequisites

- Python 3.8 or later
- VS Code or any editor
- Internet connection (to install packages)

---

## ✅ Installation & Running

1. Clone the Repository

```bash
git clone <your-repo-url>
cd notification_service

2. (Optional) Create Virtual Environment
bash
python -m venv venv
# Activate it:
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

3. Install Required Packages
bash
pip install -r requirements.txt

4. Start the FastAPI Server
bash
uvicorn app.main:app --reload

5. Start the Worker (in another terminal)
bash
python worker.py

🎯 Usage
📤 Send a Notification
POST http://localhost:8000/notifications
Body Example (JSON):

json
{
  "user_id": 1,
  "message": "Your order has been shipped!",
  "type": "email"
}
Supported types: "email", "sms", "in_app"

📥 Get All Notifications for a User
GET http://localhost:8000/users/1/notifications

Returns all notifications for user ID 1.

🧪 Try it on Swagger UI
FastAPI gives you free interactive docs here:

🔗 http://localhost:8000/docs

⚙️ Assumptions
This is a demo project.

Notifications are stored in memory (list in Python).

SMS/Email/In-App are simulated with random success/failure.

On real projects, you'd use:

A database (like PostgreSQL, MongoDB)

A queue system (like RabbitMQ, Redis, or Kafka)

External APIs (like Twilio for SMS, SendGrid for Email)

🚀 Future Enhancements (Bonus)
✅ Add RabbitMQ for processing notifications using a queue

✅ Implement retry logic for failed notifications

📝 Add database support (PostgreSQL or MongoDB)

🔒 Add authentication for API access

🌍 Deploy with Docker & Render/Heroku

👤 Author
ARYAN SINGH
GitHub: [https://github.com/AryanSingh-Cloud]

📄 License
This project is for demonstration purposes and does not include a specific license

