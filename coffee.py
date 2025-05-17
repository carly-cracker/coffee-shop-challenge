class Coffee:
    def __init__(self,name):
        if isinstance (name, str) and 1<= len(name) <=3:
            self._name = name
        else:
            raise ValueError("coffee name must be a string of 3 char")
    @property
    def name(self):
        return self._name
