from urls import BASE_URL, ORDERS_URL
from methods.courier_methods import CourierMethods
from helpers import Generator
import requests
import allure


class OrderMethods:

    @allure.step("Создание нового заказа")
    def create_new_order(self):
        generator = Generator()
        payload = generator.order_data()
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=payload)
        return response.status_code, response.text, response.json().get("track")

    @allure.step("Создание нового заказа без ввода цаета самоката")
    def create_order_without_color_param(self):
        generator = Generator()
        payload = generator.order_data_without_color()
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", data=payload)
        return response.status_code, response.text, response.json()["track"]

    @allure.step("Получение списка заказов")
    def get_orders_list(self):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}?courierId=434108&limit=5")
        return response.status_code, response.json()['orders']

    @allure.step("Принять заказ")
    def take_order(self):
        st_code_or, text_or, order_id = self.create_new_order()
        courier_methods = CourierMethods()
        st_code_c, text_c, courier_id = courier_methods.courier_auth()
        response = requests.put(f"{BASE_URL}{ORDERS_URL}accept/{order_id}?courierId={courier_id}")
        return response.status_code, response.text

    @allure.step("Попытка принять заказ без ввода id заказа")
    def take_order_without_order_id(self):
        courier_methods = CourierMethods()
        st_code_c, text_c, courier_id = courier_methods.courier_auth()
        response = requests.put(f"{BASE_URL}{ORDERS_URL}accept/courierId={courier_id}")
        return response.status_code, response.json()["message"]

    @allure.step("Попытка принять заказ без ввода id курьера")
    def take_order_without_courier_id(self):
        order_track = self.create_new_order()
        order_id = int(order_track[2])
        response = requests.put(f"{BASE_URL}{ORDERS_URL}accept/{order_id}?")
        return response.status_code, response.json()["message"]

    @allure.step("Попытка принять заказ, используя невалидный id заказа")
    def take_order_with_wrong_order_id(self):
        courier_methods = CourierMethods()
        st_code_c, text_c, courier_id = courier_methods.courier_auth()
        response = requests.put(f"{BASE_URL}{ORDERS_URL}accept/0?courierId={courier_id}")
        return response.status_code, response.json()["message"]

    @allure.step("Попытка принять заказ, используя невалидный id курьера")
    def take_order_with_wrong_courier_id(self):
        order_track = self.create_new_order()
        order_id = int(order_track[2])
        response = requests.put(f"{BASE_URL}{ORDERS_URL}accept/{order_id}?courierId=0")
        return response.status_code, response.json()["message"]

    @allure.step("Получение заказа по id заказа")
    def get_order(self):
        st_code_o, text_o, order_track = self.create_new_order()
        response = requests.get(f"{BASE_URL}{ORDERS_URL}track?t={order_track}")
        return response.status_code, response.text

    @allure.step("Попытка получения заказа без ввода id заказа")
    def get_order_without_order_id(self):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}track?t=")
        return response.status_code, response.json()["message"]

    @allure.step("Попытка получения заказа используя невалидный id заказа")
    def get_order_with_wrong_order_id(self):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}track?t=0")
        return response.status_code, response.json()["message"]
