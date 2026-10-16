import tracemalloc
import inspect

tracemalloc.start()
before = tracemalloc.take_snapshot()

kept = []
for i in range(200_000):
    kept.append(str(i))              # the line that is holding on to the memory
append_line = inspect.currentframe().f_lineno - 1

after = tracemalloc.take_snapshot()
top = after.compare_to(before, "lineno")[0]

print("tracemalloc points at the append line:", top.traceback[0].lineno == append_line)
print("it grew by more than 1 MB:", top.size_diff > 1_000_000)
tracemalloc.stop()
