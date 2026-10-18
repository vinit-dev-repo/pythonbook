def noisy(n):
    print(f"checking {n}")
    return n > 0

numbers = [1, 2, -5, 4]
print(any(noisy(n) for n in numbers))
