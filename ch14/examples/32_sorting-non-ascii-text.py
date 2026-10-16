import unicodedata

def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if not unicodedata.combining(c)
    )

fruits = ["caju", "atemoia", "cajá", "açaí", "acerola"]
print(sorted(fruits, key=strip_accents))
