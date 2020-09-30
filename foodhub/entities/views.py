#from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import viewsets

from entities.models import Merchant, Item, Store, Order
from entities.serializers import MerchantSerializer, ItemSerializer, StoreSerializer, OrderSerializer
# Create your views here.


class MerchantViewSet(viewsets.ModelViewSet):
    """
    API view to retrieve list of Merchants or create new Merchant
    """
    serializer_class = MerchantSerializer
    queryset = Merchant.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    """
    API view to retrieve list of Items or create new Item
    """
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class StoreViewSet(viewsets.ModelViewSet):
    """
    API view to retrieve list of Stores or create new Store
    """
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    """
    API view to retrieve list of Orders or create new Order
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
