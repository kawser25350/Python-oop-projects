from users import *
from restaurent import Restaurent
from fooditem import *

r1=Restaurent("mamar restaurent","mohammadpur")

f1=Pizza("chessy",1200,10)
r1.foodmenu.add_food("pizza",f1)
r1.foodmenu.show_food()

# c1=Customer(1,"kawser","23059432","mohmmadpur")