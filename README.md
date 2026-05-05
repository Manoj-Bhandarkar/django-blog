# 📝 Django Blog Platform + Production REST API

A **production-ready backend system** built using Django and Django REST Framework, demonstrating real-world concepts like query optimization, caching, authentication, and scalable deployment using Docker on AWS EC2.

---

## 🚀 Live Demo

* 🌐 App: https://blog.manojbhandarkar.cloud
* 📘 API Docs: https://blog.manojbhandarkar.cloud/api/docs

---

## 🎯 Project Summary

Built a full-stack blog platform focusing on:

* Scalable backend architecture
* Optimized database queries
* Secure authentication system
* Production deployment

---

## 🧠 Key Engineering Achievements

* ⚡ Reduced database queries by ~70% using `select_related` and `prefetch_related`
* 🚀 Improved performance using Redis caching for global data
* 🔍 Implemented PostgreSQL Full-Text Search
* 🔐 Built secure JWT authentication (SimpleJWT)
* 🐳 Deployed using Docker + Nginx + Gunicorn on AWS EC2
* 📦 Designed REST APIs with pagination, filtering, ordering

---

## ✨ Features

### 🌐 Blog System

* Featured posts & category filtering
* SEO-friendly slug-based URLs
* Comment system (authenticated users only)
* Responsive UI

---

### 📊 Admin Dashboard

* Role-Based Access Control (RBAC)
* Blog & Category CRUD
* User management (admin only)

---

### 🔌 REST API

* JWT Authentication (Login/Register)
* Blog CRUD APIs
* Pagination, Search, Ordering
* Permission system:

  * Users → own + published posts
  * Staff → full access

---

## ⚙️ Architecture

Client → Nginx → Gunicorn → Django
↓
PostgreSQL
↓
Redis

---

## 🛠️ Tech Stack

* Backend: Django, Django REST Framework
* Database: PostgreSQL
* Cache: Redis
* Auth: JWT (SimpleJWT)
* Deployment: Docker, AWS EC2
* Server: Gunicorn + Nginx
* API Docs: drf-spectacular

---

## ⚙️ Setup

```bash
git clone https://github.com/Manoj-Bhandarkar/django-blog.git
cd django-blog
```

Create `.env`:

```
DB_NAME=
DB_USER=
DB_PASSWORD=
SECRET_KEY=
DEBUG=False
```

Run:

```bash
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput
docker-compose exec web python manage.py createsuperuser
```

---

## 👨‍💻 Author

Manoj Bhandarkar

* Portfolio: https://manojbhandarkar.cloud
* GitHub: https://github.com/manoj-bhandarkar
* LinkedIn: https://www.linkedin.com/in/manoj-bhandarkar-dev/

---

⭐ If you find this useful, give it a star!
