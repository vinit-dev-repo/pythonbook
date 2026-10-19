# async_limits.py
import asyncio

async def run_limited(values, *, limit=2, fail_on=None):
    if not values:
        return {
            "results": [], "errors": [], "peak": 0, "active": 0,
            "processing_tasks": 0, "coordinator_tasks": 0, "all_done": True,
        }

    semaphore = asyncio.Semaphore(limit)
    ready = asyncio.Event()
    release = asyncio.Event()
    first_wave = min(limit, len(values))
    active = 0
    peak = 0
    results = []
    errors = []

    async def process(index, value):
        nonlocal active, peak
        async with semaphore:
            active += 1
            peak = max(peak, active)
            if active == first_wave:
                ready.set()
            try:
                await release.wait()
                await asyncio.sleep(0)
                if value == fail_on:
                    raise ValueError("selected failure")
                results.append((index, value, value * value))
            finally:
                active -= 1

    async def release_first_wave():
        await ready.wait()
        release.set()

    try:
        async with asyncio.TaskGroup() as group:
            jobs = [
                group.create_task(process(index, value))
                for index, value in enumerate(values)
            ]
            coordinator = group.create_task(release_first_wave())
    except* ValueError as failures:
        errors = [str(error) for error in failures.exceptions]

    return {
        "results": sorted(results),
        "errors": errors,
        "peak": peak,
        "active": active,
        "processing_tasks": len(jobs),
        "coordinator_tasks": 1,
        "all_done": coordinator.done() and all(task.done() for task in jobs),
    }

async def main():
    report = await run_limited([0, 1, 2, 3, 4], limit=2)
    print("indexed results:", report["results"])
    print("peak active:", report["peak"])
    print("processing tasks:", report["processing_tasks"])
    print("active after group:", report["active"])
    print("all child tasks done:", report["all_done"])

if __name__ == "__main__":
    asyncio.run(main())
