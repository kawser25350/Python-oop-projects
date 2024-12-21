from bank import Bank
from persons import Customer, Admin

class OperationManager:

   #customer part
    def customer_login_menu(self,bank):
        print('Enter your customer ID')
        customer_id = input().strip()
        print('Enter your password')
        password = input().strip()
        customer = bank.authenticate(customer_id,password,'customer')
        if customer:
            self.customer_menu(customer,bank)
        else:
            print('Login failed')

    def customer_register_menu(self,bank):
        print('Enter your name')
        name = input()
        print('Enter your email')
        email = input()
        print('Enter your account type')
        account_type = input()
        print('Enter your password')
        password = input()
        customer = Customer(name,email,account_type)
        bank.add_account(customer,'customer',password)
       

    def customer_menu(self,customer,bank):
        while True:
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Check Balance')
            print('4. Balance Transfer')
            print('5. Take Loan')
            print('6. Loan Payment')
            print('7. Exit')
            choice = input()
            if choice == '1':
                print('Enter amount to deposit')
                amount = int(input())
                print(customer.deposit(amount,bank))
            elif choice == '2':
                print('Enter amount to withdraw')
                amount = int(input())
                print(customer.withdraw(amount,bank))
            elif choice == '3':
                print(customer.check_balance())
            elif choice == '4':
                print('Enter amount to transfer')
                amount = int(input())
                print('Enter recipient ID')
                recipient = input()
                print(customer.balance_transfer(amount,recipient,bank))
            elif choice == '5':
                print('Enter amount to take loan')
                amount = int(input())
                print(customer.take_loan(amount,bank))
            elif choice == '6':
                print('Enter amount to pay loan')
                amount = int(input())
                print(customer.loan_payment(bank, amount))
            else:
                break



    #admin part

    def admin_login_menu(self,bank):
        print('Enter your admin ID')
        admin_id = input().strip()
        print('Enter your password')
        password = input().strip()
        admin = bank.authenticate(admin_id,password,'admin')
        if admin:
            self.admin_menu(admin,bank)
        else:
            print('Login failed')

    def admin_register_menu(self,bank):
        print('Enter your name')
        name = input()
        print('Enter your email')
        email = input()
        print('Enter your password')
        password = input()
        admin = Admin(name,email)
        bank.add_account(admin,'admin',password)
        print('Account created successfully')

   
    

    def admin_menu(self,admin,bank):
        while True:
            print('1. Show all customers')
            print('2. Delete customer')
            print('3. Exit')
            choice = input()
            if choice == '1':
                bank.show_all_customers()
            elif choice == '2':
                print('Enter customer ID to delete')
                customer_id = input()
                print(admin.delete_customer(customer_id, bank))
            else:
                break

     # main menu
    def main_menu(self,bank):
        bank = bank
        while True:
            print('1. Customer Login')
            print('2. Customer Register')
            print('3. Admin Login')
            print('4. Admin Register')
            print('5. Exit')
            choice = input()
            if choice == '1':
                self.customer_login_menu(bank)
            elif choice == '2':
                self.customer_register_menu(bank)
            elif choice == '3':
                self.admin_login_menu(bank)
            elif choice == '4':
                self.admin_register_menu(bank)
            else:
                break