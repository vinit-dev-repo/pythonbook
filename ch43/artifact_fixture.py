# artifact_fixture.py
import asyncio
from contextlib import asynccontextmanager
from aiohttp import web

ARTIFACTS = {"card": b"fold along the dotted line\n",
             "label": b"label the finished model\n"}

def make_app():
    async def metadata(request):
        item = request.match_info["item"]
        if item == "broken":
            raise web.HTTPServiceUnavailable(text="fixture maintenance")
        if item == "malformed":
            return web.json_response({"size": "many"})
        if item not in ARTIFACTS:
            raise web.HTTPNotFound()
        await asyncio.sleep(0.02)
        return web.json_response({"size": len(ARTIFACTS[item])})

    async def payload(request):
        item = request.match_info["item"]
        if item not in ARTIFACTS:
            raise web.HTTPNotFound()
        await asyncio.sleep(0.02)
        return web.Response(body=ARTIFACTS[item],
                            content_type="application/octet-stream")

    app = web.Application()
    app.add_routes([web.get("/metadata/{item}", metadata),
                    web.get("/payload/{item}", payload)])
    return app

@asynccontextmanager
async def fixture():
    runner = web.AppRunner(make_app(), access_log=None)
    await runner.setup()
    try:
        site = web.TCPSite(runner, "127.0.0.1", 0)
        await site.start()
        port = runner.addresses[0][1]
        yield f"http://127.0.0.1:{port}"
    finally:
        await runner.cleanup()
