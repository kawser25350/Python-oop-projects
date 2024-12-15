from user import User

class Customer(User):
    def __init__(self, user_name, contact, address):
        super().__init__(user_name, contact, address)
        self.cart = []
        self.bill = 0

    def order_food(self, restaurant, category, foodname):
        if category in restaurant.foodmenu.fooditems:
            foodlist = restaurant.foodmenu.fooditems[category]  # Get the specific category list

            for fd in foodlist:
                if fd.name == foodname:
                    if fd.quantity > 0:
                        self.cart.append(fd)
                        fd.quantity -= 1  # Reduce stock by 1
                        print(f"'{foodname}' added to your cart.")
                        return  # Exit after adding the food
                    else:
                        print(f"'{foodname}' is out of stock!")
                        return
            print(f"'{foodname}' not found in {category}.")
        else:
            print(f"Category '{category}' not found!")
    
  
  
  
  
    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for food in self.cart:
                food.display()  # Assuming `display()` is defined in the Food class
    
    def show_bill(self):
        self.__calcualte_bill()
        print(f"your total bill is {self.bill}")
    

    def pay_bill(self,money):
        self.__calcualte_bill()
        
        if self.bill > money:
            self.bill-= money
            print(f"you have to pay {self.bill} more Taka!")
            
        elif self.bill < money:
            print(f"paid! returnable money is {money-self.bill} Taka")
            self.bill=0
        else:
            print("Paid full ")

    def __calcualte_bill(self):
        for x in self.cart:
            self.bill+=x.price