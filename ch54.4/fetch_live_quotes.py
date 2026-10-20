# fetch_live_quotes.py
import requests

from quote_scraper import write_quotes


URL = "https://quotes.toscrape.com/"
HEADERS = {"User-Agent": "python-tutorial-scraper/1.0 (learning project)"}


def fetch_live_html(*, get=requests.get):
    response = get(URL, headers=HEADERS, timeout=(3, 10))
    with response:
        response.raise_for_status()  # inspect the status before reading the body
        return response.text


if __name__ == "__main__":
    write_quotes(fetch_live_html(), "quotes.csv")
