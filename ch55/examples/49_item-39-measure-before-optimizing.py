def sum_with_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

for size, expected in ((0, 0), (1, 0), (10, 45), (1000, 499500)):
    assert sum(range(size)) == expected
    assert sum_with_loop(size) == expected
print("sum checks passed")
