from unicodedata import normalize

combining_acute = chr(0x0301)

def canonical_caseless_key(text):
    decomposed = normalize("NFD", text)
    folded = decomposed.casefold()
    return normalize("NFD", folded)

def text_equal(a, b):
    return canonical_caseless_key(a) == canonical_caseless_key(b)

print(text_equal("café", "cafe" + combining_acute))
print(text_equal("Straße", "STRASSE"))

# U+0390 and U+03AA U+0301 are canonically caseless-equal.
greek_a = chr(0x0390)
greek_b = chr(0x03AA) + chr(0x0301)
print(text_equal(greek_a, greek_b))
