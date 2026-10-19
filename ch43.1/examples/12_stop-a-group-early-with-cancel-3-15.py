import asyncio

async def search(name, delay, found, group):
    await asyncio.sleep(delay)
    print(f"{name} answered")
    found.append(name)
    group.cancel()   # the goal is reached: stop the other searches

async def main():
    found = []
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(search(name, delay, found, group))
                 for name, delay in [("slow", 0.3), ("fast", 0.1), ("medium", 0.2)]]
    print("first answer:", found)
    print([task.cancelled() for task in tasks])

asyncio.run(main())
