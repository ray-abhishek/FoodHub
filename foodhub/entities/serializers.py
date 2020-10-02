from rest_framework import serializers
from entities.validators import (validate_store_merchant,
                                 validate_items_merchant)
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


class AttrPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):

        action = self.context['view'].action
        if action == "update":
            merchant = self.context['view'].get_object().merchant
            return Item.objects.filter(merchant=merchant)

        return Item.objects.all()


class StoreSerializer(serializers.ModelSerializer):
    items = AttrPKField(many=True)

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
    items = AttrPKField(many=True)

    class Meta:
        model = Order
        fields = ('pk', 'merchant', 'store', 'total_cost',
                  'status', 'items', 'created_at')

    def validate(self, data):
        """
        Perform object level validation for Merchant Integrity during Order
        Creation.

        validate_store_merchant : Checks if the Store's Merchant is same as
        Order's Merchant.
        validate_items_merchant : Checks if the Items' Merchant is same as
        Order's Merchant.
        """

        validate_store_merchant(data)
        validate_items_merchant(data)

        return data
