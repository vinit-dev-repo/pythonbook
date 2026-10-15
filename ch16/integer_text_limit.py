# integer_text_limit.py
large = 2 ** 20_000
print("value bits:", large.bit_length())
print("hex round trip:", int(hex(large), 16) == large)
try:
    text = str(large)
except ValueError:
    print("decimal conversion exceeds the configured limit")
else:
    print("decimal digits:", len(text))
