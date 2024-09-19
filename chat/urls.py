from django.urls import path
from .views import ChatListCreateView

urlpatterns = [
    path('chat/', ChatListCreateView.as_view(), name='create-chat'),
]