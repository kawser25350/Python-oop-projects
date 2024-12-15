from rastaurent import Rastaurent
from fooditem import Food
from admin import Admin
from employee import Employee
from customer import Customer

def admin_functional_menu(currentadmin):
    while True:
        print(f"wellcome {currentadmin.user_name}")
        print("1.Add employee.")
        print("2.Reomve employee.")
        print("3.Add food.")
        print("4.Remove food")
        print("5.View food menu.")
        print("6.View all employee.")
        print("7.Logout.")
        x=input(">>")

        if x==1:

            print("enter employee information:")
            username=input("USERNAME")
            contact=input("CONTACT:")
            address=            
            currentadmin.add_employee(r1,)





def admin_login_menu():
    while True:
        print("Admin Login Menu:")
        print("1.Login(user name).")
        print("2.Register.")
        print("3.exit.") 
        n=input(">>")
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
            contact=input("CONTACT NUMBER:")
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
        print("Customer Login Menu:")
        print("1.Login(user name).")
        print("2.Register.")
        print("3.exit.") 
        n=input(">>")
        if(n==1):
            username=input("Enter user name to login:")
            if username in r1.customerlist:
                currentadmin=r1.customerlist[username]
               ## customer_functional_menu(currentadmin) ## calling the customer function menu with the current customer user
            else:
                print(f"{username} not registered yet!")
    
        elif n==2:
            print("please enter your information to register:")
            username=input("USERNAME:")
            contact=input("CONTACT NUMBER:")
            address=input("ADDRESS:")
            c1=Admin(username,contact,address) # createing new customer object 
            r1.customerlist[username]=c1     # stroing the customer obj to the rastaurent's customer list to save customer user

        elif n==3:
            print("exiting..")
            break
        else:
            print("Invalid choice!")
    


r1=Rastaurent("sonargao","sytel") ## creating the rastaurent object 


if __name__ == "__main__":
    while True:
        print("Rastaurent Managment System")
        print("1.Admin.")
        print("2.Customer.")
        print("3.Exit.")
        choice=input("enter your choice")
        if choice==1:
            admin_login_menu()
        elif choice==2:
            customer_login_menu()
        elif choice==3:
            print("exiting...")
            break
        else:
            print("invalid choice!")