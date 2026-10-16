data = {"name": "Ana"}

# LBYL
if "age" in data:
    print(data["age"])
else:
    print("no age")

# EAFP — Pythonic
try:
    print(data["age"])
except KeyError:
    print("no age")
