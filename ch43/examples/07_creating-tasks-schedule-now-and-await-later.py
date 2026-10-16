import asyncio

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} result"

async def main():
    task_a = asyncio.create_task(fetch("A", 2))   # queued to run
    task_b = asyncio.create_task(fetch("B", 1))   # this one too

    print("both tasks are scheduled to run")
    result_a = await task_a       # wait for A's result whenever we need it
    result_b = await task_b
    print(result_a, result_b)

asyncio.run(main())
