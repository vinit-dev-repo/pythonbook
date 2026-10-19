# measure_report.py
import platform
import timeit

from profile_report import build_workload
from report import summarize_indexed, summarize_naive


REPEAT = 5
CALLS_PER_BATCH = 3


def measure(name, summary, rows, categories):
    batches = timeit.repeat(
        lambda: summary(rows, categories),
        repeat=REPEAT,
        number=CALLS_PER_BATCH,
    )
    best_per_call = min(batches) / CALLS_PER_BATCH
    print(f"{name} raw batches (seconds): {batches}")
    print(f"{name} best observed per call (seconds): {best_per_call}")


if __name__ == "__main__":
    rows, categories = build_workload()
    assert summarize_naive(rows, categories) == summarize_indexed(rows, categories)
    print(f"Python: {platform.python_implementation()} {platform.python_version()}")
    print(f"Workload: {len(rows)} rows, {len(categories)} requested categories")
    print(f"Batches: {REPEAT}; calls per batch: {CALLS_PER_BATCH}")
    measure("naive", summarize_naive, rows, categories)
    measure("indexed", summarize_indexed, rows, categories)
