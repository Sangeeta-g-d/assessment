🏋️‍♀️ Fitness Class Booking System
A Django-based web application and REST API that allows users to view fitness classes and book slots. 
Admins can manage classes, and clients can book using the frontend or via API.

🚀 Features
📋 List all available fitness classes
🧘 Book a class (if slots are available)
✉️ Prevent duplicate bookings per email per class
🗂️ View bookings by email
🖥️ Admin UI to manage classes
🔗 REST API support for booking and retrieval

🛠️ Technologies Used
Backend: Django, Django REST Framework
Frontend: HTML + Bootstrap (admin UI)
Database: SQLite (default)
API Client: Postman

🔧 Setup Instructions
Clone the repository
git clone project-url,
cd project-name

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py makemigrations
python manage.py migrate

Run the server
python manage.py runserver

📡 API Endpoints
Get All Classes: GET /api/classes/

Book a Class : POST /api/book/
Body (JSON):
{
  "class_id": 1,
  "client_name": "Sangeeta G",
  "client_email": "sangeeta@gmail.com"
}

Get Bookings by Email: GET /api/bookings/?email=sangeeta@gmail.com

Access the Django admin panel at:http://127.0.0.1:8000/
