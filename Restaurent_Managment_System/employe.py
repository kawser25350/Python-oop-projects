
class Employe:
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
            self.__employees[category]={}        #creating new employee category ##githubcodespace changes
            lst=self.__employees[category]
            lst[employe.id]=employe

    
    def remove_employee(self,category,employeId):
        if category in self.__employees:
            lst=self.__employees[category]
            if employeId in lst:
                del lst[employeId]
            else:
                print(employ)
        else:
            print(f"{category} no found!")



