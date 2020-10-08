from entities.models import Merchant, Item, Store, Order
from celery.decorators import task
import structlog

log = structlog.get_logger()


@task(name="create_order")
def create_order(data):
    merchant_instance = Merchant.objects.filter(pk=data['merchant']).first()
    store_instance = Store.objects.filter(pk=data['store']).first()
    items = data.pop('items')
    order_instance = Order.objects.create(
        merchant=merchant_instance, store=store_instance, total_cost=data['total_cost'])
    order_instance.items.set(items)
    log.msg('Order Created', orderID=order_instance.id)


"""
@task(name="create_random_orders")
def create_random_orders(num_of_orders):
    if num_of_orders < 0:
        return
    present, store, item = get_item_store()
    if not present:
        return
    for _ in range(num_of_orders):
        order = Order.objects.create(
            merchant=item.merchant, store=store, total_cost=item.cost)
        order.items.set([item])
        print(order.id)


def get_item():
    items = Item.objects.all()
    for item in items:
        yield item


def get_item_store():

    item = get_item()
    store = None
    while True:
        try:
            current_item = next(item)
            store = Store.objects.filter(
                merchant=current_item.merchant).first()
        except StopIteration:
            return False, None, None
        finally:
            if store is not None:
                return True, store, current_item
"""
