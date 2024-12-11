import random
import string
from faker import Faker

fake = Faker()


class Generator:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def order_data():
        data_order = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": 1,
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
            "metroStation": 12,
            "phone": "89665677878",
            "rentTime": fake.random_int(1, 24),
            "deliveryDate": fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
            "comment": fake.text(20)
        }
        return data_order


