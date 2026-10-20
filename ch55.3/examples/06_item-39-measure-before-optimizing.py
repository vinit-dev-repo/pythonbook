import timeit

executions = 1000
builtin_totals = timeit.repeat(
    lambda: sum(range(1000)), number=executions, repeat=3
)
loop_totals = timeit.repeat(
    lambda: sum_with_loop(1000), number=executions, repeat=3
)
print("built-in sum totals (seconds):", builtin_totals)
print("loop totals (seconds):", loop_totals)
print(f"built-in best per call: {min(builtin_totals) / executions:.9f} seconds")
print(f"loop best per call: {min(loop_totals) / executions:.9f} seconds")
