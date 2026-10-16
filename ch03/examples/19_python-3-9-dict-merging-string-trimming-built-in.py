defaults = {"colour": "blue", "size": "M"}
custom = {"size": "L"}
merged = {**defaults, **custom}
print(merged)
