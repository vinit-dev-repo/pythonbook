import queue
import threading
import time

q = queue.Queue()

def producer():
    for i in range(5):
        time.sleep(0.2)  # illustrative pacing, not synchronization
        q.put(f"task-{i}")
        print(f"Produced task-{i}")
    q.put(None)

def consumer():
    while True:
        item = q.get()
        try:
            if item is None:
                return
            print(f"Consumed {item}")
        finally:
            q.task_done()  # every successful get, including None, is acknowledged

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()       # the producer has stopped adding work
q.join()        # every queued item has received task_done()
t2.join()       # the consumer has stopped
