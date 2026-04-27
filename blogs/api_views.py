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

    def get_queryset(self):
        user = self.request.user

        # Staff can see all
        if user.is_staff and user.is_authenticated:
            return Blog.objects.all()

        # Normal users → only own posts
        return Blog.objects.filter(status="published")
    
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