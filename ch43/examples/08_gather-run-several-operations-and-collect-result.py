async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} took {delay}s"

async def main():
    results = await asyncio.gather(
        fetch("slow", 2),
        fetch("fast", 1),
    )
    print(results)     # "slow" is still listed FIRST -- order matches the call, not finish time

asyncio.run(main())
