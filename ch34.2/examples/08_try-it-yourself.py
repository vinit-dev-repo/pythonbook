# 1
import sys
list_version = [x for x in range(100_000)]
gen_version = (x for x in range(100_000))
print(sys.getsizeof(gen_version) < sys.getsizeof(list_version))
print(sum(gen_version))

# 2
def noisy(n):
    print("call", n)
    return n * n

squares = (noisy(n) for n in [1, 2, 3])
print("created")
print(next(squares))
print(next(squares))

# 3
evens = (n for n in range(10) if n % 2 == 0)
print(sum(evens))
print(sum(evens))
print(sum(n * n for n in range(4)))
