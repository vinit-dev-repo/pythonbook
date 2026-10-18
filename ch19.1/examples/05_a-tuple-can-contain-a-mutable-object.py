record = ("Ana", [85, 90, 78])
print(record)

record[1].append(100)     # allowed: this changes the list, not the tuple
print(record)

record[0] = "Bea"          # not allowed: this assigns a new object to a tuple position
