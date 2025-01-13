import pytest
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier():
    response = CourierMethods().courier_auth()
    response_json = response.json()
    yield response_json("id")
    CourierMethods().delete_courier()


@pytest.fixture
def courier_without_first_name():
    response = CourierMethods().auth_of_courier_without_first_name()
    response_json = response.json()
    yield response_json("id")
    CourierMethods().delete_courier_without_first_name()
