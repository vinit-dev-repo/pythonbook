# locked_update.py
import threading


def protected_update(start=100, amount=1):
    balance = start
    lock = threading.Lock()

    def deposit():
        nonlocal balance
        with lock:
            current = balance
            balance = current + amount

    workers = [threading.Thread(target=deposit) for _ in range(2)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    assert all(not worker.is_alive() for worker in workers)
    return balance


if __name__ == "__main__":
    actual = protected_update()
    assert actual == 102
    print("protected result:", actual)
