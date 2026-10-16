Path("source.txt").write_text("hello\nworld\n")

with open("source.txt") as infile:
    with open("upper.txt", "w") as outfile:
        for line in infile:
            outfile.write(line.upper())

print(Path("upper.txt").read_text())
