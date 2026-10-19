import threading


# 1
class Ledger:
    def __init__(self):
        self.total = 0
        self.lock = threading.RLock()

    def add(self, amount):
        with self.lock:
            self.total += amount

    def add_twice(self, amount):
        with self.lock:
            self.add(amount)
            self.add(amount)


ledger = Ledger()
threads = [threading.Thread(target=ledger.add_twice, args=(5,)) for _ in range(4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(ledger.total)
