# measure_slot_memory.py
import argparse
import gc
import json
import platform
import tracemalloc
from measure_slots import DictionaryRecord, SlotRecord


def measure_memory(kind, count):
    if type(count) is not int:
        raise TypeError("count must be a built-in integer")
    if count < 1:
        raise ValueError("count must be positive")
    gc.collect()
    tracemalloc.start()
    try:
        before = tracemalloc.get_traced_memory()[0]
        records = [kind() for _ in range(count)]
        for record in records:
            record.left = 7
            record.right = 11
        del record
        current, peak = tracemalloc.get_traced_memory()
        del records
        gc.collect()
        after = tracemalloc.get_traced_memory()[0]
    finally:
        tracemalloc.stop()
    return {
        "implementation": platform.python_implementation(),
        "version": platform.python_version(),
        "class": kind.__name__,
        "count": count,
        "retained_delta_bytes": current - before,
        "peak_delta_bytes": peak - before,
        "after_release_delta_bytes": after - before,
        "measure": "traced Python allocations; not process RSS",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("dictionary", "slots"))
    parser.add_argument("--count", type=int, default=10000)
    options = parser.parse_args()
    kind = DictionaryRecord if options.kind == "dictionary" else SlotRecord
    print(json.dumps(measure_memory(kind, options.count), indent=2))
