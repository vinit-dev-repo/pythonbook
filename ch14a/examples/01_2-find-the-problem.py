def add_mark(name, mark, marks=[]):
    marks.append(mark)
    return name, marks

print(add_mark("Amara", 70))
print(add_mark("Ravi", 65))
