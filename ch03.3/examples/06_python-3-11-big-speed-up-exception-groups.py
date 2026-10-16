import asyncio

async def good():
    await asyncio.sleep(0.1)
    return "ok"

async def bad():
    raise ValueError("this task failed")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(good())
            tg.create_task(bad())
    except* ValueError as group:
        print("TaskGroup raised:", type(group).__name__)
        print("inner errors    :", [str(e) for e in group.exceptions])

asyncio.run(main())
