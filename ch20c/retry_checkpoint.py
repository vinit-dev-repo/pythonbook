# retry_checkpoint.py
from functools import wraps

def retry(times):
    if isinstance(times, bool) or not isinstance(times, int):
        raise TypeError("times must be an integer, not bool")
    if times <= 0:
        raise ValueError("times must be positive")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
        return wrapper
    return decorator

if __name__ == "__main__":
    attempts = []

    @retry(3)
    def flaky():
        """Succeed on the third attempt."""
        attempts.append(1)
        if len(attempts) < 3:
            raise ValueError("not yet")
        return "worked on attempt " + str(len(attempts))

    print(flaky())
    print(flaky.__name__)
