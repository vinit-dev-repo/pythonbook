# source_file_namespace.py
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

total = 99
namespace = {"__name__": "scratch_exec"}
with TemporaryDirectory() as folder:
    path = Path(folder) / "rule.py"
    for value in (7, 11):
        source = (f"total = {value}\n"
                  "runs = globals().get('runs', 0) + 1\n")
        path.write_text(source, encoding="utf-8")
        code = compile(path.read_text(encoding="utf-8"), str(path), "exec")
        exec(code, namespace)
        print("file result:", namespace["total"], namespace["runs"])
print("caller total:", total)
print("registered module:", "scratch_exec" in sys.modules)
