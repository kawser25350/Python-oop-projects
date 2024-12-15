from user import User

class Employee(User):
    def __init__(self, user_name, contact, address,salary):
        super().__init__(user_name, contact, address)
        self.salary=salary

    def __repr__(self):
        return f"Name:{self.user_name} Contact:{self.contact}  Adress:{self.address} Salary:{self.salary}"
    