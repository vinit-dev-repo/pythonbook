import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "cafe.txt"

    # 1
    with open(path, "w", encoding="utf-8") as file:
        print(file.write("café"))        # 4
    with open(path, encoding="utf-8") as file:
        print(file.read())               # café
    with open(path, encoding="cp1252") as file:
        print(file.read())               # cafÃ©

    # 2
    with open(path, "w", encoding="utf-8", newline="") as file:
        file.write("east\nwest\n")
    print(path.read_bytes())             # b'east\nwest\n'

    # 3
    with open(path, "w", encoding="utf-8-sig") as file:
        file.write("café")
    print(path.read_bytes())             # b'\xef\xbb\xbfcaf\xc3\xa9'
    with open(path, encoding="utf-8") as file:
        print(ascii(file.read()))        # '\ufeffcaf\xe9'
    with open(path, encoding="utf-8-sig") as file:
        print(ascii(file.read()))        # 'caf\xe9'

# 4
text = "A\U0001f680"
print(len(text.encode("utf-16-be")))    # 6
print(text.encode("utf-16-be").hex())   # 0041d83dde80
