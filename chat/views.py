from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.conf import settings
from .models import Chat
from .serializers import ChatSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

AVAILABLE_QUESTIONS = [
    "hello",
    "what does upnyx do",
    "what services does upnyx offer",
    "how to contact upnyx",
    "where is upnyx located"
    ]

PREDEFINED_RESPONSES = {
    "hello": (f"Welcome to Upnyx Chat, you can ask these questions: {AVAILABLE_QUESTIONS}"),
    "what does upnyx do": (
        "We support decision makers like you to build/grow your organization. By partnering with you to identify bottlenecks "
        "and issues, craft a plan to improve business, and develop strategies to achieve sustainable results, we will provide "
        "you with a roadmap to success."
    ),
    "what services does upnyx offer": (
        "AI AND MACHINE LEARNING SOLUTIONS, DIGITAL MARKETING AND ANALYTICS, IT Consulting and User Support, Mobile & Web Development"
    ),
    "how to contact upnyx": (
        "Feel free to talk to our online representative at any time you please. Please be patient while waiting for a response. "
        "(24/7 Support!), Phone General Inquiries: +91-9747911474"
    ),
    "where is upnyx located": (
        "Head office:UPNyX Innovative Solutions, 11/725, Arunima, Kalluvarambu, Aramkallu, Karakulam PO, TrivandrumPIN:695581"
    )
}

def default_response(user_message):
    return f"Please ask any of these questions: {AVAILABLE_QUESTIONS}"

class ChatListCreateView(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Chat.objects.filter(user=self.request.user).order_by('-timestamp')

    def perform_create(self, serializer):
        user = self.request.user
        message = serializer.validated_data['message'].strip().lower()

        # Check if user has sufficient tokens
        if user.tokens >= settings.CHAT_TOKEN_SETTINGS.MINIMUM:
            user.tokens -= settings.CHAT_TOKEN_SETTINGS.MINIMUM
            user.save()

            response = PREDEFINED_RESPONSES.get(message, default_response(message))
            serializer.save(user=user, message=message, response=response, timestamp=timezone.now())
        else:
            raise ValueError("Insufficient tokens.")

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
