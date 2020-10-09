from entities.models import Merchant, Store, Order
from celery.decorators import task
import structlog

log = structlog.get_logger()


@task(name="create_order")
def create_order(data):
    """
    This function is used to create Order asynchronously.
    """
    merchant_instance = Merchant.objects.filter(pk=data['merchant']).first()
    store_instance = Store.objects.filter(pk=data['store']).first()
    items = data.pop('items')
    order_instance = Order.objects.create(
        merchant=merchant_instance, store=store_instance,
        total_cost=data['total_cost'])
    order_instance.items.set(items)
    log.msg('Order Created', orderID=order_instance.id)
