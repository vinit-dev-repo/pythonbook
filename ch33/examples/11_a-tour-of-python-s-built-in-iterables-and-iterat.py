r = range(3)
print(iter(r) is iter(r))    # False -- range hands out a FRESH iterator each time (it's an iterable)

e = enumerate(["a", "b"])
print(iter(e) is e)          # True -- enumerate IS its own iterator
