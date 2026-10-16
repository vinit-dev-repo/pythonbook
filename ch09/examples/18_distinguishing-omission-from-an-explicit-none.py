_MISSING = object()

def choose_colour(colour=_MISSING):
    if colour is _MISSING:
        return "blue"
    if colour is None:
        return "no colour"
    return colour

print(choose_colour())
print(choose_colour(None))
print(choose_colour("red"))
