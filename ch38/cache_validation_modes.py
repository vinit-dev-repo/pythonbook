# cache_validation_modes.py
import os
import py_compile
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

for mode in (py_compile.PycInvalidationMode.TIMESTAMP,
             py_compile.PycInvalidationMode.CHECKED_HASH):
    with TemporaryDirectory() as folder:
        root = Path(folder)
        source = root / "parcel_revision.py"
        source.write_text("VALUE = 11\n", encoding="utf-8")
        stamp = source.stat()
        py_compile.compile(str(source), doraise=True, invalidation_mode=mode)
        source.write_text("VALUE = 22\n", encoding="utf-8")
        os.utime(source, ns=(stamp.st_atime_ns, stamp.st_mtime_ns))
        result = subprocess.run(
            [sys.executable, "-E", "-c",
             "import parcel_revision; print(parcel_revision.VALUE)"],
            cwd=root, capture_output=True, text=True, check=True,
        )
        print(mode.name, result.stdout.strip())
