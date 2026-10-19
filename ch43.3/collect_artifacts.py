# collect_artifacts.py
import asyncio
import json
import re
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
import aiohttp
from artifact_fixture import fixture

class MissingArtifact(Exception):
    pass

class DownloadError(Exception):
    pass

async def body(session, url, limit, expected_type):
    async with session.get(url, allow_redirects=False) as response:
        if response.status == 404:
            raise MissingArtifact(url)
        if response.status != 200:
            raise DownloadError(f"HTTP {response.status}")
        if response.content_type != expected_type:
            raise DownloadError("unexpected content type")
        result = bytearray()
        async for chunk in response.content.iter_chunked(1024):
            result.extend(chunk)
            if len(result) > limit:
                raise DownloadError("response exceeds limit")
        return bytes(result)

async def save_finished(path, data):
    write = asyncio.create_task(asyncio.to_thread(path.write_bytes, data))
    try:
        return await asyncio.shield(write)
    except asyncio.CancelledError as cancellation:
        # Join this short write before our owner removes the directory.
        try:
            await write
        except Exception as error:
            cancellation.add_note(f"write also failed: {error!r}")
        raise

async def collect(base, items, directory, limit=2, report=None):
    items = tuple(items)
    if type(limit) is not int or limit < 1:
        raise ValueError("limit must be a positive integer")
    if any(not isinstance(item, str) or
           re.fullmatch(r"[a-z]{1,16}", item) is None for item in items):
        raise ValueError("invalid artifact identifier")
    if len(set(items)) != len(items):
        raise ValueError("artifact identifiers must be unique")
    directory = Path(directory)
    permits = asyncio.Semaphore(limit)

    async def one(session, item):
        stage = "metadata"
        try:
            async with permits:
                async with asyncio.timeout(2):
                    raw = await body(session, f"{base}/metadata/{item}",
                                     2048, "application/json")
                    metadata = json.loads(raw)
                    if (not isinstance(metadata, dict) or
                        type(metadata.get("size")) is not int or
                        not 0 <= metadata["size"] <= 4096):
                        raise DownloadError("invalid metadata size")
                    stage = "payload"
                    data = await body(session, f"{base}/payload/{item}",
                                      4096, "application/octet-stream")
                    if len(data) != metadata["size"]:
                        raise DownloadError("payload size mismatch")
                stage = "write"
                count = await save_finished(directory / f"{item}.bin", data)
                if count != len(data):
                    raise OSError("incomplete write")
            return "saved", ""
        except MissingArtifact:
            return "missing", stage
        except (DownloadError, aiohttp.ClientError, TimeoutError,
                OSError, ValueError) as error:
            return "failed", f"{stage}: {type(error).__name__}: {error}"

    outcomes = {}
    timeout = aiohttp.ClientTimeout(total=2)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with asyncio.TaskGroup() as group:
            owners = {group.create_task(one(session, item)): item
                      for item in items}
            async for task in asyncio.as_completed(owners):
                item = owners[task]
                outcomes[item] = task.result()
                if report is not None:
                    report(len(outcomes), len(items), item, *outcomes[item])
    return outcomes

async def main():
    progress = []
    def record(done, total, item, status, detail):
        progress.append((done, total, item, status))

    with TemporaryDirectory() as folder:
        async with fixture() as base:
            results = await collect(base,
                ["card", "missing", "label", "broken", "malformed"],
                folder, report=record)
        print(sorted((item, status) for item, (status, _) in results.items()))
        print(sorted(Counter(status for status, _ in results.values()).items()))
        print([row[0] for row in progress])
        print(sorted(path.name for path in Path(folder).iterdir()))

if __name__ == "__main__":
    asyncio.run(main())
