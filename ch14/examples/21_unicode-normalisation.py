combining_acute = chr(0x0301)

s1 = "café"                    # the accented "e" as one code point
s2 = "cafe" + combining_acute  # a plain "e" plus a separate accent mark

print(s1, s2)
print(s1 == s2)
print(len(s1), len(s2))

from unicodedata import normalize

print(len(normalize("NFC", s1)), len(normalize("NFC", s2)))
print(normalize("NFC", s1) == normalize("NFC", s2))
