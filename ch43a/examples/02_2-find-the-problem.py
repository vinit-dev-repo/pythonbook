readings = (n * 2 for n in range(5))
total = 0
largest = None
for r in readings:
    total += r
    largest = r if largest is None else max(largest, r)
print("total:", total, "largest:", largest)
