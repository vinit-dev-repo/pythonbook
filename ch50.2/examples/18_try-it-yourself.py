import pandas as pd

sales = pd.read_csv("sales.csv")

# 1
print(sales.loc[(sales["product"] == "Gadget") & (sales["units"] >= 2)])

# 2
print(sales.sort_values("price", ascending=False).head(3))
