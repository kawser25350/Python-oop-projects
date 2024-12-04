
class Employee_menu:
    def __init__(self):
        self.__employees={
            "staf":{},
            "cheif":{},
            "cleaner":{}
        }

    def add_employee(self,category,employe):
        if category in self.__employees:
            lst=self.__employees[category]
            lst[employe.id]=employe
        else:                 
            self.__employees[category]={}        #creating new employee category 
            lst=self.__employees[category]
            lst[employe.id]=employe

    def remove_employee(self,category,employeId):
        if category in self.__employees:
            lst=self.__employees[category]
            if employeId in lst:
                del lst[employeId]
            else:
                print(f"{employeId} not found ")
        else:
            print(f"{category} no found!")

    def showall_employee(self):
        for k,i in self.__employees.items():
            print(f"       catogery:{k}")
            for x in i.values():
                  print(f"ID:{x.id} Name:{x.name} Phone:{x.phone} salary:{x.salary} ")                                         


