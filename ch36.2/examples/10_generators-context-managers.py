import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield                       # this is where the "with" block's code runs
    finally:
        print(f"took {int((time.perf_counter() - start) * 10) / 10:.1f} seconds")
