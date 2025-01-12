from methods.courier_methods import CourierMethods
import allure


class TestCreateCourier:

    @allure.title("Проверка создания нового курьера")
    def test_register_new_courier(self):
        courier_methods = CourierMethods()
        status_code, response_context, login_pass = courier_methods.register_new_courier_without_first_name()
        assert status_code == 201
        assert response_context == '{"ok":true}'
        assert login_pass is not None

    @allure.title("Проверка создания нового курьера без ввода пароля")
    def test_register_new_courier_without_password(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.try_register_new_courier_without_password()
        assert status_code == 400
        assert response_context == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка создания нового курьера с одинаковыми данными")
    def test_register_two_same_couriers(self):
        courier_methods = CourierMethods()
        courier_methods.try_register_same_couriers()
        status_code, response_context = courier_methods.try_register_same_couriers()
        assert status_code == 409
        assert response_context == "Этот логин уже используется. Попробуйте другой."
