from urls import BASE_URL, ORDERS_URL
from helpers import Generator
import requests


class OrderMethods:

    def create_new_order(self):
        payload = Generator.order_data()
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=payload)
        return response.status_code, response.json()

    def create_order_without_color_param(self):
        payload = Generator.order_data_without_color()
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=payload)
        return response.status_code, response.json()

    def get_orders_list(self):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}?courierId=434108&limit=5")
        return response.status_code, response.json()['orders']

