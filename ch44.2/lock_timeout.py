# lock_timeout.py
import threading

lock_b = threading.Lock()
attempts = []

def try_lock():
    acquired = lock_b.acquire(timeout=0.05)
    try:
        attempts.append(acquired)
    finally:
        if acquired:
            lock_b.release()

lock_b.acquire()
try:
    worker = threading.Thread(target=try_lock)
    worker.start()
    worker.join()
    assert not worker.is_alive()
finally:
    lock_b.release()

assert attempts == [False]
print("held lock: attempt timed out")
try_lock()
assert attempts == [False, True]
assert not lock_b.locked()
print("released lock: attempt succeeded")
