import pytest
from coffee import Coffee
from customer import Customer

def test_valid_name():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_invalid_name_type():
    with pytest.raises(ValueError):
        Coffee(123)

def test_invalid_name_length():
    with pytest.raises(ValueError):
        Coffee("Hi")

def test_orders_customers_num_orders_average_price():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Latte")
    order1 = customer1.create_order(coffee, 4.0)
    order2 = customer1.create_order(coffee, 5.0)
    order3 = customer2.create_order(coffee, 6.0)

    assert order1 in coffee.orders()
    assert order2 in coffee.orders()
    assert order3 in coffee.orders()
    
    customers = coffee.customers()
    assert customer1 in customers and customer2 in customers
    
    assert coffee.num_orders() == 3
    
    expected_avg = (4.0 + 5.0 + 6.0) / 3
    assert abs(coffee.average_price() - expected_avg) < 0.01

def test_average_price_no_orders():
    coffee = Coffee("Americano")
    assert coffee.average_price() == 0
