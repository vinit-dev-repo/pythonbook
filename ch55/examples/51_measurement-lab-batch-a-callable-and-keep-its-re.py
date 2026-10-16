import time

def measure_batch(operation, *, number=10):
    if type(number) is not int or number <= 0:
        raise ValueError("number must be a positive integer")
    started = time.perf_counter_ns()
    for _ in range(number):
        result = operation()
    elapsed_ns = time.perf_counter_ns() - started
    return elapsed_ns, result

samples = [measure_batch(lambda: sorted(["elm", "spruce"],
                                       key=len, reverse=True), number=5)
           for _ in range(3)]
best_ns, result = min(samples, key=lambda sample: sample[0])
print(result)
print("samples:", len(samples))
print("best seconds per call:", best_ns / 5 / 1_000_000_000)
