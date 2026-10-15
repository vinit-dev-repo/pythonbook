# namespace_demo/check_regular.py
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
sys.path[:0] = [str(root / "dir1"), str(root / "dir2"), str(root / "regular")]
import tools
print(tools.KIND)
try:
    import tools.alpha
except ModuleNotFoundError:
    print("namespace alpha is not in this regular package")
