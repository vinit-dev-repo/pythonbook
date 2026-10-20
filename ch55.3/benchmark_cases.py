# benchmark_cases.py
import json
import platform
import sys
import timeit

def adjust(value):
    return value * 3 - 1

def with_loop(values, operation):
    result = []
    for value in values:
        result.append(operation(value))
    return result

def with_list(values, operation):
    return [operation(value) for value in values]

def with_map(values, operation):
    return list(map(operation, values))

def with_expression(values, operation):
    return list(operation(value) for value in values)

def emit_values(values, operation):
    for value in values:
        yield operation(value)

def with_generator(values, operation):
    return list(emit_values(values, operation))

def inline_loop(values):
    result = []
    for value in values:
        result.append(value * 3 - 1)
    return result

def inline_list(values):
    return [value * 3 - 1 for value in values]

def benchmark():
    values = tuple(range(-100, 100))
    number, repeat = 100, 3
    jobs = []
    builders = (with_loop, with_list, with_map, with_expression, with_generator)
    for label, operation in (("absolute", abs), ("affine", adjust)):
        expected = [operation(value) for value in values]
        for builder in builders:
            call = lambda builder=builder, operation=operation: builder(values, operation)
            jobs.append((f"{label}/{builder.__name__}", call, expected))
    expected = [adjust(value) for value in values]
    for builder in (inline_loop, inline_list):
        jobs.append((builder.__name__, lambda builder=builder: builder(values), expected))
    results = []
    for label, call, expected in jobs:
        if call() != expected:
            raise AssertionError(f"wrong result: {label}")
        totals = timeit.Timer(call).repeat(number=number, repeat=repeat)
        results.append({"case": label, "totals_seconds": totals,
                        "best_seconds_per_call": min(totals) / number})
    return {"implementation": platform.python_implementation(),
            "version": platform.python_version(), "executable": sys.executable,
            "platform": platform.platform(), "input_size": len(values),
            "number": number, "repeat": repeat, "results": results}

if __name__ == "__main__":
    print(json.dumps(benchmark()))
