from string.templatelib import Interpolation

name = "World"

for part in t"Hello {name}!":
    if isinstance(part, str):
        print("literal      :", repr(part))
    else:
        print("interpolation:", repr(part.value), "from expression", repr(part.expression))
