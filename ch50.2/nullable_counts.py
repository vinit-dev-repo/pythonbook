# nullable_counts.py
import pandas as pd

counts = pd.Series([2, None, 5], dtype="Int64")
print(counts.dtype, counts.isna().tolist())
positive = counts > 3
print(positive.tolist())
print(counts[positive].tolist())
try:
    bool(positive.iloc[1])
except TypeError:
    print("unknown is not True or False")
unknown = pd.Series([None, None], dtype="Int64")
print(int(unknown.sum()), pd.isna(unknown.sum(min_count=1)))
dates = pd.to_datetime(pd.Series(["2026-01-02", None]))
print(dates.isna().tolist())
