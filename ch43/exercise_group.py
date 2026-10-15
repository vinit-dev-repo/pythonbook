# exercise_group.py
import asyncio


async def main():
    names = ("index", "cache")
    readiness = {name: asyncio.Event() for name in names}
    release = asyncio.Event()
    events = []
    errors = []
    workers = {}

    async def worker(name):
        events.append(("started", name))
        try:
            readiness[name].set()
            await release.wait()
        except asyncio.CancelledError:
            events.append(("cancelled", name))
            raise
        finally:
            events.append(("cleaned", name))

    async def validate():
        for ready in readiness.values():
            await ready.wait()
        events.append(("failed", "validator"))
        raise ValueError("bad batch")

    try:
        async with asyncio.TaskGroup() as group:
            for name in names:
                workers[name] = group.create_task(worker(name), name=name)
            validator = group.create_task(validate(), name="validator")
    except* ValueError as failures:
        errors = [str(error) for error in failures.exceptions]
        events.append(("handled", "group"))

    assert errors == ["bad batch"]
    assert type(validator.exception()) is ValueError
    assert str(validator.exception()) == "bad batch"
    assert validator.done() and not validator.cancelled()
    assert all(task.done() and task.cancelled() for task in workers.values())
    cleaned = sorted(name for event, name in events if event == "cleaned")
    cancelled = sorted(name for event, name in events if event == "cancelled")
    assert cleaned == cancelled == ["cache", "index"]
    failed_at = events.index(("failed", "validator"))
    handled_at = events.index(("handled", "group"))
    for name in names:
        assert events.index(("started", name)) < failed_at
        assert failed_at < events.index(("cancelled", name))
        assert events.index(("cancelled", name)) < events.index(("cleaned", name))
        assert events.index(("cleaned", name)) < handled_at
    assert asyncio.all_tasks() == {asyncio.current_task()}
    print("cleaned:", cleaned)
    print("selected errors:", errors)
    print("both waiting workers are done and cancelled")


if __name__ == "__main__":
    asyncio.run(main())
