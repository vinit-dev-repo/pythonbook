# measure_slots.py
import json
import platform
import timeit


class DictionaryRecord:
    pass


class SlotRecord:
    __slots__ = ("left", "right")


def workload(record_class, count=500):
    records = []
    total = 0
    for number in range(count):
        record = record_class()
        record.left = number
        record.right = number + 1
        total += record.left + record.right
        records.append(record)
    return total, len(records)


def measure():
    expected = (500 * 500, 500)
    assert workload(DictionaryRecord) == expected
    assert workload(SlotRecord) == expected
    samples = {}
    for kind in (DictionaryRecord, SlotRecord):
        samples[kind.__name__] = timeit.repeat(
            lambda: workload(kind), repeat=3, number=50
        )
    return {
        "implementation": platform.python_implementation(),
        "version": platform.python_version(),
        "records_per_call": 500,
        "calls_per_batch": 50,
        "class_definition_timed": False,
        "batch_seconds": samples,
        "best_seconds_per_call": {
            name: min(batches) / 50 for name, batches in samples.items()
        },
    }


if __name__ == "__main__":
    print(json.dumps(measure(), indent=2))
