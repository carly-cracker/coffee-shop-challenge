from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self,customer,coffee,price):
        if not isinstance(customer, Customer):
            raise TypeError ("the customer must be an object instance of Customer") 
        self._customer = customer
        if not isinstance(coffee, Coffee):
            raise TypeError ("the coffee name must be an object insctance of Coffee")
        self._coffee = coffee
        if not isinstance(price, float) or not  (1.0<= price <=10.0):
            raise ValueError("the price must be between 1.0 - 10.0")
        self._price = float(price)


    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

if __name__ == "__main__":
    from coffee import Coffee
    from order import Order

    alice = Customer("alice")

    bob = Customer("bob")
    latte = Coffee("latte")
    cappuchinno= Coffee("cappuchinno")
    order1 = alice.create_order(latte, 4.7)
    order2 = bob.create_order(cappuchinno, 8.0)
    print(alice.name)
    print(order1.price)
    print(order1.customer.name)
    print(order1.coffee.name)
    print(order2.coffee.name)
    print("total orders for latte:",latte.num_orders())

