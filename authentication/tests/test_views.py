import pytest
from rest_framework import status
from django.urls import reverse

@pytest.mark.django_db
class TestSignupView:
    def test_signup_success(self, api_client):
        url = reverse("signup")
        data = {"username": "testuser", "password": "password123"}
        
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert "tokens" in response.data
        assert response.data["username"] == "testuser"

    def test_signup_missing_fields(self, api_client):
        url = reverse("signup")
        data = {"username": "testuser"}  # Missing password
        
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_signup_weak_password(self, api_client):
        url = reverse("signup")
        data = {"username": "testuser", "password": "12345"}  # Weak password
        
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "password" in response.data

    def test_signup_duplicate_username(self, api_client, create_user):
        create_user(username="testuser", password="password123")
        url = reverse("signup")
        data = {"username": "testuser", "password": "password123"}
        
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "username" in response.data


@pytest.mark.django_db
class TestLoginTokenObtainPairView:
    def test_login_success(self, api_client, create_user):
        create_user(username="testuser", password="password123")
        url = reverse("login")
        data = {"username": "testuser", "password": "password123"}
        
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

    def test_login_invalid_credentials(self, api_client):
        url = reverse("login")
        data = {"username": "invaliduser", "password": "invalidpass"}
        
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "No active account found" in response.data["detail"]
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "No active account found" in response.data["detail"]

    def test_login_blank_fields(self, api_client):
        url = reverse("login")
        data = {"username": "", "password": ""}
        
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestAvailableChatTokensView:
    def test_get_chat_tokens_success(self, api_client, create_user):
        user = create_user(username="testuser", password="password123")
        api_client.force_authenticate(user=user)
        
        url = reverse("fetch-chat-tokens")
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]["tokens"] == 4000

    def test_get_chat_tokens_with_zero_tokens(self, api_client, create_user):
        user = create_user(username="testuser", password="password123", tokens=0)
        api_client.force_authenticate(user=user)
        
        url = reverse("fetch-chat-tokens")
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]["tokens"] == 0

    def test_unauthenticated_request(self, api_client):
        url = reverse("fetch-chat-tokens")
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
