from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from entities.models import (Merchant, Item, Store, Order)
from entities.serializers import (MerchantSerializer, ItemSerializer,
                                  StoreSerializer, OrderSerializer)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class MerchantViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Merchant.
    """
    serializer_class = MerchantSerializer
    queryset = Merchant.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True)
    def stores(self, request, pk=None):
        merchant = Merchant.objects.filter(pk=pk).first()
        stores = Store.objects.filter(merchant=merchant)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def items(self, request, pk=None):
        merchant = Merchant.objects.filter(pk=pk).first()
        items = Item.objects.filter(merchant=merchant)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def orders(self, request, pk=None):
        merchant = Merchant.objects.filter(pk=pk).first()
        orders = Order.objects.filter(merchant=merchant)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class ItemViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Item
    """
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class StoreViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Store
    """
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True)
    def orders(self, request, pk=None):
        store = Store.objects.filter(pk=pk).first()
        orders = Order.objects.filter(store=store)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Order
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
