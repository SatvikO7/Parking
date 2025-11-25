# CampusWheels – Vehicle Parking Management System

## 📌 Project Overview

CampusWheels is a web-based Vehicle Parking Management System built with Django and MySQL.
It allows college authorities to register vehicles, assign parking slots, and manage parking history efficiently.

## 🚀 Features

Vehicle registration (students & staff)

Parking slot assignment

Vehicle check-in and check-out

Parking history and dashboard

Admin panel for management

Tailwind CSS styling for UI

## 🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, Tailwind CSS

Database: MySQL / SQLite

Other: Django ORM, Bootstrap (optional)

## 📂 Project Structure

```
VEHICLE_PARKING/
│── env/                 # Virtual environment
│── parking_project/     # Main Django project
│   ├── parking_project/ # Project settings, urls
│   ├── vehicle_app/     # Main app with models, views
│   └── manage.py
│── vehicle_db/          # Database file (if SQLite)
```

## ⚙️ Installation & Setup
1. Clone the repository
```
git clone https://github.com/SatvikO7/Parking.git
cd vehicle_parking/parking_project
```

3. Create & activate virtual environment
```
python -m venv env
env\Scripts\activate   # On Windows
source env/bin/activate  # On Linux/Mac
```

5. Install dependencies
```
pip install -r requirements.txt
```

7. Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```

9. Create superuser
```
python manage.py createsuperuser
```

11. Run the server
python manage.py runserver
