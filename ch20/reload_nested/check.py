# reload_nested/check.py
from pathlib import Path
import importlib
import importlib.util
import parent

print(parent.read())
source = Path(parent.child.__file__)
source.write_text('value = "new"\n', encoding="utf-8")
cached = Path(importlib.util.cache_from_source(str(source)))
if cached.exists():
    cached.unlink()
importlib.invalidate_caches()
importlib.reload(parent)
print(parent.read())
importlib.reload(parent.child)
print(parent.read())
