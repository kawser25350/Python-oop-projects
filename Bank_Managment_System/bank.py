from utitlity import Utility

class Bank:
    def __init__(self, name, address, bank_balance):
        self.name = name
        self.customers_list = {}
        self.admins_list = {}
        self.authentication = {}
        self.address = address
        self.bank_balance = bank_balance
        self.loan_list = {}
        self.given_loan = 0

    def show_all_customers(self):
      
        if not self.customers_list:
            print('No customer found')
        else:
            for userid,customer in self.customers_list.items():
                print(f"Customer ID: {userid} Name: {customer.name} Email: {customer.email} Account Type: {customer.account_type} Balance: {customer.balance}")
        
    def add_account(self, account, type, password):
        if type == 'customer':
            self.customers_list[str(account.customer_id)] = account
            self.authentication[str(account.customer_id)] = password
            print(f"Account created successfully. Your {type} ID is {account.customer_id}")
        else:
            self.admins_list[str(account.admin_id)] = account
            self.authentication[str(account.admin_id)] = password
            print(f"Account created successfully. Your {type} ID is {account.admin_id}")
    
    def authenticate(self, userid, password, account_type):
        print(f"Authenticating user ID: {userid}, Account Type: {account_type}")
        if userid in self.authentication:
            print(f"User ID found.")
            if self.authentication[userid] == password:
                if account_type == 'customer' and userid in self.customers_list:
                    if self.customers_list[userid].bankrupt:
                        print('Your account is blocked')
                        return None
                    else:
                        return self.customers_list[userid]
                elif account_type == 'admin' and userid in self.admins_list:
                    return self.admins_list[userid]
                else:
                    print('Invalid account type or user ID not found in the specified account type')
                    return None
            else:
                print('Incorrect password')
                return None
        else:
            print('User not found')
            return None

