from methods.order_methods import OrderMethods
import allure


class TestGetOrder:

    @allure.title("Проверка получения заказа")
    def test_get_order(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.get_order()
        assert status_code == 200
        assert "id" in response_context

    @allure.title("Проверка получения заказа без ввода id заказа")
    def test_get_order_without_order_id(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.get_order_without_order_id()
        assert status_code == 400
        assert response_context == "Недостаточно данных для поиска"

    @allure.title("Проверка получения заказа, используя невалидный id заказа")
    def test_et_order_with_wrong_order_id(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.get_order_with_wrong_order_id()
        assert status_code == 404
        assert response_context == "Заказ не найден"
