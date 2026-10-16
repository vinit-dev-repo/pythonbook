import os
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "café.txt"
    path.write_text("hello", encoding="utf-8")

    text_names = os.listdir(folder)
    byte_names = os.listdir(os.fsencode(folder))

    print(type(text_names[0]).__name__)
    print(type(byte_names[0]).__name__)
    print(os.fsdecode(byte_names[0]) == text_names[0])
