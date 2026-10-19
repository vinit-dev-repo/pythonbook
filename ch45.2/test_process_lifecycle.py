# test_process_lifecycle.py
import multiprocessing
import os

from process_lifecycle import observe_result, observe_stop

def require_success(report, value):
    assert report["exitcode"] == 0 and report["message"] == ("ok", value * value), "child did not deliver a successful result"
    assert not report["eof"]

def require_cleanup(report):
    assert report["pid"] != os.getpid()
    assert not report["alive"]
    assert report["receiver_closed"] and report["sender_closed"]
    assert report["process_closed"] and not report["forced_termination"]
    assert all(child.pid != report["pid"] for child in multiprocessing.active_children())

def main():
    success = observe_result(3)
    require_success(success, 3)
    require_cleanup(success)
    assert success["join_return"] is None
    failure = observe_result(3, fail=True)
    assert failure["message"] is None and failure["eof"]
    assert failure["exitcode"] == 1 and failure["join_return"] is None
    require_cleanup(failure)
    try:
        require_success(failure, 3)
    except AssertionError as error:
        assert str(error) == "child did not deliver a successful result"
    else:
        raise AssertionError("failed child was accepted as successful")
    stopped = observe_stop()
    assert stopped["ready"] == "ready" and stopped["cleaned"] == "cleaned"
    assert stopped["short_join_return"] is None
    assert stopped["alive_after_short_join"]
    assert stopped["exitcode_after_short_join"] is None
    assert stopped["completed_join_return"] is None and stopped["exitcode"] == 0
    require_cleanup(stopped)
    fresh = observe_result(4)
    require_success(fresh, 4)
    require_cleanup(fresh)
    assert multiprocessing.active_children() == []
    print("raw process lifecycle assertions passed")

if __name__ == "__main__":
    main()
