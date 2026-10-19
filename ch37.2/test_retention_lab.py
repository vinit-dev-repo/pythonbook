# test_retention_lab.py
import tracemalloc
import retention_lab

def check(count, size):
    report = retention_lab.run_experiment(count, size)
    assert not tracemalloc.is_tracing()
    assert report["count"] == count
    assert report["total_payload_bytes"] == count * size
    assert report["grew"] and report["still_owned"] and report["released"]
    assert report["scalar_result"] == (count, count * size)
    assert report["scalar_before_bytes"] == report["scalar_after_bytes"]
    assert report["scalar_retained_nothing"]

def check_decrease_rule():
    report = retention_lab.run_experiment(16, 4096)
    assert not tracemalloc.is_tracing()
    try:
        retention_lab.require_decrease(report["retained_bytes"], report["still_owned_bytes"])
    except AssertionError:
        pass
    else:
        raise AssertionError("the actual still-owned snapshot must not count as release")
    retention_lab.require_decrease(report["still_owned_bytes"], report["released_bytes"])
    assert report["released"]

if __name__ == "__main__":
    check(32, 8192)
    check(16, 4096)
    check_decrease_rule()
    assert not tracemalloc.is_tracing()
    print("two batch sizes retain, then release traced payload bytes")
