import pytest
from django.urls import reverse
import json
from entities.models import Merchant


@pytest.mark.parametrize('name,email,phone,status_code', [
    ('', '', '', 400),
    ("Test Merchant", "merchant@test.com", "9438155726", 201),
    (123, '', 9438155726, 201),
    ('Merchant', 'merchant@test.com', 9438155726, 201),
    ('Merchant', 'merchanttest.com', 9438155726, 400),
    ('Merchant', 'merchant@test', 9438155726, 400),
])
def test_merchant_creation(name, email, phone, status_code,
                           api_client_with_credentials):
    data = {
        'name': name,
        'email': email,
        'phone': phone
    }
    url = reverse('merchant-list')
    response = api_client_with_credentials.post(url, data=data)
    assert response.status_code == status_code


@pytest.mark.django_db
def test_merchant_listview(api_client_with_credentials):
    merchants_in_db = Merchant.objects.all()
    url = reverse('merchant-list')
    response = api_client_with_credentials.get(url)
    merchant_list = json.loads(response.content)
    assert len(merchants_in_db) == len(merchant_list)


@pytest.mark.parametrize('initial_details,updated_details', [(
    {"name": "Merchant", "email": "", "phone": "9438155726"},
    {"name": "Merchant", "email": "", "phone": "1111111111"})])
def test_merchant_updation(initial_details, updated_details,
                           api_client_with_credentials):

    creation_url = reverse('merchant-list')
    creation_response = api_client_with_credentials.post(
        creation_url, data=initial_details)
    initial_merchant = json.loads(creation_response.content)

    updation_url = reverse('merchant-list') + str(initial_merchant["pk"]) + '/'
    response = api_client_with_credentials.patch(
        updation_url, data=updated_details)
    updated_merchant = json.loads(response.content)
    updated_merchant.pop('pk', None)
    updated_merchant.pop('created_at', None)

    assert updated_details == updated_merchant
