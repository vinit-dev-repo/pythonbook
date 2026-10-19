import queue
import threading
from concurrent.futures import ThreadPoolExecutor

# 1
with ThreadPoolExecutor(max_workers=2) as pool:
    lengths = list(pool.map(len, ["a", "bb", "ccc"]))
print(lengths)

# 2
box = queue.Queue(maxsize=1)
totals = []


def produce():
    for number in range(1, 6):
        box.put(number)
    box.put(None)


def consume():
    running = 0
    while True:
        item = box.get()
        try:
            if item is None:
                break
            running += item
        finally:
            box.task_done()
    totals.append(running)


producer = threading.Thread(target=produce)
consumer = threading.Thread(target=consume)
producer.start()
consumer.start()
producer.join()
box.join()
consumer.join()
print(totals[0])
