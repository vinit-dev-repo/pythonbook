import pandas as pd

# 3
orders = pd.DataFrame({"city": ["London", "Tokyo", "London", "Tokyo"], "units": [5, None, 2, 4]})
print(int(orders["units"].isna().sum()))
filled = orders.fillna({"units": 0})
dropped = orders.dropna()
print(filled["units"].tolist())
print(len(dropped), int(orders["units"].isna().sum()))
print(round(float(filled["units"].mean()), 2), round(float(dropped["units"].mean()), 2))
