# retention_lab.py
import gc
import inspect
import tracemalloc

def allocate_payload(size):
    return bytearray(size)

def allocator_line_number():
    lines, first_line = inspect.getsourcelines(allocate_payload)
    return first_line + next(index for index, line in enumerate(lines) if "bytearray(size)" in line)

def bytes_at_allocator(snapshot):
    line = allocator_line_number()
    only_allocator = tracemalloc.Filter(True, __file__, lineno=line)
    return sum(stat.size for stat in snapshot.filter_traces((only_allocator,)).statistics("lineno"))

def require_decrease(before, after):
    assert after < before, (before, after)

def run_experiment(count=32, size=8192):
    if count <= 0 or size <= 0:
        raise ValueError("count and size must be positive")
    if tracemalloc.is_tracing():
        raise RuntimeError("run this helper in a fresh non-tracing process")

    tracemalloc.start()
    try:
        baseline = bytes_at_allocator(tracemalloc.take_snapshot())
        history = []
        batch = [allocate_payload(size) for _ in range(count)]
        history.append(batch)
        logical_count = len(batch)
        total_payload_bytes = sum(map(len, batch))
        expected_content = bytes(batch[0][:4])
        retained = bytes_at_allocator(tracemalloc.take_snapshot())
        gc.collect()
        still_owned = bytes_at_allocator(tracemalloc.take_snapshot())
        assert len(history) == 1 and len(history[0]) == logical_count
        assert bytes(history[0][0][:4]) == expected_content
        assert still_owned >= retained > baseline
        del batch
        history.clear()
        released = bytes_at_allocator(tracemalloc.take_snapshot())
        require_decrease(still_owned, released)
        scalar_before = bytes_at_allocator(tracemalloc.take_snapshot())
        scalar_result = scalar_only_work(count, size)
        scalar_after = bytes_at_allocator(tracemalloc.take_snapshot())
        assert scalar_result == (logical_count, total_payload_bytes)
        assert scalar_after == scalar_before
        return {"count": logical_count, "total_payload_bytes": total_payload_bytes,
                "baseline_bytes": baseline, "retained_bytes": retained,
                "still_owned_bytes": still_owned, "released_bytes": released,
                "scalar_result": scalar_result, "scalar_before_bytes": scalar_before,
                "scalar_after_bytes": scalar_after,
                "grew": retained > baseline, "still_owned": still_owned >= retained,
                "released": released < still_owned, "scalar_retained_nothing": scalar_after == scalar_before}
    finally:
        tracemalloc.stop()

def scalar_only_work(count, size):
    batch = [allocate_payload(size) for _ in range(count)]
    return len(batch), sum(map(len, batch))

if __name__ == "__main__":
    report = run_experiment()
    assert report["scalar_result"] == (report["count"], report["total_payload_bytes"])
    print("retained batch survives collection:", report["still_owned"])
    print("allocator bytes grow then decrease:", report["grew"] and report["released"])
    print("scalar-only batch leaves allocator total unchanged:", report["scalar_retained_nothing"])
