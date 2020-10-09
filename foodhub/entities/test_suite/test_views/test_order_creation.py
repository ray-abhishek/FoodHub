import pytest
import json
from django.urls import reverse


@pytest.mark.parametrize('merchant_data, item_data, store_data, order_data,status_code', [(
    {"name": "TestMerchant", "phone": 9428155726},
    {"name": "TestFoodItem", "cost": 100},
    {"name": "TestStore"},
    {"total_cost": 100}, 201)])
def test_order_creation(merchant_data, item_data, store_data, order_data,
                        status_code, api_client_with_credentials):

    # Create a merchant
    merchant_url = reverse('merchant-list')
    response = api_client_with_credentials.post(
        merchant_url, data=merchant_data)
    merchant = json.loads(response.content)

    # Create an item for above merchant
    item_data["merchant"] = merchant["pk"]
    item_url = reverse('item-list')
    response = api_client_with_credentials.post(item_url, data=item_data)
    item = json.loads(response.content)

    # Create a store with above merchant, item
    store_data["merchant"] = merchant["pk"]
    store_data["items"] = item["pk"]
    store_url = reverse('store-list')
    response = api_client_with_credentials.post(store_url, data=store_data)
    store = json.loads(response.content)

    # Place an order with above merchant, item, store
    order_data["merchant"] = merchant["pk"]
    order_data["store"] = store["pk"]
    order_data["items"] = item["pk"]
    order_url = reverse('order-list')
    response = api_client_with_credentials.post(order_url, data=order_data)

    assert response.status_code == status_code
