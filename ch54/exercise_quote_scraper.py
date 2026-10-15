# exercise_quote_scraper.py
from pathlib import Path

from bs4 import BeautifulSoup

from quote_scraper import LayoutError, extract_quotes


def required(card, selector, field, card_number):
    element = card.select_one(selector)
    value = "" if element is None else element.get_text(" ", strip=True)
    if not value:
        raise LayoutError(f"card {card_number}: missing {field}")
    return value


def extract_changed_quotes(html):
    if not isinstance(html, str):
        raise TypeError("html must be a str")
    cards = BeautifulSoup(html, "html.parser").select("article.quotation")
    if not cards:
        raise LayoutError("expected at least one article.quotation card")
    records = []
    for card_number, card in enumerate(cards, start=1):
        records.append({
            "text": required(card, "p.words", "text", card_number),
            "author": required(card, "span.byline", "author", card_number),
            "tags": ", ".join(tag.get_text(" ", strip=True) for tag in card.select("ul.categories li")),
        })
    return records


def run_exercise():
    html = Path("quotes_changed.html").read_text(encoding="utf-8")
    try:
        extract_quotes(html)
    except LayoutError:
        pass
    else:
        raise AssertionError("the old parser accepted the changed layout")
    expected = [
        {"text": "Check the page structure.", "author": "Example Writer", "tags": "layout, tests"},
        {"text": "Keep the input visible.", "author": "Second Writer", "tags": ""},
    ]
    assert extract_changed_quotes(html) == expected
    missing_byline = '<article class="quotation"><p class="words">Rejected</p></article>'
    try:
        extract_changed_quotes(missing_byline)
    except LayoutError as error:
        assert "card 1: missing author" in str(error)
    else:
        raise AssertionError("missing byline was accepted")
    print("changed layout: ok")


if __name__ == "__main__":
    run_exercise()
