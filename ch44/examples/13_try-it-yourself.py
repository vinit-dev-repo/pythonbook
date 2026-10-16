import threading
# 3
import time
sem = threading.Semaphore(2)

def worker(n):
    with sem:
        print(f"Worker {n} started")
        time.sleep(0.5)
        print(f"Worker {n} finished")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
