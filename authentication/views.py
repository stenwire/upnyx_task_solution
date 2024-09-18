from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from authentication.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import SignupSerializer, LoginTokenObtainPairSerializer
# Create your views here.

class SignupView(CreateAPIView):
  serializer_class = SignupSerializer
  queryset = User.objects.all()

class LoginTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginTokenObtainPairSerializer