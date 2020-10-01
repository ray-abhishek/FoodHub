import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate
from entities.views import MerchantViewSet


@pytest.mark.django_db
def test_unauthorized_request(api_client):
    url = reverse('merchant-list')
    response = api_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_authorized_request(api_client_with_credentials):
    url = reverse('merchant-list')
    response = api_client_with_credentials.get(url)
    assert response.status_code == 200


@pytest.mark.skip
@pytest.mark.django_db
def test_factory(api_request_factory, test_user):
    view = MerchantViewSet.as_view({'get': 'list'})
    request = api_request_factory.get('/merchants/')
    force_authenticate(request, user=test_user)
    response = view(request)
    assert response.status_code == 200
