print(slice(1, 5))
letters = ["A", "B", "C", "D", "E", "F"]
print(letters[1:5])              # normal slicing
print(letters.__getitem__(slice(1, 5)))   # exactly the same thing
