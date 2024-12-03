from users import *
from restaurent import Restaurent
from fooditem import *

if __name__ == "__main__":
     

    r1=Restaurent("mamar restaurent","mohammadpur")

    f1=Pizza("chessy",1200,10)
    r1.fmenu.add_food("pizza",f1)
    r1.fmenu.show_food()

# c1=Customer(1,"kawser","23059432","mohmmadpur")