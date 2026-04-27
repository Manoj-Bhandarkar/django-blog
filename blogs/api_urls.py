from rest_framework.routers import DefaultRouter
from .api_views import BlogViewSet, register_user, CustomLoginView
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', BlogViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register_user'),
    path('api_login/', CustomLoginView.as_view(), name='api_login'),    ]
