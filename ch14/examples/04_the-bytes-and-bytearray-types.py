data = b"hello"
print(data)
print(type(data))

buf = bytearray(b"hello")
print(buf)
buf[0] = ord("H")
print(buf)
