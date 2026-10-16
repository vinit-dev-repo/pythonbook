import unicodedata

for character in ("5", "٥", "³", "¼"):
    print(ascii(character), character.isdecimal(), character.isdigit(),
          character.isnumeric(), unicodedata.numeric(character))

try:
    int("³")
except ValueError:
    print("superscript is not an integer input")
