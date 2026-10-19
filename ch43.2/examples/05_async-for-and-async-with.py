class AsyncCountdown:
    def __init__(self, start):
        self._current = start

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._current <= 0:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)     # pretend this took a little network time
        value = self._current
        self._current -= 1
        return value

async def main():
    async for n in AsyncCountdown(3):
        print(n)

asyncio.run(main())
