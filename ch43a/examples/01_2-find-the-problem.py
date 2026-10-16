readings = (n * 2 for n in range(5))

total = sum(readings)
print("total:", total)
try:
    print("largest:", max(readings))
except ValueError as e:
    print("ValueError:", e)
