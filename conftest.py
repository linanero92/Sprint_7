import pytest
from methods.courier_methods import CourierMethods

@pytest.fixture()
def courier():
    response = CourierMethods().courier_auth()
    yield response.json()['id']
    CourierMethods().delete_courier(response.json()['id'])
