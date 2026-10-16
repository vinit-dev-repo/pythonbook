for line in ("ready\n", "ready"):
    print(repr(line.removesuffix("\n")), repr(line[:-1]))
print(repr("ready  \n".rstrip()))
print("report.txt".removesuffix(".txt"))
print("report.txt".rstrip(".txt"))
