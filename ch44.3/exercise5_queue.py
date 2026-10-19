# exercise5_queue.py
from queue_lifecycle import run_batch

values = list(range(1, 11))
successes, failures = run_batch(values)
assert successes == [(value, value * value) for value in values]
assert failures == []
print("squares:", [square for value, square in successes])

successes, failures = run_batch(values, fail_on=5)
assert successes == [
    (1, 1), (2, 4), (3, 9), (4, 16), (6, 36),
    (7, 49), (8, 64), (9, 81), (10, 100),
]
assert failures == [5]
print("successful jobs:", len(successes), "failed jobs:", failures)

repeated = run_batch([0, 3, 3], fail_on=3)
assert repeated == ([(0, 0)], [3, 3])
print("repeated jobs:", repeated)
