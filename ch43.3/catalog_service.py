# catalog_service.py
import asyncio
import json
from contextlib import asynccontextmanager, suppress
import aiohttp
from aiohttp import web

CATALOG = ("blue paper", "copper wire", "graph paper",
           "paper clips", "wooden dowel")

def search_page(query, page=0):
    if not isinstance(query, str) or not 1 <= len(query.strip()) <= 40:
        raise ValueError("query must contain 1 to 40 characters")
    if type(page) is not int or not 0 <= page <= 1000:
        raise ValueError("page must be an integer from 0 to 1000")
    term = query.strip().casefold()
    matches = [name for name in CATALOG if term in name.casefold()]
    start = page * 2
    return {"items": matches[start:start + 2],
            "next": page + 1 if start + 2 < len(matches) else None}

@asynccontextmanager
async def catalog_services():
    clients = set()
    async def handle(reader, writer):
        clients.add(asyncio.current_task())
        try:
            while True:
                try:
                    raw = await asyncio.wait_for(reader.readline(), 5)
                except (ValueError, TimeoutError):
                    break
                if not raw:
                    break
                try:
                    if not raw.endswith(b"\n"):
                        raise ValueError("unfinished request line")
                    request = json.loads(raw.decode("utf8"))
                    if not isinstance(request, dict):
                        raise ValueError("request must be an object")
                    result = search_page(request.get("q"),
                                         request.get("page", 0))
                except (UnicodeError, ValueError) as error:
                    result = {"error": str(error)}
                writer.write((json.dumps(result) + "\n").encode("utf8"))
                await writer.drain()
                await asyncio.sleep(0)
        except ConnectionError:
            pass
        finally:
            writer.close()
            with suppress(ConnectionError):
                await writer.wait_closed()
            clients.discard(asyncio.current_task())

    async def http_search(request):
        try:
            page = int(request.query.get("page", "0"))
            result = search_page(request.query.get("q"), page)
        except ValueError as error:
            return web.json_response({"error": str(error)}, status=400)
        return web.json_response(result)

    app = web.Application()
    app.add_routes([web.get("/search", http_search)])
    runner = web.AppRunner(app, access_log=None)
    await runner.setup()
    server = None
    try:
        server = await asyncio.start_server(handle, "127.0.0.1", 0,
                                            limit=1024)
        site = web.TCPSite(runner, "127.0.0.1", 0)
        await site.start()
        yield (server.sockets[0].getsockname()[1],
               f"http://127.0.0.1:{runner.addresses[0][1]}")
    finally:
        if server is not None:
            server.close()
            server.close_clients()
            await server.wait_closed()
            if clients:
                await asyncio.gather(*tuple(clients), return_exceptions=True)
        await runner.cleanup()

async def main():
    async with catalog_services() as (port, base):
        reader, writer = await asyncio.open_connection("127.0.0.1", port)
        try:
            for page in (0, 1):
                request = json.dumps({"q": "paper", "page": page})
                writer.write((request + "\n").encode("utf8"))
                await writer.drain()
                print("TCP", json.loads(await reader.readline()))
        finally:
            writer.close()
            await writer.wait_closed()
        async with aiohttp.ClientSession() as session:
            async with session.get(base + "/search",
                                   params={"q": "paper", "page": 0}) as response:
                response.raise_for_status()
                print("HTTP", await response.json())

if __name__ == "__main__":
    asyncio.run(main())
