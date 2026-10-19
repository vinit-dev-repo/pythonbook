import asyncio
import time
from contextlib import aclosing


# 1
class Countdown:
    def __init__(self, start):
        self.current = start

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current <= 0:
            raise StopAsyncIteration
        await asyncio.sleep(0)
        self.current -= 1
        return self.current + 1


async def q1():
    seen = [n async for n in Countdown(3)]
    print("countdown:", seen)


# 2
async def numbers(log):
    try:
        for n in range(5):
            await asyncio.sleep(0)
            yield n
    finally:
        log.append("closed")


async def q2():
    log = []
    async with aclosing(numbers(log)) as stream:
        async for n in stream:
            if n == 2:
                break
    print("log after break:", log)


# 3
def slow_square(n):
    time.sleep(0.2)
    return n * n


async def q3():
    start = time.perf_counter()
    results = await asyncio.gather(*(asyncio.to_thread(slow_square, n) for n in (1, 2, 3)))
    elapsed = time.perf_counter() - start
    print("results:", results)
    print(f"total time: {round(elapsed)}.0s")


# 4
class Session:
    def __init__(self, log):
        self.log = log

    async def __aenter__(self):
        await asyncio.sleep(0)
        self.log.append("open")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(0)
        self.log.append("close")
        return False


async def q4():
    log = []
    try:
        async with Session(log):
            log.append("work")
            raise ValueError("boom")
    except ValueError:
        log.append("handled")
    print("session log:", log)


async def main():
    await q1()
    await q2()
    await q3()
    await q4()


asyncio.run(main())
