data = b"caf\xc3\xa9"
print(ascii(data.decode("utf-8")))
print(ascii(data.decode("latin-1")))
