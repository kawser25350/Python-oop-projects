
class Food_menu:
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
        print("fooditem added succesfully!")

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


