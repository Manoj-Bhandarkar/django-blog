# 📝 Full Stack Blog Platform (Django + DRF + React)

## 🚀 Overview

A production-ready full-stack blog application with a **Django REST Framework backend** and **React frontend**.
Implements secure JWT authentication, role-based access control, and scalable API architecture.

---

## 🔗 Live Demo

* 🌐 Portfolio: https://manojbhandarkar.cloud
* 📘 API Docs (Swagger): https://blog.manojbhandarkar.cloud/swagger/
* ⚛️ Frontend App: https://blog.manojbhandarkar.cloud

---

## 🧰 Tech Stack

### Backend

* Django
* Django REST Framework (DRF)
* JWT Authentication (SimpleJWT)
* Swagger (drf-yasg)

### Frontend

* React
* Axios
* React Router

### Deployment

* Render (Backend)
* Hostinger (Domain + DNS)

---

## 🔐 Authentication

### Login

`POST /api/login/`

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Response

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token",
  "username": "user",
  "email": "user@email.com"
}
```

---

### Register

`POST /api/register/`

```json
{
  "username": "user",
  "email": "user@email.com",
  "password": "password"
}
```

---

### Refresh Token

`POST /api/token/refresh/`

---

## 📚 API Endpoints

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| GET    | /api/posts/      | List posts (paginated) |
| POST   | /api/posts/      | Create post            |
| GET    | /api/posts/{id}/ | Retrieve post          |
| PUT    | /api/posts/{id}/ | Update post            |
| DELETE | /api/posts/{id}/ | Delete post            |

---

## 🔒 Authorization

Use JWT token in header:

```
Authorization: Bearer <access_token>
```

---

## ✨ Features

* 🔐 JWT Authentication (Login + Refresh)
* 👤 User Registration API
* 📝 Blog CRUD Operations
* 📄 Pagination Support
* 🔍 Search & Filtering
* 📘 Swagger API Documentation
* 🔄 Auto Token Refresh (Frontend)
* 🌐 Full-stack deployment with custom domain

---

## ⚙️ Backend Setup

```bash
git clone <your-backend-repo>
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## ⚛️ Frontend Setup

```bash
git clone <your-frontend-repo>
cd frontend
npm install
npm start
```
## 👨‍💻 Author

**Manoj Bhandarkar**

* Portfolio: https://manojbhandarkar.cloud
* GitHub: https://github.com/manoj-bhandarkar

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
