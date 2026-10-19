with (
    open("source.txt") as infile,
    open("upper.txt", "w") as outfile,
):
    for line in infile:
        outfile.write(line.upper())

print(Path("upper.txt").read_text())
