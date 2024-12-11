import pytest
from methods.order_methods import OrderMethods


class TestCreateOrders:

    @pytest.mark.parametrize('colors', [
        ['BLACK', 'GREY'],
        ['BLACK'],
        ['GREY'],
        ['']
    ])
    def test_create_order_with_all_color_of_scooter(self, colors):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.create_new_order()
        assert status_code == 201
        assert 'track' in response_context

    def test_create_order_without_color_param(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.create_order_without_color_param()
        assert status_code == 201
        assert 'track' in response_context
