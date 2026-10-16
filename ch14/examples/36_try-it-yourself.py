# 1
city = "München"
data = city.encode("utf-8")
print(data)
print(len(city), len(data))

# 2
place = "Zürich"
print(place.encode("ascii", errors="replace"))

# 3
import unicodedata
s1 = "e" + chr(0x0301)
s2 = "é"
print(s1 == s2)
print(unicodedata.normalize("NFC", s1) == unicodedata.normalize("NFC", s2))

# 4
a = "STRASSE"
b = "straße"
print(a == b)
print(a.casefold() == b.casefold())

# 5
def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if not unicodedata.combining(c)
    )

words = ["maçã", "manga", "melancia", "mamão", "melão"]
print(sorted(words))
print(sorted(words, key=strip_accents))
