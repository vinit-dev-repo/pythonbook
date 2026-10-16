text = "Qé\n"
codes = []
total = 0
for character in text:
    code = ord(character)
    codes.append(code)
    total += code
print(codes, total)
print([ord(character) for character in text])
print(sum(codes))
print("bell representation:", repr("\a"), "code:", ord("\a"))
