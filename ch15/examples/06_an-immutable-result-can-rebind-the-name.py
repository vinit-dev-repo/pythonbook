items = [1, 2, 3]
before = id(items)
items.append(4)            # this changes the SAME object in place
print("same object as before?", id(items) == before)
