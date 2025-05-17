from customer import Customer
from coffee import Coffee


alice = Customer("Alice")
bob = Customer("Bob")
mill =  Customer("Mill")

latte = Coffee("Latte")
espresso = Coffee("Espresso")


alice.create_order(latte, 4.5)
alice.create_order(latte, 5.0)
bob.create_order(espresso, 3.5)
bob.create_order(latte, 5.5)
mill.create_order(espresso, 7.8)

print("Latte - Total Orders:", latte.num_orders())  
print("Latte - Average Price:", round(latte.average_price(), 2))  
print("Espresso - Total Orders:", espresso.num_orders())  
print("Espresso - Average Price:", espresso.average_price())  


print("Alice's Coffees:", [c.name for c in alice.coffees()])  
print("Bob's Coffees:", [c.name for c in bob.coffees()]) 