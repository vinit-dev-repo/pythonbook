import time
import threading
import multiprocessing

def count_primes(limit):
    count = 0
    for n in range(2, limit):
        is_prime = True
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

LIMIT = 200_000
WORKERS = 4

def run_serial():
    start = time.perf_counter()
    for _ in range(WORKERS):
        count_primes(LIMIT)
    return time.perf_counter() - start

def run_threaded():
    start = time.perf_counter()
    threads = [threading.Thread(target=count_primes, args=(LIMIT,)) for _ in range(WORKERS)]
    for t in threads: t.start()
    for t in threads: t.join()
    return time.perf_counter() - start

def run_multiprocess():
    start = time.perf_counter()
    processes = [multiprocessing.Process(target=count_primes, args=(LIMIT,)) for _ in range(WORKERS)]
    for p in processes: p.start()
    for p in processes: p.join()
    return time.perf_counter() - start

if __name__ == "__main__":
    print(f"Serial:        {run_serial():.2f}s")
    print(f"Threaded:      {run_threaded():.2f}s")
    print(f"Multiprocess:  {run_multiprocess():.2f}s")
