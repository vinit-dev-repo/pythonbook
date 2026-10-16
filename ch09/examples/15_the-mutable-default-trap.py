def add_item(item, items=None):
    if items is None:
        items = []          # a fresh list when items is None
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
