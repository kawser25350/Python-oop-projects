
from employee_menu import Employeemenu
from food_menu import Foodmenu


class Rastaurent:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.foodmenu=Foodmenu()
        self.employeemenu=Employeemenu()
        self.adminlist={}
        self.customerlist={}
    
    def view_menu(self):
        for keys,item in self.foodmenu.fooditems.items():
            print(f"\nCategory:{keys}")
            for x in item:
                print(x)
                
    # more functionality for only reastaurent 
    # where admin can see revinue and and pay salary of employee 
    #
