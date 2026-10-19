import asyncio


# 1
async def delayed(value, delay):
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    loop.call_later(delay, future.set_result, value)
    return await future


async def q1():
    first, second = await asyncio.gather(delayed("a", 0.02), delayed("b", 0.01))
    print("futures:", first, second)


# 2
async def q2():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    def deliver(value):
        if not future.done():
            future.set_result(value)

    deliver(1)
    deliver(2)
    print("guarded result:", await future)
    try:
        future.set_result(3)
    except asyncio.InvalidStateError:
        print("unguarded second set_result: InvalidStateError")


# 3
async def handle(reader, writer):
    while line := await reader.readline():
        writer.write(line.upper())
        await writer.drain()
    writer.close()
    await writer.wait_closed()


async def q3():
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    for word in ("alpha", "beta"):
        writer.write(word.encode() + b"\n")
        await writer.drain()
        print("reply:", (await reader.readline()).decode().strip())
    writer.close()
    await writer.wait_closed()
    server.close()
    await server.wait_closed()


async def main():
    await q1()
    await q2()
    await q3()


asyncio.run(main())
