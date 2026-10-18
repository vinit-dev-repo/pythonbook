import re
from unicodedata import normalize

# 1
s1 = "e" + chr(0x0301)
s2 = "é"
print(s1 == s2)                                        # False
print(normalize("NFC", s1) == normalize("NFC", s2))    # True

# 2
a = "STRASSE"
b = "straße"
print(a == b)                                  # False
print(a.casefold() == b.casefold())            # True

# 3
print("³".isdigit())                           # True
try:
    int("³")
except ValueError:
    print("ValueError")
print("٥".isdecimal(), int("٥"))               # True 5

# 4
print([f"U+{ord(c):04X}" for c in normalize("NFKC", "½")])   # ['U+0031', 'U+2044', 'U+0032']

def canonical_caseless_key(text):
    folded = normalize("NFD", text).casefold()
    return normalize("NFD", folded)

def text_equal(first, second):
    return canonical_caseless_key(first) == canonical_caseless_key(second)

print(text_equal("café", "cafe" + chr(0x0301)))   # True
print(text_equal("café", "cafe"))                 # False

# 5
print(re.findall(r"\w+", "café"))                 # ['café']
print(re.findall(rb"\w+", "café".encode("utf-8")))   # [b'caf']
