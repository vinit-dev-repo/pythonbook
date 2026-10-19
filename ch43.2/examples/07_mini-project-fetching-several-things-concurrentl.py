import asyncio
import time
import urllib.request

def fetch_page(url):
    """A normal, BLOCKING function -- exactly the kind to_thread is for."""
    with urllib.request.urlopen(url, timeout=5) as response:
        return len(response.read())

async def fetch_all(urls):
    tasks = [asyncio.to_thread(fetch_page, url) for url in urls]
    return await asyncio.gather(*tasks, return_exceptions=True)

async def main():
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.example.com",
    ]
    start = time.perf_counter()
    results = await fetch_all(urls)
    for url, result in zip(urls, results):
        if isinstance(result, Exception):
            print(f"{url}: FAILED ({result})")
        else:
            print(f"{url}: {result} bytes")
    print(f"total time: {time.perf_counter() - start:.1f}s")

asyncio.run(main())
