# to_thread_lifecycle.py
import asyncio
import threading


async def run_case(*, preserve_result=False, value=42):
    loop = asyncio.get_running_loop()
    ready = asyncio.Event()
    cleaned = asyncio.Event()
    release = threading.Event()
    workers = []

    def worker():
        workers.append(threading.current_thread())
        loop.call_soon_threadsafe(ready.set)
        try:
            release.wait()
            return value
        finally:
            # Notify the loop after this job's cleanup work.
            loop.call_soon_threadsafe(cleaned.set)

    task = asyncio.create_task(asyncio.to_thread(worker))
    result = None
    timed_out = False
    try:
        await ready.wait()
        awaited = asyncio.shield(task) if preserve_result else task
        try:
            await asyncio.wait_for(awaited, timeout=0)
        except TimeoutError:
            timed_out = True
        at_timeout = {
            "started": ready.is_set(),
            "cancelled": task.cancelled(),
            "done": task.done(),
            "cleaned": cleaned.is_set(),
            "worker_alive": workers[0].is_alive(),
        }
    finally:
        # Cooperate with the job before the loop is allowed to close.
        release.set()
        await cleaned.wait()
        if preserve_result:
            result = await task

    return {
        "preserve_result": preserve_result,
        "timed_out": timed_out,
        "at_timeout": at_timeout,
        "cleaned_after": cleaned.is_set(),
        "task_done_after": task.done(),
        "task_cancelled_after": task.cancelled(),
        "result": result,
        "worker": workers[0],
    }


async def main():
    return [await run_case(), await run_case(preserve_result=True)]


if __name__ == "__main__":
    reports = asyncio.run(main())
    for report in reports:
        label = "shielded" if report["preserve_result"] else "ordinary"
        state = report["at_timeout"]
        print(label, "timeout:", report["timed_out"],
              "cancelled:", state["cancelled"], "cleaned:", state["cleaned"])
        print(label, "after cleanup:", report["cleaned_after"],
              "result:", report["result"])
    assert all(not report["worker"].is_alive() for report in reports)
    print("worker threads stopped after asyncio.run")
