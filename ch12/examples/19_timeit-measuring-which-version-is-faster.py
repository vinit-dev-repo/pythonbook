import timeit

executions = 1000
list_totals = timeit.repeat(
    "sum([i * i for i in range(1000)])", number=executions, repeat=3
)
generator_totals = timeit.repeat(
    "sum(i * i for i in range(1000))", number=executions, repeat=3
)
print("list totals (seconds):", list_totals)
print("generator totals (seconds):", generator_totals)
print(f"list best per execution: {min(list_totals) / executions:.9f} seconds")
print(f"generator best per execution: {min(generator_totals) / executions:.9f} seconds")
