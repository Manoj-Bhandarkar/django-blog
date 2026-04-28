# 📝 Django Blog Management System + REST API

A professional, full-stack Blog Application featuring a custom Management Dashboard and a secure REST API.  Fully containerized with Docker, secured with SSL (Let's Encrypt), and deployed on AWS EC2.

---

## 🚀 Live Demo
* ⚛️ **Live App:** [https://blog.manojbhandarkar.cloud](https://blog.manojbhandarkar.cloud)
* 📘 **API Docs (Swagger):** [https://blog.manojbhandarkar.cloud/api/docs](https://api.manojbhandarkar.cloud/api/docs)

---

## 🧠 Key Highlights

- 🔒 HTTPS-enabled deployment with Nginx + Let's Encrypt
- 🐳 Fully Dockerized architecture (Django + PostgreSQL + Redis + Nginx)
- ⚡ Production-ready setup on AWS EC2
- 🔁 Reverse proxy with Nginx (static/media handling)
- 📦 Clean separation of services using Docker Compose

---

## ✨ Key Features

### 🌐 Public Frontend
* **Dynamic Content:** Featured posts, category filtering, and smart search.
* **SEO Optimized:** Slug-based URLs for better indexing.
* **Engagement:** Comment system with moderation workflow.
* **Performance:** Optimized database queries using `select_related` and `prefetch_related`.
* **Secure Auth:** JWT Authentication (SimpleJWT) for stateless login.
* **Standardized Docs:** Interactive OpenAPI 3.0 documentation via Swagger/Redoc. 
* **Resource Management:** Paginated and filtered blog endpoints.

### 🐳 DevOps & Deployment
* **Containerization:** Multi-container setup using Docker Compose.
* **Reverse Proxy:** Nginx handling SSL termination and static file serving.
* **Database & Cache:** PostgreSQL for persistent storage and Redis for caching.
* **Security:** SSL/TLS encryption via Let's Encrypt (Certbot).

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
* **Database:** PostgreSQL.
* **Cache:** Redis
* **Webserver:** Gunicorn + Nginx.
* **Security:** JWT (SimpleJWT), SSL/TLS, Environment Variables.
* **Infrastructure:** Docker, AWS EC2.
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
   git clone https://github.com/Manoj-Bhandarkar/django-blog.git
   cd blog-project

   ```
2. **Configure Environment**
   Create a .env file with your DB_NAME, DB_USER, DB_PASSWORD, and SECRET_KEY.
   
3. **Build & Launchbash**
   ```bash
   docker-compose up -d --build
   ```

4. **Initialize App**
   
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py collectstatic --no-input
   docker-compose exec web python manage.py createsuperuser
   ```
---

## 👨‍💻 Author
**Manoj Bhandarkar**
* **Portfolio:** [manojbhandarkar.cloud](https://manojbhandarkar.cloud)
* **GitHub:** [@manoj-bhandarkar](https://github.com/manoj-bhandarkar)
* **LinkedIn:** [@manoj0bhandarkar](https://www.linkedin.com/in/manoj-bhandarkar-dev/)

---

⭐ **If you find this project helpful, please give it a star!**
