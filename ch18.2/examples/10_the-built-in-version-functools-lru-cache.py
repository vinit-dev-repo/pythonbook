@functools.lru_cache(maxsize=2)
def cached_list(n):
    return [n]

first = cached_list(3)
first.append(9)
second = cached_list(3)
print(first is second)
print(second)
