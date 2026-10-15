# namespace_growth/check.py
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
sys.path.insert(0, str(root / "dir1"))
import tools
saved = tools
print("initial portions:", len(list(tools.__path__)))
sys.path.insert(0, str(root / "dir2"))
import tools.alpha
import tools.shared.first
import tools.shared.second
import tools.regular
print("same object:", tools is saved)
print("later portions:", len(list(tools.__path__)))
print(tools.alpha.VALUE)
print("shared portions:", len(list(tools.shared.__path__)))
for item in (tools.shared, tools.regular, tools.alpha):
    print(item.__name__, item.__spec__.origin is None, hasattr(item, "__path__"))
