import asyncio

async def callback_value(value):
    loop = asyncio.get_running_loop()
    ready = loop.create_future()

    def delivered():
        if not ready.done():
            ready.set_result(value)

    delivery = loop.call_soon(delivered)
    try:
        return await ready
    finally:
        delivery.cancel()

async def main():
    loop = asyncio.get_running_loop()
    waiting = loop.create_future()
    try:
        waiting.result()
    except asyncio.InvalidStateError:
        print("pending is not a result")
    waiting.cancel()
    first = await callback_value(7)
    second = await callback_value(first * 3)
    print(first, second)

asyncio.run(main())
