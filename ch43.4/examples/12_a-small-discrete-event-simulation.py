import heapq
from itertools import count

def print_station(name, durations, cleaned):
    try:
        clock = yield (0, "ready")
        for job, duration in enumerate(durations, start=1):
            clock = yield (duration, f"job {job} complete")
        return clock
    finally:
        cleaned.append(name)

def simulate_stations(specifications, *, until):
    if type(until) is not int or until < 0:
        raise ValueError("until must be a nonnegative integer")
    prepared = {}
    for name, (start, durations) in specifications.items():
        if type(name) is not str or not name:
            raise ValueError("each station needs a nonempty name")
        if type(start) is not int or start < 0:
            raise ValueError("start must be a nonnegative integer")
        if type(durations) not in (list, tuple):
            raise TypeError("durations must be a finite list or tuple")
        if any(type(value) is not int or value <= 0 for value in durations):
            raise ValueError("durations must be positive integers")
        prepared[name] = (start, tuple(durations))

    queue = []
    sequence = count()
    active = {}
    cleaned = []
    trace = []
    completed = {}
    try:
        for name, (start, durations) in prepared.items():
            process = print_station(name, durations, cleaned)
            active[name] = process
            delay, action = next(process)
            heapq.heappush(queue, (start + delay, next(sequence), name, action))
        while queue and queue[0][0] <= until:
            clock, _, name, action = heapq.heappop(queue)
            trace.append((clock, name, action))
            try:
                delay, action = active[name].send(clock)
            except StopIteration as done:
                completed[name] = done.value
                del active[name]
            else:
                heapq.heappush(queue, (clock + delay, next(sequence), name, action))
        pending = [(time, name, action) for time, _, name, action in sorted(queue)]
    finally:
        for process in active.values():
            process.close()
    return trace, completed, pending, cleaned

specifications = {"north": (0, [3, 2]), "south": (1, [2])}
trace, completed, pending, cleaned = simulate_stations(specifications, until=4)
for event in trace:
    print(event)
print("completed:", completed)
print("pending:", pending)
print("cleaned:", sorted(cleaned))
