# shared_binding/check.py
import store
from store import items
items.append("shared")
print(items is store.items, store.items)
items = ["caller"]
print(items, store.items)
old = store.items
store.items = ["module"]
print(old, store.items, items)
