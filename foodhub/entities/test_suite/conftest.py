import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def test_user(django_db_blocker):

    with django_db_blocker.unblock():
        user = User.objects.create_user(
            username='admin', password='admin')
        print("\n Creating User \n")
        yield user


@ pytest.fixture(scope="session")
def api_client():
    print("returning APIClient()")
    return APIClient()


"""@pytest.fixture
def api_request_factory():
    factory = APIRequestFactory()
    return factory
"""


@ pytest.fixture(scope="session")
def api_client_with_credentials(django_db_blocker, api_client, test_user):

    with django_db_blocker.unblock():
        api_client.force_authenticate(user=test_user)
        print("\nAuthenticating\n")
        yield api_client
        print("\nUnauthenticating\n")
        api_client.force_authenticate(user=None)


"""
setup function - pytest
django_db_blocker
"""
