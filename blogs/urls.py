from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_categories, name="all_categories"), 
    path('<slug:slug>/', views.posts_by_category , name='posts_by_category'),
    ]
