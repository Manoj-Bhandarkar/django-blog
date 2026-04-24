# 📝 Django Blog Management System

A full-featured Blog Web Application + REST API built using Django and Django REST Framework.

## 🚀 Overview
Public blog website
Admin-style dashboard (custom, not Django admin)
Authentication system
Role-based access (simple: User / Staff / Superuser)
REST API with JWT authentication


## 🔗 Live Demo
* ⚛️ Live App: https://blog.manojbhandarkar.cloud
* 📘 API Docs (Swagger): https://blog.manojbhandarkar.cloud/swagger/
---

🚀 Features
---
🌐 Frontend (User Side)
View all blog posts
Filter posts by category
Search blogs
View blog details
Add comments (approval required)
Pagination support


🔐 Authentication
---
User Registration
Login / Logout
JWT Authentication (for API)


📊 Dashboard (Custom Admin Panel)
---
👤 Normal User
Access dashboard
Add blog posts
Edit own posts

🧑‍💼 Staff User (is_staff=True)
Manage categories (Add/Edit/Delete)
Manage all blog posts
Manage users (Add/Edit/Delete)

👑 Superuser (is_superuser=True)
Full access
Access user listing page

----
🧩 Blog Features
---
Slug-based URLs (SEO friendly)
Featured posts
Draft / Published status
Image uploads
Category system

---
💬 Comment System
---
Authenticated users can comment
Comments require admin approval
Ordered by latest

---
🔌 REST API (Django REST Framework)
---
Authentication
JWT-based login
Register via API

## 📚 API Endpoints

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| POST   | /api/register/   | Register user          |
| POST   | /api/login/      | Get JWT token          |
| GET    | /api/posts/      | List posts (paginated) |
| POST   | /api/posts/      | Create post            |
| GET    | /api/posts/{id}/ | Retrieve post          |
| PUT    | /api/posts/{id}/ | Update post            |
| DELETE | /api/posts/{id}/ | Delete post            |
---

🛠️ Tech Stack
---
Python
Django
Django REST Framework
SQLite (default)
Bootstrap 4
Crispy Forms
JWT (SimpleJWT)

📁 Project Structure
---
blog_main/
│
├── blogs/           # Blog app (models, views, API)
├── dashboards/      # Custom admin dashboard
├── about/           # About & social links
├── templates/       # HTML templates
├── static/          # Static files
├── media/           # Uploaded images
│
└── manage.py
---

⚙️ Installation
---
1. Clone repository
git clone https://github.com/your-username/blog-project.git
cd blog-project

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Create superuser
python manage.py createsuperuser

6. Run server
python manage.py runserver

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

🔐 Permissions Summary
---------------------------------------------------
| Action            | User   | Staff  | Superuser |
| ----------------- | ------ | ------ | --------- |
| Add Post	        |  ✅	   |  ✅	  |  ✅       |
| Edit Own Post	    |  ✅	   |  ✅	  |  ✅       |
| Edit Any Post	    |  ❌	   |  ✅	  |  ✅       |
| Delete Post	      |  ❌	   |  ✅	  |  ✅       |
| Manage Categories |  ❌	   |  ✅	  |  ✅       |
| Manage Users	    |  ❌	   |  ✅	  |  ✅       |
| View Users Page	  |  ❌	   |  ❌	  |  ✅       |
----------------------------------------------------

## 👨‍💻 Author

**Manoj Bhandarkar**
* Portfolio: https://manojbhandarkar.cloud
* GitHub: https://github.com/manoj-bhandarkar
---

## ⭐ Show your support
If you like this project, give it a ⭐ on GitHub!
