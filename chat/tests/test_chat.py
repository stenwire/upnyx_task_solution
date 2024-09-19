import pytest
from django.urls import reverse
from rest_framework import status
from chat.models import Chat

@pytest.mark.django_db
def test_create_chat_with_sufficient_tokens(api_client, user_with_sufficient_tokens):
    api_client.force_authenticate(user=user_with_sufficient_tokens)
    url = reverse("list-create-chat")
    payload = {"message": "hello"}

    response = api_client.post(url, payload, format="json")
    
    assert response.status_code == status.HTTP_201_CREATED
    chat = Chat.objects.get(user=user_with_sufficient_tokens)
    assert chat.response == (
        "Welcome to Upnyx Chat, you can ask these questions: "
        "['hello', 'what does upnyx do', 'what services does upnyx offer', "
        "'how to contact upnyx', 'where is upnyx located']"
    )
    user_with_sufficient_tokens.refresh_from_db()
    assert user_with_sufficient_tokens.tokens == 3900


@pytest.mark.django_db
def test_create_chat_with_unrecognized_message(api_client, user_with_sufficient_tokens):
    api_client.force_authenticate(user=user_with_sufficient_tokens)
    url = reverse("list-create-chat")
    payload = {"message": "unknown question"}

    response = api_client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    chat = Chat.objects.get(user=user_with_sufficient_tokens)
    assert chat.response == (
        "Please ask any of these questions: ['hello', 'what does upnyx do', "
        "'what services does upnyx offer', 'how to contact upnyx', 'where is upnyx located']"
    )
    user_with_sufficient_tokens.refresh_from_db()
    assert user_with_sufficient_tokens.tokens == 3900


@pytest.mark.django_db
def test_create_chat_with_insufficient_tokens(api_client, user_with_insufficient_tokens):
    api_client.force_authenticate(user=user_with_insufficient_tokens)
    url = reverse("list-create-chat")
    payload = {"message": "hello"}

    response = api_client.post(url, payload, format="json")
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["detail"] == "Insufficient tokens."
    user_with_insufficient_tokens.refresh_from_db()
    assert user_with_insufficient_tokens.tokens == 50
