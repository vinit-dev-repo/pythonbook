# lock_order.py
import threading


def check_released(locks):
    for lock in locks:
        acquired = lock.acquire(blocking=False)
        assert acquired, "a worker left a lock held"
        lock.release()


def opposite_order():
    lock_a = threading.Lock()
    lock_b = threading.Lock()
    both_holding = threading.Barrier(2)
    outcomes = [None, None]

    def worker(index, first, second):
        first.acquire()
        try:
            both_holding.wait(timeout=5)
            acquired = second.acquire(timeout=0.2)
            if acquired:
                try:
                    outcomes[index] = "completed"
                finally:
                    second.release()
            else:
                outcomes[index] = "timed out"
        finally:
            first.release()

    workers = [
        threading.Thread(target=worker, args=(0, lock_a, lock_b)),
        threading.Thread(target=worker, args=(1, lock_b, lock_a)),
    ]
    for thread in workers:
        thread.start()
    for thread in workers:
        thread.join()
    assert all(not thread.is_alive() for thread in workers)
    assert all(value in {"completed", "timed out"} for value in outcomes)
    assert "timed out" in outcomes
    check_released((lock_a, lock_b))
    return outcomes


def same_order():
    lock_a = threading.Lock()
    lock_b = threading.Lock()
    outcomes = [None, None]

    def worker(index):
        with lock_a:
            with lock_b:
                outcomes[index] = "completed"

    workers = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
    for thread in workers:
        thread.start()
    for thread in workers:
        thread.join()
    assert all(not thread.is_alive() for thread in workers)
    assert outcomes == ["completed", "completed"]
    check_released((lock_a, lock_b))
    return outcomes


if __name__ == "__main__":
    opposite = opposite_order()
    ordered = same_order()
    print("opposite order: two outcomes:", len(opposite) == 2)
    print("opposite order: at least one timeout:", "timed out" in opposite)
    print("same order: both completed:", ordered == ["completed", "completed"])
