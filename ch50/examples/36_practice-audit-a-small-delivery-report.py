from pathlib import Path
import pandas as pd

def write_delivery_totals(frame, destination):
    if frame["id"].duplicated().any():
        raise ValueError("duplicate delivery id")
    known = frame.dropna(subset=["units"])
    totals = known.groupby("depot")["units"].sum()
    totals = totals.rename("known_units").reset_index()
    totals.to_csv(destination, index=False)
    return len(frame), int(frame["units"].isna().sum()), len(known)

deliveries = pd.DataFrame({
    "id": [101, 102, 103, 104],
    "depot": ["east", "west", "east", "west"],
    "units": [3, None, 5, 4],
})
original = deliveries.copy()
target = Path("delivery_totals.csv")
print(write_delivery_totals(deliveries, target))
loaded = pd.read_csv(target)
print(loaded.to_dict("records"))
assert loaded.to_dict("records") == [
    {"depot": "east", "known_units": 8.0},
    {"depot": "west", "known_units": 4.0},
]
assert deliveries.equals(original)
before_rejection = target.read_bytes()
duplicate = pd.concat([deliveries, deliveries.iloc[[0]]], ignore_index=True)
try:
    write_delivery_totals(duplicate, target)
except ValueError as error:
    print(error)
assert target.read_bytes() == before_rejection
