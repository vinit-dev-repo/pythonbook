d = {"fruit": 2}
live = d.keys()
snapshot = list(live)
d["veg"] = 3
print(list(live))
print(snapshot)
