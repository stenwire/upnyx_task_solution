from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.models import User
from authentication.serializers import (
    AvailableChatTokensSerializer,
    LoginTokenObtainPairSerializer,
    SignupSerializer,
)

# Create your views here.


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class LoginTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginTokenObtainPairSerializer


class AvailableChatTokensView(ListAPIView):
    serializer_class = AvailableChatTokensSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)
