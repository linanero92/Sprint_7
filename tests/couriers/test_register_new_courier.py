from methods.courier_methods import CourierMethods


class TestCreateCourier:

    def test_register_new_courier(self):
        courier_methods = CourierMethods()
        status_code, response_context, login_pass = courier_methods.register_new_courier_and_return_login_password()
        assert status_code == 201
        assert response_context == '{"ok":true}'
        assert login_pass is not None

    def test_register_new_courier_without_first_name(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.register_new_courier_without_first_name()
        assert status_code == 201
        assert response_context == '{"ok":true}'

    def test_register_new_courier_without_login(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.try_register_new_courier_without_login()
        assert status_code == 400
        assert response_context == "Недостаточно данных для создания учетной записи"

    def test_register_two_same_couriers(self):
        courier_methods = CourierMethods()
        courier_methods.try_register_same_couriers()
        status_code, response_context = courier_methods.try_register_same_couriers()
        assert status_code == 409
        assert response_context == "Этот логин уже используется. Попробуйте другой."
