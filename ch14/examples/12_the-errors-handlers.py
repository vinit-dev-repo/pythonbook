raw = b"caf\xe9"  # not a valid byte sequence on its own in UTF-8
text = raw.decode("utf-8", errors="surrogateescape")
print(ascii(text))

back = text.encode("utf-8", errors="surrogateescape")
print(back == raw)
