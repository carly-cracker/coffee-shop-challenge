class Customer:
    def __init__(self,name): 
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,val):
        if isinstance(val, str) and 1<=len(val)<=15:
            self._val = val
        else:
            raise ValueError("Name must be a string btwn 1 and 15 char")