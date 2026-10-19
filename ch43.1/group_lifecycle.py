# group_lifecycle.py
import asyncio

async def run_group(*, fail=True):
    ready = asyncio.Event()
    release = asyncio.Event()
    events = []
    errors = []

    async def worker():
        events.append("worker-started")
        try:
            ready.set()
            await release.wait()
            events.append("worker-completed")
            return "work complete"
        except asyncio.CancelledError:
            events.append("cancellation-observed")
            raise  # preserve cancellation after observing it
        finally:
            events.append("cleanup-finished")

    async def validate():
        await ready.wait()
        if fail:
            events.append("validation-failed")
            raise ValueError("invalid record")
        events.append("validation-passed")
        release.set()
        return "record valid"

    try:
        async with asyncio.TaskGroup() as group:
            worker_task = group.create_task(worker(), name="worker")
            validator_task = group.create_task(validate(), name="validator")
    except* ValueError as failures:
        errors = [str(error) for error in failures.exceptions]
        events.append("group-handled")
    else:
        events.append("group-completed")

    assert worker_task.done() and validator_task.done()
    worker_cancelled = worker_task.cancelled()
    validator_error = validator_task.exception()
    state = {
        "worker_done": worker_task.done(),
        "worker_cancelled": worker_cancelled,
        "worker_result": None if worker_cancelled else worker_task.result(),
        "validator_done": validator_task.done(),
        "validator_cancelled": validator_task.cancelled(),
        "validator_error": validator_error,
        "validator_result": (
            validator_task.result() if validator_error is None else None
        ),
    }
    return events, errors, state

async def main():
    events, errors, state = await run_group()
    for event in events:
        print(event)
    print("selected errors:", errors)
    print("worker cancelled:", state["worker_cancelled"])
    print("both done:", state["worker_done"] and state["validator_done"])

if __name__ == "__main__":
    asyncio.run(main())
