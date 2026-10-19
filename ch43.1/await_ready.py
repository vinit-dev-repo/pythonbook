# await_ready.py
import asyncio

async def ready():
    return 42

async def main():
    trace = []

    async def peer():
        trace.append("peer")

    peer_task = asyncio.create_task(peer())
    trace.append("before")
    value = await ready()
    trace.append(f"after: {value}")
    assert not peer_task.done()
    await peer_task
    assert trace == ["before", "after: 42", "peer"]
    print(trace)

if __name__ == "__main__":
    asyncio.run(main())
