import asyncio
import time

async def async_task(name):
    print(f"{name}: starting")
    await asyncio.sleep(3)      # pauses this coroutine; other tasks can run
    print(f"{name}: done")

async def main():
    start = time.perf_counter()
    await asyncio.gather(
        async_task("A"),
        async_task("B"),
        async_task("C"),
    )
    print(f"total time: {round(time.perf_counter() - start)}.0s")
