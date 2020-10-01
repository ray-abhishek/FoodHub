import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient


@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username='admin', password='admin')
    return user


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_request_factory():
    factory = APIRequestFactory()
    return factory


@pytest.fixture
def api_client_with_credentials(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    yield api_client
    api_client.force_authenticate(user=None)
