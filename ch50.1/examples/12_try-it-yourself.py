import pandas as pd

# 2
first = pd.Series({"x": 1, "y": 2, "z": 3})
second = pd.Series({"y": 10, "z": 20, "w": 30})
print(first + second)
print((second + first).to_dict())

# 3
rows = [
    {"day": "Mon", "sales": 100},
    {"day": "Tue", "sales": 150},
    {"day": "Wed", "sales": 120},
]
table = pd.DataFrame(rows).set_index("day")
print(table.loc["Tue", "sales"])
print(table.reset_index().columns.tolist())
