x = [1, 2, 3]
before = id(x)
x = [4, 5, 6]              # a brand new list; x now points at it
print("same object as before?", id(x) == before)
