# test_weak_replacement.py
from catalog import Catalog

def test_shared_record_changes():
    catalog = Catalog()
    original = {"id": "pen", "quantity": 2}
    catalog.put(original)
    before = (original["id"], original["quantity"])

    original["quantity"] = 5
    catalog.put(original)

    stored = catalog.records["pen"]
    assert (stored["id"], stored["quantity"]) != before
    assert stored["quantity"] == 5
