from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.dashboard_categories, name='dashboard_categories'),
   

 ]
