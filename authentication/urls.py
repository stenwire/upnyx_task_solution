from django.conf.urls import include
from django.urls import path
from authentication.views import SignupView

urlpatterns = [
    path('sign-up/', SignupView.as_view(), name='signup'),
]