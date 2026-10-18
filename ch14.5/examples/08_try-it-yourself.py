import struct
import unicodedata

# 1
data = bytearray(b"hello world")
chunk = memoryview(data)[0:5]
chunk[1] = ord("A")
print(data)                           # bytearray(b'hAllo world')

# 2
layout = ">2sBh"
packet = struct.pack(layout, b"QZ", 2, 300)
print(packet.hex())                   # 515a02012c
tag, flags, temperature = struct.unpack(layout, packet)
print(bool(flags & 0b001), bool(flags & 0b010), temperature)   # False True 300
print(struct.pack(layout, b"QZX", 2, 300)[:2])                 # b'QZ'

# 3
def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if not unicodedata.combining(c)
    )

words = ["maçã", "manga", "melancia", "mamão", "melão"]
print(sorted(words))                       # ['mamão', 'manga', 'maçã', 'melancia', 'melão']
print(sorted(words, key=strip_accents))    # ['maçã', 'mamão', 'manga', 'melancia', 'melão']
