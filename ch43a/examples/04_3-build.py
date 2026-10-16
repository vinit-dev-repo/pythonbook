import time
from contextlib import contextmanager

class timed_section:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        elapsed = time.perf_counter() - self.start
        status = "failed" if exc_type else "ok"
        print(f"{self.name}: {status} in {int(elapsed * 10) / 10:.1f}s")
        return False              # False = do NOT swallow the error

@contextmanager
def timed_section2(name):
    start = time.perf_counter()
    status = "ok"
    try:
        yield
    except Exception:
        status = "failed"
        raise                     # re-raise, so the error still escapes
    finally:
        elapsed = time.perf_counter() - start
        print(f"{name}: {status} in {int(elapsed * 10) / 10:.1f}s")

with timed_section("class version"):
    time.sleep(0.2)

try:
    with timed_section2("function version"):
        raise ValueError("boom")
except ValueError as e:
    print("error escaped, as it should:", e)
