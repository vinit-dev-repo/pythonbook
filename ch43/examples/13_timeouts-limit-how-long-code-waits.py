import asyncio

async def slow_task():
    await asyncio.sleep(5)
    return "finally done"

async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2)
        print(result)
    except TimeoutError:
        print("gave up -- took too long")

asyncio.run(main())
