import asyncio
import time

# 1
async def greet(name):
    await asyncio.sleep(1)
    print(f"hi {name}")

async def q1():
    start = time.perf_counter()
    await asyncio.gather(greet("Amy"), greet("Ben"))
    print(f"took {round(time.perf_counter() - start)}.0s")

asyncio.run(q1())

# 2
async def wait_for(n, seconds):
    await asyncio.sleep(seconds)
    print(f"{n}: waited {seconds}s")

async def q2():
    start = time.perf_counter()
    await asyncio.gather(wait_for("A", 1), wait_for("B", 2), wait_for("C", 3))
    print(f"total: {round(time.perf_counter() - start)}.0s")   # requested waits can overlap; observed total varies

asyncio.run(q2())

# 3
async def might_fail(n):
    if n == 2:
        raise ValueError("bad n")
    return n * 10

async def q3():
    results = await asyncio.gather(
        might_fail(1), might_fail(2), might_fail(3),
        return_exceptions=True,
    )
    for r in results:
        print(r)

asyncio.run(q3())

# 4
async def slow():
    await asyncio.sleep(3)
    return "done"

async def q4():
    try:
        print(await asyncio.wait_for(slow(), timeout=1))
    except TimeoutError:
        print("too slow")

asyncio.run(q4())

# 5
async def worker(name, seconds):
    await asyncio.sleep(seconds)
    print(f"{name} finished")

async def q5():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(worker("first", 1))
        tg.create_task(worker("second", 2))
    print("all done")

asyncio.run(q5())
