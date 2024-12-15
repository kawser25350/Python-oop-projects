from fooditem import Food

class Foodmenu:

    def __init__(self):
        self.fooditems = {
            "pizza": [],
            "biriyani": [],
            "colddrinks": [],
            "deserts": []
        }
    
    def add_food(self, category, food):
        if category in self.fooditems:
            if food in self.fooditems[category]:
                print(f"{food.name} is already exists in {category} category!")
                return
            self.fooditems[category].append(food)
            print(f"Food '{food.name}' successfully added to {category} category!.")
        else:
            print(f"Category '{category}' not found!")
    
    def delete_food(self, category, foodname):
        if category in self.fooditems:
            # Iterate and remove the food item if found
            for foodobj in self.fooditems[category]:
                if foodname == foodobj.name:
                    self.fooditems[category].remove(foodobj)
                    print(f"Food '{foodname}' successfully removed from {category} category!.")
                    return
            print(f"Food '{foodname}' not found in {category}.")
        else:
            print(f"Category '{category}' not found!")
