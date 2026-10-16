names = ["Ben", "Amy", "Ben", "Cara", "Amy"]

deduped_unordered = set(names)
deduped_ordered = list(dict.fromkeys(names))

print(sorted(deduped_unordered))   # sorted() so this Output is stable to print here — the SET itself still has no order
print(deduped_ordered)
