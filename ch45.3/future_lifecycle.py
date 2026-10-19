# future_lifecycle.py
import threading
from concurrent.futures import CancelledError, ThreadPoolExecutor


def run_lifecycle():
    started = threading.Event()
    release = threading.Event()
    side_effects = []
    worker_threads = []

    def held_job():
        worker_threads.append(threading.current_thread())
        started.set()
        release.wait()
        return "finished"

    def failed_job():
        raise ValueError("job failed")

    def cancelled_job():
        side_effects.append("cancelled job ran")

    with ThreadPoolExecutor(max_workers=1) as pool:
        running = pool.submit(held_job)
        try:
            assert started.wait(timeout=5), "worker did not start"
            failed = pool.submit(failed_job)
            queued = pool.submit(cancelled_job)
            assert running.running()
            assert not failed.running() and not failed.done()
            assert not queued.running() and not queued.done()

            running_cancel = running.cancel()
            timed_out = False
            try:
                running.result(timeout=0)
            except TimeoutError:
                timed_out = True
            running_after_timeout = running.running()

            queued_cancel = queued.cancel()
            cancelled_error = None
            if queued_cancel:
                try:
                    queued.result()
                except CancelledError as error:
                    cancelled_error = type(error)
        finally:
            # Release before the executor context waits for its worker.
            release.set()

        value = running.result()
        failure = None
        try:
            failed.result()
        except ValueError as error:
            failure = error

    return {
        "value": value,
        "failure": failure,
        "running_cancel": running_cancel,
        "timed_out": timed_out,
        "running_after_timeout": running_after_timeout,
        "queued_cancel": queued_cancel,
        "queued_cancelled": queued.cancelled(),
        "cancelled_error": cancelled_error,
        "all_done": all(f.done() for f in (running, failed, queued)),
        "failed_cancelled": failed.cancelled(),
        "side_effects": side_effects,
        "workers_stopped": all(not thread.is_alive() for thread in worker_threads),
    }


def run_shutdown():
    started = threading.Event()
    release = threading.Event()
    side_effects = []
    worker_threads = []

    def held_job():
        worker_threads.append(threading.current_thread())
        started.set()
        release.wait()
        return "released after shutdown"

    def queued_job():
        side_effects.append("queued job ran")

    with ThreadPoolExecutor(max_workers=1) as pool:
        running = pool.submit(held_job)
        try:
            assert started.wait(timeout=5), "worker did not start"
            queued = pool.submit(queued_job)
            pool.shutdown(wait=False, cancel_futures=True)
            still_running = running.running()
            submit_error = None
            try:
                pool.submit(queued_job)
            except RuntimeError as error:
                submit_error = error
        finally:
            release.set()
        # Leaving this context performs waiting shutdown, even after wait=False.

    return {
        "still_running_after_shutdown": still_running,
        "running_cancelled": running.cancelled(),
        "value": running.result(),
        "running_done": running.done(),
        "queued_cancelled": queued.cancelled(),
        "queued_done": queued.done(),
        "submit_error": submit_error,
        "side_effects": side_effects,
        "workers_stopped": all(not thread.is_alive() for thread in worker_threads),
    }


def main():
    state = run_lifecycle()
    print("running cancel:", state["running_cancel"])
    print("wait timed out:", state["timed_out"])
    print("running value:", state["value"])
    print("job error:", type(state["failure"]).__name__, str(state["failure"]))
    print("queued cancelled:", state["queued_cancelled"])
    print("cancelled job effects:", state["side_effects"])
    shutdown = run_shutdown()
    print("running after wait=False:", shutdown["still_running_after_shutdown"])
    print("shutdown cancelled queued:", shutdown["queued_cancelled"])
    print("new submit rejected:", type(shutdown["submit_error"]) is RuntimeError)
    print("workers stopped:", state["workers_stopped"] and shutdown["workers_stopped"])


if __name__ == "__main__":
    main()
