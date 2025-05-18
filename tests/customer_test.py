import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_valid_name():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_invalid_name_type():
    with pytest.raises(ValueError):
        Customer(123)

def test_invalid_name_length():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("ANameThatIsWayTooLong")

def test_orders_and_coffees():
    customer = Customer("Alice")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    order1 = customer.create_order(coffee1, 4.5)
    order2 = customer.create_order(coffee2, 3.5)

    orders = customer.orders()
    assert len(orders) == 2
    assert orders[0].coffee == coffee1
    assert orders[0].price == 4.5
    assert orders[1].coffee == coffee2
    assert orders[1].price == 3.5

def test_create_order_returns_order():
    customer = Customer("Bob")
    coffee = Coffee("Mocha")
    order = customer.create_order(coffee, 6.0)
    assert order in customer.orders()
    assert order.price == 6.0
