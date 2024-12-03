from fooditem import *

class Menu:
    def __init__(self):
        self.__menu = {
            "pizza": {},
            "burger": {},
            "drinks": {},
            "coffee": {}
        }

    def add_food(self, category, item):
        if category in self.__menu:
            foodmap = self.__menu[category]
            if item.name in foodmap:
                foodmap[item.name] += item.quantity
            else:
                foodmap[item.name] = item
        else:
            self.__menu[category] = {}  # Creating a new category for food
            foodmap = self.__menu[category]
            foodmap[item.name] = item

    def remove_food(self, category, itemname):
        if category in self.__menu:
            foodmap = self.__menu[category]
            if itemname in foodmap:
                del foodmap[itemname]
                print(f"Successfully removed {itemname}")
            else:
                print("item no availavle")
        else:
            print("Category does not exist")

    def show_food(self):
        for category, items in self.__menu.items():  
           
            print("\t",category)
            for item in items.values():  
                print(f"Name:{item.name} Price:{item.price} Quantiry:{item.quantity}")
            print()


m1 = Menu()

fooditem = Pizza("cheese_pizza", 250, 5)  # Example food item
m1.add_food("pizza", fooditem)
m1.show_food()
m1.remove_food("pizza","cheese_pizza")
m1.show_food()
