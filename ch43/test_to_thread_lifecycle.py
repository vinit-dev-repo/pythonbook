# test_to_thread_lifecycle.py
import asyncio
from to_thread_lifecycle import run_case


def require_cleanup(complete):
    assert complete, "worker cleanup has not completed"


def check_report(report, value):
    state = report["at_timeout"]
    preserved = report["preserve_result"]
    assert report["timed_out"]
    assert state["started"] and state["worker_alive"]
    assert state["cancelled"] is (not preserved)
    assert state["done"] is (not preserved)
    try:
        require_cleanup(state["cleaned"])
    except AssertionError as error:
        assert str(error) == "worker cleanup has not completed"
    else:
        raise AssertionError("timeout incorrectly treated as worker cleanup")
    require_cleanup(report["cleaned_after"])
    assert report["task_done_after"]
    assert report["task_cancelled_after"] is (not preserved)
    assert report["result"] == (value if preserved else None)


async def check_cases(value=42):
    reports = []
    for _ in range(2):
        for preserved in (False, True):
            report = await run_case(preserve_result=preserved, value=value)
            check_report(report, value)
            reports.append(report)
            pending = asyncio.all_tasks() - {asyncio.current_task()}
            assert not pending, pending
    return reports


if __name__ == "__main__":
    reports = asyncio.run(check_cases())
    assert all(not report["worker"].is_alive() for report in reports)
    print("four fresh task/cleanup/result checks passed")
    print("all recorded worker threads stopped")
