from methods.courier_methods import CourierMethods


class TestCourierLogin:

    def test_courier_successful_auth(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.courier_auth()
        assert status_code == 200
        assert "id" in response_context

    def test_courier_auth_with_wrong_login(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.courier_auth_with_wrong_login()
        assert status_code == 404
        assert response_context == "Учетная запись не найдена"

    def test_courier_auth_with_wrong_password(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.courier_auth_with_wrong_password()
        assert status_code == 404
        assert response_context == "Учетная запись не найдена"

    def test_courier_auth_without_login(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.courier_auth_without_login()
        assert status_code == 400
        assert response_context == "Недостаточно данных для входа"