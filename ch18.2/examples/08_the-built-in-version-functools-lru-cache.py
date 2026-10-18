calls_naive = 0

def fib_naive(n):
    global calls_naive
    calls_naive += 1
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

calls_memo = 0

@functools.lru_cache(maxsize=None)
def fib_memo(n):
    global calls_memo
    calls_memo += 1
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

fib_naive(30)
fib_memo(30)
print(f"Calls without caching: {calls_naive:,}")
print(f"Calls with lru_cache:  {calls_memo}")
