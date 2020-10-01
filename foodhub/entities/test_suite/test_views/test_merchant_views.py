import pytest
from django.urls import reverse
import json
from entities.test_suite.test_views.helper_functions import (
    create_merchants, create_merchant
)


@pytest.mark.parametrize('name,email,phone,status_code', [
    ('', '', '', 400),
    ("Test Merchant", "merchant@test.com", "9438155726", 201),
    (123, '', 9438155726, 201),
    ('Merchant', 'merchant@test.com', 9438155726, 201),
    ('Merchant', 'merchanttest.com', 9438155726, 400),
    ('Merchant', 'merchant@test', 9438155726, 400),
])
def test_merchant_creation(name, email, phone, status_code, api_client_with_credentials):
    data = {
        'name': name,
        'email': email,
        'phone': phone
    }
    url = reverse('merchant-list')
    response = api_client_with_credentials.post(url, data=data)
    assert response.status_code == status_code


@pytest.mark.parametrize('number_of_merchants', [1, 3, 5])
def test_merchant_listview(number_of_merchants, api_client_with_credentials):
    create_merchants(number_of_merchants)
    url = reverse('merchant-list')
    response = api_client_with_credentials.get(url)
    merchant_list = json.loads(response.content)
    assert len(merchant_list) == number_of_merchants


@pytest.mark.parametrize('initial_details,updated_details', [({"name": "Merchant", "email": "", "phone": "9438155726"}, {"name": "Merchant", "email": "", "phone": "1111111111"})])
def test_merchant_updation(initial_details, updated_details, api_client_with_credentials):

    initial_merchant = create_merchant(initial_details)
    url = reverse('merchant-list') + str(initial_merchant.id) + '/'
    response = api_client_with_credentials.patch(url, data=updated_details)
    updated_merchant = json.loads(response.content)
    updated_merchant.pop('pk', None)
    updated_merchant.pop('created_at', None)
    assert updated_details == updated_merchant
