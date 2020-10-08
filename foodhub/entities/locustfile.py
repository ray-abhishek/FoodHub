import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("")

    @task
    def view_merchants(self):
        self.client.get("/merchants/", auth=("admin", "admin"))

    @task
    def view_orders(self):
        self.client.get("/orders/", auth=("admin", "admin"))

    @task
    def view_stores(self):
        self.client.get("/stores/", auth=("admin", "admin"))

    @task
    def view_items(self):
        self.client.get("/items/", auth=("admin", "admin"))
