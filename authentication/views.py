from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import SignupSerializer, LoginTokenObtainPairSerializer
from authentication.serializers import AvailableChatTokensSerializer
# Create your views here.

class SignupView(CreateAPIView):
  serializer_class = SignupSerializer
  queryset = User.objects.all()

class LoginTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginTokenObtainPairSerializer


class AvailableChatTokensView(ListAPIView):
    serializer_class = AvailableChatTokensSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)