import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_valid_order():
    customer = Customer("Charlie")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 5.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.5
    assert order in customer.orders()
    assert order in coffee.orders()

def test_invalid_customer_type():
    coffee = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("NotCustomer", coffee, 5.0)

def test_invalid_coffee_type():
    customer = Customer("Dave")
    with pytest.raises(TypeError):
        Order(customer, "NotCoffee", 5.0)

def test_invalid_price_type():
    customer = Customer("Eve")
    coffee = Coffee("Mocha")
    with pytest.raises(ValueError):
        Order(customer, coffee, "cheap")

def test_price_out_of_bounds():
    customer = Customer("Eve")
    coffee = Coffee("Mocha")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)
