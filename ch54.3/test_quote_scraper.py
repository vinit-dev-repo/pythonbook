# test_quote_scraper.py
from pathlib import Path
import tempfile

import pandas as pd

from quote_scraper import COLUMNS, LayoutError, extract_quotes, write_quotes


EXPECTED = [
    {"text": '"Simplicity is the soul of efficiency."', "author": "Austin Freeman", "tags": ""},
    {"text": '"The world as we have created it..."', "author": "Albert Einstein", "tags": "change, deep-thoughts, world"},
]


def raises_layout(html, message, *, extractor=extract_quotes):
    try:
        extractor(html)
    except LayoutError as error:
        assert message in str(error), error
    except Exception as error:
        raise AssertionError(f"expected LayoutError, got {type(error).__name__}") from error
    else:
        raise AssertionError("LayoutError was required")


def run_checks():
    fixture = Path("quotes_sample.html").read_text(encoding="utf-8")
    assert extract_quotes(fixture) == EXPECTED
    duplicate = '<div class="quote"><span class="text">Again</span><small class="author">Writer</small><div class="tags"><a>x</a></div></div>'
    assert extract_quotes(duplicate + duplicate) == [
        {"text": "Again", "author": "Writer", "tags": "x"},
        {"text": "Again", "author": "Writer", "tags": "x"},
    ]
    assert extract_quotes('<div class="quote"><span class="text">A <b>nested</b> value</span><small class="author">Writer</small><div class="tags"><a>x</a><a>x</a></div></div>') == [{"text": "A nested value", "author": "Writer", "tags": "x, x"}]
    try:
        extract_quotes(b"not text")
    except TypeError:
        pass
    else:
        raise AssertionError("non-string input was accepted")
    raises_layout("", "expected at least one")
    raises_layout("<p>no cards</p>", "expected at least one")
    raises_layout('<div class="quote"><small class="author">Writer</small></div>', "card 1: missing text")
    raises_layout('<div class="quote"><span class="text">   </span><small class="author">Writer</small></div>', "card 1: missing text")
    raises_layout('<div class="quote"><span class="text">Text</span></div>', "card 1: missing author")
    raises_layout('<div class="quote"><span class="text">Text</span><small class="author">   </small></div>', "card 1: missing author")
    raises_layout('<div class="quote"><span class="text">One</span><small class="author">First</small></div><div class="quote"><span class="text">Two</span></div>', "card 2: missing author")
    with tempfile.TemporaryDirectory(prefix="quote_scraper_") as temporary:
        destination = Path(temporary) / "quotes.csv"
        destination.write_text("keep-this-file", encoding="utf-8")
        try:
            write_quotes('<div class="quote"><span class="text">Text</span></div>', destination)
        except LayoutError as error:
            assert "card 1: missing author" in str(error), error
        else:
            raise AssertionError("write_quotes accepted a bad card")
        assert destination.read_text(encoding="utf-8") == "keep-this-file"
        frame = write_quotes(fixture, destination)
        assert list(frame.columns) == COLUMNS
        assert frame.to_dict("records") == EXPECTED
        readback_frame = pd.read_csv(destination, keep_default_na=False)
        assert list(readback_frame.columns) == COLUMNS
        readback = readback_frame.to_dict("records")
        assert readback == EXPECTED
    print("quote scraper checks: ok")


if __name__ == "__main__":
    run_checks()
