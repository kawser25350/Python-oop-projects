from random import randint
from utitlity import Utility

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

## this is the customer class
class Customer(Person):
    def __init__(self, name, email, account_type):
        super().__init__(name,email)
        self.account_type = account_type
        self.balance = 0
        self.loan=Loan()
        self.bankrupt = False
        # Generate a unique ID for each customer and ensure it is not previously used 
        self.customer_id = str(Utility.generate_id())

    def deposit(self,amount,bank):
        self.balance += amount
        bank.bank_balance += amount
        return f"deposit succesfull- {self.balance} $"
    
    def withdraw(self,amount,bank):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            bank.bank_balance -= amount
            return f" withdraw succesfull {amount}. new balance is :{self.balance} $"
        
    def check_balance(self):
        return f" you balance is - {self.balance} $"    
    
    def balance_transfer(self,amount,recipient,bank):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            if recipient not in bank.customers_list:
                print('Recipient not found')
            else:
                bank.customers_list[recipient].deposit(amount, bank)
                self.balance -= amount
                return f"Transfer successful - {amount} $"

    def take_loan(self,amount,bank):
        if self.loan.eligibility : 
            self.loan.add_loan(amount)  #using the loan class object to take loan
            self.balance += amount 
            bank.bank_balance -= amount #updating bank balance after loan taken
            bank.given_loan += amount #updating bank balance after loan taken
            return f"Loan taken successfully, your balance is {self.balance} $"
        else:
            return 'You are not eligible for loan'
        

    def loan_payment(self,bank,amount):
        if self.loan.payment(amount):
            bank.bank_balance += amount    #updateing bank balance after loan payment
            bank.given_loan -= amount  
            return f"loan payment of {amount} is succesfull!"   #updateing bank given loan amount after payment
        else:
            return 'you have paid extra ammount amount of loan'

        
## this is the admin class
class Admin(Person):
    def __init__(self, name, email):
        super().__init__(name,email)
        self.admin_id = str(Utility.generate_id())
    
    def delete_customer(self,customerid,bank):
        if customerid in bank.customers_list:
            bank.customers_list[customerid].bankrupt = True
            return f"Customer {customerid} has been removed or bankrupt"
        else:
            return 'Customer not found'
            ## authintication theke id delete kori nih karon , bankrupt kora hoise oita show korbe account remove kori nai

        
        
    def show_all_customers(self,bank):
        bank.show_all_customers();

    def bank_balance(self,bank):
       print(f"{bank.name} has total balance of :-{bank.bank_balance}")
    
    def turn_off_loan(self,customerid,bank):
        if customerid in bank.customers_list:
            bank.customers_list[customerid].loan.eligibility = False; 
            return f"succefully loan featuers off for this {customerid} "  #using the loan class object to turn off the loan
        else:
            return 'Customer not found'
    
    def turn_on_loan(self,customerid,bank):
        if customerid in bank.customers_list:
            bank.customers_list[customerid].loan.eligibility = True;
            return f"succefully loan featuers on for this {customerid} "
  

## Loan class
class Loan:
    def __init__(self):
        self.loan_amount = 0
        self.eligibility = True
        self.loan_history = []

    def add_loan(self,amount):
        self.loan_amount += amount
        self.loan_history.append(amount)

    def payment(self,amount):
        if amount <= self.loan_amount:
            self.loan_amount -= amount
            return True
        else:
            return False

