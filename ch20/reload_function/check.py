# reload_function/check.py
from pathlib import Path
import importlib
import importlib.util
import message
from message import render as saved

print(saved())
source = Path(message.__file__)
source.write_text('prefix = "new"\n\ndef render():\n    return prefix + " body-v2"\n', encoding="utf-8")
cached = Path(importlib.util.cache_from_source(str(source)))
if cached.exists():
    cached.unlink()
importlib.invalidate_caches()
importlib.reload(message)
print(saved is message.render)
print(saved())
print(message.render())
