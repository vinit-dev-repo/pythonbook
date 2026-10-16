with open("positions.bin", "wb") as file:
    file.write(b"abcdef")

with open("positions.bin", "r+b") as file:
    file.seek(2)
    print("bytes written:", file.write(b"XY"))
    file.flush()
    with open("positions.bin", "rb") as reader:
        print("another reader:", reader.read())
    file.seek(-2, 2)
    print("last two bytes:", file.read())
    print("byte position:", file.tell())
