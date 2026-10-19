import pandas as pd

sales = pd.read_csv("sales.csv")

# 1
sales["total"] = sales["units"] * sales["price"]
print(sales[["city", "total"]])

# 2
print(sales.groupby("product")["units"].sum())
