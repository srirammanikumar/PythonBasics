students = []


class Student:

    school_name = "abc school" #statuc variable
    def __init__(self,name):
        self.name = name # instance attribute
        students.append(self)

    def __str__(self):
        return "printing student "+self.name

    def add_student(self,name, student_id=123):
        student = {"name": name, "student_id": student_id}
        students.append(student)

mark = Student("Mark")
print(mark)

class HighScoolStudent(Student): #extending Student

    school_name = "high school"