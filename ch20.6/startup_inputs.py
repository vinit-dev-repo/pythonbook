# startup_inputs.py
from pathlib import Path
import os
import subprocess
import sys
import tempfile

with tempfile.TemporaryDirectory() as folder:
    root = Path(folder)
    extra = root / "extras"
    extra.mkdir()
    (extra / "launch_probe.py").write_text("value = 29\n", encoding="utf-8")
    environment = {key: value for key, value in os.environ.items()
                   if not key.upper().startswith("PYTHON")}
    environment["PYTHONPATH"] = str(extra)
    query = ("import importlib.util; "
             "print(importlib.util.find_spec('launch_probe') is not None)")
    for label, flags in (("ordinary", []), ("ignore environment", ["-E"]),
                         ("isolated", ["-I"]), ("skip site", ["-S"])):
        result = subprocess.run([sys.executable, *flags, "-c", query],
                                cwd=root, env=environment, capture_output=True,
                                text=True, check=True)
        print(label + ":", result.stdout.strip())
