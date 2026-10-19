import pandas as pd

# 3
items = pd.DataFrame({
    "name": ["pen", "book", "lamp", "desk"],
    "qty": [10, 2, 1, 1],
    "price": [1.5, 12.0, 30.0, 150.0],
})
items["total"] = items["qty"] * items["price"]
items["band"] = items["price"].apply(lambda p: "small" if p < 20 else "large")
print(items.groupby("band")["total"].sum())
print(items.groupby("band")["name"].count().to_dict())
