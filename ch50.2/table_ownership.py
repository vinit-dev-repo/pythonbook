# table_ownership.py
import pandas as pd

table = pd.DataFrame({"qty": [2, 4]}, index=["east", "west"])
alias = table
selected = table["qty"]
selected.loc["east"] = 9
print(table["qty"].tolist(), selected.tolist())
table.loc["west", "qty"] = 6
print(alias is table, alias["qty"].tolist(), selected.tolist())
table["limit"] = pd.Series({"west": 12, "east": 8})
print(table["limit"].tolist())
