p = Point(1, 2)
locations = {p: "start"}

p.x = 99          # mutating a field the hash depends on!

print(p in locations)          # False — Python is now looking in the WRONG bucket
print(list(locations.keys()))  # the key is still physically there...
