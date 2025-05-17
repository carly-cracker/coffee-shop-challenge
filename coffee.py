class Coffee:
    def __init__(self,name):
        if isinstance (name, str) and 3 <= len(name) :
            self._name = name
        else:
            raise ValueError("coffee name must be a string of 3 char")
        self._orders = []

    @property
    def name(self):
        return self._name
    
    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})
    
    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if self._orders:
            return sum(order.price for order in self._orders) / len(self._orders)
        return 0


