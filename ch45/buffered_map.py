# buffered_map.py
import threading
from concurrent.futures import ThreadPoolExecutor


def observe_map(*, buffersize=None):
    consumed = []
    release = threading.Event()
    worker_threads = []

    def source():
        for value in range(6):
            consumed.append(value)
            yield value

    def square(value):
        worker_threads.append(threading.current_thread())
        release.wait()
        return value * value

    with ThreadPoolExecutor(max_workers=1) as pool:
        try:
            results = pool.map(square, source(), buffersize=buffersize)
            before_results = list(consumed)
        finally:
            release.set()
        values = list(results)

    assert all(not thread.is_alive() for thread in worker_threads)
    return before_results, values


def main():
    default_seen, default_values = observe_map()
    buffered_seen, buffered_values = observe_map(buffersize=2)
    assert default_values == buffered_values == [0, 1, 4, 9, 16, 25]
    print("default initial consumption:", default_seen)
    print("buffered initial consumption:", buffered_seen)
    print("both result lists:", buffered_values)


if __name__ == "__main__":
    main()
