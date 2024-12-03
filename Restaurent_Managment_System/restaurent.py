from foodmenus import Food_menu
from employeemenu import Employeemenu

class Restaurent:
    def __init__(self,name,Address):
        self.name=name
        self.address=Address
        self.employemenue=Employeemenu()                           
        self.foodmenu=Food_menu()
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
                

                


              
    
                                                                         