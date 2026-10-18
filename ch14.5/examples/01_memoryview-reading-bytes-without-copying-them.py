data = bytearray(b"hello world")
view = memoryview(data)

chunk = view[0:5]
print(bytes(chunk))

chunk[0] = ord("H")
print(data)
