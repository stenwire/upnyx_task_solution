import pytest
from authentication.serializers import SignupSerializer, LoginTokenObtainPairSerializer
from authentication.models import User

@pytest.mark.django_db
class TestSignupSerializer:
    def test_create_user_success(self):
        data = {"username": "testuser", "password": "password123"}
        serializer = SignupSerializer(data=data)
        
        assert serializer.is_valid()
        user = serializer.save()
        
        assert isinstance(user, User)
        assert user.username == "testuser"
        assert user.check_password("password123")

    def test_create_user_missing_password(self):
        data = {"username": "testuser"}
        serializer = SignupSerializer(data=data)
        
        assert not serializer.is_valid()
        assert "password" in serializer.errors

    def test_create_user_missing_username(self):
        data = {"password": "password123"}  # Missing username
        serializer = SignupSerializer(data=data)
        
        assert not serializer.is_valid()
        assert "username" in serializer.errors

    def test_create_user_weak_password(self):
        data = {"username": "testuser", "password": "12345"}
        serializer = SignupSerializer(data=data)
        
        assert not serializer.is_valid()
        assert "password" in serializer.errors


@pytest.mark.django_db
class TestLoginTokenObtainPairSerializer:
    def test_validate_valid_user(self, create_user):
        user = create_user(username="testuser", password="password123")
        data = {"username": "testuser", "password": "password123"}
        
        serializer = LoginTokenObtainPairSerializer(data=data)
        assert serializer.is_valid()
        result = serializer.validated_data
        
        assert "access" in result
        assert "refresh" in result

    def test_validate_blank_fields(self):
        data = {"username": "", "password": ""}
        serializer = LoginTokenObtainPairSerializer(data=data)
        
        assert not serializer.is_valid()
        assert "username" in serializer.errors
        assert "password" in serializer.errors
