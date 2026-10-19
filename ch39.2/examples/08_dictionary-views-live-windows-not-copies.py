d = {"a": 1, "b": 2}
k = d.keys()
print(k)

d["c"] = 3
print(k)          # the view already shows the new key!
