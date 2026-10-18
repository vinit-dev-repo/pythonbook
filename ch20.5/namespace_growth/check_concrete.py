# namespace_growth/check_concrete.py
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
sys.path[:0] = [str(root / "dir1"), str(root / "dir2"), str(root / "concrete")]
import tools
print(tools.KIND)
print(hasattr(tools, "__path__"))
try:
    import tools.alpha
except ModuleNotFoundError:
    print("selected tools is not a package")
