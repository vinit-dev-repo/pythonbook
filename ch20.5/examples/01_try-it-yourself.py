# 1
# dir1/tools/alpha.py
VALUE = "alpha"

# dir2/tools/beta.py
VALUE = "beta"

# check.py  (no __init__.py in either tools folder)
import sys
sys.path[:0] = ["dir1", "dir2"]
import tools.alpha
import tools.beta
print(tools.alpha.VALUE, tools.beta.VALUE)     # alpha beta
print(len(list(tools.__path__)))               # 2

# 2
from pathlib import Path
from zipfile import ZipFile
import sys

with ZipFile("modules.zip", "w") as bundle:
    bundle.write("archive_module.py", "archive_module.py")
sys.path.insert(0, str(Path("modules.zip").resolve()))
import archive_module
print("modules.zip" in archive_module.__file__)   # True
