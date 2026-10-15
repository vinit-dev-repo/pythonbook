# exercise_retention.py
import gc
import tracemalloc

from retention_lab import allocate_payload, bytes_at_allocator, require_decrease


def main():
    if tracemalloc.is_tracing():
        raise RuntimeError("run this exercise in a fresh non-tracing process")
    tracemalloc.start()
    try:
        history = [[allocate_payload(4096) for _ in range(8)]]
        second_owner = list(history)
        retained = bytes_at_allocator(tracemalloc.take_snapshot())
        assert history is not second_owner
        assert history[0] is second_owner[0]
        assert len(history[0]) == 8 and sum(map(len, history[0])) == 8 * 4096
        history.clear()
        gc.collect()
        still_owned = bytes_at_allocator(tracemalloc.take_snapshot())
        assert len(second_owner) == 1 and len(second_owner[0]) == 8
        assert still_owned >= retained
        try:
            require_decrease(retained, still_owned)
        except AssertionError:
            pass
        else:
            raise AssertionError("the second owner still retains the payloads")
        second_owner.clear()
        released = bytes_at_allocator(tracemalloc.take_snapshot())
        require_decrease(still_owned, released)
        print("second owner keeps shared payloads:", True)
        print("bytes decrease after both owners release:", True)
    finally:
        tracemalloc.stop()


if __name__ == "__main__":
    main()
