import pytest
from rest_framework.test import APIClient
from authentication.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def user_with_sufficient_tokens(create_user):
    return create_user(username="testuser", password="password123", tokens=4000)

@pytest.fixture
def user_with_insufficient_tokens(create_user):
    return create_user(username="lowtokens", password="password123", tokens=50)
