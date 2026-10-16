import asyncio
import time

def blocking_work(name):
    time.sleep(2)
    return f"{name} finished"

async def good_task(name):
    print(f"{name}: starting")
    return await asyncio.to_thread(blocking_work, name)     # runs on a real thread

async def main():
    results = await asyncio.gather(good_task("A"), good_task("B"))
    for line in results:            # gather returns results in ARGUMENT order
        print(line)
