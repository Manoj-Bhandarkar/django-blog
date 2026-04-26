# 📝 Django Blog Management System + REST API

A professional, full-stack Blog Application featuring a custom Management Dashboard and a secure REST API. Built with Django's best practices for scalability and security.

## 🚀 Live Demo
* ⚛️ **Live App:** [https://blog.manojbhandarkar.cloud](https://blog.manojbhandarkar.cloud)
* 📘 **API Docs (Swagger):** [https://manojbhandarkar.cloud](https://manojbhandarkar.cloud)

---

## ✨ Key Features

### 🌐 Public Frontend
* **Dynamic Content:** Featured posts, category filtering, and smart search.
* **SEO Optimized:** Slug-based URLs for better indexing.
* **Engagement:** Comment system with moderation workflow.
* **Performance:** Optimized database queries using `select_related` and `prefetch_related`.

### 📊 Custom Dashboard (Admin Panel)
* **Role-Based Access Control (RBAC):** Distinct permissions for Users, Staff, and Superusers.
* **Content Management:** Full CRUD for Blogs and Categories.
* **User Management:** Superuser-only interface to manage platform accounts.
* **Modern UI:** Styled with Bootstrap 4 and Django-Crispy-Forms.

### 🔌 REST API (DRF)
* **Secure Auth:** JWT Authentication (SimpleJWT) for stateless login.
* **Standardized Docs:** Interactive OpenAPI 3.0 documentation via Swagger/Redoc.
* **Resource Management:** Paginated and filtered blog endpoints.

---

## 🛠️ Tech Stack
* **Backend:** Python, Django 5.x+, Django REST Framework (DRF).
* **Database:** PostgreSQL (Production), SQLite (Development).
* **Security:** JWT (SimpleJWT), Django Middleware, Environment Variables (`python-dotenv`).
* **Frontend:** Bootstrap 4, FontAwesome, Django Templates.
* **API Documentation:** drf-spectacular (OpenAPI 3.0).

---

## 🔐 Permissions Logic

| Action | User | Staff | Superuser |
| :--- | :---: | :---: | :---: |
| Write Posts | ✅ | ✅ | ✅ |
| Edit Own Post | ✅ | ✅ | ✅ |
| Edit Any Post | ❌ | ✅ | ✅ |
| Delete Post | ❌ | ✅ | ✅ |
| Manage Categories | ❌ | ✅ | ✅ |
| Manage Users | ❌ | ❌ | ✅ |

---

## ⚙️ Installation & Setup

1. **Clone & Environment**
   ```bash
   git clone https://github.com
   cd blog-project
   python -m venv venv
   source venv/bin/activate  # venv\Scripts\activate on Windows
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**
   *Configure your .env file with your Database credentials.*
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run Project**
   ```bash
   python manage.py createsuperuser
   python manage.py runserver
   ```

---

## 👨‍💻 Author
**Manoj Bhandarkar**
* **Portfolio:** [manojbhandarkar.cloud](https://manojbhandarkar.cloud)
* **GitHub:** [@manoj-bhandarkar](https://github.com/manoj-bhandarkar)
* **LinkedIn:** [Your-LinkedIn-Link]

---
⭐ **If you find this project helpful, please give it a star!**
