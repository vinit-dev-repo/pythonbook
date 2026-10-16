name, rest = "state::working::retry".split("::", 1)
print(name)
print(rest)
for text in ("done\n", "done"):
    print(repr(text.removesuffix("\n")), repr(text[:-1]))
