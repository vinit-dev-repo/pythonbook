# utf16_streams.py
import codecs
from io import BytesIO, TextIOWrapper

text = "A\U0001f680"
big_endian = text.encode("utf-16-be")
print(len(text), len(big_endian), len(text.encode("utf-32-be")))
print(big_endian.hex())
marked = codecs.BOM_UTF16_BE + big_endian
with TextIOWrapper(BytesIO(marked), encoding="utf-16") as stream:
    print(stream.read() == text)
print(marked.decode("utf-16-be").startswith("\ufeff"))
try:
    with TextIOWrapper(BytesIO(big_endian), encoding="utf-16") as stream:
        stream.read()
except UnicodeError:
    print("Stream requires a BOM")
with TextIOWrapper(BytesIO(big_endian), encoding="utf-16-be") as stream:
    print(stream.read() == text)
