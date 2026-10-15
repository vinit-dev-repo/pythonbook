# catalog.py
class Catalog:
    def __init__(self):
        self.records = {}

    def put(self, record):
        if type(record) is not dict:
            raise TypeError("record must be a plain dictionary")
        if set(record) != {"id", "quantity"}:
            raise ValueError("record must have exactly id and quantity")

        item_id = record["id"]
        quantity = record["quantity"]
        if type(item_id) is not str:
            raise TypeError("id must be a built-in string")
        if not item_id:
            raise ValueError("id must not be empty")
        if type(quantity) is not int:
            raise TypeError("quantity must be a built-in integer")
        if quantity < 0:
            raise ValueError("quantity must be nonnegative")

        self.records[item_id] = record
