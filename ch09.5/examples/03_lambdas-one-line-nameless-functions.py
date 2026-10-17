students = [("Amara", 21), ("Ravi", 19), ("Sam", 24)]
by_age = sorted(students, key=lambda student: student[1])
print(by_age)
