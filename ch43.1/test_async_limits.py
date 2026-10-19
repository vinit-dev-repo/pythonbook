# test_async_limits.py
import asyncio

from async_counter import lost_update, protected_update
from async_limits import run_limited

def require_intended_total(actual, start, amount):
    assert actual == start + 2 * amount, "one increment was lost"

async def main():
    for values, limit in [([], 2), ([0, 1, 2, 3, 4], 2), ([1, 2], 1), ([2, 2, 5], 2)]:
        report = await run_limited(values, limit=limit)
        assert report["results"] == [
            (index, value, value * value) for index, value in enumerate(values)
        ]
        assert report["errors"] == []
        assert report["peak"] == min(limit, len(values))
        assert report["active"] == 0 and report["all_done"]
        assert report["processing_tasks"] == len(values)
        assert report["coordinator_tasks"] == (1 if values else 0)
        assert asyncio.all_tasks() == {asyncio.current_task()}

    failure = await run_limited([0, 1, 2, 3, 4], limit=2, fail_on=0)
    assert failure["errors"] == ["selected failure"]
    assert 1 <= failure["peak"] <= 2
    assert failure["active"] == 0 and failure["all_done"]
    assert asyncio.all_tasks() == {asyncio.current_task()}
    fresh = await run_limited([3], limit=2)
    assert fresh["results"] == [(0, 3, 9)] and fresh["errors"] == []
    assert fresh["peak"] == 1 and fresh["active"] == 0 and fresh["all_done"]

    for start, amount in [(100, 1), (10, 4)]:
        broken = await lost_update(start, amount)
        fixed = await protected_update(start, amount)
        assert broken == start + amount
        try:
            require_intended_total(broken, start, amount)
        except AssertionError as error:
            assert str(error) == "one increment was lost"
        else:
            raise AssertionError("controlled lost update was not detected")
        require_intended_total(fixed, start, amount)
        assert asyncio.all_tasks() == {asyncio.current_task()}
    print("async capacity, cleanup and counter assertions passed")

if __name__ == "__main__":
    asyncio.run(main())
