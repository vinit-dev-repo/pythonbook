# binary_operations.py
raw = b"red|blue"
print(raw.find(b"|"), raw.split(b"|"))
print(raw.replace(b"red", b"gold"), raw)
print(b"%b:%03d" % (b"port", 7))
try:
    raw.replace("red", "gold")
except TypeError:
    print("Replacement needs binary arguments")
buf = bytearray(b"ab")
buf.append(99)
buf.extend(b"de")
changed = buf.replace(b"ab", b"XY")
print(buf, changed)
buf[1:3] = b"!"
print(buf)
