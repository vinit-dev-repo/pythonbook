# namespace_demo/check.py
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
sys.path[:0] = [str(root / "dir1"), str(root / "dir2")]
import tools.alpha
import tools.beta
print(tools.alpha.VALUE, tools.beta.VALUE)
print(len(list(tools.__path__)))
