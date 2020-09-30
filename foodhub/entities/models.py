from django.db import models


# Field Choices

class OrderStatus(models.TextChoices):
    ACTIVE = 'ACT', 'Active'
    CANCELLED = 'CAN', 'Cancelled'
    FINISHED = 'FIN', 'Finished'


# Table Models

class Merchant(models.Model):
    """
    Merchants like KFC etc are represented by this model.

    Optional Fields : Email
    """
    name = models.CharField("Name", max_length=150)
    email = models.EmailField("Email", max_length=254, blank=True)
    phone = models.CharField("Phone", max_length=20)
    created_at = models.DateTimeField(
        "Created At", auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Food Items are represented by this model.

    Optional Fields : Description
    """
    name = models.CharField("Name", max_length=200)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    cost = models.DecimalField("Cost", max_digits=10, decimal_places=2)
    description = models.TextField("Description", blank=True)
    created_at = models.DateTimeField(
        "Created At", auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    """
    Merchant's stores are represented by this model.

    Optional Fields : address, lon(longitude), lat(latitude)
    """
    name = models.CharField("Name", max_length=150)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    address = models.TextField("Address", blank=True)
    lon = models.FloatField("Longitude", blank=True, null=True)
    lat = models.FloatField("Latitude", blank=True, null=True)
    active = models.BooleanField("Active", default=False)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(
        "Created At", auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.merchant} : {self.name}'


class Order(models.Model):
    """
    Orders are represented by this model.
    """
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    total_cost = models.DecimalField(
        "Total Cost", max_digits=10, decimal_places=2)
    status = models.CharField("Order Status",
                              max_length=100,
                              choices=OrderStatus.choices, default=OrderStatus.ACTIVE)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(
        "Created At", auto_now_add=True, null=True)
