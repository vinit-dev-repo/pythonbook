def add_mark(name, mark, marks=None):
    if marks is None:
        marks = []
    marks.append(mark)
    return name, marks

print(add_mark("Amara", 70))
print(add_mark("Ravi", 65))
