octets = b"Montr\xe9al"
print(octets.decode("cp1252"))
print(octets.decode("iso8859-7"))

try:
    octets.decode("utf-8")
except UnicodeDecodeError as e:
    print(e)

print(octets.decode("utf-8", errors="replace"))
