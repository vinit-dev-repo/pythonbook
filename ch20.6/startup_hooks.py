# startup_hooks.py
from pathlib import Path
import os
import subprocess
import sys
import tempfile

with tempfile.TemporaryDirectory() as folder:
    root = Path(folder)
    startup = root / "welcome.py"
    startup.write_text("launch_note = 'ready'\n", encoding="utf-8")
    task = root / "task.py"
    task.write_text("print('task ran')\n", encoding="utf-8")
    environment = {key: value for key, value in os.environ.items()
                   if not key.upper().startswith("PYTHON")}
    environment["PYTHONSTARTUP"] = str(startup)
    query = "print('startup name:', 'launch_note' in globals())\n"
    cases = (("interactive", ["-i"]),
             ("after script", ["-i", str(task)]),
             ("ignored", ["-E", "-i"]))
    for label, arguments in cases:
        result = subprocess.run([sys.executable, "-S", *arguments],
                                input=query, cwd=root, env=environment,
                                capture_output=True, text=True, check=True)
        print(label + ":", " | ".join(result.stdout.splitlines()))
