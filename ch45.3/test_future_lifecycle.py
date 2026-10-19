# test_future_lifecycle.py
from concurrent.futures import CancelledError

from buffered_map import observe_map
from future_lifecycle import run_lifecycle, run_shutdown

def main():
    for _ in range(2):
        state = run_lifecycle()
        assert state["queued_cancel"] and state["queued_cancelled"], "queued cancellation missing"
        assert state["side_effects"] == [], "cancelled function ran"
        assert state["cancelled_error"] is CancelledError
        assert not state["running_cancel"]
        assert state["timed_out"] and state["running_after_timeout"]
        assert state["value"] == "finished"
        assert type(state["failure"]) is ValueError
        assert str(state["failure"]) == "job failed"
        assert not state["failed_cancelled"]
        assert state["all_done"] and state["workers_stopped"]

        shutdown = run_shutdown()
        assert shutdown["still_running_after_shutdown"]
        assert not shutdown["running_cancelled"]
        assert shutdown["value"] == "released after shutdown"
        assert shutdown["running_done"] and shutdown["queued_done"]
        assert shutdown["queued_cancelled"]
        assert type(shutdown["submit_error"]) is RuntimeError
        assert str(shutdown["submit_error"]) == "cannot schedule new futures after shutdown"
        assert shutdown["side_effects"] == []
        assert shutdown["workers_stopped"]

        default_seen, default_values = observe_map()
        buffered_seen, buffered_values = observe_map(buffersize=2)
        assert default_seen == [0, 1, 2, 3, 4, 5]
        assert buffered_seen == [0, 1]
        assert default_values == buffered_values == [0, 1, 4, 9, 16, 25]
    print("future lifecycle and buffering assertions passed")

if __name__ == "__main__":
    main()
