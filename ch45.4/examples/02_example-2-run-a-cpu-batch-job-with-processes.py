import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor

sys.set_int_max_str_digits(1_000_000)   # Python 3.11+ caps int→str conversion at 4,300 digits by default

def big_factorial(n):
    return n, len(str(math.factorial(n)))   # return the digit COUNT, not the huge number itself

numbers = [50_000, 60_000, 70_000, 80_000]

if __name__ == "__main__":
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        for n, digit_count in pool.map(big_factorial, numbers):
            print(f"{n}! has {digit_count} digits")
    print(f"Took {time.perf_counter() - start:.2f}s")
