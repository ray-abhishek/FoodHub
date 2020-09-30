#from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import viewsets

from entities.models import Merchant, Item, Store, Order
from entities.serializers import MerchantSerializer, ItemSerializer, StoreSerializer, OrderSerializer
# Create your views here.


class MerchantViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Merchant.
    """
    serializer_class = MerchantSerializer
    queryset = Merchant.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Item
    """
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class StoreViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Store
    """
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Order
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
