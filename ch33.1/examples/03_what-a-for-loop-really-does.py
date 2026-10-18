obj = ["a", "b", "c"]        # any iterable at all

it = iter(obj)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)                 # <-- the loop body runs here
