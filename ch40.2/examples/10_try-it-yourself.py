# 1
subscribed = {"news", "sports"}
available = {"news", "sports", "weather", "tech"}
print(sorted(available - subscribed))

# 2
monday = {"Amy", "Ben", "Cara"}
tuesday = {"Ben", "Dan"}
print(sorted(monday & tuesday))
print(sorted(monday - tuesday))

# 3
tags = {"python"}
tags.add("tutorial")
tags.discard("nonexistent")
try:
    tags.remove("nonexistent")
except KeyError as error:
    print("KeyError:", error)
print(sorted(tags))

# 4
a = {1, 2, 3}
b = a | {4}
a |= {5}
print(sorted(a), sorted(b))
c = a.copy()
c.add(6)
print(sorted(a), sorted(c))

# 5
d = {1, 2, 3}
print(sorted(d.union([3, 4])))
try:
    d | [3, 4]
except TypeError as error:
    print("TypeError:", error)
