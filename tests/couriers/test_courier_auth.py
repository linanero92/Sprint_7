from methods.courier_methods import CourierMethods
from error_messages import *
import allure


class TestCourierLogin:

    @allure.title("Проверка авторизации курьера")
    def test_courier_successful_auth(self):
        courier_methods = CourierMethods()
        status_code, response_context, courier_id = courier_methods.courier_auth()
        assert status_code == 200
        assert "id" in response_context
        assert courier_id is not None

    @allure.title("Проверка авторизации курьера, используя невалидный логин")
    def test_courier_auth_with_wrong_login(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.courier_auth_with_wrong_login()
        assert status_code == 404
        assert response_context == ACCOUNT_NOT_FOUND

    @allure.title("Проверка авторизации курьера, используя невалидный пароль")
    def test_courier_auth_with_wrong_password(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.courier_auth_with_wrong_password()
        assert status_code == 404
        assert response_context == ACCOUNT_NOT_FOUND

    @allure.title("Проверка авторизации курьера без ввода логина")
    def test_courier_auth_without_login(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.courier_auth_without_login()
        assert status_code == 400
        assert response_context == NOT_ENOUGH_LOGIN_DATA
