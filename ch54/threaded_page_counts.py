# threaded_page_counts.py
"""Count parsed text in a finite batch of trusted UTF-8 HTML pages."""
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup


def count_page(url):
    with requests.get(url, timeout=(2, 3), allow_redirects=False) as response:
        if response.status_code != 200:
            raise ValueError(f"HTTP {response.status_code}")
        media_type = response.headers.get("Content-Type", "").split(";", 1)[0]
        if media_type.strip().lower() != "text/html":
            raise ValueError("expected HTML")
        html = response.content.decode("utf-8")
    text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)
    return len(text)


def collect_counts(urls, *, workers=2):
    if type(workers) is not int or workers < 1:
        raise ValueError("workers must be a positive integer")
    urls = list(urls)
    results = [None] * len(urls)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        positions = {pool.submit(count_page, url): index
                     for index, url in enumerate(urls)}
        for future in as_completed(positions):
            index = positions[future]
            try:
                results[index] = (urls[index], future.result(), None)
            except (requests.RequestException, ValueError) as error:
                results[index] = (urls[index], None, str(error))
    return results


if __name__ == "__main__":
    import sys
    for url, count, error in collect_counts(sys.argv[1:]):
        print(url, f"text characters: {count}" if error is None else f"failed: {error}")
