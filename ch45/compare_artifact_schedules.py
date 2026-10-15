# compare_artifact_schedules.py
import asyncio
import json
import platform
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, build_opener
import aiohttp
from artifact_fixture import ARTIFACTS, fixture
from collect_artifacts import collect, DownloadError, MissingArtifact

ITEMS = ("card", "missing", "label", "broken", "malformed")

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        return None

def blocking_one(base, item, directory):
    opener = build_opener(NoRedirect())
    def read(part, maximum, content_type):
        try:
            with opener.open(f"{base}/{part}/{item}", timeout=2) as response:
                if response.status != 200:
                    raise DownloadError(f"HTTP {response.status}")
                if response.headers.get_content_type() != content_type:
                    raise DownloadError("unexpected content type")
                data = response.read(maximum + 1)
                if len(data) > maximum:
                    raise DownloadError("response exceeds limit")
                return data
        except HTTPError as error:
            error.close()
            if error.code == 404:
                raise MissingArtifact(item) from error
            raise DownloadError(f"HTTP {error.code}") from error
    try:
        metadata = json.loads(read("metadata", 2048, "application/json"))
        if (not isinstance(metadata, dict) or
            type(metadata.get("size")) is not int or
            not 0 <= metadata["size"] <= 4096):
            raise DownloadError("invalid metadata size")
        data = read("payload", 4096, "application/octet-stream")
        if len(data) != metadata["size"]:
            raise DownloadError("payload size mismatch")
        if (directory / f"{item}.bin").write_bytes(data) != len(data):
            raise OSError("incomplete write")
        return "saved"
    except MissingArtifact:
        return "missing"
    except (DownloadError, URLError, OSError, ValueError):
        return "failed"

def blocking_batch(base, directory, threaded):
    if not threaded:
        return {item: blocking_one(base, item, directory) for item in ITEMS}
    with ThreadPoolExecutor(max_workers=2) as pool:
        owners = {pool.submit(blocking_one, base, item, directory): item
                  for item in ITEMS}
        results = {}
        for future in as_completed(owners):
            results[owners[future]] = future.result()
        return results

async def main():
    print(platform.python_implementation(), platform.python_version(),
          "aiohttp", aiohttp.__version__, "jobs", len(ITEMS), "limit", 2)
    expected = dict(card="saved", label="saved", missing="missing",
                    broken="failed", malformed="failed")
    with TemporaryDirectory() as root:
        async with fixture() as base:
            for mode in ("serial", "threads", "async"):
                directory = Path(root) / mode
                directory.mkdir()
                start = time.perf_counter()
                if mode == "async":
                    outcomes = await collect(base, ITEMS, directory, limit=2)
                    results = {key: value[0] for key, value in outcomes.items()}
                else:
                    results = await asyncio.to_thread(
                        blocking_batch, base, directory, mode == "threads")
                elapsed = time.perf_counter() - start
                assert results == expected
                assert {p.stem: p.read_bytes() for p in directory.iterdir()} == ARTIFACTS
                print(mode, "outcomes and bytes verified", f"{elapsed:.3f}s")

if __name__ == "__main__":
    asyncio.run(main())
