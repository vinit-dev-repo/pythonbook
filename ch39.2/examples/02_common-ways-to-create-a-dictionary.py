keys = ["north", "south"]
shared = dict.fromkeys(keys, [])
separate = {key: [] for key in keys}
shared["north"].append(7)
separate["north"].append(7)
print(shared)
print(separate)
print(shared["north"] is shared["south"])
print(separate["north"] is separate["south"])
