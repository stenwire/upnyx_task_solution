from rest_framework import serializers
from authentication.models import User

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