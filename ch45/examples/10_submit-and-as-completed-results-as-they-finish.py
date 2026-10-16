import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def slow_task(n):
    time.sleep(random.uniform(0.1, 1.0))
    return n * n

with ThreadPoolExecutor(max_workers=4) as pool:
    futures = {pool.submit(slow_task, n): n for n in range(1, 6)}
    for future in as_completed(futures):
        original_n = futures[future]
        print(f"n={original_n} -> {future.result()}")
