import chardet

original = "name=Rin\n"
raw = original.encode("utf-8")
guess = chardet.detect(raw)
print(guess["encoding"])
print(guess["confidence"])
print(raw.decode("ascii") == raw.decode("utf-8") == raw.decode("latin-1"))
