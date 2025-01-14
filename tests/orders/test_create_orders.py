import pytest
from methods.order_methods import OrderMethods
import allure


class TestCreateOrders:

    @allure.title("Проверка создания заказа")
    @pytest.mark.parametrize('colors', [
        ['BLACK', 'GREY'],
        ['BLACK'],
        ['GREY'],
        ['']
    ])
    def test_create_order_with_all_color_of_scooter(self, colors):
        order_methods = OrderMethods()
        status_code, response_context, order_id = order_methods.create_new_order()
        assert status_code == 201
        assert 'track' in response_context
        assert order_id is not None

    @allure.title("Проверка создания заказа без параметра выбора цвета самоката")
    def test_create_order_without_color_param(self):
        order_methods = OrderMethods()
        status_code, response_context, order_id = order_methods.create_order_without_color_param()
        assert status_code == 201
        assert 'track' in response_context
        assert order_id is not None
