from rest_framework import serializers
from entities.validators import (validate_store_merchant,
                                 validate_items_merchant, validate_total_cost)
from entities.models import (Merchant, Item, Store, Order)


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ('pk', 'name', 'email', 'phone', 'created_at')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('pk', 'name', 'merchant', 'cost',
                  'description', 'created_at')


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('pk', 'name', 'merchant', 'address', 'lon',
                  'lat', 'active', 'items', 'created_at')

    def validate(self, data):
        """
        Perform object level validation for Merchant Integrity during Store
        Creation.

        validate_items_merchant : Checks if the Items' Merchant is same as
        Order's Merchant.
        """

        validate_items_merchant(data)

        return data


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('pk', 'merchant', 'store', 'total_cost',
                  'status', 'items', 'created_at')

    def validate(self, data):
        """
        Perform object level validation for Merchant Integrity during Order
        Creation.

        Contains below functions :-
        1. validate_store_merchant : Checks if the Store's Merchant is same as
        Order's Merchant.
        2. validate_items_merchant : Checks if the Items' Merchant is same as
        Order's Merchant.
        3. validate_total_cost : Checks if the Sum of Item Costs is equal to
        Total Cost
        """

        validate_store_merchant(data)
        validate_items_merchant(data)
        validate_total_cost(data)

        return data
