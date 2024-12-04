
from abc import ABC

class Order:
    def __init__(self,items):
        self.bill=0
        self.items=items
        for i in items:
            self.bill+=i.price
    
class User(ABC):
    def __init__(self,id,name,phone,address):
        self.id=id
        self.name=name
        self.phone=phone
        self.address=address

class Customer(User):
    def __init__(self, id, name, phone, address):
        super().__init__(id, name, phone, address)
    
    def add_order(self,restaurent,id,order):
        restaurent.add_order(order)

    def pay_bill(self,restaurent,id,bill):
        restaurent.pay_bill(id,bill)
    
    def show_bill(self,restaurent,id):
        restaurent.show_bill(id)
    

    def check:
        pass
    
    


        









                                       