# exercise_to_thread_lifecycle.py
import asyncio
from to_thread_lifecycle import run_case
from test_to_thread_lifecycle import check_report


async def solve():
    ordinary = await run_case(value=99)
    preserved = await run_case(preserve_result=True, value=99)
    for report in (ordinary, preserved):
        check_report(report, 99)
    assert ordinary["result"] is None
    assert preserved["result"] == 99
    assert not (asyncio.all_tasks() - {asyncio.current_task()})
    return ordinary, preserved


if __name__ == "__main__":
    ordinary, preserved = asyncio.run(solve())
    assert not ordinary["worker"].is_alive()
    assert not preserved["worker"].is_alive()
    print("ordinary result:", ordinary["result"])
    print("preserved result:", preserved["result"])
    print("both jobs cleaned up; runner stopped worker threads")
