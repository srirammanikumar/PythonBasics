students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("could not read")


# returns after every line
def read_students(f):
    for line in f:
        yield line


read_file();
print(students)

"""
Lambda functions, simple 1 line anonymous functions -
the function is equivalent to 
def double(x):
    return x*2
"""

double = lambda x: x * 2

print(double(5))
