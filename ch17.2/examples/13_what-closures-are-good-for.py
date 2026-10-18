# Simple memoization by hand: remember answers you've already computed
def make_memoized_square():
    cache = {}
    def square(n):
        if n not in cache:
            print(f"computing {n}**2...")
            cache[n] = n ** 2
        return cache[n]
    return square

square = make_memoized_square()
print(square(4))
print(square(4))     # no "computing" message — served from the cache
