base = ChainMap({"x": 1})
scoped = base.new_child({"x": 2})   # a temporary override layer on top
print(scoped["x"])   # sees the new layer
print(base["x"])     # original is untouched
