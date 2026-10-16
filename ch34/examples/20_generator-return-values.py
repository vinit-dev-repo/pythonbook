def counted_items():
    yield "apple"
    yield "banana"
    return "finished with 2 items"

gen = counted_items()
print(next(gen))
print(next(gen))
try:
    next(gen)
except StopIteration as stop:
    print(stop.value)
