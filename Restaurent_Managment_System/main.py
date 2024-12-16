from rastaurent import Rastaurent
from fooditem import Food
from admin import Admin
from employee import Employee
from customer import Customer

def admin_functional_menu(currentadmin):          #admin functionality
    while True:
        print(f"\nwellcome {currentadmin.user_name}")
        print("1.Add employee.")
        print("2.Reomve employee.")
        print("3.Add food.")
        print("4.Remove food")
        print("5.View food menu.")
        print("6.View all employee.")
        print("7.Logout.")
        x=int(input(">>"))

        if x==1:
            print("\nenter employee information:")
            username=input("USERNAME:")
            contact=str(input("CONTACT:"))
            address=input("ADDRESS:")
            salary=int(input("SALARY:"))
            emp=Employee(username,contact,address,salary)
            currentadmin.add_employee(r1,emp)
        
        elif x==2:
            empname=input("\nTO remove employye write name of employee:")
            currentadmin.remove_employee(r1,empname)

        elif x==3:
            print("\nenter fooddetails:")
            category=input("enter catagory type first:")
            foodname=input("FOODNAME:")
            price=int(input("PRICE:"))
            quantity=int(input("QUANTITY:"))

            fd=Food(foodname,price,quantity)  ##creating food obj

            currentadmin.add_item(r1,category,fd)

        elif x==4:
            print("\nEnter category and fooditemname to remove:")
            category=input("CATEGORY:")
            foodname=input("FOODNAME:")
            currentadmin.delete_items(r1,category,foodname)
        elif x==5:
            print()
            r1.view_menu()
        elif x==6:
            currentadmin.view_employee_list(r1)
        elif x==7:
            print("log out succesfull!")
            break
        else:
            print("Invalid choice!")



def customer_functional_menu(currentcustomer):          #customer functionality
    while True:
        print(f"\nwellcome {currentcustomer.user_name}")
        print("1.Show food menu.")
        print("2.Order food.")
        print("3.Show cart.")
        print("4.Show bill.")
        print("5.Pay bill.")
        print("6.Logout.")
        x=int(input(">>"))

        if x==1:
            print()
            r1.view_menu()       

        elif x==2:
            print("Write food details to order:")
            category=input("CATEGORY:")
            foodname=input("FOOD NAME:")
            currentcustomer.order_food(r1,category,foodname)

        elif x==3:
            currentcustomer.view_cart()

        elif x==4:
           currentcustomer.show_bill()
        elif x==5:
            payment=input("Enter ammonunt you want to pay!")
            currentcustomer.pay_bill(payment)
          
        elif x==6:
            print("log out succesfull.!")        
            break
       
        else:
            print("Invalid choice!")


def admin_login_menu():
    while True:
        print("\nAdmin Login Menu:")
        print("1.Login(user name).")
        print("2.Register.")
        print("3.exit.") 
        n=int(input(">>"))
        if(n==1):
            username=input("Enter user name to login:")
            if username in r1.adminlist:
                currentadmin=r1.adminlist[username]
                admin_functional_menu(currentadmin) ## calling the admin function menu with the current user admin
            else:
                print(f"{username} not registered yet!")
    
        elif n==2:
            print("please enter your information to register:")
            username=input("USERNAME:")
            contact=str(input("CONTACT NUMBER:"))
            address=input("ADDRESS:")
            a1=Admin(username,contact,address) # createing new admin abject 
            r1.adminlist[username]=a1     # stroing the admin obj to the rastaurent adminlist to save admin user

        elif n==3:
            print("exiting..")
            break
        else:
            print("Invalid choice!")

        

def customer_login_menu():
     while True:
        print("\nCustomer Login Menu:")
        print("1.Login(user name).")
        print("2.Register.")
        print("3.exit.") 
        n=int(input(">>"))
        if(n==1):
            username=input("Enter user name to login:")
            if username in r1.customerlist:
                currentcustomer=r1.customerlist[username]
                customer_functional_menu(currentcustomer) ## calling the customer function menu with the current customer user
            else:
                print(f"{username} not registered yet!")
    
        elif n==2:
            print("please enter your information to register:")
            username=input("USERNAME:")
            contact=str(input("CONTACT NUMBER:"))
            address=input("ADDRESS:")
            c1=Customer(username,contact,address) # createing new customer object 
            r1.customerlist[username]=c1     # stroing the customer obj to the rastaurent's customer list to save customer user

        elif n==3:
            print("exiting..")
            break
        else:
            print("Invalid choice!")
    


r1=Rastaurent("sonargao","sytel") ## creating the rastaurent object 


if __name__ == "__main__":
    while True:
        print("\nRastaurent Managment System")
        print("1.Admin.")
        print("2.Customer.")
        print("3.Exit.")
        choice=int(input("enter your choice:"))
        if choice==1:
            admin_login_menu()
        elif choice==2:
            customer_login_menu()
        elif choice==3:
            print("exiting...")
            break
        else:
            print("invalid choice!")