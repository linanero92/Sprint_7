import requests
from urls import BASE_URL, COURIERS_URL
from helpers import Generator
from data import Data
import allure


class CourierMethods:

    @allure.step("Создание нового курьера без заполнения поля 'Имя'")
    def register_new_courier_without_first_name(self):
        generator = Generator()
        login_pass = []
        login = generator.generate_random_string(length=8)
        password = generator.generate_random_string(length=8)

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)

        return response.status_code, response.text, login_pass

    @allure.step("Попытка создания нового курьера без ввода пароля")
    def try_register_new_courier_without_password(self):
        generator = Generator()
        login = generator.generate_random_string(length=8)
        first_name = generator.generate_random_string(length=8)

        payload = {
            "login": login,
            "firstName": first_name
        }

        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)
        return response.status_code, response.json()['message']

    @allure.step("Попытка создания курьеров с одинаковыми данными")
    def try_register_same_couriers(self):
        payload = Data.courier_data_for_registration_same_courier
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)
        return response.status_code, response.json()['message']

    @allure.step("Авторизация курьера в системе")
    def courier_auth(self):
        generator = Generator()
        st_code_c, text_c, courier_data = generator.register_new_courier()

        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }

        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=payload)
        response_json = response.json()
        return response.status_code, response.text, response_json.get("id")

    @allure.step("Попытка авторизации курьера в системе с невалидным логином")
    def courier_auth_with_wrong_login(self):
        payload = Data.courier_data_with_wrong_login
        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=payload)
        return response.status_code, response.json()['message']

    @allure.step("Попытка авторизации курьера в системе с невалидным паролем")
    def courier_auth_with_wrong_password(self):
        payload = Data.courier_data_with_wrong_password
        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=payload)
        return response.status_code, response.json()['message']

    @allure.step("Попытка авторизации курьера в системе без заполнения поля 'Логина'")
    def courier_auth_without_login(self):
        payload = Data.courier_data_without_login
        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=payload)
        return response.status_code, response.json()['message']

    @allure.step("Удаление курьера")
    def delete_courier(self):
        status_code, response_text, courier_id = self.courier_auth()

        payload = {
            "id": courier_id
        }

        response = requests.delete(f"{BASE_URL}{COURIERS_URL}{courier_id}", json=payload)
        return response.status_code, response.text

    @allure.step("Попытка удаления курьера с вводом невалидного id")
    def delete_courier_with_wrong_id(self):

        payload = {
            "id": "0"
        }

        response = requests.delete(f"{BASE_URL}{COURIERS_URL}0", json=payload)
        return response.status_code, response.json()["message"]

    @allure.step("Попытка удаления курьера без ввода id")
    def delete_courier_without_id(self):

        payload = {
            "id": ""
        }

        response = requests.delete(f"{BASE_URL}{COURIERS_URL}", json=payload)
        return response.status_code, response.json()["message"]
