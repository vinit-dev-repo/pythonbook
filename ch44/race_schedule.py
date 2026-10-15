# race_schedule.py
import threading


def lost_update(start=100, amount=1):
    balance = start
    both_read = threading.Barrier(2)

    def deposit():
        nonlocal balance
        current = balance
        both_read.wait(timeout=5)
        balance = current + amount

    workers = [threading.Thread(target=deposit) for _ in range(2)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    assert all(not worker.is_alive() for worker in workers)
    return balance


if __name__ == "__main__":
    actual = lost_update()
    assert actual == 101
    print("intended:", 102)
    print("controlled result:", actual)
