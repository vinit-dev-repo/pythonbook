print(sales.dropna())              # drop any row with ANY missing value -> 7 rows
print(sales.dropna(axis=1))        # drop whole COLUMNS that have any missing value
print(sales.fillna({"units": 0}))  # fill only the "units" column, with 0
