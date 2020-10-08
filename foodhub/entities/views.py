from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from entities.models import (Merchant, Item, Store, Order)
from entities.serializers import (MerchantSerializer, ItemSerializer,
                                  StoreSerializer, OrderSerializer)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from entities.tasks import create_order
import structlog
from silk.profiling.profiler import silk_profile

# Create your views here.

log = structlog.get_logger()


class MerchantViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Merchant.
    """
    serializer_class = MerchantSerializer
    queryset = Merchant.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        log.msg('Create Merchant Request', req=request.data)
        return response

    # @silk_profile(name='stores')
    @action(detail=True)
    def stores(self, request, pk=None):
        merchant = Merchant.objects.filter(pk=pk).first()
        stores = Store.objects.filter(merchant=merchant)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    # @silk_profile(name='items_of_merchants')
    @action(detail=True)
    def items(self, request, pk=None):
        merchant = Merchant.objects.filter(pk=pk).first()
        items = Item.objects.filter(merchant=merchant)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    # @silk_profile(name='orders_of_merchants')
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
    queryset = Item.objects.select_related('merchant').all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        log.msg('Create Item Request', req=request.data)
        return response


class StoreViewSet(viewsets.ModelViewSet):
    """
    API view to perform CRUD operations on Store
    """
    serializer_class = StoreSerializer
    queryset = Store.objects.select_related(
        'merchant').prefetch_related('items')
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        log.msg('Create Store Request', req=request.data)
        return response

    @silk_profile(name='orders_of_store')
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
    queryset = Order.objects.select_related(
        'merchant', 'store').prefetch_related('items')
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        log.msg('Create Order Request', req=request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            create_order.delay(serializer.data)
            headers = self.get_success_headers(serializer.validated_data)
            log.msg('Serializer Data', data=serializer.data,
                    validated_data=serializer.validated_data)
            response = {"message": "Order is being placed"}
            return Response(response, status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            response = {"message": "Order could not be placed."}
            return Response(response, status=status.HTTP_400_BAD_REQUEST,
                            headers=headers)
