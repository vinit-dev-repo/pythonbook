def small_numbers():
    yield 10
    yield 20

gen = small_numbers()
print(next(gen))              # works with next()
for n in gen:                  # works with for -- and continues where next() left off
    print(n)

print(list(small_numbers()))   # a FRESH generator -- works with list() too

used_up = small_numbers()
list(used_up)                  # drain it completely
print(list(used_up))            # single-use -- empty the second time
