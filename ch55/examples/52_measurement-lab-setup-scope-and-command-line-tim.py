import timeit

observed = []
timer = timeit.Timer(
    "observed.append(values.pop())",
    setup="values = list(seed)",
    globals={"seed": [3, 8], "observed": observed},
)
totals = timer.repeat(number=2, repeat=3)
print(observed)
print("batch count:", len(totals))
