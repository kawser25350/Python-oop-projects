from school import School
from classroom import Classroom
from person import Student,Teacher
from subject import Subject

s1=School("holly mission school","madarjong,jamalpur") ## creating scool object


two=Classroom("two") ## creating classroom object



teach=Teacher("shuvo")

stud=Student("kawser",two) 

sub=Subject("bangla",teach,100,50)



two.add_student(stud)    #insering student object to classroom obj.sutdent list
two.add_subject(sub)     #adding subject to classrom obj.subject list

s1.add_classroom(two)  ## adding classroom object to scholl 
s1.add_teacher("bangla",teach)  ## adding teacher to school


s1.classroom_list["two"].take_semester_final(two.student_list) 
#taking exam for class two  by using classroom take_semeester_final 
# and then each sub will conduct exam number will given by teacher and lso calculate fina great of students
#  using student function  called  calculate_final_grade



class_two =s1.classroom_list["two"]

for stu in class_two.student_list:
    print(stu.final_grade)

          