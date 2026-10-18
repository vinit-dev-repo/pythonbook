from pyuca import Collator

collator = Collator()
names = ["Zora", "Émile", "Ana"]
print(collator.UCA_VERSION)
print(sorted(names, key=collator.sort_key))
print(collator.sort_key("é") == collator.sort_key("e\u0301"))
