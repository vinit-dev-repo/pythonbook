student = {"name": "Amara", "age": 22, "email": "amara@example.com"}

del student["email"]          # remove a key; crashes if key is missing
print(student)

removed_age = student.pop("age")   # remove a key AND hand you its value back
print(removed_age)
print(student)
