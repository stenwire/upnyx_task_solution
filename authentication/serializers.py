from django.contrib.auth import authenticate
from rest_framework import exceptions, serializers
from authentication.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SignupSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["username", "password"]
    extra_kwargs = {"password": {
      "write_only": True,
      "min_length": 8
    }}

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user

  def to_representation(self, instance):
    """Overriding to remove Password Field when returning Data"""
    ret = super().to_representation(instance)
    ret.pop('password', None)
    ret["tokens"] = instance.tokens
    return ret


class LoginTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs):
        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password')
        }

        user = authenticate(**credentials)

        if user:
            if not user.is_active:
                raise exceptions.AuthenticationFailed('User is deactivated')

            data = {}
            refresh = self.get_token(user)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            return data
        else:
            raise exceptions.AuthenticationFailed('No active account found with the given credentials')