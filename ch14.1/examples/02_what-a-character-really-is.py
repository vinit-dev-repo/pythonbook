decomposed = "cafe" + chr(0x0301)
print(ascii(decomposed))
print(len(decomposed), len(decomposed.encode("utf-8")))
