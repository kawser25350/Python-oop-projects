
class Classroom:
    def __init__(self,name):
        self.name=name
        self.student_list=[]
        self.subject_list=[]

        def add_student(self,student):
            self.student_list.append(student)

        def add_subject(self,subject):
            self.subject_list.append(subject)
        
        def take_semester_final(self,student_list):
               
            for subject in self.subject_list:
                subject.conducts_exam(self.student_list)
            for student in self.student_list:
                student.calculate_final_grade()
            

      


        