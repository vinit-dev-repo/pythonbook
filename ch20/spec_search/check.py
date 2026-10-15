# spec_search/check.py
from pathlib import Path
import importlib
import importlib.util
import sys

name = "plugin"
print("before:", importlib.util.find_spec(name) is None)
root = Path(__file__).resolve().parent / "external"
sys.path.insert(0, str(root))
spec = importlib.util.find_spec(name)
print("found:", spec.name, spec.origin.endswith("plugin.py"))
print("executed:", name in sys.modules)
print("finder hooks:", bool(sys.meta_path))
importlib.import_module(name)
print("caller bound:", name in globals())
print("cached:", name in sys.modules)
module = importlib.import_module(name)
print(module.value)
