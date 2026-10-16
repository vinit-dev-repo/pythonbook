custom = chr(0xE000)
print(hex(ord(custom)), len(custom))

accented = "e" + "\u0301"
print(accented, len(accented))

coder = "\U0001F469\u200d\U0001F4BB"
print(coder, len(coder))
