from django.db import models


# Field Choices

class OrderStatus(models.TextChoices):
    ACTIVE = 'ACT', 'Active'
    CANCELLED = 'CAN', 'Cancelled'
    FINISHED = 'FIN', 'Finished'


# Table Models

class Merchant(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=150)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    address = models.TextField()
    lon = models.FloatField()
    lat = models.FloatField()
    active = models.BooleanField(default=False)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=100,
        choices=OrderStatus.choices, default=OrderStatus.ACTIVE)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
