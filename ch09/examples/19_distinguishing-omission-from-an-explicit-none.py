MISSING = sentinel("MISSING")

def choose_colour(colour=MISSING):
    if colour is MISSING:
        return "blue"
    if colour is None:
        return "no colour"
    return colour

print(choose_colour(), choose_colour(None), choose_colour("red"))
print(MISSING)
print(sentinel("MISSING") is MISSING)
