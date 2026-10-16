import inspect

def running_totals(readings):
    total = 0
    for reading in readings:
        total += reading
        replacement = yield total
        if replacement is not None:
            total = replacement
    return total

generator = running_totals([2, 5, 1])
print("created:", inspect.getgeneratorstate(generator))
print("first:", next(generator))
saved_frame = generator.gi_frame
print("paused:", inspect.getgeneratorstate(generator))
print("second:", next(generator))
print("reset then add:", generator.send(10))
print("same frame:", generator.gi_frame is saved_frame)
try:
    next(generator)
except StopIteration as finished:
    print("returned:", finished.value)
print("closed:", inspect.getgeneratorstate(generator), generator.gi_frame is None)
del saved_frame
