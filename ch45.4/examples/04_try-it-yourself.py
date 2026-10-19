# 1 and 2
import math
import threading
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

barrier = threading.Barrier(3)


def meet(number):
    barrier.wait(timeout=2)
    return number


def digit_count(n):
    return n, len(str(math.factorial(n)))


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as pool:
        print(list(pool.map(meet, [1, 2, 3])))
    with ProcessPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(digit_count, [500, 1000])))

# 3
if __name__ == "__main__":
    choices = {
        "fetch a few dozen web pages": "threads",
        "resize 40 large images": "processes",
        "serve 5000 mostly idle connections": "asyncio",
    }
    for job, model in choices.items():
        print(f"{job}: {model}")
