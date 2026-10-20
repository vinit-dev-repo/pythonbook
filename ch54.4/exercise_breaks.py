# exercise_breaks.py
import requests
from bs4 import BeautifulSoup

from fetch_live_quotes import fetch_live_html
from quote_scraper import LayoutError, extract_quotes

# 1
changed = '<article class="quotation"><p class="words">Hi</p><span class="byline">Ada</span></article>'
try:
    extract_quotes(changed)
except LayoutError as error:
    print("LayoutError:", error)


# 2
class FakeResponse:
    def __init__(self, status):
        self.status = status
        self.text_reads = 0
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.closed = True

    def raise_for_status(self):
        if self.status >= 400:
            raise requests.HTTPError(f"{self.status} Client Error")

    @property
    def text(self):
        self.text_reads += 1
        return "<html></html>"


response = FakeResponse(404)
try:
    fetch_live_html(get=lambda url, **kwargs: response)
except requests.HTTPError as error:
    print("HTTPError:", error)
print("text reads:", response.text_reads, "| closed:", response.closed)

# 3
page = '<html><body><div id="app"></div></body></html>'
print(len(BeautifulSoup(page, "html.parser").select("div.quote")))
