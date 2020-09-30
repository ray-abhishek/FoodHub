from rest_framework import serializers


def validate_store_merchant(data):
    """
    Checks if the Store's Merchant is same as Order's Merchant.
    """
    store_merchant_id = data['store'].merchant.id
    order_merchant_id = data['merchant'].id
    if store_merchant_id != order_merchant_id:
        raise serializers.ValidationError(
            {"store": "Merchant ID doesn't match with Order's Merchant."})


def validate_items_merchant(data):
    """
    Checks if the Items' Merchant is same as Order's Merchant.
    """
    order_merchant_id = data['merchant'].id
    item_merchant_ids = [item.merchant.id for item in data['items']]
    for item_merchant_id in item_merchant_ids:
        if item_merchant_id != order_merchant_id:
            raise serializers.ValidationError(
                {"items": "Item(s) do not belong to the Order's Merchant."})
