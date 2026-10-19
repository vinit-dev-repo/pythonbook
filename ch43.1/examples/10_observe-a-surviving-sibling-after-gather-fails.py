import asyncio

async def gather_failure():
    ready = asyncio.Event()
    release = asyncio.Event()
    trace = []

    async def sibling():
        ready.set()
        try:
            await release.wait()
            trace.append("sibling finished")
            return 7
        finally:
            trace.append("sibling cleanup")

    async def fail():
        await ready.wait()
        raise ValueError("bad input")

    survivor = asyncio.create_task(sibling())
    failed = asyncio.create_task(fail())
    try:
        await asyncio.gather(survivor, failed)
    except ValueError:
        trace.append("caller caught")
        print("sibling pending:", not survivor.done())
    finally:
        release.set()
        await survivor
    print(trace)
    assert failed.done() and not survivor.cancelled()

asyncio.run(gather_failure())
