# exercise_futures.py
import threading
from concurrent.futures import CancelledError, ThreadPoolExecutor


def main():
    started = threading.Event()
    release = threading.Event()
    effects = []
    worker_threads = []

    def square_3():
        worker_threads.append(threading.current_thread())
        started.set()
        release.wait()
        return 3 * 3

    def fail_5():
        raise ValueError("bad 5")

    def record_9():
        effects.append(9)
        return 9 * 9

    with ThreadPoolExecutor(max_workers=1) as pool:
        success = pool.submit(square_3)
        try:
            assert started.wait(timeout=5)
            failure = pool.submit(fail_5)
            cancelled = pool.submit(record_9)
            assert not success.cancel()
            try:
                success.result(timeout=0)
            except TimeoutError:
                pass
            else:
                raise AssertionError("held job unexpectedly finished")
            assert success.running()
            assert cancelled.cancel()
        finally:
            release.set()

    assert success.done() and not success.cancelled()
    assert success.result() == 9
    assert failure.done() and not failure.cancelled()
    try:
        failure.result()
    except ValueError as error:
        assert type(error) is ValueError and str(error) == "bad 5"
    else:
        raise AssertionError("job 5 did not fail")
    assert cancelled.done() and cancelled.cancelled()
    try:
        cancelled.result()
    except CancelledError:
        pass
    else:
        raise AssertionError("cancelled result did not raise")
    assert effects == []
    assert all(not thread.is_alive() for thread in worker_threads)
    print("job 3:", success.result())
    print("job 5: ValueError bad 5")
    print("job 9: cancelled; side effects:", effects)


if __name__ == "__main__":
    main()
