# test_report.py
# Final regressions
from report import category_total, summarize_indexed, summarize_naive


def test_no_rows_has_a_zero_total():
    assert category_total([], "books") == 0


def test_one_matching_row_is_its_quantity():
    assert category_total([{"category": "books", "quantity": 2}], "books") == 2


def test_separated_matching_rows_are_added():
    rows = [
        {"category": "books", "quantity": 2},
        {"category": "pens", "quantity": 7},
        {"category": "books", "quantity": 3},
    ]
    assert category_total(rows, "books") == 5


def test_missing_category_has_a_zero_total():
    assert category_total([{"category": "books", "quantity": 2}], "games") == 0


def test_summaries_agree_for_missing_and_unrequested_categories():
    rows = [
        {"category": "books", "quantity": 2},
        {"category": "pens", "quantity": 7},
        {"category": "books", "quantity": 3},
        {"category": "stickers", "quantity": 9},
    ]
    categories = ["books", "pens", "games"]
    expected = {"books": 5, "pens": 7, "games": 0}
    assert summarize_naive(rows, categories) == expected
    assert summarize_indexed(rows, categories) == expected
