# lazy_demo/compat.py
__lazy_modules__ = ["heavy"]
import sys
import heavy

print("loaded:", "heavy" in sys.modules)
print(heavy.value)
