from math import ceil
from random import Random

def sampled_jobs(seed, number):
    rng = Random(seed)
    return [max(1, ceil(rng.expovariate(1 / 4))) for _ in range(number)]

durations = sampled_jobs(29, 4)
assert durations == sampled_jobs(29, 4)
trace, completed, pending, cleaned = simulate_stations(
    {"sample": (0, durations)}, until=sum(durations)
)
assert completed == {"sample": sum(durations)} and pending == []
assert cleaned == ["sample"]
print("seeded batch completed:", len(trace) - 1)
