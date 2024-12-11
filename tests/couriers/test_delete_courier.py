from methods.courier_methods import CourierMethods


class TestDeleteCourier:

    def test_delete_courier_successful(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.delete_courier()
        assert status_code == 200
        assert response_context == '{"ok":true}'

    def test_delete_courier_with_wrong_id(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.delete_courier_with_wrong_id()
        assert status_code == 404
        assert response_context == "Курьера с таким id нет."

    def test_delete_courier_without_id(self):
        courier_methods = CourierMethods()
        status_code, response_context = courier_methods.delete_courier_without_id()
        assert status_code == 404
        assert response_context == "Not Found."
