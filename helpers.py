import random
import string
from faker import Faker
import requests
from urls import *
import allure

fake = Faker()


class Generator:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @allure.step("Регистрация нового курьера")
    def register_new_courier(self):
        login_pass = []
        login = Generator.generate_random_string(10)
        password = Generator.generate_random_string(10)
        first_name = Generator.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return response.status_code, response.text, login_pass

    @staticmethod
    def order_data():
        data_order = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": "2",
            "phone": "89665677878",
            "rentTime": fake.random_int(1, 24),
            "deliveryDate": fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
            "comment": fake.text(15),
            "color": []
        }
        return data_order

    @staticmethod
    def order_data_without_color():
        data_order = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": "3",
            "phone": "89665677878",
            "rentTime": fake.random_int(1, 24),
            "deliveryDate": fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
            "comment": fake.text(20)
        }
        return data_order
