# package_trace/check_spec.py
import importlib.util
import sys

spec = importlib.util.find_spec("myapp.utils.numbers")
print("found:", spec.name)
print("target executed:", "myapp.utils.numbers" in sys.modules)
print("parents cached:", "myapp" in sys.modules, "myapp.utils" in sys.modules)
