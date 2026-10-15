# membership_scaling_lab.py
from timeit import repeat

def count_present(queries, collection):
    return sum(item in collection for item in queries)

for size in (1_000, 10_000, 100_000):
    values = list(range(size))
    members = set(values)
    keyed = dict.fromkeys(values)
    queries = (0, size // 2, size - 1, size, size + 1)
    query_set = set(queries)
    operations = {
        "list": lambda: count_present(queries, values),
        "set": lambda: count_present(queries, members),
        "dict": lambda: count_present(queries, keyed),
        "intersection": lambda: len(query_set & members),
    }
    assert all(operation() == 3 for operation in operations.values())
    print("size:", size, "matches:", 3)
    for name, operation in operations.items():
        samples = repeat(operation, number=10, repeat=3)
        best_per_batch = min(samples) / 10
        print(f"{name}: {best_per_batch:.9f} seconds per five-query batch")
