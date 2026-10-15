# relative_targets/red/check.py
from . import helper
print(helper.VALUE)
try:
    from . import missing
except ImportError:
    print("relative target is absent")
