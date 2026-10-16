print(sales["city"].value_counts())      # how many rows per city
print(sales["city"].unique().tolist())   # the distinct cities as a plain list
print(sales["city"].nunique())           # HOW MANY distinct cities
print(sales["price"].mean())
print(sales["price"].sum())
print(sales[["units", "price"]].corr())  # correlation between numeric columns
