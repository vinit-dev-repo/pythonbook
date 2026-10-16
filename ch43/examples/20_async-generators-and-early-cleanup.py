import asyncio
from contextlib import aclosing, asynccontextmanager

@asynccontextmanager
async def batch_session(log):
    log.append("session open")
    try:
        yield {"batch": 12}
    finally:
        await asyncio.sleep(0)
        log.append("session closed")

async def batch_rows(log):
    try:
        for number in range(3):
            await asyncio.sleep(0)
            yield number
    finally:
        await asyncio.sleep(0)
        log.append("rows closed")

async def early_exit():
    log = []
    async with batch_session(log) as session:
        async with aclosing(batch_rows(log)) as rows:
            async for number in rows:
                log.append((session["batch"], number))
                break
        log.append("after rows")
    print(log)

asyncio.run(early_exit())
