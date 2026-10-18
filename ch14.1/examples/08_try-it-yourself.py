# 1
city = "München"
data = city.encode("utf-8")
print(data)                   # b'M\xc3\xbcnchen'
print(len(city), len(data))   # 7 8

# 2
print(bytes(2))      # b'\x00\x00'
print(bytes([2]))    # b'\x02'

# 3
text = "cafe" + chr(0x0301)
print(ascii(text))                      # 'cafe\u0301'
print(len(text), len(text.encode("utf-8")))   # 5 6

# 4
buf = bytearray(b"hello")
buf[0] = ord("J")
print(buf)                              # bytearray(b'Jello')
try:
    b"hello"[0] = ord("J")
except TypeError as error:
    print("TypeError:", error)          # TypeError: 'bytes' object does not support item assignment
