# exercise_process.py
import multiprocessing

from process_lifecycle import observe_result
from test_process_lifecycle import require_cleanup, require_success


def main():
    first = observe_result(4)
    second = observe_result(5, fail=True)
    require_success(first, 4)
    assert first["message"] == ("ok", 16) and not first["eof"]
    assert second["message"] is None and second["eof"]
    assert second["exitcode"] == 1
    assert first["join_return"] is None and second["join_return"] is None
    require_cleanup(first)
    require_cleanup(second)
    assert multiprocessing.active_children() == []
    print("first child:", first["message"], "exit:", first["exitcode"])
    print("second child: EOF:", second["eof"], "exit:", second["exitcode"])
    print("both resources closed; no active child")


if __name__ == "__main__":
    main()
