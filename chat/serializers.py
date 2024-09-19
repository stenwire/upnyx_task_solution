from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['user', 'message', 'response', 'timestamp']
        read_only_fields = ['user', 'response', 'timestamp']
