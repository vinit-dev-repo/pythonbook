import time
from concurrent.futures import ThreadPoolExecutor
import urllib.request

urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net",
]

def fetch_length(url):
    with urllib.request.urlopen(url, timeout=5) as response:
        return url, len(response.read())

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:
    for url, length in pool.map(fetch_length, urls):
        print(f"{url}: {length} bytes")
print(f"Took {time.perf_counter() - start:.2f}s")
