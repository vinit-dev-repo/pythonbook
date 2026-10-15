# lazy_demo/check.py
import sys

lazy import heavy

print("start; loaded:", "heavy" in sys.modules)
print("binding:", type(globals()["heavy"]).__name__)
print("value:", heavy.value)
print("loaded:", "heavy" in sys.modules)
print("binding:", type(globals()["heavy"]).__name__)
