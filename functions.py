students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student.title)
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name,student_id = 123):
    student = {"name":name,"student_id":student_id}
    students.append(name)

students_list = get_students_titlecase()

add_student("Ram")

""" var args demo """
def var_args(name, *args):
    print(name)
    print(args)

def var_args_with_keys(name, **kwargs):
    print(name)
    print(kwargs["desc"],kwargs["params"])

var_args("ram","aaaa","var args","one more")

var_args_with_keys("ram", desc="aaaa", params="var args",extra = "one more")