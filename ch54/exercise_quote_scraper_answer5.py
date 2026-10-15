# exercise_quote_scraper_answer5.py
from pathlib import Path

from bs4 import BeautifulSoup


def run_answer():
    html = Path("quotes_sample.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for quote_card in soup.select("div.quote"):
        author = quote_card.select_one("small.author")
        if author is not None and author.get_text(" ", strip=True) == "Albert Einstein":
            print([tag.get_text(" ", strip=True) for tag in quote_card.select("div.tags a")])
            break
    else:
        raise LookupError("Albert Einstein quote card was not found")


if __name__ == "__main__":
    run_answer()
