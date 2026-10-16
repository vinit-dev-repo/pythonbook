print("|{value:{width}.{places}f}|".format(value=6.5, width=8, places=3))
print("{0!s} | {0!r} | {0!a}".format("café"))
formatter = "{:04d}".format
print(list(map(formatter, [6, 18])))
