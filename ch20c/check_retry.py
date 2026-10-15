# check_retry.py
from retry_checkpoint import retry

calls = []
@retry(3)
def add(a, *, extra):
    """Add two values."""
    calls.append(1)
    return a + extra

print(add(2, extra=5), len(calls))
print(add.__name__, add.__doc__)

for count in (0, -1, True, 2.5):
    try:
        retry(count)
    except (TypeError, ValueError) as error:
        print(type(error).__name__)
print(len(calls))
