from rest_framework import generics, permissions
from .models import User
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# User Registration View
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
