ordered = OrderedDict(a=1, b=2)
reversed_order = OrderedDict(b=2, a=1)
plain = {"b": 2, "a": 1}
print(ordered == reversed_order)
print(ordered == plain, reversed_order == plain)
