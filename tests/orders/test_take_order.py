from methods.order_methods import OrderMethods
import allure


class TestTakeOrder:

    @allure.title("Проверка принятия заказа")
    def test_take_order(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.take_order()
        assert status_code == 200
        assert response_context == '{"ok":true}'

    @allure.title("Проверка принятия заказа без ввода id заказа")
    def test_take_order_without_order_id(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.take_order_without_order_id()
        assert status_code == 400
        assert response_context == "Недостаточно данных для поиска"

    @allure.title("Проверка принятия заказа без ввода id курьера")
    def test_take_order_without_courier_id(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.take_order_without_courier_id()
        assert status_code == 400
        assert response_context == "Недостаточно данных для поиска"

    @allure.title("Проверка принятия заказа, используя невалидный id заказа")
    def test_take_order_with_wrong_order_id(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.take_order_with_wrong_order_id()
        assert status_code == 404
        assert response_context == "Заказа с таким id не существует"

    @allure.title("Проверка принятия заказа, используя невалидный id курьера")
    def test_take_order_with_wrong_courier_id(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.take_order_with_wrong_courier_id()
        assert status_code == 404
        assert response_context == "Курьера с таким id не существует"
