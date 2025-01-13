from methods.courier_methods import CourierMethods
from error_messages import *
import allure


class TestDeleteCourier:

    @allure.title("Проверка удаления курьера")
    def test_delete_courier_successful(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.delete_courier()
        assert status_code == 200
        assert response_context == '{"ok":true}'

    @allure.title("Проверка удаления курьера, используя невалидный id курьера")
    def test_delete_courier_with_wrong_id(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.delete_courier_with_wrong_id()
        assert status_code == 404
        assert response_context == WRONG_COURIER_ID

    @allure.title("Проверка удаления курьера без ввода id курьера")
    def test_delete_courier_without_id(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.delete_courier_without_id()
        assert status_code == 404
        assert response_context == NOT_FOUND
