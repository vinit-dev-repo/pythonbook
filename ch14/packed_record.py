# packed_record.py
import struct
from pathlib import Path
from tempfile import TemporaryDirectory

layout = ">2sBh"
packet = struct.pack(layout, b"QZ", 5, -12)
print(struct.calcsize(layout), packet.hex())
with TemporaryDirectory() as folder:
    path = Path(folder) / "reading.bin"
    path.write_bytes(packet)
    tag, flags, temperature = struct.unpack(layout, path.read_bytes())
print(tag, flags, temperature)
print("Ready:", bool(flags & 0b001))
print("Warning:", bool(flags & 0b010))
try:
    struct.unpack(layout, packet[:-1])
except struct.error:
    print("Incomplete record rejected")
try:
    struct.pack(layout, b"QZ", 256, -12)
except struct.error:
    print("Flag byte out of range")
