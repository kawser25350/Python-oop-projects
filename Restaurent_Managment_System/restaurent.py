from menu import Menu
from employee import Employee
class Restaurent:
    def __init__(self,name,Address):
        self.name=name
        self.address=Address
        self.employee=Employee()
        self.menu=Menu()
        