# async_counter.py
import asyncio

async def lost_update(start=100, amount=1):
    balance = start
    arrivals = 0
    both_read = asyncio.Event()

    async def add():
        nonlocal balance, arrivals
        current = balance
        arrivals += 1
        if arrivals == 2:
            both_read.set()
        await both_read.wait()
        balance = current + amount

    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(add()) for _ in range(2)]
    assert all(task.done() for task in tasks)
    return balance

async def protected_update(start=100, amount=1):
    balance = start
    lock = asyncio.Lock()

    async def add():
        nonlocal balance
        async with lock:
            current = balance
            await asyncio.sleep(0)
            balance = current + amount

    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(add()) for _ in range(2)]
    assert all(task.done() for task in tasks)
    return balance

async def main():
    broken = await lost_update()
    fixed = await protected_update()
    assert broken == 101
    assert fixed == 102
    print("intended:", 102)
    print("controlled lost update:", broken)
    print("protected update:", fixed)

if __name__ == "__main__":
    asyncio.run(main())
