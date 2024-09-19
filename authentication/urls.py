from django.urls import path
from authentication.views import SignupView, LoginTokenObtainPairView, AvailableChatTokensView

urlpatterns = [
    path('sign-up/', SignupView.as_view(), name='signup'),
    path('login/', LoginTokenObtainPairView.as_view(), name='login'),
    path('chat-tokens/', AvailableChatTokensView.as_view(), name='fetch-chat-tokens'),
]