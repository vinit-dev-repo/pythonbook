import locale

names = ["Zora", "Émile", "Ana"]
previous = locale.setlocale(locale.LC_COLLATE)
try:
    locale.setlocale(locale.LC_COLLATE, "C")
    print(sorted(names, key=locale.strxfrm))
finally:
    locale.setlocale(locale.LC_COLLATE, previous)
print(locale.setlocale(locale.LC_COLLATE) == previous)
