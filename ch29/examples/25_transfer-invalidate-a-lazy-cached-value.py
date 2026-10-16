r.numbers.append(50)
print("stale:", r.total)
del r.total
print("recomputed:", r.total)
