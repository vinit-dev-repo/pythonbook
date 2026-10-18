import functools

def retry(times):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*a, **kw):
            for attempt in range(1, times + 1):
                try:
                    return func(*a, **kw)
                except ValueError:
                    print(f"  attempt {attempt} failed")
            raise RuntimeError("gave up")
        return wrapper
    return decorate

calls = []

@retry(times=3)
def flaky():
    calls.append(1)
    if len(calls) < 3:
        raise ValueError("not yet")
    return "worked on attempt 3"

print(flaky())
