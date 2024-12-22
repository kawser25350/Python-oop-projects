import os
from bank import Bank
from persons import Customer, Admin

class OperationManager:
    

    #customer part
    def customer_login_menu(self, bank):
        print('Customer Login Menu')
        print('Enter your customer ID')
        print('>> ', end='')
        customer_id = input().strip()
        print('Enter your password')
        print('>> ', end='')
        password = input().strip()
        customer = bank.authenticate(customer_id, password, 'customer')
        if customer:
            self.customer_menu(customer, bank)
            print()
        else:
            print('Login failed\n')

    def customer_register_menu(self, bank):
        print('Customer Register Menu')
        print('Enter your name')
        print('>> ', end='')
        name = input()
        print('Enter your email')
        print('>> ', end='')
        email = input()
        print('Enter your account typez[savings/current]')
        print('>> ', end='')
        account_type = input()
        print('Enter your password')
        print('>> ', end='')
        password = input()
        customer = Customer(name, email, account_type)
        bank.add_account(customer, 'customer', password)
        print()

    def customer_menu(self, customer, bank):
        while True:
            print('Customer Menu')
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Check Balance')
            print('4. Balance Transfer')
            print('5. Take Loan')
            print('6. Loan Payment')
            print('7. Logout')
            print('>> ', end='')
            choice = input()
            print()
            if choice == '1':
                print('Enter amount to deposit')
                print('>> ', end='')
                amount = int(input())
                print(customer.deposit(amount, bank))
            elif choice == '2':
                print('Enter amount to withdraw')
                print('>> ', end='')
                amount = int(input())
                print(customer.withdraw(amount, bank))
            elif choice == '3':
                print(customer.check_balance())
            elif choice == '4':
                print('Enter amount to transfer')
                print('>> ', end='')
                amount = int(input())
                print('Enter recipient ID')
                print('>> ', end='')
                recipient = input()
                print(customer.balance_transfer(amount, recipient, bank))
            elif choice == '5':
                print('Enter amount to take loan')
                print('>> ', end='')
                amount = int(input())
                print(customer.take_loan(amount, bank))
            elif choice == '6':
                print('Enter amount to pay loan')
                print('>> ', end='')
                amount = int(input())
                print(customer.loan_payment(bank, amount))
            elif choice == '7':
                break
            else:
                print('Invalid input, please try again.')
            print()

    #admin part

    def admin_login_menu(self, bank):
        print('Admin Login Menu')
        print('Enter your admin ID')
        print('>> ', end='')
        admin_id = input().strip()
        print('Enter your password')
        print('>> ', end='')
        password = input().strip()
        admin = bank.authenticate(admin_id, password, 'admin')
        if admin:
            self.admin_menu(admin, bank)
            print()
        else:
            print('Login failed\n')

    def admin_register_menu(self, bank):
        print('Admin Register Menu')
        print('Enter your name')
        print('>> ', end='')
        name = input()
        print('Enter your email')
        print('>> ', end='')
        email = input()
        print('Enter your password')
        print('>> ', end='')
        password = input()
        admin = Admin(name, email)
        bank.add_account(admin, 'admin', password)
        print('Account created successfully\n')

    def admin_menu(self, admin, bank):
        while True:
            print('Admin Menu')
            print('1. Show all customers')
            print('2. Delete customer')
            print('3. Check bank balance')
            print('4. Check given loan of bank')
            print('5. Turn off customer loan eligibility')
            print('6. Turn on customer loan eligibility')
            print('7. Logout')
            print('>> ', end='')
            choice = input()
            print()
            if choice == '1':
                bank.show_all_customers()
            elif choice == '2':
                print('Enter customer ID to delete')
                print('>> ', end='')
                customer_id = input()
                print(admin.delete_customer(customer_id, bank))
            elif choice == '3':
                admin.bank_balance(bank)
            elif choice == '4':
                print(f"Total given loan: {bank.given_loan}")
            elif choice == '5':
                print('Enter customer ID to turn off loan eligibility')
                print('>> ', end='')
                customer_id = input()
                print(admin.turn_off_loan(customer_id, bank))
            elif choice == '6':
                print('Enter customer ID to turn on loan eligibility')
                print('>> ', end='')
                customer_id = input()
                print(admin.turn_on_loan(customer_id, bank))
            elif choice == '7':
                break
            else:
                print('Invalid input, please try again.')
            print()

    # main menu
    def main_menu(self, bank):
        bank = bank
        while True:
            print('Main Menu')
            print('1. Customer Login')
            print('2. Customer Register')
            print('3. Admin Login')
            print('4. Admin Register')
            print('5. Exit')
            print('>> ', end='')
            choice = input()
            print()
            if choice == '1':
                self.customer_login_menu(bank)
            elif choice == '2':
                self.customer_register_menu(bank)
            elif choice == '3':
                self.admin_login_menu(bank)
            elif choice == '4':
                self.admin_register_menu(bank)
            elif choice == '5':
                break
            else:
                print('Invalid input, please try again.')
            print()

