# reload_demo/check.py
import importlib
from pathlib import Path
import settings
from settings import VALUE

original = settings
Path(settings.__file__).write_text('VALUE = "second version"\n', encoding="utf-8")
cached = settings.__spec__.cached
if cached:
    Path(cached).unlink(missing_ok=True)
importlib.invalidate_caches()
importlib.reload(settings)

print(settings is original)
print(settings.VALUE)
print(VALUE)
print(settings.REMOVED)
