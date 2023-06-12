student = {"name":"John", "email":"john@gmail.com","age":"19"}
a = student.keys()
print(a)
b = student.values()
print(b)
c = student.items()
print(c)
student["age"]="25"
print(student)
student["email"]="johnnjangi2@gmail.com"
print(student)
student.update({"email":"johnalannamu@hotmail.co.ke"})
print(student)
if "name" in student:
    print("yes name is in student")
else:
    print("name not in student")