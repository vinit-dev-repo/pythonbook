import itertools

readings = [12, 17, 16, 22, 25]
print("changes:", [later - earlier for earlier, later in itertools.pairwise(readings)])
print("batches:", list(itertools.batched(readings, 2)))
print("no pair:", list(itertools.pairwise([12])))
print("empty:", list(itertools.batched([], 2)))

source = iter(readings)
strict_batches = itertools.batched(source, 2, strict=True)
print("first:", next(strict_batches))
print("second:", next(strict_batches))
try:
    next(strict_batches)
except ValueError as error:
    print("short final batch:", type(error).__name__)
print("source remaining:", list(source))
