# caller_binding/check.py
import sys
import item
saved = item
del item
print("item" in globals(), "item" in sys.modules)
import item
print(item is saved)
