import timeit

pieces = 2000
executions = 2
plain_totals = timeit.repeat(
    lambda: build_concat(pieces), number=executions, repeat=3
)
join_totals = timeit.repeat(
    lambda: build_join(pieces), number=executions, repeat=3
)
kept_totals = timeit.repeat(
    lambda: build_concat_kept(pieces), number=executions, repeat=3
)
print("plain += totals (seconds):", plain_totals)
print("join totals (seconds):", join_totals)
print("retained-prefix totals (seconds):", kept_totals)
print(f"plain += best per build: {min(plain_totals) / executions:.9f} seconds")
print(f"join best per build: {min(join_totals) / executions:.9f} seconds")
print(f"retained-prefix best per build: {min(kept_totals) / executions:.9f} seconds")
