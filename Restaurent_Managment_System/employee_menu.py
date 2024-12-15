class Employeemenu:

    def __init__(self):
        self.employeelist=[]
    
    def add_employee(self,employee):
        self.employeelist.append(employee)
        print(f"employee {employee.user_name} added succesfully!")
    
    def delete_employee(self,employeename):
        for i, emp in enumerate(self.employeelist):
            if emp.user_name == employeename:
                del self.employeelist[i] 
                print("employee deleted!")
            else:
                print(f"{employeename} not found in employeelist!")
        
    def view_employee(self):
        print("\nemployee dateils:")
        for emp in self.employeelist:
            print(emp)
    