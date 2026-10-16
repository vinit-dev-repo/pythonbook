import time

class Timer:
    def __enter__(self):
        self._start = time.perf_counter()
        return self                       # "as t" will be bound to this

    def __exit__(self, exc_type, exc_value, traceback):
        self.seconds = time.perf_counter() - self._start
        # fewer displayed digits; the measured time can still vary
        print(f"took {int(self.seconds * 10) / 10:.1f} seconds")
