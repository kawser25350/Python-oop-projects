
from abc import ABC,abstractmethod

class Food(ABC):
    def __init__(self,name,price,quantity):
        self.name=name 
        self.price=price
        self.quantity=int(quantity)
        

    def __repr__(self):
        return f"Food Name:{self.name} Price:{self.price} Quantity:{self.quantity}"
    
