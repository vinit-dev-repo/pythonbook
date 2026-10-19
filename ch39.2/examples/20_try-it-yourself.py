import copy

# 1
names = ["Amy", "Ben"]
scores = [88, 91]
exam = dict(zip(names, scores))
print(exam)

# 2
inventory = {}
for item, count in [("apple", 3), ("banana", 2), ("apple", 5)]:
    inventory.setdefault(item, 0)
    inventory[item] += count
print(inventory)

# 3
defaults = {"volume": 50, "brightness": 80}
user = {"volume": 70}
merged = defaults | user
print(merged)
print(defaults)

# 4
prices = {"apple": 1.2}
print(prices.get("pear"), prices.get("pear", 0.0))
print(prices.pop("pear", None))
try:
    prices.pop("pear")
except KeyError as error:
    print("KeyError:", error)

# 5
original = {"tags": ["a"]}
shallow = original.copy()
deep = copy.deepcopy(original)
shallow["tags"].append("b")
deep["tags"].append("c")
print(original)
print(shallow)
print(deep)
