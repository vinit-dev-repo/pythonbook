# sourceless_cache.py
import py_compile
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

probe = """try:
    import parcel_cache
    print(parcel_cache.VALUE)
except ImportError as error:
    print(type(error).__name__)
"""
with TemporaryDirectory() as folder:
    root = Path(folder)
    source = root / "parcel_cache.py"
    source.write_text("VALUE = 27\n", encoding="utf-8")
    cached = Path(py_compile.compile(str(source), doraise=True))
    source.unlink()

    def check(label):
        result = subprocess.run(
            [sys.executable, "-E", "-c", probe], cwd=root,
            capture_output=True, text=True, check=True,
        )
        print(label, result.stdout.strip())

    check("orphan cache:")
    adjacent = root / "parcel_cache.pyc"
    adjacent.write_bytes(cached.read_bytes())
    check("adjacent bytecode:")
    data = adjacent.read_bytes()
    adjacent.write_bytes(b"BAD!" + data[4:])
    check("wrong magic:")
