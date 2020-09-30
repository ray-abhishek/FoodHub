from django.contrib import admin
from entities.models import Merchant, Item, Store, Order
# Register your models here.

models_iterable = [Merchant, Item, Store, Order]

admin.site.register(models_iterable)
