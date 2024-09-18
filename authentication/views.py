from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from authentication.models import User
from authentication.serializers import SignupSerializer
# Create your views here.

class SignupView(CreateAPIView):
  serializer_class = SignupSerializer
  queryset = User.objects.all()