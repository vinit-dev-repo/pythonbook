import unicodedata

def catalogue_alias(original):
    punctuation = str.maketrans({"—": "-", "’": "'", "\u00a0": " "})
    expanded = unicodedata.normalize("NFD", original.translate(punctuation))
    kept = []
    ascii_base = False
    for character in expanded:
        if unicodedata.combining(character):
            if not ascii_base:
                kept.append(character)
        else:
            ascii_base = ("A" <= character <= "Z" or "a" <= character <= "z")
            kept.append(character)
    alias = unicodedata.normalize("NFC", "".join(kept))
    return {"original": original, "alias": alias, "changed": alias != original}

record = catalogue_alias("Résumé — 東京")
print(record["original"])
print(record["alias"])
print(record["changed"])
print(record["alias"].isascii())
print(catalogue_alias("Ζέφυρος")["alias"])
