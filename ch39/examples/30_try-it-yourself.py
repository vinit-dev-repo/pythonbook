# 1
h = hash("hello")
print(h)   # an integer; it may differ in another process
# hash(["h", "e"]) -> TypeError: unhashable type: 'list'
# Lists are mutable, so Python refuses to hash them.

# 2
names = ["Amy", "Ben"]
scores = [88, 91]
exam = dict(zip(names, scores))
print(exam)   # {'Amy': 88, 'Ben': 91}

# 3
inventory = {}
for item, count in [("apple", 3), ("banana", 2), ("apple", 5)]:
    inventory.setdefault(item, 0)
    inventory[item] += count
print(inventory)   # {'apple': 8, 'banana': 2}

# 4
defaults = {"volume": 50, "brightness": 80}
user = {"volume": 70}
merged = defaults | user
print(merged)     # {'volume': 70, 'brightness': 80}
print(defaults)   # unchanged: {'volume': 50, 'brightness': 80}

# 5
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)
    def __hash__(self):
        return hash((self.x, self.y))

a = Point(3, 4)
b = Point(3, 4)
d = {a: "corner"}
print(b in d)   # True
