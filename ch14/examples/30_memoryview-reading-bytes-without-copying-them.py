import struct

data = bytes([0x02, 0x00, 0xe6, 0x00])  # two little-endian 16-bit numbers
view = memoryview(data)
width, height = struct.unpack("<HH", view)
print(width, height)
