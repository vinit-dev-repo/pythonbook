import asyncio

async def fetch(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done")
    return name

async def main():
    async with asyncio.TaskGroup() as tg:
        task_a = tg.create_task(fetch("A", 1))
        task_b = tg.create_task(fetch("B", 2))
    # by the time we get here, BOTH tasks are guaranteed finished
    print(task_a.result(), task_b.result())

asyncio.run(main())
