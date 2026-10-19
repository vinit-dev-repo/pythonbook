# test_queue_lifecycle.py
import queue

from queue_lifecycle import run_batch


assert run_batch([]) == ([], [])
assert run_batch([0, 1, 2, 3, 4]) == (
    [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)],
    [],
)
assert run_batch([0, 1, 2, 3, 4], fail_on=2) == (
    [(0, 0), (1, 1), (3, 9), (4, 16)],
    [2],
)
assert run_batch([0, 3, 3], fail_on=3) == ([(0, 0)], [3, 3])
assert run_batch([3, 3]) == ([(3, 9), (3, 9)], [])
assert run_batch([0, 1], fail_on=0) == ([(1, 1)], [0])
assert run_batch([2]) == ([(2, 4)], [])

# Test the queue's capacity without depending on thread scheduling.
full = queue.Queue(maxsize=1)
full.put(1)
try:
    full.put_nowait(2)
except queue.Full:
    pass
else:
    raise AssertionError("a full queue accepted another item")
assert full.get() == 1
full.task_done()
full.put_nowait(2)
assert full.get() == 2
full.task_done()
full.join()
print("queue lifecycle checks: ok")
