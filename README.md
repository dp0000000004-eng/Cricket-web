# 🏏 Cricket Management Web

A full-stack cricket management platform built with Django and Django REST Framework, designed to manage teams, players, venues, match data, bookings, and fan interactions in a clean and responsive web experience.

This project blends:
- a responsive HTML/CSS frontend
- Django backend logic
- DRF API endpoints
- JWT-based authentication
- real-world cricket domain modeling

It’s a practical example of a modern sports management web app with both UI and API capabilities.

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python)
![DRF](https://img.shields.io/badge/DRF-API-ff1709?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite)
![HTML](https://img.shields.io/badge/Frontend-HTML%20%2F%20CSS-1572B6?style=for-the-badge&logo=html5)

---

## 🚀 Project Overview

Cricket Management Web is a domain-based application that models a cricket ecosystem, connecting:

- teams
- players
- venues
- cities
- matches
- fan engagement
- booking-related workflows

The app is not just a static website — it includes backend data handling and API endpoints, making it feel like a professional, modular sports platform rather than a simple demo.

---

## ✨ Key Features

- Responsive cricket portal with HTML-based UI
- Team and player management
- Venue and city relationship modeling
- Match and cricket data views
- Fan interaction and data handling
- Booking support workflow
- JWT authentication
- API key generation
- Email verification flow
- Django admin integration
- Scalable and modular architecture

---

## 🧠 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML
- CSS
- JavaScript
- JWT (SimpleJWT)
- Pillow
- python-dotenv

---

## 📁 Project Structure

```bash
Cricket-web/
├── bigCameL/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── throttles.py
│   ├── urls.py
│   └── views.py
├── bigLaMA/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── manage.py
├── requirements.txt
├── db.sqlite3
├── README.md
├── .gitignore
└── ...
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/dp0000000004-eng/Cricket-web.git
cd Cricket-web
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the application:

```bash
python manage.py runserver
```

Open in the browser:

```bash
http://127.0.0.1:8000/
```

---

## 🔐 API & Authentication

The project includes JWT-based authentication and API capabilities, including:

- user login
- token generation
- token refresh
- API access handling
- email verification flow

This gives the project a modern full-stack flavor and makes it more than a traditional template-based app.

---

## 🏟️ Domain Model

The application models a cricket ecosystem built around:

- Teams
- Players
- Venues
- Cities
- Match-related data
- User engagement and booking logic

This gives the platform a rich and realistic domain structure, which is a strong sign of complexity and project depth.

---

## 📈 Project Scale Estimate

This project is best described as a:

- Medium-scale Django project
- Full-stack MVP / portfolio-grade application
- Domain-driven web app with API support

Why this estimate fits:
- multiple Django modules
- custom models, serializers, forms, views
- authentication flows
- frontend templates + API endpoints
- real-world sports domain logic
- modular architecture for future expansion

It’s not a tiny demo project — it’s structured enough to be considered a serious full-stack application. If this were developed by a single developer, it likely reflects several weeks of thoughtful work and continuous iteration.

---

## 🤝 Contributing

Contributions are welcome. Feel free to:

1. fork the repository
2. create a feature branch
3. make improvements
4. open a pull request

---

## 👨‍💻 Author

- Debasish

---

## 🌟 Final Note

This project shows strong signs of a well-structured, real-world full-stack application:
- backend logic
- API thinking
- responsive frontend
- domain modeling
- scalable architecture

It has the potential to grow into a much larger cricket platform with:
- admin dashboards
- advanced analytics
- team stats
- player rankings
- match scheduling
- payment/booking systems
- live score integrations

---

If you want, I can also generate:
1. a more minimal premium version
2. a super modern GitHub README with badges and sections
3. a portfolio-style README for your personal profile
4. a production-ready README with screenshots and architecture diagram
