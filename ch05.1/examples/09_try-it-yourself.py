# 1
temperature = 15
if temperature < 10:
    print("cold")
elif temperature < 25:
    print("mild")
else:
    print("hot")

# 2
number = 7
label = "even" if number % 2 == 0 else "odd"
print(label)   # odd

# 3
items = []
if items:
    print("has items")
else:
    print("empty")   # empty: an empty list is falsy
