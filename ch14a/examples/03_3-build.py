from unicodedata import normalize

def canonical_caseless_key(text):
    return normalize("NFD", normalize("NFD", text).casefold())

def word_report(text):
    words = text.replace(".", " ").replace(",", " ").split()
    counts = {}
    for word in words:
        key = canonical_caseless_key(word)
        counts[key] = counts.get(key, 0) + 1
    return {
        "count": len(words),
        "longest": max(words, key=len) if words else None,
        "frequencies": {key: count for key, count in sorted(counts.items())},
    }

r = word_report("The cat sat. The cat, again.")
print(r["count"], r["longest"])
print(r["frequencies"])
print(word_report("")["longest"])
print(word_report("Straße STRASSE")["frequencies"])
