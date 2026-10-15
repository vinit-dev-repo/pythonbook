# cache_failure/check.py
import sys

try:
    import broken
except ValueError as error:
    print(error)
print("broken" in sys.modules)
print("dependency" in sys.modules)

sys.modules["blocked_demo"] = None
try:
    import blocked_demo
except ModuleNotFoundError:
    print("None blocks import")
finally:
    del sys.modules["blocked_demo"]
