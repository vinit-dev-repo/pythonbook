import pandas as pd

sales = pd.read_csv("sales.csv")

# 1
print(sales.shape)
print(sales.dtypes)

# 2
sales["total"] = sales["units"] * sales["price"]
print(sales[["city", "total"]])

# 3
print(sales.loc[(sales["product"] == "Gadget") & (sales["units"] >= 2)])

# 4
print(sales.groupby("product")["units"].sum())

# 5
print(sales.sort_values("price", ascending=False).head(3))
