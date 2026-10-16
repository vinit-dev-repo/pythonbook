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
import multiprocessing

def send_numbers(q):
    for i in range(1, 6):
        q.put(i)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=send_numbers, args=(q,))
    p.start()
    # Read the number of items we KNOW were sent. Never loop on `q.empty()`:
    # the docs call it unreliable, because an item already handed over may not
    # have arrived in the queue yet, so `empty()` can say True and then be wrong.
    for _ in range(5):
        print(q.get())
    p.join()   # drain first, THEN join - a child can block waiting to hand over

# 4
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

# 5
# Windows starts new processes with "spawn", which re-imports the whole
# script fresh in the new process — without the __main__ guard, that
# re-import would try to start MORE processes, over and over.
