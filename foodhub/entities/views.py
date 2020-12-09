import json
from rest_framework.settings import api_settings
from json.encoder import JSONEncoder
from rest_framework.pagination import LimitOffsetPagination
from django.http.response import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from entities.models import (Merchant, Item, Store, Order)
from entities.serializers import (MerchantSerializer, ItemSerializer,
                                  StoreSerializer, OrderSerializer)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from entities.tasks import create_order, relay_order
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import structlog
from rest_framework.utils.urls import remove_query_param, replace_query_param
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
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        user_agent = self.request.headers.get('User-Agent', None)
        log.info('INSIDE paginator',user_agent = user_agent)
        if not hasattr(self, '_paginator'):
        
            if self.pagination_class is None:
                self._paginator = None
            else:
                if 'Postman' in user_agent:
                    self._paginator = CustomPagination()
                else:
                    self._paginator = self.pagination_class()
        return self._paginator

    def create(self, request):
        log.msg('Create Order Request', req=request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_order.apply_async(args=[serializer.data], link=relay_order.s())
        headers = self.get_success_headers(serializer.validated_data)
        log.msg('Serializer Data', data=serializer.data,
                validated_data=serializer.validated_data)
        response = {"message": "Order is being placed"}
        return Response(response, status=status.HTTP_201_CREATED,
                        headers=headers)

class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'end'
    offset_query_param = 'start'

    def paginate_queryset(self, queryset, request, view=None):
        self.count = self.get_count(queryset)
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.offset = self.get_offset(request)
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or self.offset > self.count:
            return []
        return list(queryset[self.offset : self.limit])

    def get_next_link(self):
        if self.limit >= self.count:
            return None

        url = self.request.build_absolute_uri()
        url = replace_query_param(url, self.offset_query_param, self.limit)

        offset = self.limit + self.default_limit
        return replace_query_param(url, self.limit_query_param, offset)

    def get_previous_link(self):
        if self.offset <= 0:
            return None

        url = self.request.build_absolute_uri()
        limit = self.offset
        url = replace_query_param(url, self.limit_query_param, limit)

        if self.offset - self.default_limit <= 0:
            return remove_query_param(url, self.offset_query_param)

        offset = self.offset - self.default_limit

        return replace_query_param(url, self.offset_query_param, offset)


@csrf_exempt
@require_POST
def webhook_endpoint(request):
    log.msg('Inside Mock Merchant Webhook Endpoint')
    return HttpResponse(status=200)
