import asyncio
import time

async def bad_task(name):
    print(f"{name}: starting")
    time.sleep(2)          # BLOCKING call inside async code -- freezes EVERYTHING
    print(f"{name}: done")

async def main():
    await asyncio.gather(bad_task("A"), bad_task("B"))
