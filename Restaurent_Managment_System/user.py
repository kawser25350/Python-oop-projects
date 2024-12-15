from abc import ABC, abstractmethod

class  User(ABC):

    def __init__(self,user_name,contact,address):
        self.user_name=user_name
        self.contact=contact 
        self.address=address 

            
