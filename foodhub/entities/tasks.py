from entities.serializers import OrderSerializer
from entities.models import Merchant, Store, Order
from celery.decorators import task
from django.db.utils import OperationalError
import structlog
import requests

log = structlog.get_logger()


@task(name="create_order", autoretry_for=(OperationalError,), retry_kwargs={
    'max_retries': 5,
    'countdown': 2})
def create_order(data):
    """
    This function is used to create Order asynchronously.
    """
    log.msg('Creating Order ', initial_data=data)
    merchant_instance = Merchant.objects.filter(pk=data['merchant']).first()
    store_instance = Store.objects.filter(pk=data['store']).first()
    items = data['items']
    order_instance = Order.objects.create(
        merchant=merchant_instance, store=store_instance,
        total_cost=data['total_cost'])
    order_instance.items.set(items)
    log.msg('Order Created', orderID=order_instance.id)
    serialized_order = OrderSerializer(order_instance)
    log.msg('Serialized Order Data', data=serialized_order.data)
    return serialized_order.data


@task(name="relay_order", autoretry_for=(Exception,), retry_kwargs={
    'max_retries': 5,
    'countdown': 2}, retry_backoff=True)
def relay_order(data):
    """
    Sends Order Details through POST Request to Merchant's URL webhook.

    Arguments :
    data : Serialized Order Data 
    """
    log.msg('Enter Order Relay', json=data)

    response = requests.post(
        'http://e3253a83fce4.ngrok.io/webhook/', params=data)
    log.msg('Response Code ', status=response.status_code)
