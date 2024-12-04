
from foodmenu import Food_menu
from employeemenu import Employee_menu

class Restaurent:
    def __init__(self,name,Address):
        self.name=name
        self.address=Address
        self.emenu=Employee_menu()                           
        self.fmenu=Food_menu()
        self.orders={
            "customerid":[]
        }
        
    def add_order(self,id,orders):
        if id not in self.orders:
            self.orders[id] = []
        self.orders[id].append(orders)

        
    def show_bill(self,customerid):
        bill=0
        if customerid in self.orders:
            order=self.orders[customerid]

            for x in order:
                bill+=x.price
            
            print(bill)
            
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
            
    def add_employee(self,category,employee):
        self.emenu.add_employee(category,employee)

    def remove_employee(self,category,empid):
        self.emenu.remove_employee(category,id)

    def add_food(self,category,item):
        self.fmenu.add_food(category,item)
    
    def remove_food(self,category,itemname):
        self.fmenu.remove_food(category,itemname)
    
    def show_food(self):
        self.fmenu.show_food()

    def show_all_employe(self):
        self.emenu.showall_employee()

    
 
    
    

                


              
    
                                                                         