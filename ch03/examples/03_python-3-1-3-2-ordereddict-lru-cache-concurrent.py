from functools import lru_cache

calls = []

@lru_cache(maxsize=None)
def slow_square(n):
    calls.append(n)
    return n * n

print(slow_square(4))
print(slow_square(4))
print("times the body actually ran:", len(calls))
print(slow_square.cache_info())
