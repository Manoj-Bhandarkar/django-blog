from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema
from .models import Blog
from .serializers import BlogSerializer, RegisterSerializer, CustomTokenSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

class BlogPagination(PageNumberPagination):
    page_size = 5

# ---------------- REGISTER ----------------
@extend_schema(
    request=RegisterSerializer,
    responses={201: {"example": {"message": "User created successfully"}}}
)
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------------- LOGIN ----------------

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

# ---------------- BLOG VIEWSET ----------------  
class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = BlogPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "short_description"]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        user = self.request.user

        queryset = Blog.objects.select_related("author", "category")

        # Staff can see all
        if user.is_staff:
            return queryset

        if user.is_authenticated:
            return queryset.filter(Q(status="published") | Q(author=user)).distinct()
        
        return queryset.filter(status="published")
    
    def perform_create(self, serializer):
            serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()

        if not (self.request.user.is_staff or post.author == self.request.user):
            raise PermissionDenied("You cannot edit this post")

        serializer.save()

    def perform_destroy(self, instance):
        if not (self.request.user.is_staff or instance.author == self.request.user):
            raise PermissionDenied("You cannot delete this post")

        instance.delete()