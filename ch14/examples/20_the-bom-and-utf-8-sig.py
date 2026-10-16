text = "café"

with open("bom_test.txt", "w", encoding="utf-8-sig") as f:
    f.write(text)

with open("bom_test.txt", "rb") as f:
    raw = f.read()
print(raw)

with open("bom_test.txt", encoding="utf-8") as f:
    plain = f.read()
print(ascii(plain))

with open("bom_test.txt", encoding="utf-8-sig") as f:
    clean = f.read()
print(ascii(clean))
