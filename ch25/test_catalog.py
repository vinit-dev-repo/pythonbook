# test_catalog.py
import re
import pytest

from catalog import Catalog


def snapshot(catalog):
    return {
        key: (record["id"], record["quantity"])
        for key, record in catalog.records.items()
    }


def test_put_sequence():
    catalog = Catalog()
    original = {"id": "pen", "quantity": 2}
    catalog.put(original)
    assert snapshot(catalog) == {"pen": ("pen", 2)}
    assert catalog.records["pen"] is original

    before = snapshot(catalog)
    with pytest.raises(ValueError, match=re.escape("quantity must be nonnegative")) as error:
        catalog.put({"id": "pen", "quantity": -1})
    assert error.type is ValueError
    assert snapshot(catalog) == before
    assert catalog.records["pen"] is original

    replacement = {"id": "pen", "quantity": 5}
    assert replacement is not original
    catalog.put(replacement)
    assert snapshot(catalog) == {"pen": ("pen", 5)}
    assert catalog.records["pen"] is replacement
    assert original == {"id": "pen", "quantity": 2}
    assert before == {"pen": ("pen", 2)}


def test_zero_quantity_is_valid():
    catalog = Catalog()
    catalog.put({"id": "pen", "quantity": 0})
    assert snapshot(catalog) == {"pen": ("pen", 0)}


@pytest.mark.parametrize(
    "record, expected_error",
    [
        (None, TypeError),
        ({"id": "pen"}, ValueError),
        ({"id": 9, "quantity": -1}, TypeError),
        ({"id": "", "quantity": 2}, ValueError),
        ({"id": "pen", "quantity": True}, TypeError),
        ({"id": "pen", "quantity": 1.0}, TypeError),
    ],
)
def test_invalid_record_preserves_state(record, expected_error):
    catalog = Catalog()
    original = {"id": "book", "quantity": 3}
    catalog.put(original)
    before = snapshot(catalog)

    with pytest.raises(expected_error) as error:
        catalog.put(record)

    assert error.type is expected_error
    assert snapshot(catalog) == before
    assert catalog.records["book"] is original
