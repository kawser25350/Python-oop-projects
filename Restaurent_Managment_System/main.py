
from Menu import admin_login_menu,customer_login_menu
if __name__ == "__main__":
    while True:
        print("\nRastaurent Managment System")
        print("1.Admin.")
        print("2.Customer.")
        print("3.exit.")
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