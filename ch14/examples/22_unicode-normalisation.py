print(ascii(normalize("NFC", "q" + chr(0x0301))))
for form in ("NFKC", "NFKD"):
    fraction = normalize(form, "½")
    print(form, [f"U+{ord(c):04X}" for c in fraction], fraction == "1/2")
