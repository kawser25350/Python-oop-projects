from school import School

class Subject:
    def __init__(self,name,teachaer,max_marks,pass_marks):
        self.name=name
        self.teacher=teachaer       ## teacher object
        self.max_marks=max_marks
        self.pass_marks=pass_marks

    def conducts_exam(self,student_list):
        for student in student_list:
            mark=self.teacher.evaluate_exam()
            student.marks[self.name]=mark
            student.subject_grade[self.name]=School.calculate_grade(mark)
           
            ##print(mark)
            

       