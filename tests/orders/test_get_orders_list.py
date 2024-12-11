from methods.order_methods import OrderMethods


class TestGetOrdersList:

    def test_get_orders_list(self):
        order_methods = OrderMethods()
        status_code, response_context = order_methods.get_orders_list()
        assert status_code == 200
        assert response_context is not None
