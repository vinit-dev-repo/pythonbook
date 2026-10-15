# test_group_lifecycle.py
import asyncio

from group_lifecycle import run_group


async def main():
    events, errors, state = await run_group()
    assert events == [
        "worker-started", "validation-failed", "cancellation-observed",
        "cleanup-finished", "group-handled",
    ]
    assert errors == ["invalid record"]
    assert state["worker_cancelled"], "worker must remain cancelled"
    assert state["worker_done"] and state["validator_done"]
    assert not state["validator_cancelled"]
    assert type(state["validator_error"]) is ValueError
    assert str(state["validator_error"]) == "invalid record"
    assert state["worker_result"] is None
    assert state["validator_result"] is None
    assert asyncio.all_tasks() == {asyncio.current_task()}

    # A fresh successful call follows the failed call in this same event loop.
    events, errors, state = await run_group(fail=False)
    assert events == [
        "worker-started", "validation-passed", "worker-completed",
        "cleanup-finished", "group-completed",
    ]
    assert errors == []
    assert state == {
        "worker_done": True,
        "worker_cancelled": False,
        "worker_result": "work complete",
        "validator_done": True,
        "validator_cancelled": False,
        "validator_error": None,
        "validator_result": "record valid",
    }
    assert asyncio.all_tasks() == {asyncio.current_task()}
    print("group lifecycle assertions passed")


if __name__ == "__main__":
    asyncio.run(main())
