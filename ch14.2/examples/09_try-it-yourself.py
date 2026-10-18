# 1
place = "Zürich"
print(place.encode("ascii", errors="replace"))             # b'Z?rich'
print(place.encode("ascii", errors="ignore"))              # b'Zrich'
print(place.encode("ascii", errors="xmlcharrefreplace"))   # b'Z&#252;rich'

# 2
octets = b"Montr\xe9al"
print(octets.decode("cp1252"))   # Montréal
try:
    octets.decode("utf-8")
except UnicodeDecodeError as error:
    print(error)   # 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte

# 3
raw = b"caf\xe9"
text = raw.decode("utf-8", errors="surrogateescape")
print(ascii(text))                                            # 'caf\udce9'
print(text.encode("utf-8", errors="surrogateescape") == raw)  # True
