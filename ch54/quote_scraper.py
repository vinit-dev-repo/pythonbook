# quote_scraper.py
from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup


COLUMNS = ["text", "author", "tags"]


class LayoutError(ValueError):
    """The fixed quote-card layout did not supply a required value."""


def _required_text(card, selector, field, card_number):
    element = card.select_one(selector)
    value = "" if element is None else element.get_text(" ", strip=True)
    if not value:
        raise LayoutError(f"card {card_number}: missing {field}")
    return value


def extract_quotes(html):
    if not isinstance(html, str):
        raise TypeError("html must be a str")

    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select("div.quote")
    if not cards:
        raise LayoutError("expected at least one div.quote card")

    records = []
    for card_number, card in enumerate(cards, start=1):
        text = _required_text(card, "span.text", "text", card_number)
        author = _required_text(card, "small.author", "author", card_number)
        tags = ", ".join(tag.get_text(" ", strip=True) for tag in card.select("div.tags a"))
        records.append({"text": text, "author": author, "tags": tags})
    return records


def write_quotes(html, destination):
    records = extract_quotes(html)  # validate the whole candidate before opening the CSV
    frame = pd.DataFrame(records, columns=COLUMNS)
    frame.to_csv(destination, index=False, encoding="utf-8")
    return frame


if __name__ == "__main__":
    fixture = Path("quotes_sample.html").read_text(encoding="utf-8")
    frame = write_quotes(fixture, "quotes.csv")
    print(f"{len(frame)} quotes written to quotes.csv")
