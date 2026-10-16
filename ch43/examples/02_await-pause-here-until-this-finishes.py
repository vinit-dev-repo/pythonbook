import asyncio

async def greet():
    print("hello from inside the coroutine")
    return "done"

async def main():
    result = await greet()   # actually runs greet(), and waits for its result
    print(result)

asyncio.run(main())
