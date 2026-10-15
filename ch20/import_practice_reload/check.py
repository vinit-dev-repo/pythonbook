# import_practice_reload/check.py
from pathlib import Path
import importlib
import importlib.util
import library
from library import label_pair as saved

source = Path(library.__file__)
source.write_text('def label_pair(first, second):\n    return first + " + " + second\n', encoding="utf-8")
cached = Path(importlib.util.cache_from_source(str(source)))
if cached.exists():
    cached.unlink()
import library
print("repeat:", library.label_pair("red", "blue"))
importlib.invalidate_caches()
importlib.reload(library)
print("saved:", saved("red", "blue"))
print("current:", library.label_pair("red", "blue"))
print(saved is library.label_pair)
