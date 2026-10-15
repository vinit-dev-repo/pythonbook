# test_labels.py
from labels import to_label, from_label

def test_known_values():
    assert to_label("pen") == "item:pen"
    assert from_label("item:book") == "book"

def test_round_trip():
    assert from_label(to_label("pen")) == "pen"
