import requests
from urls import BASE_URL, COURIERS_URL
from helpers import Generator
from data import Data


class CourierMethods:

    def register_new_courier_and_return_login_password(self):

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = Generator.generate_random_string(10)
        password = Generator.generate_random_string(10)
        first_name = Generator.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращает словарь
        return payload

    def register_new_courier_return_list(self):
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
            login_pass = [login, password, first_name]

        return login_pass

    def register_new_courier_without_first_name(self):
        login_pass = []
        login = Generator.generate_random_string(length=8)
        password = Generator.generate_random_string(length=8)

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)

        return response.status_code, response.text, login_pass

    def try_register_new_courier_without_login(self):
        login = Generator.generate_random_string(length=8)
        first_name = Generator.generate_random_string(length=8)

        payload = {
            "login": login,
            "firstName": first_name
        }

        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)
        return response.status_code, response.json()['message']

    def try_register_same_couriers(self):
        payload = Data.courier_data_for_registration_same_courier
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)
        return response.status_code, response.json()['message']

    def courier_auth(self):
        courier_data = self.register_new_courier_return_list()

        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }

        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=payload)
        return response.status_code, response.text, response.json().get("id")

    def courier_auth_with_wrong_login(self):
        payload = Data.courier_data_with_wrong_login
        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=payload)
        return response.status_code, response.json()['message']

    def courier_auth_with_wrong_password(self):
        payload = Data.courier_data_with_wrong_password
        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=payload)
        return response.status_code, response.json()['message']

    def courier_auth_without_login(self):
        payload = Data.courier_data_auth["password"]
        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=payload)
        return response.status_code, response.json()['message']

    def delete_courier(self):
        status_code, response_text, courier_id = self.courier_auth()

        payload = {
            "id": courier_id
        }

        response = requests.delete(f"{BASE_URL}{COURIERS_URL}{courier_id}", json=payload)
        return response.status_code, response.text

    def delete_courier_with_wrong_id(self):

        payload = {
            "id": "0"
        }

        response = requests.delete(f"{BASE_URL}{COURIERS_URL}0", json=payload)
        return response.status_code, response.json()["message"]

    def delete_courier_without_id(self):

        payload = {
            "id": ""
        }

        response = requests.delete(f"{BASE_URL}{COURIERS_URL}", json=payload)
        return response.status_code, response.json()["message"]