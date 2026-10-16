d = {"a": 1, "b": 2, "c": 3}
del d["a"]
print(d)

removed = d.pop("b")
print(removed, d)

last = d.popitem()
print(last, d)
