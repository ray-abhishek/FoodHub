from entities.models import Merchant, Item, Store, Order
from celery.decorators import task


@task(name="create_orders")
def create_orders(num_of_orders):
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
