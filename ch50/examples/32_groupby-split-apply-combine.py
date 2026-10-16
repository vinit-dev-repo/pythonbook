tokyo_units = sales.loc[sales["city"] == "Tokyo", "units"]
print(len(tokyo_units), tokyo_units.count(), float(tokyo_units.mean()))
print(round(float(tokyo_units.fillna(0).mean()), 3))
