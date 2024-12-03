
class Food:
    def __init__(self,name,quantity,price):
         
        self.__name=name
        self.quantity=quantity
        self.__price=price
    
    @property
    def name(self):
        return self.__name
    @property
    def quantity(self):
        return self.quantity


class Pizza(Food):
    pass
class Coke(Food):
    pass
class Burger(Food):
    pass
class Frenchfry(Food):
    pass

