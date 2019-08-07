import webbrowser


def read_file():
    try:
        f = open("links.txt", "r")
        for student in f.readlines():
            webbrowser.open(student, new=2)
            print("opening",student)
        f.close()
    except Exception:
        print("could not read")


read_file()
