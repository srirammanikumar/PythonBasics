students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=123):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("cannot save")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("could not read")


read_file();
print_students_titlecase()

while (1):
    prompt = input("Do you want to add student?(Y/N)")
    if (prompt == "Y"):
        student_name = input("Enter name for student :")
        student_id = input("Enter ID :")
        add_student(student_name, student_id)
        save_file(student_name)
    else:
        break
