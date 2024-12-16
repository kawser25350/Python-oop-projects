from user import User


class Admin(User):
    
    
    def add_employee(self,rastaurent,employee):
         rastaurent.employeemenu.add_employee(employee)

    def view_employee_list(self,restaurent):
        restaurent.employeemenu.view_employee();

    def add_item(self,rastaurent,category,food):
        rastaurent.foodmenu.add_food(category,food)

    def delete_items(self,rastaurent,category,foodname):
        rastaurent.foodmenu.delete_food(category,foodname);
    
    def remove_employee(self,rastaurent,employeename):
        rastaurent.employeemenu.delete_employee(employeename);
    

