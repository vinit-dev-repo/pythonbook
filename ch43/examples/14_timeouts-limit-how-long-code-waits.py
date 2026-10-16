import asyncio

async def main():
    try:
        async with asyncio.timeout(2):
            await asyncio.sleep(1)
            print("first part finished")
            await asyncio.sleep(5)     # this pushes us past the 2-second budget
            print("never gets here")
    except TimeoutError:
        print("the whole block ran out of time")

asyncio.run(main())
