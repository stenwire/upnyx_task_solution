import factory
from django.utils import timezone
from chat.models import Chat
from authentication.models import User
from authentication.tests.factories import UserFactory

class ChatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Chat

    user = factory.SubFactory(UserFactory)
    message = "hello"
    response = "Welcome to Upnyx Chat, you can ask these questions: ..."
    timestamp = timezone.now()
