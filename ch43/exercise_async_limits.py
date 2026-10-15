# exercise_async_limits.py
import asyncio

from async_counter import lost_update, protected_update
from async_limits import run_limited


async def main():
    report = await run_limited([2, 2, 5], limit=2)
    assert report["results"] == [(0, 2, 4), (1, 2, 4), (2, 5, 25)]
    assert report["errors"] == []
    assert report["peak"] == 2 and report["processing_tasks"] == 3
    assert report["coordinator_tasks"] == 1
    assert report["active"] == 0 and report["all_done"]
    broken = await lost_update(10, 4)
    fixed = await protected_update(10, 4)
    assert broken == 14 and fixed == 18
    assert asyncio.all_tasks() == {asyncio.current_task()}
    print("indexed squares:", report["results"])
    print("peak active:", report["peak"], "processing tasks:", report["processing_tasks"])
    print("counter comparison:", broken, fixed)


if __name__ == "__main__":
    asyncio.run(main())
