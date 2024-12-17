
from abc import ABC 
from school import School
import random


class Person(ABC):
    def __init__(self,name):
        self.name=name


class Teacher(Person): #inherit Person
    
    def evaluate_exam(self):
        return random.randint(50,100)
    

class Student(Person):  #inherit Person
    
    def __init__(self, name,classroom):   # recieve classroom object
        super().__init__(name)
        self.classroom=classroom   #classroom object
        self.marks={}       #{'sub':23}
        self.subject_grade={}     # {'sub':'A+'}
        self.final_grade=None
        self.__id=None


    @property
    def id(self):
        return self.id
    
    @id.setter
    def id(self,value):
        self.id=value


    def calculate_final_grade(self):

        for grade in self.subject_grade.values():

            point=School.grade_to_value(grade)
            sum+=point 
        
        if sum==0:
            self.final_grade='F'
        else:
            gpa=sum/len(self.subject_grade)
            self.final_grade=School.value_to_grade(gpa)
            return f"name {self.name}  grade:{self.final_grade} cgpa:{gpa}"

