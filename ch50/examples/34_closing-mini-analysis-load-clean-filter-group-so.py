import pandas as pd

# 1. load and retain the original values
source_sales = pd.read_csv("sales.csv")
sales = source_sales.copy()

# 2. apply the chosen zero-fill policy to the working table
sales["units"] = sales["units"].fillna(0)

# 3. include positive-unit rows in this report
sales = sales[sales["units"] > 0].copy()

# 4. new column
sales["total"] = sales["units"] * sales["price"]

# 5. group: total revenue per city
by_city = sales.groupby("city")["total"].sum()

# 6. sort: biggest city first
by_city = by_city.sort_values(ascending=False)
print(by_city)

# 7. save
by_city.to_csv("revenue_by_city.csv")
print("saved revenue_by_city.csv")
