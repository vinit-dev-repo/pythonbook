import time
import numpy as np

n = 10_000_000
numbers = list(range(n))
arr = np.arange(n)

start = time.perf_counter()
total = sum(numbers)
loop_time = time.perf_counter() - start

start = time.perf_counter()
total_np = arr.sum()
numpy_time = time.perf_counter() - start

assert int(total_np) == total == n * (n - 1) // 2

print(f"Python sum():  {loop_time:.4f} seconds")
print(f"NumPy arr.sum(): {numpy_time:.4f} seconds")
print(f"Python/NumPy duration ratio: {loop_time / numpy_time:.2f}")
