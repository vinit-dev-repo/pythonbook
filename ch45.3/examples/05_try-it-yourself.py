# 1 & 2
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def sum_of_squares(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    N = 5_000_000

    start = time.perf_counter()
    for _ in range(4):
        sum_of_squares(N)
    print(f"Serial: {time.perf_counter() - start:.2f}s")

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        list(pool.map(sum_of_squares, [N] * 4))
    print(f"Processes: {time.perf_counter() - start:.2f}s")

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(sum_of_squares, [N] * 4))
    print(f"Threads: {time.perf_counter() - start:.2f}s")   # observed durations vary; interpret them for this Python build

# 3
import random
from concurrent.futures import as_completed

def random_wait(n):
    time.sleep(random.uniform(0.1, 0.5))
    return n

if __name__ == "__main__":
    # ProcessPoolExecutor, as the exercise asks - so `random_wait` must be a
    # top-level function (picklable) and the pool must sit inside the guard.
    with ProcessPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(random_wait, n) for n in range(1, 6)]
        for f in as_completed(futures):
            print(f.result())
