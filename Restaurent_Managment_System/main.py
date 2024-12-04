from users import *
from restaurent import Restaurent
from fooditem import *


     

r1=Restaurent("mamar restaurent","mohammadpur")


# f1=Pizza("chessy",1200,10)
# r1.fmenu.add_food("pizza",f1)

# c1=Customer(1,"kawser","23059432","mohmmadpur")
# c1.add_order(r1,c1.id,f1)
# c1.add_order(r1,c1.id,f1)
 
# c1.show_bill(r1,c1.id)

ad=Admin(1,"kawser",982347,"mohammadpur",)
e1=Employee(23,"shuvo",3422,"mohammadpur",23324.23)
 
ct="staf"
ad.add_employees(r1,ct,e1)
ad.show_employees(r1)
print()
ad.remove_employee(r1,"staf",23)
print()
ad.show_employees(r1)
