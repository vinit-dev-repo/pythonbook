import threading
import time

condition = threading.Condition()
basket = []

def producer():
    for i in range(3):
        time.sleep(0.5)
        with condition:
            basket.append(f"apple-{i}")
            print(f"Produced apple-{i}")
            condition.notify()          # wake up one waiting consumer

def consumer():
    for _ in range(3):
        with condition:
            while not basket:           # wait UNTIL there is something
                condition.wait()
            item = basket.pop()
            print(f"Consumed {item}")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()
