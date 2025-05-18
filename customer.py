from coffee import Coffee

class Customer:
    def __init__(self,name): 
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,val):
        if isinstance(val, str) and 1<=len(val)<=15:
            self._name = val
        else:
            raise ValueError("Name must be a string btwn 1 and 15 char")
       
    def orders(self):
        return self._orders
    
    def coffees(self):
        return {order.coffee for order in self._orders}
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price) 

    
