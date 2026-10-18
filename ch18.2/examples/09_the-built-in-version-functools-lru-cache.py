computations = []

@functools.lru_cache(maxsize=2)
def square_cached(n):
    computations.append(n)
    return n * n

print([square_cached(n) for n in [1, 2, 1, 3, 2]])
print(computations)
print(square_cached.cache_info())
