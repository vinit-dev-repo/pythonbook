def small_numbers():
    yield 1
    yield 2

def all_numbers():
    yield from small_numbers()   # same as: for n in small_numbers(): yield n
    yield 3
    yield 4

print(list(all_numbers()))
