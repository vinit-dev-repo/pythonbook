# queue_lifecycle.py
import queue
import threading

END = object()

def run_batch(values, *, fail_on=None):
    work = queue.Queue(maxsize=2)
    outcomes = queue.Queue()

    def worker():
        while True:
            value = work.get()
            try:
                if value is END:
                    return
                try:
                    if value == fail_on:
                        raise ValueError("selected failure")
                    square = value * value
                except ValueError:
                    outcomes.put(("failure", value))
                else:
                    outcomes.put(("success", value, square))
            finally:
                work.task_done()

    workers = [
        threading.Thread(target=worker, daemon=False)
        for _ in range(2)
    ]
    for thread in workers:
        thread.start()

    for value in values:
        work.put(value)
    for _ in workers:
        work.put(END)

    work.join()
    for thread in workers:
        thread.join()
    assert all(not thread.is_alive() for thread in workers)

    successes = []
    failures = []
    for _ in values:
        record = outcomes.get_nowait()
        if record[0] == "success":
            successes.append((record[1], record[2]))
        else:
            failures.append(record[1])
    return sorted(successes), sorted(failures)
