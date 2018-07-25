student = {
    "name": "Ram",
    "age": "25"
}

try:
    first_name = student["first_name"]
except KeyError as error:
    print("The error is : {0}".format(error))
    print("key doesn't exist")
except Exception:
    print("some error")

print("completed")