from foodmenu import Foodmenu
from employeemenu import Employeemenu
from fooditem import *


from users import Customer
class Restaurent:
    def __init__(self,name,Address):
        self.name=name
        self.address=Address
        self.employemenue=Employeemenu()                           
        self.foodmenu=Foodmenu()
        self.orders={
            "customerid":[]
        }
        
        def add_order(self,id,orders):
            orders[id].append(orders)
        
        def show_bill(self,customerid):
            bill=0
            if customerid in self.orders:
                orders=self.orders[customerid]

                for x in orders:
                    bill+=x.bill
                
                return bill
                
            else: 
                print(f"wrong customerId provided!")
                      
        def pay_bill(self,customerid,payment):
            if customerid in self.orders:

                bill=self.show_bill(customerid)

                if payment < bill:
                    print(f"pyment rejected! nedd more{bill} money.")
                elif payment> bill:
                    print(f"you will get return {abs(payment-bill)} money")
                    del self.orders[customerid]
                else:
                    print(f"Thank you bill payed! { payment}  money")
                    del self.orders[customerid]
                

                

r1=Restaurent("mamar restaurent","mohammadpur")

f1=Pizza("chessy",1200,10)
r1.foodmenu.add_food("pizza",f1)
r1.foodmenu.show_food()

# c1=Customer(1,"kawser","23059432","mohmmadpur")
              
    
                                                                         